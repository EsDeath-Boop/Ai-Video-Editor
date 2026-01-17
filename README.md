InvisibleEditor — AI-Powered Automated Video Editing
Project Overview

InvisibleEditor is an AI-powered video editing pipeline that automatically converts long-form videos into concise, meaningful clips by detecting speech segments and removing silence. The system is intended for content creators, educators, and researchers who need scalable and automated video post-processing.

The project focuses on speech-based segmentation, automated clipping, and video rendering using AI-assisted transcription and multimedia processing tools.

Problem Statement

Manual video editing is time-consuming, repetitive, and does not scale well for long recordings. Editors must manually locate important speech segments, remove silence, and render clips, which leads to inefficiency and inconsistency.

This project aims to automate the video editing process by identifying spoken segments using AI-generated transcripts and generating clean, trimmed video clips without manual intervention.

AI Task

Speech analysis

Audio-based segmentation

Automated video processing

System Design and Architecture
High-Level Workflow

Input video ingestion

Audio extraction using FFmpeg

Speech-to-text transcription

Timestamp-based segment selection

Silence removal and video clipping

Final video rendering

Repository Structure
videoEditor/
│
├── analysis/            Speech-to-text and segment selection logic
├── ingest/              Video and audio loading modules
├── continuity/          Silence removal and trimming logic
├── framing/             Camera smoothing and cropping
├── gaze/                Face and gaze tracking (optional)
├── render/              Video composition and encoding
├── utils/               Logging utilities
│
├── run.py               Main execution script
├── config.yaml          Configuration file
├── transcript.json      Generated transcript
├── input.mp4            Sample input video
└── README.md

Data Understanding and Preparation
Data Source

Input video provided by the user in MP4 format

Audio extracted internally using FFmpeg

Transcript generated using the Whisper speech-to-text model

Preprocessing

Audio resampling to 16 kHz mono

Timestamp-aligned transcription

Segment extraction using millisecond offsets

Model and AI Techniques Used
Core Techniques

Speech-to-text transcription using Whisper

Timestamp-based speech segmentation

Video processing and clipping using FFmpeg

Design Justification

Whisper provides accurate timestamps required for precise segmentation. FFmpeg ensures reliable, high-performance video slicing. A modular architecture improves maintainability and extensibility.

Core Implementation
Key Features

End-to-end automated pipeline

Modular Python-based design

Configuration-driven parameters

Reproducible execution

Running the Project
python run.py


The main script orchestrates audio extraction, transcription, segment selection, clipping, and final encoding.

Evaluation and Results
Evaluation Method

Qualitative evaluation of output clips

Timestamp verification against transcripts

Playback validation for audio-video synchronization

Results

Successful extraction of speech-based segments

Generation of multiple valid video clips

Accurate alignment between audio and video

Limitations

No semantic importance ranking of segments

Silence detection is timestamp-based, not acoustic

Face and gaze correction modules are currently disabled

Ethical Considerations and Responsible AI

No personal data collection

User-provided inputs only

Facial analysis modules disabled by default

Transparent AI usage for transcription

Learnings
Technical Learnings

FFmpeg automation and multimedia pipelines

Speech-to-text integration using Whisper

Modular AI system design

System and Design Learnings

Importance of clear module interfaces

Debugging and validating multimedia workflows

Handling noisy real-world audio data

Future Improvements

Semantic importance and highlight detection

Improved silence detection

Web-based user interface

Batch video processing

Optional activation of face and gaze correction

Tools and Technologies

Python

FFmpeg

Whisper

MediaPipe (optional)

OpenCV (optional)

YAML

AI Usage Disclosure

AI tools were used for speech transcription, debugging assistance, and documentation support. All architectural and implementation decisions were made by the project author.

Conclusion

InvisibleEditor demonstrates how AI-assisted transcription and automated video processing can significantly reduce manual editing effort. The system provides a solid foundation for building scalable, intelligent video editing solutions.
