package br.com.empresa.banco.conta;

public class Poupanca extends Conta{
    public Poupanca(int numero, float saldo){

        super(numero, saldo);
    }

    public void renderJuros(float taxa){
        super.creditar(super.getSaldo() * taxa);
    }
}
