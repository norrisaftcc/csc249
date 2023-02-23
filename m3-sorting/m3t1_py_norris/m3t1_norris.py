"""
python version of M3T1 - selection sort
todo:
    - add debug statements
    - toggle them off a global constant
    - update repository
"""
DEBUG = True # only print debug if True (type is bool)
COMPARES = 0
SWAPS = 0 

def selection_sort(numbers):
   for i in range(len(numbers)-1):
   
      
      # Find index of smallest remaining element
      index_smallest = i
      for j in range(i+1, len(numbers)):
         # this if statement is a compare
         COMPARES++
         if numbers[j] < numbers[index_smallest]:
            index_smallest = j
            if DEBUG:
                print("\tsmallest:", numbers[index_smallest],"@",index_smallest)
      
      # Swap numbers[i] and numbers[index_smallest]
      # obviously, this is a swap
      SWAPS++
      temp = numbers[i]
      numbers[i] = numbers[index_smallest]
      numbers[index_smallest] = temp
      if DEBUG:
          print("\t\tswap", i, "and", index_smallest)
          print("PART_SORTED", numbers)
          print("compares=", COMPARES, " swaps=", SWAPS)


def main():
  # Main program to test the selection sort algorithm
  numbers = [10, 2, 78, 4, 45, 32, 7, 11]
  
  # Display the contents of the list
  print('UNSORTED:', numbers)
  
  # Call the selection_sort() function
  selection_sort(numbers)
  
  # Display the (sorted) contents of the list
  print('SORTED:', numbers)
  
  #print('Total comparisons:', comparisons)
  print("compares=", COMPARES, " swaps=", SWAPS)

# start program
if __name__ == "__main__":
  main()