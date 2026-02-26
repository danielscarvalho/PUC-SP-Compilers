# PUC-SP - Computer Science
## Compilers
### LAB 1 - Lex regexp scanner

A **fase 1** de um compilador, chamada **análise léxica** (ou **scanner** / analisador léxico), é a primeira etapa (de 6 etapas) do processo de compilação e tem como objetivo principal ler o programa-fonte caractere por caractere (fluxo de entrada) e agrupá-los em unidades mínimas com significado na linguagem, chamadas **tokens** (ex.: identificador, palavra reservada `if`, número inteiro, operador `+`, etc.), eliminando tabs (identação), espaços em branco, comentários e outros elementos irrelevantes. Essa tarefa é normalmente implementada por meio de um **autômato finito determinístico** (ou não-determinístico convertido para determinístico), que reconhece padrões de strings descritos por **expressões regulares** — que, por sua vez, correspondem exatamente às linguagens regulares definidas por **gramáticas regulares** (tipo 3 na hierarquia de Chomsky). Assim, o scanner usa tabelas de transição (baseadas no autômato) para decidir rapidamente quando um lexema termina e qual token ele representa, passando essa sequência limpa e classificada para o analisador sintático da próxima fase. [X Grok AI LLM - Editado]

Ler cap. 1 do livro do dragão.

Atividades:

- Bash - Prompt do Linux Ubuntu - Loop infinito do terminal - Conceitos básicos de comandos do Linux no terminal
- RegExp - https://regexr.com/ - Regexp para reconhecer e-mails, números, telefones e outros padrões...
- RegExp - https://regex101.com/ - Regexp para reconhecer e-mails, números, telefones e outros padrões...
- Find replace em editores de texto com regex, útil para processar arquivos de dados
- RegExp - em Java e Python
- OpenAI tokenizer - https://platform.openai.com/tokenizer (é um pouco diferente dos tokens de compiladores que seguem a gramática da linguagem de programação)
- JFLAP - https://www.jflap.org/tutorial/ - Automatos Finitos e regex
- Google Colab - https://colab.research.google.com/ - Regexp com Python
- Criar analisador léxico - Scanner - 1 fase de compilação (análise) para quebrar texto em língua portuguesa em uma lista de tokens

**Fase 1 de Compiladores (Análise Léxica / Scanner)**: Capítulo 1 do Livro do Dragão 

**Objetivo do LAB**  
Após ler o Capítulo 1 (especialmente a seção 1.2.1 – Lexical Analysis), vamos **vivenciar na prática** o que o livro explica: o scanner lê o fluxo de caracteres (`character stream`), agrupa em lexemas e gera tokens (exemplo clássico da página 6: `position = initial + rate * 60`).

### Preparação (material para o LAB)
- Ler **Capítulo 1 completo** do Livro do Dragão (foco em 1.2.1 Lexical Analysis + Figura 1.7).
- PC desktop ou notebook com Ubuntu 22.04/24.04 ou VM Ubuntu + internet, ou no Windows 10 ou 11 no WSL2.

### LAB – ~4 horas (pode ser dividido em 2 sessões/aulas)

#### **Atividade 1 – Bash no Terminal Ubuntu: Simulando o “fluxo de entrada” do Scanner** (30 min)
**Objetivo:** Entender o conceito de *character stream* que o livro menciona.  
**Professor demonstra no projetor:**
Experimentar comandos básicos do Linux no terminal e visão geral de como o Bash funciona.<br>
Como criar scripts executáveis no Linux.
```bash
while true; do
    read -r linha
    echo "[SCANNER] Linha recebida: '$linha'"
    # aqui virá o processamento léxico depois
done
```
**Etapas:**
1. Criar arquivo `scanner_simples.sh`
2. Fazer loop infinito que lê linhas de um arquivo `exemplo.c` (fornecido pelo professor com o exemplo do livro + comentários).
3. Adicionar `tr -d ' \t\r'` para remover espaços em branco (pré-processamento típico do scanner).
4. Testar com `cat exemplo.c | ./scanner_simples.sh`

**Conexão com o livro:** “The lexical analyzer reads the stream of characters...” (p. 6).

#### **Atividade 2 – Expressões Regulares online (regexr + regex101)** (45 min)
**Objetivo:** Ver na prática que tokens são definidos por **expressões regulares** (base do scanner).

**Passo a passo (alunos + professor juntos):**
1. Acessar **https://regexr.com/** e **https://regex101.com/**
2. Usar o texto do livro:
   ```
   position = initial + rate * 60
   ```
3. Criar regex para cada token:
   - Identificador: `[a-zA-Z_][a-zA-Z0-9_]*`
   - Número inteiro: `\d+`
   - Operadores: `[=+\-*]`
   - Ignorar espaços: `\s+`
4. Testar flags `/g` e modo “global”.
5. Desafio: criar uma única regex que capture **todos** os tokens do exemplo do livro em um array.
6. Criar e experimentar regexp para reconhecer e-mail, CEP, CPF, RG, telefone, etc...

**Entrega (Evidência):** Printscreen da tela com regex funcionando + explicação de 3 linhas.

#### **Atividade 3 – Find/Replace com regex em editores de texto** (20 min)
**Objetivo:** Mostrar aplicação real de regex fora de compiladores (processamento de dados).

**Ferramentas:** MS VS Code, vi ou gedit (modo regex ativado).
**Exercícios:**
- Remover todos os comentários `//` e `/* */` de um arquivo grande.
- Substituir todos os `=` por `:=` (simulando mudança de linguagem).
- Limpar espaços extras em um arquivo CSV de 10 mil linhas.
- Tornar um CSV em um TSV
- CSV com dados em português para inglês, trocar `,` -> `.` e `,` -> `;`

