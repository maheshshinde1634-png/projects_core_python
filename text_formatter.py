"""
1. Text Formatter ⭐ (You've already started)
Features
Convert to uppercase
Convert to lowercase
Capitalize
Title case
Swap case
Count characters
Count words
Remove extra spaces
Exit

"""
text = input("enter your text or sentence to format = ")
while True:
    print("\n ---------------------------------------TEXT FORMATTING SYSTEM------------------------------------------")
    print("1. to convert in uppercase ")
    print("2. to convert in lower case ")
    print("3. to convert in capitalize ")
    print("4. to convert in title case ")
    print("5. to convert in swapcase ")
    print("6. to count characters ")
    print("7. to count words ")
    print("8. to remove extra spaces")
    print("9. EXIT")
    print("-"*80)

    choice = int(input("select operation from above = "))
    match choice:
        case 1:
            print(text.upper())
        case 2:
            print(text.lower())
        case 3:
            print(text.capitalize())
        case 4:
            print(text.title())
        case 5:
            print(text.swapcase())
        case 6:
            print(len(text))
        case 7:
            words = text.split()
            print("Total words =", len(words))
        case 8:
            text = " ".join(text.split())
            print("Updated Text:", text)
        case 9:
            print("🙏THANKS FOR USING OUR SYSTEM 😊 ")
            break