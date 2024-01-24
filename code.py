#length of string without using len function
a=input('Enter string: ')
count=0
for i in a:
    count+=1
print('The length of the string is', count)

#extracting email before @ is given
a=input('Enter string: ')
pos=a.index('@')
print(a[:pos])

#frequency of the character in astring
a=input('Enter string: ')
term=input('Enter term for the search: ')
count=0
for i in a:
    if i==term:
        count+=1
print("Frequency",count)

#removing particular character from string
a=input('Enter string: ')
term=input('Enter term for the removal: ')
result=''
for i in a:
    if term!=i:
        result=result+i

print(result)

#if the string is palindrome or not
a=input('Enter string: ')
flag=True
for i in range(0,len(i)//2):
    if a[i]!=a[len[s]-i-1]:
        flag=False
        print('Not a palindrome')
if flag:
        print("It's a palindrome.")

#storing wodrs of string without using split fun(), the if loop won't work on last word of the string because it doesn't have space so using append at last

a=input('Enter string: ')
temp=''
L=[]
for i in a:
    if i!=' ':
        temp+=i
    else:
        L.append(temp)
        temp=''
L.append(temp)
print(L)

#string to title case without using title function
a=input('Enter string: ')
L=[]
for i in a.split():
    L.append(i[0].upper()+i[1:].lower())
print(" ".join(L))

#Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
"""5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1"""
rows=5

for i in range(0,rows):
    for j in range(rows-i,0,-1):
        print(j,end=' ')
    print( )



#Print the following pattern.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
rows=int(input('Enter rows: '))

for i in range(1,rows+1,1):
    for j in range(0,i):
        print('*',end=' ')
    print( )

for i in range(1,rows+1):
    for j in range(rows-i,0,-1):
        print('*',end=' ')
    print( )

#Write a program to print the following pattern
''''
    *
   * *
  * * *
'''
rows=int(input('Enter rows: '))
for i in range(1,rows+1):
    print(" "*rows,end='')
    print("* "*i)
    rows-=1


#Write a program to print the following pattern
'''
1

2 1

3 2 1

4 3 2 1

5 4 3 2 1
'''

rows=int(input('Enter rows: '))
for i in range(rows+1,0):
    for j in range(i,0,-1):
        print(j,end=' ')
    print( )

#Write a Python Program to Find the Sum of the Series till the nth term:
#1 + x^2/2 + x^3/3 + … x^n/n
#n will be provided by the user
n=5
x=10
s=''
sum=1

print('1 + ',end='')
for i in range(2,n+1):
    sum+=x**i/i
    s=s+ f'x^{i}/{i} +'
print(s[:-1])
print(sum)

#The natural logarithm can be approximated by the following series.
#If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.
x=10
n=5
s=' '
sum=0
for i in range(1,n+1):
    sum+=(1/i)*((x-1)/x)**i
    s=s+f'(1/{i})*((x-{i})/x)**{i}  +'
print(s[:-1])
print(sum)

#Find the sum of the series upto n terms.
#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.
#output=5 and input=2+22+222+2222+22222 Sum of  series is: 24690

start=2
sum=0
stop=0
n=int(input('Enter n: '))
for i in range(0,n):
    if i<n-1:
        print(start,end='+ ')
    else:
        print(start)
    sum+=start*10+2
    start=start*10+2

print(sum)

#Write a program to print all the unique combinations of 1,2,3 and 4
#Output:1 2 3 4,1 2 4 3,1 3 2 4,1 3 4 2,1 4 2 3,1 4 3 2,..and so on
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                print(i,j,k,l)

#Write a program that will take a decimal number as input and prints out the binary equivalent of the number

n=int(input('Enter number: '))
binary=[]
while n>0:
    binary.append(n%2)
    n=n//2
for i in binary[::-1]:
    print(i,end='')

#Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

greater=0
x=int(input('Enter first number: '))
y=int(input('Enter second number: '))
if x>y:
  greater=x
else:
  greater=y
while True:
  if (greater%x==0) and (greater%y==0):
    lcm=greater
    break
  else:
    greater+=1
print(lcm)

#hcf or gcd
smaller=0
x=int(input('Enter 1 number: '))
y=int(input('Enter 2 number: '))
if x<y:
  smaller=x
else:
  smaller=y
for i in range(1,smaller+1):
  if (x%i==0) and (y%i==0):
    hcf=i
print(hcf)

#Create Short Form from initial character Given a string create short form ofthe string from Initial character. Short form should be capitalised.
#Input:Data science mentorship program Output:DSMP
a=input('Enter string: ').split( )
b=[(i[0]).upper() for i in a]
print(''.join(b))

#Append second string in the middle of first string Input:campusx,data and Output:camdatapusx
a=input('Enter string one: ')
b=input('Enter string second: ')
mid=len(a)//2
print(''.join(a[:mid]+b+a[mid:]))

#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.Given:str1 = PyNaTive Expected Output:yaivePNT
a=input('Enter string: ')
lowercase=[c for c in a if c.islower()]
uppercase=[c for c in a if c.isupper()]
result=''.join(lowercase+uppercase)
print(result)

#Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.Input: hel123O4every093 ,Output:Sum: 22 Avg: 2.75

a=input('Enter alphanumeric string: ')
sum=0
count=0
for i in a:
    if i.isdigit():
        sum+=int(i)
        count+=1
print(sum)
print('avg:',sum/count)

#Removal of all characters from a string except integers Given:str1 = 'I am 25 years and 10 months old' Expected Output:2510
s=input('Enter string to remove ch: ')
a=''
for i in s.split( ):
    if i.isdigit():
        a+=i      
print(a)

#Check whether the string is Symmetrical. Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.Input khokho Output The entered string is symmetrical
s=input('Enter string: ')
mid=len(s)//2
first_half=(s[:mid])
second_half=(s[mid:])if len(s)%2==0 else s[mid+1:]
if first_half==second_half:
    print('Yes')
else:
    print('No')

#Reverse words in a given String Statement: We are given a string and we need to reverse words of a given string. Example 1:Input:geeks quiz practice code. Output: code practice quiz geeks
s=input('Enter string: ').split( )
a=[]
for i in s:
    a.append(i)
print(" ".join(a[::-1]))

#Find uncommon words from two Strings.Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.Input:A = "apple banana mango" B = "banana fruits mango" Output:['apple', 'fruits']
a="apple banana mango".split(" ")
b="banana fruits mango".split(" ")
s=[word for word in a if word not in b and a] + [i for i in b if i not in a and b]
print(s)

#Word location in String.
# Statement: Find a location of a word in a given sentence.

s='We can learn data science through campusx mentorship program.'
word ='campusx'
for i in s.split( ):
    res+=1
    if i==word:
        break
print(res)



#Write a program that can remove all the duplicate characters from a string. User will provide the input.
s=input('Enter string: ')
result=''
for i in s:
    if i not in result:
        result+=i
print(result)

 #Combine two lists index-wise(columns wise) Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list. 
list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]
list3=[[i,j] for i,j in zip(list1, list2)]
print(list3)

#Add new item to list after a specified item Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


#Update no of items available
#Suppose you are given a list of candy and another list of same size representing no of items of respective candy.
#Write a program to show no. of items of each candy type.
#Output:Jelly Belly-10,Kit Kat-20,Double Bubble-34,Milky Way-74,Three Musketeers-32
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
c_l=[]
for i,candy in enumerate(candy_list):
    c_l.append(f"{candy}:{no_of_items[i]}")
print(c_l)# or use zip function as well.
for (i,j) in zip(candy_list, no_of_items):
        print(i,'-',j)


#Running Sum on list. Write a program to print a list after performing running sum on it.Output:[1,3,6,10,15,21]
list1 = [1,2,3,4,5,6]
s=[]
j=0
for i in list1:
    j+=i
    s.append(j)
print(s)

#You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].[22,20,16,10,23]
l1=[2,4,6,10,1]
k=[]
for i in l1:
    sum=0
    for j in l1:
        if i<=j:
            sum+=j
    k.append(sum)
print(k)  

# Find list of common unique items from two list. and show in increasing order
num1 = [23,45,67,78,89,34,67]
num2 = [34,89,55,56,39,67,67]
s=[]
for i in num1:
    if i in num2:
        if i not in s:
            s.append(i)
s.sort()
print(s)

#Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
lst1=['1ac21', '23fg', '456', '098d','1','kls']
prod_val=[]
for i in lst1:
    product=1
    for ch in i:
        if ch.isdigit():
            product*=int(ch)
    prod_val.append(product)
print([i[1] for i in sorted(list(zip(prod_val,lst1)),reverse=True)])

#Split String of list on K character.Output:['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']

lst=['CampusX is a channel', 'for data-science', 'aspirants.']
s=[]
for words in lst:
    s.extend(words.split(' '))
    
print(s)

#Convert Character Matrix to single String using string comprehension.

