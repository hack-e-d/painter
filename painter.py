import cv2


def pencilsketch():
	img = cv2.imread('img2.jpg')
	print("Painting the image....")
	dst_gray, res = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
	cv2. imshow("pencilsketch image", res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite("pencilsketch.jpg", res )

def watercolor():
	img = cv2.imread("img2.jpg")
	print("Painting the image....")
	res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
	cv2. imshow("watercolor image", res)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imwrite("watercolor.jpg", res )

watercolor()
