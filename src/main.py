import cv2
from face_detect import detect_face

def main():
    img = cv2.imread("test.jpg")
    face = detect_face(img)
    
    if face is not None:
        print("Face detected!")
    else:
        print("No face detected.")

if __name__ == "__main__":
    main()