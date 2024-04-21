package conversor; // Reemplaza "tu_paquete" con el nombre de tu paquete

import javax.swing.JOptionPane;

public class ConversorDeMoneda {
    public static boolean iniciarConversorMoneda() {
        String[] direcciones = {"De Euro a Otra Moneda", "De Otra Moneda a Euro"};
        String direccion = (String) JOptionPane.showInputDialog(null,
                "Seleccione la dirección de la conversión", "Dirección", JOptionPane.PLAIN_MESSAGE,
                null, direcciones, direcciones[0]);

        if (direccion == null) {
            int opcion = JOptionPane.showConfirmDialog(null,
                    "¿Desea volver a seleccionar una opción?", "Continuar",
                    JOptionPane.YES_NO_OPTION);
            return opcion == JOptionPane.YES_OPTION;
        }

        String[] monedas;
        double[] tasasDeCambio;
        if (direccion.equals("De Euro a Otra Moneda")) {
            monedas = new String[]{"Dólar", "Bolívares", "Yen", "Pesos", "Soles", "Libras"};
            tasasDeCambio = new double[]{1.0, 0.85, 110620.0, 130.87, 88.49, 0.73}; // Tasas de cambio de Euro a otras monedas
        } else {
            monedas = new String[]{"Dólar", "Bolívares", "Yen", "Pesos", "Soles", "Libras"};
            tasasDeCambio = new double[]{1.18, 0.0000090, 0.0076, 0.0113, 0.28, 1.37}; // Tasas de cambio de otras monedas a Euro
        }

        while (true) {
            String monedaDestino = (String) JOptionPane.showInputDialog(null,
                    "Elija la moneda de destino",
                    "Monedas", JOptionPane.PLAIN_MESSAGE, null, monedas, monedas[0]);

            if (monedaDestino == null) {
                int opcion = JOptionPane.showConfirmDialog(null,
                        "¿Desea volver a seleccionar una opción?", "Continuar",
                        JOptionPane.YES_NO_OPTION);
                return opcion == JOptionPane.YES_OPTION;
            }

            double cantidadDeDinero = obtenerCantidadDeDinero();

            if (Double.isNaN(cantidadDeDinero)) {
                JOptionPane.showMessageDialog(null,
                        "No se ingresó ningún valor.");
                continue;
            }

            double cantidadConvertida;
            if (direccion.equals("De Euro a Otra Moneda")) {
                cantidadConvertida = cantidadDeDinero * tasasDeCambio[indiceMoneda(monedaDestino)];
            } else {
                cantidadConvertida = cantidadDeDinero / tasasDeCambio[indiceMoneda(monedaDestino)];
            }

            JOptionPane.showMessageDialog(null,
                    "Tienes " + cantidadConvertida + " " + monedaDestino);

            int opcion = JOptionPane.showConfirmDialog(null, "¿Desea realizar otra conversión?", "Continuar",
                    JOptionPane.YES_NO_CANCEL_OPTION);

            switch (opcion) {
                case JOptionPane.YES_OPTION:
                    break;
                case JOptionPane.NO_OPTION:
                case JOptionPane.CANCEL_OPTION:
                default:
                    JOptionPane.showMessageDialog(null, "Programa Finalizado");
                    return false;
            }
        }
    }

    private static int indiceMoneda(String moneda) {
        String[] monedas = {"Dólar", "Bolívares", "Yen", "Pesos", "Soles", "Libras"};
        for (int i = 0; i < monedas.length; i++) {
            if (moneda.equals(monedas[i])) {
                return i;
            }
        }
        return -1; // Si no se encuentra la moneda
    }

    private static double obtenerCantidadDeDinero() {
        double cantidadDeDinero = Double.NaN;
        do {
            String cantidad = JOptionPane.showInputDialog(null,
                    "Ingrese la cantidad de dinero que desea convertir:");
            if (cantidad == null) {
                return Double.NaN;
            }
            try {
                cantidadDeDinero = Double.parseDouble(cantidad);
                if (cantidadDeDinero < 0) {
                    JOptionPane.showMessageDialog(null, "Por favor, ingrese un número positivo.");
                }
            } catch (NumberFormatException e) {
                JOptionPane.showMessageDialog(null, "Por favor, ingrese un número válido.");
            }
        } while (cantidadDeDinero < 0);
        return cantidadDeDinero;
    }
}
