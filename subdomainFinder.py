import requests

def request(url):
    for proto in ["https://", "http://"]:
        try:
            r = requests.head(proto + url, timeout=2, allow_redirects=True)
            if r.status_code < 400:
                return r
        except requests.exceptions.RequestException:
            pass
    return None

targetUrl = input("Hedef Url (ör: google.com): ")

try:
    with open("subdomainlist.txt", "r") as listfile:
        for line in listfile:
            word = line.strip()
            testUrl = word + "." + targetUrl
            sonuc = request(testUrl)

            if sonuc:
                print("Subdomain Bulundu --> " + testUrl)

except KeyboardInterrupt:
    print("\nTarama durduruldu.")
