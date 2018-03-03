#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
def typelist(lst):
    str_l = ""
    sum_l = 0
    for el in lst:
        # print el, type(el)
        if type(el) is int or type(el) is float:
            sum_l += el
        elif type(el) is str:
            str_l += el + " "

    if str_l != "" and sum_l != 0:
        print "The lise you enterd is mixed type"
        print "String:", str_l
        print "Sum:", sum_l, "\n"
    elif sum_l != 0:
        print "The list you entered is of integer type"
        print "Sum:", sum_l, "\n"
    elif str_l != "":
        print "The list you entered is of string type"
        print "String:", str_l, "\n"



typelist(l)

# input
l = [2,3,1,7,4,12]
typelist(l)
# #output
# "The list you entered is of integer type"
# "Sum: 29"

# input
l = ['magical','unicorns']
typelist(l)
# #output
# "The list you entered is of string type"
# "String: magical unicorns"
