
from typing import List, Tuple
import sys


def load_input(src_fn: str) -> Tuple[List[int], List[int]]:
    """Load two integer lists from a TSV input file."""
    with open(src_fn, 'r') as f:
        text_lines = f.readlines()
    text_tuples = [x.strip().split() for x in text_lines]
    l1 = []
    l2 = []
    for tpl in text_tuples:
        l1.append(int(tpl[0]))
        l2.append(int(tpl[1]))
    return l1, l2


def distance_between_lists(l1: List[int], l2: List[int]) -> int:
    """Compute distance between two lists."""
    l1s = sorted(l1)
    l2s = sorted(l2)
    distances = [abs(v1 - v2) for v1, v2 in zip(l1s, l2s)]
    return sum(distances)


def similarity_score(l1: List[int], l2: List[int]) -> int:
    """Compute similarity score between two lists."""
    counter = {}
    for el in l2:
        if el in counter:
            counter[el] += 1
        else:
            counter[el] = 1
    score = 0
    for el in l1:
        score += el * counter.get(el, 0)
    return score


def main() -> int:
    l1, l2 = load_input('day01/input_test.tsv')
    l3, l4 = load_input('day01/input_main.tsv')
    distance_test = distance_between_lists(l1, l2)
    distance_main = distance_between_lists(l3, l4)
    print(f'Distance Test: {distance_test}')
    print(f'Distance Main: {distance_main}')
    score_test = similarity_score(l1, l2)
    score_main = similarity_score(l3, l4)
    print(f'Similarity Score Test: {score_test}')
    print(f'Similarity Score Main: {score_main}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
