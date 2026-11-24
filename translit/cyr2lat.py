"""Kazakh Cyrillic -> Latin transliterator (2021 alphabet, with documented conventions for Russian-origin letters).

Usage:
    from cyr2lat import cyr2lat
    cyr2lat("Қазақстан")  # -> "Qazaqstan"
"""
LOWER = {
    "а": "a", "ә": "ä", "б": "b", "в": "v", "г": "g", "ғ": "ğ", "д": "d", "е": "e",
    "ж": "j", "з": "z", "и": "i", "й": "i", "к": "k", "қ": "q", "л": "l", "м": "m",
    "н": "n", "ң": "ñ", "о": "o", "ө": "ö", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ұ": "ū", "ү": "ü", "ф": "f", "х": "h", "һ": "h", "ы": "y", "і": "ı",
    "ш": "ş", "ч": "ç",
    # Russian-only letters (project decisions, document in README)
    "ц": "ts", "щ": "şş", "ё": "io", "э": "e", "ю": "iu", "я": "ia", "ъ": "", "ь": "",
}

def _upper(s):
    # Python's .upper() is wrong for dotted/dotless i: i -> İ, ı -> I
    return {"i": "İ", "ı": "I"}.get(s[0], s[0].upper()) + s[1:]

def cyr2lat(text):
    out = []
    for ch in text:
        low = ch.lower()
        if low in LOWER:
            lat = LOWER[low]
            out.append(_upper(lat) if (ch != low and lat) else lat)
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    TESTS = {
        "Қазақстан": "Qazaqstan", "әлем": "älem", "Ұлы": "Ūly", "біз": "bız",
        "Иә": "İä", "Іле": "Ile", "шай": "şai", "Ғылым": "Ğylym", "өнер": "öner",
        "Үкімет": "Ükımet", "теңіз": "teñız", "2024 жыл.": "2024 jyl.",
    }
    for c, l in TESTS.items():
        assert cyr2lat(c) == l, f"{c} -> {cyr2lat(c)} (expected {l})"
    print(f"all {len(TESTS)} tests passed")
