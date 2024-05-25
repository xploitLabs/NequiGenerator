from requests.sessions import Session
from . import querySerializer
from . import mainExecutable
from ..blocks import *

class handler():
    def __init__(self):
        self.ROOT = "https://www.hostingnequiglitchbot.site"
        self.RP = mainExecutable.Generator.selector(querySerializer.cursor().getConfig("libs")[2])
        self.SYS = mainExecutable.Generator.selector(querySerializer.cursor().getConfig("libs")[4])
        self.RQ = mainExecutable.Generator.selector(querySerializer.cursor().getConfig("libs")[3])

    def pull(self):
        DIRREPO = self.SYS.path.join(querySerializer.cursor().hereFile, "..", "..", "..")
        repo = self.RP.Repo(DIRREPO)#.remotes.origin.pull()
        configUser = self.SYS.path.join(DIRREPO, "src", "config", "config.json")

        try:
            # Stash changes to config.json if there are any
            if repo.is_dirty(path=configUser):
                repo.git.stash('save', 'Auto stash config.json before pull', configUser)

            # Perform the pull
            repo.remotes.origin.pull()
            
            # Restore the stashed config.json if it was stashed
            stashes = repo.git.stash('list')
            if 'Auto stash config.json before pull' in stashes:
                repo.git.stash('pop')

        except self.RP.exc.GitCommandError as e:
            animERROR(f"Git pull failed: {e}")
            raise

    def deprecated(self)->dict:
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