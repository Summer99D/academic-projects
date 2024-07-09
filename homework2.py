# PPHA 30537
# Spring 2024
# Homework 2

# Summer Negahdar
# Summer99D

# Due date: Sunday April 21st before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################



#I import all the needed libraries in the beginning for ease of use
import pandas as pd
import os
import us
import numpy as np

# I don't like seeing numbers in scientific method so I change format:
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# PART 1: Macro Data Exploration

# Question 1.1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.

#I looked up how to use os and it needs to have a file path as well as the name of the file we want to call
#that's why I created "pop_est" which is the csv file we want to call and "working_directory" which is the path we want to call
working_directory= '/Users/samarnegahdar/Documents/school/spring quarter/Python/homework 2/homework-2-Summer99D'
pop_est= 'NST-EST2022-ALLDATA.csv'
file_path= os.path.join(working_directory, pop_est)
pop_est_df= pd.read_csv(file_path)
print(pop_est_df)


# Question 1.2: Your data only includes fips codes for states (STATE).  Use 
# the us library to crosswalk fips codes to state abbreviations.  Drop the
# fips codes.
#the fips are integers so I need to convert them to strings for us to work:
    


#I looked up how to use the us library to convert fips to state abbreviations
#and then wrote a for loop to go over every "fips" in the column STATE and return the state name
fips_convert = {}
for fips in pop_est_df['STATE']:
    fips_interpret = us.states.lookup(fips)
    if fips_interpret is not None:
        fips_convert[fips] = fips_interpret.abbr

    
#I am creating a new column called stat_name and call the for loop to iterate over existing data in fips. 
pop_est_df['State_name']= pop_est_df['STATE'].map(fips_convert)

#now that I have created the new column, I will delete the original state column with fips codes. the "inplace=True"
#is in place meaning that instead of creating a new data frame it will write over the existing one. 
pop_est_df.drop(columns= ['STATE'], 
                inplace=True)
print(pop_est_df)
#result: there are rows with a fips code 0, there are no states with fips code 0 and 0 usually refers to either USA
#as a whole or the culmination of a few states. for now we have them as NaNs.

# Question 1.3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.  Do not 
# create plots or use groupby; we will do that in future homeworks.  
# Show the relevant exploration output with print() statements.

#let's see how many rows and cols we have here:
print("dimension of our dataframe is:", pop_est_df.shape)

#I want to first check the summary stats for numerical columns:
print('statistical summary:', 
      pop_est_df.describe())

#I sorted them by the base population column in 2020 
#and then took a look at the first few rows.
print('sorted data based on base population on 2020_first rows:', 
      pop_est_df.sort_values(
          by= 'ESTIMATESBASE2020').head())
#let's see how many states are present in this df
print(pop_est_df['State_name'].unique().shape, 
      'states are present in this dataset')


# Question 1.4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.

Q1_4= pop_est_df[['State_name','POPESTIMATE2020','POPESTIMATE2021', 
                  'POPESTIMATE2022']]
Q1_4 = Q1_4.dropna(subset= ['State_name'])
print(Q1_4.shape)
print(Q1_4)
Q1_4['State_name'].unique()


# Question 1.5: Show only the 10 largest states by 2021 population estimates,
# in decending order.

#first thing we do is to gorup by states and sort them by 'popestimate2021'
#and to make it decsending, we should turn of ascending
#now we call for the frist 10 thorugh head() and assign number
Q1_5= Q1_4.sort_values(
    by= 'POPESTIMATE2021', ascending=False).head(10)
print(Q1_5)

# Question 1.6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?

#my code did not work so apparantly I have to reset the index for lambda to work
#what reset.index does is that it iterates over the original datafram
#which in this case is Q1_4
def pop_change(row):
    return row['POPESTIMATE2022']- row['POPESTIMATE2020']
Q1_4['POPCHANGE']= Q1_4.apply(pop_change, axis=1)
# since there are NaNs, I had to add a 
#third condition to return NA if there is no data available. 
def pop_binary_var(row):
        if row['POPCHANGE'] > 0:
            return 'positive'
        elif row['POPCHANGE'] < 0:
            return 'negative'
        else:
            return 'not applicapable'
Q1_4['POPCHANGE']= pd.to_numeric(Q1_4['POPCHANGE'])
#I added a new column to see the positive anf negative amounts for population change
# I am going to use this to get ah headcount of positive and negative growth.
Q1_4['pop_change_binary']= Q1_4.apply(lambda row:pop_binary_var(row),
                                      axis=1 )
pos_growth= (Q1_4['pop_change_binary'] == 'positive').sum()
print('the number of states that had a positive population growth in 2022 form 2020 is:',
      pos_growth)
neg_growth= (Q1_4['pop_change_binary'] == 'negative').sum()
print('the number of states that had a negative population growth in 2022 form 2020 is:',
      neg_growth)
print(f' We can see that {pos_growth} states had a rise in population and {neg_growth} states had a drop in population between 2020 and 2022')

# Question 1.7: Show all the states that had an estimated change in either
# direction of smaller than 1000 people.

