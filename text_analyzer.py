'''
Count total characters, words, and sentences
Count vowels, consonants, digits, and special characters
Convert text to uppercase and lowercase
Check whether a specific word exists in the text
Find frequency of each word
Remove extra spaces from the text

Menu driven
1. Count total characters, words, and sentences
'''

text = input("Enter the paragraph or sentence = ").lower()

while True:
    print("\n-----------Text Analyzer System-------------")
    print("1. Count total characters, words, and sentences")
    print("2. Count vowels, consonants, digits, and special characters")
    print("3. Convert text to uppercase and lowercase")
    print("4. Check whether a specific word exists in the text")
    print("5. Find frequency of each word")
    print("6. Remove extra spaces from the text")
    print("7. Exit")

    choice = int(input("Enter your choice = "))
    match choice:
        case 1:
            total_char = len(text)
            total_word = len(text.split(" "))
            sentence_count = text.count(".") + text.count("!") + text.count("?")
            print("-------------------------------------------------------")
            print("The total char = ",total_char)
            print("The total word = ",total_word)
            print("The sentence = ",sentence_count)
        case 2:
            vowels = 0
            const = 0
            digit = 0
            special_char = 0

            for i in text:
                if i in "aeiou":
                    vowels = vowels + 1
                elif i.isalpha():
                    const = const + 1
                elif i.isdigit():
                    digit = digit + 1
                elif i != " ":
                    special_char = special_char + 1
                
            print("Vowels = ",vowels)
            print("Const = ",const)
            print("Digits = ",digit)
            print("Special Char = ",special_char)
        case 3:
            print("Upper Case = ",text.upper())
            print("Lower Case = ",text.lower())
        case 4:
             word = input("Enter the word to search = ").lower()
             if word in text:
                 print(f"The word {word} is present")
             else:
                # print("The word {} is not present".format(word))
                 print("The word ", word ," is not present")
        case 5:
             frq_word = input("Enter the word to check freq = ").lower()
             words = text.split(" ")
             print("The frequancy is = ",words.count(frq_word))
        case 6:
            pass
        case 7:
            print("Thanks for using our application")
            break
        case _:
            print("Please enter valid the choice between 1 to 7.")