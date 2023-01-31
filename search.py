#naive search
import random
import time

def naive_search(sorted_list,target):
    for i in range(len(sorted_list)):
        if sorted_list[i]==target:
            #print(i)
            return i
    return -1

#binary search
def binary_search(l,target,low=None,high=None):
    if high >= low:
        mid =(low+high)//2
    if high<low:
        return -1
    if l[mid]==target:
        return mid 
    elif l[mid]>target:
        return binary_search(l,target,low,mid-1)
    else :
        return binary_search(l,target,mid+1,high)


#l = [3, 4, 5, 6, 7, 8, 9]
target = 9000
length=10000
sorted_list=set()
while len(sorted_list) <length:
    sorted_list.add(random.randint(-3*length,3*length))
sorted_list=sorted(list(sorted_list))
result = binary_search(sorted_list,target, 0, len(sorted_list)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
result=0

start=time.time()
for target in sorted_list:
   naive_search(sorted_list,target) 
end=time.time()
print("naive search time:",(end-start)/length,"seconds")


start=time.time()
for target in sorted_list:
   binary_search(sorted_list,target, 0, len(sorted_list)-1) 
end=time.time()
print("binary search time:",(end-start)/length,"seconds")