a=[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
print(" ".join(["".join(i)for i in a]))

#Add Space between Potential Words.

a=['campusxIs', 'bestFor', 'dataScientist']
s=[]
for i in a:
    temp=[[]]
    for j in i:
        if j.isupper():
            temp.append([])
        temp[-1].append(j)
    temp_string=" "
    for i in temp:
        temp_string=temp_string+ "".join(i)+" "
    s.append(temp_string[0:-1])
print(s)

    

#Write a program that can perform union operation on 2 lists[1,2,3,4,5,7,8]
a=[1,2,3,4,5,1]
b=[2,3,5,7,8]
s=[]
for i in a:
    if i not in s :
        s.append(i)
for i in b:
    if i not in s :
        s.append(i)
print(s)

#Write a program that can find the max number of each row of a matrix [3,6,9]
a=[[1,2,3],[4,5,6],[7,8,9]]
s=[]
for i in a:
    s.append(max(i))
print(s)

# Write a list comprehension to print the following matrix
a=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#j+3*i is formula always works for finding elements of matrix.
s=[[j+3*i for j in range(3)] for i in range(3)]
print(s)

#Write a list comprehension that can transpose a given matrix
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

s=[[rows[i] for rows in matrix] for i in range(len(matrix))]
print(s)

#Write a list comprehension that can flatten a nested list
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
a=[items for rows in matrix for items in rows]
print(a)

#Join Tuples if similar initial element
#While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.
Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
unique=[]
for i in test_list:
    unique.append(i[0])
unique=set(unique)
result=[]
for i in unique:
    result.append([i])
    for j in test_list:
        if i==j[0]:
            result[-1].append(j[1])
print(list(map(tuple,result)))

#Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
#Resultant tuple after multiplication : 
#(1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)
l=(1, 5, 7, 8, 10)
L=[]
L.append(l[0]*l[1])
for i in range(1,len(l)-1):
    L.append((l[i]*l[i-1])+(l[i]*l[i+1]))
L.append(l[-1]*l[-2])
print(tuple(L))

#Check is tuples are same or not?Two tuples would be same if both tuples have same element at same index
t1 = (1,2,3,0)
t2 = (0,1,2,3)
flag=True
for i,j in zip(t1,t2):
    if i==j:
        continue
    else:
        flag=False
        break
if flag:
    print(' same')
else:
    print('Not same')

#Count no of tuples, list and set from a list
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
output=[0,0,0]
for i in list1:
    if type(i)==list:
        output[0]+=1
    elif type(i)==set:
        output[1]+=1
    elif type(i)==tuple:
        output[2]+=1
print(f"List: {output[0]}, Set: {output[1]}, Tuple: {output[2]}")


#Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.Show every students record in form of tuples if matches all required criteria.It is assumed that there will be only one primry skill.If no such candidate found, print No such candidate
'''Enter No of records- 2
Enter Details of student-1
Enter Student name- Manohar
Enter Higher Education- B.Tech
Enter Primary Skill- Python
Enter Year of Graduation- 2022
Enter Details of student-2
Enter Student name- Ponian
Enter Higher Education- B.Sc.
Enter Primary Skill- C++
Enter Year of Graduation- 2020

Enter Job Role Requirement
Enter Skill- Python
Enter Higher Education- B.Tech
Enter Year of Graduation- 2022'''

'''students=[]
no_of_participant=int(input('Enter the number of participants: '))
for i in range(no_of_participant):
  print('Enter the details of',i+1,'participant.')
  name=input('Enter name: ')
  h_ed=input('Enter higher education: ')
  p_skill=input('Enter primary skill: ')
  y_o_g=input('Enter year of graduation: ')
  students.append((name,h_ed,p_skill,y_o_g))
print('Enter job requirements:-')

flag=False

required_skill=input('Enter skill: ')
required_h_ed=input('Enter higher education: ')
required_y_o_g=input('Enter year of graduation: ')
for i in students:
  if required_skill==i[2] and required_h_ed==i[1] and required_y_o_g==i[3]:
    print(i)
    flag=True
if flag==False:
    print('NO such participant.')'''

#Write a program to find set of common elements in three lists using sets.
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1=set(ar1)
s2=set(ar2)
s3=set(ar3)
print(list((s1.intersection(s2)).intersection(s3)))

#Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
Str1="hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
s=set(Str1)
vowels=set('aeiouAEIOU')
print('No of unique vowels used in this sentence are:',len(s.intersection(vowels)))

#Write a program to Check if a given string is binary string of or not.A string is said to be binary if it's consists of only two unique characters.
a=input('Enter string: ')
if len(set(a))==2:
    print('Binary')
else:
    print('No it is not binary')

#find union of n arrays.
a=[[1, 2, 2, 4, 3, 6],
[5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
s=set()
for i in a:
    s.update(i)
print(s)

#Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
print(list(lst1.intersection(lst2)))

#Key with maximum unique values Given a dictionary with values list, extract key whose value has most unique values.
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
max_val=0
max_key=''
for i in test_dict:
    if max_val<len(set(test_dict[i])):
        max_val=len(set(test_dict[i]))
        max_key=i
print(max_key)

#Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
s=[]
for i in test_str.split( ):
  if i in repl_dict:
    s.append(repl_dict[i])
  else:
    s.append(i)
print(' '.join(s))

#Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]
s=[]
n=len(test_list)
for i in range(0,n,2):
    s.append({key_list[0]:test_list[i],key_list[1]:test_list[i+1]})
print(s)

#Convert a list of Tuples into Dictionary.
l=[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
s={}
for i,j in l:
    s[i]=[j]
print(s)

# Sort Dictionary key and values List.
a={'c': [3], 'b': [12, 10], 'a': [19, 4]}
res={}
for i in sorted(a):
    res[i]=sorted(a[i])
print(res)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
a=[1,2,3,3,3,3,4,5]
def unique(l):
  s=[]
  for i in l:
    if i not in s:
      s.append(i)
  return s
a=[1,2,3,3,3,3,4,5]
print(unique(a))

#Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.
#input=green-red-yellow-black-white
l='green-red-yellow-black-white'
def hypen_sort(l):
  s=[]
  for i in sorted(l.split('-')):
     s.append(i)
  
  return "-".join(s)

print(hypen_sort(l))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
a='CampusX is an Online Mentorship Program fOr EnginEering studentS.'

def up_low(s):
  count_0=0
  count_1=0
  for i in s:
    if i.islower():
      count_0+=1
    elif i.isupper():
      count_1+=1
    elif i==' ':
      continue
  return f"Lower characters: {count_0}, Upper characters: {count_1}"
print(up_low(a))

#Write a Python function to check whether a number is perfect or not.A Perfect number is a number that is half the sum of all of its positive divisors (including itself).The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
def perfect_no(num):
    s=[]
    
    for i in range(1,num):
        if num%i==0:
          s.append(i)
    if sum(s)==num:
            return('perfect')
    else:
            return('not prefect')

print(perfect_no(28))

#Write a Python program to print the even numbers from a given list.

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def even(l):
  s=[]
  for i in l:
    if i%2==0:
      s.append(i)
  return s
print(even(a))

#Write a Python function to concatenate any no of dictionaries to create a new one.

def concat_dict(**d):
  dt={}
  for i in d:
     dt.update(d[i])
  return dt
print(concat_dict(dic1={1:10, 2:20},dic2={3:30, 4:40},dic3={5:50,6:60}))

#Write a python function that accepts a string as input and returns the word with most occurence.
a='hello how are you i am fine thank you'
def most_occur(n):
  d={}
  for i in n.split( ):
    if i in d:
      d[i]=d[i]+1
    else:
      d[i]=1
  max_val=max(d.values())
  for i in d:
    if d[i]==max_val:
      return f'{i} -> {d[i]}'
      break

def most_occur(l):
  vocab={}
  for i in l.split():
    vocab[i]=l.split().count(i)
  max_key=max(vocab, key=vocab.get)
  return [max_key, vocab[max_key]]
most_occur(s)
 
print(most_occur('how do you do these you days you'))

#Write a python function that receives a list of integers and prints out a histogram of bin size 10

l=[13,42,15,37,22,39,41,50]
def histogram(l):
  import math
  min_bin=math.floor(min(l)/10)*10
  max_bin=math.ceil(max(l)/10)*10
  d={}
  for i in range(min_bin,max_bin,10):
    count=0
    for j in l:
      if i+1<=j<=i+10: #(11-20,21-30,31-40==j or not)
        count+=1
    d[str(i+1)+'-'+str(i+10)]=count
  return d
print(histogram(l))

#Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.
List_of_Coordinates=[(1,1),(2,2),(3,3),(4,4)]
Query_Point=(0,0)
def shortest_distance(cood, query):
  temp=[]
  for i in cood:
    distance=((i[0] - query[0])**2 + (i[1] - query[1])**2)**0.5
    temp.append(distance)
  return cood[sorted(list(enumerate(temp)),key=lambda x:x[1])[0][0]]
 
cood=[(1,1),(2,2),(3,3),(4,4)]
query=(0,0)
shortest_distance(cood,query)

#Write a python program that receives a list of strings and performs bag of word operation on those strings
#https://en.wikipedia.org/wiki/Bag-of-words_model
#bag of words meaning conversion of words into numbers
#list of stings[cat,mat,bat,rat]=lists of lists[1,1,1,0],[3,0,0,0],[0,0,2,1]
l=[
    'cat mat rat cat',
    'sat bat fat cat rat',
    'pat cat mat rat'
]
def bow(l):
  vocab=set()
  for i in l:
    vocab.update(i.split( ))
  result=[]
  for i in l:
    result.append([])
    for j in vocab:
      result[-1].append(i.count(j))
  print(vocab)
  return result
    
bow(l)

#Write a Python program to add three given lists using Python map and lambda.
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
print(list(map(lambda x,y,z: x+y+z,l1,l2,l3)))

#Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
list1 = [1,2,3,4,5,6]
print(list(map(lambda x,y :x**y, list1,range(len(list1)))))

#Using filter() and list() functions and .lower() method filter all the vowels in a given string.
str1='FIFA world cup in 2022 will take place in Qatar.'
print(list(filter(lambda  x:True if x.lower() in 'aeiou' else False ,str1)))

#Use reduce to convert a 2D list to 1D
l=[[1,2,3],
  [3,6,7],
  [7,5,4]]
import functools
print(list(functools.reduce(lambda x,y: x+y,l)))

#A dictionary contains following information about 5 employees:
'''First name
Last name
Age
Grade(Skilled,Semi-skilled,Highly skilled)'''
#Write a program using map/filter/reduce to a list of employees(first name + last name) who are highly skilled
employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }
    
]
print(list(map(lambda x:x['fname']+' '+x['lname'],list(filter(lambda x:True if x['grade']=='highly-skilled' else False ,employees)))))

#Rectangle Class
#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.
#Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
#Eg. After making above classes and methods, on executing below code:-
#my_rectangle = Rectangle(3 , 4)
#my_rectangle.display()
class Rectangle:
  def __init__(self,l, w):
    self.length=l
    self.width=w
  def __perimeter(self):#it won't accessible to call outside directly.
    return(self.length + self.width)*2
  def __area(self):
    return self.length * self.width
  def display(self):
    print('The length of the rectangle is :',self.length)
    print('The width of the rectangle is :',self.width)
    print('The perimeter of rectangle is :',self.__perimeter())
    print('The area of rectangle is:',self.__area())

my_rectangle= Rectangle(3 , 4)
my_rectangle.display()

#Bank Class
#Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
#Create a constructor with parameters: accountNumber, name, balance.
#Create a Deposit() method which manages the deposit actions.
#Create a Withdrawal() method which manages withdrawals actions.
#Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
#Create a display() method to display account details. Give the complete code for the BankAccount class.

class BankAccount:
  def __init__(self,account_number,name,balance):
    self.__account_number=int(account_number)
    self.__name=str(name)
    self.__balance=int(balance)
  def display(self):
    print('The account number is', self.__account_number)
    print("The account holder's name is", self.__name)
    print('The account balance is', self.__balance)
  def deposit(self):
    self.deposit=int(input('Enter the amount to deposit: '))
    self.__balance+=self.deposit
    print(f"{self.deposit}/- amount deposited.")
    print(f"Bank balance is:{self.__balance}")
  def withdrawal(self):
    self.withdrawal=int(input('Enter amount to withdraw: '))
    if self.withdrawal>self.__balance:
      print(f"Insufficient funds.")
    else:
      self.__balance-=self.withdrawal
      print(f'{self.withdrawal}/- deducted.')
      self.bank_fees()
  def bank_fees(self):
    self.reduction=(self.__balance*0.05)
    print(f"Bank fees {self.__balance*0.05}/- deducted.")
    print(f"Bank balance is:{self.__balance-self.reduction}")
  

newAccount = BankAccount(2178514584, "Mandy" , 2800)
newAccount.withdrawal()
newAccount.deposit()
newAccount.display()

#Computation class
#Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
#Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method
#Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.
#Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.
#Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.
#Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
#Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

class Computation:
  def __init__(self):
    pass

  def factorial(self,n):
    j=1
    for i in range(1,n+1):
      j*=i
    return j

  def natural_sum(self,n):
    j=0
    for i in range(1,n+1):
        j+=i
    return j

  def testPrime(self,n):
    j=0
    for i in range(1,n+1):
      if n%i==0:
        j+=1
    if j==2:
        return 'Prime'
    else:
        return 'Not Prime'

  def testPrims(self,n,n1):
    common=0
    for i in range(1,n+1):
      if n%i==0 and n1%i==0:
        common+=1
      if common!=1:
        return 'Not co-prime'
      else:
        return 'Co-prime'
        
  def tableMut(self,n):
    for i in range(1,11):
      print(n,'x',i,'=',n*i)

  def allTablesMut(self):
    for i in range(1,10):
      print('Table of',i)
      for j in range(1,11):
        print(i,'x',j,'=',i*j)
  
  def listDiv(self,n):
    lDiv=[]
    for i in range(1,n+1):
      if n%i==0:
        lDiv.append(i)
    return lDiv

  def listDivPrim(self,n):
    lDiv=[]
    for i in range(1, n+1):
      if n%i==0 and self.testPrime(i):
        lDiv.append(i)
    return lDiv


a=Computation()
print(a.factorial(5))
print(a.natural_sum(3))
print(a.testPrime(12))
print(a.testPrims(4,9))
print(a.tableMut(8))
print(a.listDiv(12))
print(a.listDivPrim(22))

#Build flashcard using class in Python.
#Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.
"""
Create a class named FlashCard.
Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong."""

class FlashCard:
  def __init__(self):
    self.fruits={
        'banana':'yellow',
        'watermelon':'green',
        'strawberry':'pink',
        'guava':'green',
        'mango':'yellow'
    }
  def quiz(self):
    print('Welcome to the fruit quiz.')
    while True:
      import random
      fruit, color= random.choices(list(self.fruits.items()))[0]
      print(f'What is the color of {fruit}?')
      user_ans=input( )
      if user_ans.lower()==color:
          print('Right answer.')
      else:
          print('Wrong answer.')
      option=int(input('Enter 0 to continue. 1 to quit. '))
      if option:
          break
    

f=FlashCard()
f.quiz()

#Problem 5 based on OOP Python.
#TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
"""eligibility criteria:
if experience is more than 3 years, average feedback should be 4.5 or more
if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course
Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

Note:
Consider all instance variables to be private and methods to be public.
An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
"""
class Instructor:
  def __init__(self,name,tech_skill,experience,feedback):
    self.__name=name
    self.__tech_skill=tech_skill
    self.__experience=experience
    self.__feedback=feedback
  def eligibility(self):
    if self.__experience > 3 and self.__feedback >= 4.5:
      return True
    elif self.__experience <= 3 and self.__feedback >= 4:
      return True
  def allocate_course(self,tech):
    is_eligible= self.eligibility()
    if is_eligible:
      if tech in self.__tech_skill:
        return 'Eligible for teaching.'
      else:
        return 'Not eligible for teaching.'
    else:
      return 'Not eligible for teaching.'

ins=Instructor('v',['web dev'],5,7)
print(ins.allocate_course('data science'))

#Count number of instances of a class created in Python?
'''Example: Say Car is any class.
maruti = Car()
bmw = Car()
honda = Car()
So after creating above instances. We want to count how many instances are created of Car class.
For above example no of instances = 3.
Write a program for above problem.'''

class Car:
  __counter=0
  def __init__(self):
    Car.__counter+=1
  def get_counter():
    return Car.__counter


maruti=Car()
bmw=Car()
honda=Car()
Car.get_counter()

#Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:
'''The Deck class should have a deal method to deal a single card from the deck
After a card is dealt, it is removed from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
Deck Class
It is class of all possible cards in a deck. Total 52 cards.
Methods - deal() it will take out one card from the deck of cards.
Deck of cards should get shuffeled while creating the deck object.
no of cards remaining in deck - <number> should dsiplay on printing any deck object.
Card class
It is a class of card
Atrributes - suit and value
<suit> of <value> should dsiplay on printing any card object.'''

import random
class Card:
  def __init__(self,suit,value):
    self.suit=suit
    self.value=value
  def __repr__(self):
    return f"{self.suit}-->{self.value}"


class Deck:
  def __init__(self):
    suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    self.Cards=[Card (suit,value) for suit in suits for value in values]

  def shuffle(self):
    if len(self.Cards)<52:
     print('Only full deck can be shuffled.')
    else:
      random.shuffle(self.Cards)
    return self.Cards

  def __str__(self):
    return 'Cards left:-'+str(len(self.Cards))

    
  def deal(self):
    if len(self.Cards)==0:
      print('All cards have been dealt.')
    return self.Cards.pop()

d=Deck()
d.shuffle()
print(d.deal())
d.shuffle()
print(d.deal())
print(d.deal())
print(d)


#Find the area of a rectangle.
'''Approach:
The class name should be Rectangle.
The constructor should accept two parameters length and height but you can't pass the values directly to it while creating the constructor. E.g., rectangle = Rectangle(length=10, height=8) <-- you can't do that while creating the instances.
Create a method called area() which has no parameters.
Create a method called is_square() which also has no parameters. Return True if the rectangle is a square otherwise return False.
If you are using a if-else block inside the is_square() method, then use the one-linear syntax.
'''
class Rectangle:
  def __init__(self,l,h):
    self.length=l
    self.height=h
    print('in constructor')
  @classmethod #class=rectangle
  def property(cls, len, bread):
    print('in class method')
    return cls(len,bread)

  def area(self):
    return self.length*self.height

  def is_square(self):
    return True if self.height==self.length else False



r=Rectangle.property(3,4)
print(r.area())
print(r.is_square())

#Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.

from datetime import datetime
class ExpiryDate:
  def __init__(self):
    self.manufacture_date=input('Enter manufacturing date, month, year of product(dd-mm-yyyy): ')
    self.expiry_date=input('Enter expiry date, month, year of product(dd-mm-yyyy): ')

    self.manufacture_date=datetime.strptime(self.manufacture_date, '%d-%m-%Y')
    self.expiry_date=datetime.strptime(self.expiry_date, '%d-%m-%Y')

  def time_to_expire(self):
    today= datetime.now()
    if today>self.expiry_date:
      print('Product is expired already.')
    else:
      time_left=self.expiry_date.date()-today.date()
      print(time_left)
      

f=ExpiryDate()
print(f.time_to_expire())

# A university wants to automate their admission process. Students are admitted based on the marks scored in the qualifying exam. A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
'''
Age is greater than 20
Marks is between 0 and 100 (both inclusive)
A student qualifies for admission, if

Age and marks are valid and
Marks is 65 or more
Write a python program to represent the students seeking admission in the university. The details of student class are given below.
attributes-private student_id,marks,age all instances values =None
methods-public(validate_marks, validate_age, check_qualifications, )
setter methods
getter methods'''

class Student:
  def __init__(self):
    self.__sid=None
    self.__age=None
    self.__marks=None

  #setters
  def set_sid(self,sid):
    self.__sid=sid

  def set_age(self,age):
    self.__age=age

  def set_marks(self,marks):
    self.__marks=marks

  #getters 
  def get_sid(self):
   return self.__sid
  def get_age(self):
    return self.__age
  def get_marks(self):
    return self.__marks

  def validate_marks(self):
    return self.__marks > 0 and self.__marks <= 100

  def validate_age(self):
    return self.__age>=20

  def check_qualifications(self):
    if self.validate_age() and  self.validate_marks():
      return self.__marks>65
    else:
      return False

s1=Student()
s1.set_age(14)
s1.set_marks(95)
s1.set_sid(101)
print(s1.get_age())
print(s1.get_marks())
print(s1.get_sid())
s1.check_qualifications()

#Ice-Cream Scoops and Bowl shop
'''Create a class Scoop which has one public property flavor and one private proptery price. Take flavor values during object creation.

Create a class Bowl with private prperty scoop_list which will have list of scoopd object.

Create a method add_scoops in Bowl class which will add any no of Scoop objects given as parameter and store it in scoops_list.

Make getter and setter method for price property.

Make a method display to display flavour and price of each Scoop in scoop_list and print total price of the bowl by adding all flavour scoops prices.

Make a method sold in both Scoop class and Bowl class to print no of quantity sold.'''

class Scoop:
  __counter=0
  def __init__(self, flavor):
    self.flavor=flavor
    self.__price=None
    Scoop.__counter+=1

  def setter(self,price):
    self.__price=price

  def getter(self):
    return self.__price

  @staticmethod
  def sold():
    return Scoop.__counter

  def __str__(self):
    return f"Flavor- {self.flavor}, Price- {self.__price}"


class Bowl:
  __counter=0
  def __init__(self):
    self.__scoop_list=[]
    Bowl.__counter+=1

  def add_scoops(self,*new_scoop):
    for scoop in new_scoop:
      self.__scoop_list.append(scoop)

  def display(self):
    total=0
    for scoop in self.__scoop_list:
      print(scoop)
      total=total+scoop.getter()
    return f'Total price: {total}'
  
  @staticmethod
  def sold():
    return Bowl.__counter

choco=Scoop('chocolate')
choco.setter(120)
berry=Scoop('Berry')
berry.setter(125)
vanilla=Scoop('Vanilla')
vanilla.setter(150)

bowl=Bowl()
bowl.add_scoops(choco)
bowl.add_scoops(berry,vanilla)

print(bowl.display())
print(Bowl.sold())
print(Scoop.sold())


#Ice-Cream Bowl continue..
'''Making advancement in the above classes. Scoop and Bowl

Introduce a property max_scoops in Bowl class to signify maximum scoops that a bowl can have, exceeding that it will display Bowl is full. Take default value as 3.

no_of_scoop in Scoop class with default value of 1

Print <flavour> added with every scoop added.'''

class Scoop:
  __counter=0
  def __init__(self, flavor, num_scoops=1):
    self.flavor=flavor
    self.__price=None
    self.num_scoops=num_scoops
    Scoop.__counter+=1

  def setter(self,price):
    self.__price=price

  def getter(self):
    return self.__price

  @staticmethod
  def sold():
    return Scoop.__counter

  def __str__(self):
    return f"Flavor- {self.flavor}, Price- {self.__price}"


class Bowl:
  __counter=0
  def __init__(self,max_scoops=3):
    self.max_scoops=max_scoops
    self.scoop_added=0
    self.__scoop_list=[]
    Bowl.__counter+=1

  def add_scoops(self,*new_scoop):
    for scoop in new_scoop:
      if self.scoop_added+scoop.num_scoops<=self.max_scoops:
        self.__scoop_list.append(scoop)
        self.scoop_added=self.scoop_added + scoop.num_scoops
        print('Flavor',scoop.flavor,'added!')
      else:
        print('The bowl is full.')
        break
    

  def display(self):
    total=0
    for scoop in self.__scoop_list:
      print(scoop)
      total=total+scoop.getter()
    return f'Total price: {total}'
  
  @staticmethod
  def sold():
    return Bowl.__counter

choco=Scoop('chocolate')
choco.setter(120)
berry=Scoop('Berry',1)
berry.setter(125)
vanilla=Scoop('Vanilla',2)
vanilla.setter(150)

bowl=Bowl()
bowl.add_scoops(choco)
bowl.add_scoops(berry,vanilla)

print(bowl.display())
print(Bowl.sold())
print(Scoop.sold())

'''Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.'''

class Vehicle:
    def __init__(self,type,capacity):
        self.type=type
        self.capacity=capacity
    
    def fare(self):
        return 100*self.capacity

class Bus(Vehicle):
    def fare(self):
        base_fare=super().fare()
        bus_fare=base_fare+0.1*base_fare
        return bus_fare

v=Vehicle('bus',100)
print(v.fare())
b=Bus('Bus',50)
print(b.fare())

# Write a program that has a class Point. Define another class Location which has two objects (Location & Destination) of class Point. Also define a function in Location that prints the reflection of Destination on the x axis.

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show_point(self):
        return f'{self.x},{self.y}'


class Location:
    def __init__(self,x1,y1,x2,y2):
        self.source=Point(x1,y1)
        self.destination=Point(x2,y2)

    def show(self):
        print('The source is ',self.source.show_point())
        print('The destination is ',self.destination.show_point())

    def reflection(self):
        self.destination.y=-self.destination.y
        print('The reflection is ',self.destination.show_point())

l=Location(0,0,1,1)
print(l.show())
print(l.reflection())

#Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triamgle from Polygon and write methods to get the details of their dimensions and hence calculate the area.

from abc import ABC, abstractmethod

class Polygon(ABC):
  
  @abstractmethod
  def get_data():
    pass

  @abstractmethod
  def area():
    pass

class Rectangle(Polygon):
  
  def get_data(self,l,b):
    self.l=l
    self.b=b
  
  def area(self):
    return self.l*self.b

class Triangle(Polygon):
  
  def get_data(self,b,h):
    self.b=b
    self.h=h

  def area(self):
    return 0.5*self.b*self.h


rect=Rectangle()
rect.get_data(4,5)
print(rect.area())
t=Triangle()
print(t.get_data(4,5))
print(t.area())

#Write a function get_final_line(filename), which takes filename as input and return final line of the file.
#Note: You can choose any file of your choice.

def get_final_line(file_name):
    final_line=' '
    for current_file in open(file_name, 'r'):
        final_line=current_file
    return final_line

print(get_final_line('sample.txt'))


# Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation -- dictionary.



'''Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python to read through the file you’ve created. For each line, multiply each first number by the second and include it in the file in third column. In last add a line Total, by summing the value of third column
'''

with open('numbers.txt','w') as f:
    for i in range(1,11,2):
        f.write(f'{i}\t{i+1}\n')
        
with open('numbers.txt','r') as f:
    lines=f.readlines()

total=0
with open('numbers.txt','w') as f:
    for line in lines:
        num1, num2=map(int, line.split('\t'))
        result=num1*num2
        total+=result
        f.write(f'{num1}\t{num2}\t{result}\n')
    f.write(f'Total: {total}')

    
#Create line wise reverse of a file
#Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).
'''abc def -->> fed cba'''

def reversed(infile,outfile):
    with open(infile,'r') as f:
        lines=f.readlines()

    with open(outfile,'w') as f:
        for line in lines:
            f.write(line.rstrip()[::-1]+'\n')

#Create a Serialized dict of frequency of words in the file. And from given list of words, using serialized dict show word count.
strings = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do:  once or twice she had
            peeped into the book her sister was reading, but it had no
            pictures or conversations in it, `and what is the use of a book,'
            thought Alice `without pictures or conversation?'

            So she was considering in her own mind (as well as she could,
            for the hot day made her feel very sleepy and stupid), whether
            the pleasure of making a daisy-chain would be worth the trouble
            of getting up and picking the daisies, when suddenly a White
            Rabbit with pink eyes ran close by her.

            There was nothing so VERY remarkable in that; nor did Alice
            think it so VERY much out of the way to hear the Rabbit say to
            itself, `Oh dear!  Oh dear!  I shall be late!'  (when she thought
            it over afterwards, it occurred to her that she ought to have
            wondered at this, but at the time it all seemed quite natural);
            but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-
            POCKET, and looked at it, and then hurried on, Alice started to
            her feet, for it flashed across her mind that she had never
            before seen a rabbit with either a waistcoat-pocket, or a watch to
            take out of it, and burning with curiosity, she ran across the
            field after it, and fortunately was just in time to see it pop
            down a large rabbit-hole under the hedge."""

word_list = ['alice', 'wonder', 'natural']

word_count={}
for word in strings.lower().split(' '):
    try:
        word_count[word]+=1
    except:
        word_count[word]=1
    
import pickle as pkl 
pkl.dump(word_count,open('word_count','wb'))
pkl.load(open('word_count','rb'))

for s in word_list:
    try:
        print(s.title(),':',word_count[s])
    except:
        print(f'{s.title()} not found.')


#Given a string calculate length of the string using recursion.
"abcd"

def length_recursion(s):
    if s=='':
        return 0
    else:
        return 1+length_recursion(s[1:])

print(length_recursion('datascience'))

#Write a function that accepts two numbers and returns their greatest common divisior. Without using any loop
'''def gcd(int, int) => int

gcd(16,24) will give 8'''

def gcd(n1,n2):
    if n1==n2:
        return n1
    else:
        if n1>n2:
           return gcd(n1-n2,n2)
        else:
            return gcd(n1,n2-n1)
    
print(gcd(16,64))

'''String Edit Distance
Use your recursive function to write a program that reads two strings from the user and displays the edit distance between them.

The edit distance between two strings is a measure of their similarity—the smaller the edit distance, the more similar the strings are with regard to the minimum number of insert, delete and substitute operations needed to transform one string into the other.

Consider the strings kitten and sitting. The first string can be transformed into the second string with the following operations:

Substitute the k with an s,
substitute the e with an i,
and insert a g at the end of the string.
This is the smallest number of operations that can be performed to transform kitten into sitting. As a result, the edit distance is 3.

Write a recursive function that computes the edit distance between two strings.

Use the following algorithm:

Let s and t be the strings
    If the length of s is 0 then
        Return the length of t
    Else if the length of t is 0 then
        Return the length of s
    Else
        Set cost to 0
        If the last character in s does not equal the last character in t then
            Set cost to 1
        Set d1 equal to the edit distance between all characters except the last one in s, and all characters in t, plus 1
        Set d2 equal to the edit distance between all characters in s, and all characters except the last one in t, plus 1

        Set d3 equal to the edit distance between all characters except the last one in s, and all characters except the last one in t, plus cost
        Return the minimum of d1, d2 and d3'''



def edit_string_distance(s1,s2):
    if len(s1)==0:
        return len(s2)
    elif len(s2)==0:
        return len(s1)
    else:
        cost=0
        if s1[-1]!=s2[-1]:
            cost=1
        d1=edit_string_distance(s1[:-1],s2)+1
        d2=edit_string_distance(s2[:-1],s1)+1
        d3=edit_string_distance(s1[:-1],s2[:-1])+cost
    return min(d1,d2,d3)

print(edit_string_distance('sizing','sitting'))

''' Run-Length Encoding
Run-length encoding is a simple data compression technique that can be effective when repeated values occur at adjacent positions within a list. Compression is achieved by replacing groups of repeated values with one copy of the value, followed by the number of times that the value should be repeated. For example, the list

["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
would be compressed as ["A", 12, "B", 4, "A", 6, "B", 1].

Write a recursive function that implements the run-length compression technique described above. Your function will take a list or a string as its only parameter. It should return the run-length compressed list as its only result. Include a main program that reads a string from the user, compresses it, and displays the run-length encoded result.'''

def run_encoding(string):
    if not string:
        return []
    else:
        index=1
        for i in range(1,len(string)):
            if string[i]!=string[0]:
                break
            else:
                index+=1
        return [string[0], index] + run_encoding(string[index:])
        

print(run_encoding('zzzoooopooo'))


#Write a recursive function to convert a decimal to binary.

def dec_to_bin(dec):
    if dec==0:
        return 0
    elif dec==1:
        return '1'
    else:
        return dec_to_bin(dec//2) +str(dec%2)

print(dec_to_bin(9))

#You are given a function definition. There might be several issues on execution of this function. You are asked to do exception handling for diffrent errors that this function goes in to without altering this function. And print error text.
'''Function parameters l -> list, s -> could be anything'''

'''def function(l: list, s, **args):
    last_element = l[-1]

    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10

    res = sum(l)

    p = args['p']
    # print(p)
    return res/last_element * p + any_element
Check for different function calls:-

function([1,2,1], 12)
function([1,2,1]*9, '1-2')
function([1,'2',1]*9, 12)
function([1,'2',1]*9, 12)
function([1,2,0]*9, 12  )
function([1,2,1]*9, 12, p=None)
function([1,2,0]*9, 12, p=10)'''

def function(l: list, s, **args):
    last_element = l[-1]
    
    # print(p)
    try:
      l[int(s)]=10
      any_element = l[int(s)+10]
      l[s]=10

      res = sum(l)

      p = args['p']
      res= res/last_element * p + any_element
      print(f"Result:{res}")
    except IndexError as i:
        print(type(i))
        print(f'{i} error occured.') 
    except ValueError as v:
        print(type(v))
        print(f'{v} error occured.')
    except TypeError as t:
        print(type(t))
        print(f'{t} error occured.')
    except KeyError as k:
        print(type(k))
        print(f'{k} error occured.')
    except ZeroDivisionError as z:
        print(type(z))
        print(f'{z} error occured.')
    except Exception as e:
        print(f'{e} error occured.')
    finally:
        print('Thank you')
        

function([1,2,1], 12)
function([1,2,1]*9, '1-2')
function([1,'2',1]*9, 12)
function([1,2,0]*9, 12  )
function([1,2,1]*9, 12, p=None)
function([1,2,0]*9, 12, p=10)
function([1,2,1]*9, 12, p=10)


#You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of sum of elements.
'''List have elemnts as any no of key-pair dict with key as list index and value as any integer, integers and numeric-strings. There is always only one element in the dict.

l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])


print(s)'''

l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    try:
      s+=l[i]
    except TypeError:
      try:
        s += l[i].get(i)
      except AttributeError:
        s += int(l[i])
print(s)


#File Handling with Exception handling
#Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).

def func(file_name):
  try:
      if file_name:
        with open(file_name,'r') as f:
          f.write('Hello, Good Morning!!!')
          return 'File written successfully'
      else:
        return 'File name is empty or None.'
      
  except FileNotFoundError:
    return ('File not found.')
  except IOError as i:
    return (f'{i} error occured.')
  except TypeError as t:
    return (f'{t} error occured.')
  except NameError as n:
    return (f'{n} error occured.')
  except ValueError as v:
    return (f'{v} error occured.')
  except OSError as o:
    return (f'{o} error occured.')
  except io.UnsupportedOperation as u:
    return (f'{u} error occured.')
  except Exception as e:
    print(f'{e} error occured.')

print(func('a'))

# Number game program.
#Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a ValueTooLarge exception. If the value is smaller the number to be guessed the, raise a ValueTooSmall exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise GuessError if user guess a number less than 1.

class ValueTooLarge(Exception):
  def display(self):
    print('Larger.')
  
class ValueTooSmall(Exception):
  def display(self):
    print('Smaller')

class GuessError(Exception):
  def display(self):
    print('A guessing number must be between 1 to 100 only.')


import random
number=random.randint(1,100)
print('Welcome to the guess game.')
try:
  while True:
    guess=int(input('Guess a number between 1 to 100: '))
    try:
      if number==guess:
        print('Bravo!! You succeeded.')
        break
      if number>guess:
        raise ValueTooSmall

      if number<guess:
        raise ValueTooLarge

      if number<1 or type(guess)!=int:
        raise GuessError

    except ValueTooLarge as v:
        v.display()

    except ValueTooSmall as s:
        s.display()

    except GuessError as g:
        g.display()

except Exception as e:
    print(f'{e} error occured')


#Cast vote
#Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create InvalidAge exception and for name, create InvalidName exception. The name will be invalid when the string will be empty or name has only one word.
'''Enter the name: goransh s
Enter the age: 25
Goransh S  Congratulation !!! You can vote.'''

class InvalidAge(Exception):
  def display(self):
    print(f'You can cast your vote when you will turn 18 or plus.')
  
class InvalidName(Exception):
  def display(self):
    print(f'Please, enter a valid name....')

def vote():
  try:

    name=input('Enter your name: ')

    if name=='' or len(name.split(' '))<2:
      raise InvalidName
    else:
     age=int(input('Enter your age: '))

     if age>=18:
        print(f' Congratulations, {name} you can cast your vote.')

     else:
        raise InvalidAge

  except InvalidName as i:
    i.display()

  except InvalidAge as a:
    a.display()
  
  except Exception as e:
    print(f'{e} error occured.')
  finally:
    print('Thank you!')

vote()

#Write a python function which infinitely prints natural numbers in a single line. Raise the StopIteration exception after displaying first 20 numnbers to exit from the program.

def display(n):
  i=0
  while True:
    try:
      i+=1
      n+=1
      if i==21:
        raise StopIteration
    except StopIteration:
       break
    else:
      print(n,end=' ')

display(10)

#Write Person Class as given below and then display it's namespace.
'''Class Name - Person

Attributes:
name - public
state - public
city - private
age - private

Methods:
address - public
It give address of the person as "<name>, <city>, <state>"'''

class Person:
    def __init__(self,name,state):
        self.name=name
        self.state=state
        self.__city=None
        self.__age=None

    def set_city(self,city):
        self.__city=city
    
    def get_city(self):
        return self.__city
    
    def set_age(self,age):
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def address(self):
        return f"<{self.name}>, <{self.__city}>, <{self.state}>"

for i in Person.__dict__:
    print(i)


#Write a program to show namespace of object/instance of above(Person) class.

p=Person('j','la')
p.set_age(20)
p.set_city('sf')
print(f"Address:{p.address()}")
for i in p.__dict__:
    print('\n',i)

#Write a recursive program to to calculate gcd and print no. of function calls taken to find the solution.

counter=0
def gcd(a,b):
    global counter
    counter+=1
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(5, 10),", count:",counter)


#Iterator And Generator
#Create your own MyEnumerate class such that someone can use it instead of enumerate. It will need to return a tuple with each iteration, with the first element in the tuple being the index (starting with 0) and the second element being the current element from the underlying data structure. Trying to use MyEnumerate with a noniterable argument will result in an error.
'''
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')

0 : a
1 : b
2 : c'''

class EnumerateIterator:
        def __init__(self, data, max_items):
            self.data=data
            self.max_items=max_items
            self.index=0

        def __next__(self):
            if self.index>=self.max_items:
                raise StopIteration
        
            value=(self.index,self.data[self.index])
            self.index+=1
            return value


class MyEnumerate:
    def __init__(self,data):
        self.data=data

    def __iter__(self):
        return EnumerateIterator(self.data, len(self.data))
    
for index, letter in MyEnumerate('abc'):
    print(f'{index}:{letter}')

class MyEnumerate:
    def __init__(self,data):
        self.data=data
        self.index=0
        self.max_items=len(self.data)

    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index>=self.max_items:
                raise StopIteration
        
        value=(self.index,self.data[self.index])
        self.index+=1
        return value

for index, letter in MyEnumerate('abc'):
    print(f'\n{index}:{letter}')

    
#Iterate in circle
#Define a class, Circle, that takes two arguments when defined: a sequence and a number. The idea is that the object will then return elements the defined number of times. If the number is greater than the number of elements, then the sequence repeats as necessary. You can define an another class used as a helper (like I call CircleIterator).

'''c = Circle('abc', 5)
d = Circle('abc', 7)
print(list(c))
print(list(d))
Output

[a, b, c, a, b]
[a, b, c, a, b, c, a]'''

class Circle:
    def __init__(self,data,max_items):
        self.data=data
        self.max_items=max_items
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index>=self.max_items:
          raise StopIteration
        value=self.data[self.index%len(self.data)]
        self.index+=1
        return value

c = Circle('abc', 5)
print(list(c))


''' Generator time elapsed
Write a generator function whose argument must be iterable. With each iteration, the generator will return a two-element tuple. The first element in the tuple will be an integer indicating how many seconds have passed since the previous iteration. The tuple’s second element will be the next item from the passed argument.

Note that the timing should be relative to the previous iteration, not when the generator was first created or invoked. Thus the timing number in the first iteration will be 0

for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)
Output:

(0.0, 'a')
(2.005651817999933, 'b')
(2.0023095009998997, 'c')
(2.001949742000079, 'd')
Note: Your output may differ because of diffrent system has different processing configuration.'''

import time
def elapsed_since(data):
    last_time=time.perf_counter()
    yield(0,data[0])
    for i in data[1:]:
        current_time=time.perf_counter()
        delta=current_time-last_time
        last_time=current_time
        yield (delta,i)

for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)


#Decorators
#Write a Python program to make a chain of function decorators (bold, italic, underline etc.) on a given function which prints "hello world"
'''bold - wrap string with <b> tag. <b>Str</b>
italic - wrap string with <i> tag. <i>Str</i>
underline- wrap string with <u> tag. <u>Str</u>'''

def bold(func):
    def wrapper():
        return f"<b> {func()} </b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i> {func()} </i>"
    return wrapper

def underline(func):
    def wrapper():
        return f"<u> {func()} </u>"
    return wrapper

@bold
@italic
@underline
def hello():
    return 'hello world'

print(hello())

#Write a decorator called printer which causes any decorated function to print their return values. If the return value of a given function is None, printer should do nothing.
from functools import wraps

def printer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        return_value=func(*args,**kwargs)
        if return_value is not None:
            print(return_value)
        return return_value
    return inner

@printer
def hello(s):
    return s 

print(hello('v'))
help(hello)

#Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.

def double(func):
    wraps(func)
    def wrapper(*args,**kwargs):
       func(*args,**kwargs)
       return func(*args,**kwargs)
    return wrapper

@double
def hello(string):
   return string



print(hello('s'))
#Write a decorator which doubles the return value of any function. And test that decoratos is working correctly or not using asert.

def twice(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        return 2*func(*args,**kwargs)
    return wrapper

def add_dec(a, b):
  return a + b

@twice
def add(a, b):
  return a + b


a=2
b=3
print(add(2,3))
assert add(a, b)==add_dec(a, b)*2, 'It is wrong.'
print('Values are matching.')

import numpy as np
#Create a null vector of size 10 but the fifth value which is 1.

a=np.nan*np.empty(10)
a[4]=1
print(a)

#Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.

def program(a,b):
  a1=np.random.random([a,b])
  avg=np.mean(a1)
  return a1, avg


a,b=map(int,input('Enter a and b with "," in-between:  ').split(','))
a1,avg=program(a,b)
print('Array:',a1)
print("Average:",avg)

#Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.

def pro(a,b):
  a1=np.ones([a,b])
  a1[1:-1,1:-1]=0
  return a1

a,b=map(int,input('Enter a and b with "," in-between: ').split(','))
print(pro(a,b))

#Create a vector of size 10 with values ranging from 0 to 1, both excluded.

a1=np.linspace(0,1,12)[1:-1]
print(a1)

#Can you create a identity mattrix of shape (3,4). If yes write code for it.

a1=np.zeros([3,4])
np.fill_diagonal(a1,1)
print(a1)
a1=np.eye(3,4)
print(a1)#it is not possible

#Create a 5x5 matrix with row values ranging from 0 to 4.

a1=np.zeros([5,5])
a1+=np.arange(5)
print(a1)

#Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates of a point as array is given. Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type.

coordinate=np.random.randint(1,101,[10,2])
point=np.array([2,3])
distance=np.sqrt(np.sum((coordinate-point)**2,axis=1).astype(int))
print(distance)

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

a=np.unravel_index(100,(6,7,8))
print(a)
#or
a=np.zeros([6,7,8])
#print(a)

#You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.

'''Input Format:

A single line of input containing space separated numbers.

Output Format:

Print the reverse NumPy array with type float.

Example 1:

Input:

1 2 3 4 -8 -10'''

a1="1 2 3 4 -8 -10"
a1=list(map(float,a1.strip().split(' ')))
a1=a1[::-1]
print(a1)


#Count the number of elements of a numpy array.

a1=np.zeros([3,4])
print(a1.size)

#Create a Python function to calculate the Softmax of the given numpy 1D array. The function only accepts the numpy 1D array, otherwise raise error.
'''
σ(z⃗ )i=ezi/∑Kj=iezj
input=[86.03331084 37.7285648  48.64908087 87.16563062 38.40852563 37.20006318]'''

def softmax(a):
  if type(a)!=np.ndarray:
    raise TypeError('Requires numpy arrays')
  elif a.ndim > 1:
    raise TypeError('Requires 1-D array')
 
  a_ex=np.exp(a)
  a_sum=np.sum(a_ex)
  softmax_a=a_ex/a_sum
  return softmax_a

print(softmax(np.array([86.03331084, 37.7285648,  48.64908087, 87.16563062, 38.40852563, 37.20006318])))


#Write a python function that accepts infinite number of numpy arrays and do the vertical stack to them. Then return that new array as result. The function only accepts the numpy array, otherwise raise error.
'''input=a= [[0 1 2 3 4]
 [5 6 7 8 9]]

b= [[1 1 1 1 1]
 [1 1 1 1 1]]'''

def vertical_stack(*args):
    for i in args:
        if type(i)!=np.ndarray:
            raise TypeError('Requires numpy array.')
    return np.vstack(args)

a=np.array([[0, 1, 2, 3, 4],
[5, 6, 7, 8, 9]])

b=np.array([[1, 1, 1, 1, 1],
[1, 1, 1, 1, 1]])

c=np.array([[0.10117373, 0.1677244,  0.73764059, 0.83166097, 0.48985695],
[0.44581567, 0.13502419, 0.55692335, 0.16479622, 0.61193593]])

print(vertical_stack(a,b,c))
    
#Create a python function named date_array that accepts two dates as string format and returns a numpy array of dates between those 2 dates. The function only accept 2 strings, otherwise raise error. The date format should be like this only: 2022-12-6. The end date should be included and for simplicity, choose dates from a same year.
def date_array(start:str,end:str):
    if type(start)!=str and type(end)!=str:
        raise TypeError('Requires only string type.')
    start = np.datetime64(start)
    end = np.datetime64(end)
    if end < start:
        raise ValueError("End date must be after start date.")
    while end != end.astype('datetime64[M]'):
        end -= np.timedelta64(1,'D')
    dates=np.arange(start, end + np.timedelta64(1,'D'))
    return dates

print(date_array(start = '2020-11-25', end = '2020-12-01'))


 #Subtract the mean of each row from a matrix.

a=np.eye(3,4)
mean=np.mean(a,axis=1,keepdims=True)
result=a-mean
print(result)


 #Swap column-1 of array with column-2 in the array.
a=np.arange(9).reshape(3,3)
print(a)
a=a[:, [0, 2, 1]]
print(a)

#Replace odd elements in arrays with -1.
a=np.arange(10)
a[a%2!=0]=-1
print(a)

#Given two arrays of same shape make an array of max out of two arrays. (Numpy way)
a=np.array([6,3,1,5,8])
b=np.array([3,2,1,7,2])
result=np.maximum.reduce([a,b])
print(result)


#Answer below asked questions on given array:
'''Fetch Every alternate column of the array
Normalise the given array
There are different form of normalisation for this question use below formula.

Xnormalized=X−Xmin/Xmax−Xmin '''

arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)

print(arr1[:,::2])
print(arr1)

normalize=(arr1-arr1.min())/(arr1.max()-arr1.min())
print(normalize)



# Write a function which will accept 2 arguments.
'''First: A 1D numpy array arr

Second: An integer n {Please make sure n<=len(arr)}

Output: The output should be the nth largest item out of the array

# Example1 : arr=(12,34,40,7,1,0) and n=3, the output should be 12
# Example2 : arr=(12,34,40,7,1,0) and n=1, the output should be 40'''

def nthmax(arr,n):
    if n>len(arr):
        raise IndexError('Value is out of range.')
    arr.sort()
    return arr[-n]
print(nthmax(np.array([12,34,40,7,1,0]),1))



'''Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])'''

a=np.array([1,2,3])
a=np.hstack([np.repeat(a,3),np.tile(a,3)])
print(a)

import numpy as np
import matplotlib.pyplot as plt

# Find the nearest element in the array to a given integer.
'''Ex:- 
a=23 and array - [10 17 24 31 38 45 52 59].
Nearest element is 24
Hint: Read about this function argmin()'''

a=np.array([10, 17, 24, 31, 38, 45, 52, 59])
value=23
v=a[(np.abs(a-value)).argmin()]
print(v)


''' Replace multiples of 3 or 5 as 0 in the given array.
arr=[1 2 3 4 5 6 7 9]

result-> [1 2 0 4 0 0 7 0]'''

a1=np.asarray([1, 2, 3, 4, 5, 6, 7, 9])
a1[(a1%3==0) | (a1%5==0)]=0
print(a1)


#Use Fancy Indexing.
'''Double the array elements at given indexes

arr = np.arrange(10)
indexes = [0,3,4,9]
Result -> [ 0 1 2 6 8 5 6 7 8 18]

Using a given array make a different array as in below example

array = [1,2,3]
result array -> [1 1 1 2 2 2 3 3 3]
Internal-repetion should be as length of the array.
Hint:

if a is an array
a = [2,4]
a[[1,1,0,1]] will result in-> [4 4 2 4]'''

#1que.'s  solution
arr = np.arange(10)
indexes=[0,3,4,9]
print(arr)
arr[indexes]*=2
print(arr)

#2 ques.'s solution

a=np.array([1,2,3])
indexes=[]
for index in range(len(a)):
    indexes.extend([index]*len(a))
a[index]
print(indexes)



#Your are given an array which is havig some nan value. You job is to fill those nan values with most common element in the array.

arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
arr=np.array([[1,2,np.nan],[4,2,6],[np.nan,np.nan,5]])
print(arr)
arr[np.where(np.isnan(arr))]=np.argmax(arr)
print(arr)

#Write a NumPy program
'''to find the missing data in a given array. Return a boolean matrix.
also try to fill those missing values with 0. For that, you can use np.nan_to_num(a)'''


a=np.array([[3, 2, np.nan, 1],
          [10, 12, 10, 9],
          [5, np.nan, 1, np.nan]])

print(np.isnan(a))
arr_no_nan = np.nan_to_num(a)
print(arr_no_nan)


#Given two arrays, X and Y, construct the Cauchy matrix C.
#Cij =1/(xi - yj)
x = np.array([1,2,3,4]).reshape((-1, 1))
y = np.array([5,6,7])
print(np.broadcast_to(x,(4,3)))
print(np.broadcast_to(y,(4,3)))
cij=1/x-y
print(cij)

#Plot this below equation.
'''y=ex−e−x/ex+e−x 

Note: This equation is called tanh activation function. In deep learning, many times this function is used. If you find some difference between the sigmoid function and this tanh function, note that to your notebook.'''

x=np.linspace(-30,30,1000)
y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
a=plt.plot(x,y)
print(plt.show())


# Plot the below equation.
'''y=36−(x−4)2−−−−−−−−−−√+2 

The range of x should be between -2 to 10.  x∈[−2,10]'''

y=(np.sqrt(36-(np.linspace(-2,10)-4)**2))+2
plt.plot(y)
print(plt.show())


# Write a program implement Boradcasting Rule to check if two array can be added or not.
'''Given tuples of shapes.

shape of a- (3,2,2)
shape of b- (2,2)

check_broadcast(a, b) -> return Boolean (True if can broadcasted, False other wise.)'''


def check_broadcast(a,b):
    a=a[::-1]
    b=b[::-1]
    for ai,bi in zip(a,b):
        if ai!=bi and ai!=1 and bi!=1:
            return False
    return True

print(check_broadcast((3,2,2),(4,2,2)))

#Create a random 3x4 matrix with value between 0-100. And perform below tasks
'''i. Sort this matrix. np.sort()
ii. Sort this matrix based on values in 2nd column.
iii. Sort this matrix based on max value in each row.
iv. Sort based on elements value.'''

arr=np.random.randint(0,100,(4,3))
print(arr)
# solution1
ar=np.sort(arr)
print(f'{ar},\n')

#solution 2
col2=arr[:, 1].argsort()
print(arr[col2])

#solution3

max_row=np.array(sorted(arr, key=lambda x :max(x)))
print("\n",max_row,'\n')

#solution4
a=np.sort(arr,axis=None).reshape(arr.shape)
print(a)



#There is an array of marks of 5 students in 4 subjects. Further you are asked to perform below task.
'''i. Add marks every student of an extra subject in the same array.
ii. Add two new students marks in respective 5 subjects.(one subject added in above task)
iii. Add extra column with sum of all subjects(5-subjects) marks
iv. Sort the array(non-ascending order) on total marks column--one added in above task. Show top 2 rows.
Note: Change dimension of arrays during concatenation or appending if required.

Given Array-'''

marks =np.array([[13, 10,  9, 33],
       [63, 46, 90, 42],
       [39, 76, 13, 29],
       [82,  9, 29, 78],
       [67, 61, 59, 36]])

extra_subject = np.array([41, 87, 72, 36, 92]).reshape(-1,1)
#solution1
marks=np.concatenate([marks,extra_subject],axis=1)
print(marks)
#or
np.hstack((marks,extra_subject))

# Two extra students record-
rec1 = np.array([77, 83, 98, 95, 89]).reshape(1,-1)
rec2 = np.array([92, 71, 52, 61, 53]).reshape(1,-1)


#solution2
marks=np.concatenate([marks,rec1,rec2],axis=0)
print('\n',marks)
#or
np.vstack((marks,rec1,rec2))

#solution3
sum_m=np.hstack((np.sum(marks,axis=1))).reshape(-1,1)
marks=np.hstack((marks,sum_m))
print(marks)

#or
sum_marks=np.sum(marks,axis=1,keepdims=True)
np.concatenate([marks,sum_marks],axis=1)

#solution4
marks=np.array(sorted(marks,key=lambda x: x[-1],reverse=True))
print('\n',marks)

#solution5
print(marks[:,:2])


#Find unique arrays from a 2D array column wise and row wise.
arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])
print(arr)                

#solution1
col=np.unique(arr,axis=0)
print('\n',col,'\n')
#solution2
row=np.unique(arr,axis=1)
print(row)


# Flip given 2-D array along both axes at the same time.

arr = np.array([[1,2,3,3,1,1],
                [0,9,1,2,8,8],
                [1,2,3,8,8,8],
                [1,2,3,3,1,1]])
print(arr)
print(np.flip(arr,axis=None))
#or
np.flip(arr,axis=[0,1])


#Get row numbers of NumPy array having element larger than X.
arr = np.array([[1,2,3,4,5], 
      [10,-3,30,4,5], 
      [3,2,5,-4,5], 
      [9,7,3,6,5]])

X = 6

a=arr[np.where(np.any(arr>X,axis=1))][0]
print(a)


#How to convert an array of arrays into a flat 1d array?
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

print(arr1)
print(arr2)
print(arr3)
n=np.concatenate((arr1,arr2,arr3))
print(n)


#You are given a array. You have to find the minimum and maximum array element and remove that from the array.

np.random.seed(400)
arr = np.random.randint(100, 1000, 200).reshape((1, 200))
min_element=arr.argmin()
max_element=arr.argmax()
print(arr.max(), arr.min())
arr=np.delete(arr, max_element, axis=1)
arr=np.delete(arr, min_element, axis=1)
print(arr.max(), arr.min())


#You are given an arrays. You have to limit this array's elements between 100 to 200.  arr∈[100,700] . So replace those values accordingly with the minimum and maximum value. Then sort the array and perform the cumulative sum of that array.

a=np.random.randint(0,2000,500)
b=np.cumsum(np.sort(np.clip(a,a_min=100,a_max=200)))


#You are given a array ( arr∈[0,1] ). First you have round off the elements upto 3 decimal places and compare that
'''0th percentile == minimum value of the array
100th percentile == maximum value of the array
also find the difference betwen 51th percenile and 50th percentile values'''

a=np.random.random(100)
a=np.around(a,decimals=3)

#solution1
print('0th percentile == minimum value of the array: ',np.min(a)==np.percentile(a,0))

#solution2
print('100th percentile == maximum value of the array: ',np.max(a)==np.percentile(a,100))

#solution3
print('The difference betwen 51th percenile and 50th percentile values: ',(np.percentile(a,51)-np.percentile(a,50)))

#Write a program to create an empty series.
s=pd.Series([],dtype=float)
print(s)

# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
def program(s1,s2):
  s1=pd.Series(s1)
  s2=pd.Series(s2)
  sum=s1+s2
  subtract=s1-s2
  multiply=s1*s2
  division=s1/s2
  
  return sum, subtract, multiply, division

s1=[0,1,2,3]
s2=[2,2,2,2]
print(program(s1,s2))

#Write a Pandas program to compare the elements of the two Pandas Series.
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
s1=pd.Series([2, 4, 6, 8, 10])
s2=pd.Series([1, 3, 5, 7, 10])
print(s1==s2)
print(s1<s2)
print(s1>s2)


#Write a function to change the data type of given a column or a Series. Function takes series and data type as input, returns the converted series.
'''series = pd.Series([1,2,'Python', 2.0, True, 100])
change to float type data pd.to_numeric()'''
def program(s,dtype):
  s=pd.to_numeric(pd.Series(s),errors='coerce').astype(float)
  return s

series = pd.Series([1,2,'Python', 2.0, True, 100])
print(program(series,float))


#download data of batter and runs
runs=pd.read_csv('C:\\Users\91905\Downloads\\batsman_runs_series.csv')
print(runs)
#Find top 10 most run getter from the series.

batter=runs.sort_values('batsman_run',ascending=False).head(10)
print(batter)

# No of players having runs above 3000
runs_3000=runs[runs['batsman_run']>3000].shape[0]
print(runs_3000)


#No of players having runs above mean value?
above_mean=runs[runs['batsman_run']>runs['batsman_run'].mean()].shape[0]
print(above_mean)


#download items series
items=pd.read_csv("C:\\Users\91905\Downloads\\items.csv",index_col='item_name').squeeze('columns')
print(items)
#i. Read `items.csv` making `item_name` as index.
#ii. Show no of nan values
#ii. Item price is given in $, so convert it to rupees without currency symbol.
#iii. Make data type of newly made series as float.
#iv. Fill nan with mean of the series

#above done (i)
#(ii)
i=items[items.isna()].size
print(i)
#2(ii)
def rupees(x):
    try:
        y=x[1:]
    except:
        y=x
    return float(y)*82.49

items=items.apply(rupees)
print(items)

#(iii)done above
#(iv)
items=items.fillna(items.mean())
print(items)

#i. Find mean price
#ii. Find 30th and 6th percentile value
#iii. Plot Histogram on price with bin size 50
#iv. No of items price lies between [1000 to 2000]
#(i)
m=items.mean()
print(m)

#(ii)
p30=items.quantile(0.3)
p6=items.quantile(0.06)
print(p30)
print(p6)

#(iii)
h=items.plot.hist(bins=50)
plt.show()

#(iv)
r=items[(items>1000)& (items<2000)]
print(r)

data = {'birds': ['Cranes', 'Cranes', 'plovers', 'spoonbills', 'spoonbills', 'Cranes', 'plovers', 'Cranes', 'spoonbills', 'spoonbills', 'Cranes'], 
        'age': [3.5, 4, 1.5, np.nan, 6, 3, 5.5, np.nan, 8, 4, 3.5], 'visits': [2, 4, 3, 4, 3, 4, 2, 2, 3, 2, 2], 
        'priority': ['yes', 'yes', 'no', np.nan, 'no', 'no', 'no', 'yes', 'no', 'no','yes']}


labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

#1
#i. Create a DataFrame birds from the above dictionary data which has the index labels.
#ii. Display basic information about the dataFrame.
#iii. Show Alternate rows of the dataframe.
#(i)
data=pd.DataFrame(data,index=[labels])
print(data)
#(ii)
print(data.info())
print(data.describe())
#(iii)
print(data.iloc[::2])


#2
#i. Show only rows [1st, 3rd, 7th] from columns ['bird', 'age']
#ii. Select rows where the number of visits is less than 4.
#(i)
r=data.iloc[[0,2,6]][['birds','age']]
print(r)
#(ii)
v=data[data['visits']<4]
print(v)

#3
#i. Select all rows with nan values in age and visits column.
#ii. Fill nan with respective series mode value.
#(i)
n=data[data[['age','visits']].isnull().any(axis=1)]
a=data[data['age'].isna()| data['visits'].isna()]
print(a)

#(ii)
n=data.fillna(data.mode().iloc[0],inplace=True)
print(data)

#4
#i. Find the total number of visits of the bird Cranes
#ii. Find the number of each type of birds in dataframe.
#iii. Print no of duplicate rows
#iv. Drop Duplicates rows and make this changes permanent. Show dataframe after changes.
#(i)
d=data[data['birds']=='Cranes']['visits'].sum()
print(d)

#(ii)
n=data['birds'].value_counts()
print(n)

#(iii)
d=data.duplicated().sum()
print(d)

#(iv)
data.drop_duplicates(inplace=True)
print(data)

#downlaod ipl 2008-2022 data
ipl=pd.read_csv("C:\\Users\\91905\Downloads\IPL_Matches_2008_2022.csv")
#5
''' In IPL matches dataset some teams name has changed.
You will have to consider them as same.

'Delhi Capitals' formerly as 'Delhi Daredevils' 
'Punjab Kings' formerly as 'Kings XI Punjab'
'Rising Pune Supergiant' formerly as 'Rising Pune Supergiants'
You need to make changes accordingly. Consider current name for each teams.

Be careful Gujrat Titans and Gujrat Lions are different teams.'''
#(i)
changed_name={'Delhi Capitals': 'Delhi Daredevils',
'Punjab Kings':'Kings XI Punjab',
'Rising Pune Supergiant':'Rising Pune Supergiants'}
ipl.replace(changed_name.values(),changed_name.keys(),inplace=True)
print(ipl[ipl['Team1']=='Punjab Kings'].sample(5))



#6 Write a code which can display the bar chart of top 5 teams who have played maximum number of matches in the IPL.
#Hint: Be careful the data is divided in 2 different cols(Team 1 and Team 2)
i=(ipl['Team1'].value_counts()+ ipl['Team2'].value_counts()).sort_values(ascending=False).head().plot(kind='bar')
print(i)
plt.show()


#7 Player who got Most no. of player of the match award playing against Mumbai Indians.
#Just for this question assume player of the match award is given to players from winning team. Although this is true in most of the cases.
m1=(ipl.Team1=='Mumbai Indians') | (ipl.Team2=='Mumabi Indians')
m2=ipl.WinningTeam != 'Mumbai Indians'
m=ipl[m1&m2].Player_of_Match.value_counts().head(1)
print(m)



#8 Create a function which will take two string(name of two teams) as input. Show win Loss record between them and player getting most player of the match award in matches between these two teams.
def player(team1,team2):
  m1=(ipl['Team1']==team1) | (ipl['Team2']==team1)
  m2=(ipl['Team1']==team2) | (ipl['Team2']==team2)
  matches=ipl[m1& m2]
  print(matches['Player_of_Match'].value_counts().head(1))
  return matches['WinningTeam'].value_counts()
  
print(player('Kolkata Knight Riders','Chennai Super Kings'))



#9  Find out the top 7 cities where the matches of Kolkata Knight Riders are played frequently and plot the result as bar chart.
i=ipl[(ipl['Team1']=='Kolkata Knight Riders')| (ipl['Team2']=='Kolkata Knight Riders')]['City'].value_counts().head(7).plot(kind='bar')
print(i)
plt.show()

#10 Find out the average margin for the team Mumbai Indians for only the session 2011.

mi=ipl[((ipl['Team1'] =='Mumbai Indians') | (ipl['Team2']=='Mumbai Indians')) & (ipl['Season']=='2011')]['Margin'].mean()
print(mi)

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT3D_x_4DS6d51LKJ7ze1sxT5WpV5uiSVOFYHLwBiGru6vFyVv5h5-83AwFjxWYiWfCDjDAaarHAV-k/pub?gid=0&single=true&output=csv"
df = pd.read_csv(url)
print(df.head())

#1
''' Use the football dataset. Find out the total percentages that each team made on target. Display the result as a python dictionary where the keys are the team list and the values are the percentage values. Round off the percentage values up to 2 decimal places.
Help:

First, find out how many total teams are participated in this worldcup. For that, you can use unique() method on the column "Team" or "Against".
Loop through the teams list that you have found in previous section, and then filter the dataset according to that. After filtering the dataset, find out total attempts sum and total on target sum.
After getting these values, find out the percentage by total on target divided by total attempts and multiply by 100. And store to a python dictionary where the key will be the team name and the values will be the percentages.
At the end,sort the dictionary by the values (not by the keys) and print the result.'''

teams=df['Team'].unique()
on_target_percentage={}
for team in teams:
    on_target=df[df['Team']==team]['On Target'].sum()
    total_attempts=df[df['Team']==team]['Total Attempts'].sum()
    on_target_percentage[team]=round(on_target/total_attempts*100,2)
sorted_dict=dict(sorted(on_target_percentage.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict)



#2
'''Find out how many times the teams are played in this Fifa Worldcup-2022. On top of this, find out the ranks of the teams.
Note: The DataFrame.rank() method takes an optiinal parameter named method. This parameter takes different values, but one of them is average which is by-default. So, when you do the rank, you will get some 2.5 like floating values. But if you change the value as first, then you will get in integers but the datatype will be float. So, try with method="first" parameter. '''
print(df['Team'].nunique())
r=df['Team'].value_counts().rank(method='first')
print(r)



#3
'''Find out these below topics:
The information about the Fifa worldcup dataset.
The description about the Fifa worldcup dataset
Check is there any missing values, if there is any missing values, fill that value with the average value for that particular column.
Drop all the duplicate rows permanently.
Drop the columns: "Sl No", "Match No.", "Red Cards" and "Pts" permanently. '''

#(i)
info=df.info()
print(info)

#(ii)
des=df.describe()
print(des)

#(iii)
na=df.isnull().sum()
print(na)

#(iv)
df.drop_duplicates(inplace=True)

#(v)
df.drop(columns=["Sl. No", "Match No.", "Red Cards" , "Pts"],inplace=True)
print(df)


#4
'''Do these below operations:
Find out the rank based on the "Team" column and save the result by adding a new column named "Rank".
Change the datatype of this column to integer by using np.int16
Set the index of the DataFrame by using this "Rank" column permanently.
After that, sort the dataframe based on the "Rank" index. '''

#(i)
df['Rank']=df['Team'].rank(method='first')
print(df['Rank'])

#(ii)
df['Rank']=df['Rank'].astype(np.int16)
print(df['Rank'].dtype)

#(iii)
df.set_index(df['Rank'],inplace=True)
print(df.index)

#(iv)
df.sort_index(inplace=True)
print(df)

#downloading dataset 2
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQjh5HzZ1N0SU7ME9ZQRzeVTaXaGsV97rU8R7eAcg53k27GTstJp9cRUOfr55go1GRRvTz1NwvyOnuh/pub?gid=1562145139&single=true&output=csv'
d1=pd.read_csv(url)
print(d1.head())

#downloading dataset 3
url='https://docs.google.com/spreadsheets/d/e/2PACX-1vQcPvQsSC9aNFogvbUG08nu0bGHlOclGYaOlhND_LE5Ff7ZnHQ5VYzAgpyT5XNklgiT54SsNgHePsUa/pub?gid=1656109608&single=true&output=csv'
d2=pd.read_csv(url)
print(d2.head())


#5
'''Do the below tasks:
With dataset 1, drop those records which only have missing values of the "Age" column permanently.

With the dataset 2, fill the missing values with 20 to the only "Age" column permanently.'''

#(i)
d1['Age'].dropna(inplace=True)

#(ii)
d2['Age'].fillna(20, inplace=True)

#downloading ipl dataset
ipl= "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
ipl=pd.read_csv(ipl)
print(ipl.head(2))

#6
'''Make a dataframe of each team in IPL with details like - Team Name, Matches Played, Win%, Home Win%, Away Win%.
Show sorted dataframe on Win%

Replace old team name as new name before performing any tasks.

Delhi Daredevils ->Delhi Capitals
Kings XI Punjab -> Punjab Kings
Rising Pune Supergiants -> Rising Pune Supergiant
Note: Team1 represents Home team. Exclude not result matches. '''

#replace
ipl['Team1'].replace({'Delhi Daredevils':'Delhi Capitals', 'Kings XI Punjab': 'Punjab Kings', 'Gujarat Lions':'Gujarat Titans', 'Pune Warriors':'Rising Pune Supergiant','Rising Pune Supergiants':'Rising Pune Supergiant', },inplace=True)
ipl['Team2'].replace({'Delhi Daredevils':'Delhi Capitals', 'Kings XI Punjab': 'Punjab Kings', 'Gujarat Lions':'Gujarat Titans', 'Pune Warriors':'Rising Pune Supergiant','Rising Pune Supergiants':'Rising Pune Supergiant', },inplace=True)

data=[]
df=ipl[~ipl['WinningTeam'].isna()]
teams=df['Team1'].unique()
for team in teams:
  played=df[(df['Team1']==team) | (df['Team2']==team)].shape[0]
  wins=df[df['WinningTeam']==team].shape[0]/played*100
  home_win=df[(df['WinningTeam']==team) | (df['Team1']==team)].shape[0]/df[df['Team1']==team].shape[0]*100
  away=df[(df['WinningTeam']==team) | (df['Team2']==team)].shape[0]/df[df['Team2']==team].shape[0]*100
  data.append([team,played,wins,home_win,away])
new_df=pd.DataFrame(data, columns=['Team', 'Played', 'Win', 'Home Win', 'Away Win'])
new_df.sort_values('Win', inplace=True, ascending=False)
print(new_df)

#7
#Venues with most "no result" matches.

v=ipl[ipl['WonBy']=='NoResults'].Venue.value_counts().index[0]
print(v)

#8
#Player with most appearance in final match.
'''Team1Players and Team2Players have all players name. It is not a list of players name instead it is str. So handle it as string.
Hint: split and strip will help; Make a series of all players in final and do value counts'''

new=pd.Series()
df_final=ipl[ipl['MatchNumber']=='Final']
def get_player(l):
    return pd.Series(list(map(lambda x: x.strip("'"),l.strip("'[").rstrip("]'").split(', '))))
for player in df_final['Team1Players']:
    x=get_player(player)
    new=pd.concat([new, x])
for player in df_final['Team2Players']:
    x=get_player(player)
    new=pd.concat([new, x])

print(new.value_counts().head())


#9
''' IPL Point Table
Make a function point_table which take season as parameter and show points table in non-ascendng order of points and in ascending order of team name.

For winning - 2 Ponits; For loosing - 0 Point For not result both team gets 1 points.

Make dataframe which will have TeamName MatchesPlayed MatchesWon NoResult Points make TeamName as index.

season parametr should be one of these->
['2022', '2021', '2020/21', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2009/10', '2009', '2007/08']
Output of two Top 2 in season 2022

TeamName    MatchesPlayed    MatchesWon    NoResult    Points

Gujarat Titans        16       12           0         24
Rajasthan Royals      17       10           0         20'''

def played(df, team):
    return df[(df['Team1']==team) | (df['Team2']==team)].shape[0]

def win(df, team):
    return df[df['WinningTeam']==team].shape[0]

def no_result(df, team):
 return df[((df['Team1']==team) | (df['Team2']==team)) & (df['WinningTeam'].isnull())].shape[0]

def points(season):
    df=ipl[ipl['Season']==season]
    new_df=pd.DataFrame()
    new_df['Team']=df['Team1'].unique()
    new_df['Played']=new_df['Team'].apply(lambda x: played(df, x))
    new_df['Win']=new_df['Team'].apply(lambda x: win(df, x))
    new_df['No Result']=new_df['Team'].apply(lambda x: no_result(df, x))
    new_df['Points']=new_df['Win']*2 +new_df['No Result']
    new_df.sort_values('Points', ascending=False, inplace=True)
    new_df.set_index('Team', inplace=True)
    return new_df

print(points('2022'))



#10
'''IPL Point Table cont.
Extend the above IPL Point Table with an extra column as SeasonPosition

Team below top 4 after sorting on Points and then on TeamName Will have same SeasonPosition as there rank. use rank function.

Teams in Top four will have SeasonPosition as:

    'Winner' - Team won final
    'Runner' - Team lost Final
    3 - Losing Team in Qualifier2
    4 - Losing Team in Eliminator
For changing value of pariticular cell use df.at[row_index, col_label] = value

Output of two Top 2 in season 2022. Your result should have all teams.

TeamName    MatchesPlayed    MatchesWon    NoResult    Points   SeasonPosition

Gujarat Titans        16       12           0         24         Winner
Rajasthan Royals      17       10           0         20         Runner
Note: If you try to chnage value of view of any dataframe a warnig will be shown. To avoid it, make a copy of the dataframe you want to change in by df.copy()'''


def points_extension(season):
    df=ipl[ipl['Season']==season].copy()
    df2=points(season)
    df2['SeasonPosition']=df2['Points'].rank(ascending=False,method='first').astype('object')
    df['LossingTeam'] = pd.concat([df[df['WinningTeam']==df['Team1']]['Team2'], df[df['WinningTeam']==df['Team2']]['Team1']])
    final=df[df['MatchNumber']=='Final']
    winner=final['WinningTeam'].values[0]
    runner=final['LossingTeam'].values[0]
    df2.at[winner, 'SeasonPosition']='Winner'
    df2.at[runner, 'SeasonPosition']='Runner'
    q=df[df['MatchNumber']=='Qualifier 2']
    e=df[df['MatchNumber']=='Eliminator']
    third=q.LossingTeam.values[0]
    fourth=e.LossingTeam.values[0]
    df2.at[third, 'SeasonPosition']='Third'
    df2.at[fourth, 'SeasonPosition']='Fourth'
    return df2

print(points_extension('2022'))

