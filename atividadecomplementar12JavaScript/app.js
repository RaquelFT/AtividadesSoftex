const express = require('express');
const app = express();

const db = require('./models/db');

app.get("/", async (req, res) => {
    res.send("Página Inicial - Atividade Complementar 12");
});

app.get("/cadastrar", async (req, res) => {
    res.send("Página cadastrar - Atividade complementar 12");
});

app.listen(8080, () => {
    console.log("Servidor iniciado na porta 8080: http://localhost:8080");
})