#in Q1_4 we look at all the popchange variables whose absolute value is less than 1000
Q1_7= Q1_4[Q1_4['POPCHANGE'].abs() < 1000]['State_name'].tolist()
print(Q1_7)
# I asked chatGPT for a way to be 
#able to see the name of states specifically that meet this conditions 
#and it recommended using tolist() function



# Question 1.8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.


# I am going to use the method we had in lab assignment5b for writing a zscore
Z_sc = (Q1_4['POPCHANGE'] - Q1_4['POPCHANGE'].mean()) / Q1_4['POPCHANGE'].std()

#the answer to Q8 is all the Z-sc that have an absolute value greater than 1
#and then I arrange then in a descending order
Q1_8 = (Z_sc[Z_sc.abs() > 1]).sort_values(ascending=False)
print(Q1_8)

#I'm guessing we are being asked to return the name of the states 
#where this condition holds and then as the second step 
#organize them on a descending order






#PART 2: Data manipulation

# Question 2.1: Reshape the data from wide to long, using the wide_to_long function,
# making sure you reset the index to the default values if any of your data is located 
# in the index.  What happened to the POPCHANGE column, and why should it be dropped?
# Explain in a brief (1-2 line) comment.

long_df = pd.wide_to_long(Q1_4, 'POPESTIMATE', i= 'State_name', j='Year').reset_index()
long_df = long_df.drop(columns=['POPCHANGE','pop_change_binary'])
print(long_df)
example= long_df[long_df['State_name'] == 'FL']
print(example)

        
#the reason is because when we use wide-to-long, 
#it usually is effective for data types that have been recorded over time(repetatively)
#and since popchange was only measured once (over the course of two years) 
#it keeps repeating the same amount for each state(like the example) 
#for different years which is not correct!

# Question 2.2: Repeat the reshaping using the melt method.  Clean up the result so
# that it is the same as the result from 2.1 (without the POPCHANGE column).
Q2_2= Q1_4.melt(id_vars= ['State_name'],
                value_vars= ['POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022'],
                var_name= 'Year', value_name= 'population estimate')
#when I print it, in the year oclumn is see the whole phrase
#so I asked GPT "how to extract a part of the word of a value in a column"
Q2_2['Year']=Q2_2['Year'].str.extract(r'(\d{4})')
print(Q2_2)

# Question 2.3: Open the state-visits.xlsx file in Excel, and fill in the VISITED
# column with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the xlsx file as a dataframe in
# Python, and merge the VISITED column into your original wide-form population 
# dataframe, only keeping values that appear in both dataframes.  Are any 
# observations dropped from this?  Show code where you investigate your merge, 
# and display any observations that weren't in both dataframes.
state_visit= 'state-visits.xlsx'
file_path2= os.path.join(working_directory, state_visit)
state_visit_df= pd.read_excel(file_path2)
print(state_visit_df.head(10))
Q2_3= long_df.merge(state_visit_df, left_on='State_name',right_on='STATE', 
                    how='outer', indicator= True).drop(columns=['STATE'])
#by adding the indicator column we will be able to see where vlaue is not form both
print(Q2_3)
Q2_3['State_name'].unique()



#I want to see whether an vlaues have dropped from the df or not
start_length= len(long_df)
end_length= len(Q2_3)
assert(start_length == end_length),'the final df length is not equivalent of original df'
#apparantly some values have dropped, but what?
print(start_length)
print(end_length)

#I asked GPT for a way to negate a statement that has isin in it. 
#it said to use a tilda "~"
non_common_val = long_df[~long_df[
    'State_name'].isin(Q2_3['State_name'])]
print("the unique rows after merge are:")
print(non_common_val)



# Question 2.4: The file policy_uncertainty.xlsx contains monthly measures of 
# economic policy uncertainty for each state, beginning in different years for
# each state but ending in 2022 for all states.  The EPU_National column esimates
# uncertainty from national sources, EPU_State from state, and EPU_Composite 
# from both (EPU-N, EPU-S, EPU-C).  Load it as a dataframe, then calculate 
# the mean EPU-C value for each state/year, leaving only columns for state, 
# year, and EPU_Composite, with each row being a unique state-year combination.

#we first load in and assign it to be a dataframe
policy_uncer= 'policy_uncertainty.xlsx'
file_path3= os.path.join(working_directory, policy_uncer)
policy_uncer_df= pd.read_excel(file_path3)
print(policy_uncer_df.head(10))

#what I did was first I dropped the month, state and national EPU
#then O grouped by year and state and took a mean based on those gorups which would be
#the composite EPU for each year for each state
#I resetted the index cause I don't want "state col
#to be my index!
Q2_4= policy_uncer_df.drop(columns= ['month', 'EPU_National', 
                                     'EPU_State']).groupby(['state', 
                                                            'year']).mean().reset_index()
print(Q2_4)

# Question 2.5) Reshape the EPU data into wide format so that each row is unique 
# by state, and the columns represent the EPU-C values for the years 2022, 
# 2021, and 2020. 

