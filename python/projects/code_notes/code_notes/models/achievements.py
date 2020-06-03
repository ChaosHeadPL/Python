import requests
import logging
import json
from bs4 import BeautifulSoup
import pandas as pd
import xml.etree.ElementTree as ET


EU4_URL = "https://eu4.paradoxwikis.com"
DIFFICULT = {
    "VE": "Very Easy",
    "E": "Easy",
    "M": "Medium",
    "H": "Hard",
    "VH": "Very Hard",
    "I": "Insane",
    "UC": "Uncategorized",
}


def fetch_achievements(table):
    output = []
    for row in table.find_all("tr"):
        achievement = {
            "achievment": "",
            "description": "",
            "image": "",
            "starting_conditions": [],
            "requirements": [],
            "notes": "",
            "version": "",
            "difficult": "",
        }
        columns = []

        for column in row.find_all("td"):
            columns.append(column)

        if columns:
            achievement["achievment"] = list(columns[0].div.div)[0].text.strip()
            achievement["description"] = list(columns[0].div.div)[1].text.strip()
            achievement["image"] = f"{EU4_URL}{columns[0].find('img')['src']}"
            achievement["starting_conditions"].extend(
                [x for x in columns[1].text.strip().split("\n") if x]
            )
            achievement["requirements"].extend(
                [x for x in columns[2].text.strip().split("\n") if x]
            )
            achievement["notes"] = columns[3].text.strip()
            achievement["version"] = columns[5].text.strip()
            achievement["difficult"] = DIFFICULT[columns[6].text.strip()]

        if achievement["achievment"]:
            output.append(achievement)

    return output


def fetch_html_table(data):
    soup = BeautifulSoup(data, "html.parser")
    table = soup.find("table", attrs={"class": "mildtable sortable plainlist"})
    return table


def get_request_response(url):
    logging.info(f"Connecting to {url}")
    data = requests.get(url)
    return data.content


def build_steam_url(appid, key, steamid):
    return (
        f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements"
        f"/v0001/?appid={appid}&key={key}&steamid={steamid}"
    )


def preapare_map(xml):
    achiev_map = {}
    root = ET.fromstring(xml)
    achievements = root.find("achievements")
    for achievement in achievements:
        key = achievement.find("apiname").text
        value = achievement.find("name").text
        achiev_map[key] = value
    return achiev_map


def combine_data(steam, eu4, map_achiev):
    """
    Found errors:
        Steam:                           EU4:
        'Agressive Expander' instead of 'Aggressive Expander'
        'Blood for the Sky God!' instead of 'Blood for the Sky God'
        'Where am I?' isntead of 'Where Am I?'
        'You Get a New Home, and You Get a New Home' instead of 
            'You Get A New Home, and You Get a New Home'
        'I'll graze my horse here.. And here...' instead of 'I’ll graze my horse
             here.. And here…'
        'One Faith!' instead of 'One Faith'
    """
    test = []
    exceptions_dict = [
        ("Aggressive Expander", "Agressive Expander"),
        ("Blood for the Sky God!", "Blood for the Sky God!"),
        ("Where am I?", "Where Am I?"),
        ("Yarr Harr a Pirate's Life for Me", "Yarr Harr a Pirate's Life For Me"),
        (
            "You Get a New Home, and You Get a New Home",
            "You Get A New Home, and You Get a New Home",
        ),
        (
            "I'll graze my horse here.. And here...",
            "I’ll graze my horse here.. And here…",
        ),
        ("One Faith!", "One Faith"),
    ]

    for achievement in steam["achievements"]:
        # print(map_achiev[achievement['apiname']])
        if map_achiev[achievement["apiname"].lower()] not in test:
            test.append(map_achiev[achievement["apiname"].lower()])
    # find and replace different achievement names:
    for y, x in enumerate(eu4):
        if y == 67:
            print(x)
        if x["achievment"] not in test:
            for exception in exceptions_dict:
                if x["achievment"] == exception[0]:
                    # print(f"zmieniam {x['achievment']} na {exception[1]}")
                    eu4[y]["achievment"] = exception[1]

    # steam_df = pd.DataFrame(achievement)
    for y, x in enumerate(eu4):
        pass
        # print(f"{y}:{x}")
    # print(steam_df)
    # TODO: finish combaining data


def main():
    # get html from paradox site:
    url_target = "Achievements"
    response = get_request_response(url=f"{EU4_URL}/{url_target}")
    # fetch table from html response:
    html_table = fetch_html_table(response)
    # fetch achievements from html table
    eu4_achievements = fetch_achievements(html_table)

    steam_appid = "236850"
    steam_key = "19A08431492852D5F0735C75A0468DF1"
    steam_id = "76561198113930913"

    # get steam data:
    response = get_request_response(
        url=build_steam_url(appid=steam_appid, key=steam_key, steamid=steam_id)
    )
    steam_achievements = json.loads(response.decode("utf-8"))["playerstats"]

    # get map steam_achievement -> eu4_achievement
    map_achievements = get_request_response(
        f"https://steamcommunity.com/profiles/{steam_id}/stats/{steam_appid}/?xml=1"
    )
    map_achievements = preapare_map(map_achievements)

    combine_data(steam_achievements, eu4_achievements, map_achievements)


if __name__ == "__main__":
    main()
