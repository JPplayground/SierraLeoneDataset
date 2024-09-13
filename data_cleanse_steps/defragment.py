def defragment(data):

    # ONE EDGE CASE HERE -
    # 420501105 Preschool West Freetown City Council 5 PROGRESSIVE PREPARATORY SCHOOL 56 C MISSION
    # ROAD CALAB TOWN FREE TOWN 76558803 Private
    # 420501107 Preschool West Freetown City Council 5 UNITED METHODIST CHURCH PRE PRIMARY SCHOOL KOROMA STREET CALABA TOWN MAYENKENEHE. 76713168 Mission

    # The last element in each line should match one of these
    owners = ["government", "mission", "community", "private", "other"]

    for i in range(len(data)):
        data[i] = data[i].rstrip("\n")

    defragmented_data = []

    skipper = 0
    for idx, line in enumerate(data):

        # Used to track fragmentation index as to not repeat already reconstructed lines
        if skipper != 0:
            skipper -= 1
            continue

        # Skip first line
        if idx == 0:
            defragmented_data.append(line)
            continue

        # Handle the one edge case present (info at top of function)
        if idx == 8372:
            correct_line = f"{line} {data[8373]} {data[8374]} {data[8375]} {data[8376]} {data[8377]}"
            defragmented_data.append(correct_line)
            skipper = 5
            continue

        line_list = line.split(" ")

        if line_list[-1].lower() in owners:
            defragmented_data.append(line)

        else:

            # Start jumping lines to try and find where the actual ending is
            # Finding the actual ending relies on a line ending with an owner
            relative_idx = 0
            while True:

                # Progress one line
                relative_idx += 1
                secondary_idx = idx + relative_idx

                last_element_in_curr_line = data[secondary_idx].split(" ")[-1].strip("\n").lower()

                if last_element_in_curr_line in owners:
                    # Correct line found! Reassemble
                    new_line_constructor_list = []

                    # Set skipper so we can avoid these lines on next iteration
                    skipper = secondary_idx - idx

                    # Store the out-of-place lines
                    while secondary_idx != idx:
                        new_line_constructor_list.insert(0, data[secondary_idx])
                        secondary_idx -= 1

                    # Combine with original line
                    new_line_constructor_list.insert(0, data[idx])
                    reconstructed_line = " ".join(new_line_constructor_list)
                    defragmented_data.append(reconstructed_line)
                    break

    return defragmented_data