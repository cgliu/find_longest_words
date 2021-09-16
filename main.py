"""
Find the longest English word that can be typed with the first line
of a standard keyboard.
"""


def find_sorted_longest_words(filename):
    must_have = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    candidates = []
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.rstrip("\n")
            all_in_must_have = True
            for c in line:
                all_in_must_have &= c in must_have
            if all_in_must_have:
                candidates.append(line)
    candidates.sort(reverse=True, key=len)
    return candidates


if __name__ == "__main__":
    words = find_sorted_longest_words('./words_alpha.txt')
    top10 = words[:10]
    for word, length in zip(top10, map(len, top10)):
        print(f"{word} {length}")
