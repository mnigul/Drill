file = open("drill.ngc", 'r')
path = ""
for line in file:
    if line == "":
        continue # skip random files
    elif "G81" in line:
        path = [] #empty path for coords
        split_line = line.split(" ") # split line, add result in a list
        R_coordinate = split_line[1]
        F_coordinate = split_line[2]
        X_coordinate_init = split_line[3]
        Y_coordinate_init = split_line[4]
        path.append((X_coordinate_init, Y_coordinate_init))

    elif len(path) != 0: 
        split_line = line.split(" ")
        X_coordinate = split_line[0]
        Y_coordinate = split_line[0]
        
distances[0] = int(path[0][0])**2 + int(path[0][1])**2

