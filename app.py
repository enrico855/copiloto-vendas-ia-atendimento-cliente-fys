import streamlit as st
import os
import google.generativeai as genai

# Configuração da Página
st.set_page_config(
    page_title="FYS - Copiloto de PDV",
    page_icon="🥤",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilização Customizada para um visual Premium
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stButton>button {
        background-color: #00bcd4;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #008c9e;
        color: white;
        box-shadow: 0 0 10px #00bcd4;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .highlight-cyan {
        color: #00bcd4;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🥤 FYS - Copiloto de Diagnóstico de PDV")
st.subheader("Transforme padarias comuns em pontos de venda de alta performance para FYS")

# Sidebar para Chave de API
st.sidebar.header("🔑 Configurações da API")
api_key_input = st.sidebar.text_input("Digite sua Gemini API Key:", type="password")

# Tenta carregar do ambiente se não for digitada na barra lateral
api_key = api_key_input or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.sidebar.warning("⚠️ Insira sua Gemini API Key na barra lateral ou defina a variável de ambiente GEMINI_API_KEY para habilitar a IA.")

# --- SEÇÃO 1: INFORMAÇÕES DO PDV ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🏪 1. Identificação do Estabelecimento")
nome_pdv = st.text_input("Nome da Padaria / Ponto de Venda:", placeholder="Ex: Padaria Bela Vista")
col1, col2 = st.columns(2)
with col1:
    vende_heineken = st.radio("O estabelecimento já vende cervejas do grupo (ex: Heineken, Amstel)?", ["Sim", "Não"])
with col2:
    fluxo_clientes = st.selectbox("Fluxo diário de clientes na padaria:", ["Baixo", "Médio", "Alto"])
st.markdown("</div>", unsafe_allow_html=True)

# --- SEÇÃO 2: AUDITORIA E CHECKLIST ---
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 🔍 2. Checklist Inteligente de Visibilidade")
st.write("Marque o que está atualmente ativo no ponto de venda:")

col3, col4 = st.columns(2)
with col3:
    fys_gelada = st.checkbox("FYS está gelada na geladeira?")
    fys_altura_olhos = st.checkbox("FYS está na altura dos olhos dos clientes?")
with col4:
    exposicao_quente = st.checkbox("Tem FYS quente exposta no balcão de pães/caixa?")
    comunicacao_visual = st.checkbox("Há cartazes, displays de mesa ou FYS no cardápio?")
st.markdown("</div>", unsafe_allow_html=True)

# --- SEÇÃO 3: LÓGICA DE PRIORIZAÇÃO (SCORE) ---
st.markdown("### 📈 3. Classificação de Potencial")

# Lógica de negócio para definir o potencial do PDV
score = 0
if vende_heineken == "Sim":
    score += 3
if fluxo_clientes == "Alto":
    score += 3
elif fluxo_clientes == "Médio":
    score += 1.5

if fys_gelada:
    score += 1
if exposicao_quente:
    score += 1
if comunicacao_visual:
    score += 1

if score >= 7:
    potencial = "Alto Potencial 🌟 (Foco Máximo de Ativação)"
    cor_potencial = "#4caf50"
elif 4 <= score < 7:
    potencial = "Médio Potencial ⚡ (Oportunidade de Crescimento)"
    cor_potencial = "#ff9800"
else:
    potencial = "Baixo Potencial 💤 (Acompanhar e Melhorar Visibilidade)"
    cor_potencial = "#f44336"

st.markdown(
    f"<div class='card' style='border-left: 6px solid {cor_potencial};'>"
    f"O potencial deste PDV para FYS foi classificado como: <br>"
    f"<span style='color: {cor_potencial}; font-size: 20px; font-weight: bold;'>{potencial}</span>"
    f"</div>",
    unsafe_allow_html=True
)

# --- SEÇÃO 4: INTEGRAÇÃO COM GEMINI API ---
st.markdown("### 🤖 4. Plano de Ação Personalizado")
st.write("Clique no botão abaixo para gerar uma estratégia sob medida usando IA com base no contexto da marca FYS.")

if st.button("Gerar Estratégia FYS"):
    if not api_key:
        st.error("❌ Não foi possível gerar a estratégia: Chave de API do Gemini não configurada. Por favor, adicione-a na barra lateral esquerda.")
    elif not nome_pdv:
        st.warning("⚠️ Por favor, preencha o nome do Ponto de Venda no formulário acima.")
    else:
        # Configurar a API do Gemini
        genai.configure(api_key=api_key)
        
        # Definição do Prompt de Sistema com base no repositório de inspiração
        system_instruction = """
        Você é o "FYS Copiloto de PDV", um assistente especialista em trade marketing e vendas para o refrigerante FYS (Grupo HEINEKEN).
        Seu objetivo é analisar o diagnóstico de uma padaria e sugerir ações de ativação baratas, criativas e no tom de voz da marca FYS.

        Seu tom de voz deve ser igual ao da FYS: leve, descontraído, com uma pitada de autoironia ("Menos marketing, mais sabor"), mas focado em resultados práticos para o vendedor.

        Diretrizes de Ativação baseadas na Live FYS:
        1. "Produto escondido não faz milagre": Se a FYS estiver no fundo da geladeira ou escondida, sugira colocá-la na altura dos olhos ou ao lado da Heineken (gatilho de associação de marca).
        2. "Aproveite a fila do pão": Padarias têm pico de fluxo de manhã/tarde. Expor FYS quente perto do balcão de pães gera curiosidade e experimentação.
        3. "Degustação de balcão": Se o dono da padaria for resistente, sugira que o vendedor ofereça amostras de copos pequenos (shot) para os clientes que aguardam na fila.
        4. "O trunfo Heineken": Se o PDV já vende Heineken, lembre o vendedor de usar isso como argumento (mesmo caminhão de entrega, facilidade de faturamento, força do grupo).
        """
        
        # Montagem dos dados recolhidos do formulário
        prompt_usuario = f"""
        Gere uma estratégia personalizada para o PDV com os seguintes dados:
        - Nome do PDV: {nome_pdv}
        - Vende cerveja Heineken: {vende_heineken}
        - Fluxo diário de clientes: {fluxo_clientes}
        - FYS está gelada: {'Sim' if fys_gelada else 'Não'}
        - FYS está na altura dos olhos: {'Sim' if fys_altura_olhos else 'Não'}
        - Tem exposição quente no caixa/balcão de pão: {'Sim' if exposicao_quente else 'Não'}
        - Tem comunicação visual (cardápio, display): {'Sim' if comunicacao_visual else 'Não'}

        Formate seu output usando Markdown contendo:
        1. **Diagnóstico da Padaria**: Um breve parágrafo analisando o cenário atual.
        2. **3 Ações Rápidas de Baixo Custo**: Três ideias baratas para o vendedor aplicar hoje mesmo nesta padaria.
        3. **Argumento FYS do Dia**: Uma frase persuasiva (no tom FYS de brincar com si mesma) para o vendedor falar para o dono da padaria.
        """
        
        with st.spinner("Conectando ao Gemini e gerando insights..."):
            try:
                # Instancia o modelo Gemini 1.5 Flash
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=system_instruction
                )
                
                # Gera o conteúdo
                response = model.generate_content(prompt_usuario)
                
                # Exibe a resposta
                st.success("✨ Estratégia Gerada com Sucesso!")
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Ocorreu um erro ao conectar com o Gemini: {e}")
                st.info("Verifique se sua API Key está correta e ativa.")
