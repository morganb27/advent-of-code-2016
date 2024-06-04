def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    directions = content.split('\n')
    return directions

data = read_file("input.txt")

def bathroom_code(items):
    result = ""
    result_part_two = ""
    current_position_part_one = [1, 1]
    current_position_part_two = '5'
    for item in items:
        result += str(decrypt_instructions(item, current_position_part_one))
        result_part_two += decrypt_instrunctions_part_two(item, current_position_part_two)
    return result, result_part_two

def decrypt_instructions(str, currentPosition):
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for char in str:
        if char == 'U' and currentPosition[0] > 0:
            currentPosition[0]-=1
        elif char == 'D' and currentPosition[0] < 2:
            currentPosition[0]+=1
        elif char == "L" and currentPosition[1] > 0:
            currentPosition[1]-=1
        elif char == 'R' and currentPosition[1] < 2:
            currentPosition[1]+=1
    return keypad[currentPosition[0]][currentPosition[1]]

def decrypt_instrunctions_part_two(str, currentPosition):
    keypad = {
        '1': { 'U': '1', 'D': '3', 'L': '1', 'R': '1'},
        '2': { 'U': '2', 'D': '6', 'L': '2', 'R': '3'},
        '3': { 'U': '1', 'D': '7', 'L': '2', 'R': '4'},
        '4': { 'U': '4', 'D': '8', 'L': '3', 'R': '4'},
        '5': { 'U': '5', 'D': '5', 'L': '5', 'R': '6'},
        '6': { 'U': '2', 'D': 'A', 'L': '5', 'R': '7'},
        '7': { 'U': '3', 'D': 'B', 'L': '6', 'R': '8'},
        '8': { 'U': '4', 'D': 'C', 'L': '7', 'R': '9'},
        '9': { 'U': '9', 'D': '9', 'L': '8', 'R': '9'},
        'A': { 'U': '6', 'D': 'A', 'L': 'A', 'R': 'B'},
        'B': { 'U': '7', 'D': 'D', 'L': 'A', 'R': 'C'},
        'C': { 'U': '8', 'D': 'C', 'L': 'B', 'R': 'C'},
        'D': { 'U': 'B', 'D': 'D', 'L': 'D', 'R': 'D'},
    }
    for char in str:
        currentPosition = keypad[currentPosition][char]
    return currentPosition

print(bathroom_code(data))