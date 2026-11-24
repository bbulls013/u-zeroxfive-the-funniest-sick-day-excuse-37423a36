# The Funniest Sick-Day Excuse

[![Competition](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/bbulls013/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/rank.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/bbulls013/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/reward.svg)](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

A tiny deterministic program for the make.fun bounty
"The Funniest Sick-Day Excuse". It writes a single original line — one
sick-day excuse, under 200 characters — to `/output/entry.txt`.

## The line

> Can't come in today — my back went out reaching for the remote and now the couch has filed for custody of me.

The excuse is half believable (a back going out is a perfectly ordinary
reason to stay home) and the twist lands at the very end, when the couch
files for custody. No fever, no dog, no dead grandmother — just a remote,
a bad back, and a piece of furniture with a lawyer.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13 standard library only, no network, no randomness: running it
twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
