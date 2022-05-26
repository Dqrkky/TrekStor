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

def req(js0n=None, r_=None):
    if js0n != None and isinstance(js0n, dict) and len(js0n) > 0:
        if "r" in js0n and js0n["r"] != None:
            r = js0n["r"]
        else:
            if r_ != None:
                r = r_
            else:
                r = None
        if "method" in js0n and js0n["method"] != None:
            method = js0n["method"]
        else:
            method = None
        if "url" in js0n and js0n["url"] != None:
            url = js0n["url"]
        else:
            url = None
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            aftermethod = js0n["aftermethod"]
        else:
            aftermethod = None
        if r != None and method != None and url != None and aftermethod != None:
            try:
                re = r.request(method=method, url=url)
            except Exception:
                re = None
            if re != None:
                aftermethod = str(aftermethod).lower()
                out = None
                if aftermethod == "text":
                    try:
                        out = re.text
                    except Exception:
                        pass
                if aftermethod == "json":
                    try:
                        out = re.json()
                    except Exception:
                        pass
                if aftermethod == "content":
                    try:
                        out = re.content
                    except Exception:
                        pass
                return out

def dtsup(params=None):
    if params != None and isinstance(params, dict) and len(params) > 0:
        return urllib.parse.urlencode(params)

#method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json
ip = input("Type TreckSor's Ip : ")
password = getpass.getpass("Type TreckSor's Password : ")
with requests.session() as ses:
    login_data = config["security"]["pwdchk"]
    login_data["params"]["pwd1"] = password
    storage_data = config["storage"]["disk"]
    logout_data = config["logout"]
    list_data = [
        f'{login_data["url"].format(ip)}?{dtsup(login_data["params"])}',
        f'{storage_data["url"].format(ip)}?{dtsup(storage_data["params"])}',
        f'{logout_data["url"].format(ip)}?{dtsup(logout_data["params"])}'
    ]
    for url in list_data:
        if url != None:
            data_0 = req({"r": ses, "method": "get", "url": url, "aftermethod": "text"})
            if data_0 != None:
                data_1 = html_to_json.convert(data_0)
                if data_1 != None:
                    print(data_1)