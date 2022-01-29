from glob import glob
from time import sleep

import cv2
import serial


stop_rotation = b'D'
rotate_right = b'R'
rotate_left = b'L'
out_seconds = 1
usb_port: list = glob('/dev/tty.usbserial*')


def main():
    if not usb_port:
        raise FileNotFoundError("Не удалось найти USB-порт. "
                                "Убедитесь, что Arduino подключен через USB")

    ser = serial.Serial(port=usb_port[0], baudrate=9600)
    sleep(1.6)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    shift = 120 if width <= 1280 else 240
    right_shift = (width/2)-shift
    left_shift = (width/2)+shift
    cap.set(3, width)
    cap.set(4, height)

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        for (x, y, w, h) in faces:

            center = int(x+(w/2))
            if center < right_shift:
                print("Вы находитесь правее")
                ser.write(rotate_right)
            elif left_shift <= center <= width:
                print("Вы находитесь левее")
                ser.write(rotate_left)
            else:
                print("Вы находитесь по центру")
                ser.write(stop_rotation)

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        ser.write(stop_rotation)
        cv2.imshow('video', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break

    ser.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
