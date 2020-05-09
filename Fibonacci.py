n = int(input("enter the digit="))
if n<0 :
   print("please enter postive number")
elif n>0:
   n1=0
   n2=1
   print(n1,n2)
   while n2<=n:
   	  n3=n1+n2
       	print (n3)
   	   n1=n2
   	   n2=n3
