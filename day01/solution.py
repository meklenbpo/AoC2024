
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


def main() -> int:
    l1, l2 = load_input('day01/input_main.tsv')
    distance = distance_between_lists(l1, l2)
    print(distance)
    return 0


if __name__ == '__main__':
    sys.exit(main())
