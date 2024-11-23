- Em produção...

# Zé de Vicente  

O site "Zé de Vicente" foi desenvolvido para a **Material de Construção Zé de Vicente**, uma empresa com mais de 50 anos de tradição no mercado. Ele visa representar a história e os valores da empresa, oferecendo uma interface moderna e acessível. Além disso, possui funcionalidades para envio de currículos, promovendo novas oportunidades de trabalho.

---

## Estrutura do Projeto  

### **1. Front-End**  
O front-end foi desenvolvido utilizando tecnologias web padrão:  
- **HTML**: Estruturação do conteúdo.  
- **CSS**: Estilização para tornar a interface visualmente agradável.  
- **JavaScript**: Interatividade e funcionalidades dinâmicas.

#### Principais Funcionalidades:
- **Seção "Sobre a Empresa"**: Explica a história e os valores da empresa.  
- **Carrossel de Imagens**: Exibe fotos da empresa, destacando momentos e infraestrutura.  
- **Formulário de Envio de Currículos**: Permite aos candidatos preencherem seus dados e anexarem o currículo em formato PDF.  

### **2. Back-End**  
O back-end foi desenvolvido em **Flask**, um framework em Python, para gerenciar as requisições e o processamento dos dados.  

#### Funcionalidades:
- **Recebimento de Currículos**: Processa as informações enviadas pelo formulário, como nome, e-mail, telefone e cargo desejado.  
- **Armazenamento de Arquivos**: Faz upload e armazenamento seguro do currículo em PDF.  
- **Integração com Banco de Dados**: Registra as informações dos candidatos em uma base de dados.  

### **3. Banco de Dados**  
O sistema utiliza **SQLite**, uma solução leve e eficaz para o armazenamento de dados.  

#### Estrutura do Banco de Dados:  
Tabela `candidatos`:  
| Campo           | Tipo         | Descrição                               |  
|------------------|--------------|-----------------------------------------|  
| id              | INTEGER      | Identificador único do candidato (PK). |  
| nome            | TEXT         | Nome completo do candidato.            |  
| email           | TEXT         | Endereço de e-mail do candidato.       |  
| telefone        | TEXT         | Telefone de contato do candidato.      |  
| cargo_desejado  | TEXT         | Cargo escolhido pelo candidato.        |  
| arquivo_curriculo | TEXT       | Caminho para o arquivo PDF enviado.    |  
| data_envio      | DATETIME     | Data e hora do envio do currículo.     |  

---

## Configuração do Projeto  

### **Requisitos**  
- Python 3.12 ou superior  
- Flask  
- SQLite  

### **Instalação e Execução**  
1. **Clone o repositório:**  
   ```bash
   git clone https://github.com/biancaalvess/ze-vicente
   cd ze-de-vicente


Desenvolvido com 💻 e ☕ por Bianca Alves.
