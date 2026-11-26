"""One-line pizza topping pitch for the make.fun "The Worst Pizza Topping" bounty.

Writes a single funny line, under 200 characters, pitching a terrible
pizza topping to /output/entry.txt. Pure standard library, deterministic:
the same text on every run.
"""

import os

LINE = (
    "Try our new pizza topping: a single wet sock, gently steamed over the "
    "cheese \u2014 it tastes like laundry day, it smells like defeat, and it "
    "pairs beautifully with regret."
)


def main():
    # The gate requires 1 to 200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert LINE.strip(), "entry line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
