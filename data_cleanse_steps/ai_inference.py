import os
from openai import OpenAI

def ai_inference():

    school_and_town_list = open("../inferred_data/0-raw_schools_and_towns.txt", "r", encoding="utf-8").readlines()

    # Set your OpenAI API key
    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key
    )

    completions = []

    system_message = """You are a text categorizer. Your job is to categorize text into 'school name' and 'town name' and return the response as JSON. Here are some examples of unfiltered data and their expected response:
    
    If a town name appears at the end of the school name, categorize it as the 'town name'.
    If a town name appears twice in the input, the first occurrence is part of the school name, and the second occurrence is the town name.
    If no clear town name is present, return the 'town name' as null.
    Town names are usually distinct place names, whereas school names typically contain keywords like "Primary," "Secondary," "Pre-Primary," and religious affiliations (e.g., "Catholic," "Islamic," "Methodist").
    Examples of input data and expected responses:
    
    {
        input = "roman catholic primary school sienga sienga"
        output = {"school_name": "roman catholic primary school", "town_name": "sienga"}
    }
    {
        input = "roman catholic primary school kormende"
        output = {"school_name": "roman catholic primary school", "town_name": "kormende"}
    },
    {
        input = "assembly of god primary school yengema"
        output = {"school_name": "assembly of god primary school", "town_name": "yengema"}
    },
    {
        input = "roman catholic primary school buedu buedu"
        output = {"school_name": "roman catholic primary school buedu", "town_name": "buedu"}
    },
    {
        input = "free pentecostal primary school kamakpondu"
        output = {"school_name": "free pentecostal primary school", "town_name": "kamakpondu"}
    },
    {
        input = "sierra leone muslim brotherhood primary school mano sewallu"
        output = {"school_name": "sierra leone muslim brotherhood primary school", "town_name": "mano sewallu"}
    },
    {
        input = "roman catholic primary school"
        output = {"school_name": "roman catholic primary school", "town_name": null}
    }
    
    Please return all responses in this exact JSON format. Use the rules outlined above to distinguish between the 'school name' and 'town name'."""


    with open("../inferred_data/1-raw-responses.txt", "w", encoding="utf-8") as f:

        counter = 0

        for string in school_and_town_list:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_message,
                    },
                    {
                        "role": "user",
                        "content": f"{string}",
                    }
                ],
                model="gpt-4o-mini",
                max_tokens=50
            )

            completions.append(chat_completion)

            # Monitor as we progress
            print(f"{counter}: String being identified: {string}")

            response_content = chat_completion.choices[0].message.content

            print(f"Response: {response_content}")

            f.write(f"{response_content}\n")
