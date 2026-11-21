"""Write the competition joke to /output/entry.txt as UTF-8 without a newline."""

from pathlib import Path


JOKE = "My agent rehearsed the demo flawlessly. Live, it panicked and refactored the crash into three smaller crashes."


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
