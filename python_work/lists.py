# no1
# create a list of  5 fruits and print each fruit on a new line

fruits=['orange','apple','mango','grape','lemon']
for fruit in fruits:
      print(fruit)
      
#n02) create a function that takes a list of numbers and results a new list with each number squared
#example[1,2,3] should become[1,4,9]
def squared_numbers():
      squared_numbers =[]
      numbers =[1,2,3]
      for num in numbers:
            squared_numbers.append(num**2)
      return squared_numbers
result =squared_numbers() 
print(result)     

#no3) write a python program that takes two lists , list1=[1,2,3] and list2=[4,5,6] and combines them into a single list
#combines =[1,4,2,5,3,6]
def lists():
    list1 =[1,2,3,]
    list2 =[4,5,6]
    combined =[]

    for A in  range (len(list1)):
      combined.append(list1[A])
      combined.append(list2[A])
      print(combined)
      
lists()



#no4) Given alist of numbers [3,1,4,1,5,9,2] write a program that finds and prints the largest number without using the max function.
def largest_number():
      y =[3,1,4,1,5,9,2]
      
      largest = second_largest =float('-inf')
      for value in y:
            if value > largest:
                  
                  second_largest = largest
                  largest =value
            elif value > second_largest and value != largest:
                  largest = value

      print(largest)
      print(second_largest)

     
     