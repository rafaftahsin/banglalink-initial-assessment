from flask import Flask
from flask import request
import sys
import datetime

app = Flask(__name__)


@app.route('/', methods=['POST'])
def dif():
    data = request.get_data().decode('utf-8').split('\n')
    output = []

    T = int(data[0])

    for t in range(T):
        # Ref: https://www.programiz.com/python-programming/datetime/strptime
        t1 = datetime.datetime.strptime(data[t*2 + 1], '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.datetime.strptime(data[t*2 + 2], '%a %d %b %Y %H:%M:%S %z')
        # Ref: https://stackoverflow.com/a/43308104/4814427
        dt = int((t1 - t2).total_seconds())
        output.append(str(dt))
    return str(output)


if __name__ == '__main__':
    app.run()
