# AIDEMOyanlian

`caseapi/` contains a set of Python scripts and Jupyter notebooks that demonstrate common LLM API use cases:

- Sentiment analysis
- Function calling for weather queries
- Table extraction
- Operations incident handling
- DeepSeek access through DashScope
- Web search through the OpenAI-compatible API

## Environment

This project uses the local virtual environment at `.venv/`.

Select this interpreter in PyCharm:

```bash
/Users/ligangjian/Documents/PythonProject/my-ai-project/.venv/bin/python
```

## Install Dependencies

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Required Environment Variables

Most examples use DashScope:

```bash
export DASHSCOPE_API_KEY="your_api_key"
```

## Run Examples

Run a Python script directly:

```bash
python caseapi/6-联网搜索.py
```

Or open the corresponding `.ipynb` file in PyCharm/Jupyter and make sure the kernel is also set to `.venv`.
