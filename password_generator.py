#Create a program that generates a random password with:
#uppercase, lowercase, numbers, and special characters
#User specifies length
#Hint: Use the string and random modules
import string
import random

def generate_password(length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    char_list = [random.choice(char_set) for _ in range(length)]
    password = ''.join(char_list)
    return password

pass_length = int(input('Enter the password length: ')) 

for _ in range(10): 
    print(generate_password(pass_length))
