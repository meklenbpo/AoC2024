
from typing import List

Report = List[int]


def load_input(src_fn: str) -> List[Report]:
    """Load source data from input file."""
    with open(src_fn, 'r') as f:
        lines = f.readlines()
    data_str = [x.split() for x in lines]
    data_int = [[int(x) for x in y] for y in data_str]
    return data_int


def is_report_safe(report: Report) -> bool:
    """Assess if report is safe or not based on task rules."""
    diffs = [next_el - curr_el for curr_el, next_el in zip(report, report[1:])]
    is_decreasing = all([x <= 0 for x in diffs])
    is_increasing = all([x >= 0 for x in diffs])
    safe_steps = all([0 < abs(x) < 4 for x in diffs])
    is_safe = (is_decreasing or is_increasing) and safe_steps
    return is_safe


def is_safe_with_dampener(report: Report) -> bool:
    """Test all variants of `dampened` reports and return True if at
    least one of them is safe."""
    safes = []
    for idx in range(len(report)):
        p1 = report[:idx]
        p2 = report[idx + 1:]
        damp_report = p1 + p2
        safes.append(is_report_safe(damp_report))
    return any(safes)


def count_safe_reports(data: List[Report]) -> int:
    safes = [is_safe_with_dampener(x) for x in data]
    count_safes = sum(safes)
    return count_safes


def main() -> int:
    data_test = load_input('day02/input_test.txt')
    data_main = load_input('day02/input_main.txt')
    print(count_safe_reports(data_test))
    print(count_safe_reports(data_main))
    return 0


if __name__ == '__main__':
    main()
