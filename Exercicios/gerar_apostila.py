# -*- coding: utf-8 -*-
"""Gera a apostila PDF dos exercícios de OO."""

from pathlib import Path
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "Apostila_Exercicios_OO.pdf"
OUT_FALLBACK = ROOT / "Apostila_Exercicios_OO_atualizada.pdf"
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")
FONT_ITALIC = Path(r"C:\Windows\Fonts\ariali.ttf")


class Apostila(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("ArialBody", "I", 9)
        self.set_text_color(100, 100, 100)
        self.set_x(self.l_margin)
        self.cell(0, 8, "Apostila — Exercícios de Orientação a Objetos", align="L")
        self.ln(4)
        self.set_draw_color(180, 180, 180)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def footer(self):
        self.set_y(-15)
        self.set_font("ArialBody", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"{self.page_no()}", align="C")


def usable_width(pdf: FPDF) -> float:
    return pdf.w - pdf.l_margin - pdf.r_margin


def add_title(pdf: Apostila, text: str):
    pdf.set_font("ArialBody", "B", 18)
    pdf.set_text_color(25, 55, 95)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 10, text)
    pdf.ln(2)


def add_subtitle(pdf: Apostila, text: str):
    pdf.set_font("ArialBody", "B", 13)
    pdf.set_text_color(35, 75, 120)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 8, text)
    pdf.ln(1)


def add_heading(pdf: Apostila, text: str):
    pdf.set_font("ArialBody", "B", 11)
    pdf.set_text_color(40, 40, 40)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 7, text)
    pdf.ln(1)


def add_body(pdf: Apostila, text: str):
    pdf.set_font("ArialBody", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 5.5, text)
    pdf.ln(2)


