import subprocess
import json
import os

WHISPER_BIN = r"D:\tools\whisper.cpp\Release\whisper-cli.exe"
WHISPER_MODEL = r"D:\tools\whisper.cpp\Release\models\ggml-small.bin"

def transcribe(audio_path):
    out_prefix = "transcript"

    subprocess.run([
        WHISPER_BIN,
        "-m", WHISPER_MODEL,
        "-f", audio_path,
        "-oj",                 
        "-ojf",               
        "-of", out_prefix,     
        "-np"                  
    ], check=True)

    with open(f"{out_prefix}.json", "r", encoding="utf-8") as f:
        return json.load(f)
