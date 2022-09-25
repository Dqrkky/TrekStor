import requests, urllib, html_to_json, getpass

config = {
    "security": {
        "pwdchk": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "set",
                "fname": "security",
                "opt": "pwdchk",
                "name": "admin",
                "pwd1": None
            }
        },
        "curtype": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "security",
                "opt": "curtype"
            }
        },
        "dirlist": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "security",
                "opt": "dirlist",
                "user": "admin"
            }
        }
    },
    "service": {
        "smb": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "service",
                "opt": "smb"
            }
        }
    },
    "logout": {
        "url": "http://{}/index.csp",
        "params": {
            "fname": "logout"
        }
    },
    "system": {
        "devinfo": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "devinfo"
            }
        },
        "host": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "host"
            }
        },
        "time_run": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "time_run"
            }
        },
        "webdavcp": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "webdavcp"
            }
        },
        "time_zone": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "time_zone"
            }
        },
        "time_info": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "time_info"
            }
        },
        "cpu": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "cpu"
            }
        },
        "setting": {
            "reboot": {
                "url": "http://{}/protocol.csp",
                "params": {
                    "function": "get",
                    "fname": "system",
                    "opt": "setting",
                    "action": "reboot"
                }
            }
        },
        "auto_update": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "auto_update"
            }
        },
        "wizard": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "system",
                "opt": "wizard"
            }
        }
    },
    "net": {
        "wifi_phymode": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_phymode"
            }
        },
        "wifi_ap": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_ap"
            }
        },
        "wifi_lan_ip": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_lan_ip"
            }
        },
        "wifi_channel_region": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_channel_region"
            }
        },
        "wifi_dhcpd": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_dhcpd"
            }
        },
        "wifi_client": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_client"
            }
        },
        "wifi_wan": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "wifi_wan"
            }
        },
        "waninfo": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "net",
                "opt": "waninfo"
            }
        }
    },
    "storage": {
        "disk": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "storage",
                "opt": "disk"
            }
        },
        "partopt": {
            "sda": {
                "url": "http://{}/protocol.csp",
                "params": {
                    "function": "get",
                    "fname": "storage",
                    "opt": "partopt",
                    "diskname": "sda"
                }
            }
        },
        "raid": {
            "url": "http://{}/protocol.csp",
            "params": {
                "function": "get",
                "fname": "storage",
                "opt": "raid"
            }
        }
    }
}


def req(js0n: dict=None, r=None):
    if js0n != None and isinstance(js0n, dict) and len(js0n) > 0:
        if "r" in js0n and js0n["r"] != None:
            r_ = js0n["r"]
        else:
            if r != None:
                r_ = r
            else:
                r_ = None
        if "method" in js0n and js0n["method"] != None:
            method_ = js0n["method"]
        else:
            method_ = None
        if "url" in js0n and js0n["url"] != None:
            url_ = js0n["url"]
        else:
            url_ = None
        if "params" in js0n and js0n["params"] != None:
            params_ = js0n["params"]
        else:
            params_ = None
        if "data" in js0n and js0n["data"] != None:
            data_ = js0n["data"]
        else:
            data_ = None
        if "headers" in js0n and js0n["headers"] != None:
            headers_ = js0n["headers"]
        else:
            headers_ = None
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            aftermethod_ = str(js0n["aftermethod"]).lower()
        else:
            aftermethod_ = None
        if r_ != None:
            try:
                re = r_.request(
                    method=method_,
                    url=url_,
                    params=params_,
                    data=data_,
                    headers=headers_
                )
            except Exception:
                re = None
            if re != None:
                out = None
                if aftermethod_ == "text":
                    try:
                        out = re.text
                    except Exception:
                        pass
                if aftermethod_ == "json":
                    try:
                        out = re.json()
                    except Exception:
                        pass
                if aftermethod_ == "content":
                    try:
                        out = re.content
                    except Exception:
                        pass
                return out

def dtsup(params=None):
    if params != None and isinstance(params, dict) and len(params) > 0:
        return urllib.parse.urlencode(params)

def jtd(d1 :dict=None, d2 :dict=None):
    if d1 != None and isinstance(d1, dict) and len(d1) > 0 and d2 != None and isinstance(d2, dict) and len(d2) > 0:
        for i in d2:
            d1[i] = d2[i]
        return d1

ip = input("Type TreckSor's Ip : ")
password = getpass.getpass("Type TreckSor's Password : ")
with requests.session() as ses:
    config["security"]["pwdchk"]["url"] = config["security"]["pwdchk"]["url"].format(ip)
    config["security"]["pwdchk"]["params"]["pwd1"] = password
    config["service"]["smb"]["url"] = config["service"]["smb"]["url"].format(ip)
    config["logout"]["url"] = config["logout"]["url"].format(ip)
    list_data = [
        config["security"]["pwdchk"],
        config["service"]["smb"],
        config["logout"]
    ]
    for data in list_data:
        if data != None:
            data0 = req(jtd({"r": ses, "method": "get", "aftermethod": "text"}, data))
            if data0 != None:
                data1 = html_to_json.convert(data0)
                if data1 != None:
                    print(data1)