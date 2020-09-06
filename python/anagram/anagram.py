def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]


def is_anagram(a, b):
    a, b = a.lower(), b.lower()
    return a != b and sorted(a) == sorted(b)
