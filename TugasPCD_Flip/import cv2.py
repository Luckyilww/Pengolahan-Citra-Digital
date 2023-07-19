import cv2

load = cv2.imread('lucky.jpg')
flip = cv2.flip(load, 0)
flip1 = cv2.flip(load, 2)
flip2 = cv2.flip(load, -1)

cv2.imshow('Putar Gambar 0',flip)
cv2.imshow('Putar Gambar 1',flip1)
cv2.imshow('Putar Gambar -1',flip2)

cv2.waitKey(0)
cv2.destroyAllWindows()