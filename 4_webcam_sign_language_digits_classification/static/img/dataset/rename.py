import shutil
import os

folder_name = "9"
#folder_name = "green_apple"
files = os.listdir("./" + folder_name + "/")

for i in range(0, len(files)):
    print (files[i])
    root, extension = os.path.splitext(files[i])
    if files[i] == ".DS_Store":
        print("This is no image.")
    elif extension == ".png" or ".jpeg" or ".jpg" or ".JPG":
        shutil.move("./" + folder_name + "/" + files[i],"./" + folder_name + "/" + folder_name + "_" + str(i + 1) + ".jpg")

print("Rename Done.")
