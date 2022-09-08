
function Livro(title, author, country) {
  this.arr = [title, author, country]; 
  this.title = title;
  this.author = author;
  this.country = country;
};

function propriedades(objeto){
  return Object.keys(objeto);
};

function elementos(array){
  for (let elemento of array)
    console.log(elemento);
};


books = new Livro("Lord of the Rings", "J. R. R. Tolkien", "United Kingdom");

console.log(propriedades(books));
elementos(books.arr);