package br.com.empresa.banco.conta;
public class Conta {
    private int numero;
    private float saldo;

    public Conta(int numero, float saldo){
        this.numero = numero;
        this.saldo = saldo;
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero){
        this.numero = numero;
    }

    public float getSaldo() {
        return saldo;
    }
    public boolean debitar (float valor){
        boolean resultado = false;
            if((this.saldo - valor) >= 0){
                this.saldo = this.saldo - valor;
                resultado = true;
            }

            return resultado;
    }
    public boolean creditar(float valor){
        this.saldo = this.saldo + valor;
        return true;
    }

}
