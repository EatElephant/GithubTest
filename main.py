import introduce

def main():
    print("Hello!")
    introduce.introduce()
    name = introduce.ask_name()
    print("Nice to meet you, {}!".format(name))

if __name__ == "__main__":
    main()
