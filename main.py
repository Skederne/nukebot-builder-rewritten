try:
    import os, colorama
    from colorama import Fore, init
    init()
except ModuleNotFoundError:
    import os
    os.system("pip install -r requirements.txt")
    os.system("cls")
    import colorama
    from colorama import Fore, init
    init()




def load_tokens():
    if not os.path.exists("token.txt"):
        print("Файл token.txt не найден.")
        return []
    with open("token.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


print(Fore.MAGENTA + r'''
 _   _ _   _ _   __ ___________  _____ _____     ______ _   _ _____ _    ______ ___________ 
| \ | | | | | | / /|  ___| ___ \|  _  |_   _|    | ___ \ | | |_   _| |   |  _  \  ___| ___ \
|  \| | | | | |/ / | |__ | |_/ /| | | | | |______| |_/ / | | | | | | |   | | | | |__ | |_/ /
| . ` | | | |    \ |  __|| ___ \| | | | | |______| ___ \ | | | | | | |   | | | |  __||    / 
| |\  | |_| | |\  \| |___| |_/ /\ \_/ / | |      | |_/ / |_| |_| |_| |___| |/ /| |___| |\ \ 
\_| \_/\___/\_| \_/\____/\____/  \___/  \_/      \____/ \___/ \___/\_____/___/ \____/\_| \_|
''')

def select_token(tokens):
    print("Выберите токен:")
    for idx, token in enumerate(tokens):
        print(f"[{idx + 1}] {token[:25]}...")
    try:
        choice = int(input("Введите номер токена для запуска: "))
        return tokens[choice - 1]
    except:
        print("Неверный ввод.")
        return None

def run_bot(token):
    os.environ["DISCORD_BOT_TOKEN"] = token
    os.system("python bot_template.py")

if __name__ == "__main__":
    tokens = load_tokens()
    if not tokens:
        exit("Нет токенов.")
    selected = select_token(tokens)
    if selected:
        run_bot(selected)
