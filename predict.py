import cv2


def main():
    cap = cv2.VideoCapture("video/overpass.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
