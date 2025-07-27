class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            mini = i
            for j in range(i+1,len(arr)):
                if arr[mini] > arr[j]:
                    mini = j
            arr[mini],arr[i] = arr[i],arr[mini]
        return arr