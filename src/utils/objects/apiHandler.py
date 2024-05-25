from requests.sessions import Session
from . import querySerializer
from . import mainExecutable

class handler():
    def __init__(self):
        self.ROOT = "https://www.hostingnequiglitchbot.site"
        self.RP = mainExecutable.Generator().selector(querySerializer.cursor().getConfig("libs")[2])
        self.SYS = mainExecutable.Generator().selector(querySerializer.cursor().getConfig("libs")[4])
        self.RQ = mainExecutable.Generator().selector(querySerializer.cursor().getConfig("libs")[3])

    def pull(self):
        self.RP.Repo(self.SYS.path.join(querySerializer.cursor().hereFile, "..", "..", "..")).remotes.origin.pull()

    def deprecated(self):
        echo = str(self.RP.Repo(self.SYS.path.join(querySerializer.cursor().hereFile, "..", "..", "..")).head.commit.hexsha)
        hash = str(self.RQ.get("https://api.github.com/repos/xploitLabs/NequiGenerator/commits").json()[0]["sha"])
        return {'STTS': echo != hash}

    def api(self) -> Session:
        return self.RQ.session()
    
    def joinerDirs(self, listData:list) -> str:
        subdirs = "/".join(listData)
        DIR = self.ROOT+"/"+subdirs
        return DIR 

    def listDataRequirements(self) -> list:
        return ([handler().joinerDirs(["DisponibleValor", "agregarName.php"]), handler().joinerDirs(["DisponibleValor", "upload.php"]), handler().joinerDirs(["DisponibleValor", "Comprobantes", "descargar.php?"])], ["NumeroNequi", "Nombre", "Valor"])