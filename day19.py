url ="https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts/?limit=8"



import requests


# r = requests.get(url=url)
# if r.status_code ==200:
#     result = r.json()
#     print(type(result))
#     print(result.keys())
#     final_result = result['data']['news']
#     for i in final_result:
#         print(i['title'], )


# url ="https://www.onlinekhabar.com/smtm/home/ipo-corner-filed"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()['response']
#     for i in data:
#         print(f"{i['company_name']} - {i['application_date']}")

# pip install requests

# import requests


url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/players/466052"


r = requests.get(url=url)
if r.status_code == 200:
    
    print(r.json()[0].keys())