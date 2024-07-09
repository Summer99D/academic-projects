# PPHA 30537
# Spring 2024
# Homework 1

# Summer Negahdar
# Summer99D

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
any_list= ["Mary", "Daisy", "Rose", "Lily"]
for object in any_list:
    print("the value at position", any_list.index(object), "is" , object)
    
    


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
palindrome = ["radar", "A man, a plan, a canal, Panama", "Microsoft", "This isn't a palindrome"]

for phrase in palindrome:
    cleaned_phrase = ''.join(character.lower() for character in phrase if character.isalnum())
    if cleaned_phrase == cleaned_phrase[::-1]:
        print(f"'{phrase}' is a palindrome.")
    else:
        print(f"'{phrase}' is not a palindrome.")



# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while choice not in available_vegetables:
    print("Invalid choice, please try again.")
    choice = input('Please pick a vegetable I have available: ')
print("Please pick up your vegetable. Thank you for shopping with us!")

        
        


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.
my_list = ["A", "B", "C", "D", "E", "F"]
new_list = [letter.lower() for letter in my_list if letter not in ["A", "B"]]
print(new_list)




# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']
converted_names= {}
for i in range(len(short_names)):
    converted_names[short_names[i]]=long_names[i]
    
  #only bychanging the spacing before print, it makes a difference what it prints  
print(converted_names)


#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]
def summation(a,b):
    sum = a+b
    if sum > 10:
        return "big"
    elif sum==10:
        return "just right"
    else:
        return "small"
result_list = [summation(a,b) for a,b in start_list]
print(result_list)



# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.


def my_func(a=10):
    b = 40
    return a + b
x = my_func()
print(x)


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
import string
import random

def password_generate(length, special_chars=True, include_numbers=True):
    if length < 8 or length > 16:
        return "Password length must be between 8 and 16 characters."
    
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if special_chars:
        chars += "!@#$%^&*"
    
    return ''.join(random.choice(chars) for _ in range(length))
example_password = password_generate(11)
print(example_password)


    
  
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

import random

class Movie:
    def __init__(self,name,genre,rating):
        self.name = name
        self.genre= genre
        self.rating= rating
    
class MovieDatabase:
    def __init__(self, creator_name):
        #the instance will be called the creator's name
        self.creator_name = creator_name
        #we create an empty list for movies to recommend
        self.movies = []
        #we define the method to add movie and its detail that include genre and personal rating
    def add_movie(self, movie_name, genre, personal_rating):
        movie = Movie(movie_name, genre, personal_rating)
        self.movies.append(movie)
        #define another method for asking for recommendations, here we just say to 
        #return the answer "not found" in case the movie list is empty (so it won't go crazy)
    def what_to_watch(self):
        if not self.movies:
           print("there are no movies in the database")
 #randomize and pick a movie from the list of movies I provide in "movies"   
        random_movie = random.choice(self.movies)
        #the way to call the name the genre and the rating is (f'name: {random_movie.name})
        print(f"{self.creator_name}'s suggestion for the day is:")
        print(f"name: {random_movie.name}")
        print(f"genre: {random_movie.genre}")
        print(f"rating: {random_movie.rating}/5")

        
my_database = MovieDatabase("Summer")

#adding the movies

my_database.add_movie("past Lives", "romance", 4.5)
my_database.add_movie("The boy and the Heroen", "Anime", 4)
my_database.add_movie("poor things", "Dark Comedy", 0)
my_database.add_movie("Sheyda", "Narrative", 4.5)

#now it will give us a recommendation.
my_database.what_to_watch()









