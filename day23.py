mport json

import requests

api_key = "55e1edf1a6f1ee63-fdcf599f8afa85a3-402747bfb52de1cf"
user_id = "KF6YtUCcWxwkJ2z7m9WOtg=="


viber_data={
    "auth_token":api_key,
    "from":user_id,
    "type":"text",
    "text":"message url"
}


viber_data['text']=1

viber_url = "https://chatapi.viber.com/pa/post"
url ="https://www.thesportsdb.com/api/v1/json/123/all_leagues.php"

r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()
    final = data['leagues']
    for i in final:
        result = f"{i['strLeague']} - {i['strSport']}"
        viber_data['text']=result
        r = requests.post(url=viber_url, data=json.dumps(viber_data))
        if r.status_code == 200:
            print(r.json())