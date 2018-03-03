# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify 
# whether it's an odd or even number.
def odd_even():
    for c in range(1, 2001):
        if c % 2 == 0:
            print "Number is", str(c) + ". This is an even number."
        else:
            print "Number is", str(c) + ". This is an oadd number."

odd_even()

# Create a function called 'multiply' that iterates through each value in a list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
def multiply(lst, num):
    for i in range(0,len(lst)):
        lst[i] *= num
    return lst

a = [2, 4, 10, 16]
print multiply(a, 5)

# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list. 
# Here's an example:
# layered_multiples(multiply([2,4,5],3))
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def layered_multiples(arr):
  new_array = []
  for elem in arr:
        arr1 = []
        for i in range(0, elem):
            arr1.append(1)
        new_array.append(arr1)

  return new_array
  
x = layered_multiples(multiply([2,4,5],3))
print x
