import subprocess
import os

def remove_silences(video_path, audio_path, start, end, cfg):
    duration = max(0.05, end - start)  
    out = f"seg_{int(start * 1000)}.mp4"

    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-ss", f"{start:.3f}",
        "-t", f"{duration:.3f}",
        "-map", "0:v:0",
        "-map", "0:a:0",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-movflags", "+faststart",
        "-reset_timestamps", "1",
        "-avoid_negative_ts", "make_zero",
        out
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(out) or os.path.getsize(out) < 5_000:
        raise RuntimeError(f"FFmpeg produced empty clip: {out}")

    return out
