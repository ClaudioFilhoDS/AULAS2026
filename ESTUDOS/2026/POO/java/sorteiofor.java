import java.util.Arrays;
import java.util.Random;
import javax.swing.JOptionPane;

public class sorteiofor {
    public static void main(String[] args) {

        int[] numeros = new int[6];
        Random random = new Random();

        for (int i = 0; i < 6; i++) {
            
            int numero = random.nextInt(60) + 1;
            boolean repetido = false;

          
            for (int j = 0; j < i; j++) {
                if (numeros[j] == numero) {
                    repetido = true;
                    break; 
                }
            }

       
            if (!repetido) {
                numeros[i] = numero;
            } 
        
            else {
                i--; 
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