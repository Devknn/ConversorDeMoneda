import javax.swing.JOptionPane;

public class Pri {
    public static void main(String[] args) {
        String[] eleccion = {"Conversor de Moneda", "Medidor de temperatura"};

        boolean continuar = true;


        while (continuar) {
            String seleccionarValor = (String) JOptionPane.showInputDialog(null,
                    "Seleccione una opción", "CONVERSOR", JOptionPane.PLAIN_MESSAGE, null,
                    eleccion, eleccion[0]);

            switch (seleccionarValor) {
                case "Conversor de Moneda":
                    continuar = conversor.ConversorDeMoneda.iniciarConversorMoneda();
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida");
                    break;
            }
        }
    }


}
