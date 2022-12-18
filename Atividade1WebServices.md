# Web Services - Client

## Atividade #1
----

Na mensagem está sendo realizada uma requição(POST) para o endereço `http://127.0.0.1/cadastro` passando como parâmetro o nome `Raquel Fernandes` dentro da tag Nome. 

```xml
POST /cadastro HTTP/1.1
Host: 127.0.0.1
Content-Type: text/xml; charset=utf-8
Content-Length: length


<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Header/>
   <soap:Body>
       <Cadastro xmlns="http://127.0.0.1/cadastro">
            <Nome>Raquel Fernandes</Nome>
       </Cadastro>
   </soap:Body>
</soap:Envelope>
```

Caso a requisição seja bem sucedida receberemos como retorno a seguinte resposta:

```xml
HTTP/1.1 200 OK
Content-Type: text/xml; charset=utf-8
Content-Length: length

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
   <soap:Body>
       <Cadastro xmlns="http://127.0.0.1/cadastro">
            <Nome>Raquel Fernandes</Nome>
            <Endereco>Rua dos Bocós</Endereco>
            <Telefone>1234-5678</Telefone>
       </Cadastro>
   </soap:Body>
</soap:Envelope>
```
O status code é 200, o que significa que a requisição foi bem sucedida, e como retorno foram enviadas pelo servidor, as informações que estavam cadastradas referentes ao parâmetro consultado.