import cv2


def main():
    cap = cv2.VideoCapture("video/example.mp4")
    cv2.namedWindow("item detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("item detection", 800, 600)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            cv2.imshow("item detection", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
