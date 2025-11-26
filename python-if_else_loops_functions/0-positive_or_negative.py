#!/usr/bin/python3
"""
Random Number Sign Checker

This script generates a random integer between -10 and 10
and prints whether the number is positive, negative, or zero.
"""

import random

# Generate a random number
number = random.randint(-10, 10)

# Print whether it's positive, negative, or zero
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

print("\n---\n")

# Readme-style output
print("# Random Number Sign Checker\n")
print(
    "This Python script generates a random integer between -10 and 10 "
    "and prints whether the number is positive, negative, or zero.\n"
)
print("## How to Run\n")
print("```bash\npython3 number_sign.py\n```\n")
print("## Example Output\n")
print("```\n7 is positive\n-3 is negative\n0 is zero\n```\n")
print("## Requirements\n- Python 3.x\n- Standard Python library (no extra packages needed)")
