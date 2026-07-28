#!/usr/bin/env python3
"""Direct transcription test - no subprocess needed"""
from faster_whisper import WhisperModel
import argparse
import sys

def transcribe_file(file_path, model_size="tiny.en"):
    print(f"Loading model {model_size}...")
    model = WhisperModel(model_size, device="cpu", compute_type="float32")
    
    print(f"Transcribing {file_path}...")
    segments, _ = model.transcribe(file_path)
    
    print("Results:")
    result_text = ""
    for segment in segments:
        print(f"{segment.start:.2f}s-{segment.end:.2f}s: {segment.text}")
        result_text += f"{segment.start:.2f}-{segment.end:.2f}: {segment.text}\n"
    
    return result_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--model", default="tiny.en")
    args = parser.parse_args()
    
    try:
        text = transcribe_file(args.file, args.model)
        print("\n--- OUTPUT START ---")
        print(text)
        print("--- OUTPUT END ---")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)