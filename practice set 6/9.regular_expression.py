# 9. Create a regular expression that:
# a). Identifies and display the string starting with 's' and having 4 characters.
# b). Splits the string where some special characters are found.
# c). Display the word starting with number.
# d). Display the word having 3 or 4 or 5 characters.
# e). Display only the dates from the string.
# f). Create a string with name of the person and his Aadhar number, display only Aadhar
# number.
# g). Display all the words that starts with 'at' or 'ap'.
# h). Check if the string starts with 'at' than display appropriate message and otherwise.
import  re

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Regular Expression")
    
    try:
        text = "sam went to atul on 12-05-2023, his aadhar is 1234-5678-9123 and apple costs 50"

        # a) string starting with 's' and having 4 characters
        print("a)")
        result = re.findall(r'\bs\w{3}\b', text)
        print(result)

        # b) split string where special characters are found
        print("\nb)")
        split_result = re.split(r'[^\w\s]', text)
        print(split_result)

        # c) word starting with number
        print("\nc)")
        result = re.findall(r'\b\d\w*\b', text)
        print(result)

        # d) word having 3 or 4 or 5 characters
        print("\nd)")
        result = re.findall(r'\b\w{3,5}\b', text)
        print(result)

        # e) display only dates
        print("\ne)")
        result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
        print(result)

        # f) extract Aadhar number
        print("\nf)")
        aadhar_text = "Name: Ramesh Aadhar: 1234-5678-9123"
        result = re.findall(r'\d{4}-\d{4}-\d{4}', aadhar_text)
        print(result)

        # g) words starting with 'at' or 'ap'
        print("\ng)")
        result = re.findall(r'\b(a[tp]\w*)\b', text)
        print(result)

        # h) check if string starts with 'at'
        print("\nh)")
        if re.match(r'^at', text):
            print("String starts with 'at'")
        else:
            print("String does not start with 'at'")
        


    except Exception as e:
        print(e)






    print('='*50)


if __name__ == "__main__":
    main()