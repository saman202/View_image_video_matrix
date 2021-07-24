import cv2
import numpy as np
import math
import ctypes




class ShowMatrixPic():
    def __init__(self, row=0, column=0, atuoTile=False, width=200, height=200, text='None'):
        super(ShowMatrixPic, self).__init__()
        self.row = row
        self.column = column
        self.atuoTile = atuoTile
        self.width = width
        self.height = height
        self.text = text
        if self.row < 0:
            self.row = 0
        if self.column < 0:
            self.column = 0


        # user32 = ctypes.windll.user32
        # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # print(screensize)
        #

    def __rawAndColumn(self,imgList):
        r = c = 0
        resSubtraction = 1
        if self.column == 0 and self.row == 0:
            lenList = len(imgList)
            k = round(math.sqrt(lenList))
            if k > 5:
                r = 5
                if lenList % r == 0:
                    c = lenList // k
                else:
                    num2 = lenList // r
                    if num2 > r:
                        c = k + (num2 - r)
                    else:
                        c = k + num2


            else:
                r = k
                if lenList % r == 0:
                    c = lenList // r
                else:
                    u = r ** 2
                    num2 = lenList % r
                    if u < lenList:
                        if num2 < r:
                            c = r + 1
                        else:
                            c = r + num2
                    else:
                        c = r
        elif self.column == 0 and self.row != 0:
            lenList = len(imgList)
            r = self.row
            c = math.ceil(lenList / self.row)
        elif self.column != 0 and self.row == 0:
            lenList = len(imgList)
            c = self.column
            r = math.ceil(lenList / self.column)
        else:
            r = self.row
            c = self.column

        return r, c

    def showVideo(self, imgList):

        r, c = self.__rawAndColumn(imgList)


        image = []
        l = len(imgList)
        print(l)
        for img in imgList:
            # print(img)
            if img is not None:
                img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            else:
                img = np.zeros((self.height, self.width, 3), np.uint8)
                textSize = round(self.width * 0.005, 2)
                textThickness = round(self.width / 100)
                cv2.putText(img, self.text, ((self.width // 4), (self.height // 2)), cv2.FONT_HERSHEY_COMPLEX,
                            textSize, (255, 255, 255), textThickness)

            image.append(img)




        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThickness = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThickness)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)
        else:
            lenOfimg = len(imgList)
            tableNum = r * c

            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    if o > lenOfimg:
                        image.append(image[o % lenOfimg])
                    else:
                        image.append(image[o])


        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal

    def showPic(self, imgList):

        r, c = self.__rawAndColumn(imgList)

        image = []
        l = len(imgList)
        print(l)
        for i in range(l):
            img = cv2.imread(imgList[i])
            img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
            image.append(img)
        if not self.atuoTile:
            lenOfimg = len(imgList)
            tableNum = r * c
            emptyImg = np.zeros((self.height, self.width, 3), np.uint8)
            h, w = emptyImg.shape[:2]
            textSize = round(w * 0.005, 2)
            textThick = round(w / 100)
            cv2.putText(emptyImg, self.text, ((w // 4), (h // 2)), cv2.FONT_HERSHEY_COMPLEX,
                        textSize, (255, 255, 255), textThick)
            if (tableNum - lenOfimg) > 0:

                for o in range(tableNum - lenOfimg):
                    image.append(emptyImg)

        numpy_vertical = []

        for n in range(c):
            numpy_vertical.append(np.vstack((image[n * r:r + (n * r)])))
        numpy_horizontal = np.hstack(numpy_vertical)
        return numpy_horizontal






def main():

    smp = ShowMatrixPic(width=320, height=240, row=3, column=4, atuoTile=True)
    cap0 = cv2.VideoCapture('Video/1.mp4')
    cap1 = cv2.VideoCapture('Video/11.mp4')
    cap2 = cv2.VideoCapture('Video/22.mkv')
    cap3 = cv2.VideoCapture('Video/44.mkv')
    cap4 = cv2.VideoCapture('Video/55.avi')
    while True:

        _, frame0 = cap0.read()
        _, frame1 = cap1.read()
        _, frame2 = cap2.read()
        _, frame3 = cap3.read()
        _, frame4 = cap4.read()

        imgListOne = [frame0, frame1, frame2, frame3, frame4]

        # imgListOne = ['PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png',
        #               'PeopleEntrance/Friday_02_07_2021/20_54_30_(1)_Cam_1.png'
        #               ]
        numpy_horizontal = smp.showVideo(imgListOne)
        cv2.imshow('img', numpy_horizontal)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()


