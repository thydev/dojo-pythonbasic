words = "It's thanksgiving day. It's my birthday,too!"
# print the position of the first instance of the word "day"
print words.find("day")

x = [2,54,-2,7,12,98]
# Print the min and max values
print max(x)
print min(x)

x = ["hello",2,54,-2,7,12,98,"world"]
# Print the first and last values
print x[0]
print x[len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
# Sort your list first. Then, split your list in half. 
# Push the list created from the first half to position 0 of the list created from the second half. 
# The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
x.sort()
firsthalf = x[0 : len(x)/2]
secondhalf = x[len(x)/2 : len(x)]
print x
print firsthalf
print secondhalf
secondhalf.insert(0, firsthalf)
print secondhalf
