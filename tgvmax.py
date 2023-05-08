import urllib.request
import json

class Monitor:
    def __init__(self):
        self.listResearch = []

    class Research:
        def __init__(self, origine, destination):
            self.origine = origine
            self.destination = destination
            self.dataBuffer = self.getData()

        def changementHandler():
            data = self.getData()
            if(self.dataBuffer == data):
                self.dataBuffer = data
                return true
            else:
                return false

        def getData():
            url = "https://ressources.data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&facet=origine&facet=destination&facet=od_happy_card&refine.origine=" +
            self.origine + "&refine.destination=" + 
            self.destination    
            response = urllib.request.urlopen(url)
            json_data = response.read().decode("utf-8")
            json_object = json.loads(json_data)
            return json_objet

    def addResearch(origine, destination):
        self.listResearch.insert(new Research("origine", "destination"))



    def initBuffer():
        for r in self.listResearch:
            if(r.dataBuffer = None):
                r.dataBuffer = self.getData(r)

    def startMonitor():
        self.initBuffer()


        




