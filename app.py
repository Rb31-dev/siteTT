import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Vault Store", page_icon="🛍️", layout="wide")

# 2. Injeção de CSS para o estilo rústico clássico
st.markdown("""
<style>
    /* Força fundo claro global */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAFAFA !important;
    }
    
    /* Barra Lateral Clara */
    [data-testid="stSidebar"] {
        background-color: #F0F0F0 !important;
        border-right: 2px solid #111111 !important;
    }

    /* Textos padrão do site */
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .secondary-text {
        color: #555555 !important;
        font-size: 0.9em;
        font-weight: 600;
    }

    /* Cards e Caixas na Sidebar e Vitrine */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 6px !important;
        border: 2px solid #111111 !important;
        background-color: #FFFFFF !important;
        box-shadow: 4px 4px 0px #111111 !important;
        padding: 14px;
        margin-bottom: 15px;
    }

    /* Estilo dos Botões */
    div.stButton > button {
        background-color: #1B2A4A !important;
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        box-shadow: 3px 3px 0px #111111 !important;
        padding: 8px 16px !important;
        transition: all 0.1s ease !important;
    }

    /* Texto interno dos Botões em Branco Puro */
    div.stButton > button p, 
    div.stButton > button span, 
    div.stButton > button div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.9em !important;
        letter-spacing: 0.5px !important;
    }

    /* Hover dos Botões */
    div.stButton > button:hover {
        background-color: #111111 !important;
        box-shadow: 4px 4px 0px #1B2A4A !important;
    }

    div.stButton > button:hover p,
    div.stButton > button:hover span {
        color: #FFFFFF !important;
    }

    /* Inputs e Selects */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        background-color: #FFFFFF !important;
    }

    /* Estilização do Menu Navegação do Cabeçalho */
    div[data-testid="stRadio"] > div {
        background-color: #FFFFFF;
        border: 2px solid #111111;
        padding: 8px 15px;
        border-radius: 6px;
        box-shadow: 3px 3px 0px #111111;
    }
</style>
""", unsafe_allow_html=True)

# 3. Estado da Aplicação (Carrinho e Produtos)
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Função para resetar os produtos para o padrão atualizado (múltiplas categorias)
def resetar_produtos():
    st.session_state.produtos = [
        # --- TÊNIS ---
        {
            "id": 1,
            "categoria": "👟 Tênis",
            "nome": "Air Jordan 1 Retro High",
            "marca": "Nike",
            "cor": "Vermelho",
            "tamanhos": [39, 40, 41, 42],
            "preco": 1299.90,
            "imagem": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500",
        },
        {
            "id": 2,
            "categoria": "👟 Tênis",
            "nome": "Adidas Yeezy Boost 350",
            "marca": "Adidas",
            "cor": "Preto",
            "tamanhos": [38, 39, 40, 41, 42, 43],
            "preco": 1499.90,
            "imagem": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500",
        },
        {
            "id": 3,
            "categoria": "👟 Tênis",
            "nome": "Puma Suede Classic",
            "marca": "Puma",
            "cor": "Preto",
            "tamanhos": [37, 38, 39, 40],
            "preco": 399.90,
            "imagem": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=500",
        },
        {
            "id": 4,
            "categoria": "👟 Tênis",
            "nome": "New Balance 550",
            "marca": "New Balance",
            "cor": "Verde",
            "tamanhos": [40, 41, 42, 43, 44],
            "preco": 899.90,
            "imagem": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500",
        },
        # --- CAMISAS ---
        {
            "id": 5,
            "categoria": "👕 Camisas",
            "nome": "Camiseta Oversized Streetwear",
            "marca": "Nike",
            "cor": "Preto",
            "tamanhos": ["P", "M", "G", "GG"],
            "preco": 149.90,
            "imagem": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500",
        },
        {
            "id": 6,
            "categoria": "👕 Camisas",
            "nome": "Camisa Polo Classic",
            "marca": "Lacoste",
            "cor": "Branco",
            "tamanhos": ["M", "G"],
            "preco": 349.90,
            "imagem": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=500",
        },
        # --- INFORMÁTICA ---
        {
            "id": 7,
            "categoria": "💻 Informática",
            "nome": "Teclado Mecânico RGB",
            "marca": "Redragon",
            "cor": "Preto",
            "tamanhos": ["Único"],
            "preco": 299.90,
            "imagem": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
        },
        {
            "id": 8,
            "categoria": "💻 Informática",
            "nome": "Mouse Gamer Sem Fio",
            "marca": "Logitech",
            "cor": "Preto",
            "tamanhos": ["Único"],
            "preco": 450.00,
            "imagem": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=500",
        },
    ]

