# Desafios de Programação em Python 🐍

Este repositório contém três exercícios práticos focados em lógica de programação e estruturas de dados fundamentais (Pilhas e Filas). Cada script simula uma situação do mundo real no terminal.

---

## 📂 Desafio 1: Sistema de Votação (`desafio_01_votacao.py`)

**1. Qual problema o programa resolve:**
O programa simula uma urna eletrônica simples. Ele permite contabilizar votos para três candidatos predefinidos (Ana, Bruno e Carlos) de forma contínua até que a votação seja encerrada, exibindo o total de votos de cada um e o grande vencedor.

**2. Quais estruturas foram utilizadas:**
* Laço de repetição (`while True`) para manter a votação aberta.
* Estruturas condicionais (`if/elif/else`) para validar e contabilizar os votos.
* Variáveis acumuladoras de inteiros para a contagem.
* Manipulação de strings (`capitalize()`) para padronizar a entrada do usuário.

**3. Como executar o programa:**
No terminal, navegue até a pasta onde o arquivo está salvo e digite:
> `python desafio_01_votacao.py`

**4. Exemplo simples de entrada e saída:**
* **Entrada:** `ana`, `bruno`, `ana`, `fim`
* **Saída:**
    ```text
    Resultados da votação
    Totais: Ana: 2
     Bruno: 1
     Carlos: 0
    Ana venceu!
    ```

---

## 📂 Desafio 2: Editor de Texto com Pilha (`desafio_02_editor_pilha.py`)

**1. Qual problema o programa resolve:**
Simula a funcionalidade básica de um editor de texto com a opção de "Desfazer" (Ctrl+Z). O usuário pode digitar palavras que vão compondo um texto, e caso digite algo errado, pode remover a última palavra inserida.

**2. Quais estruturas foram utilizadas:**
* **Pilha (Stack):** Implementada através de uma lista padrão do Python usando o conceito **LIFO** (Last In, First Out - O último a entrar é o primeiro a sair) através dos métodos `.append()` e `.pop()`.
* Laço de repetição (`while True`) para o menu iterativo.
* Estrutura de decisão condicional (`match/case`) para navegar pelas opções do menu.

**3. Como executar o programa:**
No terminal, navegue até a pasta onde o arquivo está salvo e digite:
> `python desafio_02_editor_pilha.py`

**4. Exemplo simples de entrada e saída:**
* **Entradas no menu:**
    * Opção `1` -> Digita: `Olá`
    * Opção `1` -> Digita: `Mundo`
    * Opção `2` (Desfazer)
    * Opção `3` (Mostrar texto)
* **Saídas correspondentes:**
    ```text
    Palavra adicionada: Olá
    Palavra adicionada: Mundo
    Palavra removida: Mundo
    Texto atual: Olá
    ```

---

## 📂 Desafio 3: Fila de Atendimento (`desafio_03_fila_atendimento.py`)

**1. Qual problema o programa resolve:**
Gerencia o fluxo de atendimento em uma Secretaria Acadêmica. Ele permite adicionar alunos a uma fila de espera, chamar o próximo aluno para atendimento seguindo a ordem de chegada, e visualizar como a fila está no momento.

**2. Quais estruturas foram utilizadas:**
* **Fila (Queue):** Implementada através de uma lista padrão do Python usando o conceito **FIFO** (First In, First Out - O primeiro a entrar é o primeiro a sair) através dos métodos `.append()` e `.pop(0)`.
* Laço de repetição (`while True`) acoplado com a função `enumerate()` para gerar os menus e listas numeradas.
* Estrutura de decisão condicional (`match/case`) para processar a escolha do usuário.

**3. Como executar o programa:**
No terminal, navegue até a pasta onde o arquivo está salvo e digite:
> `python desafio_03_fila_atendimento.py`

**4. Exemplo simples de entrada e saída:**
* **Entradas no menu:**
    * Opção `1` -> Nome: `João`
    * Opção `1` -> Nome: `Maria`
    * Opção `3` (Mostrar fila)
    * Opção `2` (Chamar próximo)
* **Saídas correspondentes:**
    ```text
    João entrou na fila de atendimento
    Maria entrou na fila de atendimento
    Fila Atual:
    1 - João
    2 - Maria
    Chamando Aluno: João
    ```
