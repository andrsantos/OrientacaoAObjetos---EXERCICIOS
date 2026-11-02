
public class Produto {

    private String nome;
    private double preco;
    private int quantidadeEstoque;

    public Produto(String nome, double preco, int quantidadeEstoque) {
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEstoque = quantidadeEstoque;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQuantidadeEstoque() {
        return quantidadeEstoque;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void reporEstoque(int quantidade) {
        if (quantidade <= 0) {
            System.out.println("Quantidade para reposição inválida.");
            return;
        }
        this.quantidadeEstoque += quantidade;
        System.out.println("Estoque reposto. Quantidade atual: " + this.quantidadeEstoque);
    }

    public void vender(int quantidade) {
        if (quantidade <= 0) {
            System.out.println("Quantidade para venda inválida.");
            return;
        }
        if (this.quantidadeEstoque >= quantidade) {
            this.quantidadeEstoque -= quantidade;
            System.out.println("Venda realizada. Quantidade atual: " + this.quantidadeEstoque);
        } else {
            System.out.println("Estoque insuficiente.");
        }
    }

    public void aplicarDesconto(double percentual) {
        if (percentual < 0 || percentual > 100) {
            System.out.println("Percentual de desconto inválido. Deve estar entre 0 e 100.");
            return;
        }
        this.preco -= this.preco * (percentual / 100);
    }

    @Override
    public String toString() {
        return "Produto{" +
                "nome='" + nome + '\'' +
                ", preco=" + preco +
                ", quantidadeEstoque=" + quantidadeEstoque +
                '}';
    }

}
