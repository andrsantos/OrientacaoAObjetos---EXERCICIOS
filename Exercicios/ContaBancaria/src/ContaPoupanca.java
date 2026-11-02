public class ContaPoupanca extends ContaBancaria {

    Double taxaJuros;

    public ContaPoupanca(String nomeCliente, String numeroConta, Double saldo, Double taxaJuros) {
        super(nomeCliente, numeroConta, saldo);
        this.taxaJuros = taxaJuros;
    }

    public Double getTaxaJuros() {
        return taxaJuros;
    }

    public void setTaxaJuros(Double taxaJuros) {
        this.taxaJuros = taxaJuros;
    }

    public void aplicarRendimento() {
        Double rendimento = this.getSaldo() * (this.taxaJuros / 100);
        this.depositar(rendimento);
        System.out.println("Rendimento aplicado: " + rendimento + ". Saldo atual: " + this.getSaldo());
    }
    
}
