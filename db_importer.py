# import database from cloudflare to mysql
import os
import pymysql
import requests

db_setting = {
    'db_host': os.getenv("DB_HOST", "localhost"),
    'db_user': os.getenv("DB_USER", ""),
    'db_password': os.getenv("DB_PASSWORD", ""),
    'db_name': os.getenv("DB_NAME", ""),
}


def main():
    # get data from https://view.hezongjian.workers.dev/
    url = "https://view.hezongjian.workers.dev/"
    resp = requests.get(url)
    data = resp.json()
    # import data to mysql
    conn = pymysql.connect(
        host=db_setting['db_host'],
        user=db_setting['db_user'],
        password=db_setting['db_password'],
        db=db_setting['db_name'],
        cursorclass=pymysql.cursors.DictCursor
    )
    with conn.cursor() as cursor:
        for item in data:
            # convert from ISO 8601 to MySQL DATETIME
            time = item['Time'].replace('T', ' ').replace('Z', '')
            sql = f"INSERT INTO `Access` \
                (`Time`, `IP`, `asOrganization`, `country`, `region`, \
                `postalCode`, `city`, `latitude`, `longitude`, `timezone`, \
                `url`, `useragent`) VALUES \
                ('{time}', '{item['IP']}', '{item['asOrganization']}', \
                '{item['country']}', '{item['region']}', \
                '{item['postalCode']}', '{item['city']}', \
                '{item['latitude']}', '{item['longitude']}', \
                '{item['timezone']}', '{item['url']}', \
                '{item['useragent']}');"
            print(sql)
            cursor.execute(sql)
        conn.commit()

if __name__ == "__main__":
    main()
