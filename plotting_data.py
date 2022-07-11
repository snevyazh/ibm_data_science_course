import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


URL = 'http://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'

df_can = pd.read_excel(URL, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
print(df_can.head())

#list of column headers
print(df_can.columns)

#set a list out of columns
print('first     ', df_can.columns.tolist())

# delete columns unneeded, in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#rename columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

#add column with total number
df_can['Total'] = df_can.sum(axis=1)

#set a list out of columns
print('last       ', df_can.columns.tolist())


#check NULL objects
print(df_can.isnull().sum())

#stat data of the table
print(df_can.describe())

print(df_can.Country)  # returns a series
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]) # returns a dataframe

# Default index of the dataset is a numeric range from 0 to 194. 
# This makes it very difficult to do a query by a specific country. 
# For example to search for data on Japan, we need to know the corresponding index value.
# This can be fixed very easily by setting the 'Country' column as the index using set_index() method
df_can.set_index('Country', inplace=True)

# 1. the full row data (all columns)
print(df_can.loc['Japan'])

print(df_can[df_can.index == 'Japan'])
# 2. for year 2013
df_can.loc['Japan', 2013]

# alternate method
# year 2013 is the last column, with a positional index of 36
df_can.iloc[87, 36]

# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]

print(df_can.columns == list(map(str, df_can.columns)))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

df_can.index.name = None

# # # useful for plotting later on
years = list(range(1980, 2014))
# # # print(years)

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
# 2. pass this condition into the dataFrame
df_can[condition]

# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

# bar for vertical bar plots
# barh for horizontal bar plots
# hist for histogram
# box for boxplot
# kde or density for density plots
# area for area plots
# pie for pie plots
# scatter for scatter plots
# # hexbin for hexbin plot

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake') # see note below
plt.show() # need this line to show the updates made to the figure

df_can.sort_values(by='Total', axis=0, ascending=False, inplace=True)
print(df_can.head())
df_can_top = df_can.iloc[0:6, ]
print('top 5',df_can_top)
#df_can_top.set_index('Country', inplace=True)
df_can_top=df_can_top[years].transpose()


df_can_top.plot(kind='area' )
plt.title('Immigration from top5')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() 



##artist layer
df_bottom = df_can.tail()
df_bottom.head()
df_bottom = df_bottom[years].transpose()
#df_bottom.index = df_bottom.index.map(int) # let's change the index values of df_least5 to type integer for plotting

ax = df_bottom.plot(kind='area', alpha=0.55, stacked = False, figsize=(20, 10))
ax.set_title('Immigration Trend of least 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')




# np.histogram returns 2 values
count, bin_edges = np.histogram(df_can[2013])
print(count) # frequency count
print(bin_edges) # bin ranges, default = 10 bins

df_can[2013].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()


# create a dataframe of the countries of interest (cof)
df_cof = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years]
# transpose the dataframe
df_cof = df_cof.transpose() 
# let's get the x-tick values
count, bin_edges = np.histogram(df_cof, 15)
# Un-stacked Histogram
df_cof.plot(kind ='hist',figsize=(10, 6),bins=15,alpha=0.35,xticks=bin_edges,color=['coral', 'darkslateblue', 'mediumseagreen'])
plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()

#Bar chart
# step 1: get the data
df_iceland = df_can.loc['Iceland', years]

df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',  # s: str. will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )

plt.show()

# pie chart
# group countries by continents and apply sum() function 
df_continents = df_can.groupby('Continent', axis=0).sum()

# note: the output of the groupby method is a `groupby' object. 
# we can not use it further until we apply a function (eg .sum())
print(type(df_can.groupby('Continent', axis=0)))

# Plot the data. We will pass in kind = 'pie' keyword, along with the following additional parameters:
# autopct - is a string or function used to label the wedges with their numeric value. 
# The label will be placed inside the wedge. If it is a format string, the label will be fmt%pct.
# startangle - rotates the start of the pie chart by angle degrees counterclockwise from the x-axis.
# shadow - Draws a shadow beneath the pie (to give a 3D feel).


# autopct create %, start angle represent starting point
df_continents['Total'].plot(kind='pie',figsize=(5, 6), autopct='%1.1f%%', startangle=90, shadow=True)

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal') # Sets the pie chart to look like a circle.

plt.show()
### 

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%', 
                            startangle=90,    
                            shadow=True,       
                            labels=None,         # turn off labels on pie chart
                            pctdistance=1.12,    # the ratio between the center of each pie slice and the start of the text generated by autopct 
                            colors=colors_list,  # add custom colors
                            explode=explode_list # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12) 

plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

plt.show()


#### all continents for 2013
df_continents[2013].plot(kind='pie',figsize=(15, 6),autopct='%1.1f%%', startangle=90,    shadow=True,       
                                labels=None,                 # turn off labels on pie chart
                                pctdistance=1.12,            # the ratio between the pie center and start of text label
                                explode=explode_list         # 'explode' lowest 3 continents
                                )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent in 2013', y=1.12) 
plt.axis('equal') 

# add legend
plt.legend(labels=df_continents.index, loc='upper left') 

# show plot
plt.show()





###box plot
df_japan = df_can.loc[['Japan'], years].transpose()
df_japan.head()
df_japan.plot(kind='box', figsize=(8, 6))

plt.title('Box plot of Japanese Immigrants from 1980 - 2013')
plt.ylabel('Number of Immigrants')

plt.show()


df_CI=df_can.loc[['China', 'India'], years].transpose()
# horizontal box plots
df_CI.plot(kind='box', figsize=(10, 7), color='blue', vert=False)

plt.title('Box plots of Immigrants from China and India (1980 - 2013)')
plt.xlabel('Number of Immigrants')

plt.show()

###### two plots at once
fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot). See tip below**

# Subplot 1: Box plot
df_CI.plot(kind='box', color='blue', vert=False, figsize=(20, 6), ax=ax0) # add to subplot 1
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')

# Subplot 2: Line plot
df_CI.plot(kind='line', figsize=(20, 6), ax=ax1) # add to subplot 2
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()

#######

df_can.sort_values(by = ['Total'], axis = 0, ascending = False, inplace = True)
df_top=df_can.head(15)

# create a list of all years in decades 80's, 90's, and 00's
years_80s = list(range(1980, 1990))
years_90s = list(range(1990, 2000))
years_00s = list(range(2000, 2010)) 

# slice the original dataframe df_can to create a series for each decade
df_80s = df_top.loc[:, years_80s].sum(axis=1) 
df_90s = df_top.loc[:, years_90s].sum(axis=1) 
df_00s = df_top.loc[:, years_00s].sum(axis=1)

new_df = pd.DataFrame({'1980s': df_80s, '1990s': df_90s, '2000s':df_00s}) 

# display dataframe

new_df.plot(kind='box')

### scatter plot
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))

# change the years to type int (useful for regression later on)
df_tot.index = map(int, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()

df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

plt.show()

###!!!!!!!
x = df_tot['year']      # year on x-axis
y = df_tot['total']     # total on y-axis
fit = np.polyfit(x, y, deg=1)
df_tot.plot(kind='scatter', x='year', y='total', figsize=(10, 6), color='darkblue')

plt.title('Total Immigration to Canada from 1980 - 2013')
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')

# plot line of best fit
plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

plt.show()

# print out the line of best fit
#'No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1]) 


##### bubble plot
# transposed dataframe
df_can_t = df_can[years].transpose()

# cast the Years (the index) to type int
df_can_t.index = map(int, df_can_t.index)

# let's label the index. This will automatically be the column name when we reset the index
df_can_t.index.name = 'Year'

# reset index to bring the Year in as a column
df_can_t.reset_index(inplace=True)

# view the changes
df_can_t.head()

# normalize Brazil data
norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())

# normalize Argentina data
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())

# Brazil
ax0 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Brazil',
                    figsize=(14, 8),
                    alpha=0.5,  # transparency
                    color='green',
                    s=norm_brazil * 2000 + 10,  # pass in weights 
                    xlim=(1975, 2015)
                    )

# Argentina
ax1 = df_can_t.plot(kind='scatter',
                    x='Year',
                    y='Argentina',
                    alpha=0.5,
                    color="blue",
                    s=norm_argentina * 2000 + 10,
                    ax=ax0
                    )

ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 to 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')


### Regression plot Seaborn
import seaborn as sns
df_1=df_can.drop(['Continent', 'Region','DevName'], axis =1)
df_1.loc['Sum']=df_1.sum()
df_2=df_1.loc[['Sum', ]].transpose()
df_2.rename(columns={'Country':'Year','Sum':'Number'}, inplace=True)
df_2.drop(['Total'], inplace=True)
df_2['Year']=years
ax=sns.regplot(x='Year', y='Number', data=df_2)

##pretty regression plot
plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()


# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)

# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)

# rename columns
df_tot.columns = ['year', 'total']

# view the final dataframe
df_tot.head()


plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013 from Denmark, Sweden and Norway')
plt.show()