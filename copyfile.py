#!/usr/bin/env python3
""" Copies a source and duplicates it to the destination."""

source = input("Please type the origin file:\n")
destination = input("Please type file Destination:\n")

with open(source) as f:
    with open(destination, "w") as f1:
        for line in f:
            f1.write(line)