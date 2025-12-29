
# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Studio Legale Ruocco", page_icon="⚖️")

# --- BROCARDI E MOTIVAZIONE ---
frasi = [
    "«Iustitia est constans et perpetua voluntas ius suum cuique tribuendi»",
    "«Pacta sunt servanda» - Ricorda le fatture di oggi!",
    "«Ad impossibilia nemo tenetur» - Gestisci il tuo tempo con saggezza.",
    "L'eccellenza è un'abitudine, non un atto. Buon lavoro Avvocato!"
]

st.sidebar.title("⚖️ Studio Ruocco")
st.sidebar.info(random.choice(frasi))

# --- DATABASE CONTRATTI FISSI ---
contratti = [
    {"giorno": 3, "cliente": "Art & Leisure"},
    {"giorno": 7, "cliente": "Società Telema srl"},
    {"giorno": 10, "cliente": "Dottoressa Lancellotta"},
    {"giorno": 24, "cliente": "Fabio Store srl"},
    {"giorno": 26, "cliente": "Società Zaco srl"},
    {"giorno": 29, "cliente": "Società Golfo srl"},
    {"giorno": 30, "cliente": "Società Uomini & Affari srl"}
]

# --- MENU PRINCIPALE ---
scelta = st.sidebar.radio("Vai a:", ["🏠 Home", "📅 Scadenziario Fatture", "💰 Incassi e Spese", "🚄 Utility Viaggio"])

if scelta == "🏠 Home":
    st.title("Bentornato, Avvocato Ruocco")
    st.write(f"Oggi è il {datetime.now().strftime('%d/%m/%Y')}")
    st.info("«Iura novit curia» - Il giudice conosce le leggi. Tu pensa ai fatti.")

elif scelta == "📅 Scadenziario Fatture":
    st.header("Scadenze Fatturazione Mensile")
    oggi = datetime.now().day
    for c in contratti:
        if oggi == c['giorno']:
            st.error(f"🔴 EMETTERE OGGI: {c['cliente']}")
        elif c['giorno'] > oggi:
            st.warning(f"🟡 Prossima: {c['cliente']} (Giorno {c['giorno']})")
        else:
            st.success(f"✅ Gestita: {c['cliente']} (Giorno {c['giorno']})")

elif scelta == "💰 Incassi e Spese":
    st.header("Gestione Economica Rapida")
    st.write("Inserisci i dati per il tuo registro:")
    tipo = st.selectbox("Operazione", ["Incasso Ricevuto", "Spesa Studio/Viaggio"])
    importo = st.number_input("Importo (€)", min_value=0.0)
    desc = st.text_input("Descrizione")
    if st.button("Registra"):
        st.success("Registrazione simulata con successo!")

elif scelta == "🚄 Utility Viaggio":
    st.header("Trasferte Roma / Lavoro")
    st.link_button("Biglietti Trenitalia", "https://www.trenitalia.com/")
    st.link_button("Biglietti Italo", "https://www.italotreno.it/")
