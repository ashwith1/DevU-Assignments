#***************************************************************************************************************

# 1)fill a list with inputs provided by the user

list = []
n = int(input("Enter number of elements: "))

for i in range(1,n+1):
    ele = int(input())

    list.append(ele)

print(list)

#*****************************************************************************************************************

# 2)find the max and min number from a list

l = [8,9,-4,-6,13]
i=1

for i in range(len(l)):
    if l[i-1] > l[i]:
        max = l[i-1]
        min = l[i]

    else:
        max = l[i]
        min = l[i-1] 

print("The max element is ", max)
print("The min element is ", min)

#******************************************************************************************************************

# 3)How many odds and evens are there in the list

lis = [ 2, 3, 12, 23, 36, 45 ]
even_count, odd_count = 0, 0

for i in range(len(lis)):
    if lis[i] % 2 == 0:
        
        even_count +=1
        

    else:
        
        odd_count += 1

print("the number of even count: ", even_count)
print("the number of odd count: ", odd_count) 


#************************************************************************************

# 4)separate positive from negative - in the same list and in a different list.

li = [-6, 4, 1, 3, -20, 16]
positive = []
negative = []

for i in range(len(li)):
    if li[i] >= 0:
            positive.append(li[i])

    else: 
            negative.append(li[i])

print("The positive list is: ", positive)
print("The negative list is: ", negative)

#********************************************************************************

# 5)output the items that are larger than the arithmetic mean of the list.

list = [20, 50, 12, 5, 30, 1, 90, 2]
n=len(list)
am, a = 0, 0
greater = []
for i in range(len(list)):

    a += list[i]
    am = a / n

for i in range(len(list)):
    if list[i]>am:
        greater.append(list[i])

print("The output is: ", greater)

#**********************************************************************************

# 6)number of elements that belongs to an inputted range.

list_range = [-5, 20, 2, 100, 50, -20, 4, 10, 500]
count = 0

a = int(input("upper limit for range: "))
b = int(input("lower limit for range: "))

for i in range(len(list_range)):
    if list_range[i] < a and list_range[i] > b:

            count += 1

print("The number of elements in the range are: ", count)

#**************************************************************************************888

# 7)distribution of values by ranges

list_rang = [-5, 20, 2, 100, 50, -20, 4, 10, 500]

range_list = []

a = int(input("upper limit for range: "))
b = int(input("lower limit for range: "))

for i in range(len(list_rang)):
    if list_rang[i] < a and list_rang[i] > b:

            range_list.append(list_rang[i])

print("elements in the range are: ", range_list)

#*********************************************************************************

# 8)replacing list items

replace_list = [-5, 20, 2, 100, 50, -20, 4, 10, 500]

for i in range(len(replace_list)):
    if replace_list[i] > 0:
        replace_list[i] = 1

    elif replace_list[i] == 0:
        replace_list[i] = 0

    else:
        replace_list[i] = -1


print("The replaced list is: ", replace_list)

#*********************************************************************************

# 9) reversing the list.

reverse_list = [-5, 20, 2, 100, 50, -20, 4, 10, 500]

print("The reverse list is: ", reverse_list[::-1])

#********************************************************************************8

# 10) checking the file extention



#*************************************************************************************

#11)longest word in a string



#*************************************************************************************

#12)convert test to word with punctuation removed


#*************************************************************************************

#13) intersection of lists - find the common item from 2 or more than 2 lists


#*************************************************************************************

#14) most common word/letter in a list


#*************************************************************************************

#15)bubblesort


#*************************************************************************************

#16) selection sort


#*************************************************************************************

#17)binary search - find the number in an ordered array


#*************************************************************************************

#18)sieve of eratosthenes


#*************************************************************************************

#19)sorting words in a list - ascending and descending order



#*************************************************************************************
