# View image video matrix

In order to display photos and videos as a matrix


<pre><code>pip install -r requirements.txt
</code></pre>


## Example for Image


<pre><code>
smp = ShowMatrixPic(width=180, height=240, row=3, column=4, atuoTile=True)
  

imgListOne = ['pic/Scott Glenn.jpg','pic/Brad Pitt.jpg',
              'pic/Scott Glenn.jpg','pic/Brad Pitt.jpg',
              'pic/Scott Glenn.jpg','pic/Brad Pitt.jpg',
              'pic/Scott Glenn.jpg','pic/Brad Pitt.jpg',
              'pic/Scott Glenn.jpg','pic/Brad Pitt.jpg'
              ]
numpy_horizontal = smp.showPic(imgListOne)
cv2.imshow('img', numpy_horizontal)
cv2.waitKey(0)
</code></pre>
![Alt text](/img/1.png)


## Example for Video
smp = ShowMatrixPic(width=320, height=240, row=3, column=4, atuoTile=True)

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)
cap3 = cv2.VideoCapture(0)
cap4 = cv2.VideoCapture(0)
while True:
	_, frame0 = cap0.read()
        _, frame1 = cap1.read()
        _, frame2 = cap2.read()
        _, frame3 = cap3.read()
        _, frame4 = cap4.read()

        imgListOne = [frame0, frame1, frame2, frame3, frame4]
   
        numpy_horizontal = smp.showVideo(imgListOne)
        cv2.imshow('img', numpy_horizontal)
        cv2.waitKey(1)
![Alt text](/img/2.gif)
