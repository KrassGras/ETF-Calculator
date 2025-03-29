import streamlit as st
import pandas as pd

def berechne_Wert(P, r, t,  M):
    endkapital = P * ((1 + r) ** t) + M * 12 * (((1 + r) ** t) - 1) / r
    return endkapital



st.title("ETF-Rechner")
st.write("Einamlige Anlage in €")
einamligeAnlage = st.text_input("Einmalige Anlage in €")
st.write("montaliche Einzahlungen in €")
montatlich = st.text_input("monatliche Einzahlungen in €")
st.write("Laufzeit")
laufzeit = st.text_input("Laufzeit in Jahre")
st.write("Rendite")
rendite = st.text_input("Rendite %")
chartdata = dict()

endkapital = berechne_Wert(int(einamligeAnlage), float(rendite)/100, 1, int(montatlich))
chartdata[1] = endkapital

P = int(einamligeAnlage)
M = int(montatlich)
t = int(laufzeit)
r = float(rendite) / 100
eingezahlterBetrag = P
for jahr in range(1, t + 1):
    endkapital = berechne_Wert(endkapital, r, 1, M)  # Monatliche Einzahlungen werden jährlich addiert
    eingezahlterBetrag += M*12
    chartdata[jahr] = endkapital

reineRendite = endkapital - eingezahlterBetrag

data = pd.DataFrame({
    "Jahr": chartdata.keys(),
    "wert": chartdata.values()
})


st.line_chart(data.set_index("Jahr"))

col1, col2, col3 = st.columns(3)
col1.metric(label="Endvermögen", value=f"{round(endkapital)}€")
col2.metric(label="eingezahler Betrag", value=f"{eingezahlterBetrag}€")
col3.metric(label="Rendite", value=f"{round(reineRendite)}€")




