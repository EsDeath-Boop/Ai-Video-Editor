def select_segments(transcript, audio, cfg):
    segments = []

    for seg in transcript["transcription"]:
        start_ms = seg["offsets"]["from"]
        end_ms   = seg["offsets"]["to"]

        start = start_ms / 1000.0
        end   = end_ms / 1000.0

        # Guard against zero / invalid segments
        if end - start < cfg.get("min_segment_duration", 1.5):
            continue

        segments.append((start, end))

    return segments
