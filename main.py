from pathlib import Path


# Main entry point
def main():
    p = Path('/Users/tkrehbiel/Downloads')
    for f in sorted(p.glob("*.zip"), key=lambda i: i.name.casefold()):
        print(f.name)


if __name__ == "__main__":
    main()
