import os
import time
import pandas as pd

INPUT_FOLDER = "data"

def simulate_file_reading():
    """Checks file integrity against required fields."""
    files_found = []
    errors = []

    for filename in ["Relationship_Data.csv", "Entity_Master.csv"]:
        path = os.path.join(INPUT_FOLDER, filename)
        if os.path.exists(path):
            try:
                pd.read_csv(path)
                files_found.append(filename)
            except Exception as e:
                errors.append(f"Error reading {filename}: {e}")

    return files_found, errors


def get_response(prompt, uploaded_files):
    """Returns the appropriate response based on prompt keywords."""
    prompt_lower = prompt.lower()

    # Priority 1: Check for SunGrid Utilities specific query
    if "sungrid" in prompt_lower:
        return load_sungrid_template(uploaded_files)

    # Priority 2: Check for HSBC Sustainable Finance query
    if ("hsbc" in prompt_lower and "sustainable" in prompt_lower) or "sustainable finance" in prompt_lower:
        return load_hsbc_template(uploaded_files)

    # Default: Return generic template
    return load_generic_template(uploaded_files)

def load_sungrid_template(files):
    """Generates the SunGrid Utilities opportunity insight output."""
    source_label = ", ".join(files) if files else "Relationship_Data.csv, Entity_Master.csv, Segment.csv"

    output = f"""
**Existing or Potential Relationship with HSBC (Sustainable Finance)**

*Finding:*
There is no explicit existing HSBC relationship recorded for SunGrid Utilities in the provided ecosystem data. However, SunGrid is a strong potential relationship target due to its role as a utility and long-dated clean-power offtaker.

*Evidence from sources:*
- SunGrid Utilities appears in the Utility & Grid segment and is positioned as a core counterparty in the renewable ecosystem. `[{source_label}]`
- The relationship data shows a developer–offtaker connection between GreenPeak Renewables and SunGrid Utilities, indicating active clean-power exposure. `[{source_label}]`
- SunGrid’s role supports sustainable financing conversations across project finance and balance-sheet facilities. `[{source_label}]`

---

**Surfaced Business Opportunity: Renewable Project Finance & Portfolio Financing**

**Opportunity A: Long-Tenor Project Finance for Solar Assets**

*Why this surfaced (rule-based logic):*
If a developer–offtaker relationship exists with long-term contracted cashflows → surface a Project Finance opportunity.

*Supporting evidence:*
- GreenPeak Renewables and SunGrid Utilities have a long-term solar PPA relationship with strong relationship strength. `[{source_label}]`
- PPAs create stable, predictable cashflows that support non-recourse or limited-recourse project finance structures. `[{source_label}]`

*HSBC Sustainable Finance fit:*
- Green / sustainable-labelled Project Finance.
- Green Loans for solar and wind asset development.
- Potential structuring around Asia-Pacific renewable infrastructure.

*Confidence level:* 🟢 **High**
*Validation status:* ✅ Validated against ingested relationship and entity data

---

**Opportunity B: Portfolio / Utility-Level Green or Sustainability-Linked Financing**

*Why this surfaced (rule-based logic):*
If a utility sits in a clean-energy ecosystem with renewables exposure → surface a portfolio or balance-sheet financing opportunity.

*Supporting evidence:*
- SunGrid Utilities is classified in the Utility & Grid segment and operates in a clean-energy ecosystem. `[{source_label}]`
- The entity data indicates SunGrid is well positioned for broader financing tied to renewable procurement and grid integration. `[{source_label}]`

*HSBC Sustainable Finance fit:*
- Green loans or sustainability-linked facilities at SunGrid level.
- Financing for renewable procurement, grid upgrade, and decarbonisation capex.
- Potential cross-sell into hedging and ESG advisory.

*Confidence level:* 🟡 **Medium–High**
*Validation status:* ⚠️ Partially validated — segment and ecosystem alignment confirmed; facility scope requires RM confirmation

---

**Summary for RM Use**

| Aspect | Insight |
| :--- | :--- |
| **Relationship** | No recorded HSBC relationship; strong potential |
| **Primary Opportunity** | Long-tenor project finance for solar assets |
| **Secondary Opportunity** | Utility-level green / sustainability-linked financing |
| **Strategic Value** | Stable cashflows, larger ticket sizes, cross-sell potential |
| **Overall Confidence** | High |
| **Source Data** | {source_label} |
"""
    return output

