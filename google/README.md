# Google Cloud

```
sa_key.json AND service_account AND project_id language:JSON
```
![image](https://github.com/user-attachments/assets/2f184849-5ece-48dc-b5c3-a3785414ee4c)

```
gcloud auth activate-service-account --key-file=<path-to-your-token-file>
```
Google Cloud Services
```
*. storage.googleapis.com
*. cloudfunctions.net
*. appspot.com
```

Google IMDS
```
curl -H "Metadata-Flavor:Google" http://169.254.169.254/computeMetadata/v1/instance/service-accounts/
```
![image](https://github.com/user-attachments/assets/79e30468-9c86-4e79-8e3d-8b098f4b60c7)

```
curl -H "Authorization: Bearer <YOUR_BEARER_TOKEN>" https://cloudresourcemanager.googleapis.com/v1/projects
curl -H "Authorization: Bearer <YOUR_BEARER_TOKEN>" "https://www.googleapis.com/compute/v1/projects/YOUR_PROJECT_ID/zones"
curl -H "Authorization: Bearer <YOUR_BEARER_TOKEN>" https://www.googleapis.com/compute/v1/projects/YOUR_PROJECT_ID/zones/YOUR_ZONE/instances
```
