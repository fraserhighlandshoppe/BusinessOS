#!/usr/bin/env python3
"""Transcribe audio files using faster-whisper, output .md and optional .srt to guru directories"""
import argparse
import sys
from pathlib import Path
from faster_whisper import WhisperModel
from datetime import datetime

# Guru mapping - match from filename
GURU_MAP = {
    'digitalmarketer': 'DigitalMarketer',
    'david.stackexchange': 'David StackExchange',
    'dm': 'DigitalMarketer',
    'ali_brown': 'Ali Brown',
    'abrown': 'Ali Brown',
    'grant_cardone': 'Grant Cardone',
    'grand_cardone': 'Grant Cardone',
    'researchfreak': 'ResearchFreak',
    'fourways': 'ResearchFreak',
    'corner_your_market': 'ResearchFreak',
    'troy_white': 'Troy White',
    'drayton_bird': 'Troy White',
    'lisamanyon': 'Lisa Mannon',
    'bob_proctor': 'Bob Proctor',
    'jeanette_weinstein': 'Jeanette Weinstein',
    'cmorgan': 'Christian Mickelsen',
    'unknown': 'Unknown'
}

def get_guru_from_filename(filename: str) -> str:
    """Extract guru from filename using keyword matching"""
    name_lower = filename.lower()
    for keyword, guru in GURU_MAP.items():
        if keyword in name_lower or guru.lower() in name_lower:
            return guru
    return 'Unknown'

def transcribe_audio(file_path: str, model_size: str = "tiny.en"):
    """Transcribe audio file and return segments"""
    model = WhisperModel(model_size, device="cpu", compute_type="float32")
    segments, _ = model.transcribe(file_path)
    return segments

def write_markdown(segments, out_path):
    with open(out_path, 'w') as f:
        for s in segments:
            f.write(f"{s.start:.1f}-{s.end:.1f}: {s.text}\n")

def write_srt(segments, out_path):
    """Write Whisper segments to SRT format"""
    def format_time(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds * 1000) % 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    with open(out_path, 'w') as f:
        for i, s in enumerate(segments, start=1):
            f.write(f"{i}\n")
            f.write(f"{format_time(s.start)} --> {format_time(s.end)}\n")
            f.write(f"{s.text.strip()}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio using faster-whisper")
    parser.add_argument("files", nargs="+", help="Audio files to transcribe")
    parser.add_argument("--model", default="tiny.en", help="Model size to use")
    parser.add_argument("--srt", action="store_true", help="Also generate .srt subtitle file")
    args = parser.parse_args()
    
    for f in args.files:
        path = Path(f)
        if path.exists():
            # Determine output directory based on guru
            guru = get_guru_from_filename(path.name)
            output_dir = Path(f"/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions/{guru}")
            output_dir.mkdir(parents=True, exist_ok=True)
            
            segments = transcribe_audio(str(path), args.model)
            # Write .md
            md_path = output_dir / f"{path.stem}.md"
            write_markdown(segments, md_path)
            print(f"--- {path.name} ---")
            print(f"Saved transcript to {md_path}")
            # Write .srt if requested
            if args.srt:
                srt_path = output_dir / f"{path.stem}.srt"
                write_srt(segments, srt_path)
                print(f"Saved subtitles to {srt_path}")
        else:
            print(f"File not found: {f}", file=sys.stderr)