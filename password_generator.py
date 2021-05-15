import random
import pandas as pd

url = 'https://github.com/rohanmadhale/pass_phrase_generator/blob/main/pass_phrase_words.txt?raw=true'
a_file = pd.read_csv(url)
words = a_file['a'].tolist()

password = [i.capitalize() for i in random.sample(
    [i for i in words if len(i) == random.randint(3,9)], k=3)]
password.append(str(random.randint(1, 9)))
# password[2:4] = [''.join(password[2:4])]
pass_len = 3
for char in password:
    pass_len = pass_len + len(char)
print(f'\nPassword has {pass_len} characters')
print('Your password is : ')
print(*password, sep=('-'))

print('\nYou can check strngth of your password on below websites : ')
print('https://howsecureismypassword.net/')
print('https://www.my1login.com/resources/password-strength-test/')
print('https://password.kaspersky.com/')

