def count():
    a = [[0, 0], [0, 0], [0, 0], [0, 0], [0,0]]  # [[[2, 4], [4, 4], [5, 4]], [[2, 1], [6, 4], [7, 4], [8, 4], [9, 1]], [[6, 3], [10, 4], [11, 4], [13, 4], [14, 4]]]
    list=[[1,2],[1,3],[1,6],[2,6],[2,6]]
    for list1 in list:
        for count in range(5):
            if a[count][0] == list1[0]:
                a[count][1] = a[count][1] + 1
                break
            elif a[count][0] == 0:
                a[count][0] = list1[0]
                a[count][1] = a[count][1] + 1
                break
            print(count)
            print(a)
from itertools import combinations
def zi():
    list=[[6, 4], [6, 3], ['A', 2],[2, 3], [3, 1], [5, 4], ['Q', 4], ['Q', 3], [7, 1], [8, 3], [10, 4], [10, 3], [10, 2]]
    for i in combinations(list,5):
        #print(i)
        if i ==([6,4],[6,3],[10,4],[10,3],[10,2]):
            print(i)
            print(1)


