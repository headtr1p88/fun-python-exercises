#Write a program that calculates the compound interest on an investment
#Prompt the user for the investment amount, interest rate, number of times interest is compounded per year, and the investment duration
#Formula: A = P(1 + r/n)^nt
#P = Principal    r = Interest rate (Decimal)    n = times compounded per year    t = years

def compound_interest(p, r, n, t):
    return p * (1 + r / n) ** (n * t)

principal = float(input('Enter the investment amount: '))
rate = float(input('Enter the interest rate: '))
rate /= 100
compound_num = int(input('Enter the number of times interest is compounded per year: '))
years = float(input('Enter the number of years: ')) 

total = compound_interest(principal, rate, compound_num, years)
total = round(total, 2)

print(f'Your investment will be worth ${total} after {years} years')