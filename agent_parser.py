from user_agents import parse


def main():
    agent_str = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    ua = parse(agent_str)
    print(ua)


if __name__ == "__main__":
    main()
