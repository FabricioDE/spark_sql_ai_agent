# SQL to Spark SQL AI Agent

This project is an **AI agent** built with [LangChain](https://www.langchain.com/) that converts standard SQL scripts into **Spark SQL**.  
It uses **Poetry** for dependency management.

---

## Features

- Reads a standard SQL script
- Cleans comments and formats the query
- Optionally loads context embeddings
- Converts SQL to Spark SQL using OpenAI LLM via LangChain
- Modular and extendable

---

## Prerequisites

- Python 3.11+
- Git
- Poetry (can be installed via official installer or pip)

---

## Setup Instructions

### 1. Clone the repository

bash
git clone https://github.com/FabricioDE/spark_sql_ai_agent.git

cd spark_sql_ai_agent



### 2. Install Poetry

You can install Poetry on macOS/Linux or Windows using the commands below:

**macOS / Linux:**


#### Using official installer
bash
curl -sSL https://install.python-poetry.org | python3 -

#### Or using pip
pip install --user poetry

#### Make sure Poetry's bin directory is in your PATH
export PATH="$HOME/.local/bin:$PATH"
#### Add this line to your shell configuration (~/.bashrc or ~/.zshrc) to make it permanent

#### Check installation
poetry --version

**Windows**

#### Using official installer
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

#### Or using pip
pip install --user poetry

#### Add Poetry to PATH (example for PowerShell)
setx PATH "$env:USERPROFILE\AppData\Roaming\Python\Python311\Scripts;$env:PATH"

#### Check installation
poetry --version
