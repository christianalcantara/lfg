### Baixe o código fonte e acesse o diretório `frontend`

```angular2html
git@github.com:christianalcantara/plp.git
cd frontend
```

### Configure as variáveis de ambiente

```
nano .env
```

Adicione as seguintes informações no arquivo ou altere caso necessário.

```
PORT=8081
baseURL=http://localhost:8000
```

### Configuração do projeto

No diretório do projeto, execute:

```
npm install
# ou
yarn install
```

### Executar o projeto

```
export NODE_OPTIONS=--openssl-legacy-provider
```

```
npm start
# ou
yarn start
```

Abra no navegador [http://localhost:8081](http://localhost:8081).
