import cv2
import time
from tkinter import messagebox

def capture(ID):
    # set the coundown timer to 5 seconds.
    counter = int(5)
    # open the camera.
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    img_counter = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Capture Image", frame)

        countdown = time.time()

        while counter >= 0:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # display text above the rectangle.
            txt = "Look at the camera"

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(frame,(200, 50),(450, 350),(0,255,0),2)
            cv2.putText(frame, str(counter),(250, 250), font,6, (255,0,0),8, cv2.LINE_AA)
            cv2.putText(frame, str(txt),(150, 30), font,1, (255,0,0),2, cv2.LINE_AA)
            cv2.imshow('Capture Image', frame)
            cv2.waitKey(2)

            # current time.
            current_time = time.time()

            # update the countdown.
            if (current_time - countdown >= 1):
                countdown = current_time
                counter = counter - 1
        else:
            ret, frame = cap.read()
            cv2.imshow('Capture Image', frame)
            cv2.moveWindow('Capture Image',400,200)
            cv2.waitKey(2000)
            # saves users name as a image 
            img_name = "C:/Users/kopry/Applied-Project-and-Minor-Dissertation/Application/images/" + ID.get() + ".jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            messagebox.showinfo("Info", "You have been successfully registered!")
            img_counter += 1
            # close the camera
            cap.release()
            # close all the opened windows
            cv2.destroyAllWindows()

        # close the camera
        cap.release()
        # close all the opened windows
        cv2.destroyAllWindows()