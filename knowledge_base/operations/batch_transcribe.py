#!/usr/bin/env python3
"""Batch transcription processor for Marketing audio files"""
import subprocess
import json
from pathlib import Path
from datetime import datetime

MARKETING_DIR = Path("/mnt/fhsws002_business/Marketing")
OUTPUT_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions")
OUTPUT_DIR.mkdir(exist_ok=True)

def find_audio_files():
    """Find all audio files in Marketing directory"""
    audio_files = []
    for pattern in ["*.mp3", "*.wav", "*.m4a", "*.flac"]:
        audio_files.extend(MARKETING_DIR.rglob(pattern))
    return sorted(audio_files)

def transcribe_file(audio_path, index):
    """Transcribe a single file using faster-whisper"""
    output_file = OUTPUT_DIR / f"{index:04d}_{audio_path.stem}.txt"
    
    cmd = [
        "python3",
        "/home/fhs_kevin/BusinessOS/knowledge_base/operations/transcribe.py",
        str(audio_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    
    with open(output_file, "w") as f:
        f.write(f"# {audio_path.name}\n\n")
        f.write(f"**Transcribed:** {datetime.now().isoformat()}\n\n")
        f.write(result.stdout)
    
    return {"file": str(audio_path), "output": str(output_file)}

def main():
    audio_files = find_audio_files()
    print(f"Found {len(audio_files)} audio files")
    
    results = []
    for i, audio_file in enumerate(audio_files):
        print(f"Processing {i+1}/{len(audio_files)}: {audio_file.name}")
        try:
            result = transcribe_file(audio_file, i)
            results.append({"status": "success", **result})
            print(f"  ✓ Completed: {result['output']}")
        except Exception as e:
            results.append({"status": "error", "file": str(audio_file), "error": str(e)})
            print(f"  ✗ Error: {e}")
    
    with open(OUTPUT_DIR / "transcription_index.json", "w") as f:
        json.dump({"created": datetime.now().isoformat(), "files": results}, f, indent=2)
    
    print(f"\nTranscription complete. Results in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()