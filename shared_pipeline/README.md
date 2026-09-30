# Shared Pipeline

- `test_claude.py`: confirms your Claude API key works (run this first)
- `llm.py`: minimal scaffold that turns any SI result dict into a structured narrative

Usage from any track:

```python
from shared_pipeline.llm import interpret
narrative = interpret(result_dict)
```
