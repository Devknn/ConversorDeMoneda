package com.conversor.de.monedas; // Reemplaza "tu_paquete" con el nombre de tu paquete

import javax.swing.JOptionPane;

public class ConversorDeMoneda {
    public static boolean iniciarConversorMoneda() {
        String[] eleccionesMonedas = {"De Euro a Otra Moneda", "De Otra Moneda a Euro"};
        String elecionMoneda = (String) JOptionPane.showInputDialog(null,
                "Seleccione la elección de la conversión", "Elección", JOptionPane.PLAIN_MESSAGE,
                null, eleccionesMonedas, eleccionesMonedas[0]);

        if (elecionMoneda == null) {
            int opcion = JOptionPane.showConfirmDialog(null,
                    "¿Desea volver a seleccionar una opción?", "Continuar",
                    JOptionPane.YES_NO_OPTION);
            return opcion == JOptionPane.YES_OPTION;
        }

        String[] monedas;
        double[] tasasDeCambio;

        if (elecionMoneda.equals("De Euro a Otra Moneda")) {
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

            double cantidadDeDinero = ObtenerCantidadDeDinero.obtenerCantidadDeDinero();

            if (Double.isNaN(cantidadDeDinero)) {
                JOptionPane.showMessageDialog(null,
                        "Cancelando opereración.");
                continue;
            }

            double cantidadConvertida;


            if (elecionMoneda.equals("De Euro a Otra Moneda")) {
                cantidadConvertida = cantidadDeDinero * tasasDeCambio[IndiceMoneda.indiceMoneda(monedaDestino)];
            } else {
                cantidadConvertida = cantidadDeDinero / tasasDeCambio[IndiceMoneda.indiceMoneda(monedaDestino)];
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


}
