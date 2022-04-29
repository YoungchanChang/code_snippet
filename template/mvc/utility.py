import json
import requests


class SlackAlarm:
    _token = "<input your token>"
    _url = f"https://hooks.slack.com/services/{_token}"
    _header = { "Content-Type": "application/json; charset=utf-8" }
    _http_ok = 200

    @staticmethod
    def send_slack_alarm(title, message):
        slack_data = {
            "attachments": [
                {
                    "color": "#D00000",
                    "fields": [
                        {
                            "title": title,
                            "value": message,
                            "short": False
                        }
                    ]
                }
            ]
        }
        try:
            res = requests.post(SlackAlarm._url, data=json.dumps(slack_data), headers=SlackAlarm._header, verify=False, timeout=5)

            if res.status_code != SlackAlarm._http_ok:
                res.raise_for_status()
        except Exception as e:
            print(f"예외 발생: {e}")
            raise