class BubbleSort:
    def bubble_sort(self, arr):
        n = len(arr)

        
        for i in range(n-1, -1, -1):

            for j in range(i):

                if arr[j] >  arr[j+1]:

                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

sorter = BubbleSort()

arr1 = [13, 46, 24, 52, 20, 9]

print(sorter.bubble_sort(arr1))