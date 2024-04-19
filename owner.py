import items
import orders
def viewlist():
    #if choice=="y":
        while 1:
            print("\n-----------What do You Want to do?-----------\n")
            print("\t\t\t1. Update Items List")
            print("\t\t\t2. Dispatch Order")
            print("\t\t\t3. View The Items List")
            print("\t\t\t4. Close")
        
   
            choice=int(input("Enter The Choice:"))
            if choice==1:
                items.update()
            if choice==2:
                orders.dispatch()
            if choice==3:
                items.itemslist()
                print()
            if choice==4:
                print("Thank You!")
                break
            # if choice!="y":
            #     print("Thank You!")
            #     break
        else:
            print("invalid Choice")

    
    