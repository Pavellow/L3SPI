package Vecteur3D;

public class Main {
    public static void main(String[] args) {
        Vecteur3D u = new Vecteur3D(3, 5, 8);
        Vecteur3D v = new Vecteur3D(7,2,6);

        u.show();
        v.show();

        System.out.println(u.norme());

        System.out.println(u.produitScalaire(v));

        Vecteur3D w = u.somme(v);
        w.show();
    }

}