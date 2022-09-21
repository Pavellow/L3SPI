import java.lang.reflect.Array;

public class DeMemoire extends Des {
    private String nom;
    private int nbrFace;
    private int array[] = new int[nbrFace];

    DeMemoire(String nomPara, int nbrFacePara) {
        this.nom = nomPara;
        this.nbrFace = nbrFacePara;
    }

    int lancer() {
        int nbAleatoire= this.aleatoire(1,this.getNbrFaces());
        System.out.println(this.nom+ " vaut "+ nbAleatoire);
        return nbAleatoire;
    }

    int lancer(int nbrLancer) {
        return 0;
    }

}
