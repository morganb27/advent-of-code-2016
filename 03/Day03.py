def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    directions = content.split('\n')
    return directions

data = read_file("input.txt")

def count_valid_triangles(items):
    count = 0
    for item in items: 
      side_one, side_two, side_three = parse_input(item)
      print(side_one, side_two, side_three)
      if is_valid_triangle(side_one, side_two, side_three):
          count+=1
    return count
        
def parse_input(item):
    side_one, side_two, side_three = map(int, item.split())
    return side_one, side_two, side_three

def is_valid_triangle(x, y, z):
    if x + y <= z:
        return False
    if x + z <= y:
        return False
    if y + z <= x:
        return False
    return True    


print(count_valid_triangles(data))