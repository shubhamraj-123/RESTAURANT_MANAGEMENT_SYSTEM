import user
import owner
print("----- "+"\U0001F60B "+"WELCOME TO THE YUMMY RESTAURANT APP"+" \U0001F60B"+" -----")
print()
print("Login Type:")
print()
print("\t1. Customer")
print("\t2. Restaurant Owner")
print()
choice=int(input("Enter Your Choice 1/2: "))
print("="*100)
print()
if choice==1:
    user.login()
elif choice==2:
    password=input("Enter Password :")
    p="Restaurant@456"
    while(password!=p):
        print("Invalid")
        password=input("Enter Password:")
    if p==password:
        print()
        print("*-"*5,"Logged In Successfully","-*"*5)
    owner.viewlist()
else:
    print("Invalid choice")    