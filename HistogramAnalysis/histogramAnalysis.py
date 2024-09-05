import cv2
import numpy as np

from matplotlib import pyplot as plt

'''
@author: tahacolak
This script creates a basic image with two white rectangles on a black background,
reads an external image file, and then calculates and displays the color histograms
of the blue, green, and red channels of the image using OpenCV and matplotlib.
'''

img=np.zeros((500,500),np.uint8)+1
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)

volcanoImage=cv2.imread("BURAYA RESMİN BULUNDUĞU KISAYOL ADRESİNİ GİRİNİZ(ENTER THE PATH THAT CONTAINS IMAGE FILE ADDRESS)")

'''
[TR]
Kısayol adresi girerken copy&paste yaptığınızda \ şeklinde dizinler ayrılır. 
Bu durumda sorun yaşayabilirsiniz, o yüzden \\ şeklinde dizin ayraçlarını düzeltiniz.

[EN]
Duration of entering shortcut adress, when click copy&paste , path parts are seperated by \
In this case, you'd get an error, so; you should arrange path parts as \\
'''

b,g,r=cv2.split(volcanoImage)

#check histogram densities from the plot-table.

cv2.imshow("Volcano Image: ",volcanoImage)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()








cv2.waitKey(0)
cv2.destroyAllWindows()