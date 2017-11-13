def mergesort(numbers):
    # check for the empty list or the list with single element
    if not numbers or len(numbers) == 1:
        return numbers
    # recursive splitting (Divide)
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)


def merge(left, right):
    # left and right are the sorted lists to be merged
    # The merged list after sorting
    merged = []
    # Loop till left or right becomes empty
    while left and right:
        # remove the minimum of left[0] and right[0]
        # and add it to the merged list
        if left[0] < right[0]:
            merged += [left.pop(0)]
        else:
            merged += [right.pop(0)]
    # add the remaining elements of left, if any
    merged += left
    # add the 
    return merged #remaining elements of right, if any
    merged += right




numbers = [-3,-5,-7,-8]
print(mergesort(numbers))

