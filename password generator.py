import string
import random

len=int(input("Enter the length of password you want to generate: "))

alp=string.ascii_letters
nums=string.digits
symbls=string.punctuation

combination=alp+nums+symbls
password=""

for i in range(len):
    next_char=random.choice(combination)
    password+=next_char
print("Your random password is:",password)


