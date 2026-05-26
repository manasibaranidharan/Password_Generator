import random
letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+','@']

print("WELCOME TO THE PERSONAL PyPASSWORD GENERATOR!")
nr_letters = int(input("How many letters would you like in your password?:"))
nr_numbers = int(input("How many number would you like in your password?:"))
nr_symbols = int(input("How many symbols would you like in your password:"))

n=int(input("Do you want an ordered password(1) or a mixed password(2)?:"))
if n==1:
    
    #Easy Level (letters, numbers and symbols are in order)

    print("\nOutput using random.sample() function and .join() function")
    print("".join(random.sample(letters, nr_letters) + random.sample(numbers, nr_numbers) + random.sample(symbols, nr_symbols)))

    print("\nOutput using for loop, range, and random.choice() function")
    password=""
    for i in range(0, nr_letters):
        password+=random.choice(letters)
    for i in range(0, nr_numbers):
        password+=random.choice(numbers)
    for i in range(0, nr_symbols):
        password+=random.choice(symbols)

    print(password)

if n==2:
    #Hard Level (letters, numbers and symbols are mixed here)

    password_list=[]
    for i in range(0, nr_letters):
        password_list.append(random.choice(letters))
    for i in range(0, nr_numbers):
        password_list.append(random.choice(numbers))
    for i in range(0, nr_symbols):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    print("".join(password_list))