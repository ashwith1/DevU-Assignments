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



