class Robot {
    String ref;
    String nom;
    int x;
    int y;
    int orientation;
    static int robotCrees = 0;
    Robot(String nom, int x, int y, int orientation) {
        this.nom = nom;
        this.x = x;
        this.y = y;
        this.orientation = orientation;
        robotCrees = robotCrees + 1;
        this.ref = "ROB" + Integer.toString(robotCrees);
    }
    Robot(String nom) {
        this.nom = nom;
        robotCrees = robotCrees + 1;
        this.x = 0;
        this.y = 0;
        this.orientation = 0;
        this.ref = "ROB" + Integer.toString(robotCrees);
    }

    void changeOrientation(int change) {
        this.orientation = change;
    }

    void deplacer(int pas) {
        if(this.orientation == 0) {
            this.y = y + pas;
        }
        else if(this.orientation == 1) {
            this.x = x + pas;
        }
        else if(this.orientation == 2) {
            this.y = y - pas;
        }
        else {
            this.x = x - pas;
        }

        if(this.x < 0) {
            this.x = 0;
        }
        if(this.y < 0){
            this.y = 0;
        }

    }

    void changerOrientation(int newOrientation) {
        if(newOrientation > 3) {
            this.orientation = 0;
        }
        else {this.orientation = newOrientation;}
    }

    void afficheToi() {
        System.out.println("Le robot "+this.nom+" a ete cree. Il se situe a la position "+this.x+" et "+this.y+". Son orientation est "+this.orientation+". La reference de ce robot est "+this.ref);
    }

}

class Main {
    public static void main(String[] args) {

        Robot robotOne = new Robot("Antoine", 10,20,2);
        Robot robotTwo = new Robot("Charles", 0, 0, 0);

        robotOne.afficheToi();
        robotOne.changeOrientation(3);
        robotOne.deplacer(3);
        robotOne.afficheToi();

        robotTwo.afficheToi();
        robotTwo.changeOrientation(1);
        robotTwo.deplacer(7);
        robotTwo.afficheToi();

    }
}

