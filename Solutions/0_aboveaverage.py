# This is the main function, this is 100% not neccessary to have but 
# i like to do it as it makes things seem neater to me
def main():
  # Get how many test cases there is
  # Using the int function here is important as all inputs are strings
  # But we want to use this input as a number to we cast it to an int
  # Be sure if an input is a decimal to cast it using float NOT int
  C = int(input())

  # This is the loop for each test case
  # for every number between 0 and C 
  # if C = 3 then i would go 0, 1, 2
  for i in range(C):
    # Get the next line of input
    line = input()

    # Each piece of information is seperated by a space so we need to split
    # the string on every space
    # Python has a function for this: split
    # This will split the string into an array on each of the character you give it
    # The string will be split by a " "  
    values = line.split(" ")
    # printing this will now return ["x", "y", "z"] but with actual numbers
    # Again we need these as numbers not strings, so we cast each index to a int
    # len gives the length of the array values
    for i in range(len(values)):
      values[i] = int(values[i])

    # The first value on a line is the number of values so we will get this number
    N = values[0]

    # Below uses array splicing to remove this first number as its not a student score
    # This means take every value from the values from index 1 to the end

    studentScores = values[1:]

    # Now onto solving the problem
    # This problem wants us to 
    for score in studentScores:
      


    



main()
