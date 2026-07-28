#!/usr/bin/env python3
"""Robust transcription processor with guru classification"""
import subprocess
import json
import re
from pathlib import Path
from datetime import datetime

# Configuration
MARKETING_DIR = Path("/mnt/fhsws002_business/Marketing")
AUDIO_TRANS_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions")
FRAMEWORKS_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/gurus")
OUTPUT_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/knowledge_mappings")

# Guru mapping
GURU_MAP = {
    "david.stackexchange": "DM", "dm": "DM", "david": "DM", "cmorgan": "Christian Mickelsen",
    "ali_brown": "Ali Brown", "abrown": "Ali Brown", "survival": "Ali Brown",
    "grant_cardone": "Grant Cardone", "gcardone": "Grant Cardone", "grand_cardone": "Grant Cardone",
    "researchfreak": "ResearchFreak", "fourways": "ResearchFreak", "corner_your_market": "ResearchFreak",
    "troy_white": "Troy White", "troywhite": "Troy White", "drayton_bird": "Troy White",
    "lisamanyon": "Lisa Mannon", "lisa_mannon": "Lisa Mannon",
    "unknown": "Unknown"
}

# Enhanced error handling
class TranscriptionError(Exception):
    pass

def transcribe_and_organize(audio_path: Path) -> dict:
    try:
        # Classify guru from filename
        guru = "Unknown"
        audio_lower = audio_path.name.lower()
        for pattern, guru_id in GURU_MAP.items():
            if pattern.replace('_', ' ') in audio_lower or guru_id.lower() in audio_lower:
                guru = guru_id
                break
        
        # Create transcript
        cmd = ["python3", "/home/fhs_kevin/BusinessOS/knowledge_base/operations/transcribe.py", str(audio_path)]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        
        # Handle transcription errors
        if not result.stdout:
            raise Exception(f"Transcription failed: {result.stderr}")
        
        # Create guru-specific directory
        output_dir = AUDIO_TRANS_DIR / guru
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate smart filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        index = len(list(AUDIO_TRANS_DIR.glob(f"{guru}/*" + audio_path.stem + ".md")))
        filename = f"{timestamp}_{index:03d}_{audio_path.stem}.md"
        output_file = output_dir / filename
        
        # Create markdown file
        with open(output_file, "w") as f:
            f.write(f"# {audio_path.name}\n\n")
            f.write(f"**Source Path:** {str(audio_path)}\n")
            f.write(f"**Guru:** {guru}\n")
            f.write(f"**Transcribed:** {datetime.now().isoformat()}\n\n")
            f.write(result.stdout)
        
        return {"status": "success", "file": str(output_file)}
    
    except subprocess.TimeoutExpired:
        error_dir = AUDIO_TRANS_DIR / "Timeout"
        error_dir.mkdir(parents=True, exist_ok=True)
        error_file = error_dir / f"{audio_path.stem}_TIMEOUT.md"
        with open(error_file, "w") as f:
            f.write(f"# TRANSCRIPTION TIMED OUT\n**Audio:** {audio_path.name}\n**Error:** The transcription process exceeded the 15-minute timeout limit.")
        return {"status": "timeout", "file": str(error_file)}
    except Exception as e:
        error_dir = AUDIO_TRANS_DIR / "Errors"
        error_dir.mkdir(exist_ok=True)
        error_file = error_dir / f"{audio_path.stem}_CRITICAL.md"
        with open(error_file, "w") as f:
            f.write(f"# CRITICAL ERROR\n**Audio:** {audio_path.name}\n**Error:** {str(e)}\n")
        return {"status": "critical_error", "file": str(error_file)}

# Main processing function
if __name__ == "__main__":
    audio_files = sorted([f for f in MARKETING_DIR.rglob("*") if f.suffix.lower() in ['.mp3', '.wav', '.m4a', '.flac']])
    print(f"Found {len(audio_files)} audio files")
    
    results = []
    upones = []
    fives = []
    for i, audio_file in enumerate(audio_files):
        print(f"Processing file {i+1}/{len(audio_files)}: {audio_file.name}")
        result = transcribe_and_organize(audio_file)
        results.append(result)
        
        if (i+1) % 5 == 1:
            upones.append(result)
        if (i+1) % 5 == 0:
            fives.append(result)
        # Save every 10 files
        if (i+1) % 10 == 0:
            with open(str(AUDIO_TRANS_DIR / "transcription_progress.json"), "w") as f:
                json.dump({"success": fives, "pending": upones}, f)
            upones = []
            fives = []
    
    # Save final summary
    summary = {
        "total": len(results),
        "success": sum(1 for r in results if r["status"] == "success"),
        "timeout": sum(1 for r in results if r["status"] == "timeout"),
        "errors": sum(1 for r in results if r["status"] in ("error", "critical_error")),
        "details": results
    }
    with open(str(AUDIO_TRANS_DIR / "transcription_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print("Transcription complete. Summary saved to transcription_summary.json")