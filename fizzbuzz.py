#Write a function called fizzbuzz that has one parameter n and returns:
#"FizzBuzz" if n is divisible by both 3 and 5
#"Fizz" if n is divisible by 3
#"Buzz" if n is divisible by 5
#The number n as a string if it is not divisible by either 3 or 5
#Arithmetic operator %

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print(fizzbuzz(15)) 