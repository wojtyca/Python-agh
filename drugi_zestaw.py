import glob
import pathlib


def file_counter(dir_path):

    count = 0
    for path in pathlib.Path(dir_path).iterdir():
        if path.is_file():
            count += 1
    print(count)

#file_counter(r'C:\Users\student');


def recursive(main_path):
    files = main_path.glob(r'C:\Users\student\Pictures\*',
                      recursive=True)
    for file in files:
        print(file)



def jpg_creator(i):
    from PIL import Image
    for i in range (i):
        open(r"C:\Users\student\Pictures\file{}.jpg".format(i), "x")
        im1 = Image.open(r'C:\Users\student\Pictures\file{}.jpg".format(i)')
        im1.save(r'C:\Users\student\Pictures\Cat04.png')
        i -= 1







