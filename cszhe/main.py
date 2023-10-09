import os

import ipinfo
import pymysql
from fastapi import FastAPI, Request

app = FastAPI()

db_setting = {
    'db_host': os.getenv("DB_HOST", "localhost"),
    'db_user': os.getenv("DB_USER", ""),
    'db_password': os.getenv("DB_PASSWORD", ""),
    'db_name': os.getenv("DB_NAME", ""),
}

ipinfo_token = os.getenv("IPINFO_TOKEN", "")


@app.get("/")
def read_root(request: Request):
    print(db_setting)
    # print header
    print(request.headers)
    return {"OK"}


@app.get("/healthz")
def healthz():
    """
    Check database connection
    """
    try:
        conn = pymysql.connect(
            host=db_setting['db_host'],
            user=db_setting['db_user'],
            password=db_setting['db_password'],
            db=db_setting['db_name'],
            cursorclass=pymysql.cursors.DictCursor
        )
        conn.ping()
    except Exception as ex:
        return {"status": "ERROR", "message": str(ex)}

    return {"status": "All OK"}


@app.get("/access")
def cszhe_logger(
        page: str,
        request: Request
        ):
    """
    Log client access
    """
    print(page)
    # client_ip = request.client.host
    # behind proxy
    client_ip = request.headers['x-forwarded-for']
    user_agent = request.headers['user-agent']
    handler = ipinfo.getHandler(ipinfo_token)

    details = handler.getDetails(client_ip)
    all = details.all
    print(all)
    #
    # {'ip': '211.140.195.141', 'city': 'Shanghai', 'region': 'Shanghai',
    # 'country': 'CN', 'loc': '31.2222,121.4581',
    # 'org': 'AS56044 China Mobile communications corporation',
    # 'timezone': 'Asia/Shanghai', 'country_name': 'China',
    # 'isEU': False,
    # 'continent': {'code': 'AS', 'name': 'Asia'},
    # 'latitude': '31.2222', 'longitude': '121.4581'}
    access = {
        "IP": client_ip,
        "asOrganization": all.get('org', ''),
        "country": all.get('country', ''),
        "region": all.get('region', ''),
        "postalCode": all.get('postal', ''),
        "city": all.get('city', ''),
        "latitude": all.get('latitude', ''),
        "longitude": all.get('longitude', ''),
        "timezone": all.get('timezone', ''),
        "url": page,
        "useragent": user_agent
    }

    try:
        conn = pymysql.connect(
            host=db_setting['db_host'],
            user=db_setting['db_user'],
            password=db_setting['db_password'],
            db=db_setting['db_name'],
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            sql = '''
            INSERT INTO `Access` (IP, asOrganization, country, region,
            postalCode, city, latitude, longitude, timezone, url, useragent)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (
                access['IP'],
                access['asOrganization'],
                access['country'],
                access['region'],
                access['postalCode'],
                access['city'],
                access['latitude'],
                access['longitude'],
                access['timezone'],
                access['url'],
                access['useragent']))
        conn.commit()
        conn.close()
    except Exception as ex:
        return {"status": "ERROR", "message": str(ex)}

    return {"OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
