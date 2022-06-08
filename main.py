import numpy as np
import cv2 as cv

if __name__ == "__main__":
    vid = cv.VideoCapture("0.hevc")

    lk_params = dict(
        winSize=(15,15),
        maxLevel=2,
        criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)
    )

    prev_frame = None

    while True:
        status, cur_frame = vid.read()
        if status == False:
            break

        if prev_frame == None:
            prev_frame = gray
            continue

        gray = cv.cvtColor(cur_frame, cv.COLOR_RGB2GRAY)

        kp1, st, err = cv.calcOpticalFlowPyrLK(prev_frame, cur_frame, )

        cv.imshow("frame", cur_frame)

        prev_frame = gray

        key = cv.waitKey()

        if key == 113:
            quit()
