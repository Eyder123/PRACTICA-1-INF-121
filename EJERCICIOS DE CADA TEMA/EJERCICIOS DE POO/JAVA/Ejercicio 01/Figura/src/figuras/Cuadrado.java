package figuras;

public class Cuadrado extends Figura {
    double lado;

    public Cuadrado(double lado) {
        this.lado = lado;
    }

    @Override
    public double calcularArea() {
        return lado * lado;
    }

    @Override
    public void mostrar() {
        System.out.println("Soy un Cuadrado. Lado: " + lado + ", Área: " + calcularArea());
    }
}
