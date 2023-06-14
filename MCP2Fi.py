Number = int(input("enter the number  : "))
n1 , n2 = 0 , 1
i = 0
if  Number<=0 :
    print("Enter a Positive Number")
elif Number==1:
    print ("The fibonacci series is ")
    print(n1)
else:
    while Number < i:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i=i+1