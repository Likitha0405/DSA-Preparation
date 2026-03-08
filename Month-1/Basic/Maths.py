# 1.count digits in a number
n = 12345
digits = 0
while n>0:
    digits += 1
    n = n//10
print(digits)

# edge case if n = 0
n = 0
digits = 0
if n == 0:
    digits = 1
else:
    while n:
        digits += 1
        n = n//10
print(digits)

# function 
def count_digits(n):
    cnt = 0
    while n>0:
        cnt += 1
        n = n//10
    return cnt
print("the digits are",count_digits(7890))

# 2. reverse a digit of a number
def reverse_digit(n):
    rev_no = 0
    while n>0:
        last_digit = n%10
        n=n//10
        rev_no = rev_no*10 + last_digit
    return rev_no
print("the reversed number is",reverse_digit(123))
print("the reversed number is",reverse_digit(9870))