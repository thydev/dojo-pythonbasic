# Write a function that simulates tossing a coin 5,000 times. 
# Your function should print how many times the head/tail appears.
import random
# random_num = random.random()
# print round(random_num)
# print random.randint(0,1)
# What is the differences between these two
def cointosses(num):
    headcount = 0
    tailcount = 0
    for i in range(1, num+1):
        head = random.randint(0, 1)
        if head == 1:
            headcount += 1
            print "Attempt #{0}: Throwing a coin... It's a head! ... Got {1} head(s) so far and {2} tail(s) so far".format(i, headcount, tailcount)
        else:
            tailcount += 1
            print "Attempt #{0}: Throwing a coin... It's a tail! ... Got {1} head(s) so far and {2} tail(s) so far".format(i, headcount, tailcount)

cointosses(5000)