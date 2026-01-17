import yaml
from ingest.video_loader import load_video
from ingest.audio_extractor import extract_audio
from analysis.speech_to_text import transcribe
from analysis.segment_selector import select_segments
from continuity.remove_silences import remove_silences
from gaze.face_tracker import track_faces
from gaze.gaze_corrector import stabilize_gaze
from framing.vertical_cropper import crop_vertical
from framing.camera_smoother import smooth_camera
from render.compositor import compose_video
from render.encoder import encode_final
from utils.logging import setup_logger

def main():
    logger = setup_logger()

    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)

    video = load_video("input.mp4", logger)
    audio = extract_audio("input.mp4", logger)

    transcript = transcribe(audio)
    segments = select_segments(transcript, audio, cfg)

    clips = []
    for start, end in segments:

        clip = remove_silences(video, audio, start, end, cfg)

        # faces = track_faces(clip)
        # clip = stabilize_gaze(clip, faces, cfg)
        # clip = crop_vertical(clip, faces, cfg)
        clip = smooth_camera(clip, cfg)

        clips.append(clip)


    final = compose_video(clips)
    encode_final(final, "output.mp4")

if __name__ == "__main__":
    main()
