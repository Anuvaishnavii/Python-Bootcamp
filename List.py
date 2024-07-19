#list is ordered,set is always unordered
'''my_list=[1,2,4,5,7,9,-32,-76,98,69,96] 
print(*my_list) #* is used to remove square brackets
my_list.append(99999) #default insert in the last
print(my_list)
my_list.insert(3,999) #insert at specific position
print(my_list)
print(len(my_list))
my_list.pop(5)  #last element will pop out
print(my_list)
cnt=my_list.count(2)
print(cnt)
my_list_2=[6,7,8,9]
new_list=my_list.copy() #cpoying into new list
print(new_list) 


#sorting default will use quick sort alogorithm
my_list.sort()
print(my_list)
#pop default will pop last element
my_list.pop()
print(my_list)
print(*my_list) #remove braces(brackets)
my_list.pop(5)
print(*my_list) 
my_list.pop(456)
print(*my_list) '''

'''my_list=list(map(int,input().split(" ")))'''
'''my_list=list(map(int,input().split("@"))) at output dont put/give space'''
'''my_list=list(map(int,input().split(",")))
my_list.append(999)
print(*my_list)'''

#problem condition 1.append 2.pop 3.sort 4.hello length =
'''my_list=list(map(int,input().split(" ")))
choice=int(input())
if (choice==1):
    my_list.append(567)
    print(my_list)
elif(choice==2):
    my_list.pop(3)
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
else:
    print(f"Hello length is {len(my_list)}")'''

