import requests, urllib, html_to_json, getpass
config = {
    "security": {
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


import requests
import shared

class TrekStor:
    def __init__(self, ip :str=None):
        self.config = {
            "getaway": f'http://{ip}' if ip != None and isinstance(ip, str) else None
        }
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
    def login(self, name :str="admin", password :str=None):
        if hasattr(self, config) and self.config != None and isinstance(self.config, dict) and "getaway" in self.config and self.config["getaway"] != None and name != None and isinstance(name, str) and password != None and isinstance(password, str):
            config = {
                "url": f'http://{self.config["getaway"]}/protocol.csp',
                "params": {
                    "function": "set",
                    "fname": "security",
                    "opt": "pwdchk",
                    "name": name,
                    "pwd1": password
                }
            }
            return self.rss.request(
                *self.shared.convert_json_to_values(
                    config=config
                )
            )