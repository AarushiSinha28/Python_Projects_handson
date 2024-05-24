import webbrowser as wb

def webauto():
    chrome_path = "C:\Windows\WinSxS\x86_netfx4-browser_files_b03f5f7f11d50a3a_4.0.15912.0_none_06d55e201f3d4256\chrome.browser %s"  #add the path of chrome here
    URLS = (
        "stackoverflow.com",
        "https://github.com/AarushiSinha28/Python_Projects_handson"
        "gmail.com"
        "google.com"
        "youtube.com"
    )
    for url in URLS:
        print("opening :"+ url)
        wb.get(chrome_path).open(url)

webauto()