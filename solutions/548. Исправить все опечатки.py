from collections import defaultdict


def generate_variants(word):
    variants = set()
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(word)):
        for c in letters:
            if c != word[i]:
                variants.add(word[:i] + c + word[i + 1:])

    for i in range(len(word)):
        variants.add(word[:i] + word[i + 1:])

    for i in range(len(word) + 1):
        for c in letters:
            variants.add(word[:i] + c + word[i:])

    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            variants.add(word[:i] + word[i + 1] + word[i] + word[i + 2:])

    return variants


def precompute_dictionary(dictionary):
    precomputed = defaultdict(list)
    for word in dictionary:
        variants = generate_variants(word)
        for var in variants:
            precomputed[var].append(word)
    return precomputed


def process_queries(dictionary, precomputed, queries):
    results = []
    for word in queries:
        if word in dictionary:
            results.append(f'{word} 0')
        elif word in precomputed:
            correction = precomputed[word]
            results.append(f'{word} 1 {correction[0]}')
        else:
            found = False
            for variant in generate_variants(word):
                if variant in precomputed:
                    correction = precomputed[variant]
                    results.append(f'{word} 2 {variant} {correction[0]}')
                    found = True
                    break
            if not found:
                results.append(f'{word} 3+')
    return results


with open("/kaggle/input/ochepyatki/dict.txt", "r", encoding="utf-8") as f:
    dictionary = set(f.read().splitlines())

precomputed = precompute_dictionary(dictionary)

with open("/kaggle/input/ochepyatki/queries.txt", "r", encoding="utf-8") as f:
    queries = f.read().splitlines()

results = process_queries(dictionary, precomputed, queries)

with open("answer.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))
