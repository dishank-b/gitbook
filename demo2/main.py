import numpy as np
import cv2
import glob

def onMouseClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global no_pnts
        param[no_pnts/4].append([x,y])
        no_pnts+=1
        print "Point Selected"   
        if no_pnts==4:
            print "Select Four points from left frame, starting from the top left and going clockwise"
        if no_pnts==8:
            print "Select Four points from right frame, starting from the top left and going clockwise"
        if no_pnts==12:
            print "Press Esc. All points Recorded."
        
def findHomography(frames):
    # # middle_frame = img[min(frames[0][0][1],frames[0][1][1]):max(frames[0][2][1],frames[0][3][1]) ,min(frames[0][0][0],frames[0][1][0]):max(frames[0][2][0],frames[0][3][0])]
    p0= frames[0]
    p1 = frames[1]
    p2 = frames[2]

    A = np.zeros((8,9))
    # Homography matrix
    for i in range(4): # Using the corners
        A[i*2,:] = [ p1[i][0], p1[i][1], 1, 0, 0, 0, -p0[i][0]*p1[i][0], -p0[i][0]*p1[i][1], -p0[i][0] ]
        A[i*2+1,:] = [0, 0, 0, p1[i][0], p1[i][1], 1, -p0[i][1]*p1[i][0], -p0[i][1]*p1[i][1], -p0[i][1] ]

    [U,S,V]=np.linalg.svd(A)
    m = V[-1,:]
    H1 = np.reshape(m,(3,3))
    print("This value should be close to zero: "+str(np.sum(np.dot(A,m))))

    A = np.zeros((8,9))
    # Homography matrix
    for i in range(4): # Using the corners
        A[i*2,:] = [ p2[i][0], p2[i][1], 1, 0, 0, 0, -p0[i][0]*p2[i][0], -p0[i][0]*p2[i][1], -p0[i][0] ]
        A[i*2+1,:] = [0, 0, 0, p2[i][0], p2[i][1], 1, -p0[i][1]*p2[i][0], -p0[i][1]*p2[i][1], -p0[i][1] ]

    H_left, status = cv2.findHomography(p1, p0)
    H_right, status = cv2.findHomography(p2, p0)

    H1 = H_left
    H2 = H_right

    [U,S,V]=np.linalg.svd(A)
    m = V[-1,:]
    # H2 = np.reshape(m,(3,3))

    print "Homography Matrix between Left and middle frame", H1
    print "Homography Matrix between Right and middle frame", H2


    return H_left, H_right


def applyHomo(img, H, frames):

    p0= frames[0]
    p1 = frames[1]
    p2 = frames[2]

    img1 = np.zeros(img.shape)
    img2 = np.zeros(img.shape)

    for i in range(min(p1[0][1],p1[1][1]),max(p1[2][1],p1[3][1])):
        for j in range(min(p1[0][0],p1[1][0]), max(p1[2][0],p1[3][0])):
            out = np.matmul(H[0],[j, i, 1])
            # img1[int(out[1]/out[2]), int(out[0]/out[2])] = img[i,j]
    
    for i in range(min(p2[0][1],p2[1][1]),max(p2[2][1],p2[3][1])):
        for j in range(min(p2[0][0],p2[1][0]), max(p2[2][0],p2[3][0])):
            out = np.matmul(H[1],[j, i, 1])
            # img2[int(out[1]/out[2]), int(out[0]/out[2])] = img[i,j]
    img2 = img.copy()
    warp_left = cv2.warpPerspective(img[min(p1[0][1],p1[1][1]):max(p1[2][1],p1[3][1]),min(p1[0][0],p1[1][0]):max(p1[2][0],p1[3][0])], H[0],(img.shape[0],img.shape[1]) )
    warp_right = cv2.warpPerspective(img2[min(p2[0][1],p2[1][1]):max(p2[2][1],p2[3][1]),min(p2[0][0],p2[1][0]):max(p2[2][0],p2[3][0])], H[1],(img.shape[0],img.shape[1]) )

    cv2.imshow("Image 2", warp_left)
    cv2.imshow("Image 1", warp_right)
    cv2.waitKey(0)

def main():
    p1 = []
    p2 = []
    p3 = []
    img = cv2.imread("ThreePanel3.jpg")
    temp = np.zeros(img.shape)
    img = cv2.resize(img,(int(0.25*img.shape[1]), int(0.25*img.shape[0])))
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Original",onMouseClick, [p1, p2, p3])
    cv2.imshow("Original", img)
    print "Select Four points from middle frame, starting from the top left and going clockwise"  
    cv2.waitKey(0)
    print "Recorder Points: " ,p1, p2, p3
    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)
    print  "Finding the Homography."
    H_left, H_right = findHomography([p1, p2, p3] )
    applyHomo(img, [H_left, H_right], [p1, p2, p3])




if __name__ == "__main__":
    no_pnts = 0
    main()