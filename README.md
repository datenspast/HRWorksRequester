# HRWorksRequester
Python3 implementation for HRWorks (HR Works) API requests. 

Based on https://www.hrworks.de/public/HRworks_API_Reference.pdf (v1.0)

## Preparation

Replace the access keys with your credentials, e.g. these are from the documentation
```
ACCESS_KEY = "kdVDiLrylwri8+oLffNi"
SECRET_ACCESS_KEY = "T8IEuI/BGWVXYEYrPJVzU9W9B1x2o2vov0SdihAv"
```
## Usage

Example:
```
hr = HRWorksRequester()
target = "GetAllAbsenceTypes"
payload ='{"onlyActive":false}'
r=hr.request(target, payload)
print(r.text)
```

