#your'e given with a comma seperated natural numbers 1 to 10 print th even numbers
'''my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i],end=" ")   '''
#7.2 How many even no are there in the above question
'''my_list=list(map(int,input().split(",")))
count=0
for i in range(1,len(my_list),2):
    count+=1
print(count)'''
#7.3  your'e given with a space seperate interger list find no of even elements no of odd elements in a given list
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range (0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)

my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in my_list:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print(even)
print(odd)