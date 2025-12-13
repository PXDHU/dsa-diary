def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        min_index = i # Assume current index is the minimum

        # Find the minimum element in the remaining array
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first element of the unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr1 = [3, 4, 2, 9, 5, 1]

print(selection_sort(arr1))
