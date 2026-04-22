# 8. Create a file with 'with' option, name it 'marks.dat'. 
#     i). Accept subject name and marks from the user, store the data in the file.
#     ii). Give three options to the user:
#         a). To view whole file,  
#         b). Accept and edit the marks of a subject user want to change.
#     iii). Exit

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Marks Handling")
    try:
        with open('marks.dat', 'w') as f:
            print("Enter subject name and marks (enter 'exit' to quit):\n")
            while True:
                subject = input("Subject: ")
                if subject.lower() == 'exit':
                    break
                marks = input("Marks: ")
                f.write(f"{subject}: {marks}\n")
        
        while True:
            print("\nOptions:")
            print("1. View whole file")
            print("2. Edit marks of a subject")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                with open('marks.dat', 'r') as f:
                    print(f.read())
            elif choice == '2':
                with open('marks.dat', 'r') as f:
                    lines = f.readlines()
                subject = input("Enter subject to edit: ")
                for i, line in enumerate(lines):
                    if subject in line:
                        marks = input("Enter new marks: ")
                        lines[i] = f"{subject}: {marks}\n"
                        with open('marks.dat', 'w') as f:
                            f.writelines(lines)
                        break
            elif choice == '3':
                break
        

    except Exception as e:
        print(e)
        print('=' * 50)


if __name__ == "__main__":
    main()