#I first created a subset form previous quesiton to filter all years but 2020-2022
#then O used pivot to chage the formate to wide, 
#columns are the years and each cell is filled with
#EPU_composite mean form previous question. 

filtered_df= Q2_4[(Q2_4['year']<2023) & 
                  (Q2_4['year']> 2019)]
print(filtered_df)
Q2_5= filtered_df.pivot(index='state', columns='year', 
                        values='EPU_Composite').reset_index()
Q2_5= Q2_5.rename(columns={2020: 'year 2020 EPU composite mean', 
                           2021: 'year 2021 EPU composite mean', 
                           2022: 'year 2022 EPU composite mean'})



#I am using liste comprehension to change the name of the columns in a way
#people understand what they are looking at)EPU ocmposite) and not only the year



# Question 2.6) Finally, merge this data into your merged data from question 2.3, 
# making sure the merge does what you expect.

##the first problem is that state names on our new df is not abbreviated so we need
##to overwrite them so it is mergable. 
#I am going to write a for loop that takes the abbreviated names on Q2_3 and
#returns full name
Q2_3['State_name'] = Q2_3['State_name'].apply(
    lambda abbr: us.states.lookup(abbr).name if abbr else None)

    

Q2_6= Q2_3.merge(Q2_5, left_on= 'State_name', right_on='state', 
                 how= 'inner')
Q2_6.drop(columns=['State_name', 'POPESTIMATE', 'Year', '_merge'], inplace=True)
#I realized I have forgotten to drop year col after pivotting that is why
#I am dropping cols I don't need
Q2_6 = Q2_6.groupby('state').mean().reset_index()
print(Q2_6)
Q2_6['state'].nunique()
Q2_6['state'].unique()

#I want to check for any potential unique rows
start_length_6= len(Q2_5)
end_length_6= len(Q2_6)
assert start_length_6== end_length_6, 'the length of merged df does not match with that of original df'
#as expected there are some states that are not present in Q2_5!(all A-C states)



# Question 2.7: Using groupby on the VISITED column in the dataframe resulting 
# from the previous question, answer the following questions and show how you  
# calculated them: a) what is the single smallest state by 2022 population  
# that you have visited, and not visited?  b) what are the three largest states  
# by 2022 population you have visited, and the three largest states by 2022 
# population you have not visited? c) do states you have visited or states you  
# have not visited have a higher average EPU-C value in 2022?
visited= Q2_6.groupby(['VISITED'])
##A
#I can use get.group for this question, it will show me wherever my df grouped
#based on visited is equal to 1 and then I ask to show me the minimum based on
#EPU mean composite column

#Smallest state by 2022 population visited
smallest_visited = visited.get_group(1)['year 2022 EPU composite mean'].idxmin()
smallest_state_visited = Q2_6.loc[smallest_visited]
print('The state visited in 2022 with the smallest population is:')
print(smallest_state_visited)

# Smallest state by 2022 population not visited
smallest_Nvisited = visited.get_group(0)['year 2022 EPU composite mean'].idxmin()
smallest_state_Nvisited = Q2_6.loc[smallest_Nvisited]
print('The state not visited in 2022 with the smallest population is:')
print(smallest_state_Nvisited)

# B) the first part is like question A the only difference is that instead of 
#max or min prompt we sort vlaues on a descending pattern and look for top 3
#thorugh head prompt
#Largest states by 2022 population visited
largest_visited = visited.get_group(1)['year 2022 EPU composite mean'].nlargest(3)
largest_states_visited = Q2_6.loc[largest_visited.index]
print('The three largest states visited in 2022 by population are:')
print(largest_states_visited)

# Largest states by 2022 population not visited
largest_Nvisited = visited.get_group(0)['year 2022 EPU composite mean'].nlargest(3)
largest_states_Nvisited = Q2_6.loc[largest_Nvisited.index]
print('The three largest states not visited in 2022 by population are:')
print(largest_states_Nvisited)

# C) Comparing average EPU-C value in 2022 for visited and not visited states
EPU_visited_mean = visited.get_group(1)['year 2022 EPU composite mean'].mean()
EPU_Nvisited_mean = visited.get_group(0)['year 2022 EPU composite mean'].mean()

if EPU_visited_mean > EPU_Nvisited_mean:
    print('States visited in 2022 have a higher EPU_Composite mean ')
else:
    print('States not visited in 2022 have a higher EPU-Composite mean')


# Question 2.8: Transforming data to have mean zero and unit standard deviation
# is often called "standardization", or a "zscore".  The basic formula to 
# apply to any given value is: (value - mean) / std
# Return to the long-form EPU data you created in step 2.4 and then, using groupby
# and a function you write, transform the data so that the values for EPU-C
# have mean zero and unit standard deviation for each state.  Add these values
# to a new column named EPU_C_zscore.

#I am going to use the same method we had in lab assignment 5b:
zsc=Q2_4.groupby('state' , 
               group_keys=False)['EPU_Composite'].apply(
                   lambda v: (v-v.mean())/v.std())
Q2_4['EPU_C_zscore']=zsc
print(Q2_4)

