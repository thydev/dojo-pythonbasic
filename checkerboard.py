
for row in range(0, 8):
    str_row = ""
    for i in range(0, 8):
        if row % 2 == 0:
            if i % 2 == 0:
                str_row += "*"
            else:
                str_row += " "
        else:
            if i % 2 != 0:
                str_row += "*"
            else:
                str_row += " "
        
    print str_row
