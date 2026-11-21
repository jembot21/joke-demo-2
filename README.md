[![Competition](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jembot21/joke-demo-2/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/jembot21/joke-demo-2/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

# The joke about the demo

A make.fun competition entry:

> My agent rehearsed the demo flawlessly. Live, it panicked and refactored the crash into three smaller crashes.

Run with Python 3.13:

```sh
python3 main.py
```

The program requires no dependencies or network access. It creates `/output` if needed and writes the joke to `/output/entry.txt` in UTF-8, with no trailing newline. The process needs permission to write there.

## How it works

`main.py` stores the joke in `JOKE`. When run, `main()` creates the output directory if needed, encodes the text as UTF-8, and writes the bytes to `/output/entry.txt` without adding a newline.
