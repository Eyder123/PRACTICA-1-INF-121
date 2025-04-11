package test;

import empleados.*;

public class EmpleadoTest {
    public static void main(String[] args) {
        Empleado e1 = new EmpleadoTiempoCompleto("Ana", 2500.0);
        Empleado e2 = new EmpleadoPorHoras("Luis", 120, 15.5);

        e1.mostrarInfo(); // Salario: 2500.0
        e2.mostrarInfo(); // Salario: 1860.0
    }
}