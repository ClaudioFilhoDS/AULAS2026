import java.util.Arrays;
import java.util.Random;
import javax.swing.JOptionPane;

public class sorteio {
    public static void main(String[] args) {

        int[] numeros = new int[6];
        Random random = new Random();

        int i = 0;

        while (i < 6) {

            int numero = random.nextInt(60) + 1;
            boolean repetido = false;

            for (int j = 0; j < i; j++) {
                if (numeros[j] == numero) {
                    repetido = true;
                }
            }
            if (!repetido) {
                numeros[i] = numero;
                i++;
            }
        }

        Arrays.sort(numeros);

        String resultado = "Números sorteados da Mega-Sena: ";

        for (int numero : numeros) {
            resultado += numero + " ";
        }

        JOptionPane.showMessageDialog(null, resultado);
    }
}
