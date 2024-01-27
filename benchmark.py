import datetime
import json

from parser import parser


def test_my_json_parser(_data):
    parser(_data)


def test_json_parser(_data):
    json.loads(_data)


if __name__ == '__main__':
    with open("./test.json", "r", encoding='utf-8') as f:
        data = f.read()

    res = []

    start = datetime.datetime.now()
    for i in range(1000):
        test_my_json_parser(data)
    end = datetime.datetime.now()
    res.append(end - start)

    start = datetime.datetime.now()
    for i in range(1000):
        test_json_parser(data)
    end = datetime.datetime.now()
    res.append(end - start)

    print(f"my json parser: {res[0].total_seconds()}\njson parser: {res[1].total_seconds()}\nratio: {1/(res[1]/res[0])}")

