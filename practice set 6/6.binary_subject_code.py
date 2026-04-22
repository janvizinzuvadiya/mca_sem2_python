# 6. Create and open the binary file with 'with' option. Store names of all the subjects you study in semester 2.
#  Ask user to enter the subject number they wanted to see and display that subject name.

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Get Subject List frmo Binary File")
    try:
        subjects = ['Python', 'Data Structures', 'Algorithms', 'Operating Systems', 'Database Management Systems']
        print("Subjects : ", subjects)
        subjects = [subject.encode() for subject in subjects]
        
        print('-' * 50)

        print("Enter the subject number you want to see (1-5) : ")
        subject_number = int(input())

        with open('subjects.bin','wb') as f:
            for subject in subjects:
                f.write(subject + b'\n')
        
        with open('subjects.bin','rb') as f:
            all_subjects = f.readlines()
            
            if 1 <= subject_number <= len(all_subjects):
                target = all_subjects[subject_number - 1].decode().strip()
                print(f"Subject number {subject_number} is: {target}")
            else:
                print("Invalid subject number!")   

    except Exception as e:
        print(e)
        print('=' * 50)


if __name__ == "__main__":
    main()