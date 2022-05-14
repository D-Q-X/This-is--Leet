```py
def bubble_sort(array):
    l=len(array)
    
    for i in range (0,l):
        for j in range(i+1,l):
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
                
    return array

```
