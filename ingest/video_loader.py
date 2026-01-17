import subprocess, json

def load_video(path, logger):
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json",
           "-show_streams", path]
    info = json.loads(subprocess.check_output(cmd))
    stream = info["streams"][0]
    if stream["width"] < stream["height"]:
        raise ValueError("Input must be horizontal")
    logger.info("Video validated")
    return path