**Conexão:** O scanner faz exatamente isso em tempo de compilação.

#### **Atividade 4 – RegExp em Python e Java (Google Colab + Eclipse/IntelliJ)** (60 min)
**Objetivo:** Implementar um mini-scanner de verdade, lembrando que o scanner é um autômato finito.

**Python (Google Colab – https://colab.research.google.com/):**
```python
import re

codigo = "position = initial + rate * 60"
tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*]', codigo)
print(tokens)
```

Usar biblioteca do Python `requests` para ler conteúdo texto de página WEB e extrair e-mails com regexp...

**Alunos evoluem para:**
- Função `tokenize(texto)` que retorna lista de tuplas `(tipo, lexema)` (ex: `('ID', 'position')`, `('OP', '=')`).

**Java (mesma lógica):**
Usar `java.util.regex.Pattern` e `Matcher` com grupos nomeados.

**Desafio final (30 min):** Tokenizar o exemplo completo do livro e imprimir exatamente como na Figura 1.7 do Dragon Book.

#### **Atividade 5 – Autômatos Finitos com JFLAP** (50 min)
**Objetivo:** Ver o “motor” por trás do scanner (autômato finito).

**Link:** https://www.jflap.org/tutorial/

**Passo a passo guiado pelo professor:**
1. Criar DFA para reconhecer **números inteiros**.
2. Criar DFA para **identificadores**.
3. Criar NFA para operador `=` e `==` (ambiguidade).
4. Converter NFA → DFA (ferramenta automática do JFLAP).
5. Simular passo a passo com a string do livro.

**Conexão com o livro:** Capítulo 1 introduz o conceito; Capítulo 3 aprofunda (autômatos finitos são a implementação real do scanner).

#### **Atividade 6 – OpenAI Tokenizer × Tokens de Compilador** (30 min + discussão)
**Link:** https://platform.openai.com/tokenizer (ou tiktoken no Colab)

**Atividade:**
1. Colar o exemplo do livro no tokenizer da OpenAI.
2. Comparar os “tokens” gerados com os tokens léxicos que criamos nas atividades anteriores.
3. Responder em grupo:
   - Por que o tokenizer da OpenAI quebra `position` em `pos` + `ition`?
   - Qual é a diferença conceitual entre **token léxico** (segue gramática regular da linguagem) e **token de LLM** (BPE – Byte Pair Encoding)?

**Discussão final em plenária (15 min):** “Por que o scanner de compilador precisa ser preciso e seguir a gramática, enquanto o da OpenAI não?”

#### **Atividade 6 – Tokenizar livro em português (Criar analisador léxico, scanner)** (30 min + duplas)

**Atividade:**
1. Baixar livro .txt UTF-8, à escolha da equipe, do Project Gutenberg. https://www.gutenberg.org/
2. Criar programa em Python, scanner, usando regexp para quebrar em tokens o texto do livro conforme a gramática da língua portuguesa
3. A entrada (input) é um arquivo texto, a saída (output) é um vetor (lista) de strings, exemplo: `["Do", "título", ".", "Uma", "noite", "destas", ",", "vindo", "da", "cidade", "para", "o", "Engenho", "Novo", ",", "encontrei", "no", "trem", "da", "Central", "um", "rapaz", "aqui", "do", "bairro", ",", "que", "eu", "conheço", "de", "vista", "e", "de", "chapéo", ".", "Comprimentou-me", ",", "sentou-se", "ao", "pé", "de", "mim", ",", ...]`<br>
Note que ainda não estamos identificando o tipo dos tokens: verbo, adjetivo, pontuação, pronome, etc...
4. Realizar a mesma implementação em Java
5. O programa em Python e Java deve ser bem documentado
6. Subir no repo do GitHub desta atividade o arquivo do livro e o output (saída) vetor (lista), código-fonte, e todos os recursos usado no projeto/LAB

> Todas estas atividades devem ser entregues no mesmo repo do GitHub<br>
> Subir todos os arquivos de input e output utilizados, código fonte, .md, etc...

### Atividade Extra - Analisador léxico da língua portuguesa

Usando AI LLM, pedir o seguinte prompt: <br>
"Criar um programa em Python, analisador léxico - scanner,  para quebrar em tokens uma string com um livro, conforme as regras da língua portuguesa. Devolver uma lista de tuplas, o primeiro item é o token, e o segundo item é o tipo: pontuação, verbo, artigo, pronome, objeto, etc... Tokens não identificados retorne '??'"

Teste o programa criado por IA com o livro.

### Entrega final do Lab (em duplas - pairing)
- Link do relatório em MD no GitHub com:
  - Identificação: faculdade, curso, disciplina, LAB, alunos
  - Printscreen de todas as atividades
  - Código Python + Java funcionando
  - Captura das telas do JFLAP
  - Resposta da comparação OpenAI
  - Uma frase de cada aluno: “O que há de interessante no analisador léxico (scanner), automato finito”
  - Texto em MD explicando/documentação as atividades realizadas...
    
Referência - extra:

<img width="1400" height="788" alt="image" src="https://github.com/user-attachments/assets/00a5b168-bc93-408e-a868-240d8ea17f9c" />
<br>
<img width="1626" height="1134" alt="image" src="https://github.com/user-attachments/assets/30ce03e5-c6ec-4838-924b-b0674b9ccdbc" />
<br>
<img width="300" height="394" alt="image" src="https://github.com/user-attachments/assets/e84b37d3-4976-4a3d-a5a1-5788557296a3" />

