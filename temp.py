import json

from parser import parser

if __name__ == '__main__':
    with open("./test.json", "r", encoding='utf-8') as f:
        data = f.read()
        _data = json.loads(data)

        print(json.dumps(_data))
    # s = parser(data)
    # print(s)
