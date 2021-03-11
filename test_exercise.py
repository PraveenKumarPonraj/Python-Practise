def my_func(str1,str2):
    n1 = len(str1)
    n2 = len(str2)

    result = ""
    i = 0
    j = 0
    while(i <= n1 - 1 and j <=  n2 - 1):
        if (str1[i] != str2[j]):
            break
        result = result + (str1[i])


        i = i + 1
        j = j + 1

    return(result)    
def func(arr,n):

    arr.sort(reverse = False)
    print(my_func(arr[0], arr[n - 1]))








if __name__ =='__main__':
    arr=["praveen","praba","prasanth"]
    n = len(arr)

    func(arr,n)    
