# def itemslist():
#     fp =open('items.txt','r')
#     print(fp.read())
#     # val = fp.readlines()
#     # for i in val:
#     #     #print(i.rstrip(","))
#     #     print(i.strip())
#     fp.close()
# itemslist()
#while True:
    
            #password=input("Enter the Password: ")
          # print("Password must be atleast 6 char long,shhould be")
#             password=input("Enter the Password: ")
#             if (len(password)>=6):
#                 for i in password:
#                     if i.isdigit():
#                         opt1='ok'
#                     elif i.islower():
#                         opt2='ok'
#                     elif i.isupper():
#                         opt3='ok'
#                     elif i in '!@#$%^&*':
#                         opt4='ok'
#                 if opt1=='ok' and opt2=='ok' and opt3=='ok' and opt4=='ok':
#                     print("Account created successfully")
#                     break
        
#             else:
#                 print("Invalid")
#                 break
                          
# while True:
#     print("Password must be atleast 6 characters long, should have atleast one uppercase, lowercase, number and special character")
#     password=input("Enter password:")
#     opt1=0
#     opt2=0
#     opt3=0
#     opt4=0
#     if(len(password)>=6):
#         for i in password:
#             if i.isdigit():
#                 opt1='ok'
#             if i.islower():
#                 opt2='ok'
#             if i.isupper():
#                 opt3='ok'
#             if i in '!@#$%^&*_+=-':
#                 opt4='ok'
#         if opt1=='ok' and opt2=='ok' and opt3=='ok' and opt4=='ok':
#             print("******Account created Successfully******")
#             break  # valid
#         else:
#             print("Invalid")
#             print("Check Your Password")
#             continue #not valid
                
#     else:
#         print("Invalid ")
#         continue 
# fp=open("items.txt")
#     details=fp.readlines()
#     fp.close()
#     bill=0
#     list=[]
#     l1=["orderno: ",""]
#     list.append(l1)
#     while(True):
#         number=int(input("choose your dish no: "))
#         quantity=int(input("enter the quantity: "))
        
#         for i in details:
#             i=i.rstrip().split(",")
#             if i==['no', 'dish', 'price']:
#                 pass
#             elif number==int(i[0]):
#                 inner=[]
#                 inner.append(i[1])
#                 inner.append(quantity)
#                 list.append(inner)
#                 bill+=int(i[2])*quantity
#         ch=input("hit a to add more items to order: ")
#         if ch=="a":
#             continue
#         else:
#             break
#     print()
#     print(""*50,"Your order",""*50)
#     xz=random.randint(1,20)+random.randint(21,40)
#     list[0][1]=xz
#     for i in range(len(list)):
#         if i==0:
#             list[i]=tuple(list[i])
#             a,b=list[i]
#             print(a,b)
#             print()
#         else:
#             print(list[i][0],list[i][1])
#             print()

#     print(f"-"*45,">","Total Amount: Rs.",bill,"<","-"*45)
#     print()
#     cnf=input("Enter y to confirm your order: ")
#     print()
#     if cnf!="y":
#         print(""*25,"Thank you Relogin again!!",""*25)
#         print()
#     else:
#         print(""*15,"We received your order, order will be delivered soon! Thank you Visit agin! ",""*15)
#         print()
#         xz=str(xz)
#         details=""
#         for i in range(len(list)):
#             if i==0:
#                 pass
#             else:
#                 details+=list[i][0]+" "+str(list[i][1])+","
#         order=xz+","+details+"\n"
#         fp=open("orderslist.txt","a")
#         fp.write(order)
#         fp.close()
def dispatch():
    print("="*40,"Live Orders","="*40)
    fp=open("orderslist.txt")
    details=fp.readlines()
    fp.close()
    for i in range(len(details)):
        print(details[i])
    while True:
        l1=[]
        flag=0
        inp=(input("Enter The Order No.: "))
        for i in range(len(details)):
            k=details[i].rstrip().split(",")
            if k[0]==inp:
                flag=1
            else:
                l1.append(details[i])
        if flag==0:
            print("The order number do not exist choose another item number")
            continue
        else:
            #print(l1)
            fp=open("orderslist.txt","w")
            fp.writelines(l1)
            fp.close()
            print('-'*20,"Order number ",inp," dispatched!!!","-"*20)
            break
dispatch()