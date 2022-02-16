def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError:
        print("Couldn't find the mars.jpg file!")


if __name__ == '__main__':
    main()


""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
if __name__ == '__main__':
    main() """

""" try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!") """

""" def main():
    open("/path/to/mars.jpg")
if __name__ == '__main__':
    main() """
