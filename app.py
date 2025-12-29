import streamlit as st
import pandas as pd
import random
from datetime import datetime

# 1. CONFIGURAZIONE PAGINA (Deve essere la prima istruzione Streamlit)
st.set_page_config(
    page_title="Studio Legale Ruocco", 
    page_icon="⚖️",
    layout="wide"
)

# 2. INIZIALIZZAZIONE SESSION STATE
# Serve a non perdere i dati delle spese quando interagisci con la pagina
if 'lista_spese' not in st.session_state:
    st.session_state['lista_spese'] = []

# 3. DATI E COSTANTI
frasi = [
    "«Iustitia est constans et perpetua voluntas ius suum cuique tribuendi»",
    "«Pacta sunt servanda» - Ricorda le fatture di oggi!",
    "«Ad impossibilia nemo tenetur» - Gestisci il tuo tempo con saggezza.",
    "L'eccellenza è un'abitudine, non un atto. Buon lavoro Avvocato!",
    "«Dura lex, sed lex» - La legge è dura, ma è la legge."
]

contratti = [
    {"giorno": 3, "cliente": "Art & Leisure"},
    {"giorno": 7, "cliente": "Società Telema srl"},
    {"giorno": 10, "cliente": "Dottoressa Lancellotta"},
    {"giorno": 24, "cliente": "Fabio Store srl"},
    {"giorno": 26, "cliente": "Società Zaco srl"},
    {"giorno": 29, "cliente": "Società Golfo srl"},
    {"giorno": 30, "cliente": "Società Uomini & Affari srl"}
]

# 4. BARRA LATERALE (SIDEBAR)
st.sidebar.title("⚖️ Studio Ruocco")
st.sidebar.info(random.choice(frasi))

scelta = st.sidebar.radio(
    "Navigazione:", 
    ["🏠 Home", "📅 Scadenziario Fatture", "💰 Incassi e Spese", "🚄 Utility Viaggio"]
)

# 5. LOGICA DELLE PAGINE

# --- HOME ---
if scelta == "🏠 Home":
    st.title("Bentornato, Avvocato Ruocco")
    data_oggi = datetime.now().strftime('%d/%m/%Y')
    st.write(f"### 🗓️ Oggi è il {data_oggi}")
    st.divider()
    st.info("💡 «Iura novit curia» - Il giudice conosce le leggi. Tu pensa ai fatti.")
    
    # Un piccolo riepilogo rapido
    st.write("#### Panoramica veloce:")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Fatture in db", len(contratti))
    with col2:
        st.metric("Operazioni registrate oggi", len(st.session_state['lista_spese']))

# --- SCADENZIARIO ---
elif scelta == "📅 Scadenziario Fatture":
    st.header("Scadenze Fatturazione Mensile")
    oggi = datetime.now().day
    
    # Creiamo una lista per visualizzare i dati in modo pulito
    st.write(f"Giorno corrente: **{oggi}**")
    
    count_scadenze = 0
    
    for c in contratti:
        col_a, col_b = st.columns([1, 4])
        with col_a:
            st.write(f"🗓️ Giorno {c['giorno']}")
        with col_b:
            if today_match := (oggi == c['giorno']):
                st.error(f"🔴 EMETTERE OGGI: **{c['cliente']}**")
                count_scadenze += 1
            elif c['giorno'] > oggi:
                st.warning(f"🟡 Prossima: {c['cliente']}")
            else:
                st.success(f"✅ Gestita/Passata: {c['cliente']}")
    
    if count_scadenze == 0:
        st.success("Nessuna fattura urgente da emettere oggi.")

# --- INCASSI E SPESE ---
elif scelta == "💰 Incassi e Spese":
    st.header("Gestione Economica Rapida")
    
    col_input, col_output = st.columns([1, 2])
    
    # Modulo di inserimento
    with col_input:
        st.subheader("Nuova voce")
        with st.form("form_spese"):
            tipo = st.selectbox("Operazione", ["Incasso Ricevuto", "Spesa Studio/Viaggio"])
            importo = st.number_input("Importo (€)", min_value=0.0, format="%.2f")
            desc = st.text_input("Descrizione", placeholder="Es. Treno o Fattura n.1")
            submitted = st.form_submit_button("Registra")
            
            if submitted:
                # Aggiunge alla "memoria" della sessione
                nuova_riga = {
                    "Orario": datetime.now().strftime("%H:%M"),
                    "Tipo": tipo,
                    "Descrizione": desc,
                    "Importo": importo
                }
                st.session_state['lista_spese'].append(nuova_riga)
                st.success("Inserito!")
    
    # Tabella riepilogativa
    with col_output:
        st.subheader("Movimenti Sessione Attuale")
        if st.session_state['lista_spese']:
            df = pd.DataFrame(st.session_state['lista_spese'])
            st.dataframe(df, use_container_width=True)
            
            # Calcolo totali
            incassi = df[df['Tipo'] == "Incasso Ricevuto"]['Importo'].sum()
            uscite = df[df['Tipo'] == "Spesa Studio/Viaggio"]['Importo'].sum()
            saldo = incassi - uscite
            
            st.metric("Saldo Sessione (€)", f"{saldo:.2f}")
        else:
            st.info("Nessuna operazione registrata finora.")

# --- UTILITY VIAGGIO ---
elif scelta == "🚄 Utility Viaggio":
    st.header("Trasferte Roma / Lavoro")
    st.write("Link rapidi per la gestione trasferte.")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.link_button("🚆 Trenitalia", "https://www.trenitalia.com/", use_container_width=True)
    with c2:
        st.link_button("🚄 Italo Treno", "https://www.italotreno.it/", use_container_width=True)
    with c3:
        st.link_button("⚖️ PST Giustizia", "https://pst.giustizia.it/", use_container_width=True)
