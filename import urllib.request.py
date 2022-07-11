from urllib import request
file1=[]
url = 'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
request.urlretrieve(url, "/Users/imac/Downloads/icon333.txt")

with open("/Users/imac/Downloads/icon333.txt", "r") as file1:
    i=0
    for i in (1,len(file1.readlines())):
        line=file1.readline()
        print ("line  ", i, "  ",line )
    i=i+1
print ("end")

###########################################
from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")