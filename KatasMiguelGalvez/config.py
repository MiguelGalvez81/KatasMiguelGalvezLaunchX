def main():
    try:
        configuration = open('/config.txt')
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

if __name__ == '__main__':
    main()