# 8. Create a numeric array and perform following operations on it: 
# Add 2 to each elements, 
# subtract 3 from each element, 
# multiply each element with 3, 
# Divide each element by 2, 
# Find max and min, 
# find the average of all elements.

import array as arr

def print_header(title):
    print("=" * 50)
    print(f"{   title:^50}")
    print("=" * 50)

def main():
    print_header("Array Math Operations")
    array =arr.array('i', [3,43,54,23,3,54])
    print("Original Array: ", array)

    # Add 2 to each element
    array = [x + 2 for x in array]
    print("Array after adding 2 to each element: ", array)

    # Subtract 3 from each element
    array = [x - 3 for x in array]
    print("Array after subtracting 3 from each element: ", array)

    # Multiply each element by 3
    array = [x * 3 for x in array]
    print("Array after multiplying each element by 3: ", array)

    # Divide each element by 2
    array = [x / 2 for x in array]
    print("Array after dividing each element by 2: ", array)

    # Find max and min
    print("Maximum element in the array: ",max(array))
    print("Minimum element in the array: ",min(array))

    # Find the average of all elements
    print("Average of all elements in the array: ", sum(array)/len(array))

    print("=" * 50)
    print("\nThank you for using the program! 👋\n")


if __name__ == "__main__":
    main()    

