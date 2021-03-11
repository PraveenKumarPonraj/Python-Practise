arr1 = [2,3,4,5]
target1 = 7

arr2 = [5,6,7,8]
target2 = 13

def two_sum(arr,target):
    value = dict()

    for i ,elem in enumerate(arr):
        comp = target - elem
        if comp in value:
            return [value[comp],i]
        value [elem] = i

    return []

list1 = two_sum(arr1,target1)
print(list1)

list2 = two_sum(arr2,target2)
print(list2)