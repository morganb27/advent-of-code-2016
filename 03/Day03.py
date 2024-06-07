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

def count_valid_triangles_part_two(raw_items):
    items = []
    for line in raw_items:
        parts = line.split()
        row = [int(part) for part in parts]
        print(row)
        items.append(row)
    count = 0
    for row in range(0, len(items) - 1, 3):
        triangle_one = (items[row][0], items[row + 1][0], items[row + 2][0])
        triangle_two = (items[row][1], items[row + 1][1], items[row + 2][1])
        triangle_three = (items[row][2], items[row + 1][2], items[row + 2][2])

        if is_valid_triangle(*triangle_one):
            count+=1
        if is_valid_triangle(*triangle_two):
            count+=1
        if is_valid_triangle(*triangle_three):
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
print(count_valid_triangles_part_two(data))