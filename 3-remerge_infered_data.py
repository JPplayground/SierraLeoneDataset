import json

original_lines = open("cleanse_data/5-converted_to_csv.txt", "r", encoding="utf-8").readlines()

inferred_json_data = open("./inferred_data/3-converted-to-json.json", "r").read()
inferred_schools_and_towns = json.loads(inferred_json_data)

with open("inferred_data/4-merged.csv", "w", encoding="utf-8") as f:
    f.write("emis_num,level,region,council,chfdom,school_name,town_name,phone,owner\n")

    for idx, line in enumerate(original_lines[1:]):

        line = line.split(",")

        emis_num = line[0]
        level = line[1]
        region = line[2]
        council = line[3]
        chfdom = line[4]

        # REPLACING SCHOOL AND TOWN HERE
        school_name = inferred_schools_and_towns[idx]["school_name"]



        town_name = inferred_schools_and_towns[idx]["town_name"]

        if school_name is None:
            school_name = "null"
        else:
            school_name = school_name.title()

        if town_name is None:
            town_name = "null"
        else:
            town_name = town_name.title()

        phone = line[6]
        owner = line[7]

        new_line = [
            emis_num, level, region, council, chfdom, school_name, town_name, phone, owner
        ]

        new_line_as_string = ",".join(new_line)

        f.write(f"{new_line_as_string}")

