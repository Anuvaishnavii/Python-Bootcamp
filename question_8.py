#8. given an space seperated integer list find the average of elements present in the even index
'''my_list=list(map(int,input().split(" ")))
sum=0
n=len(my_list)
for i in range(0,len(my_list),2):
    sum+=my_list[i]
    avg=sum//(n//2)
print(avg)'''

'''my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
 if(i%2==0):
    sum+=my_list[i]
    count+=1
print(sum/count)'''
my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    sum+=my_list[i]
    count+=1
print(sum/count)