def compose_video(clips):
    concat_file = "concat.txt"
    with open(concat_file, "w") as f:
        for clip in clips:
            f.write(f"file '{clip}'\n")

    return concat_file
