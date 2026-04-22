# 7. Create a file named 'img1', store an image into it.
#  Open another file named 'img2', copy the same image as in the file 'img1'.
#   Also store both files into the zip file named 'imp_img.
from zipfile import *

def print_header(heading):
    print('=' * 50)
    print(heading)
    print('=' * 50)

def main():
    print_header("Zipping Images after coping them")
    try:
        with open('source.jpg', 'rb') as f:
            bytes = f.read()
        
        with open('destination.jpg', 'wb') as f:
            f.write(bytes)
        
        f=ZipFile('images.zip','w',ZIP_DEFLATED)
        f.write('source.jpg')
        f.write('destination.jpg')
        f.close()

        print("Images copied and zipped successfully!")
        

    except Exception as e:
        print(e)
        print('=' * 50)


if __name__ == "__main__":
    main()