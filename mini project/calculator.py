print("welcome to my calculator")
print("select the operation that you want to perform")
print("1)Addition")
print("2)Subtraction")
print("3)Multiplication")
print("4)Division")
print("5)Modulus operation")
print("6)Exponential operation")
n=int(input())
a=int(input("enter first number:"))
b=int(input("enter second number:"))
while(True):
  if(n==1):
    print(f"sum is {a+b}")
    break
  if(n==2):
    print(f"difference is {a-b}")
    break
  if(n==3):
    print(f"multiplication is {a*b}")
    break
  if(n==4):
    print(f"division is {a//b}")
    break
  if(n==5):
    print(f"remainder is {a%b}")
    break
  if(n==6):
    print(f"power is {a**b}")
    break
  else:
    print("sorry you typed something else")
    break
print("thanks for using the calculator")