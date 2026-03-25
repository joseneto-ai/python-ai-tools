# 🔗 Webhook Payload Parser

Normalizes incoming webhook payloads from different sources
(WhatsApp, web forms, landing pages, APIs) into a single,
consistent data structure.

Built for use inside n8n Function nodes or as a standalone
preprocessing step before any AI classification or CRM logging.

---

## The Problem This Solves

Different sources send data in wildly different formats.
WhatsApp sends nested JSON with a specific Meta API structure.
Web forms send flat key-value pairs. Landing page tools send
their own schema.

Without normalization, every integration requires custom parsing
logic. This parser abstracts that into one reusable function.

---

## Output Example

WhatsApp input:
```json
{
  "entry": [{
    "changes": [{
      "value": {
        "messages": [{
          "from": "5531999990000",
          "text": { "body": "I want to schedule a consultation" },
          "timestamp": "1700000000"
        }]
      }
    }]
  }]
}
```

Normalized output:
```json
{
  "source": "whatsapp",
  "sender_id": "5531999990000",
  "message": "I want to schedule a consultation",
  "timestamp": "2024-11-14T22:13:20",
  "raw": { ... }
}
```

---

## Supported Sources

- `whatsapp` — Meta WhatsApp Business API format
- `webform` — Standard HTML form POST payload
- `generic` — Flat JSON with message and sender fields

---

## How to Use
```python
from parser import parse_payload

raw_payload = { ... }  # your incoming webhook data
normalized = parse_payload(raw_payload, source="whatsapp")
print(normalized)
```

---

## Files

- `README.md` — This documentation
- `parser.py` — Main parser script

---

## Stack

- Python 3.10+
- No external dependencies — standard library only
  
