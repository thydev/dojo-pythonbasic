student = {
    "name": "Toto",
    "age": 12,
    "country": "USA",
    "favorite_lang": "Python"
}

print "My name is", student["name"]
print "My age is", student["age"]
print "My country is", student["country"]
print "My favorite language is", student["favorite_lang"]

def print_dict(oDict):
    for item in oDict:
        print item
    
    for k in oDict.iterkeys():
        print k
    
    for val in oDict.itervalues():
        print val
    
    for key, data in oDict.iteritems():
        print key, " = ", data

    print oDict.items()
    print oDict.keys()
    print oDict.values()

print_dict(student)