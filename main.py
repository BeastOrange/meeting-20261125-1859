from pathlib import Path

ENTRY = (
    "A 30-person meeting where two people talk and 28 unmute in unison "
    "to chorus 'Thanks everyone, bye!'"
)


def main() -> None:
    # Strip any trailing whitespace from the line before validating
    line = ENTRY.rstrip()

    # Validate single line
    if "\n" in line or "\r" in line:
        raise ValueError("Entry must be a single line without embedded newlines.")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"

    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    # Length check uses the final written text
    final_text = entry_path.read_text(encoding="utf-8").rstrip("\r\n")
    char_count = len(final_text)

    if not (1 <= char_count <= 200):
        raise ValueError(
            f"Final written text length must be 1-200 characters (got {char_count})."
        )

    print(final_text)
    print(f"Character count: {char_count}")


if __name__ == "__main__":
    main()
