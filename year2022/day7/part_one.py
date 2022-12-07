import sys
import typing


def read_commands(file_path: str) -> typing.Generator[tuple, None, None]:
    with open(file_path) as f:
        try:
            # commands start with cd /
            # let's skip this command
            next(f)
        except StopIteration as e:
            raise EOFError from e
        for line in f:
            yield tuple(line.split())


def traverse_tree(
    commands: typing.Generator[tuple, None, None],
    filter: typing.Callable,
    kept_nodes: list[int],
) -> dict[str, int | dict]:
    current_tree = {"size": 0, "sub_dirs": {}, "sub_files": {}}
    try:
        command = next(commands)
        while True:
            match command:
                case ("$", "cd", ".."):
                    if filter(current_tree["size"]):
                        kept_nodes.append(current_tree["size"])
                    return current_tree
                case ("$", "cd", _ as sub_dir):
                    current_tree["sub_dirs"][sub_dir] = traverse_tree(
                        commands, filter, kept_nodes
                    )
                    current_tree["size"] += current_tree["sub_dirs"][sub_dir]["size"]
                    command = next(commands)
                case ("$", "ls"):
                    while (command := next(commands))[0] != "$":
                        if (size := command[0]).isdigit():
                            current_tree["size"] += int(size)
    except StopIteration:
        return current_tree


def main(file_path: str):
    reader = read_commands(file_path)
    sizes = []
    traverse_tree(reader, lambda size: size <= 100_000, sizes)
    print(sum(sizes))


if __name__ == "__main__":
    main(sys.argv[1])
