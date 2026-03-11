
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
#for the sorted array time complexity is = O(logn) = O(log1024) = O(10)
#
#
#Note:
------
# 1.    n+log n ~ O(n)
#       1024+log1024 ~ 1024
#
# 2.    n^2 + n +1 = O(n^2)
#      (1024)^2 +1024 +1 ~ 1024^2


#
#Question4: there is an array of 100 elements and we need to tell if there are duplicates in the array or not
#Answer4: in this case we can't use the optimisation. we have to use brute force solution
# Array = 67, 58,  54,  90,  69,  58

#  take what is the first element i.e. 67 and check the entire array that 67 is present or not
#  again take the second element and do the same
#
# we will take 2 pointers:
#                           first pointer points to the first element in the array i.e. 67
#                           the second pointer points to the second elemnt in the array i.e 58
#                           The combinations are:
#                                                   67  58
#                                                   67  54
#                                                   67  90
#                                                   67  69
#                                                   67  58
# 
#
# if there is no match then:
#                             the first pointer should be incremented by 1. that meams the  first pointer now points to 58
#                              the second pointer points at 54 
#                              The combinations are:
#                                                     58  54
#                                                     58  90
#                                                     58  69
#                                                     58  58
#So the complexity of this approach is O(n^2) beacuse we have to create a pair with each elemnts with each other
#
#
#Optimisation of QUestion4:
---------------------------
                              we can think of sorting this array:
                              after sorting our array becomes: Array = 54  58  58  67  69  90

#  since sorting also takes time. so the beast sorting techniques have a time  complexity of O(nlogn) which is significantly less than O(n^2)
#  these best sorting techniques are:  1.Quicksort   2.merge sort. 
#  Both the above sorting techniques have the time complexity of O(nlogn)

Now we will have to scan the sorted Array only once and we wil able to get the answer by comparing the adjacents elements
like 54 58
     58 58
     58 67
     67 69
     69 90
to scan the array once the time compplexity O(n)

# so to arrive at solution we have done two steps:       
                                                   1.sorting + 2.scanning the array once
                                                     nlogn + n
                                                     n(logn+1)  = nlogn
                                                     O(nlogn) + O(n) ~ O(nlogn)

#
# Qusetions5: There is an array on 1000 elemnts and some elemnts repeat. Now we need to find the elemnt which repeats maximum number of times
ANswer5: Array = 23  42  57  12  11  69  32  ......   42  49  .....

Brute Force Approach:
---------------------
                      we have to take one elemnt and scan the entire array and compare it with each element. agai n take the second elemnt and scan the entire elemnts and so on
                      similar to the previous question. so the time complexity is O(n^2)
                     

Optimization:
-------------
             we can think of sorting the Array. After sorting my array is
            11   12   23   32  42  42  42  49  49  57
for the sorting time complexity willl  be O(nlogn). After sorting all the repeating elements of same elemnt is at same place consecutively.
 in a single scan of this array, we will compare and count the number of elemnts and we will able to tell which elemnt has repeated how many times.
so for the scan time-complexity is O(n)
  sorting + finding the answer
   O(nlogn)+O(n) ~ O(nlogn)

#----------------------------------------------------------------------------------------------

#
#
#
#
#
#
#
#
#
#
#
#
#

