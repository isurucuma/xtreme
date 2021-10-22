import numpy as np
# Longest common subsequence

str1 = "stone"
str2 = "longest"

def get_longest_subsequence(str1, str2):
    (long, short) = (str1, str2) if len(str1) > len(str2) else (str2, str1)    

    table = np.zeros((len(short) + 1, len(long) + 1))

    for i in range(len(short)):
        for j in range(len(long)):
            if short[i] == long[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    idx = []    

    # Backtracking algorithm
    def get_indices_of_longest(table, idx, i, j):
        if i == 0 or j == 0:
            return
        if table[i][j] == table[i][j - 1]:
            get_indices_of_longest(table, idx, i, j - 1)
        else:
            # diagonal movement
            idx.append(j)
            get_indices_of_longest(table, idx, i - 1, j - 1)

    get_indices_of_longest(table, idx, table.shape[0] - 1, table.shape[1] - 1)

    longest_seq = "".join([long[s - 1] for s in idx[::-1]])
    return(longest_seq)

print(get_longest_subsequence(str1, str2))