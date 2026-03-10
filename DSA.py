
# Topic1. What are all topics in DS:
------------------------------------
# Answer: 1. time complexities
#         2. space complexities
#         3. Arrays
#         4. LinkedList
#         5. Trees
#         6. Stacks
#         7. Queue
#         8. Dynamic Programming
#         9. Graphs


# Topic2. Topics that are asked in Interview for Data Engineering:
------------------------------------------------------------------
#         1. Time Complexity
#         2. Space Complexity
#         3.  Arrays
#         4.  LinkedList
#         5.  an overview of Trees
#         6.  Dynamic Programming( 3 to 4 problems we will solve)


# Time Complexity:
------------------
#                 How much solutions takes time to get completed.
#
# suppose we have an Array of 100 elemnts(unsorted)
# 23, 12, 54,  67,  25, 89......
# Question1. can you tell the elements at index 3?
#  we can answer this question in a single search as the elements of an Array can be retrive
#  easily through index number using index slicing. we don't have to write any for loop to 
#  iterate over the array. so the time complexity is order of 1 i.e. O(1)
#
#Question2. we need to find whether element 57 is present or not?
#    if we have elemnt 57 as the first elemnt then time complexity is O(1) --> best case
#    if we do not have elemnt 57 in the array at all is O(n) ---> worst case
# it has to start seacrh from the 0th elemnt and move to next and next and so on till the last element of the Array.Since 57 elemts is 
#   not present in array it has to reach till last elemnts and then also it will not get the element. it means it has to scan all the elements 
#    Hence, the time complexity is of order of one i.e O(1)
#
#Note: we need to give answer as per the worst case scenarios always for time-complexity.
#
#
#Question3.In previuos case our Array was unsorted. Now you Array is sorted and we have 1024 elements
# Array = 2,4,7,8,12,18,26,29,32,....1000
#serach whether elemnet 18 is presnt or not in the sorted array?

#since my array is sorted, I will not go search one elemnts at a time and compare with 18. I will Optimise my search using 'Binary Search Technique'
# According to 'Binary Search Technique',
# step1: since this array is sorted, we will find the middleth number and check wheteher this number is  number to equal to 18 or not. 
#
#
#
#
#

