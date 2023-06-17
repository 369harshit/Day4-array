from typing import List

def solve(a: List[int]) -> int:
    maxx = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 0:
                maxx = max(maxx, j-i+1)
    return maxx

if __name__ == "__main__":
    a = [9, -3, 3, -1, 6, -5]
    print(solve(a))