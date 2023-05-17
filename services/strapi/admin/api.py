import requests
from decouple import config

STRAPI = config("strapi")

class MicroApps:
    __endpoint = {
        "fetchOne": 'api/micro-apps/',
        "fetchAll": 'api/micro-apps'
    }
    
    def __init__(self) -> None:
        None
    
    def fetchAll(self) -> dict:
        try:
            microapps: requests.Response = requests.get(f"{STRAPI}{MicroApps.__endpoint.get('fetchAll', 'api/micro-apps')}")
            return {"status": microapps.status_codes, 'result': microapps.json()}
        except BaseException as e:
            return {"status": 'Could not Make Request to Strapi', "result": str(e)}
    
    def fetchOne(self, id: int) -> dict:
        if not id or type(id) is not int:
            return {"status": 'Invalid ID provided', 'result': 'ID must be integer'}
        try:
            microapp: requests.Response = requests.get(f"{STRAPI}{MicroApps.__endpoint.get('fetchOne', 'api/micro-apps/')}{id}")
            return {'status': microapp.status_code, 'result': microapp.json()}
        except BaseException as e:
            return {"status": 'Could not Make Request to Strapi', "result": str(e)}

if __name__ == "__main__.py":
    None

