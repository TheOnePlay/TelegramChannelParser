import os
import pandas
import requests

BASE_URL = 'http://127.0.0.1:8000/api'

new_apart = {
    'place_id':1,
    'title':'gkff',
    'address':'gccvcckff',
    'min_period': 10,
    'max_period': 30,
    'persons': 10,
    'photos': 'fkfkfkfk'
}

response = requests.post(f"{BASE_URL}/send-tg-posts", data=new_apart)


# Using OS library to call CLI commands in Python
# channel = input("Write channel name: ")
# count = input("Write count of posts: ")
# print("Starting parsing...")
# os.system(f"snscrape --jsonl --max-results {count} telegram-channel {channel} > telegram-@{channel}.json")
# # Reads the json generated from the CLI commands above and creates a pandas dataframe
# tweets_df = pandas.read_json(f'telegram-@{channel}.json', lines=True)
# print("Ending parsing.")
#
# # content = tweets_df["content"]
# # dates = tweets_df["date"]
# print("Starting save date to Excel...")
# tweets_df.to_csv(f'{channel}.csv',encoding='utf-8-sig')
#
# # file = open(f"{channel}.txt", "w", encoding="utf-8")
# # for el in content.to_numpy():
# #     file.write("{}\n".format(el))
# # file.close()
# print("Successful!")


