# PUC-SP - Computer Science
## Compilers
### LAB 2 - Parser - automato com pilha - gramática livre de contexto

A fase 2 de um compilador (de 6 fases) e ainda em análise, conhecida como análise sintática (ou parsing), recebe a sequência de tokens gerada pelo analisador léxico e verifica se eles formam uma estrutura válida de acordo com a gramática livre de contexto (context-free grammar) da linguagem de programação, construindo uma representação hierárquica como a árvore de análise (parse tree) ou a árvore sintática abstrata (abstract syntax tree – AST). De acordo com o Livro do Dragão (Compilers: Principles, Techniques, and Tools, de Aho, Sethi, Ullman e Lam), essa fase é fundamental para capturar a estrutura aninhada e recursiva dos programas — como blocos, expressões com precedência de operadores e construções de controle —, algo que não pode ser feito apenas com expressões regulares e autômatos finitos (usados na fase 1). Para reconhecer linguagens livres de contexto, o parser emprega um modelo computacional mais poderoso: o autômato com pilha (pushdown automaton – PDA), que utiliza uma pilha auxiliar para gerenciar o aninhamento recursivo (ex.: parênteses balanceados, blocos begin-end). O livro detalha principalmente técnicas de parsing top-down (como recursive-descent e LL) e bottom-up (como LR, SLR e LALR), sendo os parsers LR os mais potentes e amplamente usados em compiladores reais por sua eficiência e capacidade de lidar com gramáticas ambíguas ou complexas via tabelas de ações e goto. Assim, o parser não só detecta erros sintáticos (com estratégias de recuperação como pânico ou inserção de tokens), mas também fornece a base para as fases subsequentes de análise semântica e geração de código intermediário. [X Grok AI LLM - Editado]

Ler cap. 1 do livro do dragão.

Atividades:

Iniciamos em aula, finalização pela equipe

- JFLAP experimentar automatos com pilha, gramática livre de contexto: https://www.jflap.org/
- Balanced Parentesis: Criar parser
- XML para JSON: Criar parser

### Objetivo do LAB 2
Implementar dois analisadores sintáticos rudimentares usando **pilha explícita**, sem bibliotecas de parsing prontas:

1. Verificador de **parênteses balanceados** (linguagem clássica {aⁿbⁿ | n ≥ 0}, mas com múltiplos tipos de delimitadores)
2. Conversor simples de **XML para JSON** (sem usar bibliotecas como JAXB, DOM, Jackson, xml.etree, lxml, etc.)

**Entrega em duplas**:  
- Código em **Java** e em **Python** para cada um dos dois exercícios  
- Comentários explicando a relação com autômato com pilha  
- 3–5 casos de teste por exercício (incluindo casos de erro)  
- Relatório curto (1 página): o que a pilha está “lembrando” em cada caso

### 1. Verificador de Parênteses Balanceados (Balanced Parentheses)

**Regras aceitas**:
- Suporta `()`, `[]`, `{}`, `<>`
- Delimitadores podem ser aninhados e misturados corretamente
- Ignora todo o resto do texto (letras, números, espaços, etc.)

**Exemplos válidos**:
```
()[]{}<>
<({[]})>
[ { ( ) } ]
código (x + y) { if (true) { ok } }
{<>({}[])}
```

**Exemplos inválidos**:
```
(]
({)}
{ ( } )
<>[<[>]]
```

### 2. Conversor XML → JSON (sem bibliotecas – parser manual com pilha)

**Restrições importantes**:
- XML bem formado (sem atributos complexos, sem CDATA, sem namespaces)
- Apenas elementos com abertura e fechamento
- Suporta texto dentro de tags e aninhamento
- **Não usar** DOM, SAX, JAXB, xml.etree, lxml, BeautifulSoup, etc.

**Exemplo de entrada XML**:

```xml
<root>
    <pessoa>
        <nome>João</nome>
        <idade>30</idade>
        <cidade>São Paulo</cidade>
    </pessoa>
    <ativo>true</ativo>
</root>
```

**Saída JSON esperada**:

```json
{
  "root": {
    "pessoa": {
      "nome": "João",
      "idade": "30",
      "cidade": "São Paulo"
    },
    "ativo": "true"
  }
}
```

### Dicas

- **Relação com o Livro do Dragão**:  
  Ambos os exercícios usam **pilha** para reconhecer estruturas aninhadas → simulação direta de PDA (autômato com pilha) para linguagens livres de contexto.

- **Extensões possíveis** (bônus):
  - Suportar atributos XML simples
  - Tratar múltiplos filhos com mesmo nome → virar array no JSON
  - Adicionar verificação de bem-formação mais rigorosa
  - Tratar entidades &lt; &gt; &amp;

### Entrega final do LAB (em duplas - pairing)
- Link do relatório em MD no GitHub com:
  - Identificação: faculdade, curso, disciplina, LAB, alunos
  - Printscreen dos experimentos com o JFLAP
  - Código Python + Java funcionando dos parser de XML e Balanced Parenteses
  - Um parágrafo de cada aluno: “O que há de interessante no analisador sintático (parser), automato com pilha, gramática livre de contexto”
  - Texto em MD explicando/documentando as atividades realizadas...
  - Usar as libs JUnit e PyUnit para testes unitários
    
Referência - extra:

- Java, Python, Bash, Linux references: https://books.goalkicker.com/ 
- Parsing Techniques: A Practical Guide, Dick Grune, Ceriel J.H. Jacobs, 2010: https://freecomputerbooks.com/Parsing-Techniques-A-Practical-Guide.html