#coding:utf-8

from flask import Flask
from flask import jsonify, request

from pyowm import OWM

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["현재 날씨를 보여줘", "예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다."]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_ison()
    content = dataReceive['content']
    if content == u"현재 날씨를 보여줘":
        API_KEY = 'e4e96bc8ffc8af544c30f6c787eaa804'
        owm = OWM(API_KEY)
        obs = owm.weather_at_place('Seoul')
        w = obs.get_weather()
        dataSend = {
            "message": {
                "text": "현재 온도는 : " + w.get_temperature(unit='celsius')['temp'] + "입니다"
            },
            "keyboard": {
                "type": "buttons",
                "buttons" : ["현재 날씨를 보여줘", "예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다."]
            }
        }
    elif content == u"예보에 비해 더웠다":
        dataSend = {
            "message": {
                "text": "귀하의 의견 감사합니다.1"
            },
            "keyboard": {
            "type": "buttons",
            "buttons" : ["현재 날씨를 보여줘", "예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다."]
            }
        }

    elif content == u"예보가 적절하다":
        dataSend = {
            "message": {
                "text": "귀하의 의견 감사합니다.2"
            },
            "keyboard": {
                "type": "buttons",
                "buttons" : ["현재 날씨를 보여줘", "예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다."]
            }
        }
    elif content == u"예보에 비해 추웠다":
        dataSend = {
            "message": {
                "text": "귀하의 의견 감사합니다.3"
            },
            "keyboard": {
                "type": "buttons",
                "buttons" : ["현재 날씨를 보여줘", "예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다."]
            }
        }
    return jsonify(dataSend)

if __name__ == '__main__':
    app.run()