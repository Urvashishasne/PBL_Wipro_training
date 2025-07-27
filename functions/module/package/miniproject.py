#sort colors
def sort_colors(color_sequence):
    colors = color_sequence.split("-")
    colors.sort()
    return "-".join(colors)

color_input = input()
print(sort_colors(color_input))
