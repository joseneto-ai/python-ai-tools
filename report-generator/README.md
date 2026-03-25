# 📊 Automated Report Generator

Takes raw lead or interaction data and generates a structured,
professional summary report using GPT-4o — formatted and ready
to send to clients or internal teams without any manual writing.

---

## The Problem This Solves

After running automation workflows, someone still has to summarize
what happened: how many leads came in, what was the intent breakdown,
what actions were taken. This script eliminates that manual step
entirely.

---

## Output Example

Input data:
```json
{
  "period": "2024-11-01 to 2024-11-14",
  "total_leads": 84,
  "high_intent": 31,
  "warm": 38,
  "cold": 15,
  "urgent_escalations": 2,
  "appointments_scheduled": 24
}
```

Generated report:
```
LEAD PERFORMANCE REPORT — November 1–14, 2024

Overview:
84 leads processed over the reporting period with a 36.9% high-intent
rate — indicating strong top-of-funnel quality.

Intent Breakdown:
- High Intent: 31 leads (36.9%) → routed to sales pipeline
- Warm: 38 leads (45.2%) → enrolled in nurture sequence
- Cold: 15 leads (17.9%) → logged for long-term follow-up
- Urgent Escalations: 2 → handled by human staff

Conversion:
24 appointments scheduled from 31 high-intent leads — a 77.4%
high-intent-to-appointment conversion rate.

Recommendation:
The warm segment (45%) represents significant untapped potential.
Recommend activating a targeted re-engagement sequence for leads
older than 7 days.
```

---

## How to Use

**1. Create your `.env` file:**
```
OPENAI_API_KEY=your-key-here
```

**2. Edit the `lead_data` dictionary in `generator.py`
with your actual numbers.**

**3. Run the script:**
```bash
python generator.py
```

**4. The report is printed to console and saved as `report.txt`.**

---

## Files

- `README.md` — This documentation
- `generator.py` — Main report generator script
- `.env.example` — Environment variable reference

---

## Stack

- Python 3.10+
- OpenAI API (GPT-4o)
- `python-dotenv` for credential management
