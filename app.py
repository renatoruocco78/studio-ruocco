<!-- end list -->
import streamlit as st
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="Studio Legale Ruocco", page_icon="⚖️")

# --- BROCARDI E MOTIVAZIONE ---
frasi = [
    "«Iustitia est constans et perpetua voluntas ius suum cuique tribuendi»",
    "«Pacta sunt servanda» - Ricorda le fatture di oggi!",
    "«Ad impossibilia nemo tenetur» - Gestisci il tuo tempo con saggezza.",
    "L'eccellenza è un'abitudine, non un atto. Buon lavoro Avvocato!"
]
import random
st.sidebar.title("⚖️ Studio Ruocco")
st.sidebar.info(random.choice(frasi))

# --- LOGICA SCADENZIARIO FATTURE ---
contratti = [
    {"giorno": 3, "cliente": "Art & Leisure"},
    {"giorno": 7, "cliente": "Società Telema srl"},
    {"giorno": 10, "cliente": "Dottoressa Lancellotta"},
    {"giorno": 24, "cliente": "Fabio Store srl"},
    {"giorno": 26, "cliente": "Società Zaco srl"},
    {"giorno": 29, "cliente": "Società Golfo srl"},
    {"giorno": 30, "cliente": "Società Uomini & Affari srl"}
]

# --- MENU ---
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📅 Scadenziario Fatture", "💰 Incassi e Spese", "🚄 Utility Viaggio"])

if scelta == "🏠 Home":
    st.title("Bentornato, Avvocato Ruocco")
    st.write(f"Oggi è il {datetime.now().strftime('%d/%m/%Y')}")
    st.image("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?q=80&w=500&auto=format&fit=crop") # Immagine elegante

elif scelta == "📅 Scadenziario Fatture":
    st.header("Scadenze Fatturazione")
    oggi = datetime.now().day
    for c in contratti:
        if oggi == c['giorno']:
            st.error(f"🔴 OGGI: Emettere fattura per {c['cliente']}")
        elif c['giorno'] > oggi:
            st.warning(f"🟡 Prossima: {c['cliente']} (Giorno {c['giorno']})")
        else:
            st.success(f"🟢 Gestita: {c['cliente']} (Giorno {c['giorno']})")

elif scelta == "💰 Incassi e Spese":
    st.header("Gestione Economica")
    tipo = st.selectbox("Cosa vuoi registrare?", ["Incasso Ricevuto", "Spesa (Treno/Taxi/Altro)"])
    importo = st.number_input("Importo (€)", min_value=0.0)
    nota = st.text_input("Descrizione (es. Fattura n.1 o Taxi Roma)")
    if st.button("Salva nel Registro"):
        st.balloons()
        st.success("Dato registrato localmente!")

elif scelta == "🚄 Utility Viaggio":
    st.header("Missione Roma")
    st.write("Link rapidi per i tuoi spostamenti:")
    st.link_button("Prenota Italo", "https://www.italotreno.it/")
    st.link_button("Prenota Trenitalia", "https://www.trenitalia.com/")
