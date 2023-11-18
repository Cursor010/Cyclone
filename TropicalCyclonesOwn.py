import cv2
import numpy as np

# Load the image
def makeContors(image):

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a binary image
    _, binary = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)

    _, binary2= cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Find the contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, _ = cv2.findContours(binary2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

    filtered_contours2 = [cnt for cnt in contours2 if cv2.contourArea(cnt) > 100]


    # Create a blank canvas for drawing the outlines
    canvas = image.copy()

    # Find the contour with the largest area
    largest_contour = max(filtered_contours, key=cv2.contourArea)

    for contour2 in filtered_contours2:
        # If it's not the largest contour, calculate its area and draw it with a purple outline on the canvas
        if contour2 is not largest_contour:
            area = cv2.contourArea(contour2)
            color = (0, 0, 0)  # Purple color
            cv2.drawContours(canvas, [contour2], -1, color, 2)
            moments = cv2.moments(contour2)

            # Calculate the moments of the contour
    moments = cv2.moments(largest_contour)

        # Calculate the centroid of the contour
    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
        # Calculate the centroid of the contour
        cv2.circle(canvas, (cx, cy), 13, (255, 102, 255), 2)#center circles


    # Display the original image with the outlined textures

    #result = cv2.drawContours(image.copy(), filtered_contours, -1, (255, 102, 0), 2)
    result = cv2.drawContours(canvas, largest_contour, -1, (0, 255, 0), 3)
    return result


for i in range(1,7):
        image = cv2.imread('cyclone' + str(i) + '.jpg')
        cv2.imshow('Outlined Textures' + str(i), makeContors(image))
#image = cv2.imread('cyclone1.jpg')
#cv2.imshow('Outlined Textures', makeContors(image))
cv2.waitKey(0)
cv2.destroyAllWindows()




