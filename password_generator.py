import random

PASS=[['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'],['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
def generate(comb):
    password=""
    L=eval(input("enter the password length:"))
    for i in range(L):
        r=random.choice(comb)-1
        temp=random.choice(PASS[r])
        password+=temp
    return password


while(True):
    print("Welcome to the password generator")
    print("1.Lowercase")
    print("2.Uppercase")
    print("3.'Numbers")
    print("4.Special Characters")
    print("Example \n enter the password combination: 123 (If you need the password only to contain Lowercase, Uppercase and Numbers)")
    combination_s = input("enter the password combination or enter exit to close the application:")
    combination=[]
    if combination_s.lower()=="exit":
        break
    else:
        for i in combination_s:
            if i not in PASS[3]:
                print("Invalid Input")
                break
            else:
                combination.append(int(i))
        print(f"The Generated password is:{generate(combination)}\n\n\n\n\n")