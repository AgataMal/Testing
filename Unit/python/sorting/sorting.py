def bubble_sort(arr):
    count = 0
    need_iteration = 'true'
    while need_iteration == 'true':
        need_iteration = 'false'
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    need_iteration = 'true'
                    count +=1
 
    return count