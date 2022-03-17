import re
import os 
import time

EmailId = []
Password =[]

def LoadData():
    dataFile = open("data.txt","r")
    for line in dataFile:
        lineSplitter = line.split()
        EmailId.append(lineSplitter[0])
        Password.append(lineSplitter[1])
    dataFile.close()

def Registration():
    
    LoadData()
    os.system("clear")
    dataFile = open("data.txt","a")
    print("Registration Page")
    print("Enter Your EmailId")
    while(True):
        inputMailId=input()
        regex = "[A-Za-z0-9]{3,}@[A-Za-z]{3,}[.][A-Za-z]{2,}"
        if (not (re.fullmatch(regex,inputMailId))):
            print("\nEnter Valid EmailId")
            continue
        else:
            specialSym = ['$','@','#','%','!','&','(',')','*','^']
            os.system("clear")
            print("Enter Your Password")
            while(True):
                pwd = input()
                if (not (6<=len(pwd)<=15)):
                    print("Password Length Must be 6 to 15\n")
                    print("Enter Valid Password")
                    continue
                if not(any(char.isdigit() for char in pwd)):
                    print("Password should contain atleast one digit\n")
                    print("Enter Valid Password")
                    continue
                if not(any(char.isupper() for char in pwd)):
                    print("Password should contain atleast one Uppercase\n")
                    print("Enter Valid Password")
                    continue
                if not(any(char.islower() for char in pwd)):
                    print("Password should contain atleast one Lowercase\n")
                    print("Enter Valid Password")
                    continue
                if not(any(char in specialSym for char in pwd)):
                    print("Password should contain atleast one Special Character\n")
                    print("Enter Valid Password")
                    continue
                else:
                    dataFile.write("\n")
                    dataFile.write(inputMailId)
                    dataFile.write(" ")
                    dataFile.write(pwd)
                os.system("clear")
                print("Registration Successful")
                break
        break
    dataFile.close()
    
def Login():
    
    LoadData()
    os.system("clear")
    print("Login Page")
    print("Enter EmailId")
    inputMailId = input()
    print("\nEnter Password")
    pwd = input()
    if inputMailId in EmailId:
        index = EmailId.index(inputMailId)
        if Password[index] == pwd:
            os.system("clear")
            print("Login Successful")
            return
        else:
            os.system("clear")
            print("Password MisMatch")
            print("Choose '1' for New Registration ")
            print("Choose '2' for Forget Password")
            choice = input()
            
            if choice=='2':
                forgetPassword(inputMailId)
                return
    else:
        os.system("clear")
        print("Email Id Not registered")
        print("Redirecting To Registration Page...")
        time.sleep(2)
    Registration()

def forgetPassword(inputMailId):
    os.system("clear")
    index = EmailId.index(inputMailId)
    print("\nYour Password is",Password[index])

print("Login Page")
print("Enter '1' For New Registration")
print("Enter '2' For Login")
choice = input()

if choice == '1':
    Registration()
    
elif choice == '2':
    Login()
    
else:
    print("Invalid Input")
