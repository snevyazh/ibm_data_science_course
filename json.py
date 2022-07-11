#### converts JSON string into dictionary

import json 
    
# JSON string: 
# Multi-line string 
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""
    
# parse data: 
res = json.loads( data ) 
    
# the result is a Python dictionary: 
print( res )


#
#json.load() takes a file object and returns the json object. 
# It is used to read JSON encoded data from a file and convert it into a Python dictionary 
# and deserialize a file itself i.e. it accepts a file object.


##create json file first , data is a dictionary  
data = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
#then we create a file
with open( "data_file.json" , "w" ) as write:
    json.dump( data , write )

# we convert file into dictionary :-)
with open("data_file.json", "r") as read_content:
    print(json.load(read_content))

