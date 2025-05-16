# tinyShelf2 📚

A minimalist command-line book manager built with Python. Add, view, search, edit, and remove books—all from your terminal. Books are stored in a local JSON file.

## 🔧 Features

- Add new books with required fields (title, author, publisher, year)
- List and search books
- Edit and delete entries
- Track read/lent status
- Color-coded terminal interface (ANSI)
- Persistent storage via `library.json`
- Modular CLI with prompt classes

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tinyShelf2.git
cd tinyShelf2
```

### 2. Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows (Git Bash): source venv/Scripts/activate
pip install -r requirements.txt
```

### 3. Run the App

```bash
python main.py
```

## 📁 Project Structure

```
tinyShelf2/
├── main.py               # Entry point
├── prompts/              # Interactive CLI prompts
├── models/               # Book class and validation
├── storage/              # JSON handling
├── utils/                # Formatting and display
├── library.json          # Book database (auto-generated)
└── requirements.txt
```

## 💡 Planned Enhancements

- Recursive category system
- Export to markdown or PDF
- Tag and filter system
- PyPI packaging

## 📜 License

MIT License
