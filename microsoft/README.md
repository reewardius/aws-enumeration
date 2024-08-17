# Microsoft

![image](https://github.com/user-attachments/assets/74dfe795-fb56-4090-9223-9e0b163540e9)

Microsoft Cloud Services
```
*.azurewebsites.net
*.cloudapp.net
*.blob.core.windows.net
*.database.windows.net
```
Azure IMDS
```
curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' -H Metadata:true
```
![image](https://github.com/user-attachments/assets/60bb0912-fe8a-4952-ac24-7740761da71f)

Kubenv
```
env && printenv
set
```
![image](https://github.com/user-attachments/assets/30a3773d-f65e-46c8-8535-53880094e632)

Azure Resource
```
$accessToken = ''
$accountId = ''
Connect-AzAccount -AccessToken $accessToken -AccountId $accountId

Get-AzResource
```
![image](https://github.com/user-attachments/assets/366b10b1-6d66-4219-9517-eb8e52c6d0c5)
