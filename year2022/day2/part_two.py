import sys

from part_one import compute_score, read_input


def find_player_two_move(player_one_move: str, outcome: str) -> str:
    match (player_one_move, outcome):
        case ("A", "X") | ("B", "Z") | ("C", "Y"):
            return "Z"
        case ("A", "Y") | ("B", "X") | ("C", "Z"):
            return "X"
        case ("A", "Z") | ("B", "Y") | ("C", "X"):
            return "Y"
        case _:
            raise ValueError("Bad player move or outcome")


def play(file_path: str):
    total_score = sum(
        compute_score(player_one_move, find_player_two_move(player_one_move, outcome))
        for player_one_move, outcome in read_input(file_path)
    )
    print(total_score)


if __name__ == "__main__":
    play(sys.argv[1])
