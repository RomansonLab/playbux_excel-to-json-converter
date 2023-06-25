import pandas as pd
import json

df = pd.read_excel('account_info.xlsx')

def make_dict(d: dict) -> dict:
    data_dict = {
        "email": d["EMAIL"],
        "password": d["PASS"],
        "private_key": d["PRIVATE"],
        "proxy": d["PROXY"]
    }
    return data_dict

data_list = []
with open('a.json', 'r+') as f: # заменить 'a.json' на ваш файл
    json_data = json.load(f)
    for i in range(len(df)):
        row_dict = df.iloc[i].to_dict()
        data_list.append(make_dict(row_dict))

with open('a.json', 'w') as f: # заменить 'a.json' на ваш файл
    json.dump(data_list, f, indent=2)
