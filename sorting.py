# Using sorting as a Problem-Solving Tool
# Book page number: 136

def is_duplicated(items:list=[])-> bool:
    #Return True if there are no duplicate elements in sequence S.
    if not len(items)==0:
       items_tmp=sorted(items)

       for item in range(1, len(items_tmp)):
           if items[item-1] == items[item]:
              return False 
       return True

    else:
        print("List empty!")

print(is_duplicated([0,1,2,3]))

# Explanation:

''' The built-in function, sorted, as described in Section 1.5.2, produces a copy of
the original list with elements in sorted order. It guarantees a worst-case running
time of O(n log n).'''
