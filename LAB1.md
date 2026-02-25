# PUC-SP - Computer Science
## Compilers
### LAB 1 - Lex regexp scanner

A **fase 1** de um compilador, chamada **análise léxica** (ou **scanner** / analisador léxico), é a primeira etapa do processo de compilação e tem como objetivo principal ler o programa-fonte caractere por caractere (fluxo de entrada) e agrupá-los em unidades mínimas com significado na linguagem, chamadas **tokens** (ex.: identificador, palavra reservada `if`, número inteiro, operador `+`, etc.), eliminando espaços em branco, comentários e outros elementos irrelevantes como comentários. Essa tarefa é normalmente implementada por meio de um **autômato finito determinístico** (ou não-determinístico convertido para determinístico), que reconhece padrões de strings descritos por **expressões regulares** — que, por sua vez, correspondem exatamente às linguagens regulares definidas por **gramáticas regulares** (tipo 3 na hierarquia de Chomsky). Assim, o scanner usa tabelas de transição (baseadas no autômato) para decidir rapidamente quando um lexema termina e qual token ele representa, passando essa sequência limpa e classificada para o analisador sintático da próxima fase. [X Grok AI LLM - Editado]

Ler cap 1 do livro do dragão.
