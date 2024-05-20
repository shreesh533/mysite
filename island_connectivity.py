
number_of_islands = 0
global_largest_island = 0
local_largest_island = 0

for i in range(len(input)):
    for j in range(len(input)):
        # If the current indexed number is an island, check the right element and bottom element:
        source_index = [i]
        
        if input[i][j]:
            local_largest_island += 1
            # If the right element in the matrix is also 1, then keep going right:
            if not input[i][j+1]:
                break
        else:
            if i > 1 and j > 1 and input[i-1][j] or input[i][j-1]:
                number_of_islands += 1
                global_largest_island = max(local_largest_island, global_largest_island)