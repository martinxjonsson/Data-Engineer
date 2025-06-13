print("Welome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"Hello {name}, you are {age} years old.")


if age >= 18:
    print("You are old enough to play!")
    want_to_play = input("Do you want to play? ")
    if want_to_play == "yes":
        print("Let's play!")

else:
    print("You are too young.")



'''
< - less than
> - greater than
<= - less than or equal too
>= - greater than or equal too
== - is equals to
!= - not equal to
'''
'''
** - raise to power of
* - Multiplication
/ - Division 
+ - Addition
- - Subtraction
% - Modulus, remainder of divison
// - Integer Divison 
'''


'''
str "hello" 'hi' "89"
int 8, 54, -10, 100000
float 5.4, 6.0, 7.5, 4.2, -100.0
bool True, False
'''