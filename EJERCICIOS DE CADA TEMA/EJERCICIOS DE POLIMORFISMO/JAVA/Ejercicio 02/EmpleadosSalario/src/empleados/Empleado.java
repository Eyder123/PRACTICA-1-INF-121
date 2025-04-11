package empleados;

public class Empleado {
    protected String nombre;

    public Empleado(String nombre) {
        this.nombre = nombre;
    }

    public double calcularSalario() {
        return 0.0;
    }

    public void mostrarInfo() {
        System.out.println("Empleado: " + nombre + ", Salario: " + calcularSalario());
    }
}