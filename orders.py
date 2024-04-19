def dispatch():
    print("="*44,"Live Orders","="*44)
    print()
    fp=open("orderslist.txt")
    data=fp.readlines()
    fp.close()
    for i in range(len(data)):
        print(data[i])
    while True:
        l=[]
        flag=0
        n=(input("Enter The Order No.: "))
        for i in range(len(data)):
            k=data[i].rstrip().split(",")
            if k[0]==n:
                flag=1
            else:
                l.append(data[i])
        if flag==0:
            print("Invalid Order No., Choose Another Item No.")
            continue
        else:
            #print(l1)
            fp=open("orderslist.txt","w")
            fp.writelines(l)
            fp.close()
            print('-'*25,">>","Order No. ",n," Has Been Dispatched!!!","<<","-"*25)
            break