def merge_sort(list):
    if len(list) <= 1:
        return list

    # Find the middle of the list
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    print(left_half, right_half)
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any leftovers. Because we've exhausted one list, we know it is empty and that
    # the remainder of the other list is sorted
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Test the function
numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)