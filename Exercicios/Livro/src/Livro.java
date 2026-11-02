
public class Livro {

    private String titulo;
    private String autor;
    private int anoPublicacao;
    private int preco;

    public Livro(String titulo, String autor, int anoPublicacao, int preco) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.preco = preco;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public int getPreco() {
        return preco;
    }

    public void setPreco(int preco) {
        this.preco = preco;
    }

    @Override
    public String toString() {
        return "Livro{" +
                "titulo='" + titulo + '\'' +
                ", autor='" + autor + '\'' +
                ", anoPublicacao=" + anoPublicacao +
                ", preco=" + preco +
                '}';
    }

    public void aplicarDesconto(double percentual) {

        if (percentual < 0 || percentual > 100) {
        System.out.println("Percentual de desconto inválido. Deve estar entre 0 e 100.");
        }
        
        this.preco -= this.preco * (percentual / 100);
    }


}