# Garante que a lista de produtos exista no estado
if "produtos" not in st.session_state:
    resetar_produtos()

# --- CABEÇALHO DA PÁGINA PRINCIPAL ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("VAULT STORE 🛍️")
    st.markdown("<p class='secondary-text' style='font-size: 1.1em;'>Sua vitrine de Sneakers, Roupas e Tecnologia</p>", unsafe_allow_html=True)

with col_head2:
    st.write("")
    if st.button("🔄 Resetar Catálogo", use_container_width=True):
        resetar_produtos()
        st.toast("Catálogo atualizado para a nova versão!", icon="✅")
        st.rerun()

st.write("---")

# --- MENU DE NAVEGAÇÃO SUPERIOR (CABEÇALHO COM ABAS) ---
categoria_selecionada = st.radio(
    "Navegue pelas categorias:",
    options=["👟 Tênis", "👕 Camisas", "💻 Informática"],
    horizontal=True,
    label_visibility="collapsed"
)

st.write("")

# --- SIDEBAR (BARRA LATERAL COM CAIXAS) ---
with st.sidebar:
    st.title("🛒 SEU CARRINHO")
    
    # CAIXA 1: Conteúdo do Carrinho
    with st.container(border=True):
        if not st.session_state.carrinho:
            st.markdown("<p class='secondary-text' style='margin:0;'>O carrinho está vazio.</p>", unsafe_allow_html=True)
        else:
            total = 0
            for item in st.session_state.carrinho:
                st.markdown(f"**{item['nome']}**")
                st.markdown(f"<span class='secondary-text'>R$ {item['preco']:.2f}</span>", unsafe_allow_html=True)
                total += item["preco"]
                st.write("---")
            
            st.markdown(f"#### Total: R$ {total:.2f}")
            if st.button("FINALIZAR COMPRA", use_container_width=True):
                st.balloons()
                st.success("Pedido realizado!")
                st.session_state.carrinho = []
                st.rerun()

    st.write("")
    st.title("⚡ FILTROS")

    # Filtra produtos apenas da categoria ativa para preencher as opções dos seletores
    produtos_cat_ativa = [p for p in st.session_state.produtos if p.get("categoria", "👟 Tênis") == categoria_selecionada]

    marcas_opts = ["Todas"] + sorted(list(set([t.get("marca", "Outra") for t in produtos_cat_ativa])))
    cores_opts = ["Todas"] + sorted(list(set([t.get("cor", "Única") for t in produtos_cat_ativa])))
    
    # Busca de tamanhos com segurança
    todos_tamanhos = set()
    for t in produtos_cat_ativa:
        tams = t.get("tamanhos", [])
        if isinstance(tams, list):
            for tam in tams:
                todos_tamanhos.add(str(tam))
    
    tamanhos_opts = ["Todos"] + sorted(list(todos_tamanhos))

    # Faixa de preço com segurança
    precos = [t.get("preco", 0.0) for t in produtos_cat_ativa]
    min_p_db = float(min(precos)) if precos else 0.0
    max_p_db = float(max(precos)) if precos else 2000.0

    # CAIXA 2: Painel de Filtros Avançados
    with st.container(border=True):
        st.subheader(f"Filtrar em {categoria_selecionada}")
        
        f_marca = st.selectbox("Marca", marcas_opts)
        f_cor = st.selectbox("Cor", cores_opts)
        f_tamanho = st.selectbox("Tamanho / Opção", tamanhos_opts)
        
        st.write("---")
        st.markdown("**Faixa de Preço (R$)**")
        f_preco = st.slider(
            "Selecione o limite",
            min_value=0.0,
            max_value=float(max(max_p_db, 2000.0)),
            value=(min_p_db, max_p_db if max_p_db > 0 else 2000.0),
            step=50.0
        )

