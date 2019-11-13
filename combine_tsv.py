"""This script combines all the TSV files into two TSV files.

One contains files' names, another - their content.
Files are creating in 'results' directory.
"""

import os


def combine():
    """Read TSV files and create two TSV files."""
    try:
        os.mkdir("results")
    except FileExistsError:
        pass

    files_content = open("results/files_content.tsv", "w")
    files_name = open("results/files_name.tsv", "w")

    for file in os.listdir("."):
        if file.endswith(".tsv"):
            with open(file, "r") as f:
                files_content.write(f.read().replace("\n", ",") + "\n")
                files_name.write(file + "\n")

    files_content.close()
    files_name.close()


if __name__ == "__main__":
    combine()
