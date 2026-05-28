# Computer Science 🧠
## Compilers 🐲
### LAB 🥼👨🏻‍💻⚗️

Project: Build a Toy Compiler for Mini-Pascal or Mini-X programming language using Flex, Bison, and LLVM

- Teams of 3 students, no individual projects, no more than 3 students
- Each team needs to implement a mini compiler for a different imperative programming language, such as Pascal, Basic, C, C++, Java, JavaScript, Python, OCaml, Fortran, Go, Lua, and others...
- Use AI LLM wisely, inform the one used and the prompts
- AI LLM Prompts in English return better results than Portuguese
- Use more than one AI LLM, one to help with coding, another to review and assist with documentation
- Two weeks of work, two weeks due date

> Believe me, neither AI can help you finish this project at the last minute! ☠️ 💣

### Objective

Develop a complete toy compiler for a Mini-Pascal, or Mini-X language on Linux or Mac. The compiler must take a Mini-Pascal source file (.pas) as input and produce a native executable using Flex (lexer), Bison (parser), and LLVM (for intermediate representation and code generation).

```bash
sudo apt install flex, bison, llvm, nasm
```

Environment check (and show evidence):

```bash
gcc -v
flex --version
bison --version
nasm -v
clang --version
llvm-config --version
```

### Language Requirements (Mini-Pascal as example)

Define and implement a minimal but sufficient subset of Pascal or X programming language (as an example) with the following features:

- Data types: integer, boolean, real (optional)
- Variables declaration and assignment
- Control structures: if-then-else, while loops, for loops
- Procedures/Functions (with parameters and return values)
- Basic I/O: write, writeln (support strings and integers)
- Command-line arguments: Access to argc and argv (at least one integer parameter)
- Arithmetic and logical operators
- Comments (# or { } or (* *) or // or /* */ and so on)
- Standard program structure: program Name; ... begin ... end.

### Required Test Programs

The compiler must successfully compile and run these programs:

- factor.pas: Integer Factorization. Receives one integer via the command line. Prints its prime factors (e.g., factor 84 → 2 2 3 7).
- isprime.pas: Prime Number Check. Receives one integer via the command line. Prints true or false indicating whether the number is prime.
- pidigits.pas: Pi Digits. Receives an integer n (number of digits) via the command line. Prints the first n decimal digits of π (e.g., using a series expansion or spigot algorithm).
- fibonacci.pas: Gets an integer from the command line and calculates and prints the corresponding Fibonacci number according to the sequence.

> Create a minimum toy language to compile the test program sources (.pas, .c, .bas, etc... as your team language)

### Deliverables

- lexer.l – Flex lexical analyzer file, regexp, finite automata, scanner
- parser.y – Bison grammar file (with semantic actions), deterministic finite automata with stack, parser, CFG (Context Free Grammar)
- Supporting C/C++ code (driver, symbol table, semantic analysis, LLVM code generation, error handling)
- Makefile for easy building of the compiler
- Bash script to compile and test programs

> AI LLM can be used to create and review the Makerfile, `scanner` and `parser` input source files for your target toy language

Complete step-by-step tutorial (Markdown) for your toy programming language covering:

- Project structure
- How to set up the environment (Flex, Bison, LLVM development libraries)
- Lexical analysis implementation
- Grammar and semantic actions
- LLVM IR generation (using LLVM C++ API)
- Linking and generating the final executable
- How to compile each of the three test programs and run them
- Common issues and debugging tips
- Test programs executables, source code, lex result and grammar result files, asm file
- Evidence (screenshot) of running the test programs

Technical Constraints & Best Practices

Target: 

- Work on Linux (x86-64) or Mac, do not waste time trying on Windows, you can try WSL2 Ubuntu
- Use LLVM C++ API (recommended) or LLVM IR builder
- Proper semantic analysis (type checking, symbol table)
- Good error reporting (line numbers, meaningful messages)
- Modular code organization
- The generated executable should not depend on the compiler itself (statically or dynamically link as needed)

Additional Instructions for the AI Assistant (if using one):

- Provide clean, well-commented code.
- Show the grammar rules clearly.
- Include a working main driver that integrates Flex + Bison + LLVM.
- Prefer modern C++ where appropriate.
- Save all related files on GitHub project repo

Upload to MS Teams the link for the GitHub project repo, just one student per team

> 🃏 For God's sake, list team member names in README.md!! You are not at the first college year anymore!!

---

> THIS IS A HARD SKILL!!<br>
> THIS IS A MILESTONE IN YOUR CAREER JOURNEY TO BECOME A COMPUTER SCIENTIST!<br>
> Creating your own programming language!<br>
> Get proud of yourself!! 🎉 🥳

### References:

- 🐉 Dragon Book! Compilers: Principles, Techniques, and Tools
- https://www.geeksforgeeks.org/compiler-design/flex-fast-lexical-analyzer-generator/
- https://github.com/westes/flex
- https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/handouts/050%20Flex%20In%20A%20Nutshell.pdf
- https://www.gnu.org/software/bison/
- https://www.gnu.org/software/bison/manual/html_node/index.html
- https://llvm.org/
- https://llvm.org/docs/
