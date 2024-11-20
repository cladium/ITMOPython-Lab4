MAX_CAPACITY = 8

items = [
    ('r', 3, 25),
    ('p', 2, 15),
    ('a', 2, 15),
    ('m', 2, 20),
    ('i', 1, 5),
    ('k', 1, 15),
    ('x', 3, 20),
    ('t', 1, 25),
    ('f', 1, 15),
    ('d', 1, 10),
    ('s', 2, 20),
    ('c', 2, 20)
]

def new_print_items_table(items, row_capacity=4):
    items = sorted(items, key=lambda x: x[1], reverse=True)
    
    current_row = []
    remaining_capacity = row_capacity
    # while there are items left to place
    while items:
        found_fit = False
        
        for name, size, value in items[:]:
            if size <= remaining_capacity:
                # if the item fits in the remaining capacity, add it to the row
                current_row.extend([f'[{name}]'] * size)
                remaining_capacity -= size
                items.remove((name, size, value))
                found_fit = True
                # break because we found a fitting object, and we need to check the remaining space
                break
    
        # if no object can fit in the remaining space, print the current row and start a new one
        if not found_fit:
            print(' '.join(current_row))
            current_row = []
            remaining_capacity = row_capacity
            
    # print any remaining objects in the last row
    if current_row:
        print(' '.join(current_row))

# table for dynamic programming
n = len(items)
dp = [[0] * (MAX_CAPACITY + 1) for _ in range(n + 1)]

# filling the table
for i in range(1, n + 1):
    item_name, item_weight, item_value = items[i - 1]
    for w in range(1, MAX_CAPACITY + 1):
        if item_weight <= w:
            # if it fits
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_weight] + item_value)
        else:
            # if it doesn't, take value from previous row
            dp[i][w] = dp[i - 1][w]

# find selected items
w = MAX_CAPACITY
selected_items = []
counter = 0
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        item_name, item_weight, item_value = items[i - 1]
        selected_items.append(items[i - 1])
        w -= item_weight

new_print_items_table(selected_items, 4)
print("Итоговые очки выживания:", dp[n][MAX_CAPACITY])