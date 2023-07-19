#Nama : Imanuel Lucky Wijaya
#NPM  : 011190065
#Kelompok : Operasi Pengembangan (ThresHolding)
import cv2 as cv

#Membaca citra dari komputer
gambar_lufy=cv.imread('lufy.jpg')

#Menampilkan citra RGB dari Komputer
cv.imshow('Gambar lufy RGB',gambar_lufy)

#Mengkonversi citra RGB ke Grayscale
gray_image = cv.cvtColor(gambar_lufy,cv.COLOR_RGB2GRAY)

#Menampilkan citra Grayscale
cv.imshow('Gambar Images Grayscale',gray_image)

#Mengonverensi citra Grayscale ke Binary
_,Binary_image = cv.threshold(gray_image,127, 255, cv.THRESH_BINARY)

#Menampilkan citra Binaryz
cv.imshow('Gambar lufy Binary', Binary_image)

#Menunggu user menekan tombol
cv.waitKey(0)

#Menghapus semua jendela yang dibuka
cv.destroyAllWindows()