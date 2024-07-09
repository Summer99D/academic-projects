# PPHA 30537
# Spring 2024
# Homework 3

# Summer Negahdar

# Summer Negahdar
# Summer99D

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import matplotlib.image as mpimg
import us
import statsmodels.api as sm



x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

#my x axis was cramped so I made it a little wider and readable
plt.figure(figsize=(15, 8))
#Y1 should be a scatterplot
plt.scatter(x, y1, color='orange', label='Y1')

#now we plot Y2 which is al inear plot:
plt.plot(x, y2, color='blue', label= 'Y2')
#refining the plot
plt.xlabel('Date')
plt.ylabel('Y values')
plt.title('Q1 1 plot')
plt.legend()

#now we show the plot and save it
#I kept seeing white photo and the reason was using plt.show before saving!
plt.savefig('Q1_1_plot.png')
plt.show()


# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.

#I did not know how to load an image so I asked GPt "how to load an image using
#matplotlib
img = mpimg.imread('question_2_figure.png')

plt.imshow(img)
plt.axis('off')  # if I don't turn it off, it will show me two sets of axes
plt.show()

#now we define the plot
#X is just a range form 10 to 19

X1 = range(9, 19)  
# I found equations for each line
Y1 = [-5/4 * x + 63/2 for x in X1]  
Y2 = list(X1)  


#now I do some housekeeping
plt.plot(X1, Y1, color="red", label="Red")
plt.plot(X1, Y2, color="blue", label="Blue")

plt.xlim(9, 19)
plt.ylim(9, 19)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("X marks the spot")
plt.legend(loc='center left')
plt.savefig('Q1_2_plot.png')
plt.show()




# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

# Loading the dataset
car_df = pd.read_csv('mpg.csv')

# we need thress scatterplots, in one figure:
plt.figure(figsize=(15, 5))

#the order of numbers in the parantheses is that one row three columns and 
#then the first one
plt.subplot(1, 3, 1)
plt.scatter(car_df['displacement'], 
            car_df['mpg'], color='pink')
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.title('MPG-Displacement')
plt.savefig('Q1_3a_plot.png')

#the order of numbers is as previous one only that we are defining the second table
plt.subplot(1, 3, 2)
plt.scatter(car_df['horsepower'], 
            car_df['mpg'], color='orange')

plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.title('MPG_Horsepower')
plt.savefig('Q1_3b_plot.png')


##now this is oging to be the third scatterplot
plt.subplot(1, 3, 3)
plt.scatter(car_df['weight'], 
            car_df['mpg'], color='green')
plt.xlabel('Weight (pounds)')
plt.ylabel('MPG')
plt.title('MPG_Weight')
plt.savefig('Q1_3c_plot.png')

plt.show()



# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
plt.scatter(car_df['cylinders'], 
            car_df['mpg'], color= "red")
plt.xlabel('Cylinder')
plt.ylabel('MPG')
plt.title('MPG_cylinder')
plt.show()


#since the number of cylinders are specific(6,8,...) we don't see clearly how 
#each category of cylinders effect the MPG. that is why we need to group them based on
#the number of cylinders to see in general how each category of car have different MPGs

sns.boxplot(x='cylinders', y='mpg', data=car_df)
plt.xlabel('Cylinders')
plt.ylabel('MPG')
plt.title('MPG for each number of cylinders')
plt.show()

##this boxed plot clearly shows us how in each category the observations are dispersed.
#for example, for cars with 5 cylinders, the mean of MPG is on 25 but there are
#certain cars that have 5 cylinders but their MPG is 30(upper quantile)


# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.


# Creating a two-by-two grid of subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, 
                                             ncols=2, 
                                             figsize=(10, 8))

# scatter plot of MPg on displacement
ax1.scatter(car_df['displacement'], 
            car_df['mpg'], alpha=0.3, color= 'pink')
ax1.set_xlabel('Displacement')

#scatter plot of MPG on horsepower
ax2.scatter(car_df['horsepower'], 
            car_df['mpg'], alpha=0.3, color='orange')
ax2.set_xlabel('Horsepower')
#I need to remove the Y axis
ax2.yaxis.set_ticklabels([])


#scatter plot of MPg on weight
ax3.scatter(car_df['weight'], 
            car_df['mpg'], alpha=0.3, color='green')
ax3.set_xlabel('Weight')

#scatterp lot of MPG on acceleration
ax4.scatter(car_df['acceleration'], 
            car_df['mpg'], alpha=0.3, color='purple')
ax4.set_xlabel('Acceleration')
#removing Y axis 
ax4.yaxis.set_ticklabels([])


# I asked GPt about ways to rotate the text so it is more readable and made some adjustments.
#My plot was also very compact
fig.suptitle('Changes in MPG')
fig.text(0.04, 1, 'MPG', va='center', rotation='vertical', fontsize=14)

# Adjust layout to prevent overlapping labels
plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])

# Saving the figure and showing plot
plt.savefig('q1_5_plot.png')

plt.show()


# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.

##again since we have grouping, I am going to use boxplots:


