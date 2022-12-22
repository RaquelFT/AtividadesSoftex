const express = require("express")
const server = express()
const router = express.Router()
const fs = require('fs')

server.use(express.json({extended: true}))

const readFile = () => {
    const content = fs.readFileSync('./data/items.json', 'utf-8')
    return JSON.parse(content)
} 

const writeFile = (content) => {
    const updateFile = JSON.stringify(content)
    fs.writeFileSync('./data/items.json', updateFile, 'utf-8')
}

router.get('/', (req, res) => {
    const content = readFile()
    res.send(content)
})

router.post('/', (req, res) => {
    const {titulo, autor, isbn} = req.body
    const currentContent = readFile()
    const id = Math.random().toString(32).substr(2, 9)
    console.log(id)
    currentContent.push({id, titulo, autor, isbn})
    writeFile(currentContent)
    res.send({id, titulo, autor, isbn})
})

router.put('/:id', (req, res) => {
    const {id} = req.params

    const {titulo, autor, isbn} = req.body

    const currentContent = readFile()
    const selectedItem = currentContent.findIndex((item) => item.id === id)

    const {id: cId, titulo: cTitulo, autor: cAutor, isbn: cIsbn} = currentContent[selectedItem]

    const newObject = {
        id: cId,
        titulo: titulo ? titulo: cTitulo,
        autor: autor ? autor: cAutor,
        isbn: isbn ? isbn: cIsbn,
    }

    currentContent[selectedItem] = newObject
    writeFile(currentContent)

    res.send(newObject)
})

router.delete('/:id', (req, res) => {
    const {id} = req.params
    const currentContent = readFile()
    const selectedItem = currentContent.findIndex((item) => item.id === id)
    currentContent.splice(selectedItem, 1)
    res.send(currentContent)
})

server.use(router)

server.listen(3000, () =>{
    console.log("Rodando servidor")
})