import requests

def getWiki(name):
    #get WIKI Link
    wikiEndPoint = "https://en.wikipedia.org/w/api.php"
    wikiParams = {
    "action" : "query",
    "titles" : name,
    "prop"  :   "info",
    "inprop" : "url",
    "format" : "json",
    "formatversion" : "2",
    "origin" : "*"
    }
    result = requests.get(wikiEndPoint, wikiParams)
    result_json = result.json()
    try:
        Wiki_Link = result_json["query"]["pages"][0]["fullurl"]
    except KeyError:
        print('WIKI API fail')
    
    return(Wiki_Link)