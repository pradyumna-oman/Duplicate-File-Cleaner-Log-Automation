# Duplicate File Cleaner & Log Automation

A professional Python project that scans directories, detects duplicate files, generates reports, and automates file management.

This project is being developed incrementally using professional Git workflows and clean software engineering practices.

---

## Features

### Version 0.1.0
- Project initialization
- Professional folder structure
- Git integration
- MIT License
- Python package structure

### Version 0.2.0
- Non-recursive directory scanner
- Count files and folders
- Display directory contents
- Basic exception handling
- Modular code organization

---

## Project Structure

```
Duplicate-File-Cleaner/
│
├── src/
│   ├── __init__.py
│   ├── scanner.py
│   ├── cleaner.py
│   ├── hasher.py
│   ├── logger.py
│   ├── report.py
│   ├── scheduler.py
│   ├── config.py
│   └── utils.py
│
├── tests/
├── reports/
├── logs/
├── docs/
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Duplicate-File-Cleaner.git
```

Move into the project:

```bash
cd Duplicate-File-Cleaner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

Enter a directory path when prompted.

Example:

```
Enter directory path:
C:\Users\YourName\Downloads
```

---

## Roadmap

- [x] Project Setup
- [x] Directory Scanner
- [ ] Recursive Scanner
- [ ] File Metadata
- [ ] SHA256 Hash Generator
- [ ] Duplicate Detection
- [ ] Report Generator
- [ ] Logging
- [ ] Scheduler
- [ ] GUI
- [ ] Industrial Version

---

## Technologies

- Python 3
- Git
- GitHub
- os module

---

## License

MIT License

---

## Author

Pradyumna Rajkumar Oman