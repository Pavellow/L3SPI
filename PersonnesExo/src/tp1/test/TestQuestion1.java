package tp1.test;

import tp1.personnel.util.*;
import java.util.GregorianCalendar;
import util.Adresse;

public class TestQuestion1 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Personne a = new Personne("PA", "Vinciguerra", new GregorianCalendar(2001, 8, 31), new Adresse(21, "pascal", "20500", "corte"));
		System.out.println(a);
		Personne b = new Personne("Toto", "Famille", new GregorianCalendar(1998, 6, 25), new Adresse(21, "pascal", "20500", "corte"));
		Personne aBis = new Personne("PA", "Vinciguerra", new GregorianCalendar(2001, 8, 31), new Adresse(21, "pascal", "20500", "corte"));

	
		System.out.println(Personne.plusAgee(b, a)); //b est plus agé que a (c'est true)
		
		System.out.println(a.equals(aBis));
		
		Employe employeUn = new Employe("PA", "VINCI", new GregorianCalendar(2001, 8, 31), new Adresse(21, "pascal", "20500", "corte"), 25, new GregorianCalendar(2018, 5, 20));
		Employe employeDeux = new Employe("Laurant", "VINCI", new GregorianCalendar(2021, 5, 3), new Adresse(21, "pascal", "20500", "corte"), 25, new GregorianCalendar(2018, 5, 20));
		Employe employeTrois = new Employe("Bernard", "VINCI", new GregorianCalendar(202006, 10, 25), new Adresse(21, "pascal", "20500", "corte"), 25, new GregorianCalendar(2018, 5, 20));
		Employe employeQuatre = new Employe("Dylan", "VINCI", new GregorianCalendar(2002, 2, 3), new Adresse(21, "pascal", "20500", "corte"), 25, new GregorianCalendar(2018, 5, 20));
		Employe employeCinq = new Employe("Augustin", "VINCI", new GregorianCalendar(2005, 7, 2), new Adresse(21, "pascal", "20500", "corte"), 25, new GregorianCalendar(2018, 5, 20));
		
		System.out.println(employeUn.calculAnnuites());
		
	}
}