# --- PAINEL DE CADASTRO DE NOVOS PRODUTOS ---
with st.expander("➕ Adicionar Novo Produto ao Catálogo"):
    with st.form("form_novo_produto", clear_on_submit=True):
        st.subheader("Cadastrar Produto")
        novo_nome = st.text_input("Nome do Produto", placeholder="Ex: Monitor Gaming 144Hz")
        
        col_cat, col_m = st.columns(2)
        with col_cat:
            nova_categoria = st.selectbox("Categoria", ["👟 Tênis", "👕 Camisas", "💻 Informática"])
        with col_m:
            nova_marca = st.text_input("Marca", value="Generico")

        col_c, col_p = st.columns(2)
        with col_c:
            nova_cor = st.text_input("Cor Principal", value="Preto")
        with col_p:
            novo_preco = st.number_input("Preço (R$)", min_value=0.0, value=199.90, step=10.0)

        novos_tams_str = st.text_input("Tamanhos / Variantes (separados por vírgula)", value="P, M, G, GG ou 39, 40, 41")
        nova_imagem = st.text_input("URL da Imagem", value="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=500")
        
        btn_cadastrar = st.form_submit_button("CADASTRAR PRODUTO", use_container_width=True)
        
        if btn_cadastrar:
            if novo_nome and nova_cor:
                novo_id = len(st.session_state.produtos) + 1
                
                # Trata a entrada de tamanhos digitados
                tams_array = [t.strip() for t in novos_tams_str.split(",") if t.strip()]
                
                novo_item = {
                    "id": novo_id,
                    "categoria": nova_categoria,
                    "nome": novo_nome,
                    "marca": nova_marca,
                    "cor": nova_cor,
                    "tamanhos": tams_array if tams_array else ["Padrão"],
                    "preco": novo_preco,
                    "imagem": nova_imagem
                }
                st.session_state.produtos.append(novo_item)
                st.success(f"Produto '{novo_nome}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, preencha o nome e a cor do produto.")

st.write("---")

# --- BARRA DE BUSCA RÁPIDA ---
busca = st.text_input("🔍 Buscar por produto", placeholder="Digite o nome do produto...")

st.write("---")

# --- LÓGICA DE FILTRAGEM SEGURA ---
# 1. Filtra pela categoria selecionada na barra superior
produtos_filtrados = [t for t in st.session_state.produtos if t.get("categoria", "👟 Tênis") == categoria_selecionada]

# 2. Filtro por Marca
if f_marca != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t.get("marca") == f_marca]

# 3. Filtro por Cor
if f_cor != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t.get("cor") == f_cor]

# 4. Filtro por Tamanho
if f_tamanho != "Todos":
    produtos_filtrados = [
        t for t in produtos_filtrados 
        if f_tamanho in [str(tam) for tam in t.get("tamanhos", [])]
    ]

# 5. Filtro por Faixa de Preço
produtos_filtrados = [
    t for t in produtos_filtrados 
    if f_preco[0] <= t.get("preco", 0.0) <= f_preco[1]
]

# 6. Filtro por Texto da Busca
if busca:
    produtos_filtrados = [
        t for t in produtos_filtrados 
        if busca.lower() in t.get("nome", "").lower()
    ]

# --- VITRINE DE PRODUTOS ---
st.heading = st.subheader(f"Catálogo de {categoria_selecionada}")

if not produtos_filtrados:
    st.info("Nenhum produto encontrado nesta categoria com esses filtros.")
else:
    cols = st.columns(3)
    for idx, item in enumerate(produtos_filtrados):
        col = cols[idx % 3]
        
        with col:
            with st.container(border=True):
                st.image(item.get("imagem", ""), use_container_width=True)
                st.markdown(f"### {item.get('nome', 'Sem Nome')}")
                
                marca_str = item.get('marca', 'Indefinida')
                cor_str = item.get('cor', 'Padrão')
                st.markdown(f"<span class='secondary-text'>Marca: {marca_str} | Cor: {cor_str}</span>", unsafe_allow_html=True)
                
                tams_list = item.get('tamanhos', [])
                tams_str = ', '.join(map(str, tams_list)) if tams_list else 'Consulte'
                st.markdown(f"<span class='secondary-text'>Tamanhos/Opções: {tams_str}</span>", unsafe_allow_html=True)
                
                preco_val = item.get('preco', 0.0)
                st.markdown(f"<h4 style='color: #111111; margin-top: 8px;'>R$ {preco_val:.2f}</h4>", unsafe_allow_html=True)
                
                if st.button("ADICIONAR AO CARRINHO", key=f"btn_{item.get('id', idx)}", use_container_width=True):
                    st.session_state.carrinho.append(item)
                    st.toast(f"{item.get('nome')} adicionado ao carrinho!", icon="✅")
                    st.rerun()
