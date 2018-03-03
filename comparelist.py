def comparelist(lst1, lst2):
    if (len(lst1) != len(lst2)):
        print "The lists are not the same."
    else:
        isIdentical = True
        i = 0
        while i < len(lst1):
            if lst1[i] != lst2[i]:
                isIdentical = False
                break
            i += 1
        if isIdentical:
            print "The lists are the same."
        else:
            print "The lists are not the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
comparelist(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
comparelist(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
comparelist(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
comparelist(list_one, list_two)
