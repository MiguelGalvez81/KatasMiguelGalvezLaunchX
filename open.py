def main():
    try:
        open("/path/to/mars.jpg")
    except:
        print("No se encontró el archivo /path/to/mars.jpg");
if __name__ == '__main__':
    main()