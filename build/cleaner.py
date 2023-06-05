import os

def rm_dir(path: str):
    items = os.ilistdir(path)

    # Remove all files and directories in `path`
    for item in items:
        print(f"Removing {item}")

        # type 0x4000 is a directory
        # type 0x8000 is a file
        item_path = f"{path}/{item[0]}"
        is_dir = item[1] == 0x4000
        if is_dir:
            rm_dir(path=item_path)
            os.rmdir(item_path)
        else:
            os.remove(item_path)


if __name__ == "__main__":
    rm_dir(path="/flash")
