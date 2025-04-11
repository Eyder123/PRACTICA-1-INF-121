package test;

import figuras.Figura;
import figuras.Cuadrado;
import figuras.Rectangulo;

public class FiguraTest {
    public static void main(String[] args) {
        Figura f1 = new Cuadrado(5);
        Figura f2 = new Rectangulo(4, 3);

        f1.mostrar();
        f2.mostrar();
    }
}
