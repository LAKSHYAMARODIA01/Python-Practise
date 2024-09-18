#  WAP which finds out Whether a given name is present in a list or not .

l = ["Tom", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")