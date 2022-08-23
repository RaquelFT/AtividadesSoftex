// Este código foi retirado do endereço:
// https://www.devmedia.com.br/serializacao-de-objetos-em-java/23413
// A finalidade é praticar os exemplos para fixar os conceitos da linguagem

import java.util.ArrayList;

  public class Exemplo2 {

      public static void main(String[] args) {
          // desserialização: recuperando os objetos gravados no arquivo binário "dados.dat"
          ArrayList<Object> pessoa = Empacotamento.lerArquivoBinario("dados.dat");

          int i = 1;
          for (Object item: pessoa){
              System.out.printf("Ficha nro....:%d.\n", i++);
              // ((Pessoa)item) - implementa o mecanismo de downcast, ou seja, o objeto
              // "item" declarado a partir da classe base "Object" é referenciado com
              // um objeto "Pessoa"
              System.out.printf("Nome-----------: %s\n", ((Pessoa)item).getNome());
              System.out.printf("Peso corporal: %.2f kgs\n", ((Pessoa)item).getPC());
              System.out.printf("Altura---------: %.2f metros\n", ((Pessoa)item).getAlt());
              System.out.printf("IMC------------: %.2f\n", ((Pessoa)item).IMC());
              System.out.printf("Interpretacao: %s\n\n", ((Pessoa)item).interpretaIMC());
          }
      }
}
