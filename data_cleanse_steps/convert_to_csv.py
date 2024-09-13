import re

line_dict_template = {
    "emis_num": None,
    "level": None,
    "region": None,
    "council": None,
    "chfdom": None,
    "school-name-and-town": None,
    "phone": None,
    "owner": None
}

# Council determination logic (expects first three elements to be popped off already)
def determine_council(line_list: list[str]):

    councils = [
        "kailahun district council",
        "kenema district council",
        "kenema city council",
        "kono district council",
        "koidu-new sembehun city council",
        "bombali district council",
        "makeni city council",
        "kambia district council",
        "koinadugu district council",
        "port loko district council",
        "tonkolili district council",
        "bo district council",
        "bo city council",
        "bonthe district council",
        "bonthe municipal council",
        "moyamba district council",
        "pujehun district council",
        "western area rural district council",
        "freetown city council"
    ]

    # elements we are concerned with
    elements = []

    # Let's assume we don't encounter this for now
    if len(line_list) < 5:
        print("Line format problem!")

    # first construct 3 word combination
    r_council = f"{line_list[0]} {line_list[1]} {line_list[2]}".lower()

    if r_council in councils:
        [line_list.pop(0) for i in range(3)]
        return r_council

    r_council += " " + line_list[3].lower()

    if r_council in councils:
        [line_list.pop(0) for i in range(4)]
        return r_council

    r_council += " " + line_list[4].lower()

    if r_council in councils:
        [line_list.pop(0) for i in range(5)]
        return r_council

    return None

def convert_to_csv(data):

    # Skip first line
    data = data[1:]

    # Go ahead and write first line
    csv_data = ["emis_num,level,region,council,chfdom,school_name_and_town,phone,owner"]

    for line in data:
        line_dict = line_dict_template.copy()
        line_as_list = line.split(" ")

        # emis_num should be first on every properly formatted line
        line_dict["emis_num"] = line_as_list.pop(0)

        # As far as I can tell, all level classifications are one word
        line_dict["level"] = line_as_list.pop(0)

        # Regions are 1 word also
        line_dict["region"] = line_as_list.pop(0)

        council = determine_council(line_as_list)

        if council is None:
            print(f"Something bad happened on this line: {line.strip("\n")}")
            print(f"Current line contents: {line_as_list}")
            # Otherwise we just proceed normally knowing our council is correct

        line_dict["council"] = council

        # chfdom is next
        line_dict["chfdom"] = line_as_list.pop(0)

        # For the next section we shall jump to the end of line and proceed backwards
        line_dict["owner"] = line_as_list.pop().lower()

        # Check if a phone number is present
        # Example regex pattern to match phone numbers
        potential_number = line_as_list[-1]

        # Regex pattern to capture various phone number formats
        phone_number_pattern = r'\+?\d{2,3}[-\s]?\d{2,4}[-\s]?\d{2,4}[-\s]?/?[-\s]?\d{2,4}[-\s]?\d{0,4}'

        # Check if potential number is a match
        # Or if it is a string that has 10 digits, surely it must be a phone number
        if re.match(phone_number_pattern, potential_number) or sum(c.isdigit() for c in potential_number) >= 10:
            line_dict["phone"] = line_as_list.pop()
        else:
            # We conclude no phone number was given
            pass

        # Whats left is now the school and town
        line_dict["school-name-and-town"] = (" ".join(line_as_list))

        write_str = f"{line_dict['emis_num']},{line_dict['level']},{line_dict['region']},{line_dict['council']},{line_dict['chfdom']},{line_dict['school-name-and-town']},{line_dict['phone']},{line_dict['owner']}"

        csv_data.append(write_str)

    return csv_data