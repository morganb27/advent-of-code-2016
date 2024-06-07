def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    directions = content.split('\n')
    return directions

data = read_file("input.txt")

def decode_instructions(items):
    result = 0
    for item in items:
        potential_checksum = ""
        count = 0
        dict = {}
        letters, sector_id, checksum = parseInput(item)
        for char in letters:
            if char != '-':
                dict[char] = 1 + dict.get(char, 0)
        sorted_dict = sort_dict(dict)
        for key, _ in sorted_dict.items():
            potential_checksum += key
            count+=1
        if potential_checksum[:5] == checksum:
            result += int(sector_id)
    return result
    

def parseInput(item):
    parts = item.split('[')
    checksum = parts[1].strip(']')
    sector_id = parts[0].rsplit('-', 1)[1]
    letters = parts[0].rsplit('-', 1)[0]
    return letters, sector_id, checksum

def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))


print(decode_instructions(data))