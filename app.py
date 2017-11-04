#coding:utf-8
from pyowm import OWM
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

API_KEY = 'e4e96bc8ffc8af544c30f6c787eaa804'
owm = OWM(API_KEY)
obs = owm.weather_at_place('Seoul')
w = obs.get_weather()

result = str(w.get_temperature(unit='celsius')['temp'])

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["현재 날씨를 보여줘", "결과에 만족하시나요"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    try:
        print(request.get_json())
        dataReceive = request.get_json()
        print(dataReceive)
        content = dataReceive['content']
        if content == u"현재 날씨를 보여줘":
            dataSend = {
                "message": {
                    "text": "현재 온도는 : " + result + "도 입니다"
                },
                "keyboard": {
                    "type": "buttons",
                    "buttons": ["현재 날씨를 보여줘", "결과에 만족하시나요"]
                }
            }
        elif content == u"결과에 만족하시나요":
            dataSend = {
                "keyboard": {
                    "type": "buttons",
                    "buttons": ["예보에 비해 더웠다", "예보가 적절했다", "예보에 비해 추웠다"]
                }
            }

        elif content == u"예보에 비해 더웠다":
            dataSend = {
                "message": {
                    "text": "귀하의 더웠다는 의견 감사합니다."
                },
                "keyboard": {
                    "type": "buttons",
                    "buttons": ["현재 날씨를 보여줘", "결과에 만족하시나요"]
                }
            }

        elif content == u"예보가 적절했다":
            dataSend = {
                "message": {
                    "text": "귀하의 적절했다는 의견 감사합니다."
                },
                "keyboard": {
                    "type": "buttons",
                    "buttons": ["현재 날씨를 보여줘", "결과에 만족하시나요"]
                }
            }
        elif content == u"예보에 비해 추웠다":
            dataSend = {
                "message": {
                    "text": "귀하의 추웠다는 의견 감사합니다."
                },
                "keyboard": {
                    "type": "buttons",
                    "buttons": ["현재 날씨를 보여줘", "결과에 만족하시나요"]
                }
            }
        return jsonify(dataSend)
    except Exception as e:
        print(e)
        return ""

if __name__ == '__main__':
    app.run()