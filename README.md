# HRWorksRequester
HR Works Requests with python3
Based on https://www.hrworks.de/public/HRworks_API_Reference.pdf 

## Preparation

Replace the access keys with your credentials, e.g. this are the
```
    ACCESS_KEY = "kdVDiLrylwri8+oLffNi"
    SECRET_ACCESS_KEY = "T8IEuI/BGWVXYEYrPJVzU9W9B1x2o2vov0SdihAv"
```
## Usage

Example:
```
hr = HRWorksRequester()
target = "GetAllAbsenceTypes"
payload ='{"onlyAcive":false}'
r=hr.request(target, payload)
print(r.text)
```

