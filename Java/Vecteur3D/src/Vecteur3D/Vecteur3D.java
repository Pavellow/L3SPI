package Vecteur3D;

public class Vecteur3D {
    // Attributs
    private int x;
    private int y;
    private int z;

    //Constructeurs
    Vecteur3D(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
        }

    Vecteur3D() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    //Méthodes
    void show(){
        System.out.println("Le vecteur a pour coordonnees : <"+this.x+","+this.y+","+this.z+">");
    }

    double norme() {
        return (java.lang.Math.sqrt((this.x*this.x)+(this.y*this.y)+(this.z*this.z)));
    }

    static float produitScalaireStatic(Vecteur3D u, Vecteur3D v) { return u.x * v.x + u.y * v.y + u.z*v.z; }

    float produitScalaire(Vecteur3D v) { return this.x * v.x + this.y * v.y + this.z*v.z; }

    static Vecteur3D somme(Vecteur3D u, Vecteur3D v) {
        int a = v.x + u.x;
        int b = v.y + u.y;
        int c = v.z + u.z;
        return new Vecteur3D(a, b, c);
    }

    Vecteur3D somme(Vecteur3D v) {
        int a = this.x + v.x;
        int b = this.y + v.y;
        int c = this.z + v.z;
        return new Vecteur3D(a, b, c);
    }
}


