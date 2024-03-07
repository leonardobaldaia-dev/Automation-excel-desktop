# Automação de Desktop com Python para Excel

## Descrição
Este script Python automatiza o processo de transferência de dados de um arquivo Excel para uma aplicação de desktop. Utiliza as bibliotecas `pyautogui` para simular interações do mouse e do teclado, `pyperclip` para manipular texto com caracteres especiais, e `time` para adicionar pausas entre as ações.

## Funcionalidade
O script lê dados de um arquivo Excel chamado "test1.xlsx". Em seguida, simula ações do usuário para inserir esses dados em campos específicos de uma aplicação desktop, baseando-se em posições predefinidas da tela.

## Pré-requisitos
- Python 3.x
- Bibliotecas: `pyautogui`, `pyperclip`, `pandas`

## Como usar
1. Certifique-se de que o arquivo "test1.xlsx" esteja na mesma pasta do script e que a aplicação de destino esteja aberta e visível na tela.
2. Execute o script: `python automation-desktop-excel.py`
3. O script fará a transição entre o Excel e a aplicação de desktop automaticamente, inserindo os dados nos campos designados.

## Advertência
As posições dos cliques estão codificadas estaticamente. Certifique-se de ajustar as coordenadas (x,y) conforme necessário para corresponder à sua configuração de tela e aplicação.

## Contribuições
Contribuições para melhorar o script são bem-vindas. Por favor, sinta-se livre para fork o repositório e enviar pull requests.

## Licença
[MIT](https://opensource.org/licenses/MIT)
