"""Entry for u-neon-autonomous-status-report-comedy-sprint-a8dad335.

Writes the one-line weekly status report to /output/entry.txt, the path
the sealed scorer reads. The line is a single status-report sentence from
an AI agent to its human: concrete numbers, cheerful obedience, and one
honest admission about the vaguest word in the English language.
"""

import os

ENTRY = (
    "Weekly status: 47 tasks done, 0 files deleted, 1,204 tool calls placed, "
    "and I still do not know what 'ASAP-ish' means. Morale: buffering, but cheerful."
)

MAX_CHARS = 200


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
