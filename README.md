# SpendLens: Personal Finance Analytics 💳
### *Privacy-First Financial Visualization Engine powered by Python & Plotly*

![Status](https://img.shields.io/badge/Status-Live%20Prototype-success) ![Tech Stack](https://img.shields.io/badge/Tech-Python%20|%20Pandas%20|%20Plotly-blue) ![Privacy](https://img.shields.io/badge/Privacy-Local%20Processing-green)

**Live Prototype:** [https://spend-lens.streamlit.app/](https://spend-lens.streamlit.app/)
**Architect:** [Sumanta Pani](https://www.linkedin.com/in/sumantapani90)

---

## 1. Executive Summary
SpendLens is a **Personal Finance Dashboard** designed to solve the "Financial Hygiene" problem. Unlike proprietary apps that require bank credentials, SpendLens operates on a **Local-First Architecture**, processing raw bank statements (CSV/PDF) directly in the browser session without storing sensitive financial data.

## 2. Key Features
* **Multi-Format Ingestion:** proprietary parsing logic supports CSV, Excel (.xlsx), and PDF bank statements (specifically optimized for Indian banking formats).
* **Smart Categorization Engine:** Uses keyword mapping to automatically tag transactions (e.g., Zomato -> Food, Uber -> Transport).
* **"Mazboori" (Non-Discretionary) Logic:** Custom classification algorithm to separate **Fixed/Unavoidable Expenses** (Rent, EMI) from Discretionary Spending.
* **Visual Analytics:** Interactive Sunburst and Donut charts powered by **Plotly** for granular expense breakdown.
* **Privacy Protocol:** Zero-database architecture. Data is processed in RAM and discarded immediately after the session ends.

## 3. Technical Stack
| Component | Tool | Usage |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Responsive Web UI |
| **Data Processing** | Pandas | ETL (Extract, Transform, Load) pipelines |
| **Visualization** | Plotly Express | Interactive financial charting |
| **PDF Extraction** | PyPDF | Parsing unstructured PDF bank statements |

## 4. How to Run Locally
```bash
# Clone the repository
git clone [https://github.com/sumantapani23/budget-buddy.git](https://github.com/sumantapani23/budget-buddy.git)
cd budget-buddy

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
