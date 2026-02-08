import requests

foundURLs = []

def request(url):
    try:
        r = requests.get(url, timeout=2)
        if r.status_code < 400:
            return r
    except requests.exceptions.RequestException:
        pass
    return None

def findDirectories(base_url):
    try:
        with open("directorylist.txt", "r") as listfile:
            for line in listfile:
                word = line.strip()
                testUrl = base_url + "/" + word
                response = request(testUrl)

                if response:
                    print("Bulundu URL --> " + testUrl)
                    foundURLs.append(word)

    except KeyboardInterrupt:
        print("\nTarama durduruldu.")
        exit()

url = input("URL örnek ('https://google.com'): ").rstrip("/")

findDirectories(url)

for found in foundURLs:
    findDirectories(url + "/" + found)
