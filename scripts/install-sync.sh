#!/bin/bash
# Install CoS State Sync cron job

set -e

echo "Installing CoS State Sync..."

# Create sync directory
SYNC_DIR="/home/node/.openclaw/cos-sync"
mkdir -p "$SYNC_DIR"

# Copy sync script
cp sync-state.py "$SYNC_DIR/"
chmod +x "$SYNC_DIR/sync-state.py"

# Create cron entry for every 6 hours
CRON_ENTRY="0 */6 * * * cd $SYNC_DIR && python3 sync-state.py >> $SYNC_DIR/sync.log 2>&1"

# Add to crontab
(crontab -l 2>/dev/null | grep -v "sync-state.py"; echo "$CRON_ENTRY") | crontab -

# Test run
echo "Running test sync..."
cd "$SYNC_DIR"
python3 sync-state.py --verbose

echo "✓ Sync installed successfully"
echo "Cron schedule: Every 6 hours (0,6,12,18 UTC)"
echo "Logs: $SYNC_DIR/sync.log"
echo "Repo: https://github.com/cos-eng/cos-workspace"