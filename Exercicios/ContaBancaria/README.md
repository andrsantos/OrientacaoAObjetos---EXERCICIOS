# Conta Bancária

Exercício de herança e sobrescrita de métodos em Java.

## Classe `ContaBancaria`

Atributos:
- `nomeCliente`
- `numeroConta`
- `saldo`

Métodos:
- `depositar(valor)` — adiciona o valor ao saldo
- `sacar(valor)` — debita o valor se houver saldo suficiente (saldo não fica negativo); caso contrário, exibe mensagem de saldo insuficiente

Também possui construtor e getters/setters para os atributos.

## Subclasse `ContaPoupanca`

Estende `ContaBancaria`.

Atributo:
- `taxaJuros`

Método:
- `aplicarRendimento()` — calcula o rendimento com base no saldo e em `taxaJuros` (percentual), deposita o valor e exibe o rendimento e o saldo atual

## Subclasse `ContaEspecial`

Estende `ContaBancaria`.

Atributo:
- `limite`

Método:
- `sacar(valor)` — sobrescrito: permite saque enquanto `saldo + limite` for suficiente

## Classe `App`

Por enquanto contém apenas o `main` padrão (`Hello, World!`). Ainda não há demonstração de criação de contas, saque, depósito e rendimento.
