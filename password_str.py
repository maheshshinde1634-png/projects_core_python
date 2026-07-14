'''
2. Password Strength Checker

Check

Minimum 8 characters
Uppercase
Lowercase
Number
Special character

Output

Password: Hello@123

Strength : Strong
'''
print("\n----------------------------password strength checker--------------------------")
password = input("enter you password = ") 
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_char = "!@#$%^&*()_+\><~-=.,"

for ch in password :
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_char:
        has_special = True
#step 5 :   
score = 0 
if len(password) >= 8:
    score+=1
if has_upper :
    score+=1
if has_digit:
    score+=1
if has_special:
    score+=1

#step 6
if score <= 2:
    print("password is weak")
elif score == 3:
    print("password is medium")
elif score == 4:
    print("password is strong")
else :
    print("password  is too weak")