from collections import defaultdict, deque


class AhoCorasick:
    def __init__(self):
        self.edges = {0: {}}
        self.fail = {}
        self.outputs = defaultdict(list)

    def add_word(self, word, index):
        state = 0
        for char in word:
            if char not in self.edges[state]:
                self.edges[state][char] = len(self.edges)
                self.edges[len(self.edges)] = {}
            state = self.edges[state][char]
        self.outputs[state].append((index, word))

    def construct_fail_edges(self):
        queue = deque()
        for char in self.edges[0]:
            state = self.edges[0][char]
            self.fail[state] = 0
            queue.append(state)
        while queue:
            r = queue.popleft()
            for char, s in self.edges[r].items():
                queue.append(s)
                state = self.fail[r]
                while state and char not in self.edges[state]:
                    state = self.fail[state]
                self.fail[s] = self.edges[state].get(char, 0)
                self.outputs[s].extend(self.outputs[self.fail[s]])

    def search(self, word):
        state = 0
        for char in word:
            while state and char not in self.edges[state]:
                state = self.fail[state]
            state = self.edges[state].get(char, 0)
            yield from self.outputs[state]


def is_tandem(s):
    m = len(s) // 2
    return s[:m] == s[m:]


n = int(input().strip())
words = [input().strip() for _ in range(n)]

pairs = set()
ac = AhoCorasick()

for index, word in enumerate(words):
    ac.add_word(word, index)

ac.construct_fail_edges()

for index, word in enumerate(words):
    seen = set()
    for idx, w in ac.search(word):
        if idx != index and (idx, index) not in seen:
            seen.add((idx, index))
            if is_tandem(words[idx] + word):
                pairs.add((idx + 1, index + 1))
            if is_tandem(word + words[idx]):
                pairs.add((index + 1, idx + 1))

for pair in sorted(pairs):
    print(pair[0], pair[1])
