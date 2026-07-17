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

### Version 0.4.0
- Generate MD5 checksum
- Generate SHA256 checksum
- Binary file reading
- Efficient chunk-based hashing
- Foundation for duplicate detection

### Version 0.5.0
- Detect duplicate files using SHA256
- Hash-based duplicate grouping
- Display duplicate file paths
- Dictionary-based detection algorithm

### Version 0.6.0
- CSV duplicate report
- Automatic reports folder creation
- Excel compatible output

### Version 0.6.1
- CSV report generation
- JSON report generation
- Timestamped reports
- File size information
- Last modified timestamp
- Professional reporting module

### Version 0.7.0
- Size-based file grouping
- Skip hashing files with unique sizes
- Faster duplicate detection
- Improved scalability for large directories

### Performance Improvement

The application now groups files by size before hashing. Files with unique sizes are skipped, reducing unnecessary disk reads and making scans significantly faster on large datasets.

### Version 0.8.0
- Industrial logging
- Timestamped log files
- Automatic log directory creation
- Exception logging
- Scan summary logging

## Version 0.9.0

### New Features

- Safe duplicate file mover
- Automatic Trash folder creation
- Keeps one original copy
- Prevents filename collisions
- Logs every moved file

## Version 1.0.0 - Command Line Interface (CLI)

### Features Added

- Added command-line interface using `argparse`
- Supports directory input through `--path`
- Supports optional `--move` flag to move duplicate files
- Automatic command validation
- Built-in `--help` documentation
- Improved project usability for automation and scripting

### Usage

#### Scan a Directory

```bash
python main.py --path "D:\TestFolder"
```

#### Move Duplicate Files

```bash
python main.py --path "D:\TestFolder" --move
```

#### Display Help

```bash
python main.py --help
```

### Output

- Duplicate file report in the console
- CSV report
- JSON report
- Log file
- Optional `Trash/` folder containing moved duplicate files

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
- [x] Scanner
- [x] Recursive Scanner
- [x] Checksum Generator
- [x] Duplicate Detection
- [x] CSV Report
- [x] JSON Report
- [x] Logging
- [ ] Delete Duplicates
- [ ] Scheduler

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