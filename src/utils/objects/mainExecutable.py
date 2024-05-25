from . import querySerializer as SRLS
from . import apiHandler
import importlib as MPRLT
from .. import blocks

class Generator():
    def __init__(self, account, name, amount):
        self.account:int = account
        self.name:str = name
        self.amount:int = amount

    def initializer(self):
        responseF = SRLS.cursor().getConfig("templateResponseExecutable")
        status = False
        for C in range(3):
            handler = SRLS.cursor().reQ()
            response = handler.requests({'NumeroNequi': self.account, 'Nombre': self.name, 'Valor': self.amount, "counter": C})
            responseF["ListAux"].append(response)
            status = bool(response) if response else bool(response)
            if not status:
                return False
        return responseF
    
    def selector(selection):
        return MPRLT.import_module(selection)
    
    def conection():
        r = Generator.selector("requests")
        s = Generator.selector("sys")
        try:
            r.get("https://google.com/")
        except Exception as Error:
            blocks.animERROR("Al parecer no tienes conexión a internet.")
            s.exit()

    def os_anfitrion():
        platform = Generator.selector("platform")
        return platform.system() # Windows, linux# Ejemplo de uso