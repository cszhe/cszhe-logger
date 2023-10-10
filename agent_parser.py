import os
import pymysql
from user_agents import parse


db_setting = {
    'db_host': os.getenv("DB_HOST", "localhost"),
    'db_user': os.getenv("DB_USER", ""),
    'db_password': os.getenv("DB_PASSWORD", ""),
    'db_name': os.getenv("DB_NAME", ""),
}


def main():
    # connect to the database
    conn = pymysql.connect(
        host=db_setting['db_host'],
        user=db_setting['db_user'],
        password=db_setting['db_password'],
        db=db_setting['db_name'],
        cursorclass=pymysql.cursors.DictCursor
    )
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `Access`;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            agent_str = item['useragent']
            ua = parse(agent_str)
            sql = f"INSERT INTO `UserAgent` \
                (`AccessID`, `AgentString`, \
                `Browser_Family`, `Browser_Version`, \
                `OS_Family`, `OS_Version`, \
                `Device_Family`, `Device_Brand`, \
                `IsMobile`, `IsTablet`, \
                `IsPC`, `IsTouchCapable`, `IsBot`) VALUES \
                ('{item['AccessCount']}', '{agent_str}', \
                '{ua.browser.family}', '{ua.browser.version_string}', \
                '{ua.os.family}', '{ua.os.version_string}', \
                '{ua.device.family}', '{ua.device.brand}', \
                '{1 if ua.is_mobile else 0}', '{1 if ua.is_tablet else 0}', \
                '{1 if ua.is_pc else 0}', \
                '{1 if ua.is_touch_capable else 0}', \
                '{1 if ua.is_bot else 0}');"
            cursor.execute(sql)
        conn.commit()
    # close the connection
    conn.close()
    print("Done.")

if __name__ == "__main__":
    main()
