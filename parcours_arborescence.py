import os

def existe_un_repertoire(rep) :
    for i in os.rep :
        if not os.path.isdir(rep) :
            return False
    return True
    
    
def rechercher_fichiers(rep, nom_fichier) :
    pass


if __name__ == "__main__" :
    est_un_repertoire(".git")