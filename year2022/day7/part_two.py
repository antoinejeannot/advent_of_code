import sys

from part_one import read_commands, traverse_tree


def main(file_path: str):
    disk_size, memory_needed = 70_000_000, 30_000_000
    sizes = []
    reader = read_commands(file_path)
    tree = traverse_tree(reader, lambda size: size > 0, sizes)
    min_dir_size_to_free = min(
        size for size in sizes if size >= memory_needed - disk_size + tree["size"]
    )
    print(min_dir_size_to_free)


if __name__ == "__main__":
    main(sys.argv[1])
