# Clean Power Ecosystem Insights Agent — MVP Demo

**User Story B: Data Insights Agent**
Audience: CTO & Relationship Managers

---

## Setup

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Run the app**
```bash
streamlit run app.py
```

---

## How to Use

1. **Upload files** — Use the sidebar to upload the three CSVs from the `data/` folder (`Entity_Master.csv`, `Relationship_Data.csv`, `Segment.csv`). The app will run on sample data if no files are uploaded.
2. **Enter a query** — The default query targets HSBC Sustainable Finance. Modify as needed.
3. **Click Generate Insights** — The agent will display step-by-step processing and output the insight report with validation status and source traceability.

---

## Project Structure

```
opportunity-agent-demo/
├── app.py                  # Streamlit UI
├── rules.py                # Opportunity surfacing logic
├── requirements.txt        # Dependencies
├── README.md               # This file
└── data/
    ├── Entity_Master.csv   # Entity registry with segment classification
    ├── Relationship_Data.csv  # Cross-entity relationship mappings
    └── Segment.csv         # Eight ecosystem segments and banking solutions
```

---

## Demo Notes

- Logic is rule-based and deterministic for demo reliability.
- Validation badges are illustrative; full validation engine is out of scope for this phase.
- All outputs must be reviewed by the RM before client use.
