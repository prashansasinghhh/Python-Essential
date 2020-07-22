#Write a number to sum of n number.
num=int(input("Enter the value of n  : "))
sum=0
if num<0:
	print("Enter the Positive Number : ")
else: 
	while num>0:
		sum=sum+num
		num=num-1
	print("The sum of n numbers = ",sum)
