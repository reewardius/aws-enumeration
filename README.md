# AWS Enumeration
We utilize various search engines to conduct OSINT and gather information about leaked AWS Access & Secret Keys, as well as AWS S3 Bucket names that have been cached by crawlers.
# Javascript Files
Analyzing Javascript files for AWS Access/Secret key Disclosure & S3 Buckets
```
getjs --input targets.txt --complete --output js_links.txt
nuclei -l js_links.txt -t templates/aws-access-secret-key.yaml -silent -o aws-secrets.txt
```
![image](https://github.com/user-attachments/assets/c0b58523-c277-439e-b4fa-e7d2e541a659)
```
nuclei -l js_links.txt -t templates/s3-bucket-detect.yaml -silent -o aws-s3-buckets.txt
```
![image](https://github.com/user-attachments/assets/874ca92f-94d0-42e3-9367-0f66a8613675)


# Google Dorks
![image](https://github.com/user-attachments/assets/23a943cf-3451-49b8-a6d0-8d9ed72c5b05)

The below google dorks can be used to extract the information related with AWS S3:
```
site:s3.amazonaws.com "index of /"
inurl:s3.amazonaws.com intitle:"AWS S3 Explorer"
site:http://s3.amazonaws.com intitle:index.of.bucket ""
site:.s3.amazonaws.com "Company"
inurl:gitlab "AWS_SECRET_KEY" "
inurl:pastebin "AWS_ACCESS_KEY"
```
# Github Dorks
![image](https://github.com/user-attachments/assets/9ad909e9-2c52-48ff-a5f7-8917e2e9521c)
```
rds.amazonaws.com password
aws_access_key_id=
aws_bucket aws_key=
aws_secret=
aws_secret_access_key=
aws_secret_key=
aws_session_token=
aws_token=
bucketeer_aws_access_key_id
bucketeer_aws_secret_access_key
cache_s3_secret_key
lottie_s3_api_key
lottie_s3_secret_key
s3_access_key=
s3_access_key_id=
s3_secret_key=
sandbox_aws_access_key_id
sandbox_aws_secret_access_key
secret_key aws
aws_secretaccesskey=
secretkey aws
```
The process of searching manually for each keyword can be automated using **githubDorker** as shown below:
```
python github-aws-secrets-scanner.py -t <github-token> -day 7 -o results.txt
```
![image](https://github.com/user-attachments/assets/5e04a139-f9c3-4f4a-bb17-6d950c649056)
# grep.app
```
aws_access_key_id\s*=\s*['"]?AKIA[0-9A-Z]{16}['"]?
aws_secret_access_key="[A-Za-z0-9+/=]{40}"
AKIA[0-9A-Z]{16}
```
![image](https://github.com/user-attachments/assets/8db9fd1a-f5c4-4eb8-870d-4f058f8ffc05)

# Shodan Query
According to Shodan, the data displayed are from the past 30 days of monitored data on the internet.
![image](https://github.com/user-attachments/assets/2da48880-8619-4c88-93d7-7cf088400988)
```
html:"AWS_ACCESS_KEY_ID"
html:"AWS_SECRET_ACCESS_KEY"
html:"AWS_SESSION_TOKEN"
html:"ListBucketResult"
```
# Censys Query
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
```
![image](https://github.com/user-attachments/assets/b597f5fb-703b-44e7-af72-7509a26806f2)

![image](https://github.com/user-attachments/assets/7a44bd00-6a3f-4b8f-acad-76f3054bccba)

# Fofa Query
![image](https://github.com/user-attachments/assets/726c3616-3b20-4200-9fe7-ddb38890edd6)
```
body="AWS_ACCESS_KEY_ID"
body="AWS_SECRET_ACCESS_KEY"
body="AWS_SESSION_TOKEN"
app="amazon-AmazonS3"
body="ListBucketResult"
```
# Using Uncover with Nuclei
```
uncover -q 'html:"ListBucketResult"' -pc config.yaml -silent | httpx -silent | nuclei -id aws-object-listing -silent
```
![image](https://github.com/user-attachments/assets/1c42d75d-aea8-449d-b6fb-86993edd884b)
```
uncover -q 'html:"AWS_ACCESS_KEY_ID"' -pc config.yaml -silent -o uncover.txt
nuclei -l uncover.txt -t templates/aws-access-secret-key.yaml
```
![image](https://github.com/user-attachments/assets/a0a33f95-1a4b-4eb8-a497-8cd328b0770e)

# Detecting AWS Website
```
nuclei -l targets.txt -id s3-detect
```
![image](https://github.com/user-attachments/assets/4a22b2ad-9629-4581-8b5e-593433a3439a)

# Using Nuclei / Cloud-Enum / S3Scanner for S3 Bucket Enum
```
nuclei -id aws-s3-bucket-enum -var wordlist=fuzz.txt -rl 1 -lfa
```
![image](https://github.com/user-attachments/assets/3b7b4a5a-1d3c-484e-9b6c-85aa214fbd93)
```
python cloud_enum.py -k keyword -k keyword2
python cloud_enum.py -kf fuzz.txt -qs
```
![image](https://github.com/user-attachments/assets/e981894c-b42e-4328-b4fa-33f44a6fba6a)
```
s3scanner -bucket-file fuzz.txt -provider aws -enumerate
```
![image](https://github.com/user-attachments/assets/4d5bfc7b-16de-40d1-8e1b-efdd060a6286)
# Grayhatwarfare
GrayhatWarfare allows users to find open AWS S3 buckets.
![image](https://github.com/user-attachments/assets/a2f65204-07ac-46c5-8bda-78bf845abb66)



