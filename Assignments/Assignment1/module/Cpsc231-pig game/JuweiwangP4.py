import sys
import random

global one_number_6_round
one_number_6_round = 0
global Estimated_likelihood
Estimated_likelihood = 0
global one_number_12_round
one_number_12_round = 0
global Estimated_likelihood2
Estimated_likelihood2 = 0

def one_round_six():
    global one_number_6_round
    global count1
    global Estimated_likelihood
    count1 = 6
    while (count1 != 0):
        count1 = count1 - 1
        yours = random.randrange(1, 7)
        if (yours == 1):
            one_number_6_round = one_number_6_round + 1
        Estimated_likelihood = (one_number_6_round / 6 )

def one_round_12():
    global one_number_12_round
    global Estimated_likelihood2
    global count2
    count2 = 12
    while (count2 != 0):
        count2 = count2 - 1
        mine = random.randrange(1, 7)
        if (mine == 1):
            one_number_12_round = one_number_12_round + 1
            if (one_number_12_round <= 1):
                Estimated_likelihood2 = 0
            else :
                Estimated_likelihood2 = (one_number_12_round / 12)



one_round_six()
one_round_12()


print('Estimated likelihood of 1 once in 6:', Estimated_likelihood)
print('Estimated likelihood of 1 twice in 12:', Estimated_likelihood2)
if (Estimated_likelihood == Estimated_likelihood2):
    print('''Conclusion: There is no difference between Estimated likelihood of 1 once in
          and Estimated likelihood of 1 twice in 12 ''')
elif (Estimated_likelihood <= Estimated_likelihood2):
    print('''Conclusion: Rolling 12 times is more likely to get more one''')
else:
    print('''Conclusion: Rolling 6 times is more likely to get more one''')



