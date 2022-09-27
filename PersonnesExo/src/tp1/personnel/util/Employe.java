package tp1.personnel.util;

import java.util.Calendar;
import java.util.GregorianCalendar;

import util.Adresse;

public class Employe extends Personne{
	//Attributes
	private int salaire;
	private GregorianCalendar dateEmbauche;
	private final int AGE_MINIMAL = 16;
	private final int AGE_MAXIMAL = 65;
	//Constructors
	public Employe(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse, int salaire, GregorianCalendar dateEmbauche) {
		super(leNom, lePrenom, laDate, lAdresse);
		this.salaire = salaire;
		this.setDateEmbauche(dateEmbauche);
	}
	
	//Getter
	public int getSalaire() {
		return salaire;
	}

	public GregorianCalendar getDateEmbauche() {
		return dateEmbauche;
	}
	
	//Setter
	public void setSalaire(int salaire) {
		this.salaire = salaire;
	}

	public void setDateEmbauche(GregorianCalendar dateEmbauche) {
		this.dateEmbauche = dateEmbauche;
	}
	
	//Methods
	
	private int getTempsEcoule(GregorianCalendar dateDeDepart) {
		long now = System.currentTimeMillis();
		GregorianCalendar naissance = dateDeDepart;
		long naissanceMillis = naissance.getTimeInMillis();
		long tempsEcouleMillis = now - naissanceMillis;
		long sec = tempsEcouleMillis / 1000;
		long min = sec / 60;
		long heure = min / 60;
		long jour = heure / 24;
		long ageEnAnnee = jour / 365;
		
		return (int) ageEnAnnee;
	}
	
	 public static Employe createEmploye(Employe a) {
		 if((a.getTempsEcoule(a.dateNaissance) >= a.AGE_MINIMAL) && (a.getTempsEcoule(a.dateNaissance) <= a.AGE_MAXIMAL)) {
			 return a;
		 }
		 else {
			 return null;
		 }
		 
	 }
	 
	 public void augmenterSalaire(int pourcentage) {
		 if(pourcentage > 0) {
			 this.salaire = salaire + (salaire * (pourcentage/100));
		 }
		 else {
			 System.err.println("Veuillez utiliser la méthode baisserSalaire pour ce cas là");
		 }
	 }
	 
	 public int calculAnnuites() {
		 return this.getTempsEcoule(this.dateEmbauche);
	 }
	 
	 
}
