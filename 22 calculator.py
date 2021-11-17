##making library

a = int(input("enter first number:- "))
print("+ to add, - to subtract, / to divide, * to multiply")
c = input("enter the operation you want to do:- ")
b = int(input("enter second number:- "))

if(c ==  '+'):
    sum = a+b
    print("your sum is ", (sum))
else: pass

if(c == '-'):
    dif = a-b
    print("your diffrence is ", (dif))
else: pass

if(c == '/'):
    div = a/b
    print("your quotint is ", (div))
else: pass

if(c == '*'):
    multi = a*b
    print("your product is ", (multi))
else: pass