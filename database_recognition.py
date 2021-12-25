import cv2
import imutils
import numpy as np
import easyocr
import sys
import mysql.connector

WIDTH = 500
HEIGHT = 500

SCALE_X = 0.5
SCALE_Y = 0.5
# databasede yer alan tehlikeli araç:3,4,16,19,20,30
# databasede yer almayan normal araç:1,5,6,31

def recognition(texter):
    img = cv2.imread(texter)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
    edged = cv2.Canny(bfilter, 30, 200)  # Edge detection
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location =None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    print(location)
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2 + 1, y1:y2 + 1]
    reader = easyocr.Reader(["en"])
    result = reader.readtext(cropped_image)
    print(result)
    if not result:
        sys.exit('plate couldnt be found, list is empty')
    text = result[0][-2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1] + 60), fontFace=font, fontScale=1,
                      color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 2)

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='A976431!z976431',
        port='3306',
        database='python_video'
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM licenceplate where licenceplatetext='" + text + "'")
    plates = mycursor.fetchall()

    imgEmergency = cv2.imread("Resources/emergency.jpg")
    res2 = cv2.resize(img, (WIDTH, HEIGHT), SCALE_X, SCALE_Y, interpolation=cv2.INTER_AREA)
    res3 = cv2.resize(imgEmergency, (WIDTH, HEIGHT), SCALE_X, SCALE_Y, interpolation=cv2.INTER_AREA)
    results = res2, res3

    if not plates:
        print("This car has no criminal record.")
        return results, plates
    else:
        print(plates[0][-1])
        cv2.waitKey(0)
        return results, plates
