# git-year

A minimal and compact terminal heatmap that shows one full **year** of Git commits in a GitHub-style layout, using vertical bars instead of squares to fit comfortably in small terminal windows.

A clean and lightweight CLI contribution calendar for developers who want a quick visual overview of their Git activity directly from the command line.

---

## Features

- **Shows the past year of commit activity** for the current Git repo
- **Similar to GitHub’s contribution graph**, but runs directly in your terminal
- Jump to **any calendar year**
- **Choose Sunday or Monday as the calendar week start** and keep the preference across reboots
- **Green intensity gradient** based on commit volume
- **Compact vertical bars (`|`)** instead of large squares — fits even tiny terminals
- **Zero dependencies** (pure Python + Git)
- **256-color ANSI output** with dark-mode-friendly palette
- **Highlights the current weekday**
- Works in **macOS, Linux, Windows Terminal, VS Code terminal, Git Bash**
- **PyPI ready** (`pipx install git-year`)

---

## Installation

```
pipx install git-year
or
pip install --user git-year
```

If pipx is not installed – install it before:
```
# macOS / Linux
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Windows
py -m pip install --user pipx
py -m pipx ensurepath
```

---

## Usage

Run `git-year` inside any Git repository to display a one-year contribution heatmap in your terminal.
```bash
git-year

# outputs a GitHub-style 
# contribution heatmap
# (shown as vertical bars)
```

You’ll see a compact 7×52 bar heatmap representing your activity for the past year up to today, displayed in dark mode with retro-style green bars highlighting your commit days:

<p align="center">
  <img src="docs/assets/terminal_github_style_heatmap.png" width="460" alt="Terminal GitHub-style heatmap">
</p>

- Columns = weeks (52 total)
- Rows = weekdays (with the current day highlighted)
- Week can start on Sun or Mon
- Color intensity = commit count

### Week Start

Choose the start of the week:
```
git-year --week-start Sunday
# also can be S, Su, Sun

git-year --week-start Monday
# also can be M, Mo, Mon

# saved to `~/.config/git-year/config.toml` on Linux/macOS or `%APPDATA%\git-year\config.toml` on Windows
```

### Specific Year

Focus on a specific calendar year:
```
git-year --year 2024
```

### Version

Show the installed version:
```
git-year -V
git-year --version
```

### Help

See the available options:
```
git-year -h
git-year --help
```

---

## Requirements

- Python 3.8+
- Git installed

---

## Contributing

Contributions are welcome!
Ideas, issues, and pull requests are appreciated.

---

## License

MIT License
Copyright (c) 2025 Serge Velbovets

---

Enjoy your terminal-native Git activity graph without leaving the shell — **git-year** keeps your development rhythm visible, simple, and elegant.
