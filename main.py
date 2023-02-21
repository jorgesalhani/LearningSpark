from src.first_test import FirstTest

def app():
    res = FirstTest.read_csv()
    print(res)
    return

if __name__ == '__main__':
    app()