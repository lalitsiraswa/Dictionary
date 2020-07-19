import json
# import difflib
from difflib import get_close_matches

def myDictionary(keyword):
    # result_list = get_close_matches(keyword, data.keys())
    if keyword in data:
        return(data[keyword])
    elif keyword.lower() in data:
        return(data[keyword.lower()])
    elif keyword.title() in data:
        return(data[keyword.title()])       
    elif keyword.capitalize() in data:
        return(data[keyword.capitalize()])           
    elif keyword.upper() in data:
        return(data[keyword.upper()])
    elif(len(get_close_matches(keyword, data.keys())) > 0):
        print("did you mean %s instead" %(get_close_matches(keyword, data.keys())[0]))
        decide = input("Enter 'y' for 'yes' or 'n' for 'no' : ")
        if(decide == "y"):
            return data[get_close_matches(keyword, data.keys())[0]]
        elif(decide == "n"):
            return "You have entered wrong word, Please check it again!"
        else:
            return "You entered wrong word! Please enter just 'y' or 'n'"
    else:
        return("You have entered wrong word, Please check it again!")

if __name__ == "__main__":
    data = json.load(open("D:\\PythonProjects\\Dictionary\\data.json"))

    keyword = input("Enter the word you wan't to search : ")

    while(keyword != "exit"):
        meaning = myDictionary(keyword)
        if type(meaning) == list:
            for item in meaning:
                print(item)
        else:
            print(meaning)
        keyword = input("Enter the word you wan't to search : ")

#----------------------------------------------------------------------------------------

# data = json.load(open("D:\\PythonProjects\\Dictionary\\data.json"))

# keyword = input("Enter the word you wan't to search : ")

# while(keyword != "exit"):
#     if keyword in data:
#         # print(data[keyword])
#         for x in data[keyword]:
#             print(x)
#     elif keyword.lower() in data:
#         # print(data[keyword.lower()])
#         for x in data[keyword.lower()]:
#             print(x)
#     elif keyword.title() in data:
#         # print(data[keyword.title()])
#         for x in data[keyword.title()]:
#             print(x)        
#     elif keyword.capitalize() in data:
#         # print(data[keyword.capitalize()])
#         for x in data[keyword]:
#             print(x)               
#     elif keyword.upper() in data:
#         # print(data[keyword.upper()])
#         for x in data[keyword.upper()]:
#             print(x)
#     else:
#         print("You have entered wrong word, Please check it again!")
#     keyword = input("Enter the word you wan't to search : ")

#----------------------------------------------------------------------------------------------

# data = json.load(open("D:\\PythonProjects\\Dictionary\\data.json"))

# print(data["abandoned industrial site"])



# file = open("D:\\PythonProjects\\Dictionary\\data.json")

# content = file.read()

# print("abandoned industrial site" in content)

# x = dict(content)

# print(x)Python JSON