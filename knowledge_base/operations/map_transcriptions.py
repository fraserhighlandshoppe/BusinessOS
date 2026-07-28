#!/usr/bin/env python3
"""Map transcription content to framework topics"""
import json
import re
from pathlib import Path
from collections import defaultdict

TRANSCRIPTIONS_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions")
GURUS_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/gurus")
OUTPUT_DIR = Path("/home/fhs_kevin/BusinessOS/knowledge_base/knowledge_mappings")
OUTPUT_DIR.mkdir(exist_ok=True)

GURU_KEYWORDS = {
    "DM": ["direct mail", "list building", "profits", "sales copy"],
    "Ali Brown": ["marketing", "business", "sales funnel", "email marketing"],
    "Grant Cardone": ["10x", "marketing", "sales", "growth", "money"],
    "Dan Kennedy": ["direct copy", "sales letters", "marketing", "persuasion"],
    "Perry Marshall": ["ads", "facebook", "google ads", "ppc", "advertising"],
    "ResearchFreak": ["market research", "customer behavior", "data"],
}

def extract_topics(content):
    """Extract potential topics from transcription content"""
    topics = []
    content_lower = content.lower()
    
    for guru, keywords in GURU_KEYWORDS.items():
        for keyword in keywords:
            if keyword in content_lower:
                topics.append((guru, keyword))
    
    return topics

def map_transcriptions():
    """Create metadata mappings for all transcriptions"""
    mappings = []
    
    for transcription_file in TRANSCRIPTIONS_DIR.glob("*.md"):
        if transcription_file.name == "transcription_index.json":
            continue
            
        content = transcription_file.read_text()
        topics = extract_topics(content)
        
        file_mapping = {
            "file": str(transcription_file),
            "topics": [{"guru": t[0], "keyword": t[1]} for t in topics],
            "framework_references": []
        }
        
        for guru, keyword in topics:
            framework_path = GURUS_DIR / guru / "Brand_Framework.md"
            if framework_path.exists():
                file_mapping["framework_references"].append(str(framework_path))
        
        mappings.append(file_mapping)
    
    output_file = OUTPUT_DIR / "topic_mappings.json"
    with open(output_file, "w") as f:
        json.dump({"created": str(Path().stat().st_mtime), "mappings": mappings}, f, indent=2)
    
    return mappings

def generate_insights():
    """Generate cross-guru insights from mappings"""
    with open(OUTPUT_DIR / "topic_mappings.json") as f:
        data = json.load(f)
    
    insights = defaultdict(list)
    for mapping in data["mappings"]:
        for topic in mapping["topics"]:
            insights[topic["keyword"]].append({
                "guru": topic["guru"],
                "source": mapping["file"]
            })
    
    output_file = OUTPUT_DIR / "cross_guru_insights.md"
    with open(output_file, "w") as f:
        f.write("# Cross-Guru Insights from Transcriptions\n\n")
        for keyword, sources in insights.items():
            f.write(f"## {keyword.title()}\n\n")
            for source in sources:
                f.write(f"- {source['guru']} perspective in {Path(source['source']).name}\n")
            f.write("\n")
    
    return insights

if __name__ == "__main__":
    mappings = map_transcriptions()
    print(f"Created {len(mappings)} topic mappings")
    insights = generate_insights()
    print(f"Generated {len(insights)} cross-guru insights")
    # After mapping, trigger backup and push
    backup_script="/home/fhs_kevin/BusinessOS/push_and_backup.sh"
    if [ -f "$backup_script" ]; then
        echo "Running backup and push script..."
        bash "$backup_script"
    else
        echo "Backup script not found: $backup_script"
    fi