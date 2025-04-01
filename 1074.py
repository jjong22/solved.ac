"""
M = A B
    C D
"""

def calculate_nth_count(N, r, c):
    m = 2 ** (N - 1)
    
    if N == 0:
        return 0
    
    if r < m and c < m: # A
        return calculate_nth_count(N - 1, r, c)
    elif r < m and c >= m: # B
        return m * m + calculate_nth_count(N - 1, r, c - m)
    elif r >= m and c < m: # C
        return 2 * m * m + calculate_nth_count(N - 1, r - m, c)
    else: # D
        return 3 * m * m + calculate_nth_count(N - 1, r - m, c - m)

N, r, c = map(int, input().split())
print(calculate_nth_count(N, r, c))