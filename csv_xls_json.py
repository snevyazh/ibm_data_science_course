import pandas as pd
file = '/Users/imac/Downloads/test_file.csv'

df = pd.read_csv(file)
# df.loc[-1] = ['___', '___', '___']  # adding a row
# df.index = df.index + 1  # shifting index
# df.sort_index(inplace=True) 

print(df)
print('\n')
df.columns = ['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)


# it reads csv whith 1 row as column names and .columns just replace it


#select first row
df.loc[0] 
