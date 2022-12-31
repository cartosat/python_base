def search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return f"Target found at {i}"

    return f"{target} Not Found"

arr = [2, 3, 4, 10, 40]

print(search(arr, 40))
