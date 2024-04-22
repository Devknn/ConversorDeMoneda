package com.conversor.de.monedas;

import javax.swing.*;

public class ObtenerCantidadDeDinero {
    public static double obtenerCantidadDeDinero() {
        double cantidadDeDinero = Double.NaN;

        // con el bucle do puedo iniciar mi bucle por lo menos una vez ante de la condicion
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
