import requests
import hashlib
import json
import time
import os


class SwitchClient(object):
    base_url = 'https://{}.switchapi.com/{}'

    def __init__(self, api_key, api_secret, server=None,
                 access_token=None):
        if server is None:
            self.server = 'tr02'
            # print 'Server name is not provided, using "'"tr02"'" as default'
        else:
            self.server = server
        self.credentials_file = 'sw_db_credentials.json'
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        if access_token is None:
            try:
                os.remove(self.credentials_file)
            except OSError:
                pass
            try:
                with open(self.credentials_file) as data_file:
                    data = json.load(data_file)
                    if long(data["time_stamp"]) - 86400 <= long((time.time() + 0.5) * 1000):
                        access_token = self.get_access_token(self.api_secret, self.api_key, self.server)["access_token"]
                        data["access_token"] = access_token
                        data["time_stamp"] = _default_expire_time(30)  # default 30 days expire period
                        data_file.seek(0)
                        json.dump(data, data_file)
                        data_file.truncate()
                    self.access_token = data["access_token"]
            except IOError:
                val = self.get_access_token(self.api_secret, self.api_key, self.server)
                access_token = val["access_token"]
                expire_time = val["expire_time"]
                self.access_token = access_token
                self.credentials_save(access_token, expire_time)

    def lists(self):
        headers = {
            "APIKey": self.api_key,
            "AccessToken": self.access_token,
            "Content-type": "application/json"
        }
        try:
            data = requests.get(self.base_url.format(self.server, "Lists"), headers=headers)
            return json.loads(data.text)
        except Exception as e:
            print e

    def list(self, list_name, query):
        headers = {
            "APIKey": self.api_key,
            "AccessToken": self.access_token,
            "List": list_name,
            "Content-type": "application/json"
        }
        try:
            if 'list' not in query.keys():
                query['list'] = list_name
            data = requests.post(self.base_url.format(self.server, "List"), headers=headers,
                                 json=query)
            return json.loads(data.text)
        except Exception as e:
            print e

    def add(self, list_name, json_data):
        headers = {
            "APIKey": self.api_key,
            "AccessToken": self.access_token,
            "List": list_name,

        }
        try:
            data = requests.post(self.base_url.format(self.server, "Add"), headers=headers,
                                 json=json_data)
            return json.loads(data.text)
        except Exception as e:
            print e

    def update(self, list_name, list_item_id, json_data):
        headers = {
            "APIKey": self.api_key,
            "AccessToken": self.access_token,
            "List": list_name,
            "ListItemId": list_item_id,
            "Content-type": "application/json"
        }
        try:
            data = requests.post(self.base_url.format(self.server, "Set"), headers=headers,
                                 json=json_data)
            return json.loads(data.text)
        except Exception as e:
            print e

    def delete(self, list_name, list_item_id):
        headers = {
            "APIKey": self.api_key,
            "AccessToken": self.access_token,
            "List": list_name,
            "ListItemId": list_item_id,
            "Content-type": "application/json"
        }
        try:
            data = requests.delete(self.base_url.format(self.server, "Set"), headers=headers)
            return json.loads(data.text)
        except Exception as e:
            print e

    def credentials_save(self, access_token, time_stamp):
        try:
            f = open(self.credentials_file, 'w')
            f.write(json.dumps({'access_token': "{}".format(access_token), 'time_stamp': "{}".format(time_stamp)},
                               ensure_ascii=False))
            f.close()
        except Exception as e:
            print e
            return False
        return True

    def get_access_token(self, api_secret, api_key, server):
        expire_time = _default_expire_time(30)  # default 30 days expire period
        m = hashlib.md5(api_secret + expire_time)
        headers = {
            "APIKey": api_key,
            "Signature": m.hexdigest(),
            "Expire": expire_time
        }
        r = requests.get("https://{}.switchapi.com/Token".format(server), headers=headers)
        try:
            access_token = json.loads(r.text)["AccessToken"]
            return {"access_token": access_token, "expire_time": expire_time}
        except Exception as e:
            print e


# default n days expire period(unix timestamp)
def _default_expire_time(int_day):
    return str(long((time.time() + 0.5) * 1000) + (int_day * 86400))
