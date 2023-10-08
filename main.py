import os

import pymysql
from fastapi import FastAPI

app = FastAPI()

db_setting = {
    'db_host': os.getenv("DB_HOST", "localhost"),
    'db_user': os.getenv("DB_USER", ""),
    'db_password': os.getenv("DB_PASSWORD", ""),
    'db_name': os.getenv("DB_NAME", ""),
}


@app.get("/")
def read_root():
    print(db_setting)
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
def cszhe_logger(page: str):
    """
    Log client access
    """
    return {
        "OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
