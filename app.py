import pandas as pd
import streamlit as st

# Nastavení stránky
st.set_page_config(
    page_title="Partners - Team Ranklist | Petr Vavřík",
    page_icon="📊",
    layout="wide",
)

# Vlastní CSS pro moderní vzhled
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #00778b;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Hlavička aplikace
st.title("🚀 Partners – Měsíční Ranklist Týmu")
st.markdown(
    "**Ředitelství:** D1 Petr Vavřík | **Zpracovatel:** Eliška Burdková"
)
st.markdown("---")

# Boční panel
with st.sidebar:
    st.header("⚙️ Ovládání ranklistu")
    selected_month = st.selectbox(
        "Vyber období:", ["Duben 2026", "Květen 2026", "Březen 2026"]
    )
    st.markdown("---")
    st.subheader("📁 Nahrát data z Prometeuse")
    uploaded_file = st.file_uploader(
        "Vlož exportní soubor (.xls / .html / .csv)", type=["xls", "html", "csv"]
    )

# Hlavní záložky
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "🏆 Osobní výkony (BJ)",
        "💰 Celkové AUM",
        "💳 Aktivní BÚ",
        "📈 Nové analýzy",
        "✏️ Ruční úpravy",
    ]
)

with tab1:
    st.subheader(f"Osobní výkony – {selected_month}")
    data_osobni = {
        "Pořadí": [1, 2, 3, 4, 5, 6, 7],
        "Jméno": [
            "Holub Vojtěch",
            "Kuchař Jakub",
            "Kořenková Michaela",
            "Heřman Pavel",
            "Fohlerová Martina",
            "Vavřík Petr",
            "Žanta Jan",
        ],
        "Pozice": [
            "VSC-X",
            "VSC-III",
            "VSC-VI",
            "KFF",
            "FR",
            "D1",
            "SP",
        ],
        "BJ osobní": [2105.00, 1040.54, 843.14, 771.10, 728.62, 605.65, 537.09],
        "Počet smluv": [58, 59, 36, 9, 60, 14, 21],
    }
    df_osobni = pd.DataFrame(data_osobni)
    st.dataframe(df_osobni, use_container_width=True, hide_index=True)
    st.bar_chart(df_osobni.set_index("Jméno")["BJ osobní"])

with tab2:
    st.subheader(f"Celkové AUM pod správou – {selected_month}")
    data_aum = {
        "Poradce": [
            "Holub Vojtěch",
            "Kapr David",
            "Vrána Filip",
            "Fohlerová Martina",
            "Žanta Jan",
            "Vavřík Petr",
        ],
        "AUM (Kč)": [
            152568168,
            98830822,
            60161871,
            47532411,
            47222935,
            42175920,
        ],
    }
    st.dataframe(pd.DataFrame(data_aum), use_container_width=True, hide_index=True)

with tab3:
    st.subheader(f"Aktivní BÚ – {selected_month}")
    st.info("Zde se zobrazují aktivní BÚ dle pravidel skupiny.")

with tab4:
    st.subheader(f"Nové analýzy – {selected_month}")
    st.info("Přehled zpracovaných analýz a poměrů.")

with tab5:
    st.subheader("✏️ Ruční úpravy týmu")
    st.text_input("Přidat nováčka / upravit data")
