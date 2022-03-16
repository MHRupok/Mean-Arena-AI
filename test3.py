
a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 55, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 7, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
start_i, start_j = 1,1
end_i, end_j = 2,3





path_so_far = []


def go_to(i, j):
    global path_so_far, end_i, end_j, a, m
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a[0])-1:
        return
    # If we've already been there or there is a wall, quit
    if (i, j) in path_so_far or a[i][j] > 0:
        return
    path_so_far.append((i, j))
    a[i][j] = 2
   
    if (i, j) == (end_i, end_j):
        print("Found!", path_so_far)
        # for animate in range(10):
        #     if animate % 2 == 0:
        #         print(a)
        #     else:
        #         print(a)
        path_so_far.pop()
        return
    else:
        go_to(i - 1, j)  # check top
        go_to(i + 1, j)  # check bottom
        go_to(i, j + 1)  # check right
        go_to(i, j - 1)  # check left
    path_so_far.pop()
    # print(a, path_so_far)
    return False


go_to(start_i, start_j)