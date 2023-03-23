import os
import pandas

# Using OS library to call CLI commands in Python
channel = input("Write channel name: ")
count = input("Write count of posts: ")
print("Starting parsing...")
os.system(f"snscrape --jsonl --max-results {count} telegram-channel {channel} > telegram-@{channel}.json")
# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pandas.read_json(f'telegram-@{channel}.json', lines=True)
print("Ending parsing.")

# content = tweets_df["content"]
# dates = tweets_df["date"]
print("Starting save date to Excel...")
tweets_df.to_csv(f'{channel}.csv',encoding='utf-8-sig')

# file = open(f"{channel}.txt", "w", encoding="utf-8")
# for el in content.to_numpy():
#     file.write("{}\n".format(el))
# file.close()
print("Successful!")

