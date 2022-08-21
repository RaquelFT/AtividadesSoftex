package br.com.empresa.banco.pessoa;
import br.com.empresa.banco.conta.Conta;

public class Correntista extends Pessoa {

    private Conta contas[];
    private int totalContas;

    public Correntista(){
        this.contas = new Conta[5];
        this.totalContas = 0;
    }

    public Conta[] getContas(){
        return this.contas;
    }
    public Conta getConta(int numero){
        Conta conta = null;

        for(int i = 0; i < totalContas; i++){
            if(contas[i].getNumero() == numero){
                conta = contas[i];
            }
        }
        return conta;
    }
    public boolean addConta(Conta conta){
        boolean resultado = false;
        if(this.totalContas < contas.length){
            this.contas[this.totalContas] = conta;
            this.totalContas = this.totalContas + 1;
            resultado = true;
        }
        return resultado;
    }
}