sns.boxplot(x='origin', y='mpg', data=car_df)
plt.xlabel('Origin', fontweight='bold')
plt.ylabel('MPG', fontweight='bold')
plt.title('fuel efficiency by region')
plt.show()

#the Y axis is Miles/gallon so the higher the number of MPG is,
#the more efficient the car is. as shown in the box plot, american cars are the least efficient one



# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.

sns.scatterplot(x='displacement', 
                y='mpg', 
                hue='origin', data=car_df)
plt.xlabel('Displacement')
plt.ylabel('MPG')
plt.title('MPG_Displacement by Origin')
plt.legend(title='Origin')
plt.savefig('q1_7_plot.png')
plt.show()

##connecting the dots from our findings in Q1-6, since american cars have bigger engines
#(larger capacities) they consume more gas and therefore are less efficient. 

# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).

##Unemployment dataset
unemp_df= pd.read_csv('unemp.csv')

#policy uncertainty dataset
pol_df=pd.read_excel('policy_uncertainty.xlsx')
# I need to change the format of date in this df
##I asked gpt how to use two column to create a third column for date
pol_df['DATE'] = pd.to_datetime(pol_df['year'].astype(str) + 
                                pol_df['month'].astype(str).str.zfill(2), 
                                format='%Y%m')
pol_df.drop(columns=['year', 'month'], inplace=True)
pol_df_2020= pol_df[pol_df['DATE'] >= ' 2020-01-01']

#the states column need to be modified as one only has abbreviations
unemp_df['state'] = unemp_df['STATE'].apply(lambda x: us.states.lookup(x).name)
unemp_df.drop(columns=['STATE'], inplace=True)
unemp_df['DATE'] = pd.to_datetime(unemp_df['DATE']) #there was a problem with merging 
#so I had to look up the error and then I realized I have to convert the format of DATE
#column

#    2.1: Merge both dataframes together
##I am merging on both the state and the date 
Q2_1 = pd.merge(unemp_df, pol_df_2020, on=['DATE', 'state'], how='inner')
Q2_1.head()
Q2_1.shape()
print(Q2_1)


#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
## I am assuming that you want the result stored as a new column?
##first stage is the log of EPu_composite
Q2_1['log_EPU_Composite'] = Q2_1['EPU_Composite'].apply(lambda x: np.log(x))
#second stage is the first difference
Q2_1['LFD_EPU_Composite'] = Q2_1['log_EPU_Composite'].diff()
Q2_1.dropna(inplace=True)

#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.

##I am selecting the states I have visited so far: 
Q2_2= Q2_1.loc[Q2_1['state'].isin(['New York', 'Illinois', 
                                   'California', 'Wisconsin', 'Louisiana'])]

##I am oging to create 5 subplots, one for each state:
fig, ((ax1), (ax2), (ax3), (ax4), (ax5)) = plt.subplots(5, 1, figsize=(10, 15), sharex=True)

# Plot data for each state on its own subplot
Q2_2[Q2_2['state'] == 'California'].plot(x='DATE', 
                                         y=['unemp_rate', 'LFD_EPU_Composite'], ax=ax1)
Q2_2[Q2_2['state'] == 'Illinois'].plot(x='DATE', 
                                       y=['unemp_rate', 'LFD_EPU_Composite'], ax=ax2)
Q2_2[Q2_2['state'] == 'Louisiana'].plot(x='DATE', 
                                       y=['unemp_rate', 'LFD_EPU_Composite'], ax=ax3)
Q2_2[Q2_2['state'] == 'New York'].plot(x='DATE', 
                                       y=['unemp_rate', 'LFD_EPU_Composite'], ax=ax4)
Q2_2[Q2_2['state'] == 'Wisconsin'].plot(x='DATE', 
                                        y=['unemp_rate', 'LFD_EPU_Composite'], ax=ax5)

#we set titles 
ax1.set_title('California State')
ax2.set_title('Illinois State')
ax3.set_title('Louisiana State')
ax4.set_title('New York State')
ax5.set_title('Wisconsin State')

fig.suptitle('Unemployment Rate and LFD of EPU-C Over Time for Visited States')
fig.text(0.5, 0.01, ha='center', 
         fontweight='bold') 

plt.savefig('Q2_2_plot.png')
plt.show()

#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
#we need to add a constant
import statsmodels.formula.api as smf
regression = 'unemp_rate ~ LFD_EPU_Composite + C(state)'
Q2_1 = Q2_1.dropna(subset=['LFD_EPU_Composite', 'unemp_rate', 'state'])
model = smf.ols(regression, data=Q2_1)
result = model.fit()





    
#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.
result.summary()


##the intercept shows that there is a negative correlation(-0.1193) between unemployment
#rate and LFD for economic policy uncertainty. meaning that the higher the uncertainty 
##the R-squared is only 16% meaning that not that much of variety is explained by 
# level is, the lower the unemployment rate owuld be. however the P-value for this 
#coef is 0.236 which indicates it is not statistically significant. there is no correlation between
#LFD EPU and the unemployment rate!