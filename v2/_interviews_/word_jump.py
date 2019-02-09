from collections import deque, defaultdict
import fileinput


class WordJump:
    def __init__(self, wordList):
        # Make it into a set for a O(1) lookup check
        self.wordList = set(wordList)

        # Used to decrease the search space by using only the letters that live on the
        # given positions
        index = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                # On index i all letters with at least 1 occurrence on index i
                index[i].add(word[i])

        self.graph = defaultdict(set)
        for word in self.wordList:
            for i in range(len(word)):
                for c in index[i]:
                    candidate = word[:i] + c + word[i + 1 :]
                    if candidate in self.wordList:
                        self.graph[word].add(candidate)

    def find(self, begin_word, end_word):
        # On the frontier, we keep the cost, the current word and the path so far
        frontier = deque([(0, begin_word, [begin_word])])

        res = []
        min_cost = None
        visited = {begin_word: 0}

        while len(frontier) > 0:
            cost, cur_word, path = frontier.popleft()

            if cur_word == end_word:
                # The first hit will be at the minimun cost as we are using a bfs
                if min_cost is None:
                    min_cost = cost
                if cost == min_cost:
                    res.append(path)

            if min_cost is not None and cost > min_cost:
                # If we are seeing a cost higher than the min_cost, we already visited
                # all nodes at the min_cost
                break

            # Make the current path a set for O(1) lookup
            path_set = set(path)
            n_cost = cost + 1
            for candidate in self.graph[cur_word]:
                if (
                    candidate in self.wordList
                    and candidate not in path_set
                    and (candidate not in visited or visited[candidate] >= n_cost)
                ):
                    visited[candidate] = n_cost
                    frontier.append((n_cost, candidate, path + [candidate]))

        return len(res), res


class Problem:
    def __init__(self):
        self.start = None
        self.end = None

    def __str__(self):
        return "{},{}".format(self.start, self.end)


def parse_stdin():
    words = []
    problems = []

    # Load all file in memory
    # NOTE: might be a problem for big files
    input = []
    for line in fileinput.input():
        input.append(line.strip("\n"))

    # Load the problem. First line with problem count.
    # Each problem takes 2 lines
    problem_lines = 2 * int(input[0])
    for i in range(1, problem_lines, 2):
        # Loop jumps 2 at a time
        problem = Problem()
        problem.start = input[i]
        problem.end = input[i + 1]
        problems.append(problem)

    idx = 1 + problem_lines
    word_count = int(input[idx])
    idx += 1  # Move cursor to first word
    for i in range(word_count):
        words.append(input[idx + i])

    return problems, words


# Reads the input
problems, words = parse_stdin()
# Creates the jumper
jumper = WordJump(words)
# Generates output for each problem
for p in problems:
    _len, solutions = jumper.find(p.start, p.end)
    print(_len)
    if _len:
        for solution in solutions:
            print(",".join(solution))

