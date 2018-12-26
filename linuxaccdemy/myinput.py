#!/usr/bin/env python3.7

def get_input(reprompt = False):
    if reprompt:
        print("Please enter a file name.")
    file_name = input("Destination file name: ").strip()
    return file_name or get_input(True)

file_name = get_input()

print(f"Please enter your content, entering am emputy line will write all the content to the file {file_name}\n")

with open(file_name,'w') as f:
    eof = False
    lines = []
    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True
    f.writelines(lines)
    print(f"Write line to file {file_name}")
