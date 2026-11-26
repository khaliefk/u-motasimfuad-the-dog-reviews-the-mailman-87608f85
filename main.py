"""The Dog Reviews the Mailman — one-liner entry.

Writes one funny one-line review a dog gives the mailman to /output/entry.txt.
Stdlib only. No network, no files read.
"""

import os
import sys

ENTRY = (
    "Shows up daily, shoves paper through my slot, and runs off "
    "before I can file a complaint. Four stars, strictly for consistency."
)


def validate(text):
    """Gate: UTF-8 text, 1-200 chars, not whitespace-only, single line."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > 200:
        raise ValueError(f"entry too long: {len(text)} chars (max 200)")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()
