import os, sys
from processor import merge_files, make_pdf


def main():
    if len(sys.argv) != 2:
        print("Usage: py md-pdf.py <directory>")
        sys.exit(1)

    dir = rf"{sys.argv[1]}"
    if not os.path.exists(dir):
        print(f"Directory {dir} does not exist.")
        sys.exit(1)
    merge_files(dir)
    print("\nGenerating PDF...\n---")
    make_pdf(dir)


if __name__ == "__main__":
    main()