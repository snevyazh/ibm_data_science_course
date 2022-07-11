from urllib import request
# file1=[]
# url = 'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# request.urlretrieve(url, "/Users/imac/Downloads/icon333.txt")

#with open("/Users/imac/Downloads/icon333.txt", "r") as file1:
 #   i=0
    #line=()
  #  A=len(file1.readlines())
   # print("A = ",A)
   # for i in range (1,A+1):
    #    line=file1.readline()
     #   print ("line  ", i, "  ",line )




# with open("/Users/imac/Downloads/icon333.txt", "r") as file1:
#     z = 0
#     for line in file1:
#         print("Iteration", str(z), ": ", line)
#         z = z + 1

# with open("/Users/imac/Downloads/icon333.txt", "r") as file1:
#     B=int(input("enter number  "))
#     C=B-1
#     A=file1.readlines()
    
#     print("line ", B, "  ",A[C])
        
# with open ("/Users/imac/Downloads/new.txt", 'w') as file1:
#     i=0
#     for i in range (1, 11):
#         file1.write(str(i)+"-th line\n")
# print ("end of cycle 1")

# with open ("/Users/imac/Downloads/new.txt", "r") as file2:
#     i=0
#     for i in range (1, 11):
#         line=file2.readline()
#         print("Line ", i, line)
# print ("end")

# with open("/Users/imac/Downloads/new.txt", "r") as fileread:
#     with open("/Users/imac/Downloads/new1.txt", "w") as filewrite:
#         for line in fileread:
#             filewrite.write(line)
       
   

# with open("/Users/imac/Downloads/new1.txt", "r") as file1:
#     i=0
#     for i in file1:
#         content=file1.readline()
#         print(content)

# 
#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee =('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    with open(old,'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))


genFiles(memReg,exReg)

import os
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
    with open (currentMem, "r+") as current:
        with open(exMem, "a+") as ex:          
            for line in current:
                if "no" in line.strip("/n"):
                    ex.write(line)
                 
    with open("temp.txt" , "w") as tempfile:                   
        with open(currentMem, "r+") as current1:
            for line1 in current1:
                if "no" not in line1.strip("/n"):
                    tempfile.write(line1)

    os.replace ("temp.txt","members.txt")
                
cleanFiles(memReg,exReg)


          

