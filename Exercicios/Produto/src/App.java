public class App {
    public static void main(String[] args) throws Exception {

        Produto produto1 = new Produto("Caderno", 25.0, 10);
        Produto produto2 = new Produto("Caneta", 5.0, 50);

        System.out.println("Antes das operações:");
        System.out.println(produto1);
        System.out.println(produto2);

        produto1.reporEstoque(5);
        produto2.vender(10);

        produto1.aplicarDesconto(10);
        produto2.aplicarDesconto(20);

        produto1.vender(3);

        System.out.println("\nApós as operações:");
        System.out.println(produto1);
        System.out.println(produto2);

    }
}
