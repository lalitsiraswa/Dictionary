import json
import difflib

file = json.load(open("D:\\PythonProjects\\Dictionary\\data.json"))

# print(file.keys())

result_list = difflib.get_close_matches("Applee", file.keys())

print(result_list[0])

print(file[result_list[0]])

#-----------------------------------------------------

# import difflib
# import json

# file = json.load(open("D:\\PythonProjects\\Dictionary\\data.json"))

# result_list = difflib.get_close_matches("applee", file, cutoff=0.9)

# print(result_list)

# length = len(result_list)

# for i in range(length):
#     for line in file[result_list[i]]:
#         print(line)


