#!/usr/bin/env python3
"""
CoS State Sync Script

Syncs dynamic state files from CoS agent workspace to GitHub repo.
Run every 6 hours via cron.

Usage:
    python3 sync-state.py [--dry-run] [--verbose]
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

# Configuration
WORKSPACE_ROOT = "/home/node/.openclaw/workspace"
REPO_ROOT = "/tmp/cos-workspace-sync"  # Clone location for sync
GITHUB_REPO = "https://github.com/cos-eng/cos-workspace.git"

# Files to sync (source → destination in repo)
DYNAMIC_FILES = {
    # Orchestrator (main) files
    f"{WORKSPACE_ROOT}/MEMORY.md": "state/agents/main/MEMORY.md",
    
    # Shared knowledge files
    f"{WORKSPACE_ROOT}/CLIENT_LIST.md": "state/knowledge/CLIENT_LIST.md",
    f"{WORKSPACE_ROOT}/PROSPECT_LIST.md": "state/knowledge/PROSPECT_LIST.md",
    f"{WORKSPACE_ROOT}/CLIENT_STAKEHOLDERS.md": "state/knowledge/CLIENT_STAKEHOLDERS.md",
    f"{WORKSPACE_ROOT}/ORG_CHART.md": "state/knowledge/ORG_CHART.md",
    f"{WORKSPACE_ROOT}/DIRECT_REPORTS.md": "state/knowledge/DIRECT_REPORTS.md",
}

STATIC_FILES = {
    # Static config files (only synced on change)
    f"{WORKSPACE_ROOT}/SOUL.md": "state/agents/main/SOUL.md",
    f"{WORKSPACE_ROOT}/HEARTBEAT.md": "state/agents/main/HEARTBEAT.md",
    f"{WORKSPACE_ROOT}/TOOLS.md": "state/agents/main/TOOLS.md",
    f"{WORKSPACE_ROOT}/IDENTITY.md": "state/agents/main/IDENTITY.md",
    f"{WORKSPACE_ROOT}/USER.md": "state/agents/main/USER.md",
    f"{WORKSPACE_ROOT}/AGENTS.md": "state/agents/main/AGENTS.md",
}

def get_file_hash(filepath):
    """Calculate SHA256 hash of file content."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def clone_or_pull_repo():
    """Clone repo if not exists, otherwise pull latest."""
    if not os.path.exists(REPO_ROOT):
        print(f"Cloning repo to {REPO_ROOT}")
        subprocess.run(["git", "clone", GITHUB_REPO, REPO_ROOT], check=True)
    else:
        print(f"Pulling latest from repo")
        subprocess.run(["git", "-C", REPO_ROOT, "pull"], check=True)

def copy_file(src, dst, dry_run=False, verbose=False):
    """Copy file from source to destination in repo."""
    src_path = Path(src)
    dst_path = Path(REPO_ROOT) / dst
    
    if not src_path.exists():
        if verbose:
            print(f"  Source file does not exist: {src}")
        return False
    
    # Create destination directory if needed
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    
    if dry_run:
        print(f"  Would copy: {src} → {dst}")
        return True
    
    # Copy file
    import shutil
    shutil.copy2(src_path, dst_path)
    
    if verbose:
        print(f"  Copied: {src} → {dst}")
    
    return True

def update_readme_timestamp():
    """Update last sync timestamp in README.md."""
    readme_path = Path(REPO_ROOT) / "README.md"
    if not readme_path.exists():
        return
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    new_content = content.replace(
        "## Last Sync\n_Updated automatically by sync script_",
        f"## Last Sync\n{timestamp} — Updated automatically by sync script"
    )
    
    with open(readme_path, 'w') as f:
        f.write(new_content)

def main():
    parser = argparse.ArgumentParser(description="Sync CoS state to GitHub")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--static", action="store_true", help="Sync static files (not just dynamic)")
    args = parser.parse_args()
    
    print(f"CoS State Sync - {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Workspace: {WORKSPACE_ROOT}")
    print(f"Repo: {REPO_ROOT}")
    
    # Clone or pull repo
    if not args.dry_run:
        clone_or_pull_repo()
    
    # Determine which files to sync
    files_to_sync = DYNAMIC_FILES.copy()
    if args.static:
        files_to_sync.update(STATIC_FILES)
    
    # Copy files
    copied_count = 0
    for src, dst in files_to_sync.items():
        if copy_file(src, dst, args.dry_run, args.verbose):
            copied_count += 1
    
    # Update README timestamp
    if not args.dry_run and copied_count > 0:
        update_readme_timestamp()
        
        # Commit and push
        subprocess.run(["git", "-C", REPO_ROOT, "add", "."], check=True)
        
        commit_msg = f"CoS State Sync - {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}"
        subprocess.run(["git", "-C", REPO_ROOT, "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "-C", REPO_ROOT, "push"], check=True)
        
        print(f"✓ Synced {copied_count} files to GitHub")
    elif args.dry_run:
        print(f"✓ Dry run: Would sync {copied_count} files")
    else:
        print("✓ No files needed syncing")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())