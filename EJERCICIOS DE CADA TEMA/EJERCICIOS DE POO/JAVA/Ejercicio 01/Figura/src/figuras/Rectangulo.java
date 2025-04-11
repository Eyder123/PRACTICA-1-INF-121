package figuras;

public class Rectangulo extends Figura {
    double base, altura;

    public Rectangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    public double calcularArea() {
        return base * altura;
    }

    @Override
    public void mostrar() {
        System.out.println("Soy un Rectángulo. Base: " + base + ", Altura: " + altura + ", Área: " + calcularArea());
    }
}
