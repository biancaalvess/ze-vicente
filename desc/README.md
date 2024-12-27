# Zé de Vicente

## Project Description
The "Zé de Vicente" website was developed for **Material de Construção Zé de Vicente**, a company with over 50 years of tradition in the market. It aims to represent the company's history and values, offering a modern and accessible interface. It also includes features for sending resumes, promoting new job opportunities.

---

## Project Structure

### **1. Front-End**
The front-end was developed using standard web technologies:
- **HTML**: Content structuring.
- **CSS**: Styling to make the interface visually appealing.
- **JavaScript**: Interactivity and dynamic functionalities.

#### Main Features:
- **"About the Company" Section**: Describes the company's history and values.
- **Image Carousel**: Displays photos of the company, highlighting moments and infrastructure.
- **Resume Submission Form**: Allows candidates to fill out their details and attach a resume in PDF format.

### **2. Back-End**
The back-end was developed with **Flask**, a Python framework, to manage requests and data processing.

#### Features:
- **Resume Submission Handling**: Processes the information sent through the form, such as name, email, phone, and desired position.
- **File Storage**: Uploads and securely stores the resume in PDF format.
- **Database Integration**: Registers candidate information in a database.

### **3. Database**
The system uses **SQLite**, a lightweight and efficient solution for data storage.

#### Database Structure:
Table `candidates`:
| Field          | Type       | Description                              |
|----------------|------------|------------------------------------------|
| id             | INTEGER    | Unique identifier for the candidate (PK) |
| name           | TEXT       | Candidate's full name                    |
| email          | TEXT       | Candidate's email address                |
| phone          | TEXT       | Candidate's contact phone number         |
| desired_position | TEXT     | Position chosen by the candidate         |
| resume_file    | TEXT       | Path to the uploaded PDF resume          |
| submission_date | DATETIME  | Date and time of resume submission       |

---

## Project Setup

### **Requirements**
- Python 3.12 or higher
- Flask
- SQLite

### **Installation and Execution**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/biancaalvess/ze-vicente
   cd ze-de-vicente


# Zé de Vicente  

## Descrição do Projeto  
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


