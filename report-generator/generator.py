"""
Automated Report Generator
===========================
Generates structured lead and automation performance reports
using GPT-4o based on raw interaction data.

Author: José Neto @zNeto.AI
"""

import os
import json
from datetime import datetime, timezone
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional business analyst writing concise performance
reports for AI automation systems.

Your reports are:
- Clear and direct — no filler language
- Data-driven — reference the exact numbers provided
- Actionable — always end with one concrete recommendation
- Professional — suitable for C-level or client delivery

Format your report with these sections:
1. Overview (2-3 sentences summarizing the period)
2. Intent Breakdown (bullet points with percentages)
3. Conversion (key conversion metrics)
4. Recommendation (one specific, actionable next step)

Do not add any preamble. Start directly with the report.
"""


def generate_report(lead_data: dict) -> str:
    """
    Generates a professional performance report from lead data.

    Args:
        lead_data: Dictionary containing lead metrics for the period.

    Returns:
        Formatted report as a string.
    """
    data_summary = json.dumps(lead_data, indent=2)

    user_prompt = f"""
Generate a performance report based on the following lead data:

{data_summary}

Calculate percentages where relevant.
Be precise with numbers. Keep the report under 250 words.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Report generation failed: {str(e)}"


def save_report(report: str, filename: str = None) -> str:
    """
    Saves the generated report to a text file.

    Args:
        report: The generated report string.
        filename: Optional custom filename. Defaults to timestamped name.

    Returns:
        The path of the saved file.
    """
    if not filename:
        timestamp = datetime.now(tz=timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return filename


if __name__ == "__main__":
    # Replace with your actual data
    lead_data = {
        "period": "2024-11-01 to 2024-11-14",
        "total_leads": 84,
        "high_intent": 31,
        "warm": 38,
        "cold": 15,
        "urgent_escalations": 2,
        "appointments_scheduled": 24,
        "average_response_time_seconds": 87,
        "leads_from_off_hours": 39
    }

    print("=== Automated Report Generator ===\n")
    print("Generating report...\n")

    report = generate_report(lead_data)

    print(report)
    print("\n" + "=" * 40)

    saved_path = save_report(report)
    print(f"\nReport saved to: {saved_path}")
