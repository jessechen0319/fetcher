
import requests

class IPFetch:
    _first = [x for x in range(256)]
    _second = [x for x in range(256)]
    _third = [x for x in range(256)]
    _fourth = [x for x in range(256)]

    def generateIPAdress(self):
        for a in self._first:
            for b in self._second:
                for c in self._third:
                    for d in self._fourth:
                        yield str(a) + "." + str(a) + "." + str(c) + "." + str(d)
        return "done"

    def fetchHost(self):
        IPAdresses = self.generateIPAdress()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
        for ip in IPAdresses:
            for port in range(10000):
                host = ip + ":" + str(port)
                try:
                    r = requests.get("http://"+host + "/", headers=headers)
                    if r.status_code < 300:
                        print("works: http://"+host+"/")
                    else:
                        r = requests.get("https://"+host, headers=headers)
                        if r.status_code < 300:
                            print("works: https://" + host+"/")
                except :
                    pass



a = IPFetch()
a.fetchHost()
