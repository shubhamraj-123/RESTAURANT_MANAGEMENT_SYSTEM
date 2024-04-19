import random
import owner
def itemslist():
    with open("items.txt","r") as fp:
        print("\t\t\t\t\t!! Items list !!")
        print("="*100 )
        contents = fp.readlines()
        for i in contents:
            print(i.rstrip())
    fp.close()
def orders():
    fp=open("items.txt")
    data=fp.readlines()
    fp.close()
    amount=0
    list=[]
    l1=["Order No.: ",""]
    list.append(l1)
    while(True):
        print()
        n=input("Choose Your Dish No.: ")
        q=int(input("Enter The Quantity: "))
        
        for i in data:
            i=i.rstrip().split(",")
            if i==['No.', 'Dish', 'Price']:
                pass
            elif n==i[0]:
                inner=[]
                inner.append(i[1])
                inner.append(q)
                list.append(inner)
                amount+=int(i[2])*q
        ch=input("Hit y to Choose Another Dish: ")
        if ch=="y":
            continue
        else:
            break
    print()
    print("="*50,"Your order","="*50)
    print()
    r=str(random.randint(11,99))+str(random.randint(11,99))
    list[0][1]=r
    for i in range(len(list)):
        if i==0:
            list[i]=tuple(list[i])
            m,n=list[i]
            print(m,n)
            print()
        else:
            print(list[i][0],list[i][1])
            print()

    print(f"-"*40,">>>>","Total Amount: Rs.",amount,"<<<<","-"*40)
    print()
    c=input("Enter 'y' For Confirm Your Order: ")
    print()
    if c!="y":
        print(""*25,"Thank You! Relogin For A New Order!",""*25)
        print()
    else:
        print(""*15,"Congrats! Order Received! Visit Again. ",""*15)
        print()
        data=""
        for i in range(len(list)):
            if i==0:
                pass
            else:
                data+=list[i][0]+" "+str(list[i][1])+","
        order=r+","+data+"\n"
        fp=open("orderslist.txt","a")
        fp.write(order)
        fp.close()
        # function for update,add,delete the orders list.
def update():
    print("*"*100)
    print("\t\t\t1.Add a new item")
    print("\t\t\t2.Delete an item")
    print("\t\t\t3.Update the price")
    #print("Enter 4 to Go to previous ")
    ch=int(input("Enter choice to choose 1/2/3: "))
    fp=open("items.txt")
    data=fp.readlines()
    fp.close()
    if ch==1:
        while True:
            flag=0
            num=(input("Enter The Item No.: "))
            for i in data:
                i=i.rstrip().split(",")
                if i[0]==num:
                    flag=1
                    break
            if flag==1:
                print("Item No. already exists, Choose Another Item No.")
                continue
            else:
                name=input("Enter The Item Name: ")
                price=input("Enter The Item Price: ")
                #l=[]
                fp=open("items.txt","a")
                content=num+","+name+","+price+"\n"
                #l.append(content)
                #fp=open("items.txt","a")
                fp.writelines(content)
                fp.close()
                print("-"*25,">>","Item added successfully!!","<<","-"*25)
                #fp.close()
                break
    elif ch==2:
        while True:
            flag=0
            num=(input("Enter The Item No.: "))
            for i in range(len(data)):
                k=data[i].rstrip().split(",")
                if k[0]==num:
                    data[i]=""
                    flag=1
            if flag==0:
                print("Invalid Item No. Choose Another Item No.")
                continue
            else:
                print("-"*25,">>","Item deleted successfully","<<","-"*25)
                fd=open("items.txt","w")
                fd.writelines(data)
                fd.close()
                break
    elif ch==3:
        while True:
            flag=0
            num=input("Enter The Item No.: ")
            for i in range(len(data)):
                k=data[i].rstrip().split(",")
                if k[0]==num:
                    value=input("Enter The Updated Price Of The Item: ")
                    data[i]=k[0]+","+k[1]+","+value+"\n"
                    flag=1
            if flag==0:
                print("Invalid Item No. Choose Another Item No.")
                continue
            else:
                print("-"*25,">>","Price Updated Successfully","<<","-"*20)
                fp=open("items.txt","w")
                fp.writelines(data)
                fp.close()
                break
    #owner.viewlist()
    elif ch==4:
        owner.viewlist()

        
        
