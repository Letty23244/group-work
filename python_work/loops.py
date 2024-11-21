#no1
# write a python program thta prints all even numbers between 1 and 20 using a for loop
def even_numbers():
    for  even_num in range(2,20,2):
        print(even_num)
even_numbers()
#no2
# use a while loop to ask the user to input a number untill they provide a number greater than 10
number =0
while number <0:
    number =int(input("enter a number:"))
    
    if number >10:
        print(f"enter number greater than 10")
    else:
        print(f"enter number greater than 10")
        
    
# advance : write a program that prints the multiplication table (from 1-10) for numbers from 1to 5 using  the nested loop
def multiplication_table():
    for k in range(1,11):
        print(k,end="\t")
    print() 
multiplication_table()
for j in range(1,11):
    for k in range(1,6) :
        print(j*k, end ="\t")
    print('\n')   
multiplication_table()           
# no 4
#given a list of intergers [4,7,2,9,12,15], wrire aprogram using a for loop to find the sum of all odd numbers and print the result
def sum_of_odd_numbers():
    list = [4,7,2,9,12,15]
    sum = 0
    for num in list:
        if  num % 2!=0:
            sum+=num
    print(f"the  sum of odd numbers is {sum}")
sum_of_odd_numbers()
           
