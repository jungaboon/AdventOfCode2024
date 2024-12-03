# Add list
# List has two columns in each entry, so we'll need to split them
# Each row will need to be separated into its piece

raw = '''
INSERT COLUMNS HERE (ONLY TWO COLUMNS ALLOWED)
'''
list_raw = raw.split()
list_a = []
list_b = []

for index, item in enumerate(list_raw):
    if index % 2 == 0:
        #Even is on the left column
        list_a.append(int(item))
    else:
        # Odd is on the right column
        list_b.append(int(item))
        
# Now that we have the columns on the left and right side, we need to
# loop through each to find the smallest value (small_a and small_b) on each column, and then
# subtract them (we can probably just find the absolute value for the difference)

def get_min_total(arr1, arr2):
    total = 0
    while len(arr1) > 0:
        min_a = min(arr1)
        min_b = min(arr2)
        
        total += abs(min_a - min_b)
        arr1.remove(min_a)
        arr2.remove(min_b)
    return total

def get_similarity_score(arr1, arr2):
    total = 0
    for i in arr1:
        item_i_count = 0
        for j in arr2:
            if i == j:
                item_i_count += 1
        total += i * item_i_count
    return total
    