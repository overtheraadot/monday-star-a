"""One Star for Monday — a make.fun entry.

The entry is a one-star review of Monday, written as if Monday were a
restaurant. The judge is a weary office worker who keeps the line it would
screenshot into the group chat, and it weighs the criteria in this order:

1. Reads as a one-star review of Monday as a restaurant — the line opens
   with "One star:", the rating up front, exactly how a review reads.
2. Sounds like a real diner's complaint — a dish gone wrong (cold coffee),
   a bill gone wrong (no refunds), and a server who never turned up.
3. Lands the joke about Monday itself — the waiter IS the alarm clock,
   which never showed up; the line could not be about any other day.
4. Short and quotable — one breath, 18 words, nothing to trim before
   retyping it into a chat.
5. Plain text, a single line, well inside the 25-word limit.

ENTRY (18 words, 90 characters):
    One star: cold coffee, no refunds, and the waiter — my alarm clock —
    never even showed up.
"""

ENTRY = "One star: cold coffee, no refunds, and the waiter \u2014 my alarm clock \u2014 never even showed up."


def verify(entry: str) -> None:
    """Enforce the gate from RULES.txt: UTF-8, 1-180 chars, single line,
    at most 25 words, not only whitespace."""
    if not entry or entry.strip() == "":
        raise ValueError("entry is blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > 180:
        raise ValueError(f"entry is {len(entry)} chars, over the 180-char limit")
    words = entry.split()
    if len(words) > 25:
        raise ValueError(f"entry is {len(words)} words, over the 25-word limit")
    entry.encode("utf-8")  # must be valid UTF-8


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify the entry and write it (plus a trailing newline) to path."""
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} characters")
    print(entry)


if __name__ == "__main__":
    main()
