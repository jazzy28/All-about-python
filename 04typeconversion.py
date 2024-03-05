#in python also user inputs in python is in the form of string
#we need to convert them

old_age = input("enter your old age:")
new_age = int(old_age) + 2
print(new_age)

#can convert into float(), str(), bool()

#calculate sum of 2 numbers
a = int(input("enter first number:"))
b = int(input("enter seconf number:"))
sum = a + b #or int(a) + int(b)
print("the sum is:" + str(sum)) #convert back int to str in order to concatenate
