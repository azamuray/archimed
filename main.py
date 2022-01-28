from glob import glob
from time import sleep

import cv2
import serial


stop_rotation = b'D'
rotate_right = b'R'
rotate_left = b'L'
out_seconds = 1
usb_port: list = glob('/dev/tty.usb*')


def main():
    if not usb_port:
        raise FileNotFoundError("Не удалось найти USB-порт. "
                                "Убедитесь, что Arduino подключен через USB")

    ser = serial.Serial(port=usb_port[0], baudrate=9600)
    sleep(1.6)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cap.set(3, 1920)  # set Width
    cap.set(4, 1080)  # set Height

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
            if center < 520:
                print("Вы находитесь правее")
                ser.write(rotate_right)
            elif 760 <= center <= 1280:
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
