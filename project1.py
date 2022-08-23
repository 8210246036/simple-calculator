print ('''
       + ADD
       - SUBTRACT
       * MULTIPLY
       / DIVIDE
                ''')
a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
opr=input("enter the opr..")

if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="*":
    print(a*b)
elif opr=="/":
    print(a/b)
else:
    print("invalid operation")
