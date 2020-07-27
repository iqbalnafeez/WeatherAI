import sys, json

file_open = open("bajson.txt", "r")
splitter = file_open.read().split("\n")[:-1]
array = []
matrix = []
count = 0
print(len(splitter))
for i in splitter:
    json_conv = json.loads(i.replace("'", '"'))
    if count < 20:
        array.append(json_conv["current"]["wind_dir"])
    else:
        array = []
        count = 0
        matrix.append(array)
    count = count + 1

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))