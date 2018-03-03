def findcharacter(lst, cha):
    new_list = []
    for el in lst:
        if el.find(cha) >= 0:
            new_list.append(el)
    
    print new_list

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
findcharacter(word_list, char)
# output
# new_list = ['hello','world']
