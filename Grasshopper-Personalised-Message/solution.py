#Create a function that gives a personalized greeting. 
#This function takes two parameters: name and owner.
#Use conditionals to return the proper message:

Use conditionals to return the proper message:
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
print(greet('Giveon', 'Giveon')) 
print(greet('Giveon', 'Brent'))