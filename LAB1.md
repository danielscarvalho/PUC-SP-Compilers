# PUC-SP - Computer Science
## Compilers
### LAB 1 - Lex regexp scanner

A **fase 1** de um compilador, chamada **análise léxica** (ou **scanner** / analisador léxico), é a primeira etapa (de 6 etapas) do processo de compilação e tem como objetivo principal ler o programa-fonte caractere por caractere (fluxo de entrada) e agrupá-los em unidades mínimas com significado na linguagem, chamadas **tokens** (ex.: identificador, palavra reservada `if`, número inteiro, operador `+`, etc.), eliminando tabs (identação), espaços em branco, comentários e outros elementos irrelevantes. Essa tarefa é normalmente implementada por meio de um **autômato finito determinístico** (ou não-determinístico convertido para determinístico), que reconhece padrões de strings descritos por **expressões regulares** — que, por sua vez, correspondem exatamente às linguagens regulares definidas por **gramáticas regulares** (tipo 3 na hierarquia de Chomsky). Assim, o scanner usa tabelas de transição (baseadas no autômato) para decidir rapidamente quando um lexema termina e qual token ele representa, passando essa sequência limpa e classificada para o analisador sintático da próxima fase. [X Grok AI LLM - Editado]

Ler cap. 1 do livro do dragão.

- Bash - Prompt do Linux Ubuntu - Loop infinito do terminal
- RegExp - https://regexr.com/
- RegExp - https://regex101.com/
- OpenAI tokenizer - https://platform.openai.com/tokenizer (é um pouco diferente dos tokens de compiladores que seguem a gramática da linguagem de programação)
- JFLAP - https://www.jflap.org/tutorial/
- Google Colab - https://colab.research.google.com/
- 
  
Referência - extra:

<img width="1400" height="788" alt="image" src="https://github.com/user-attachments/assets/00a5b168-bc93-408e-a868-240d8ea17f9c" />
<br>
<img width="1626" height="1134" alt="image" src="https://github.com/user-attachments/assets/30ce03e5-c6ec-4838-924b-b0674b9ccdbc" />
