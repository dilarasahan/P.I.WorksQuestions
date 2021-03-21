def change_url(url):
    url = url.split("/")[2][:-1]
    return url
    
    
    
string = "<url>https://xcd32112.smart_meter.com</url>"

change_url(string)
