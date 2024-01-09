"""
README
This program asks for the users current class load.  
When user is finished, it will repeat the list back to the user, one item per line.
"""
def main():
    the_classes = get_list_from_user()
    print_class_list(the_classes)

def get_list_from_user():
    # Looped function to build a class list. A blank list exits the program.
    cl = [] 
    fc = (input("Please enter your first class: "))
    if fc == "": # fc == first class
        return ""
    cl.append(fc)
    while True:
        nc = input("Enter your next class, or press RETURN to print your class list: ")
        if nc == "": # nc == next class
            break
        else:
            cl.append(nc)
    return cl

def print_class_list(l):
    if l == "":
        print("\nNo class list was entered. \n\tExiting......")
        return
    print("*" * 15)
    print("\nYour Class List:")
    print("-" * 15)
    ct = 0 # count
    for cls in l:  # For 'class' in 'list'
        ct = ct + 1
        print(f"Class {ct}.  --- {cls}")
    print("*" * 15)



main()