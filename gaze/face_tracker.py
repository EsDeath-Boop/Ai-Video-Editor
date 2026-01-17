import mediapipe as mp
import cv2

def track_faces(video):
    mp_face = mp.solutions.face_mesh.FaceMesh(static_image_mode=False)
    cap = cv2.VideoCapture(video)
    landmarks = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        res = mp_face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        landmarks.append(res.multi_face_landmarks)
    return landmarks
