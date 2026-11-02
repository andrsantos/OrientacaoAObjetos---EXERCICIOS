public class App {
    public static void main(String[] args) throws Exception {

        Livro livro1 = new Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 100);
        Livro livro2 = new Livro("1984", "George Orwell", 1949, 80);

        System.out.println("Antes do desconto:");
        System.out.println(livro1);
        System.out.println(livro2);

        livro1.aplicarDesconto(10); 
        livro2.aplicarDesconto(20); 

        System.out.println("\nApós o desconto:");
        System.out.println(livro1);
        System.out.println(livro2);
    
    }
}
