# Pascal's pyramid
# 5/23/17 Jeju National University
# Jungju Kim

from datetime import datetime

def r_triangle(i, j):                       # Pascal's triangle - recursive
    if j < 0 or j > i:                      # Returning 0 outside of the triangle
        return 0
    elif j == 0:                            # Returning 1 on row 0
        return 1
    else:
        return r_triangle(i - 1, j - 1) + r_triangle(i - 1, j)

def pascals_triangle(n):
    for i in range(n + 1):
        print(str(i).rjust(2) + ':'+str('').rjust((n - i) * 3), end = '')
        # Row index에 이어서 전체 모습을 삼각형 처럼 보이게 하기 위한 공백을 출력한다
        for j in range(i + 1):
            print(str(r_triangle(i, j)).rjust(6), end='')
        print()

def r_pyramid(l, i, j):                     # Pascal's pyramid - recursive
    if j < 0 or j > i or i < 0 or i > l:    # Returning 0 outside of the pyramid
        return 0
    elif l == 0:                            # Returning 1 on row 0
        return 1
    else:
        return r_pyramid(l - 1, i - 1, j - 1) + r_pyramid(l - 1, i - 1, j) + r_pyramid(l - 1, i, j)

PascalsPyramid = [[[1]]]

def d_pyramid(l, i, j):                     # Pascal's pyramid - dynamic
    if j > i or i > l:                      # Returning 0 outside of the pyramid
                                            # Unstable when l, i, j < 0
        return 0
    else:
        if len(PascalsPyramid) <= l:
            PascalsPyramid.append([[d_pyramid(l - 1, 0, 0)]])
                                            # Recursive call to build up layers upto l - 1
            for a in range(1, l + 1):
                PascalsPyramid[l].append([PascalsPyramid[l - 1][a - 1][0] + d_pyramid(l - 1, a, 0)])
                for b in range(1, a + 1):
                    p = PascalsPyramid[l - 1][a - 1][b - 1] + d_pyramid(l - 1, a - 1, b) + d_pyramid(l - 1, a, b)
                    PascalsPyramid[l][a].append(p)
        return PascalsPyramid[l][i][j]

def pascals_pyramid(title, function, n):
    print(title)
    print('---')
    start_time = datetime.now()
    for l in range(n + 1):          # Layer
        print('Layer '+str(l))
        for i in range(l + 1):      # Row
            print(str(i).rjust(2) + ':'+str('').rjust((l - i) * 3), end = '')
            # Row index에 이어서 전체 모습을 삼각형 처럼 보이게 하기 위한 공백을 출력한다
            for j in range(i + 1):  # Column
                print(str(function(l, i, j)).rjust(6), end='')
            print()
        print()
    print('Duration {}'.format(datetime.now() - start_time))

print("Pascal's triangle")
print("---")
pascals_triangle(15)

print()

pascals_pyramid("Pascal's pyramid - recursive", r_pyramid, 12)
print()
pascals_pyramid("Pascal's pyramid - dynamic programming", d_pyramid, 12)