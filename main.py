from pathlib import Path

ENTRY = (
    "An hour-long meeting where two people talk and 28 unmute in unison "
    "just to say 'Thanks everyone, bye!'"
)


def main() -> None:
    # Strip any leading/trailing whitespace
    line = ENTRY.strip()

    # Validate single line
    if "\n" in line or "\r" in line:
        raise ValueError("Entry must be a single line without embedded newlines.")

    # Validate character length
    if not (1 <= len(line) <= 200):
        raise ValueError(
            f"Entry length must be 1-200 characters (got {len(line)})."
        )

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"

    entry_path.write_text(line + "\n", encoding="utf-8")

    # Verify written content
    final_text = entry_path.read_text(encoding="utf-8")
    lines = final_text.splitlines()
    if len(lines) != 1:
        raise ValueError(f"Output must contain exactly one line (got {len(lines)}).")

    print(lines[0])
    print(f"Character count: {len(lines[0])}")


if __name__ == "__main__":
    main()
