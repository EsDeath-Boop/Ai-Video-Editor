import subprocess

def extract_audio(video, logger):
    out = "audio.wav"
    subprocess.run([
        "ffmpeg", "-y", "-i", video,
        "-ar", "16000", "-ac", "1", out
    ], check=True)
    logger.info("Audio extracted")
    return out
