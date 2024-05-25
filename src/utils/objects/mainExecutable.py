from . import querySerializer as SRLS

class Generator():
    def __init__(self):
        self.account:int = int(input("Pon el número de cuenta: "))
        self.name:str = input("Pon el nombre del usuario: ")
        self.amount:int = int(input("Pon el monto de pago: "))

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