#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path

README = Path("README.md")
if not README.exists():
    print("README.md not found")
    raise SystemExit(1)

text = README.read_text(encoding="utf-8")
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
if "<!--LAST_UPDATED-->" not in text:
    print("Placeholder <!--LAST_UPDATED--> not found in README.md")
    raise SystemExit(0)

new_text = text.replace("<!--LAST_UPDATED-->", now)
if new_text != text:
    README.write_text(new_text, encoding="utf-8")
    print(f"Updated README.md with timestamp: {now}")
else:
    print("No changes needed")
