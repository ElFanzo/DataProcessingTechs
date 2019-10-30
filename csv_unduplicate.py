"""Unduplicate .csv files, existing in the current directory."""

import os


def unduplicate():
    files = []
    names = []
    for file in os.listdir("."):
        if file.endswith(".csv"):
            files.append(set(open(file, "r", encoding="utf-8").read().split(",")))
            names.append(file)

    for i in range(1, len(files)):
        for j in range(i):
            files[i] = files[i].difference(files[j])

        with open(names[i], "w", encoding="utf-8") as file:
            file.write(",".join(row for row in files[i]))


if __name__ == "__main__":
    unduplicate()
