import random
letters = ['a','b','c','d','e','f','g','h','i','j','k'
,'l','m','n','o','p','q','r','s','t','u','v','w','x','y'
,'z', 'A','B','C','D','E','F','G','H','I','J','K','L'
,'M','N','O','P','Q','R','S','T','Q','V','W','X','Y','Z']

num = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','?']

print("Welcome To PassWord GeneRator!")
num_letter = int(input("How Many Letter You Like To Enter In PassWord?\n"))
num_num = int(input("How Many NumBer You Like To Enter In PassWord?\n"))
num_symbol = int(input("How Many SymBol You Like To Enter In PassWord?\n"))

password_list = []

for char in range(1, num_letter + 1):
    password_list += random.choice(letters)

for char in range(1, num_num + 1):
    password_list += random.choice(num)

for char in range(1, num_symbol + 1):
    password_list += random.choice(symbol)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your PassWord Is : {password}")
