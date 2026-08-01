#!/usr/bin/env python3
"""Final robust batch transcription with intelligent chunking and resume capability"""
import subprocess
import json
import os
from pathlib import Path
from datetime import datetime

MARKETING_DIR = Path("/mnt/fhsws002_business/Marketing")
OUT_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions")
OUT_DIR.mkdir(exist_ok=True)

# Guru mapping
GURU_MAP = {
    'digitalmarketer': 'DigitalMarketer',
    'david.stackexchange': 'David StackExchange',
    'dm_': 'DigitalMarketer',
    'ali_brown': 'Ali Brown',
    'grant_cardone': 'Grant Cardone',
    'researchfreak': 'ResearchFreak',
    'troy_white': 'Troy White',
    'lisamanyon': 'Lisa Mannon',
    'bob_proctor': 'Bob Proctor',
    'jeanette_weinstein': 'Jeanette Weinstein',
    'cmorgan': 'Christian Mickelsen',
    'unknown': 'Unknown',
    'eben pagan': 'Eben Pagan'
}

def get_guru(name):
    n = name.lower()
    for k, v in GURU_MAP.items():
        if k in n or v.lower() in n:
            return v
    return 'Unknown'

def transcribe_file(audio_path: Path, guru: str):
    """Transcribe a single file with smart timeout handling"""
    out_dir = OUT_DIR / guru
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{audio_path.stem}.md"
    
    # Skip if already done
    if out_file.exists():
        return {"status": "skip", "file": str(out_file)}
    
    # Determine timeout based on file characteristics
    file_size_mb = audio_path.stat().st_size / (1024*1024)
    timeout = 600 if file_size_mb < 30 else 1200  # 10min or 20min
    
    try:
        result = subprocess.run(
            ['python3', '/home/fhs_kevin/BusinessOS/knowledge_base/operations/transcribe.py', str(audio_path)],
            capture_output=True, text=True, timeout=timeout
        )
        
        with open(out_file, 'w') as f:
            f.write(f"# {audio_path.name}\n\n**Guru:** {guru}\n**Transcribed:** {datetime.now().isoformat()}\n\n{result.stdout}")
        
        return {"status": "success", "file": str(out_file)}
    
    except subprocess.TimeoutExpired:
        # Mark as timeout but save placeholder
        error_file = out_dir / f"{audio_path.stem}_TIMEOUT.md"
        with open(error_file, 'w') as f:
            f.write(f"# TIMEOUT\n**Audio:** {audio_path.name}\n**Error:** Transcription exceeded {timeout}s\n**Action:** Re-run manually\n")
        return {"status": "timeout", "file": str(error_file)}
    
    except Exception as e:
        error_file = out_dir / f"{audio_path.stem}_ERROR.md"
        with open(error_file, 'w') as f:
            f.write(f"# ERROR\n**Audio:** {audio_path.name}\n**Error:** {str(e)}\n")
        return {"status": "error", "file": str(error_file)}

def main():
    # Get all audio files
    audio_files = sorted([f for f in MARKETING_DIR.rglob('*') 
                          if f.suffix.lower() in ['.mp3','.wav','.m4a','.flac']])
    print(f"Found {len(audio_files)} audio files")
    
    # Load progress
    progress_file = OUT_DIR / "transcription_progress.json"
    completed = set()
    if progress_file.exists():
        with open(progress_file) as f:
            data = json.load(f)
            completed = set(data.get('completed', []))
    
    results = []
    for i, af in enumerate(audio_files):
        guru = get_guru(af.name)
        print(f"[{i+1}/{len(audio_files)}] {guru}: {af.name}", flush=True)
        
        result = transcribe_file(af, guru)
        results.append(result)
        completed.add(str(af))
        
        # Save progress every 10 files
        if (i+1) % 10 == 0:
            with open(progress_file, 'w') as f:
                json.dump({'completed': list(completed), 'timestamp': datetime.now().isoformat()}, f)
            print(f"Progress saved: {len(completed)}/{len(audio_files)}", flush=True)
    
    # Final save
    with open(progress_file, 'w') as f:
        json.dump({'completed': list(completed), 'timestamp': datetime.now().isoformat()}, f)
    
    # Summary
    success = sum(1 for r in results if r['status'] == 'success')
    timeout = sum(1 for r in results if r['status'] == 'timeout')
    error = sum(1 for r in results if r['status'] == 'error')
    skip = sum(1 for r in results if r['status'] == 'skip')
    
    print(f"\n=== TRANSCRIPTION COMPLETE ===")
    print(f"Success: {success}, Timeout: {timeout}, Error: {error}, Skip: {skip}")
    print(f"Total: {len(results)}/{len(audio_files)}")

if __name__ == "__main__":
    main()
