# 🥤 FYS Copiloto de PDV - Inteligência Artificial Aplicada a Vendas

Este repositório contém a entrega final para o desafio de projeto **"Copiloto de Vendas com IA para Atendimento ao Cliente"** do Bootcamp Heineken da **DIO (Digital Innovation One)**.

O projeto consiste em um copiloto interativo para celular ou tablet desenvolvido em **Python** com **Streamlit** e integrado à **API do Google Gemini**. Ele auxilia a força de vendas a realizar auditorias rápidas em padarias e pontos de venda (PDV), calculando o potencial de venda da marca **FYS** (do Grupo HEINEKEN) e sugerindo ações de ativação baratas, práticas e criativas com base no contexto real da marca.

---

## 🎯 Desafio e Contexto de Negócio

Nas rotinas comerciais, a Heineken enfrenta o desafio de otimizar a distribuição do refrigerante FYS. A marca tem um tom de voz único (leve, humorístico e autoirônico) e concorre com gigantes consolidadas.

### As principais dores abordadas por esta solução são:
1. **Falta de braços no campo:** O vendedor não consegue visitar todas as padarias todos os dias para dar ideias de visibilidade.
2. **"Produto escondido não faz milagre":** FYS muitas vezes fica esquecida no fundo de geladeiras ou prateleiras baixas.
3. **Falta de ideias rápidas:** Vendedores precisam de sugestões instantâneas e baratas para propor ativações no PDV.

---

## ⚙️ Como a Solução Funciona

A ferramenta une **lógica de negócio baseada em regras** com **inteligência artificial generativa (Gemini API)**:

1. **Identificação e Potencial:** O vendedor responde se o PDV já vende Heineken e qual o fluxo de pessoas. O sistema gera automaticamente um **Score de Potencial** (Alto, Médio ou Baixo).
2. **Checklist Rápido:** Uma auditoria rápida de 4 perguntas sobre a presença fria (geladeira), quente (balcão), exposição e comunicação visual.
3. **Plano FYS com IA:** O Gemini 1.5 Flash analisa as respostas e gera 3 recomendações sob medida no tom autêntico da marca FYS, além de um argumento de vendas persuasivo.

---

## 🤖 Engenharia de Prompt e Regras de Negócio

O modelo utiliza o modelo **Gemini 1.5 Flash** configurado com as seguintes instruções de sistema:

### System Prompt (Instrução do Sistema):
> Você é o "FYS Copiloto de PDV", um assistente especialista em trade marketing e vendas para o refrigerante FYS (Grupo HEINEKEN).
> Seu objetivo é analisar o diagnóstico de uma padaria e sugerir ações de ativação baratas, criativas e no tom de voz da marca FYS.
> Seu tom de voz deve ser leve, descontraído e autoirônico ("Menos marketing, mais sabor").
> 
> **Diretrizes de Ativação baseadas na Live FYS:**
> 1. *Exposição:* Colocar FYS na altura dos olhos ou ao lado da Heineken na geladeira.
> 2. *Fila do pão:* Expor FYS quente perto do balcão de pães para gerar compras por impulso.
> 3. *Degustação:* Sugerir pequenas amostras de dose (shot) para quem espera no balcão.
> 4. *Heineken:* Usar a facilidade logística e faturamento da Heineken como argumento.

---

## 🛠️ Como Executar o Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as Dependências
Certifique-se de ter o Python 3.9+ instalado. Instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 3. Configurar a Chave de API
Você precisará de uma chave de API do Gemini (obtenha gratuitamente no [Google AI Studio](https://aistudio.google.com/)). 

Você pode inseri-la de duas formas:
- Diretamente na barra lateral da aplicação rodando localmente.
- Definindo a variável de ambiente:
  - **No Windows (PowerShell):** `$env:GEMINI_API_KEY="sua_chave_aqui"`
  - **No Linux/macOS:** `export GEMINI_API_KEY="sua_chave_aqui"`

### 4. Rodar a Aplicação
```bash
streamlit run app.py
```
A aplicação abrirá automaticamente no seu navegador padrão.

---

## 🔮 Melhorias Futuras

- **Reconhecimento de Imagens (Visão Computacional):** Permitir que o vendedor tire uma foto da geladeira da padaria e a IA identifique automaticamente se a FYS está visível ou escondida.
- **Integração com WhatsApp:** Permitir que o vendedor envie as respostas do checklist via texto de WhatsApp e receba a estratégia de volta instantaneamente em formato de mensagem de voz ou texto resumido.
