import os


def print_hello_world(imie):
    print("Hello World! {0}".format(imie))

def main():
    uzytkownik = os.environ.get("USER")
    print_hello_world(uzytkownik)

if __name__== "__main__":
    main()
