
import re, sys

with open(sys.argv[1], 'r', encoding='utf-8-sig') as f:
    lines = f.read().split('\n')

blocks = []
current_block = []
i = 0

while i < len(lines):
    stripped = lines[i].strip()
    if re.match(r'^\d+$', stripped) and i + 1 < len(lines) and '-->' in lines[i + 1]:
        if current_block:
            blocks.append(current_block)
        current_block = []
        i += 2
        continue
    if '-->' in lines[i]:
        i += 1
        continue
    current_block.append(lines[i])
    i += 1

if current_block:
    blocks.append(current_block)

result = []
prev = ''
for block in blocks:
    text_lines = [re.sub(r'<[^>]+>', '', l).strip() for l in block]
    text_lines = [l for l in text_lines if l]
    if text_lines:
        last_line = text_lines[-1]
        if last_line != prev:
            result.append(last_line)
            prev = last_line

print(' '.join(result).replace('. ', '.\n\n'))