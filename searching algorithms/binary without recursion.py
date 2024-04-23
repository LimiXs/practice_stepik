data = [3, 1, 3, 4, 5, 53, 5, 7, 1, 9]
data.sort()

n = len(data)

search_v = 9
left, right = 0, n - 1

while left <= right:
    middle = (left + right) // 2
    value = data[middle]
    if value == search_v:
        print(f"value - {value}, index - {middle}")
        break
    elif value < search_v:
        left = middle + 1
    elif value > search_v:
        right = middle - 1
else:
    print('Value not found')
