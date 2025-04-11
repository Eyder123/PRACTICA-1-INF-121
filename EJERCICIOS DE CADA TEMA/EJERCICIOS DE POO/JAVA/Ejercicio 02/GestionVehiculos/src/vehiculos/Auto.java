package vehiculos;

public class Auto extends Vehiculo {
    private int puertas;

    public Auto(String marca, String modelo, int puertas) {
        super(marca, modelo);
        this.puertas = puertas;
    }

    @Override
    public void mostrarInfo() {
        System.out.println("Auto: " + marca + " " + modelo + " - Puertas: " + puertas);
    }
}
