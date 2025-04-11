package vehiculos;

public class Moto extends Vehiculo {
    private boolean tieneSidecar;

    public Moto(String marca, String modelo, boolean tieneSidecar) {
        super(marca, modelo);
        this.tieneSidecar = tieneSidecar;
    }

    @Override
    public void mostrarInfo() {
        System.out.println("Moto: " + marca + " " + modelo + " - Sidecar: " + (tieneSidecar ? "Sí" : "No"));
    }
}
