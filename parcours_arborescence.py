import os

   
    
def rechercher_fichier(rep, nom_fichier) :
    
    
    for fichier in os.listdir(rep) :
        
        chemin = rep
        
        
        if fichier == nom_fichier :
        
            if os.path.isdir(chemin) :
                chemin = rep + "/" + fichier
                print("Le fichier existe et se trouve dans ", chemin)
                return chemin
        
        else :     

            chemin = rep + "/" + fichier
            
            if os.path.isdir(chemin) :
               
                rechercher_fichier(chemin, nom_fichier)
                

def factorielle(n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorielle(n - 1)

if __name__ == "__main__" :

    print(rechercher_fichier("/home/paul/Documents", "code cv jooble"))
    
    print(factorielle(5))
 
    
    