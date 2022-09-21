public class DePipe extends Des {
    private String nom;
    private int nbrFace;
    private int valMinPipage;
    DePipe(String nom, int nbrFace, int valMinPipage) {
        this.nom = nom;
        this.nbrFace = nbrFace;
        this.valMinPipage = valMinPipage;
    }

    int lancer() {
        int nbAleatoire = this.aleatoire(valMinPipage,this.getNbrFaces());
        System.out.println(this.nom+ " vaut "+ nbAleatoire);
        return nbAleatoire;
    }

    int lancer(int nbrLancer) {
        int valMax = 0;
        for(int i = 0; i <= nbrLancer; i++) {
            int nbAleatoire = this.aleatoire(valMinPipage,this.getNbrFaces());
            System.out.println("TIRAGE PIPE : " + nbAleatoire);
            if(nbAleatoire >= valMax) {
                valMax = nbAleatoire;
            }
        }
        System.out.println("Le lancer consecutif de " + this.nom + " a donne comme valeur max " + valMax);
        return valMax;
    }

}
