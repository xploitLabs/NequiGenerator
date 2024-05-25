import requests
from requests.sessions import Session
import git
from . import querySerializer
import os

class handler():
    def __init__(self):
        self.ROOT = "https://www.hostingnequiglitchbot.site"

    def git_pull(self):
        repo = git.Repo(os.path.join(querySerializer.cursor().hereFile, "..", "..", ".."))
        origin = repo.remotes.origin
        origin.pull()

    def forUpdate(self):
        repo = git.Repo(os.path.join(querySerializer.cursor().hereFile, "..", "..", ".."))
        local_hash = repo.head.commit.hexsha

        response = requests.get(f"https://api.github.com/repos/xploitLabs/NequiGenerator/commits")
        remote_hash = response.json()[0]["sha"]

        return str(local_hash) == str(remote_hash)

    def api(self) -> Session:
        return requests.session()
    
    def joinerDirs(self, listData:list) -> str:
        subdirs = "/".join(listData)
        DIR = self.ROOT+"/"+subdirs
        return DIR 

    def listDataRequirements(self) -> list:
        return ([handler().joinerDirs(["DisponibleValor", "agregarName.php"]), handler().joinerDirs(["DisponibleValor", "upload.php"]), handler().joinerDirs(["DisponibleValor", "Comprobantes", "descargar.php?"])], ["NumeroNequi", "Nombre", "Valor"])