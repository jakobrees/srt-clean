# yt-text

Converts YouTube subtitles into a clean transcript. Built for macOS.

## Requirements

Install `yt-dlp` via Homebrew:
```bash
brew install yt-dlp
```

## Setup

**1. Add the following to your `.zshrc` or `.bashrc`:**
```bash
yt-text() {
    local url="$1"
    local output="${2:-transcription.txt}"

    if [[ -z "$url" ]]; then
        echo "Usage:   yt-text <youtube_url> [output_file]"
        echo "Example: yt-text https://youtu.be/jPrdCuYD-t0 my_transcript.txt"
        return 1
    fi

    yt-dlp --skip-download --write-auto-subs \
        --sub-lang "en,en-US,en-orig" \
        --convert-subs srt \
        -o "subtitle" "$url"

    local srt_file
    srt_file=$(ls subtitle*.srt 2>/dev/null | head -1)

    if [[ -z "$srt_file" ]]; then
        echo "✗  Error: No subtitle file found"
        return 1
    fi

    python3 ~/.local/bin/srt_clean.py "$srt_file" > "$output"
    rm -f "$srt_file"
    echo "✓  Saved to: $output"
}
```

**2. Copy `srt_clean.py` to `~/.local/bin/`:**
```bash
mkdir -p ~/.local/bin
cp srt_clean.py ~/.local/bin/srt_clean.py
```

**3. Reload your shell:**
```bash
source ~/.zshrc
```

## Usage

```bash
# Default output → transcription.txt
yt-text https://youtu.be/jPrdCuYD-t0

# Custom output filename
yt-text https://youtu.be/jPrdCuYD-t0 my_transcript.txt
```
