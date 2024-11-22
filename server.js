const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const sqlite3 = require('sqlite3').verbose(); 

const app = express();
const port = 4000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static('public'));

const upload = multer({ dest: 'uploads/' });

// Inicialização do banco de dados SQLite
const db = new sqlite3.Database('./db/zevicente.db', (err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err.message);
        return;
    }
    console.log('Conectado ao banco de dados SQLite.');
});

app.post('/submit', upload.single('resume'), (req, res) => {
    const { name, email, phone, position } = req.body;
    const resumePath = req.file.path;

    const query = `
        INSERT INTO candidatos (nome, email, telefone, cargo_desejado, curriculo)
        VALUES (?, ?, ?, ?, ?)
    `;
    db.run(query, [name, email, phone, position, resumePath], (err) => {
        if (err) {
            console.error('Erro ao inserir dados no banco:', err.message);
            res.status(500).send('Erro ao salvar os dados.');
        } else {
            res.send('Dados salvos com sucesso!');
        }
    });
});

app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
