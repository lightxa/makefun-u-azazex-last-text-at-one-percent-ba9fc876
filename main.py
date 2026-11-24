"""Last Text at One Percent.

Writes the one final text message a dying phone sends at one
percent battery to /output/entry.txt.

Standard library only, deterministic, no network at runtime.
"""

from pathlib import Path

# Final text: the phone confesses it kept the ex's number on purpose.
# Cut the worn "Before I die" opener and gave the confession a motive
# ("for the drama") so the joke turns at the end instead of trailing off.
ENTRY_TEXT = (
    "Your ex is still in my contacts. "
    "I could have deleted them years ago. "
    "I kept the number for the drama. Goodbye."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
