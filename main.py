import yaml


def load_index(pathname: str):
    import os
    filename = os.path.join(pathname, "_index.yaml")
    with open(filename, "r") as file:
        index = yaml.safe_load(file)
    testname = os.path.join(pathname, "_index_rewrite.yaml")
    with open(testname, "w") as file:
        yaml.dump(index, file, sort_keys=False, encoding="utf-8", allow_unicode=True, width=999)
    return


def main(pathname: str):
    from pathlib import Path
    pathinfo = Path(pathname)
    files = sorted(pathinfo.glob("*.mp4"), key=lambda i: i.name.casefold())
    for file in files:
        print(file.name)
    return


if __name__ == "__main__":
    import sys

    path = "./files"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    print("path:", path)
    load_index(path)
    main(path)
