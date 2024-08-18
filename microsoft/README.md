# Microsoft

1. Получение токена доступа с помощью Azure CLI
```
az login --service-principal -u <appid> -p <appSecret> --tenant <tenantID>
```
![image](https://github.com/user-attachments/assets/74dfe795-fb56-4090-9223-9e0b163540e9)

2. Получение токена доступа с помощью curl
```
curl -X POST https://login.microsoftonline.com/<tenantID>/oauth2/v2.0/token -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=<appid>&client_secret=<appSecret>&scope=https://management.azure.com/.default"
```
3. Azure PowerShell
```
$tenantID = "<tenantID>"
$appid = "<appid>"
$appSecret = "<appSecret>"

$secureAppSecret = ConvertTo-SecureString $appSecret -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ($appid, $secureAppSecret)

Connect-AzAccount -ServicePrincipal -Tenant $tenantID -Credential $creds
```
Если вы используете сертификат для аутентификации, то ваша команда выглядит так:
```
$tenantID = "<tenantID>"
$appid = "<appid>"
$certThumbprint = "<certificateThumbprint>"

Connect-AzAccount -ServicePrincipal -Tenant $tenantID -ApplicationId $appid -CertificateThumbprint $certThumbprint
```
![image](https://github.com/user-attachments/assets/6e1a0d73-cc7b-424f-a29a-74b029ffef2d)

```
curl -X GET "http://localhost:8081/msi/token?api-version=2017-09-01&resource=https://management.azure.com" \
-H "secret:$IDENTITY_HEADER"

$accessToken = ''
$accountId = ''
Connect-AzAccount -AccessToken $accessToken -AccountId $accountId

Get-AzResource
```
![image](https://github.com/user-attachments/assets/7a1057fb-c50e-4bd9-a737-2d2d1d83221e)
- https://tripla.dk/2022/03/13/create-an-azure-vulnerable-lab-part-4-managed-identities/

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
