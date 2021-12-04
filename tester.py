import cv2
import numpy as np

filename = ''

imagepath = 'lena.jfif' #Image to find data into
img = cv2.imread(imagepath)
row ,col, colours = img.shape

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

madeupimg = np.zeros((row,col,3), 'uint8')

# madeupimg = []
# madeupimg.append(b)
# madeupimg.append(g)
# madeupimg.append(r)

madeupimg[:,:,0] = b
madeupimg[:,:,1] = g
madeupimg[:,:,2] = r

cv2.imwrite("b.png",b)
cv2.imwrite("g.png",g)
cv2.imwrite("r.png",r)
cv2.imwrite("madeup.png",madeupimg)


print(img.shape)
