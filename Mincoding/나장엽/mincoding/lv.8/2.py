arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 7:
        break
    print(arr[i], end=' ')