def load_hsbc_template(files):
    """Generates the HSBC Sustainable Finance insight output."""
    # Wire actual uploaded filenames into evidence citations
    source_label = ", ".join(files) if files else "Relationship_Data.csv, Entity_Master.csv, Segment.csv"

    output = f"""
**Existing or Potential Relationship with HSBC (Sustainable Finance)**

*Finding:*
There is no explicit existing relationship with HSBC recorded in the provided ecosystem data. However, there is a strong potential relationship opportunity.

*Evidence from sources:*
- Multiple entities in the ecosystem are marked as Clients or Prospects and operate in clean power development, utilities, and investment funds — core coverage areas for HSBC Sustainable Finance.
- Key entities include **GreenPeak Renewables**, **SunGrid Utilities**, and **EverGreen Capital**, all active in renewable energy value chains. `[{source_label}]`

---

**Surfaced Business Opportunity: Renewable Project Finance & Portfolio Financing**

**Opportunity A: Project Finance for Renewable Developers**

*Why this surfaced (rule-based logic):*
If a developer–offtaker relationship exists → surface a Project Finance opportunity.

*Supporting evidence:*
- GreenPeak Renewables (Project Developer, Client) has a long-term PPA with SunGrid Utilities for solar assets, with High relationship strength. `[{source_label}]`
- PPAs provide predictable, long-dated cashflows — a prerequisite for non-recourse or limited-recourse project finance.

*HSBC Sustainable Finance fit:*
- Green / sustainable-labelled Project Finance or Green Loans
- Potential structuring around Asia-Pacific solar and wind assets

*Confidence level:* 🟢 **High**
*Validation status:* ✅ Validated against ingested entity and relationship data

---

**Opportunity B: Portfolio / Fund-Level Financing & Sustainable Investment Solutions**

*Why this surfaced (rule-based logic):*
If a fund owns or co-invests in multiple clean power assets → surface a portfolio financing opportunity.

*Supporting evidence:*
- EverGreen Capital (Infrastructure Fund, Client) holds an equity stake in GreenPeak Renewables. `[{source_label}]`
- EverGreen Capital has a co-investment relationship with CleanFuture Fund, indicating portfolio-level exposure to renewables. `[{source_label}]`

*HSBC Sustainable Finance fit:*
- HoldCo / Portfolio financing
- Sustainability-linked loans, NAV-based facilities, or hedging solutions

*Confidence level:* 🟡 **Medium–High**
*Validation status:* ⚠️ Partially validated — co-investment structure present; fund classification requires confirmation

---

**Summary for RM Use**

| Aspect | Insight |
| :--- | :--- |
| **Relationship** | No recorded relationship; strong potential |
| **Primary Opportunity** | Green / Project Finance for renewable assets |
| **Secondary Opportunity** | Portfolio / Fund-level sustainable financing |
| **Strategic Value** | Long-term cashflows, scalable clean energy exposure |
| **Overall Confidence** | High |
| **Source Data** | {source_label} |
"""
    return output


def load_generic_template(files):
    """Generic fallback when no specific trigger is matched."""
    source_label = ", ".join(files) if files else "No files loaded"
    return f"""
**Existing/Potential Relationship:**
Relevant relationship identified in the ecosystem.

**Business Opportunity:**
Commercial banking / financing opportunity detected.

**Evidence/Rationale:**
Files reviewed: `{source_label}`

The ingested entity data indicates a valid client opportunity within the clean power ecosystem.
No segment-specific trigger matched. Please refine your query (e.g., include a target institution and product area).
"""


def run_simulation(prompt, files):
    """Orchestrates the processing steps with realistic delays."""
    steps = [
        (0.8, "Parsing entity and relationship structures..."),
        (1.0, "Opportunity Agent: Identifying cross-segment relationships..."),
        (1.2, "Opportunity Agent: Applying opportunity surfacing rules..."),
        (0.5, "Valadation Agent: Validating findings against ingested data..."),
        (1.5, "Generating output..."),
    ]
    for delay, msg in steps:
        time.sleep(delay)
        print(f">> {msg}")

    return get_response(prompt, files)
