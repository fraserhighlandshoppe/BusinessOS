#!/usr/bin/env python3
"""Smart transcript processor that classifies by guru and uses better naming"""
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
GURU_KEYWORDS_FILE = FRAMEWORKS_DIR / "guru_keywords.json"

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

def extract_subject(content: str) -> str:
    """Extract meaningful subject from transcription text"""
    if not content:
        return "Transcription", "content"
    
    # Simple keyword extraction - take most frequent all-caps or title-case phrases
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if not lines:
        return "General", "content"
    
    # Look for capitalized phrases that might be topics
    candidates = []
    for line in lines[:10]:  # First few lines likely contain key content
        # Match capitalized words or phrases
        caps_phrases = re.findall(r'\b[A-Z][a-zA-Z]+\b(?:\s*[A-Z][a-zA-Z]+)*\b', line)
        candidates.extend(caps_phrases)
    
        # Also look for title case multi-word phrases
        title_phrases = re.findall(r'\b[A-Z][a-z][a-zA-Z]+(?:\s+[A-Z][a-z][a-zA-Z]+)*\b', line)
        candidates.extend(title_phrases)
    
    if not candidates:
        return "General", "content"
    
    # Get frequency of each candidate
    from collections import Counter
    freq = Counter(candidates)
    most_common = freq.most_common(2)
    
    if most_common:
        terms = [term for term, _ in most_common]
        return terms[0] if len(terms) >= 1 else "General", details
    
    return "General", "content"

def get_guru_from_filename(audio_path: Path) -> str:
    """Classify audio by looking at filename patterns"""
    audio_lower = audio_path.name.lower()
    
    for pattern, guru in [
        ("david.stackexchange","DM"), ("dm","DM"), ("david","DM"),
        ("dan_kennedy","Dan Kennedy"), ("dan kennedy","Dan Kennedy"),
        ("grant_cardone","Grant Cardone"), ("grant cardone","Grant Cardone"),
        ("ali_brown","Ali Brown"), ("abrown","Ali Brown"),
        ("researchfreak","ResearchFreak"), ("fourways","ResearchFreak"),
        ("troy_white","Troy White"), ("troywhite","Troy White"), ("drayton_bird","Troy White")
    ]:
        if pattern.replace("_"," ") in audio_lower or guru.lower() in audio_lower:
            return guru
    
    return "Unknown"

def ensure_guru_subdir(audio_path: Path):
    """Create guru-specific subdirectory under transcription output"""
    guru = get_guru_from_filename(audio_path)
    output_subdir = AUDIO_TRANS_DIR / guru
    output_subdir.mkdir(parents=True, exist_ok=True)
    return output_subdir

def create_transcription_entry(audio_path: Path, index: int):
    """Process a single audio file with smart naming"""
    # Get output directory for this guru
    output_dir = ensure_guru_subdir(audio_path)
    
    # Classify and generate filename
    guru = get_guru_from_filename(audio_path)
    subject, detail = extract_subject("")  # Would use actual content later
    
    # Generate timestamp-based filename with subject hints
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    index_suffix = f"{index:03d}"
    
    # Simple pattern: {guru}/{timestamp}_{index}_{subject}_{detail}.md
    smart_filename = f"{guru}/{timestamp}_{index_suffix}_{subject}_{detail}.md"
    output_file = output_dir / smart_filename
    
    # Run transcription
    try:
        result = subprocess.run(
            ["python3", "/home/fhs_kevin/BusinessOS/knowledge_base/operations/transcribe.py", str(audio_path)],
            capture_output=True, text=True, timeout=900
        )
        
        with open(output_file, "w") as f:
            f.write(f"# {audio_path.name}\n\n")
            f.write(f"**Source:** {audio_path.parent.name}/{audio_path.name}\n")
            f.write(f"**Transcribed:** {datetime.now().isoformat()} UTC\n\n")
            f.write(result.stdout)
        
        return {"status": "success", "file": str(output_file)}
    except subprocess.TimeoutExpired:
        error_content = f"# TIMEOUT\n**Audio:** {audio_path.name}\n**Error:** Transcription timed out"
        error_file = output_dir / f"{index:04d}_TIMEOUT.md"
        with open(error_file, "w") as f:
            f.write(error_content)
        return {"status": "timeout", "file": str(error_file)}
    except Exception as e:
        error_content = f"# ERROR\n**Audio:** {audio_path.name}\n**Error:** {str(e)}"
        error_file = output_dir / f"{index:04d}_ERROR.md"
        with open(error_file, "w") as f:
            f.write(error_content)
        return {"status": "error", "file": str(error_file)}

def process_all_audio():
    """Main processing function"""
    # Find all audio files
    audio_exts = ["*.mp3", "*.wav", "*.m4a", "*.flac"]
    all_files = []
    for pattern in audio_exts:
        all_files.extend(MARKETING_DIR.rglob(pattern))
    
    audio_files = sorted(all_files)
    print(f"Found {len(audio_files)} audio files")
    
    # Process sequentially
    results = []
    for i, audio_path in enumerate(audio_files):
        print(f"Processing {i+1}/{len(audio_files)}: {audio_path.name}")
        result = create_transcription_entry(audio_path, i)
        results.append(result)
        print(f"  {'✓' if result.get('status') == 'success' else result.get('status', '?')}")
    
    # Save summary
    summary_path = AUDIO_TRANS_DIR / "transcription_summary.json"
    with open(summary_path, "w") as f:
        json.dump({"entries": len(results), "success": len([r for r in results if r.get('status') == 'success'])}, f)
    
    return results

if __name__ == "__main__":
    process_all_audio()