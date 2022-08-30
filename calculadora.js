var num1 = prompt("Digite um número: ");
var num2 = prompt("Digite o segundo número: ");
var operador = prompt("Escolha o operador lógico: ");
var resultado = 0;


if (operador == "+") {
    resultado = Number(num1) + Number(num2);
}
else if (operador == "-") {
    resultado = Number(num1) - Number(num2);
}
else if (operador == "*") {
    resultado = Number(num1) * Number(num2);
}
else if (operador == "/") {
    console.log(Number(num1) / Number(num2));
    console.log(Number(num1) % Number(num2));
}


