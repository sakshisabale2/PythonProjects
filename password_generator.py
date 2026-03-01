import random
import string

passLength = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# print(charValues)

password = ""
for i in range(passLength):
    password += random.choice(charValues)

print("Your random password is: ", password)    