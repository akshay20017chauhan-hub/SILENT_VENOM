# SILENT VENOM - Mobile Web Application

SILENT VENOM ek dark-themed, responsive, mobile-portrait multi-user web application hai jo Python Flask, SQLite aur Bootstrap 5 par aadharit hai.

---

## 🛠️ Requirements & Prerequisites

- **Python 3.8+**
- **VS Code** (Visual Studio Code)
- **Pip** (Python Package Manager)

---

## 📁 Project Directory Structure

```
SILENT_VENOM/
├── app.py                  # Main Flask Server & Database Models
├── requirements.txt        # Python Packages
├── README.md               # Setup Guide
├── static/
│   ├── css/
│   │   └── style.css       # Custom Dark Theme CSS ( exact matching reference )
│   └── js/
│       └── main.js        # Dynamic UI Logic
└── templates/
    ├── base.html           # Mobile Frame Layout
    ├── register.html       # Mobile Registration Page
    ├── login.html          # Mobile Login Page
    ├── dashboard.html      # User Dashboard
    └── admin.html          # Admin Panel
```

---

## 🚀 Windows Laptop & VS Code Setup Guide

### Step 1: Extract ZIP File
1. Final downloadable `SILENT_VENOM.zip` file ko un-zip (extract) karein.
2. Extracted folder `SILENT_VENOM` ko open karein.

### Step 2: Open Project in VS Code
1. VS Code open karein.
2. Menu se **File > Open Folder** par jayein aur `SILENT_VENOM` folder ko select karein.

### Step 3: Open Terminal in VS Code
1. VS Code ke top menu bar se **Terminal > New Terminal** par click karein (Shortcut: `Ctrl + ~`).

### Step 4: Create Virtual Environment (Optional but Recommended)
Terminal mein ye command chalayein:
```bash
python -m venv venv
```
Activate karne ke liye:
```bash
.env\Scriptsctivate
```

### Step 5: Install Requirements
Terminal mein packages install karein:
```bash
pip install -r requirements.txt
```

### Step 6: Run the Application
Project start karne ke liye:
```bash
python app.py
```

Console mein aapko ye message dikhai dega:
`* Running on http://127.0.0.1:5000`

### Step 7: Open in Browser
Browser open karein aur type karein:
`http://127.0.0.1:5000`

---

## 🔑 Login & Admin Credentials

- **Default Admin Account:**
  - **Phone / Username:** `admin`
  - **Password:** `admin123`

- **User Registration:**
  - Koi bhi user `/register` page se new phone number aur password ke saath register kar sakta hai.

---

## ✨ Key Features
1. ** exact Mobile Reference Matching:** Dark green/black theme, custom gold button, rounded input boxes, invite code pre-fill, back arrow, language badge.
2. **Strict Mobile Portrait Frame:** Centered mobile app look on Desktop browsers.
3. **Password Security:** `Werkzeug` hashing engine (PBKDF2/SHA256).
4. **Admin User Management:** Admin Panel se kisi bhi user ko instantly Block / Unblock kiya ja sakta hai.
