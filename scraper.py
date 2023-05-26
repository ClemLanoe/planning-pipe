import requests
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv
import os

def login(session, user, pw):
    headers = {
        "Host":"www.planningpipe.co.uk",
        "Connection":"keep-alive",
        "sec-ch-ua":"'Chromium';v='112', 'Google Chrome';v='112', 'Not':'A-Brand';v='99'",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"'Windows'",
        "Upgrade-Insecure-Requests":"1",
        "Origin":"https://www.planningpipe.co.uk",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document",
        "Referer":"https://www.planningpipe.co.uk/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6",
        "sec-gpc":"1",
    }

    session = requests.Session()
    url = "https://www.planningpipe.co.uk/login-register/"

    response = session.get(url, headers=headers)

    cookies = session.cookies.get_dict()

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find_all('input', attrs={"name": "csrfmiddlewaretoken"})[1]['value']

    body = {
        "csrfmiddlewaretoken": csrf_token,
        "email_address": user,
        "password": pw,
        "login": "",
    }

    headers['Referer'] = url
    headers['Cache-Control'] = 'max-age=0'
    headers['Sec-Fetch-Site'] = 'none'

    sleep(1)

    response = session.post(url, headers=headers, data=body)

    with open("data/login_response_dump.html", 'w') as f:
        f.write(response.text) 

def get_projects(session):
    headers = {
        "Host":"www.planningpipe.co.uk ", #
        "Connection":"keep-alive", #
        "Cache-Control":"max-age=0", #
        "sec-ch-ua":"'Chromium';v='112', 'Google Chrome';v='112', 'Not':'A-Brand';v='99'", # 
        "sec-ch-ua-mobile":"?0", #
        "sec-ch-ua-platform":"'Windows'", #
        "Upgrade-Insecure-Requests":"1", #
        "Origin":"https://www.planningpipe.co.uk", 
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site":"none", #
        "Sec-Fetch-Mode":"navigate", #
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document", #
        "Referer":"https://www.planningpipe.co.uk/projects/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6",
        "sec-gpc":"1",
    }

    body = {
        "csrfmiddlewaretoken": "", # Update with correct crsf token below
        "sectors[single_dwelling]": "new_build",
        "sectors[public_and_private]": "commercial",
        "sectors[public_and_private][commercial]": "commercial_development",
        "sectors[public_and_private][commercial]": "conference_and_exhibition_facility",
        "sectors[public_and_private][commercial]": "industrial_unit",
        "sectors[public_and_private][commercial]": "mixed_use_development",
        "sectors[public_and_private][commercial]": "office",
        "sectors[public_and_private][commercial]": "storage_facility",
        "sectors[public_and_private]": "community",
        "sectors[public_and_private][community]": "community_centre",
        "sectors[public_and_private][community]": "court",
        "sectors[public_and_private][community]": "emergency_service",
        "sectors[public_and_private][community]": "place_of_worship",
        "sectors[public_and_private][community]": "prison_and_secure_care",
        "sectors[public_and_private]": "education",
        "sectors[public_and_private][education]": "childcare_facility",
        "sectors[public_and_private][education]": "further_education_estab",
        "sectors[public_and_private][education]": "primary_school",
        "sectors[public_and_private][education]": "school_other",
        "sectors[public_and_private][education]": "secondary_school",
        "sectors[public_and_private]": "health",
        "sectors[public_and_private][health]": "care_home",
        "sectors[public_and_private][health]": "healthcare_centre",
        "sectors[public_and_private][health]": "hospital",
        "sectors[public_and_private]": "residential",
        "sectors[public_and_private][residential]": "hotel",
        "sectors[public_and_private][residential]": "housing_units",
        "sectors[public_and_private]": "retail",
        "sectors[public_and_private][retail]": "petrol_retail",
        "sectors[public_and_private][retail]": "retail_units",
        "sectors[public_and_private][retail]": "supermarket",
        "sectors[public_and_private][retail]": "vehicle_and_parts_retail",
        "sectors[public_and_private]": "sport_and_leisure",
        "sectors[public_and_private][sport_and_leisure]": "arena_and_auditorium",
        "sectors[public_and_private][sport_and_leisure]": "bar/cafe/restaurant",
        "sectors[public_and_private][sport_and_leisure]": "clubhouse_and_pavilion",
        "sectors[public_and_private][sport_and_leisure]": "library/museum/gallery",
        "sectors[public_and_private][sport_and_leisure]": "park/garden/playground",
        "sectors[public_and_private][sport_and_leisure]": "sport_and_leisure_facility",
        "locations": "london",
        "locations[london]": "north_east_london",
        "locations[london]": "north_london",
        "locations[london]": "south_east_london",
        "locations[london]": "south_west_london",
        "locations[london]": "west_london",
        "stages": "detailed_plans_approved",
        "values": "over_10m",
        "values": "5_to_10m",
        "values": "1_to_5m",
        "values": "100k_to_1m",
        "values": "under_100k",
        "values": "100k_plus",
        "dates": "last_7_days",
        "textsearch": "",
        "description": "",
        "frequency": "M",
    }

    headers['Referer'] = 'https://www.planningpipe.co.uk/projects/'
    url = "https://www.planningpipe.co.uk/filters"
    response = session.get(url, headers=headers)

    with open("data/filters_dump.html", 'w') as f:
        f.write(response.text) 

    # with open('data/login_response_dump.html', "rb") as f:
    #     html_content = f.read()
    # soup = BeautifulSoup(html_content, 'html.parser')

    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', attrs={"name": "csrfmiddlewaretoken"})['value']

    headers = {
        "Host":"www.planningpipe.co.uk",
        "Connection":"keep-alive",
        "Content-Length":"6069",
        "Cache-Control":"max-age=0",
        "sec-ch-ua":"'Chromium';v='112', 'Google Chrome';v='112', 'Not':'A-Brand';v='99'",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"'Windows'",
        "Upgrade-Insecure-Requests":"1",
        "Origin":"https://www.planningpipe.co.uk",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-User":"?1",
        "Sec-Fetch-Dest":"document",
        "Referer":"https://www.planningpipe.co.uk/filters/",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6",
        "sec-gpc":"1",
    }

    body['csrfmiddlewaretoken'] = csrf_token

    sleep(1)

    url = "https://www.planningpipe.co.uk/apply-filters/"
    response = session.post(url, data=body)
    session.close()

    with open("data/approved_projects_response_dump.html", 'w') as f:
        f.write(response.text) 

load_dotenv()
user = os.environ['USER']
pw = os.environ['PW']
session = requests.Session()
login(session)
sleep(1)
get_projects(session)