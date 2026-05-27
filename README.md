<div align="center">

# 🔮 is-my-code-cursed

### A CLI Tool That Roasts Your Code Using AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Powered%20by-Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com/)

**An ancient code sage analyzes your code for cursedness — bad naming, spaghetti logic, magic numbers, and crimes against readability — then delivers a dramatic verdict with a curse rating from 1 to 10.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Flags](#-flags) • [Contributing](#-contributing)

</div>

---

## ✨ Features

<table>
<tr>
<td>

🔮 **Dramatic AI Roasting**  
An ancient code sage delivers a theatrical verdict on your code

⚔️ **Brutal Mode**  
No mercy mode for when you want the harshest possible roast

📄 **Save Reports**  
Export the sage's verdict to a file for future reference

</td>
<td>

📏 **Word Limit**  
Control how long the sage's rant is with a word limit flag

📁 **Directory Support**  
Analyze entire projects recursively, skipping binary files automatically

🛡️ **Proper Error Handling**  
Clear error messages for missing API keys, files, and API failures

</td>
</tr>
</table>

---

## 🤔 Why This Project?

Ever stared at your own code and wondered if it's actually cursed? Now you can get a second opinion — from an ancient code sage powered by Gemini AI.

- 🧙 **Dramatic verdicts** — not just "this is bad", but a full theatrical roast with specific callouts
- 📊 **Curse rating** — get a score from 1 (barely cursed) to 10 (an abomination)
- ⚔️ **Brutal mode** — for when you really want to suffer
- 🛠 **Learning project** — built to learn CLI tool development and the Gemini API

---

## 🚀 Installation

### Option 1: AUR (Arch Linux)

If you're on Arch Linux or an Arch-based distro, install directly via your AUR helper:

```bash
yay -S is-my-code-cursed
```

No dependencies to install manually — just set your API key and you're good to go.

### Option 2: Manual

#### 1. Clone the repository

```bash
git clone https://github.com/HimC29/is-my-code-cursed.git
cd is-my-code-cursed
```

#### 2. Get a Gemini API key

Get a free API key from [aistudio.google.com](https://aistudio.google.com) and add it to your shell config:

```bash
# Add to ~/.zshrc or ~/.bashrc
export GEMINI_API_KEY="your_key_here"
```

Then reload your shell:

```bash
source ~/.zshrc  # or ~/.bashrc
```

#### 3. Install the CLI command

```bash
chmod +x install.sh
./install.sh
```

Now you can run `is-my-code-cursed` from anywhere!

---

## 📖 Usage

```bash
is-my-code-cursed <file|directory> [flags]
```

### Basic example

```bash
is-my-code-cursed main.py
```

### Analyze an entire project

```bash
is-my-code-cursed ./my-project
```

### Save the verdict to a file

```bash
is-my-code-cursed main.py --output report.txt
```

### Brutal mode (no mercy)

```bash
is-my-code-cursed main.py --brutal
```

### Limit the response length

```bash
is-my-code-cursed main.py --max-words 300
```

### Exclude directories

```bash
is-my-code-cursed ./my-project --exclude dist,build
```

### Combine flags

```bash
is-my-code-cursed main.py --brutal --max-words 500 --output report.txt
```

---

## 🚩 Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--output FILE` | `-o` | Save the sage's verdict to a file |
| `--brutal` | `-b` | No mercy mode — harsher roasting |
| `--max-words N` | `-w` | Limit the response to N words |
| `--verbose` | `-v` | Print status when calling the Gemini API |
| `--exclude DIRS` | `-e` | Comma-separated directories to ignore |
| `--help` | `-h` | Show help message and exit |

---

## 📁 Project Structure

```
is-my-code-cursed/
├── src/
│   └── main.py          — Main CLI script
├── install.sh            — Installs the CLI command system-wide
├── README.md             — Project documentation
└── LICENSE               — MIT license
```

---

## 📝 Changelog

### v1.1.0
- 🔧 Removed `python-google-generativeai` dependency — now uses only Python stdlib
- 📡 Gemini API calls now made directly via `urllib.request`
- ⚠️ Improved warning message when a file is skipped during directory scan
- 📦 Much easier to install — no AUR dependencies required

> From this version onwards, this project follows [Semantic Versioning](https://semver.org/):
> `MAJOR.MINOR.PATCH` — breaking changes . new features . bug fixes

### v1.0.5
- 💻 Add auto permission elevation for Linux installs in install.sh if needed

### v1.0.4
- 🚫 New `--exclude` / `-e` flag to ignore custom directories
- 🧹 Support multiple excluded folders using comma-separated values

### v1.0.3
- 📁 Add directory support — analyze entire projects recursively
- 🚫 Automatically skip binary files
- 🧹 Ignore common dependency/cache folders like `.git` and `node_modules`
- 📄 Include file names and contents in AI analysis context

### v1.0.2
- 💻 Rename add_to_path.sh to install.sh
- Improve install.sh to support Termux and have more fallback features

### v1.0.1
- 🧹 Small code cleanup
- New flag: `--verbose` to print status when importing lib and calling API

### v1.0.0
- 🎉 Initial release
- AI-powered code roasting with curse rating 1-10
- `--brutal` mode for no mercy roasting
- `--output` to save reports to a file
- `--max-words` to control response length

---

## 📝 Example Output

```
Hark, seeker of truth! I have gazed upon thy digital parchment...

Curse Rating: 7/10

A heavy curse, indeed! Your code does not merely stumble; it actively
confesses its most heinous sin in plain sight...
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new flags, better prompts, or bug fixes, feel free to open an issue or PR.

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions

- 🎨 Colored terminal output with `colorama` or `rich`
- 🔔 Support for more languages/models
- 📦 PyPI package release

---

## 📄 License

Distributed under the MIT License. See [LICENSE](/LICENSE) for more information.

---

<div align="center">

### ⭐ Star this repo if your code got roasted!

**Made with 🔮 by [HimC29](https://github.com/HimC29)**

[Report Bug](https://github.com/HimC29/is-my-code-cursed/issues) • [Request Feature](https://github.com/HimC29/is-my-code-cursed/issues)

</div>