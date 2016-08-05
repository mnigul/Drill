def function(file):
    lines = []
    for line in f:

        lines.append(line)
    return lines

with open("drill.ngc", "r") as f:
    content = function(f)
    print(content)

def extract(file):
    for line in f:
        if line == "X":
            coordinates.append(line_split(''))
            return coordinates