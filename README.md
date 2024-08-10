# AWS Enumeration
We utilize various search engines to conduct OSINT and gather information about leaked AWS Access & Secret Keys, as well as AWS S3 Bucket names that have been cached by crawlers.
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
s3_access_key
Key:amazon_secret_access_key
amazonaws
aws_access
aws_access_key_id
aws_bucket aws_key
aws_secret
aws_secret_key
aws_token
bucket_password
bucketeer_aws_access_key_id
bucketeer_aws_secret_access_key
cache_s3_secret_key
cloud_watch_aws_access_key
filename:credentials
aws_access_key_id
filename:s3cfg
lottie_s3_api_key
lottie_s3_secret_key
s3_access_key
s3_access_key_id
s3_key s3_key_app_logs
s3_key_assets
s3_secret_key
sandbox_aws_access_key_id
sandbox_aws_secret_access_key
secret_key aws
secretkey aws
filename:.bash_profile
aws filename:.s3cfg
```
# Shodan Query
According to Shodan, the data displayed are from the past 30 days of monitored data on the internet.
![image](https://github.com/user-attachments/assets/2da48880-8619-4c88-93d7-7cf088400988)
```
html:"AWS_ACCESS_KEY_ID"
html:"AWS_SECRET_ACCESS_KEY"
html:"AWS_SESSION_TOKEN"
html:"istBucketResult"
title:"AWS S3 Explorer"
html:"AWS Elastic Beanstalk overview"
html:"OpenSearch Dashboards"
"X-Amz-Server-Side-Encryption"
title:"EC2 Instance Information"
http.title:"Amazon Cognito Developer Authentication Sample"
"Server: EC2ws"
title:"AWS X-Ray Sample Application"
html:"Amazon EC2 Status"
html:"AWS EC2 Auto Scaling Lab"
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
app="amazon-AWS-ELB"
app="amazon-AWS-Elastic-Beanstalk"
app="amazon-AWS-EC2"
app="amazon-AWS-WAF"
app="amazon-ECS"
app="amazon-AmazonS3"
body="ListBucketResult"
```
# Using Uncover with Nuclei
```
uncover -q 'html:"ListBucketResult"' -pc config.yaml -silent | httpx -silent | nuclei -id aws-object-listing -silent
```
![image](https://github.com/user-attachments/assets/1c42d75d-aea8-449d-b6fb-86993edd884b)

# Using Nuclei for S3 Bucket Enumeration
```
nuclei -id aws-s3-bucket-enum -var wordlist=fuzz.txt -vv -rl 1 -lfa
```
![image](https://github.com/user-attachments/assets/3b7b4a5a-1d3c-484e-9b6c-85aa214fbd93)

# Grayhatwarfare
GrayhatWarfare allows users to find open AWS S3 buckets.
![image](https://github.com/user-attachments/assets/a2f65204-07ac-46c5-8bda-78bf845abb66)



