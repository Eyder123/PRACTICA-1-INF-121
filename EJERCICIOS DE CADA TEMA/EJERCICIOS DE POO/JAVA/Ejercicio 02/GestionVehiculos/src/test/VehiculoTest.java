package test;

import vehiculos.Auto;
import vehiculos.Moto;
import vehiculos.Vehiculo;

public class VehiculoTest {
    public static void main(String[] args) {
        Vehiculo v1 = new Auto("Toyota", "Corolla", 4);
        Vehiculo v2 = new Moto("Yamaha", "MT-07", false);

        v1.mostrarInfo();
        v2.mostrarInfo();
    }
}
