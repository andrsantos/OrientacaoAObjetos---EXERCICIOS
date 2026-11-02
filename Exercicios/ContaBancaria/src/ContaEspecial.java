public class ContaEspecial extends ContaBancaria {

    Double limite;

    public ContaEspecial(String nomeCliente, String numeroConta, Double saldo, Double limite) {
        super(nomeCliente, numeroConta, saldo);
        this.limite = limite;
    }

    public Double getLimite() {
        return limite;
    }

    public void setLimite(Double limite) {
        this.limite = limite;
    }

    @Override
    public void sacar(Double valor) {
        if (this.getSaldo() + this.limite >= valor) {
            this.setSaldo(this.getSaldo() - valor);
            System.out.println("Saque realizado com sucesso." + " Saldo atual: " + this.getSaldo());
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }
    
}
