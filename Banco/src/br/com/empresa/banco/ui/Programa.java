// Código baseado nas aulas de Robson Medeiros
// https://www.youtube.com/channel/UCGr8CBzpJBPaGFF0e4O7lAA

package br.com.empresa.banco.ui;

import br.com.empresa.banco.pessoa.*;
import br.com.empresa.banco.conta.*;

public class Programa {
    public static void main(String args[]){
        Funcionario funcionario1 = new Funcionario();
        Funcionario funcionario2 = new Funcionario();

        Endereco enderecoFuncionario1 = new Endereco("Rua Qualquer", 01, "Bairro Longe", "Cidade de Jalapão",  "Estado Ficticío", "00.000-000");
        Endereco enderecoFuncionario2 = new Endereco("Rua Lá", 10, "Bairro Distante", "Cidade de Campinas",  "Estado Defasado", "22.000-000" );

        funcionario1.setEndereco(enderecoFuncionario1);
        funcionario2.setEndereco(enderecoFuncionario2);

        funcionario1.setNome("Raquel");
        funcionario1.setSalario(3500.00f);

        funcionario2.setNome("Maria");
        funcionario2.setSalario(4000.00f);

        //System.out.println("-------------------------------------------------------------");
        //System.out.println("O nome do funcionário1 é: " + funcionario1.getNome());
//        System.out.println("O salário do funcionário1 é: " + funcionario1.getSalario());
//        System.out.println("O endereço do funcionário1 é: ");
//        System.out.println(funcionario1.getEndereco().getRua());
//        System.out.println("Numero: " + funcionario1.getEndereco().getNumero());
//        System.out.println("Bairro: " + funcionario1.getEndereco().getBairro());
//        System.out.println("Cidade: " + funcionario1.getEndereco().getCidade());
//        System.out.println("Estado: " + funcionario1.getEndereco().getEstado());
//        System.out.println("Cep: " + funcionario1.getEndereco().getCep());
//
//        System.out.println("---------------------------------------------------------------");
//        System.out.println("---------------------------------------------------------------");
//
//        System.out.println("O nome do funcionário2 é: " + funcionario2.getNome());
//        System.out.println("O salário do funcionário2 é: " + funcionario2.getSalario());
//        System.out.println("O endereço do funcionário1 é: ");
//        System.out.println(funcionario2.getEndereco().getRua());
//        System.out.println("Numero: " + funcionario2.getEndereco().getNumero());
//        System.out.println("Bairro: " + funcionario2.getEndereco().getBairro());
//        System.out.println("Cidade: " + funcionario2.getEndereco().getCidade());
//        System.out.println("Estado: " + funcionario2.getEndereco().getEstado());
//        System.out.println("Cep: " + funcionario2.getEndereco().getCep());

        Pessoa correntista = new Correntista();
        Conta contaCorrente = new Conta(1111, 1000.00F);
        ((Correntista)correntista).addConta(contaCorrente);

        Conta contaPoupanca = new Poupanca(1232, 1000F);
        ((Correntista)correntista).addConta(contaPoupanca);

        Conta contaRetornada = ((Correntista)correntista).getConta(1232);
        if(contaRetornada != null) {
            System.out.println("Saldo: " + contaRetornada.getSaldo());

            if(contaRetornada instanceof Poupanca){
                ((Poupanca)contaRetornada).renderJuros(0.001f);
            }
        }

        System.out.println("Saldo: " + contaRetornada.getSaldo());

    }
}

