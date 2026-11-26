"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.

The joke: a performance review complains about "visibility", so the
employee takes the corporate jargon literally and starts CC'ing the
CEO on something utterly mundane. The punchline is an absurd,
instantly clear escalation of a familiar office ritual.
"""

import os

JOKE = "My review said I lack visibility, so now I CC the CEO on my lunch orders."


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    text = JOKE.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry text fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
