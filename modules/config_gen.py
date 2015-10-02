import json

def create_json():
    data = {

        "discord" : {
            "email" : "YOUR_EMAIL",
            "password" : "YOUR_PASS",
            "channels" : [
                ""
            ],
            "admins" : [
                ""
            ]

        },
        "twitter" : {
            "ConsumerKey" : "",
            "ConsumerSecret" : "",
            "AccessToken" : "",
            "AccessTokenSecret" : ""
        }
    }

    with open('..\conficg.json', 'w') as f:
        json.dump(data, f)