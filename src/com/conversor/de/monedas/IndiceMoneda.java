package com.conversor.de.monedas;

public class IndiceMoneda {
    public static int indiceMoneda(String moneda) {
        String[] monedas = {"Dólar", "Bolívares", "Yen", "Pesos", "Soles", "Libras"};
        for (int i = 0; i < monedas.length; i++) {
            if (moneda.equals(monedas[i])) {
                return i;
            };
        };
        return -1; // Si no se encuentra la moneda
    }
}