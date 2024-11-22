const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('./data/ze_de_vicente.db', (err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err.message);
    } else {
        console.log('Conexão ao banco de dados estabelecida.');
    }
});

db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS candidatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            cargo_desejado TEXT NOT NULL,
            curriculo BLOB NOT NULL
        )
    `, (err) => {
        if (err) {
            console.error('Erro ao criar tabela:', err.message);
        } else {
            console.log('Tabela "candidatos" criada ou já existe.');
        }
    });
});

module.exports = db;
