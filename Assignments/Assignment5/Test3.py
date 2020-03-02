test = [[2,4],[5,7],[9,0]]

def change(test):
    if len(test) >= 3:
        win = False
        count_the_same = 0
        count_the_same1 = 0
        count_the_same2 = 0
        for i in range(len(test)):
            if test[i][0] == 0:
                count_the_same += 1
            if test[i][0] == 1:
                count_the_same1 += 1
            if test[i][0] == 2:
                count_the_same2 += 1
            if count_the_same >= 3 or count_the_same1 >= 3 or count_the_same2 >= 3:
                win = True
        count_the_same = 0
        count_the_same1 = 0
        count_the_same2 = 0
        for i in range(len(test)):
            if test[i][1] == 0:
                count_the_same += 1
            if test[i][1] == 1:
                count_the_same1 += 1
            if test[i][1] == 2:
                count_the_same2 += 1
            if count_the_same >= 3 or count_the_same1 >= 3 or count_the_same2 >= 3:
                win = True
        count = 0
        for i in range(len(test)):
            if test[i] == [1, 1]:
                count += 1
            if test[i] == [0, 0]:
                count += 1
            if test[i] == [2, 2]:
                count += 1
            if count >= 3:
                win = True
        count = 0
        for i in range(len(test)):
            if test[i] == [1, 1]:
                count += 1
            if test[i] == [0, 2]:
                count += 1
            if test[i] == [2, 0]:
                count += 1
            if count >= 3:
                win = True
    return win


win2 = change(test)
print(win2)
print(__name__)