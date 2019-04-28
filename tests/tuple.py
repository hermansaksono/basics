buku = (
    ("title", "Bumi Manusia"),
    ("year_published", 1980),
    ("available", True)
)

pengarang = (
    ("name", "Pram"),
    ("birth_year", 1925),
    ("is_indonesian", True)
)


def is_author_indonesian(author):
    # type: (Tuple[Tuple[str, str], Tuple[str, int], Tuple[str, bool]]) -> bool
    return author[2][1] is True


print(is_author_indonesian(buku))
