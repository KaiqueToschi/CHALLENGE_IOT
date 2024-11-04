### Integrantes do Grupo
- Macirander - RM551416 - 2TDSPF
- Carlos - RM97528 - 2TDSPX
- Munir - RM550893 - 2TDSPF
- Kaique - RM551165 - 2TDSPX
- Vinicius - RM98839 - 2TDSPX

### Visão Geral
O **Análise de Sentimentos** é uma aplicação web que permite ao usuário inserir mensagens de texto e obter uma análise de sentimento com base na polaridade do conteúdo. Utiliza uma interface simples em HTML e CSS, com backend em Flask para processamento de sentimentos usando a biblioteca `vaderSentiment`.

### Arquitetura

- **Frontend**: A interface é implementada com HTML e CSS, oferecendo um layout responsivo e intuitivo. Utiliza JavaScript para realizar chamadas ao backend e exibir o resultado da análise de sentimento.
  
- **Backend**: Desenvolvido em Python com Flask, o backend recebe as mensagens enviadas pelo frontend e processa o sentimento usando a biblioteca `vaderSentiment`. Os resultados incluem sentimentos classificados como `Satisfeito`, `Neutro` ou `Insatisfeito`.

### Design Patterns Utilizados

- **API RESTful**: O backend expõe um endpoint `/analyze` para a análise de sentimento. Esse endpoint recebe uma mensagem em JSON, processa a polaridade e retorna o sentimento correspondente em JSON.
- **MVC (Modelo-Visão-Controlador)**: A aplicação segue o padrão MVC, onde o Flask atua como controlador e o HTML/CSS é a visão, oferecendo separação de responsabilidades.

### Arquitetura da Aplicação

Abordagem Monolítica: O projeto é implementado como uma aplicação monolítica, em que o frontend e backend são executados juntos. Essa abordagem simplifica o desenvolvimento e a implantação para projetos de menor escala.

#### Justificativas para a Abordagem Monolítica

1. **Simplicidade na Arquitetura**
   - **Facilidade de Desenvolvimento e Testes**: Com uma única base de código, o desenvolvimento e os testes são mais diretos, sem a necessidade de gerenciar múltiplos serviços.

2. **Custo e Recursos**
   - **Menor Overhead de Infraestrutura**: Reduz os custos operacionais, pois não há necessidade de gerenciar serviços separados.

3. **Escalabilidade Inicial**
   - **Escalabilidade Vertical**: A aplicação pode escalar verticalmente para suportar a carga inicial.

### Futuro Planejado
A longo prazo, a aplicação pode ser dividida em microserviços, com uma camada separada para o processamento de sentimentos e outra para a interface de usuário. Benefícios esperados incluem:

- **Escalabilidade Granular**: Escalar componentes de forma independente para otimizar recursos.
- **Manutenção Simplificada**: Facilitar a atualização de funcionalidades específicas sem afetar o sistema completo.

### Instruções para Rodar a Aplicação

#### Pré-requisitos
- **Python 3.x**: Certifique-se de que o Python 3 está instalado.
- **Bibliotecas Flask e vaderSentiment**: Instale essas bibliotecas para rodar o backend.

#### Configuração

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/KaiqueToschi/CHALLENGE_IOT.git
    cd CHALLENGE_IOT
    ```

2. **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```
   O arquivo `requirements.txt` deve conter as bibliotecas `Flask` e `vaderSentiment`.

3. **Iniciar o Backend**
    ```bash
    python app.py
    ```
   O backend estará disponível em `http://127.0.0.1:5000`.

4. **Abrir a Interface**
   Abra o arquivo `index.html` em um navegador.

### Testando a Análise de Sentimento
1. **Digite uma mensagem na área de texto** e clique em "Analisar".
2. **Resultado da Análise**: O sentimento será exibido como `Satisfeito`, `Neutro` ou `Insatisfeito`, com cores específicas:
   - **Verde** para Satisfeito
   - **Amarelo** para Neutro
   - **Vermelho** para Insatisfeito

### Exemplo de Teste
- **Mensagem**: "Estou muito feliz com o serviço!"
  - **Resultado**: Sentimento: Satisfeito (verde)
- **Mensagem**: "Estou insatisfeito com o atendimento."
  - **Resultado**: Sentimento: Insatisfeito (vermelho)

### Arquivos Incluídos

- **app.py**: Backend em Flask que processa o sentimento usando `vaderSentiment`.
- **index.html**: Interface de usuário com uma área de texto e botão de análise.
- **style.css**: Define o estilo da interface.
- **JavaScript**: Responsável por enviar a mensagem ao backend e exibir o resultado.

Este README fornece uma visão geral do projeto, instruções para configuração e execução, e descreve os principais aspectos da arquitetura e funcionalidades da aplicação.
