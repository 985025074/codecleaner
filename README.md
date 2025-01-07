# Code Replacer

## Introduction

**Code Replacer** is a project that utilizes Python's `re` (regular expression) module to clean and replace code snippets. For example, it can remove `DEBUG` statements from `console.log` in JavaScript or perform other similar tasks.

This project is still under development and in its early stages. If you have any ideas or suggestions, feel free to join and contribute!

## Features

- Clean and replace code using regular expressions.
- Remove `DEBUG` statements such as `console.log` in JavaScript.
- Easily extendable for other languages (e.g., C++, Python) by adding new tactics in the `config.json` file.
- Supports custom code replacement strategies.

## Usage

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Run the tool:**

   If you want to check available options and get help:

   ```bash
   python3 main.py --help
   ```

3. **Install the tool:**

   You can quickly set up the tool using `setuptools`:

   ```bash
   pip install  .
   ```

4. **Custom Tactics:**

   A built-in tactic for JavaScript replacement is available. If you want to create your own custom tactic, check the `config.json` file and add your tactic by imitating the JavaScript one.

## Extension

- A **JavaScript replacer** has already been implemented.
- You can extend the functionality by creating your own tactics for other languages like **C++**, **Python**, etc.
- The project is open for contributions! Feel free to contribute new tactics or improvements.

## TODO

- Add line-by-line replacement functionality via the CLI.
- Implement additional tactics for other languages (C++, Python, etc.).
- Enhance the overall speed of replacements.
- Provide more documentation and examples.
## update record:
2025.1.7  
fix bugs : config.json cant be read when the package is installed. use package_data function instaed. I tried manifest but didn't work.I don't know why. And I changed reading config's code. for the relative path is decided by the running path,which causing bugs that config can't be found in the directory where we run the command.
the setuptools is hard to use!