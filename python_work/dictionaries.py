#Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. 
# Print each key-value pair on a new line.
student_details ={'name':'leticia', 'age':20, 'grade':'A'}
print(student_details['name'])
print(student_details['age'])
print(student_details['grade'])
#Intermediate: Write a function that takes a dictionary of people's names and their ages, 
# {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def names_and_age(details):
     adults = [names for names ,age in  details.items() if age >=21] 
     return adults
details ={'alice' :24 , 'bob':19 ,'charles':30}
adults = names_and_age(details)
print(adults)
#Advanced: Given a dictionary representing items in a store with their price
# s, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought,
# ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
prices = {'apple':0.5,'banana':0.3,'orange': 0.7}
items =['apple', 'orange', 'banana', 'banana']
total_cost = 0
for item in items:
     total_cost+=prices.get(item,0)
     print(total_cost)
 #Challenge: Write a program that counts the occurrences of each word in a given sentence.
 # Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def count_word(sentence):
      words = sentence.lower().split() # we convert the sentence to  lowercase and split it into words
      word_count={} # intialize an empty dictionary to store  word counts
      
      for word in words: # loop through each word in the list of words
            
            word = word.strip(",.?!;:")  # remove any punctuation
      if word in word_count:
           word_count[word]+=1
      else:
           word_count[word] =1
      return word_count
 
 # using the sentence below
sentence = "hello everyonr, hello people, hello world ,my world"
      #call the function and print the result 
result = count_word(sentence)
print(result)




