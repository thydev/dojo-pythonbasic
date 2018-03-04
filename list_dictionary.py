# Create a function that takes in two lists and creates a single dictionary. 
# The first list contains keys and the second list contains the values. 
# Assume the lists will be of equal length.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar","Dojo", "coding"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "fish"]
# print zip(name, favorite_animal) # Create Tuple

def make_dict(list1, list2):
    new_dict = {}
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            new_dict[list1[i]] = list2[i]
    elif len(list1) > len(list2):
        for i in range(0, len(list1)):
            if i < len(list2):
                new_dict[list1[i]] = list2[i]
            else:
                new_dict[list1[i]] = ""
    else:
        for i in range(0, len(list2)):
            if i < len(list1):
                new_dict[list2[i]] = list1[i]
            else:
                new_dict[list2[i]] = ""

    return new_dict

d = make_dict(name, favorite_animal)
print d