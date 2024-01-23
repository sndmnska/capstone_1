

'''
README
This program transforms all inputted text into camelCase.   
To do this, all inputted text will have spaces removed. Furthermore, the first word will be all lowercase, and all remaining words will be first letter uppercase. 

Optional extra question: print a warning message if the input will not produce a valid variable name. 
You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or 
containing invalid characters such as # or + or ".  
Or, would it be easier to check that the name only contains valid characters?

Design: 
1) Recieve Input
2) Check for invalid characters (regex)
3) Parse word into an ordered list or ordered array
4) first_word.lowercase()
5) subsequent_word[s].lowercase().capitalize()   # .capitalize() apparently will capitalize the first letter only.
6) Loop through

'''

def main():
    banner()
    print("\n* * * * camelCaseTransformer * * * *\n")
    t = False  # Test boolean 
    while t == False: 
        statement= input("Enter text: ")
        t, b = character_check(statement)  # Check the statement and return True, True if passes regex test
        if b == False:  # Adding a condition where user enters no text and exits the program as a result. 
            return
    # From this point t == True, so we should have a string we can work with

    # # Test lines
    # valid_test_string = "thIs is THE vaLid test STRing"
    # statement = valid_test_string

    split_list = statement.split( )
    result = list_to_camel_case(split_list)
    print('-' * 15)
    print("View results below. Thanks for using this program!\n")
    print(result)
    print("")

def list_to_camel_case(li):
    li[0] = li[0].lower()  # lowercase the first word
    for x in range(1, len(li)): # Skip the first word, capitalize the rest
        li[x] = li[x].capitalize()     
    res = ''.join(li)
    return res

def banner():
    """ Display progam name """
    message = "Awesome CamelCase program!!"
    stars = '*' * len(message)

    print(f'\n{stars}\n{message}\n{stars}')


def character_check(st): 
    # True condition is a pass and continue, False condition is a fail and reenter, else condition is a blank string (exit program). 
    # returns {test_bool for string results, and a second boolean for when the user indicates they want to exit by entering nothing.}
    
    test_bool = False
    user_continue_bool = True
    
    if st == "" or st is None:
        print ("\nNo text entered.   \n\tExiting program.....")
        user_continue_bool = False
    else:  # TODO regex for necessary characters
        # The statement must start with a Letter. 
        # The remaining characters in the statement can be alphanumeric. 

        ## ********* TODO Remove this and next line when ready to test ***********
        test_bool = True  #  <--- For testing purposes

        # print(f'****WARNING: The string entered contains invalid characters. Please try again.')



    return test_bool, user_continue_bool
main()

