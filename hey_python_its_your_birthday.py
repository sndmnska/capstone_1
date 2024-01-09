import datetime

print("Hello World\n")  

# This was mostly coded on a cell phone in the back of a car during a road trip. Neat! What an age we live in. :)

'''
DOCTYPE
This program asks for your name and the month you were born in.

It will print: 
* A greeting to you, using your name
* A message with the number of letters in your name
* A 'Happy birthday month!' message if you were born in the current month

Easier - compare the user's input to "January" or "August" or whatever the current month is
Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.


Design:
input name, input birth month as a number (more user and programmer friendly). Let's go easier: Use a month lookup array.
'''

name = input('Please enter your name: ')
birth_month = int(input('What is your birth month? Input an integer (1-12): '))
print('*' * 15)
print(birth_month)

# Compare month input to list, also count letters in name
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
txt_b_month = month_list[birth_month - 1]
txt_b_month = txt_b_month.strip()

n_letters = len(name) # TODO Might want to be more specific, detecting alphanumeric characters only.
cur_month = datetime.datetime.now().month  # Returns integer  of current month


birthday_match_msg= ""
if birth_month == cur_month:
    birthday_match_msg = "\nYou were born this month! Happy birth month!"

# Output response to user 
print(f"\nGreetings {name}, and welcome back to Python.  \
      \nThere are {n_letters} letters in your name, and you were born in {txt_b_month}.{birthday_match_msg}\n")