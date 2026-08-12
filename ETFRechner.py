import streamlit as st
import pandas as pd

def berechne_Wert(P, r, t,  M):
    if r == 0:
        return P + M * 12 * t
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


if not einamligeAnlage:
    P = 0
else:
    P = int(einamligeAnlage)
if not montatlich:
    M = 0
else:
    M = int(montatlich)

if not laufzeit:
    t = 0
else:
    t = int(laufzeit)

if not rendite:
    r = 0
else:
    r = float(rendite) / 100

endkapital = P
eingezahlterBetrag = P
chartdata[0] = P
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


st.header("Sparraten-Rechner")
st.write("Berechne die monatliche Sparrate, die du brauchst, um dein Vermögensziel zu erreichen. Einmalige Anlage und Laufzeit werden von oben übernommen.")
vermoegensziel = st.text_input("Vermögensziel in €")
zielRendite = st.text_input("erwartete jährliche Rendite in %", value="7")

if not vermoegensziel:
    ziel = 0
else:
    ziel = int(vermoegensziel)
if not zielRendite:
    zr = 0.07
else:
    zr = float(zielRendite) / 100

if ziel > 0:
    if t <= 0:
        st.write("Bitte oben eine Laufzeit angeben.")
    else:
        wachstum = (1 + zr) ** t
        if zr == 0:
            benoetigteRate = (ziel - P) / (12 * t)
        else:
            benoetigteRate = (ziel - P * wachstum) * zr / (12 * (wachstum - 1))
        if benoetigteRate <= 0:
            st.write(f"Deine einmalige Anlage von {P}€ reicht bereits aus, um das Ziel von {ziel}€ in {t} Jahren zu erreichen.")
        else:
            st.metric(label="benötigte monatliche Sparrate", value=f"{round(benoetigteRate, 2)}€")


st.write("Die hier bereitgestellten Berechnungen dienen nur zur Orientierung und erfolgen ohne Gewähr. Für finanzielle Entscheidungen sollten zusätzliche Quellen oder professionelle Beratung hinzugezogen werden.")

