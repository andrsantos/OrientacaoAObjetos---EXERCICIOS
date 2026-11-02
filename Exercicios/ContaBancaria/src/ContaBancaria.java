public class ContaBancaria {

    String nomeCliente;
    String numeroConta;
    Double saldo;

    public ContaBancaria(String nomeCliente, String numeroConta, Double saldo) {
        this.nomeCliente = nomeCliente;
        this.numeroConta = numeroConta;
        this.saldo = saldo;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    public String getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(String numeroConta) {
        this.numeroConta = numeroConta;
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public void depositar(Double valor) {
        this.saldo += valor;
    }

    public void sacar(Double valor) {
        if (this.saldo >= valor) {
            this.saldo -= valor;
        System.out.println("Saque realizado com sucesso." + " Saldo atual: " + this.saldo);
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }

}
