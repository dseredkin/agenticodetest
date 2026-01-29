# Calculator

A simple calculator project for testing AgentiCode automation.

## Usage

```python
from src.calculator import add, subtract

result = add(2, 3)  # 5
result = subtract(5, 3)  # 2
```

## Development

```bash
uv sync --dev
uv run pytest tests/
```
