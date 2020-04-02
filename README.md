# Sudoku
Sudoku é um jogo composto por uma matriz quadrada, possuindo tradicionalmente dimensão de 9x9. O objetivo do jogo é preencher esta matriz com números de 1 a 9, seguindo algumas regras préviamente estabelecidas.
A matriz pode ser divida em 9 colunas, 9 linhas ou 9 submatrizes (de tamanho 3x3 cada), sendo que, no inicio, deve estar parcialmente preenchidas com alguns dos elementos que compõem o resultado.

## 1. Regras do jogo
1.1) Não podem haver números repetidos em uma linha
1.2) Não podem haver números repetidos em uma coluna
1.3) Não podem haver números repetidos em uma submatriz
1.4) Os elementos pré-definidos não podem ser alterados

## 2. Arquivo de entrada
2.1) Arquivo de texto
2.2) Cada linha representa uma linha do Sudoku
2.3) Cada elemento é representado por um número inteiro positivo, sendo 0 reservado para representar os elementos a serem preenchidos pelo programa
2.4) Os elementos de cada linha devem ser separados por espaço
2.5) O numero de linhas deve ser igual ao número de colunas
2.6) O arquivo deve conter ao menos uma linha

## 3. Interpretação da entrada
3.1) Caso o número de linhas seja diferente do número de colunas, a execução do programa deve ser interrompida
3.2) Caso o número de colunas seja inconsistete entra as linhas, a execução do programa deve ser interrompida
3.4) Os valores a serem preenchidos fazem parte do período [1, n], sendo n a quantidade de colunas