#!/bin/bash
# /home/fhs_kevin/BusinessOS/push_and_backup.sh
# Auto-backup and push new transcription/mapping artifacts to remote repo

# -----------------------------
# Configuration
# -----------------------------
REPO_ROOT="/home/fhs_kevin/BusinessOS"
AUDIO_DIR="/home/fhs_kevin/BusinessOS/knowledge_base/audio_transcriptions"
MAPPINGS_DIR="/home/fhs_kevin/BusinessOS/knowledge_base/knowledge_mappings"
OPERATIONS_DIR="/home/fhs_kevin/BusinessOS/knowledge_base/operations"
AGENTS_DIR="/home/fhs_kevin/BusinessOS/knowledge_base/operations/Agents"

# -----------------------------
# Stage All Relevant Changes
# -----------------------------
git -C "$REPO_ROOT" add "$AUDIO_DIR" "$MAPPINGS_DIR" "$OPERATIONS_DIR" "$AGENTS_DIR"

# -----------------------------
# Commit If Changes Exist
# -----------------------------
if git -C "$REPO_ROOT" diff --cached --quiet; then
    echo "No staged changes to commit."
    exit 0
fi

# -----------------------------
# Commit With Timestamped Message
# -----------------------------
COMMIT_MSG="Auto-commit: New transcriptions & mappings - $(date +%Y-%m-%d_%H:%M:%S)"
git -C "$REPO_ROOT" commit -m "$COMMIT_MSG"

# -----------------------------
# Push To Remote (origin master)
# -----------------------------
git -C "$REPO_ROOT" push origin master

echo "✅ Backup complete - changes pushed to origin/master"