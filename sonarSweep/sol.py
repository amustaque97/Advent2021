with open('input.txt', encoding='utf-8') as f:
    list_arr = [int(num.strip()) for num in f.readlines()]
    list_arrr = list(map(int, list_arr))

    count = sum(prev < curr for prev, curr in zip(list_arr, list_arr[1:]))

    sliding_arr = [sum(sub_arr) for sub_arr in zip(list_arr, list_arr[1: ], list_arr[2: ])]
    sliding_count = sum(prev < curr for prev, curr in zip(sliding_arr, sliding_arr[1:]))

print(count)
print(sliding_count)
