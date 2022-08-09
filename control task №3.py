with open('file.txt') as f:
    var = f.read().split()
    words = len(var)

print(f"Input file contains:\n{var} letters\n{words} ")