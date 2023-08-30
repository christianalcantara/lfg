<p align="center">
  <a href="https://github.com/christianalcantara/ntk">
    <img style="height: 7em" src="docs/images/logo.png" alt="Logo">
  </a>
</p>

<h2 align="center" style="color: white;" ali>Sistema de Gestão de Propostas de Empréstimo Pessoal</h3>

<ol>
<li>
  <a href="#sobre-o-projeto">Sobre o Projeto</a>
</li>
<li>
  <a href="#começando">Começando</a>
</li>
<li>
  <a href="#mãos-na-massa">Mãos na massa</a>
  <ul>
    <li><a href="#usuário">Usuário</a></li>
    <li><a href="#administrador">Administrador</a></li>
  </ul>
</li>
<li>
   <a href="#explore">Explore</a>
</li>
</ol>

<!-- SOBRE O PROJETO -->

## Sobre o Projeto

<details>

# Challenge Django Consultant

## _Teste Técnico para Consultor Django DigitalSys_

### Introdução

Esse teste técnico visa avaliar a sua proficiência em Django com um problema real, vocẽ terá passo-a-passo de como proceder para realizar e enviar o teste técnico

### Entrega

A entrega desse desafio deverá ser feita através do e-mail code-challenge@digitalsys.com.br com as seguintes características:

- **Título do E-mail:** Code-Challenge: Django Consultant-
- **Conteúdo do E-mail:** Seu nome completo, link do github e link do seu linkedin

### _Definition of Done_ para seu projeto

- Tenha em mente que a pessoa que for avaliar seu projeto não lerá seu código antes de vê-lo funcionar, por isso, inclua no README do projeto as instruções para rodar seu projeto com sucesso.
- Dê preferência a uma solução dockerizada, um docker-compose com todas as dependências do projeto costumam funcionar melhor do que depender que o ambiente da outra pessoa possua as dependências
- Certifique-se que seu projeto faz o setup do ambiente corretamente, como, por exemplo realizar as migrações de banco, criação de usuário inicial e qualquer outra config que se fizer necessária

**Importante:** Testes técnicos não funcionais são automaticamente desconsiderados do processo

### Stack Desejada

- Django
- Django Celery
- Django Rest Framework

## Desafio Técnico

A `Loans For Good` (LFG) é uma empresa multinacional especializada na concessão de crédito e está vindo para o Brasil, para iniciar sua operação, você foi contratado como o primeiro desenvolvedor dela no Brasil e será o responsável por criar a plataforma de empréstimo.

### Requisitos Funcionais

O sistema deverá ter uma interface web onde pessoas possam solicitar propostas, nessa interface não será necessário que a pessoa esteja logada no sistema ou mesmo que ela possua um usuário no sistema

O sistema deve oferecer flexibilidade para que o admin do sistema possa configurar quais os campos que a proposta deve conter, ou seja, caberá a alguém de dentro da empresa definir o que deverá ser pedido de informação para o solicitante da proposta

