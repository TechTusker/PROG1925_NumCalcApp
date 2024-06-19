def option1():
    n=int(input("Enter number:"))
    add=0
    add1=0
    i=0
    b=0
    c=0
    j=0
    y=[]
    g=[]
    for i in range(0,20):
        n=n+1
        y.append(n) 
    print(y)
    for j in range(0,20):
        if(y[j]%2==0):
            b=y[j]*3
            g.append(b)
            add=add+g[j]
        else:
            c=y[j]*4
            g.append(c)
            add1=add1+g[j]
    print(g)
    print("Sum=",add+add1)
def option2():
    m=0
    n=0
    while(True):
        n=input("Enter value:")
        if(n.strip().isdigit()):
            m=int(n)/3
            print("value:",m)
        else:
            if(n=="end"):
                break
a=0
b=0
while(a<=2):
    print("press 1 for option 1")
    print("press 2 for option 2")
    print("press 3 for Exit")
    b=int(input("Enter your choice:"))
    if(b==1):
        option1()
    elif(b==2):
        option2()
    else:
        print("you have exited program")
        break 
