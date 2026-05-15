import javax.swing.JOptionPane;

public class Account
{
    private String name;
    private double balance;

   
    public Account(String name, double balance)
    {
        this.name = name;

        if (balance > 0.0)
        {
            this.balance = balance;
        }
    }

   
    public void deposit(double depositAmount)
    {
        if (depositAmount > 0.0)
        {
            balance += depositAmount;
        }
    }

    public void withdraw(double withdrawAmount)
    {
        if (withdrawAmount > 0.0 && withdrawAmount <= balance)
        {
            balance -= withdrawAmount;
        }
        else
        {
            JOptionPane.showMessageDialog(null,
                "Saldo insuficiente ou valor inválido!");
        }
    }

    public String getName()
    {
        return name;
    }

    public double getBalance()
    {
        return balance;
    }

  
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