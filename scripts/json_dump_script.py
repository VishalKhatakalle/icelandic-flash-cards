import json
import pandas as pd

data = pd.read_csv("../data/is_data.csv")
df = pd.DataFrame(data)
new_dict = {}
word_list = [word for word in data.words if word.strip()]
translation_list = [word for word in data.translation if word.strip()]
count_list = [count for count in data.nos]

for index in range(4999):
    new_dict = {
        index: {
            "word": word_list[index],
            "trans": translation_list[index],
            "nos": count_list[index],
            "sound": f"is_audio/{word_list[index]}.mp3"
        }
    }
    try:
        with open("../is_data.json", 'r') as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        with open("../is_data.json", 'w') as data_file:
            json.dump(new_dict, data_file, indent=4)
    else:
        # Updating old data with new data
        data.update(new_dict)

        with open("../is_data.json", 'w') as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)
