# This script is intended to reassemble fragmented rows in the dataset
from data_cleanse_steps.defragment import defragment
from data_cleanse_steps.extract_raw_school_and_town import extract_raw_school_and_town
from data_cleanse_steps.remove_extra_spaces import remove_extra_spaces
from data_cleanse_steps.replace_quotes import replace_quotes
from data_cleanse_steps.convert_to_csv import convert_to_csv
from data_cleanse_steps.normalize_hyphens import normalize_hyphens_and_remove_commas

data = open("cleanse_data/0-raw.txt", "r", encoding="utf-8").readlines()

data = defragment(data)

with open("cleanse_data/1-defragmented.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

data = remove_extra_spaces(data)

with open("cleanse_data/2-spaces_removed.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

data = replace_quotes(data)

with open("cleanse_data/3-quotes_replaced.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

data = normalize_hyphens_and_remove_commas(data)

with open("cleanse_data/4-hyphens-normalized.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

data = convert_to_csv(data)

with open("cleanse_data/5-converted_to_csv.txt", "w", encoding="utf-8") as f:
    for line in data:
        f.write(line + "\n")

raw_schools_and_towns = extract_raw_school_and_town(data)

with open("inferred_data/0-raw_schools_and_towns.txt", "w", encoding="utf-8") as f:
    for line in raw_schools_and_towns:
        f.write(line + "\n")
