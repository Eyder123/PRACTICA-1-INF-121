package test;

import animales.Animal;
import animales.Perro;
import animales.Gato;

public class AnimalTest {
    public static void main(String[] args) {
        Animal a1 = new Perro();
        Animal a2 = new Gato();

        a1.hacerSonido(); // Guau guau!
        a2.hacerSonido(); // Miau miau!
    }
}
