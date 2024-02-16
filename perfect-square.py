# Given a positive integer num, write a function that returns True if num is a perfect square else False.

def perfect_square(num):
    root = int(num**0.5)
    return root**2 == num


print(perfect_square(25))
print(perfect_square(19))


