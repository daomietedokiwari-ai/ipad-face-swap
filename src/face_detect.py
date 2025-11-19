import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection

def detect_faces(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return "Image not found"

    with mp_face.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detector:
        results = face_detector.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if not results.detections:
            return "No face detected"

        return f"Detected {len(results.detections)} face(s)"