function situacao(){
 var nota1 = prompt("Digite a primeira nota: ");
 var nota2 = prompt("Digite a segunda nota: ");
 var nota3 = prompt("Digite a terceira nota: ");
 var media = (Number(nota1) + Number(nota2) + Number(nota3))/3;
 var resultado = 0;

 resultado = media >= 7 ? "Aprovado" : "Reprovado";

    console.log(resultado);
}
