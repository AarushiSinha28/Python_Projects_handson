import webbrowser as wb

def webauto():
    chrome_path = "C:/Users/aarus/AppData/Local/Google/Chrome/Application/chrome.exe %s"  #add the path of chrome here
    URLS = (
        "stackoverflow.com",
        "https://github.com/AarushiSinha28/Python_Projects_handson",
        "gmail.com",
        "google.com",
        "youtube.com"
    )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)

webauto()