#!/usr/bin/env python3

source = input("Please type the origin file:\n")
print(f'you entered: {source}')

destination = input("Please type file Destination:\n")
print(f'you entered: {destination}')

with open(source) as f:
    with open(destination, "w") as f1:
        for line in f:
            f1.write(line)