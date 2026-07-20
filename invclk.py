""".  work
import cv2
import numpy as np

# use two images to mask and then use vedio
#live feed + red 
#background
#mag = backround without (livefeed)
#live feed + mag
#mask with red
def cloak(background,live_red):
    live_red_hsv=cv2.cvtColor(live_red,cv2.COLOR_BGR2HSV)
    lb1=np.array([0,60,120])
    ub1=np.array([10,255,255])
    #more than {350,35,50}
    lb2=np.array([170, 60, 120])
    ub2=np.array([180,255,255])
    red1=cv2.inRange(live_red_hsv,lb1,ub1)
    red2=cv2.inRange(live_red_hsv,lb2,ub2)
    red_mask=cv2.bitwise_not(cv2.bitwise_or(red1,red2))
    live_no_red=cv2.bitwise_and(live_red,live_red,mask=red_mask)
    live_no_red_grey=cv2.cvtColor(live_no_red,cv2.COLOR_BGR2GRAY)
    mask_back=cv2.bitwise_not(live_no_red_grey)
 #   _,maske_back_thr=cv2.threshold(mask_back,220,255,cv2.THRESH_BINARY).   (yet to be tried ^^-1)
    maske_back_thr=cv2.adaptiveThreshold(mask_back,255,cv2.ADAPTIVE_THRESH_MEAN_C,blockSize=11,c=2)
    back_red=cv2.bitwise_and(background,background,mask=maske_back_thr)
    final=cv2.bitwise_or(back_red,live_no_red)
    return (final)
"""

"""
ved=cv2.VideoCapture(0)
save=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter("feed.mp4",save,30,(1920,1080))
out2=cv2.VideoWriter("output.mp4",save,30,(1920,1080))
while True:
    r, frame = ved.read()
    if not r:
        break
    #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cv2.imshow("ved",frame)

    if cv2.waitKey(1) & 0xFF == ord("c"):
        bck_img=frame
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


while True:
    r, frame = ved.read()
    if not r:
        break
    
    frame2=cloak(bck_img,frame)
    #out.write(frame)
    #out2.write(frame2)
    cv2.imshow("feed",frame)
    cv2.imshow("ved_magic",frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
ved.release()
"""
""".  work
img=cv2.imread("/Users/vivekyadav/Desktop/live+red2")




















cv2.imshow("dis",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


import cv2
import numpy as np

def cloak(background,live_red):
    live_red_hsv=cv2.cvtColor(live_red,cv2.COLOR_BGR2HSV)

    lb1=np.array([0,60,120])
    ub1=np.array([10,255,255])
    lb2=np.array([170, 60, 120])
    ub2=np.array([180,255,255])
    red1=cv2.inRange(live_red_hsv,lb1,ub1)
    red2=cv2.inRange(live_red_hsv,lb2,ub2)

    red_mask_back=(cv2.bitwise_or(red1,red2))
    red_mask_live=cv2.bitwise_not(red_mask_back)
    live_no_red=cv2.bitwise_and(live_red,live_red,mask=red_mask_live)
    back_red_part=cv2.bitwise_and(background,background,mask=red_mask_back)
    final=cv2.bitwise_or(live_no_red,back_red_part)
    return(final)


ved=cv2.VideoCapture(0)
save=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter("output.mp4",save,30,(1920,1080))

while True:
    r, frame = ved.read()
    if not r:
        break
    cv2.imshow("ved",frame)

    if cv2.waitKey(1) & 0xFF == ord("c"):
        bck_img=frame
        break

while True:
    r, frame = ved.read()
    if not r:
        break
    frame2=cloak(bck_img,frame)
    #out.write(frame2)
    cv2.imshow("ved_magic",frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
ved.release()
cv2.waitKey(0)
cv2.destroyAllWindows()


