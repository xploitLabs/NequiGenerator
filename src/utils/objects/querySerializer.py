import json, base64, os
from requests.sessions import Session
from . import apiHandler, mainExecutable

class cursor():
    def __init__(self):
        self.hereFile = os.path.dirname(os.path.abspath(__file__))
        self.configName = "config.json"

    class reQ():
        def __init__(self):
            self.handler:Session = apiHandler.handler().api()
        
        def requests(self, JSONDATA):
            tasks, postKeys = apiHandler.handler().listDataRequirements()
            dicty = {}
            for k in postKeys:
                dicty[k] = JSONDATA[k]
            pRS = "" if JSONDATA["counter"] == len(tasks)-1 else f", data={dicty}"
            method = "get" if JSONDATA["counter"] == len(tasks)-1 else "post"
            try:
                response = eval(f"self.handler.{method}('{tasks[JSONDATA['''counter''']]}'{pRS})")
            except Exception as Error:
                print (f"Ocurrió un error: {Error}")
                response = None
            return response

    def getConfig(self, instance):
        return json.load(open(os.path.join(self.hereFile, self.configName), "r"))[instance]
    
    class ParserJson():
        def __init__(self, pathfile) -> None:
            self.pathfile = pathfile
            self.jsonParser = mainExecutable.Generator.selector("json")
        
        def loadJSON(self):
            return self.jsonParser.load(open(self.pathfile, "r"))
        
        def saveJSON(self, object:dict):
            return self.jsonParser.dump(object, open(self.pathfile, "w"))