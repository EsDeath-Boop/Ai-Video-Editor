import cv2
import numpy as np

LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

def stabilize_gaze(video_path, landmarks, cfg):
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(
        "gaze_fixed.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        cap.get(cv2.CAP_PROP_FPS),
        (int(cap.get(3)), int(cap.get(4)))
    )

    frame_idx = 0
    max_px = cfg["gaze"]["max_px"]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        lm = landmarks[frame_idx]
        frame_idx += 1

        if not lm:
            out.write(frame)
            continue

        h, w, _ = frame.shape
        face = lm[0]

        left_eye = np.mean(
            [(face.landmark[i].x * w, face.landmark[i].y * h) for i in LEFT_IRIS],
            axis=0
        )
        right_eye = np.mean(
            [(face.landmark[i].x * w, face.landmark[i].y * h) for i in RIGHT_IRIS],
            axis=0
        )

        eye_center = (left_eye + right_eye) / 2
        nose = np.array([
            face.landmark[1].x * w,
            face.landmark[1].y * h
        ])

        offset = nose - eye_center
        offset = np.clip(offset, -max_px, max_px)

        M = np.float32([[1, 0, offset[0]], [0, 1, offset[1]]])
        corrected = cv2.warpAffine(frame, M, (w, h))

        out.write(corrected)

    cap.release()
    out.release()
    return "gaze_fixed.mp4"
