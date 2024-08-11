import requests
import time
import argparse
from datetime import datetime, timedelta

SEARCH_TERMS = [
    'aws_access_key_id=', 'aws_bucket aws_key=', 'aws_secret=', 'aws_secret_key=',
    'aws_token=', 'aws_session_token=', 'bucket_password', 'bucketeer_aws_access_key_id', 
    'bucketeer_aws_secret_access_key', 'cache_s3_secret_key', 'cloud_watch_aws_access_key', 
    'cloudwatch_aws_access_key', 'aws_access_key_id=', 'lottie_s3_api_key', 
    'lottie_s3_secret_key', 's3_access_key=', 's3_access_key_id=', 's3_key s3_key_app_logs', 
    's3_key_assets', 's3_secret_key=', 'sandbox_aws_access_key_id', 'sandbox_aws_secret_access_key', 
    'secret_key aws', 'secretkey aws'
]
API_URL = 'https://api.github.com/search/code'
REPO_API_URL = 'https://api.github.com/repos/'

def search_github_code(term, seen_urls, output_file, token, days):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    params = {
        'q': term,
        'per_page': 100,
        'page': 1
    }

    cutoff_date = datetime.now() - timedelta(days=days)

    while True:
        response = requests.get(API_URL, headers=headers, params=params)
        
        if response.status_code == 403:
            if 'X-RateLimit-Remaining' in response.headers:
                remaining = int(response.headers['X-RateLimit-Remaining'])
                if remaining == 0:
                    reset_time = int(response.headers['X-RateLimit-Reset'])
                    wait_time = reset_time - time.time() + 5
                    if wait_time > 0:
                        print(f'Rate limit exceeded. Waiting for {wait_time:.2f} seconds before retrying.')
                        time.sleep(wait_time)
                        continue
            print(f'Error: {response.status_code} - {response.json()}')
            break

        if response.status_code == 200:
            result = response.json()
            items = result.get('items', [])
            if not items:
                break
            for item in items:
                repo_url = item["repository"]["html_url"]
                repo_owner = item["repository"]["owner"]["login"]
                if repo_owner != 'reewardius' and repo_url not in seen_urls:
                    seen_urls.add(repo_url)

                    # Check the last commit date
                    repo_name = item["repository"]["full_name"]
                    commits_url = f'{REPO_API_URL}{repo_name}/commits'
                    commits_response = requests.get(commits_url, headers=headers)
                    if commits_response.status_code == 200:
                        commits = commits_response.json()
                        if commits:
                            last_commit_date = datetime.strptime(commits[0]['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
                            if last_commit_date >= cutoff_date:
                                with open(output_file, 'a') as file:
                                    file.write(f'{repo_url} [{term}]\n')
            params['page'] += 1
        else:
            print(f'Error: {response.status_code} - {response.json()}')
            break
        
        time.sleep(2)

def main():
    parser = argparse.ArgumentParser(description='Search GitHub repositories by terms.')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='File to save the list of repository URLs')
    parser.add_argument('-t', '--token', type=str, required=True, help='GitHub token for authentication')
    parser.add_argument('-day', type=int, required=True, help='Number of days to filter repositories (1-30).')
    args = parser.parse_args()

    if not (1 <= args.day <= 30):
        print("Error: The number of days must be between 1 and 30.")
        return

    seen_urls = set()
    for term in SEARCH_TERMS:
        print(f'Searching for term: {term}')
        search_github_code(term, seen_urls, args.output, args.token, args.day)
        print(f'Finished searching for term: {term}')

if __name__ == '__main__':
    main()
