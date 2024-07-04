## O Desafio
### adicionar query parameters nos endpoints
**atleta**
1. nome
2. cpf
### customizar response de retorno de endpoints
**get all**
**/atleta**
- nome
- centro_treinamento
- categoria

**Manipular exceção de integridade dos dados em cada módulo/tabela**
**sqlalchemy.exc.IntegrityError** e devolver a seguinte mensagem: 
*“Já existe um atleta cadastrado com o cpf: x”*
**status_code: 303**
### Adicionar paginação utilizando a lib: fastapi-pagination
**limit e offset**
