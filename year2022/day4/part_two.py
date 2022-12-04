import sys

from part_one import read_assignments


def is_slightly_overlapping(
    assignement_1: tuple[int, int], assignement_2: tuple[int, int]
) -> bool:
    start_section_1, end_section_1 = assignement_1
    start_section_2, end_section_2 = assignement_2
    return start_section_1 <= end_section_2 and start_section_2 <= end_section_1


def main(input_path: str):
    overlapping_assignments = sum(
        is_slightly_overlapping(*assignements_pair)
        for assignements_pair in read_assignments(input_path)
    )
    print(overlapping_assignments)


if __name__ == "__main__":
    main(sys.argv[1])
