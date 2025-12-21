def swap(arr, i, j):
    temp = arr[j]

    arr[j] = arr[i]

    arr[i] = temp

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        minimum = i

        for j in range(i+1, n):

            if arr[j] < arr[minimum]:
                minimum = j
            
        swap(arr, minimum, i)
    
    return arr

n = int(input("Enter the number of elements in the Array: "))
arr = []

for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)


print("Array before Sorting: ", arr)

print("Array after Sorting: ", selection_sort(arr))