# 🚀 w1n

A lightweight, cross-platform environment automation and meta-package manager written in Python.

## Description

**w1n** is a minimalist CLI tool designed to deploy software packages and execute environment automation scripts from a centralized cloud JSON matrix. It bypasses heavy corporate automation frameworks, functioning as a clean, direct bridge between remote instructions and the host system shell.

### Core Specifications:
* **Zero System Dependencies:** Compiles into a single, standalone binary containing its own isolated Python execution layer. No system python packages or virtual environments required.
* **Synchronous Shell Orchestration:** Pauses execution dynamically while the system shell runs complex multi-step installation chains (like Cargo, Pip, or CMake) in real time.
* **True Cross-Platform Design:** Translates command matrix execution natively across Linux shell path structures and Windows PowerShell environments.

## CLI Usage

```text
w1n — Cross-platform environment automation manager

Usage:
  w1n install <package_name>      Download and deploy package from the cloud matrix

Examples:
  w1n install crab
```

## How It Works

When you run `w1n -S <package>`, the tool performs three distinct steps:
1. Fetches the global repository configuration matrix from GitHub via an encrypted secure network connection.
2. Locates the specified package key and extracts the direct deployment string.
3. Automatically triggers the host terminal shell to execute the precise deployment sequence synchronously, piping log outputs directly to your screen.

## Installation

### For Linux / macOS
```bash
curl -LO https://github.com/w1n4a/w1n/releases/download/v1.0.0/w1n && chmod +x w1n && mv w1n ~/.local/bin/
```

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**. Permanent copyleft reciprocity applies to all derivative works.
