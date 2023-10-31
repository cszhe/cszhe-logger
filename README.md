# cszhe-logger
This application is used to log website access from [My Blog](https://www.hezongjian.com)

## How it works

It is a simple web application based Python3 FastAPI framework. It will log the access information to a MariaDB database.

No ORM is used in this application. It is a simple SQL statement to insert the access information to the database.

There are two tables in the database. One is for the access information, the other is for the Browsers' user agent information.

The application uses [IPInfo](https://ipinfo.io/) API to get the location information and other details of the IP address. A cache has been implemented to reduce the API calls.

## How to run

It is a dockerized application. But you need to offer the following environment variables to the container.

MariaDB connection parameters:

- DB_HOST
- DB_USER
- DB_PASSWORD
- DB_NAME

IPInfo API token:

- IPINFO_TOKEN

The user agent parser `agent_parser.py` is a separate programme from the web service. It is a Python3 script. You need to run it separately. The script will read the raw user agent string from the database and parse the user agent information with the [user_agents](https://pypi.org/project/user-agents/) library. Then it will update the database with the parsed information. It's recommended to run it in a crontab.

