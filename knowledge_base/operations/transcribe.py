#!/usr/bin/env python3
"""Transcribe audio files using faster-whisper"""
import argparse
import sys
from pathlib import Path
from faster_whisper import WhisperModel

def transcribe_audio(file_path: str, model_size: str = "tiny.en") -> str:
    """Transcribe audio file and return text"""
    model = WhisperModel(model_size, device="cpu", compute_type="float32")
    segments, _ = model.transcribe(file_path)
    return "\n".join([f"{s.start:.1f}-{s.end:.1f}: {s.text}" for s in segments])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio using faster-whisper")
    parser.add_argument("files", nargs="+", help="Audio files to transcribe")
    parser.add_argument("--model", default="tiny.en", help="Model size to use")
    args = parser.parse_args()
    
    for f in args.files:
        if Path(f).exists():
            print(f"--- {f} ---")
            print(transcribe_audio(f, args.model))
        else:
            print(f"File not found: {f}", file=sys.stderr)