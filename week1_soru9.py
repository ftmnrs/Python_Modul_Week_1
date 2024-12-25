# How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

word = input("Enter a word: ")

# if word == word[::-1] :
#     print(f"{word} is a palindrom.")
# else :
#     print(f"{word} is not a palindrom.")

print(f"{word} is{" not" if word != word[::-1] else ""} a palindrom.")

