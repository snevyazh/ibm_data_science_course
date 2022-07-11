import requests
from bs4 import BeautifulSoup

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
with open('/Users/imac/Downloads/test.html', 'w') as temp_file:
    temp_file.write(table)

with open ('/Users/imac/Downloads/test.html', 'r') as html:  
    a = BeautifulSoup (html, 'html.parser')
    #print(a)
rows = a.find_all(name='tr')
for i, row in enumerate(rows):
    print('row ', i)
    cells = row.find_all(name = 'td')
    for j, cell in enumerate(cells):
        print("column ", j, "cell", cell)
