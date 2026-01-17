def crop_vertical(video_path, face_tracks, cfg):
    import cv2
    import numpy as np

    cap = cv2.VideoCapture(video_path)
    W, H = int(cap.get(3)), int(cap.get(4))
    target_w = int(H * 9 / 16)

    out = cv2.VideoWriter(
        "vertical.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        cap.get(cv2.CAP_PROP_FPS),
        (target_w, H)
    )

    alpha = cfg["camera"]["smoothing_alpha"]
    prev_x = W // 2

    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face = face_tracks[idx]
        idx += 1

        if face:
            cx = int(face[0].landmark[1].x * W)
        else:
            cx = prev_x

        cx = int(alpha * cx + (1 - alpha) * prev_x)
        prev_x = cx

        x1 = max(0, min(cx - target_w // 2, W - target_w))
        crop = frame[:, x1:x1 + target_w]

        out.write(crop)

    cap.release()
    out.release()
    return "vertical.mp4"
