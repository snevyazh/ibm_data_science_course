# import requests
# import sys
# url='http://httpbin.org/get'
# payload={'name':'Joseph', 'ID': '123' }
# r = requests.get(url, params=payload)
# # print(r.url)
# # print('headers', r.headers)
# # print('text' , r.text)
# r.json()
# print(r.json()['args'])

import os 
import requests
from PIL import Image
from IPython.display import IFrame
# url='https://www.ibm.com/'
# r=requests.get(url)
# r.status_code
# print(r.request.headers)
# print("request body:", r.request.body)
# header=r.headers
# print(r.headers)
# header['date']
# header['Content-Type']
# r.encoding
# r.text[0:100]


# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
r.headers['Content-Type']
path=os.path.join('/Users/imac/Downloads/','image.png')
print(path)
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)  



