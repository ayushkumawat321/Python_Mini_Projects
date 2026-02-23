import random
import string
print("----------------------------------------------")
print("PASSWORD GENERATOR :- ")
print("----------------------------------------------")
len = int(input("Enter length of your Password : "))
str = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(len):
    letter = random.choice(str)
    password +=  letter
print(f"Password : {password}")