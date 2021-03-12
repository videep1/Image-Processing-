import webbrowser,time,random
while True:
    sites=random.choice(['google.com','youtube.com','amazon.com'])
    visit="http://{}".format(sites)
    webbrowser.open(visit)
    seconds=random.randrange()