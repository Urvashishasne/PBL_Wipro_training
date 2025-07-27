# write a program to check if a number is positive,negetive or zero.
def number_checker(num):
    if num<0:
        print("Number is Negetive")
    elif num==0:
        print("Number is Zero")
    else:
        print("Number is Positive")

# write a program to check if a number is odd or even.
def is_odd_even(num:int):
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")
        
def last_digit(num1:int,num2:int):
    last_digit_num1=num1%10
    last_digit_num2=num2%10
    if last_digit_num1==last_digit_num2:
        return True
    else:
        return False

def print1_10():
    for i in range(1,11):
        print(i,end=" ")

# print even between 23 and 57
def evens():
    for i in range(23,58):
        if i%2==0:
            print(i)

def is_prime(num):
    is_prime=True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
def prime_10_99():
    for num in range(10, 100):
        isprime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                isprime = False
                break
        if isprime:
            print(num)

def sum_digit():
    num = int(input("Enter a number: "))
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num //= 10

    print("Sum of digits:", sum_digits)
    
def reverse_num():
    num = int(input("Enter a number: "))
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reversed number:", reverse)
    

def palindrome():
    num = int(input("Enter a number: "))
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    if original == reverse:
        print(f"{original} is a palindrome.")
    else:
        print(f"{original} is not a palindrome.")