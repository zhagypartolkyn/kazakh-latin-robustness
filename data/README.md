# Data

| File | Description |
|---|---|
| `belebele_kaz_cyrl.jsonl` | Kazakh Belebele, original Cyrillic (900 questions) |
| `belebele_kaz_latn.jsonl` | The same 900 questions transliterated to the 2021 Latin alphabet |
| `translit_gold_50.csv` | 50 hand-checked sentences used to evaluate the transliterator |

Each line in the `.jsonl` files has `id`, `flores_passage`, `question`, `mc_answer1`–`mc_answer4` and `gold` (A–D). IDs and answer keys are identical in both files.

Derived from [Belebele](https://github.com/facebookresearch/belebele) (Bandarkar et al., 2024). License: CC BY-SA 4.0.
