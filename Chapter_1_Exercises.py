# 1.9.1

# Ai could you answer all these questions?
# “What are the bitwise operators in Python?”
# “What is the order of operations in Python?”
# “What are the arguments of the round function?”
# “What is the modulus operator in Python?”

# 1. What are the bitwise operators in Python?
# Bitwise operators in Python allow you to perform operations on individual bits of integer values. Here's a breakdown:
# & (Bitwise AND): Returns 1 if both bits are 1, otherwise 0.
# | (Bitwise OR): Returns 1 if at least one of the bits is 1, otherwise 0.
# ^ (Bitwise XOR): Returns 1 if the bits are different, otherwise 0.
# ~ (Bitwise NOT): Inverts all the bits (0 becomes 1, and 1 becomes 0).
# << (Left Shift): Shifts the bits to the left by a specified number of positions.
# >> (Right Shift): Shifts the bits to the right by a specified number of positions.

#  2. What is the order of operations in Python?
#
# Python follows a specific order of operations, often remembered by the acronym PEMDAS:
#
# Parentheses (or Brackets)
# Exponents (or Orders)
# Multiplication and Division (from left to right)
# Addition and Subtraction (from left to right)

# 3. What are the arguments of the round() function?
#
# The round() function in Python takes two arguments:
#
# number: The number you want to round.
# ndigits (optional): The number of digits to round to.
#
#  If omitted, it rounds to the nearest integer.

# 4. What is the modulus operator in Python?
#
# The modulus operator in Python is represented by the symbol
#
# %. It returns the remainder of a division operation. For example, 10 % 3 would result in 1 because 10 divided by 3 has a remainder of 1.

# 1.9.2

import math
round1 = round(42.5)
print(round1)

round2 = round(43.5)
print(round2)

# 1.9.3

print(2++2)
# Print(4 2)
# ends in error, invalid syntax

round3 = round(42.5)
# print(round3
# Ends in error, needs ")"

print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))

# How many seconds are there in 42 minutes 42 seconds?
s = ((42 * 60) + 42)
print(s)
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
m = 10 / 1.61
# miles
print(f"{m} Miles")
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
s_p_m = s / m
print(f"{s_p_m} seconds per mile")
# What is your average pace in minutes and seconds per mile?
minutes = (s_p_m / 60)
seconds = (s_p_m % 60)
print(f"{int(minutes)} minutes {int(seconds)} seconds per mile")
# What is your average speed in miles per hour?
m_p_h = 60 / minutes
print(f"{m_p_h:.2f} miles per hour")

