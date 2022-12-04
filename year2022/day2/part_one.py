import sys
import typing

SHAPE_SCORE = {
    "X": 1,  # Rock is worth 1 point
    "Y": 2,  # Paper is worth 2 points
    "Z": 3,  # Scissors is worth 3 points
}


def read_input(
    file_path: str,
) -> typing.Generator[tuple[str, str], None, None]:
    with open(file_path) as f:
        for line in f:
            moves: tuple[str, str] = tuple(line.strip().split())
            yield moves


def compute_score(player_one_move: str, player_two_move: str) -> int:
    outcome = 0
    match (player_one_move, player_two_move):
        case ("A", "Z") | ("B", "X") | ("C", "Y"):  # lose
            outcome = 0
        case ("A", "X") | ("B", "Y") | ("C", "Z"):  # draw
            outcome = 3
        case _:  # win
            outcome = 6
    total_score = outcome + SHAPE_SCORE[player_two_move]
    return total_score


def play(file_path: str):
    total_score = sum(compute_score(*moves) for moves in read_input(file_path))
    print(total_score)


if __name__ == "__main__":
    play(sys.argv[1])
