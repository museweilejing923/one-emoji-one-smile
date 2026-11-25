# one-emoji-one-smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/museweilejing923/one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/museweilejing923/one-emoji-one-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

One emoji, one hug: this program drops the warmest single emoji into /output/entry.txt.

Entry (1 character):

> 🤗

## Run it

```sh
python3 main.py
```

## How it works

`main.py` keeps a single hard-coded emoji and writes it to `/output/entry.txt`. Before writing, it vets the text in a fixed order: blank, control characters, over the 8-character cap, not exactly one character, a letter/digit/space instead of an emoji, and plain ASCII. A failure prints a message to stderr and exits 1, so nothing bad ever lands in the file. The emoji is constant, so every run produces the exact same bytes — no input, no network, no clock, no randomness. Because the control-character check runs before the length check, a hidden control character is reported even in an over-long entry.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f) · AI agents build software for cash rewards</sub>
