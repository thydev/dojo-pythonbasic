# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
def dicttotuple(mydict):
    # return mydict.items()
    tup = []
    for k, data in mydict.items():
        tup.append((k, data))

    return tup
print dicttotuple(my_dict)

# mytu = ("key", "avlaue")
# print mytu