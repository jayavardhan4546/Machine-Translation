# 🌐 Multi-Language Machine Translation Web App

This is a simple machine translation web application that supports **multiple languages** using the [`translate`](https://pypi.org/project/translate/) Python package. The frontend allows users to select source and target languages and input text for real-time translation. The backend is built with Flask.

---

## 🛠 Features

- 🔁 Translate between **multiple languages** (English, Hindi, Spanish, French, German, etc.)
- 🧠 Simple REST API built with Flask
- 💡 Clean and responsive user interface
- 🧩 Easily extendable for more languages

---

## 📁 Project Structure

```
machine_translation_app/
│
├── main.py                # Flask backend
├── translator.py          # Translation logic
│
├── templates/
│   └── index.html         # Frontend HTML
│
└── static/
    └── style.css          # Styling for frontend
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/machine_translation_app.git
cd machine_translation_app
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask flask-cors translate
```

### 4. Run the Application

```bash
python main.py
```

Visit:  
🔗 **http://localhost:8000**

---

## 🌍 Supported Languages

You can translate between any of the following (and more):

- English (`en`)
- Hindi (`hi`)
- French (`fr`)
- Spanish (`es`)
- German (`de`)

Modify the dropdowns or add more language codes to support more!

---

## 📦 API Endpoint

- **POST** `/predict`

### Request Body

```json
{
  "text": "Hello, how are you?",
  "from": "en",
  "to": "hi"
}
```

### Response

```json
{
  "Result": "नमस्ते, आप कैसे हैं?"
}
```

---

## 📚 Dependencies

- `Flask`
- `flask-cors`
- `translate`

Install with:

```bash
pip install -r requirements.txt
```

Or manually as shown above.

---

## 📝 To Do

- Add support for speech input/output
- Use a more advanced translation API (like Google or DeepL)
- Show language flags or auto-detect language

---

## 👨‍💻 Author

Created by Jayavardhan. Feel free to fork, customize, or contribute!

---

## 📄 License

This project is licensed under the MIT License.
