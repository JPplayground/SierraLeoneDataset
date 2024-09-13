
def replace_quotes(data):
    new_data = []

    for line in data:
        new_line = line.replace('"', "'")
        new_data.append(new_line)

    return new_data