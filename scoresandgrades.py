# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what the grade is 
# for a particular score. Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random

def scoregrade():
    print "Scores and Grades"
    for i in range(0, 10):
        score = random.randint(60, 100)
        if score >= 60 and score < 70:
            print "Score: {0}; Your grade is D".format(score)
        elif score >= 70 and score < 80:
            print "Score: {0}; your grade is C".format(score)
        elif score >= 80 and score < 90:
            print "Score: {0}; your grade is B".format(score)
        elif score >= 90 and score <= 100:
            print "Score: {0}; your grade is A".format(score)
    print "End of the program. Bye!"

scoregrade()