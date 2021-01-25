#Code Walkthrough:
#In order to sort a list of numbers, I compared the value of each index within the list with the rest of indices in the list by using a for loop and a nested for loop.
#The purpose of the for loop is to select each index in the list and the purpose of the nested for loop is to compare the current value of the index selected by the for loop with the
#rest of the indices in the list. If the current value of the index is greater than the proceeding index values then it'll switch places. 
#And if the switched index value is greater than one of its proceeding index values, then the switch will occur again. This comparison courtesy of the if statement will occur until the list ends.
#Once the first index has been compared with, the for loop moves on the next index and performs the same comparison operation until the list ends.
#To ensure that the comparison of indexes within the scope of the nested for loop does not restart from the beginning of the list but
#rather at the same index as the current position of the selected index, I created a counter variable to keep track of where the comparison of values within the nested for loop should start to avoid
#messing up the partially sorted list.

#Test Cases:
lst_1=[9,5,1,4,2]
lst_2=[-1,5,1,4,2,33,2,5]
lst_3=[10,9,8,7,6,5,4,3,2,1,0]
lst_4=[0,1,2,3,4,5,6,7,8,9,10]


def sortfunc(num_lst):
    #Declaration of variables to help me while debugging:
    curr_val=0
    next_val=0
    counter=0
    #For loop to select each individual index to be compared with the rest of the indices in the nested for loop.
    for i in range(len(num_lst)):
        #For loop to keep track of where to what index the comparison of values to start in order to prevent the sorted part of the list from getting messed up
        counter+=1
        #Nested for loop to compare the selected index from the for loop with the rest of the values in the list. 
        for j in range(len(num_lst)-counter): #-Counter to ensure that the last value is being compared with
            #Comparing whether the selected index is greater than each proceeding index to determine
            if num_lst[i]>num_lst[j+counter]:
                #Assign value to variables for debugging--> Makes it easier to keep track of values while debugging.
                #Also to store value for switch later in the function.
                next_val=num_lst[j+counter]
                curr_val=num_lst[i]
                #If current index value is greater then:
                #Perform a switch by assigning the currrent index to the index value being compared with
                num_lst[j+counter]=curr_val
                #Do the same by assigning the next_val being the index being compared with to the current index.
                num_lst[i]=next_val
                #Reset values just to be safe and ensure that nothing gets carried over to the next iteration.
                curr_val=0
                next_val=0
    #Output new list
    return num_lst

print(sortfunc(lst_4))

