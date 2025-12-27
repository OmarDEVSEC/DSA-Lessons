#BinarySearch Alice Problem

#QUESTION 1: Alice has some cards with numbers written on them. 
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. 
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

#Visual of the alice problem, decending list and using binary search
#[12,11,10,9,8,7,6,5,4,3,2,1] - Sorted list
# [0,1,2,3,4,5,6,7,8,9,10,11,12] - Positions of sorted list 

#Here's a systematic strategy we'll apply for solving problems:

#1.State the problem clearly. Identify the input & output formats.
#2.Come up with some example inputs & outputs. Try to cover all edge cases.
#3.Come up with a correct solution for the problem. State it in plain English.
#4.Implement the solution and test it using example inputs. Fix bugs, if any.
#5.Analyze the algorithm's complexity and identify inefficiencies, if any.
#6.Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
#Applying the right technique" is where the knowledge of common data structures and algorithms comes in handy.


#Test Case Tip: Represent test cases as dictionaries
 
tests = []

#Query occurs in the middle of the set
tests.append({
    'input':{
        'cards': [13,11,10,7,4,3,1,0],
        'query': 1
    },
    'output': 6
})

#Query the first element of the set

tests.append({
    'input':{
        'cards': [4,2,1,-1],
        'query': 4
    },
    'output': 0
})

#Query occurs in the last element
tests.append({
    'input':{
        'cards': [3,-1,-9,-127],
        'query': -127
    },
    'output': 3
})

#quert contains just one element
tests.append({
    'input':{
        'cards': [6],
        'query': 6
    },
    'output': 0
})


def locate_card(cards,query):
    #create a variable position 0
    position = 0

    #set up a loop for repition
    while True:
        #Check if elment of the current position matches the query
        if cards[position] == query:
            #Answer found
            return position
        #increment the position
        position += 1

        #check if you have reached the end of the array
        if position == len(cards):
              #number not found
              return -1  
#run and print test results
for i, test in enumerate(tests):
     result = locate_card(test['input']['cards'], test['input']['query'])
     print(f"Test {i+1}: Expected {test['output']}, Got {result}, {'PASS' if result == test['output'] else 'FAIL'}")

#Binary search complete, make sure to review at the end to check for printing
# and test results
