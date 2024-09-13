def extract_raw_school_and_town(data: list[str]):

    # Skip first
    data = data[1:]

    raw_schools_and_towns = []

    for line in data:
        raw_schools_and_towns.append(line.split(",")[5].lower())

    return raw_schools_and_towns