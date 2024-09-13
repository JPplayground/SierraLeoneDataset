
def remove_extra_spaces(data):

    with_spaces_removed = []

    for i in range(len(data)):
        line = data[i]
        line_list = line.split(" ")
        line_with_removed_spaces = [s for s in line_list if s]
        line = " ".join(line_with_removed_spaces)
        with_spaces_removed.append(line)

    return with_spaces_removed