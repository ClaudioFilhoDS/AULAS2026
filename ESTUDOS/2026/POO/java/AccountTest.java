import javax.swing.JOptionPane;
public class AccountTest {
public static void main(String[] args)
    {
        String nome = JOptionPane.showInputDialog(
            "Digite o nome do titular:");

       
        double saldoInicial = Double.parseDouble(
            JOptionPane.showInputDialog(
                "Digite o saldo inicial:"));

    
        Account conta = new Account(nome, saldoInicial);

        
        double deposito = Double.parseDouble(
            JOptionPane.showInputDialog(
                "Digite o valor do depósito:"));
  
        conta.deposit(deposito);

       
        double saque = Double.parseDouble(
            JOptionPane.showInputDialog(
                "Digite o valor do saque:"));

        conta.withdraw(saque);

    
        JOptionPane.showMessageDialog(null,
            "Titular: " + conta.getName() +
            "\nSaldo final: R$ " + conta.getBalance());

        System.exit(0);
    }
}