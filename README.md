# 🥤 Copiloto de Vendas com IA: Inspiração FYS

> Um repo pequeno para uma ideia grande: usar uma live como base de conhecimento para criar soluções de IA aplicadas a vendas. Sem complicar. Sem reunião de 3 horas que podia ser um prompt.

Este repositório é um apoio para o Desafio de Projeto Final **Copiloto de Vendas com IA para Atendimento ao Cliente**.

A ideia **não é entregar uma solução pronta** e nem limitar o projeto final a um único caminho. A proposta é usar a **FYS**, marca de refrigerantes do grupo **HEINEKEN**, como inspiração para criar soluções diferentes a partir de um contexto real apresentado na live [FYS: Por Dentro da Marca, Desafios e Ideias para o Projeto Final](https://web.dio.me/lives/fys-por-dentro-da-marca-desafios-e-ideias-para-o-projeto-final?back=/track/heineken-inteligencia-artificial-aplicada-vendas).

A FYS tem uma comunicação leve, bem-humorada e um pouco ácida. Ela não tenta parecer perfeita, não força pose de marca número 1 e brinca com a própria posição no mercado. Esse tom pode inspirar projetos mais criativos, humanos e menos robóticos.

---

## 💡 A Sacada

Normalmente, uma IA responde melhor quando tem contexto.

Neste repo, o contexto vem de uma live. Pessoas da FYS explicaram a marca, comentaram desafios de vendas, falaram sobre canais, consumidores, pontos de venda e deram várias pistas que podem virar projeto.

A transcrição da live está em:

```text
knowledge/transcricao-live-fys.txt
```

Ou seja: a live virou uma **base de conhecimento**.

A partir dela, você pode criar um chatbot, copiloto, agente, simulador, análise simples, gerador de mensagens ou qualquer outra solução com IA voltada a vendas e atendimento.

---

## 🎯 Escolha Seu Desafio

Você não precisa resolver tudo. Escolha um recorte simples, explique bem a dor e mostre como a IA pode ajudar.

### 1. Quem é FYS mesmo?

Muita gente ainda não conhece a marca ou não sabe que ela faz parte do grupo **HEINEKEN**.

Ideias:

- Chatbot que apresenta a marca de forma simples;
- Agente que responde dúvidas sobre FYS;
- Gerador de mensagens para explicar a marca sem parecer propaganda chata.

### 2. Me dá uma chance aí

A FYS quer que mais pessoas experimentem o produto. Antes de virar preferência, precisa virar curiosidade.

Ideias:

- Copiloto que sugere argumentos para incentivar experimentação;
- Simulador de abordagem para primeira compra;
- Gerador de campanhas simples para degustação.

### 3. Cadê a FYS na padaria?

Padarias são um canal importante, mas nem sempre recebem a atenção que merecem.

Ideias:

- Agente para priorizar padarias com maior potencial;
- Checklist inteligente para avaliar um ponto de venda;
- Copiloto que sugere próximos passos para ativar uma padaria.

### 4. O vendedor não tem oito braços

A força de vendas precisa escolher onde atuar. A IA pode ajudar a organizar oportunidades e sugerir abordagens.

Ideias:

- Copiloto para preparar argumentos de venda;
- Gerador de mensagens para WhatsApp comercial;
- Agente que sugere abordagem com base no perfil do cliente.

### 5. Produto escondido não performa milagre

Se o consumidor não vê, não lembra. Se não lembra, não pede. Simples assim.

Ideias:

- IA que sugere ações de visibilidade no ponto de venda;
- Checklist de exposição para balcão, geladeira ou cardápio;
- Gerador de ideias de ativação com baixo custo.

### 6. Objeções de balcão

Toda venda tem resistência: preço, marca desconhecida, hábito do cliente, espaço na geladeira ou medo de o produto não girar.

Ideias:

- Agente que responde objeções comuns;
- Simulador de conversa entre vendedor e dono de padaria;
- Base de perguntas e respostas para treinamento comercial.

### 7. O tom FYS sem virar tiozão do pavê

A FYS usa humor, leveza e autoironia. Mas existe uma linha entre ser divertido e forçar a amizade.

Ideias:

- Assistente para revisar mensagens no tom da marca;
- Gerador de respostas comerciais com humor leve;
- Comparador entre mensagem formal, informal e “modo FYS”.

### 8. Dados públicos também jogam

Além da transcrição, você pode usar dados públicos sobre regiões, comércios, consumo ou comportamento do público.

Ideias:

- Análise simples para priorizar bairros ou regiões;
- Ranking de oportunidades por tipo de ponto de venda;
- Agente que combina contexto da live com dados públicos.

---

## 🤖 Usando o DIO Agent

Você pode usar o [DIO Agent](https://github.com/digitalinnovationone/dio-agent) como apoio para pensar, organizar e revisar seu projeto final.

Neste repo:

- O `README.md` explica o contexto;
- O `AGENTS.md` orienta o comportamento do agente;
- O `CLAUDE.md` funciona como alias para o `AGENTS.md`;
- A pasta `knowledge/` guarda a transcrição da live.

### Prompt para começar

Copie e cole este prompt no DIO Agent:

```text
Oi, DIO Agent! Meu nome é...
Estou fazendo o desafio "Copiloto de Vendas com IA para Atendimento ao Cliente" e quero usar este repositório da FYS como inspiração:

https://github.com/digitalinnovationone/copiloto-vendas-ia-atendimento-cliente-fys

Pode analisar o repositório e me ajudar a destravar uma ideia simples para o meu projeto?
Quero entender qual desafio posso explorar, como a IA poderia ajudar e o que eu posso colocar no README da minha entrega.
Me guie passo a passo, sem fazer o projeto inteiro por mim.
```

---

## 🗂️ Estrutura do Repositório

```text
copiloto-vendas-ia-atendimento-cliente-fys/
├── README.md
├── AGENTS.md
├── CLAUDE.md
└── knowledge/
    └── transcricao-live-fys.txt
```

A estrutura é mínima de propósito. A ideia é focar no projeto, não em criar pasta para guardar pasta.

---

## ✅ O Que Entregar no Projeto Final

No seu próprio repositório, explique:

- Qual desafio você escolheu;
- Quem usaria sua solução;
- Qual problema ela resolve;
- Como a IA ajuda;
- Qual base de conhecimento foi usada;
- Um exemplo de conversa, resposta ou análise;
- Possíveis melhorias futuras.

Você não precisa criar uma aplicação completa. Pode entregar um protótipo, prompt, agente, simulação ou documentação bem organizada.

O importante é mostrar que você entendeu o problema e usou IA para propor algo útil.

Bons estudos e bora tirar a FYS do modo “quem?” para o modo “ah, essa eu conheço” 🚀
