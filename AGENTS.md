# ETF-Calculator

A small Streamlit app for ETF investment calculations. German UI.

## Structure

- Single-file app: `ETFRechner.py` — everything lives here.
- `requirements.txt` — streamlit, pandas.
- Deployed on Streamlit Community Cloud, auto-redeploys from `main`.

## App layout

Two tabs via `st.tabs`:

1. **ETF-Rechner** — compound-interest calculator: one-time investment,
   monthly deposits, duration, return rate. Shows a line chart plus final
   value, total deposits, and profit metrics.
2. **Sparraten-Rechner** — goal calculator: net worth goal, current net
   worth, target duration, expected yearly return (default 7%). Computes
   the required monthly saving rate. Self-contained — shares no inputs
   with the first tab.

## Financial model

- Annual compounding: `FV = P*(1+r)^t + M*12*((1+r)^t - 1)/r`.
  Monthly deposits are added once per year (no intra-year interest).
- The savings-rate calculator inverts the same formula, so both tabs are
  consistent with each other. Keep them consistent when changing either.
- `r == 0` must be special-cased (the formula divides by r).
- Empty inputs default to 0 (not 100% — that was a former bug).

## Conventions

- UI labels and user-facing text are German; some contain historical
  typos (e.g. "Einamlige") — fixing them is fine but not required.
- Variable names are German (`endkapital`, `eingezahlterBetrag`, ...).
- Inputs are `st.text_input` parsed with `int()`/`float()`.
- A liability disclaimer must stay visible below both tabs.

## Workflow

- Development happens on a feature branch, then fast-forward merged into
  `main` and pushed, since the live app deploys from `main`.
- Verify changes with `python3 -m py_compile ETFRechner.py` at minimum;
  for formula changes, round-trip check against the closed-form formula.
