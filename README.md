# tiny-chess-01 — 4KB chess engine

Original MIT chess engine for the make.fun `tiny-chess-01` bounty: a complete
engine in 4,072 bytes of Python (stdlib only, deterministic).

- 0x88 board, negamax alpha-beta + quiescence, MVV-LVA ordering, iterative
  deepening under a fixed node budget.
- Eval: material + pawn-advance bonus + king rank penalty.
- Plays through the kit env (`main.py`, Python 3.13, `python3 -P -s`).

Practice Elo 876 (trial-0, official scorer) — below the 1,154 floor. This entry
is a pipeline-validation submission, not a contender for a paid place.
