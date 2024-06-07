def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    directions = content.split('\n')
    return directions

data = read_file("input.txt")

def find_error_corrected_version(items):
    dic = {}
    maxRes = ""
    minRes = ""
    for col in range(len(items[0])):
        for row in range(len(items)):
            dic[items[row][col]] = 1 + dic.get(items[row][col], 0)
        mostCommonChar = max(dic, key=dic.get)
        leastCommonChar = min(dic, key=dic.get)
        maxRes += mostCommonChar
        minRes += leastCommonChar
        dic = {}
    return maxRes, minRes

print(find_error_corrected_version(data))