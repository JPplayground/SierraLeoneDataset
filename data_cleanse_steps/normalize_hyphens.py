def normalize_hyphens_and_remove_commas(data):
    new_data = []

    for line in data:
        new_line = line.replace("‐", "-")
        new_line = new_line.replace(",", "")
        new_data.append(new_line)

    return new_data