# 🧠 Message Classifier

Classifies any incoming text message by intent using the OpenAI API.
Returns a clean JSON object with the classification result and
confidence reasoning — ready to feed directly into routing logic
or n8n workflow branches.

---

## What This Solves

In any AI automation pipeline, the first critical step is understanding
what the user actually wants. This classifier abstracts that logic into
a single, reusable function that can be called from n8n, a webhook
handler, or any Python script.

---

## Output Example

Input message:
```
"I'd like to schedule a consultation for next week, 
how much does it cost?"
```

Output:
```json
{
  "intent": "HIGH_INTENT",
  "confidence": "high",
  "reasoning": "User explicitly requests scheduling and asks about
                pricing — clear purchase signals.",
  "recommended_action": "route_to_sales"
}
```

---

## How to Use

**1. Clone or copy the script**

**2. Create your `.env` file based on `.env.example`:**
```
OPENAI_API_KEY=your-key-here
```

**3. Run the classifier:**
```bash
python classifier.py
```

**4. Or import as a module:**
```python
from classifier import classify_message

result = classify_message("I want to book an appointment")
print(result)
```

---

## Files

- `README.md` — This documentation
- `classifier.py` — Main classifier script
- `.env.example` — Environment variable reference

---

## Stack

- Python 3.10+
- OpenAI API (GPT-4o)
- `python-dotenv` for credential management
```
