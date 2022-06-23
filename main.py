from pathlib import Path


def main(pathname):
    p = Path(pathname)
    for f in sorted(p.glob("*.*"), key=lambda i: i.name.casefold()):
        print(f.name)


if __name__ == "__main__":
    import sys
    path = "."
    if len(sys.argv) > 1:
        path = sys.argv[1]
    print(path)
    main(path)
