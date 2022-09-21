import java.util.*;

public class Des {
    // Attributs
    private String nom;
    private int nbrFaces;

    public static final int MIN_FACES = 3;
    public static final int MAX_FACES = 120;
    public static final int SIX_FACES = 6;

    private static Random r = new Random();

    private static int iterDe = 0;


    // Constructeurs
    public Des(String nom, int nbrFacesPara) {
        iterDe++;
        this.nom = nom;
        setNbrFaces(nbrFacesPara);
    }

    public Des() {
        this("De n:" + iterDe, SIX_FACES);
    }

    public Des(String nomPara) {
        this(nomPara, SIX_FACES);
    }

    // Méthodes
    int getNbrFaces() {
        return nbrFaces;
    }

    void setNbrFaces(int nbrFacesPara) {
        if((nbrFacesPara < MIN_FACES ) || (nbrFacesPara > MAX_FACES)){
            System.err.println("Erreur: le nombre de face est illegal (inferieur a 3 ou superieur a 120).");
        }
        else {
            this.nbrFaces = nbrFacesPara;
        }
    }

    String getName(){
        return this.nom;
    }
    void show() {
        System.out.println("Ce de est : "+this.nom+", il a "+this.nbrFaces+" faces.");
    }

    int aleatoire(int valMin, int valMax) {
        int max = valMax;
        int min = valMin;
        int range = max - min + 1;
        int rand = (int)(Math.random() * range) + min;
        return rand;
    }

    int lancer() {
        int nbAleatoire= this.aleatoire(1,this.getNbrFaces());
        System.out.println(this.nom+ " vaut "+ nbAleatoire);
        return nbAleatoire;
    }

    int lancer(int nbrLancer) {
        int valMax = 0;
        for(int i = 0; i <= nbrLancer; i++) {
            int nbAleatoire= this.aleatoire(1,this.getNbrFaces());
            System.out.println("TIRAGE NORMAL : " + nbAleatoire);
            if(nbAleatoire >= valMax) {
                valMax = nbAleatoire;
            }
        }
        System.out.println("Le lancer consecutif de " + this.nom + " a donne comme valeur max " + valMax);
        return valMax;
    }

}

