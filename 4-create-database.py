import sqlite3

with sqlite3.connect("database/schools.db") as connection:
    cursor = connection.cursor()

    # Table name
    table_name = "schools"

    # Column names: emis_num,level,region,council,chfdom,school_name_,town_name,phone,owner
    emis_num = "emis_num"
    level = "level"
    region = "region"
    council = "council"
    chfdom = "chfdom"
    school_name = "school_name"
    town_name = "town_name"
    phone = "phone"
    owner = "owner"

    cursor.execute(f'''
    DROP TABLE IF EXISTS {table_name}
    ''')

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            "{emis_num}" INTEGER PRIMARY KEY,
            "{level}" TEXT,
            "{region}" TEXT,
            "{council}" TEXT,
            "{chfdom}" INTEGER,
            "{school_name}" TEXT,
            "{town_name}" TEXT,
            "{phone}" TEXT,
            "{owner}" TEXT
        )
    ''')

    data = open("inferred_data/4-merged.csv", "r", encoding="utf-8").readlines()
    for line in data[1:]:

        line = line.split(",")
        emis_num = line[0]
        level = line[1]
        region = line[2]
        council = line[3]
        chfdom = line[4]

        # SOME ADDITIONAL FORMATTING
        school_name = line[5]

        if "- " in school_name:
            school_name = school_name.replace("- ", "-")

        if " -" in school_name:
            school_name = school_name.replace(" -", "-")


        town_name = line[6]
        phone = line[7]
        owner = line[8].rstrip("\n")

        cursor.execute(f'''
            INSERT INTO {table_name} VALUES
            ({emis_num}, "{level}", "{region}", "{council}", {chfdom}, "{school_name}", "{town_name}", "{phone}", "{owner}")
        ''')
