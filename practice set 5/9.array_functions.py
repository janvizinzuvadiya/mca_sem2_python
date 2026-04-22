# 9. Create a numeric array and do the following: append the element, pop the element,
#  insert an element at the desired position, reverse the elements in the array, 
#  convert the array to list.

import array as arr

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Array Functions")
    array = arr.array('i', [3,43,54,23,3,54])
    print("Original Array: ", array)

    # Append the element
    array.append(10)
    print("Array after appending an element: ", array)

    # Pop the element
    array.pop()
    print("Array after popping an element: ", array)

    # Insert an element at the desired position
    array.insert(2, 20)
    print("Array after inserting an element at the desired position: ", array)

    # Reverse the elements in the array
    array.reverse()
    print("Array after reversing the elements: ", array)

    # Convert the array to list
    array = array.tolist()
    print("Array after converting to list: ", array)

    print("=" * 50)
    print("\n")
    print("\nThank you for using the program! 👋\n")


if __name__ == "__main__":
    main()    
