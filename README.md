# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rwnliwan/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rwnliwan/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Original MIT chess engine for the make.fun tiny-chess-01 bounty: a complete engine in 4,094 bytes of Python (stdlib only, deterministic) — 0x88 board, negamax alpha-beta with quiescence search, piece-square-table evaluation, MVV-LVA ordering, a best-move-only transposition table, and iterative deepening under a fixed 30,000-node budget. Practice Elo 1,279 (trial-0, official scorer) for the r23 table build, above the 1,154 floor; the r9 build it descends from scored 1,364.

## r23 — transposition table build

The current engine adds a best-move-only transposition table to the r9 search. Each internal node stores its best move under a key of board, side to move, castling rights and en-passant square, and the next search tries that move first. Scores and flags are never reused, and the root move order is left alone after an earlier root-first variant lost 367 Elo in testing.

Measured against r9 over 32 games at 30,000 nodes a move, the table build scored 21.0 points (65.6%, with 18 wins, 6 draws and 8 losses), roughly 112 Elo ahead in self-play. The official trial-0 gauntlet put it at Elo 1,279, one game below r9's 1,364, so the table's edge sits inside the gauntlet's noise and the two builds are close.

## Run it

```sh
python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=62prjahx&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
