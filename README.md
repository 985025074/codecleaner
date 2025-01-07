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
---

# 代码替换器 (Code Replacer)

## 项目介绍

**代码替换器**是一个使用 Python 的 `re`（正则表达式）模块来清理和替换代码的项目。比如，它可以删除 JavaScript 中的 `DEBUG console.log` 语句或进行其他类似的操作。

这个项目仍在开发中，目前是一个粗略的版本。如果你有任何想法或建议，欢迎加入并贡献！

## 功能

- 使用正则表达式清理和替换代码。
- 删除 JavaScript 中的 `DEBUG console.log` 语句。
- 可通过修改 `config.json` 文件，轻松扩展其他语言（如 C++、Python）的替换功能。
- 支持自定义的代码替换策略。

## 使用方法

1. **克隆仓库：**

   ```bash
   git clone <仓库地址>
   cd <项目目录>
   ```

2. **运行工具：**

   如果你想查看可用的选项并获取帮助：

   ```bash
   python3 main.py --help
   ```

3. **安装工具：**

   你可以使用 `setuptools` 快速设置并安装工具：

   ```bash
   pip install  .
   ```

4. **自定义策略：**

   已经实现了一个 JavaScript 的替换策略。如果你想编写自己的替换策略，请查看 `config.json` 文件，并模仿 JavaScript 的策略进行添加。

## 扩展功能

- 已实现 **JavaScript 替换器**。
- 你可以为其他语言（如 **C++**、**Python** 等）创建自己的替换策略，扩展功能。
- 本项目欢迎贡献！随时为新的策略或改进贡献代码。

## 待办事项

- 在命令行界面（CLI）实现逐行替换功能。
- 为其他语言（如 C++、Python 等）实现更多替换策略。
- 提升替换功能的执行速度。
- 提供更多文档和示例。