def add_bullet(pdf: Apostila, text: str):
    pdf.set_font("ArialBody", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.set_x(pdf.l_margin)
    w = usable_width(pdf)
    pdf.cell(6, 5.5, "-")
    pdf.multi_cell(w - 6, 5.5, text)
    pdf.ln(0.5)


def add_pseudo(pdf: Apostila, lines: list[str]):
    pdf.set_fill_color(245, 247, 250)
    pdf.set_draw_color(200, 210, 220)
    pdf.set_font("ArialBody", "", 9)
    pdf.set_text_color(25, 35, 50)

    w = usable_width(pdf)
    line_h = 4.8
    height = len(lines) * line_h + 6
    if pdf.get_y() + height > pdf.h - pdf.b_margin:
        pdf.add_page()

    y0 = pdf.get_y()
    pdf.rect(pdf.l_margin, y0, w, height, style="DF")
    pdf.set_xy(pdf.l_margin + 3, y0 + 3)
    for line in lines:
        pdf.set_x(pdf.l_margin + 3)
        pdf.cell(w - 6, line_h, line)
        pdf.ln(line_h)
    pdf.set_xy(pdf.l_margin, y0 + height + 4)


def add_practice_banner(pdf: Apostila):
    pdf.set_fill_color(255, 243, 224)
    pdf.set_draw_color(230, 170, 80)
    pdf.set_font("ArialBody", "B", 10)
    pdf.set_text_color(120, 70, 10)
    w = usable_width(pdf)
    if pdf.get_y() + 12 > pdf.h - pdf.b_margin:
        pdf.add_page()
    y0 = pdf.get_y()
    pdf.rect(pdf.l_margin, y0, w, 10, style="DF")
    pdf.set_xy(pdf.l_margin + 3, y0 + 2.5)
    pdf.cell(w - 6, 5, "PARA VOCE RESOLVER — sem resolucao nesta apostila")
    pdf.set_xy(pdf.l_margin, y0 + 12)


def main():
    pdf = Apostila(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("ArialBody", "", str(FONT))
    pdf.add_font("ArialBody", "B", str(FONT_BOLD))
    pdf.add_font("ArialBody", "I", str(FONT_ITALIC))
    pdf.set_margins(18, 18, 18)

    # ---- Capa ----
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font("ArialBody", "B", 22)
    pdf.set_text_color(25, 55, 95)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 12, "Apostila de Exercícios", align="C")
    pdf.set_font("ArialBody", "B", 16)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(usable_width(pdf), 9, "Orientação a Objetos", align="C")
    pdf.ln(8)
    pdf.set_draw_color(25, 55, 95)
    mid = pdf.w / 2
    y = pdf.get_y()
    pdf.line(mid - 30, y, mid + 30, y)
    pdf.set_xy(pdf.l_margin, y + 10)
    pdf.set_font("ArialBody", "", 11)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        usable_width(pdf),
        6,
        "Para cada exercício resolvido, um exercício B do mesmo nível\n"
        "para praticar (sem resolução).\n"
        "Níveis: Livro/Filme → Produto/Ingresso → Conta/Funcionário.",
        align="C",
    )
    pdf.ln(20)
    pdf.set_x(pdf.l_margin)
    pdf.set_font("ArialBody", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(
        usable_width(pdf),
        6,
        "Material de apoio — conceitos de classes, métodos e herança",
        align="C",
    )

    # ---- Sumário ----
    pdf.add_page()
    add_title(pdf, "Sumário")
    add_body(
        pdf,
        "1. Conceitos usados nestes exercícios\n"
        "2. Exercício 1 — Classe Livro (com resolução)\n"
        "3. Exercício 1B — Classe Filme (para você resolver)\n"
        "4. Exercício 2 — Classe Produto (com resolução)\n"
        "5. Exercício 2B — Classe Ingresso (para você resolver)\n"
        "6. Exercício 3 — Conta Bancária (com resolução)\n"
        "7. Exercício 3B — Funcionário (para você resolver)\n"
        "8. Observações finais",
    )
    add_body(
        pdf,
        "Como usar: estude o exercício com resolução (pseudocódigo) e, em seguida, "
        "tente sozinho o exercício B do mesmo nível — sem olhar a resolução do anterior "
        "como “cola”, só como referência de forma.",
    )

    # ---- Conceitos ----
    add_title(pdf, "1. Conceitos usados nestes exercícios")
    add_body(
        pdf,
        "Antes das resoluções, vale lembrar os pilares aplicados nos exercícios:",
    )
    add_bullet(pdf, "Classe: modelo que define atributos (dados) e métodos (comportamentos).")
    add_bullet(pdf, "Objeto: instância concreta de uma classe.")
    add_bullet(pdf, "Encapsulamento: controlar o acesso aos dados (ex.: getters/setters).")
    add_bullet(pdf, "Validação: o método protege o estado do objeto (estoque, saldo, percentual).")
    add_bullet(pdf, "Herança: uma subclasse reutiliza e especializa uma classe base.")
    add_bullet(pdf, "Sobrescrita: a subclasse redefine um método herdado com nova lógica.")
    add_body(
        pdf,
        "Ordem sugerida de estudo: Livro (1 método) → Produto (vários métodos e regras) "
        "→ Conta Bancária (herança e sobrescrita).",
    )
    pdf.ln(2)

    # ---- Exercício 1 ----
    pdf.add_page()
    add_title(pdf, "2. Exercício 1 — Classe Livro")
    add_subtitle(pdf, "2.1 Enunciado")
    add_body(pdf, "Elabore uma classe Livro com os seguintes atributos:")
    add_bullet(pdf, "titulo")
    add_bullet(pdf, "autor")
    add_bullet(pdf, "anoPublicacao")
    add_bullet(pdf, "preco")
    add_body(
        pdf,
        "E o método aplicarDesconto(), que recebe o percentual de desconto e atualiza "
        "o preço do livro.",
    )

    add_subtitle(pdf, "2.2 Resolução em pseudocódigo")
    add_heading(pdf, "Classe Livro")
    add_pseudo(
        pdf,
        [
            "CLASSE Livro",
            "    ATRIBUTOS PRIVADOS:",
            "        titulo        : texto",
            "        autor         : texto",
            "        anoPublicacao : inteiro",
            "        preco         : numero",
            "",
            "    CONSTRUTOR(titulo, autor, anoPublicacao, preco)",
            "        this.titulo        <- titulo",
            "        this.autor         <- autor",
            "        this.anoPublicacao <- anoPublicacao",
            "        this.preco         <- preco",
            "",
            "    FUNCAO getTitulo()        RETORNA titulo",
            "    FUNCAO getAutor()         RETORNA autor",
            "    FUNCAO getAnoPublicacao() RETORNA anoPublicacao",
            "    FUNCAO getPreco()         RETORNA preco",
            "    PROCEDIMENTO setPreco(novoPreco)",
            "        preco <- novoPreco",
            "",
            "    PROCEDIMENTO aplicarDesconto(percentual)",
            "        SE percentual < 0 OU percentual > 100 ENTAO",
            "            ESCREVER \"Percentual invalido (use 0 a 100)\"",
            "            RETORNAR",
            "        FIM SE",
            "        desconto <- preco * (percentual / 100)",
            "        preco    <- preco - desconto",
            "",
            "    FUNCAO paraTexto()",
            "        RETORNA \"Livro{titulo, autor, anoPublicacao, preco}\"",
            "FIM CLASSE",
        ],
    )

    add_heading(pdf, "Programa de teste")
    add_pseudo(
        pdf,
        [
            "INICIO",
            "    livro1 <- NOVO Livro(\"O Senhor dos Aneis\", \"J.R.R. Tolkien\", 1954, 100)",
            "    livro2 <- NOVO Livro(\"1984\", \"George Orwell\", 1949, 80)",
            "",
            "    ESCREVER \"Antes do desconto:\"",
            "    ESCREVER livro1.paraTexto()",
            "    ESCREVER livro2.paraTexto()",
            "",
            "    livro1.aplicarDesconto(10)   // 10%",
            "    livro2.aplicarDesconto(20)   // 20%",
            "",
            "    ESCREVER \"Apos o desconto:\"",
            "    ESCREVER livro1.paraTexto()",
            "    ESCREVER livro2.paraTexto()",
            "FIM",
        ],
    )

    add_heading(pdf, "Resultado esperado (exemplo)")
    add_body(
        pdf,
        "livro1: preço 100 com 10% de desconto → 90\n"
        "livro2: preço 80 com 20% de desconto → 64",
    )

    # ---- Exercício 1B (mesmo nível, sem resolução) ----
    pdf.add_page()
    add_title(pdf, "3. Exercício 1B — Classe Filme")
    add_practice_banner(pdf)
    add_body(
        pdf,
        "Mesmo nível do Exercício 1 (Livro): uma classe, atributos simples e um método "
        "principal que altera o preço.",
    )
    add_subtitle(pdf, "3.1 Enunciado")
    add_body(pdf, "Elabore uma classe Filme com os seguintes atributos:")
    add_bullet(pdf, "titulo")
    add_bullet(pdf, "diretor")
    add_bullet(pdf, "anoLancamento")
    add_bullet(pdf, "preco")
    add_body(
        pdf,
        "E o método aplicarDesconto(), que recebe como parâmetro o percentual de desconto "
        "e atualiza o preço do filme. Valide se o percentual está entre 0 e 100.",
    )
    add_body(
        pdf,
        "Crie um programa de teste que:\n"
        "- Crie pelo menos dois filmes\n"
        "- Mostre os dados antes do desconto\n"
        "- Aplique descontos diferentes em cada filme\n"
        "- Mostre os dados depois do desconto",
    )

    # ---- Exercício 2 (intermediário) ----
    pdf.add_page()
    add_title(pdf, "4. Exercício 2 — Classe Produto")
    add_subtitle(pdf, "4.1 Enunciado")
    add_body(
        pdf,
        "Este exercício fica entre Livro e Conta Bancária: ainda sem herança, "
        "mas com mais de um método e regras que protegem o estado do objeto.",
    )
    add_body(pdf, "Elabore uma classe Produto com os seguintes atributos:")
    add_bullet(pdf, "nome")
    add_bullet(pdf, "preco")
    add_bullet(pdf, "quantidadeEstoque")
    add_body(pdf, "E os seguintes métodos:")
    add_bullet(pdf, "reporEstoque(quantidade) — aumenta a quantidade em estoque")
    add_bullet(
        pdf,
        "vender(quantidade) — diminui o estoque (não pode vender mais do que existe)",
    )
    add_bullet(
        pdf,
        "aplicarDesconto(percentual) — recebe o percentual e atualiza o preço",
    )
    add_body(
        pdf,
        "Crie um programa de teste que: crie pelo menos dois produtos, repoha estoque, "
        "venda unidades, aplique desconto e mostre os dados antes e depois.",
    )

    add_subtitle(pdf, "4.2 Resolução em pseudocódigo")
    add_heading(pdf, "Classe Produto")
    add_pseudo(
        pdf,
        [
            "CLASSE Produto",
            "    ATRIBUTOS PRIVADOS:",
            "        nome               : texto",
            "        preco              : numero",
            "        quantidadeEstoque  : inteiro",
            "",
            "    CONSTRUTOR(nome, preco, quantidadeEstoque)",
            "        this.nome              <- nome",
            "        this.preco             <- preco",
            "        this.quantidadeEstoque <- quantidadeEstoque",
            "",
            "    FUNCAO getNome()              RETORNA nome",
            "    FUNCAO getPreco()             RETORNA preco",
            "    FUNCAO getQuantidadeEstoque() RETORNA quantidadeEstoque",
            "    PROCEDIMENTO setPreco(novoPreco)",
            "        preco <- novoPreco",
            "",
            "    PROCEDIMENTO reporEstoque(quantidade)",
            "        SE quantidade <= 0 ENTAO",
            "            ESCREVER \"Quantidade para reposicao invalida.\"",
            "            RETORNAR",
            "        FIM SE",
            "        quantidadeEstoque <- quantidadeEstoque + quantidade",
            "        ESCREVER \"Estoque reposto. Quantidade atual: \" + quantidadeEstoque",
            "",
            "    PROCEDIMENTO vender(quantidade)",
            "        SE quantidade <= 0 ENTAO",
            "            ESCREVER \"Quantidade para venda invalida.\"",
            "            RETORNAR",
            "        FIM SE",
            "        SE quantidadeEstoque >= quantidade ENTAO",
            "            quantidadeEstoque <- quantidadeEstoque - quantidade",
            "            ESCREVER \"Venda realizada. Quantidade atual: \" + quantidadeEstoque",
            "        SENAO",
            "            ESCREVER \"Estoque insuficiente.\"",
            "        FIM SE",
            "",
            "    PROCEDIMENTO aplicarDesconto(percentual)",
            "        SE percentual < 0 OU percentual > 100 ENTAO",
            "            ESCREVER \"Percentual invalido (use 0 a 100)\"",
            "            RETORNAR",
            "        FIM SE",
            "        preco <- preco - preco * (percentual / 100)",
            "",
            "    FUNCAO paraTexto()",
            "        RETORNA \"Produto{nome, preco, quantidadeEstoque}\"",
            "FIM CLASSE",
        ],
    )

    add_heading(pdf, "Programa de teste")
    add_pseudo(
        pdf,
        [
            "INICIO",
            "    produto1 <- NOVO Produto(\"Caderno\", 25.0, 10)",
            "    produto2 <- NOVO Produto(\"Caneta\", 5.0, 50)",
            "",
            "    ESCREVER \"Antes das operacoes:\"",
            "    ESCREVER produto1.paraTexto()",
            "    ESCREVER produto2.paraTexto()",
            "",
            "    produto1.reporEstoque(5)     // estoque 10 -> 15",
            "    produto2.vender(10)          // estoque 50 -> 40",
            "",
            "    produto1.aplicarDesconto(10) // preco 25 -> 22.5",
            "    produto2.aplicarDesconto(20) // preco 5 -> 4",
            "",
            "    produto1.vender(3)           // estoque 15 -> 12",
            "",
            "    ESCREVER \"Apos as operacoes:\"",
            "    ESCREVER produto1.paraTexto()",
            "    ESCREVER produto2.paraTexto()",
            "FIM",
        ],
    )

    add_heading(pdf, "Por que este exercício é intermediário?")
    add_body(
        pdf,
        "Do Livro, reaproveita a ideia de aplicarDesconto.\n"
        "Da Conta Bancária, antecipa a ideia de validar uma operação "
        "(vender só se houver estoque — parecido com sacar só se houver saldo).\n"
        "Ainda não usa herança: o foco é vários métodos alterando o mesmo objeto com regras.",
    )

    # ---- Exercício 2B (mesmo nível, sem resolução) ----
    pdf.add_page()
    add_title(pdf, "5. Exercício 2B — Classe Ingresso")
    add_practice_banner(pdf)
    add_body(
        pdf,
        "Mesmo nível do Exercício 2 (Produto): uma classe com vários métodos e regras "
        "que protegem o estado (quantidade disponível e percentual válido). Sem herança.",
    )
    add_subtitle(pdf, "5.1 Enunciado")
    add_body(pdf, "Elabore uma classe Ingresso com os seguintes atributos:")
    add_bullet(pdf, "nomeEvento")
    add_bullet(pdf, "preco")
    add_bullet(pdf, "quantidadeDisponivel")
    add_body(pdf, "E os seguintes métodos:")
    add_bullet(
        pdf,
        "disponibilizar(quantidade) — aumenta a quantidade de ingressos disponíveis",
    )
    add_bullet(
        pdf,
        "vender(quantidade) — diminui a quantidade (não pode vender mais do que existe)",
    )
    add_bullet(
        pdf,
        "aplicarDesconto(percentual) — recebe o percentual e atualiza o preço",
    )
    add_body(
        pdf,
        "Crie um programa de teste que:\n"
        "- Crie pelo menos dois ingressos (dois eventos)\n"
        "- Disponibilize mais unidades\n"
        "- Venda algumas unidades\n"
        "- Aplique desconto\n"
        "- Mostre os dados antes e depois das operações",
    )

    # ---- Exercício 3 ----
    pdf.add_page()
    add_title(pdf, "6. Exercício 3 — Conta Bancária")
    add_subtitle(pdf, "6.1 Enunciado")
    add_body(
        pdf,
        "Elabore uma classe ContaBancaria com os atributos nomeCliente, numConta e saldo, "
        "e os métodos sacar (o saldo não pode ficar negativo) e depositar.",
    )
    add_body(pdf, "Crie também duas subclasses:")
    add_bullet(
        pdf,
        "ContaPoupanca — com taxa de juros e método para aplicar rendimento ao saldo.",
    )
    add_bullet(
        pdf,
        "ContaEspecial — com limite e método sacar sobrescrito (permite usar o limite).",
    )
    add_body(
        pdf,
        "Em um programa de teste: criar contas, sacar, depositar, aplicar rendimento "
        "e mostrar os dados do cliente.",
    )

    add_subtitle(pdf, "6.2 Resolução em pseudocódigo")
    add_heading(pdf, "Classe base ContaBancaria")
    add_pseudo(
        pdf,
        [
            "CLASSE ContaBancaria",
            "    ATRIBUTOS:",
            "        nomeCliente : texto",
            "        numeroConta : texto",
            "        saldo       : numero",
            "",
            "    CONSTRUTOR(nomeCliente, numeroConta, saldo)",
            "        this.nomeCliente <- nomeCliente",
            "        this.numeroConta <- numeroConta",
            "        this.saldo       <- saldo",
            "",
            "    // getters e setters para cada atributo",
            "",
            "    PROCEDIMENTO depositar(valor)",
            "        saldo <- saldo + valor",
            "",
            "    PROCEDIMENTO sacar(valor)",
            "        SE saldo >= valor ENTAO",
            "            saldo <- saldo - valor",
            "            ESCREVER \"Saque realizado. Saldo atual: \" + saldo",
            "        SENAO",
            "            ESCREVER \"Saldo insuficiente.\"",
            "        FIM SE",
            "FIM CLASSE",
        ],
    )

    add_heading(pdf, "Subclasse ContaPoupanca")
    add_pseudo(
        pdf,
        [
            "CLASSE ContaPoupanca HERDA ContaBancaria",
            "    ATRIBUTO:",
            "        taxaJuros : numero   // percentual, ex.: 1.0 = 1%",
            "",
            "    CONSTRUTOR(nomeCliente, numeroConta, saldo, taxaJuros)",
            "        CHAMAR construtor da superclasse(nomeCliente, numeroConta, saldo)",
            "        this.taxaJuros <- taxaJuros",
            "",
            "    PROCEDIMENTO aplicarRendimento()",
            "        rendimento <- saldo * (taxaJuros / 100)",
            "        depositar(rendimento)",
            "        ESCREVER \"Rendimento: \" + rendimento + \" | Saldo: \" + saldo",
            "FIM CLASSE",
        ],
    )

    add_heading(pdf, "Subclasse ContaEspecial")
    add_pseudo(
        pdf,
        [
            "CLASSE ContaEspecial HERDA ContaBancaria",
            "    ATRIBUTO:",
            "        limite : numero",
            "",
            "    CONSTRUTOR(nomeCliente, numeroConta, saldo, limite)",
            "        CHAMAR construtor da superclasse(nomeCliente, numeroConta, saldo)",
            "        this.limite <- limite",
            "",
            "    // SOBRESCRITA do metodo sacar",
            "    PROCEDIMENTO sacar(valor)",
            "        SE (saldo + limite) >= valor ENTAO",
            "            saldo <- saldo - valor",
            "            ESCREVER \"Saque realizado. Saldo atual: \" + saldo",
            "            // saldo pode ficar negativo ate -limite",
            "        SENAO",
            "            ESCREVER \"Saldo insuficiente.\"",
            "        FIM SE",
            "FIM CLASSE",
        ],
    )

    pdf.add_page()
    add_heading(pdf, "Programa de teste (lógica sugerida)")
    add_pseudo(
        pdf,
        [
            "INICIO",
            "    // Criar contas",
            "    poupanca <- NOVO ContaPoupanca(\"Ana\", \"001\", 1000, 1.0)",
            "    especial <- NOVO ContaEspecial(\"Bruno\", \"002\", 500, 300)",
            "",
            "    // Sacar",
            "    poupanca.sacar(200)     // saldo -> 800",
            "    especial.sacar(700)     // usa limite; saldo -> -200",
            "",
            "    // Depositar",
            "    poupanca.depositar(50)  // saldo -> 850",
            "    especial.depositar(100) // saldo -> -100",
            "",
            "    // Rendimento da poupanca",
            "    poupanca.aplicarRendimento()  // +1% sobre 850",
            "",
            "    // Mostrar dados",
            "    ESCREVER poupanca.nomeCliente, poupanca.numeroConta, poupanca.saldo",
            "    ESCREVER especial.nomeCliente, especial.numeroConta, especial.saldo,",
            "             especial.limite",
            "FIM",
        ],
    )

    add_heading(pdf, "Diferença importante no saque")
    add_body(
        pdf,
        "Na conta comum, só é possível sacar até o valor do saldo.\n"
        "Na conta especial, o cliente pode sacar até saldo + limite. "
        "Por isso o saldo pode ficar negativo, desde que não ultrapasse o limite combinado.",
    )

    # ---- Exercício 3B (mesmo nível, sem resolução) ----
    pdf.add_page()
    add_title(pdf, "7. Exercício 3B — Funcionário (herança)")
    add_practice_banner(pdf)
    add_body(
        pdf,
        "Mesmo nível do Exercício 3 (Conta Bancária): classe base + duas subclasses, "
        "com sobrescrita de método.",
    )
    add_subtitle(pdf, "7.1 Enunciado")
    add_body(
        pdf,
        "Elabore uma classe Funcionario com os atributos nome e salarioBase, "
        "e o método calcularSalario(), que retorna o salarioBase.",
    )
    add_body(pdf, "Crie também duas subclasses:")
    add_bullet(
        pdf,
        "Gerente — atributo bonus; sobrescreva calcularSalario para retornar "
        "salarioBase + bonus.",
    )
    add_bullet(
        pdf,
        "Vendedor — atributos comissao (percentual) e totalVendas; sobrescreva "
        "calcularSalario para retornar salarioBase + (totalVendas * comissao / 100).",
    )
    add_body(
        pdf,
        "Crie um programa de teste que:\n"
        "- Crie um gerente e um vendedor\n"
        "- Mostre o salário calculado de cada um\n"
        "- Altere bonus ou totalVendas e mostre o novo salário\n"
        "- Exiba os dados de cada funcionário",
    )

    # ---- Observações ----
    pdf.add_page()
    add_title(pdf, "8. Observações finais")
    add_bullet(
        pdf,
        "O pseudocódigo descreve a lógica, sem sintaxe específica de Java (ou outra linguagem).",
    )
    add_bullet(
        pdf,
        "Cada exercício com resolução tem um exercício B do mesmo nível, sem resolução — "
        "para praticar sozinho.",
    )
    add_bullet(
        pdf,
        "1/1B: uma classe e um método principal (preço + desconto).",
    )
    add_bullet(
        pdf,
        "2/2B: vários métodos e validação de quantidade/estoque.",
    )
    add_bullet(
        pdf,
        "3/3B: herança e sobrescrita de método.",
    )
    add_bullet(
        pdf,
        "Na Conta, a herança evita repetir código; em ContaEspecial.sacar, o mesmo nome "
        "de método tem comportamento diferente — polimorfismo.",
    )
    pdf.ln(4)
    add_body(
        pdf,
        "Fim da apostila. Estude a resolução, resolva o exercício B, e só depois "
        "passe para o código Java.",
    )

    candidates = [
        OUT,
        OUT_FALLBACK,
        ROOT / "Apostila_Exercicios_OO_v3.pdf",
    ]
    last_error = None
    for path in candidates:
        try:
            pdf.output(str(path))
            print(f"Gerado: {path}")
            break
        except PermissionError as exc:
            last_error = exc
    else:
        raise last_error


if __name__ == "__main__":
    main()
