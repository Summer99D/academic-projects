# PPHA 30537
# Spring 2024
# Homework 4

# Summer Negahdar

# Summer Negahdar
# Summer99D

# Due date: Sunday May 12th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

## first thing first I am  going to import libraries I am using:
import pandas as pd
import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from pandas_datareader import wb
import requests
from bs4 import BeautifulSoup

pd.options.display.float_format = '{:.2f}'.format

##I want to compare South Korea and Italy from 2008 to 2020

# Question 1: Explore the data APIs available from Pandas DataReader. Pick
# any two countries, and then 
#   a) Find two time series for each place
#      - The time series should have some overlap, though it does not have to
#        be perfectly aligned.
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
#      - You do not have to make four distinct downloads if it's more appropriate
#        to do a group of them, e.g. by passing two series titles to FRED.

#South korea- FRED
start_skGDP = datetime.date(year=2008, month=1,  day=1)
end_skGDP   = datetime.date(year=2020, month=12, day=31)
series_sk = ['MKTGDPKRA646NWDB', #this is annual GDP but not seaosnally adjusted
             'LFWA64TTKRQ647S'] #this is quarterly working population, seasonally adjusted
source = 'fred'

SK_df = web.DataReader(series_sk, source, start_skGDP, end_skGDP)
SK_df.head()
##now I need to change this to annually

SK_df= SK_df.resample('Y').mean()

##now I need to change the index form date to year
SK_df['year'] = SK_df.index.year
## I am going to rename the cols to understand what is going on
SK_df.rename(columns={'MKTGDPKRA646NWDB': 'GDP'}, inplace=True) #GDP in millions
SK_df.rename(columns={'LFWA64TTKRQ647S':'Working_Pop'}, inplace=True) #working pop in tohusands
SK_df['country']= 'South Korea'
SK_df.head()
##need to see Dtypes for merging later on
SK_df.dtypes
SK_df.reset_index()['year']



#world bank- Italy
indicator = ['NY.GDP.MKTP.CD', #annual GDP (USD
             'SL.TLF.TOTL.IN'] #annual working pop(thousands)
country = 'ITA'

ITA_df = wb.download(indicator=indicator, 
                 country=country, 
                 start=2008, end=2020)

ITA_df.head()
ITA_df.reset_index()['year']
# Reset the index of the ITA_df DataFrame
ITA_df.reset_index(inplace=True)



##renaming the oclumns to understnad what is oging on:
ITA_df.rename(columns={"NY.GDP.MKTP.CD": 'GDP'}, inplace=True)
ITA_df.rename(columns={'SL.TLF.TOTL.IN': 'Working_Pop'}, inplace=True)
# Convert the data type of the 'year' column in one of the DataFrames
ITA_df['year'] = ITA_df['year'].astype(int) 

##I don't know why the GDP for Italy is funky, I made sure to look for 

Merged_df= pd.merge(SK_df, ITA_df, on= ['year', 'Working_Pop', 'GDP', 'country'], how='outer')
Merged_df.rename(columns={'year':'Year'}, inplace=True)
Merged_df.rename(columns={'country':'Country'}, inplace=True)
Merged_df.set_index('Year', inplace=True)
print(Merged_df)

#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then do any necessary merge and reshaping to put
#      them together into one long (tidy) format dataframe.




#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file. Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.
#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or some with unclear names, or a column of mixed 
#      strings and integers. Write the dataframe you've created out to a 
#      file named q1.csv, and commit it to your repo.

# Clean up column names
Merged_df.columns = ['GDP', 'Working Pop', 'Country']

# Write the DataFrame to a CSV file
Merged_df.to_csv('q1.csv', index=False)

# Print the first few rows of the cleaned DataFrame
print(Merged_df.head())



# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and 12
# bullet points under "Elective courses". Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points

#   - Add each bullet point to the csv_doc list below as strings (following 
#     the columns already specified). 

url= 'https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics'
path= '/Users/samarnegahdar/Documents/school/spring quarter/Python/homework-4-Summer99D'

response = requests.get(url)
soup= BeautifulSoup(response.text, 'lxml')
required = soup.find('h3', string='Required courses').find_next('ul')
electives = soup.find('h3', string='Elective courses').find_next('ul')

post_req= required.find_next('h3')


##I need to specify all the bullet points that are not in elective section. 
#I also asked GPT how to parse strings that are not in a row since homework was about
#a table and its rows
Required_courses = []
current_element = required
while current_element and current_element != electives:
    if current_element.name == 'li':
        Required_courses.append('Required,' + current_element.text.strip())
    current_element = current_element.find_next()

Elective_courses = []
for course in electives.find_all('li'):
##since we have wrote a condition for required we dont need to specify for the
#elective
    Elective_courses.append('Elective,' + course.text.strip())


Curriculum = Required_courses + Elective_courses

csv_doc = ['Type,Description']
with open("q2.csv", "w") as f:
    f.write(csv_doc[0] + "\n") # I am going to pass down the csv_doc as header
    for line in Curriculum:
        f.write(line + "\n")

Q2_df = pd.read_csv("q2.csv", encoding="latin1")


assert Q2_df.shape == (18, 2) 
#The first string that gets added should be 
#     approximately in the form of: 
#     'required,PPHA 30535 or PPHA 30537 Data and Programming for Public Policy I'
#   - Hint: recall that \n is the new-line character in text
#   - You do not have to clean up the text of each bullet point, or split the details out
#     of it, like the course code and course description, but it's a good exercise to
#     think about.
#   - Using context management, write the data out to a file named q2.csv
#   - Finally, import Pandas and test loading q2.csv with the read_csv function.
#     Use asserts to test that the dataframe has 18 rows and two columns.


