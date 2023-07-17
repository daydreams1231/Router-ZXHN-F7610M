import hashlib
import random
import re
import requests
header = {
    "Cookie": "_TESTCOOKIEHTTP=1",
}
fLogin = requests.get("http://192.168.1.1/")
pattern1 = r'getObj\("Frm_Logintoken"\)\.value = "(.+?)"'
pattern2 = r'getObj\("Frm_Loginchecktoken"\)\.value = "(.+?)"'

formData = {
    "Frm_Logintoken": re.search(pattern1, fLogin.text).group(1),
    "Frm_Loginchecktoken": re.search(pattern2, fLogin.text).group(1),
    "Right": "", 
    "Username": "user",
    "UserRandomNum": str(round(random.random() * 89999999) + 10000000),
    "Password": "",
    "action": "login"
}
data_ = 'tXh7G%cC' + formData['UserRandomNum']
formData['Password'] = hashlib.sha256(data_.encode("utf-8")).hexdigest()
print(formData,'\n')

sess = requests.post("http://192.168.1.1/",data=formData,headers=header,allow_redirects=False)

print(fLogin.headers,'\n\n',sess.headers)
print(fLogin.status_code,' ',sess.status_code)