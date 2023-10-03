#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        text = response.read()
        print("Body response:")
        print("\t- type:", type(text))
        print("\t- content:", text)
        print("\t- utf8 content:", text.decode())
