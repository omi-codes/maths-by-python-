def addition():
  a=eval(input("enter value of first no:")
  b=eval(input("Enter first number:"))
    c=a+b
    print("{}+{}={}".format(a,b,c))
   
def substraction():
    a=eval(input("Enter first number:"))
    b=eval(input("Enter first number:"))
    c=a-b
    print("{}-{}={}".format(a,b,c)) 
 
def multiplication():
    a=eval(input("Enter first number:"))
    b=eval(input("Enter first number:"))
    c=a*b
    print("{}*{}={}".format(a,b,c))
    
def division():
    a=eval(input("Enter first number:"))
    b=eval(input("Enter first number:"))
    c=a/b
    print("{}/{}={}".format(a,b,c)) 
print("Select option: \n 1 for addition\n 2 for substration \n 3 for multiplication \n 4 for division")
option=int(input("Enter option given in above:"))
if option==1:
	addition()
elif option==2:
	substraction()
elif option==3:
	multiplication()
elif option==4:
	division()
