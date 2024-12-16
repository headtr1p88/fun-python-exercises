#Write a function that checks if a string is a palindrome - racecar, madam, No lemon, no melon

def palindrome_check(word):
    clean_string = [x.lower() for x in word if x.isalnum()]
    clean_string = ''.join(clean_string)
    return clean_string == clean_string[::-1]

print(palindrome_check('No lemon, no melon')) 