A proposta deverá passar por uma avaliação automatizada através de uma API de Análise de Crédito já desenvolvida (documentação da API disponível em: https://loan-processor.digitalsys.com.br/swagger/index.html), caso a API retorne o status de não aprovado, a proposta deve ser negada automaticamente, caso seja aprovada, deverá ser disponibilizada para avaliação humana.

Deve haver uma listagem dentro do sistema para que o admin visualize as propostas, para aquelas marcadas para análise humana o admin deve poder mudar o status da proposta para 'Aprovada' ou 'Negada'

### Sugestão para o Desenvolvimento

- Fazer a interface de preenchimento de propostas numa interface á parte (pode ser usado um framework web como ReactJS, VueJS, Angular ou mesmo só HTML com CSS e JS)
- Essa interface de preenchimento de propostas deve se comunicar com o projeto em Django através de API
- Utilizar o Django Celery para receber as propostas vindo da API Django e realizar a chamada para a API de Análise de Crédito
- Utilizar o Django Admin para toda a parte de back-office (criação dos campos de proposta, análise da proposta, etc)

</details>

<!-- COMEÇANDO -->

## Começando

Para executar o projeto é necessário ter o Docker + Docker Compose instalado.

https://docs.docker.com/compose/install/

#### Baixe o repositório do github

```bash
$ git clone https://github.com/christianalcantara/lfg.git
```

#### Instalação

```bash
$ cd plp # Acessar o diretório do projeto
$ docker compose up
# ou
$ docker-compose up

# se necessário use o parâmetro --build no final dos comandos acima.
# Geralmente utilizado quando há modificações no código fonte.
$ docker-compose up --build
```

[![asciicast](https://asciinema.org/a/lbaeiwVjwWKTuGMHRBXyR4ZnQ.svg)](https://asciinema.org/a/lbaeiwVjwWKTuGMHRBXyR4ZnQ)

<!-- USABILIDADE -->

## Mãos na massa

### Usuário

Se tudo deu certo acesse a url: http://localhost:3000 para acessar o frontend e solicitar uma proposta.
Siga os passos na seguinte ordem:

<table>
<thead>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="width: 33%; border: unset"><img style="height: 7em" src="docs/images/tela_proposta_1.png" alt="Logo"></td>
        <td class="tg-0pky" style="width: 33%; border: unset"><img style="height: 7em" src="docs/images/tela_proposta_2.png" alt="Logo"></td>
        <td class="tg-0pky" style="width: 33%; border: unset"><img style="height: 7em" src="docs/images/tela_proposta_3.png" alt="Logo"></td>
    </tr>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="width: 33%; border: unset">1. Selecione uma proposta</td>
        <td class="tg-0pky" style="width: 33%; border: unset">2. Preencha as informações</td>
        <td class="tg-0pky" style="width: 33%; border: unset">3. Clique em <b>Enviar Proposta</b></td>
    </tr>

</thead>
</table>

### Administrador

Se você é administrador do sistema acesse a url: http://localhost:8000/admin.

- Credenciais:

```
Usuário: admin
Senha  : admin
```

<table>
<thead>
    <tr style="border: unset">
        <td class="tg-0pky" style="text-align: center; width: 50%; border: unset"><img style="height: 7em" src="docs/images/login.png" alt="Logo"></td>
        <td class="tg-0pky" style="text-align: center; width: 50%; border: unset"><img style="height: 7em" src="docs/images/admin_home.png" alt="Logo"></td>
    </tr>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="border: unset">1. Tela de login</td>
        <td class="tg-0pky" style="border: unset">2. Menu administrativo</td>
    </tr>
</thead>
</table>

##### Para cadastrar uma proposta é muito simples, siga os passos a seguir:

<table>
<thead>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_proposal_menu.png" alt="Logo"></td>
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_proposal_list.png" alt="Logo"></td>
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_proposal_view.png" alt="Logo"></td>
    </tr>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="border: unset">1. Acesse o menu <b>Proposta</b></td>
        <td class="tg-0pky" style="border: unset">2. Altere ou crie uma <b>Proposta</b></td>
        <td class="tg-0pky" style="border: unset">3. Defina um título e adicione os campos da <b>Proposta</b></td>
    </tr>
</thead>
</table>

##### Para visualizar uma pedido de empréstimo é mais simples ainda:

<table>
<thead>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_loan_menu.png" alt="Logo"></td>
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_loan_list.png" alt="Logo"></td>
        <td class="tg-0pky" style="text-align: center; width: 33%; border: unset"><img style="height: 7em" src="docs/images/admin_loan_view.png" alt="Logo"></td>
    </tr>
    <tr style="border: #e24545">
        <td class="tg-0pky" style="border: unset">1. Acesse o menu <b>Pedidos de empréstimo</b></td>
        <td class="tg-0pky" style="border: unset">2. Selecione um pedido caso queira ver os campos preenchidos</td>
        <td class="tg-0pky" style="border: unset">3. <b>Voilà</b></td>
    </tr>
</thead>
</table>
<p style="color: red">Obs: Os pedidos enviados pelo frontend, são processados em um intevalo de 10 segundos no RabbitMQ/Celery.</p>

##### Para Aprovar/Negar um pedido de empréstimo:

<img src="docs/images/tela_proposta_4.png" alt="Logo">

1. Selecione um pedido de empréstimo com o status `Aguardando Aprovação`.
2. Clique no botão `Aprovar` ou `Negar

## Explore

✨ 🍰 ✨

Caso, seja curioso acesse a url: http://localhost:8000 e veja alguns endpoints disponíveis.

<p align="center">
    <img src="docs/images/api.png">
</p>
