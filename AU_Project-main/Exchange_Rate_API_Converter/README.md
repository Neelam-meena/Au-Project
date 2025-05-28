
# 💱 Currency to INR Converter using Streamlit & Exchange Rate API

A beginner-friendly Streamlit project that lets users select a currency and instantly view its conversion rate to INR using real-time data from the **ExchangeRate-API**.

---

## 📌 Project Objective

> To build a simple and interactive **currency converter** using Python, Streamlit, and ExchangeRate API, where users can convert popular foreign currencies to Indian Rupees (INR).

---

## 🌟 Features

- 🔄 Real-time exchange rate fetch from API
- 🌐 Dropdown to select foreign currency
- 🇮🇳 Converts to INR instantly
- ✅ Clean and beginner-friendly UI
- 📦 Proper project directory with `requirements.txt` and `.gitignore`

---

## 🖼️ Project Flow

```mermaid
flowchart TD
    Start[Start App] --> UI[Streamlit UI Loads]
    UI --> UserSelect[User selects currency]
    UserSelect --> CallAPI[API Call to fetch exchange rate]
    CallAPI --> Convert[Convert 1 unit to INR]
    Convert --> ShowResult[Show INR value in UI]
    ShowResult --> End[User views result]