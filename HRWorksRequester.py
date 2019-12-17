import hashlib
import hmac
import datetime
import requests
import urllib

class HRWorksRequester():

    # These are the example keys from the documentation
    ACCESS_KEY = "kdVDiLrylwri8+oLffNi"
    SECRET_ACCESS_KEY = "T8IEuI/BGWVXYEYrPJVzU9W9B1x2o2vov0SdihAv"
    HOST = "api.hrworks.de"

    def getCanon(self, target, payload):
        date = self.getDate()
        verb = "POST"
        uri = "/"
        content = "content-type:application/json"
        host = "host:" + self.HOST
        targetString = "x-hrworks-target:" + target
        hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()

        result = [verb, uri + "\n", content, "date:" + date, host, targetString + "\n", hash]
        resultstring = "\n".join(result)
        #print("Canon: \n" + resultstring)
        return resultstring
    
    def getSignString(self,target, payload):
        canon= self.getCanon(target, payload)
        head = "HRWORKS-HMAC-SHA256"
        hash =  hashlib.sha256(canon.encode('utf-8')).hexdigest()
        result = [head+"\n", self.getDate()+"\n", hash]
        resultstring = "".join(result)
        #print("Sign string: \n" + resultstring)
        return resultstring

    def getSigniture(self,target, payload):
        date = self.getDate()[:8]
        key = "HRWORKS" + self.SECRET_ACCESS_KEY
        requestDate = hmac.new(bytes(key, 'latin-1'), msg=bytes(date, 'latin-1'), digestmod = hashlib.sha256).digest();
        realmID = hmac.new(requestDate , msg=bytes("production", 'latin-1'), digestmod = hashlib.sha256).digest()
        closingString = hmac.new(realmID, msg = bytes("hrworks_api_request", 'latin-1'), digestmod = hashlib.sha256).digest()
        signString = hmac.new(closingString, msg = bytes(self.getSignString(target, payload), 'latin-1'), digestmod = hashlib.sha256).hexdigest()
        #print("Signiture: " + signString)        
        return signString
    
    def getDate(self):
        date = datetime.datetime.now().isoformat()
        datestring = date.replace("-","").replace(":", "").replace(".","")+ "Z"
        #datestring =  "20180619T130601Z"
        return datestring
    
    def getAuthHeader(self, target, payload):
        parsedAccessKey  = urllib.parse.quote_plus(self.ACCESS_KEY)
        authorisation = "HRWORKS-HMAC-SHA256" + " Credential=" + parsedAccessKey + "/production, "
        signedHeader = "SignedHeaders=content-type;date;host;x-hrworks-target, "
        signiture = "Signature="+ self.getSigniture(target, payload)
        result = "".join([authorisation, signedHeader, signiture])
        #print("AuthHeader: " + result)
        return result
    
    def request(self, target, payload=""):
        authHead = self.getAuthHeader(target, payload)
        headers = {"Host": hr.HOST, "Date":hr.getDate(), "Authorization":authHead, 'Accept': 'application/json', "Content-Type":"application/json", "x-hrworks-target":t }
        r = requests.post('http://' + self.HOST, data = p, headers=headers)
        return r
