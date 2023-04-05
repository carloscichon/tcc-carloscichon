import cv2
from os import listdir
path = "/home/carlos/UFPR/tcc/tcc-carloscichon/data_emotionet/"

for file in listdir(path):
    print("lendo " + path+file)
    img = cv2.imread(path+file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dim = (48,48)
    result = cv2.resize(gray_img, dim)
    newfile = path + "/gray/" + file
    print(newfile)
    cv2.imwrite(newfile, result)
