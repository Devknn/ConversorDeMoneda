import javax.swing.*;

public class Principal {
    public static void main(String[] args) {
        // Mostrar el cuadro de diálogo con las opciones
        String[] options = {"Conversor de Moneda", "Otra función 1", "Otra función 2", "Salir"};
        String selectedOption = (String) JOptionPane.showInputDialog(null,
                "Seleccione una opción:", "Menú", JOptionPane.PLAIN_MESSAGE,
                null, options, options[0]);

        // Realizar una acción basada en la opción seleccionada
        if (selectedOption != null) {
            switch (selectedOption) {
                case "Conversor de Moneda":
                    // Aquí puedes llamar a tu función de conversor de moneda
                    JOptionPane.showMessageDialog(null, "Has seleccionado el Conversor de Moneda");
                    break;
                case "Otra función 1":
                    // Aquí puedes implementar la lógica para la otra función 1
                    JOptionPane.showMessageDialog(null, "Has seleccionado Otra función 1");
                    break;
                case "Otra función 2":
                    // Aquí puedes implementar la lógica para la otra función 2
                    JOptionPane.showMessageDialog(null, "Has seleccionado Otra función 2");
                    break;
                case "Salir":
                    JOptionPane.showMessageDialog(null, "Saliendo del programa...");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Opción no válida");
            }
        } else {
            JOptionPane.showMessageDialog(null, "No se seleccionó ninguna opción");
        }
    }
}
