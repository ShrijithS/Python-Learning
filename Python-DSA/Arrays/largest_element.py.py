arr = [10, 5, 20, 8]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)