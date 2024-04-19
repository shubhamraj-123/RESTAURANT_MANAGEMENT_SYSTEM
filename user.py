import items
fp=open("customer.txt")
data=fp.read()
fp.close()
def login():
    print("\t\t\t\t-----Customer Page-----")
    print("\t1. New User")
    print("\t2. Existing User")
    print()
    ch=int(input("Enter Choice 1/2: "))   
    if ch==1:
        while True:
            name=input("Enter User Name: ")
            if name in data:
                print("UserName Already Exists")
                continue
            else:
                break
        
        while True:
            password=input("Enter the Password: ")
            l=["!","@","#","$","%","^","&","*",]
            if (len(password)<6 or not any (char.isdigit() for char in password) or (not any (char.isupper() for char in password)) or (not any (char.islower() for char in password)) or (not any(char in l for char in password))):
                print("Password must be atleast 6 characters long, should have atleast one uppercase, lowercase, digit & special character")
                #continue
            # elif not any (char.isdigit() for char in password):
            #     print("At least one digit")
            #     continue
            # elif not any (char.isupper() for char in password):
            #     print("At least one capital character")
            #     continue
            # elif not any (char.islower() for char in password):
            #     print("At least one small character")
            #     continue
            # elif not any(char in l for char in password):
            #     print("At least one special character")
            #     continue
            else:
                print("******Account Created Successfully!******")
                print("="*100)
                print("="*100)
                break
        fp=open("customer.txt","a")
        contents=name+","+password+"\n"
        fp.write(contents)
        fp.close()
        items.itemslist()
        items.orders()
    
    elif ch==2:
        while True:
            name=input("Enter User Name: ")
            if name in data:
                p=input("Enter The Password: ")
                if p in data:
                    print("-"*29)
                    print("---> Login Successful <---")
                    print("-"*29)
                    print("="*100)
                    print("="*100)               
                    break
                else:
                    print("Invalid Password")
                    print("Check Your Password")
                    continue
                
            else:
                print("Name Record Not Found In Data")
                print("Try Again")
                continue
        items.itemslist()
        items.orders()  
       
    else:
         print("Invalid Choice")
