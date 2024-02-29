def remove_duplicates(arr):
    if not arr:
        return []

    unique_arr = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])

    return unique_arr

# Example usage:
array = [15, 14, 25, 14, 32, 14, 31]
sorted_array = sorted(array)  # Ensure array is sorted
unique_array = remove_duplicates(sorted_array)
print("Array with duplicates removed:", unique_array)
