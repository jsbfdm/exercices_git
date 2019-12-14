import os
import glob

def existe_un_repertoire(rep) :
    for i in os.listdir(rep) :
        if not os.path.isdir(rep) :
            return False
    return True

def nb_rep(rep) :
    nb = 0
    for i in os.listdir(rep) :
        if os.path.isdir(i) :
            nb += 1
    return nb
    
    
def rechercher_fichier(rep, nom_fichier) :
    chemin = rep

    for fichier in os.listdir(rep) :
        
        
        if fichier == nom_fichier :
            chemin = chemin + "/" + fichier
            print("Trouvéééééééééééééééééééééééééééééééé", " ====== ", chemin)
            return chemin
            
        else :     
            fichier = chemin + "/" + fichier
            
            if os.path.isdir(fichier) :
                
                
                rechercher_fichier(fichier, nom_fichier)

                
            
                        
                
            
            
    


if __name__ == "__main__" :
    existe_fichier = rechercher_fichier(".", "et voici le meilleur")
    print(existe_fichier)
 
    
    