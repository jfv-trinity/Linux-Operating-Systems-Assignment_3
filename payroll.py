#!/usr/bin/env python3
"""
payroll.py
Joseph Volpe
301118010
reads data.txt file and outputs each line on the data.txt file using a CVS translater.
"""
import csv

with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{"Employee Number, Employee Name, Hours Worked".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}  {row[1]} {row[2]} {row[3]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
