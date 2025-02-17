def quicksort(lst):
    if (len(lst)<=1):
        return lst
    pivot = lst[len(lst) // 2]

    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quicksort(left)+middle+quicksort(right)

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]