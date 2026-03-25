"""
Message Intent Classifier
=========================
Classifies incoming text messages by intent using the OpenAI API.
Returns a structured JSON result for downstream routing logic.

Author: José Neto @zNeto.AI
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an intent classification engine.

Your job is to analyze an incoming message and classify it into
one of the following intent categories:

- HIGH_INTENT: User is ready to buy, book, or take immediate action.
  They ask about pricing, availability, or express clear purchase intent.

- WARM: User is interested but in early research phase.
  They ask general questions without strong purchase signals.

- LOW_INTENT: User is vaguely curious, unlikely to convert soon.

- URGENT: User describes a problem, complaint, or emergency situation
  that requires immediate human attention.

- UNRELATED: Message is off-topic, spam, or cannot be classified.

Respond ONLY with a valid JSON object in this exact format:
{
  "intent": "<CLASSIFICATION>",
  "confidence": "<high|medium|low>",
  "reasoning": "<one sentence explanation>",
  "recommended_action": "<route_to_sales|add_to_nurture|log_and_ignore|escalate_to_human>"
}

Do not include any text outside the JSON object.
"""


def classify_message(message: str) -> dict:
    """
    Classifies a message by intent using GPT-4o.

    Args:
        message: The raw text message to classify.

    Returns:
        A dictionary with intent, confidence, reasoning,
        and recommended_action fields.
    """
    if not message or not message.strip():
        return {
            "intent": "UNRELATED",
            "confidence": "high",
            "reasoning": "Empty or blank message received.",
            "recommended_action": "log_and_ignore"
        }

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            temperature=0.1,
            max_tokens=150
        )

        raw_output = response.choices[0].message.content.strip()
        result = json.loads(raw_output)
        return result

    except json.JSONDecodeError:
        return {
            "intent": "ERROR",
            "confidence": "low",
            "reasoning": "Model returned non-JSON output.",
            "recommended_action": "escalate_to_human"
        }

    except Exception as e:
        return {
            "intent": "ERROR",
            "confidence": "low",
            "reasoning": f"API error: {str(e)}",
            "recommended_action": "escalate_to_human"
        }


def batch_classify(messages: list[str]) -> list[dict]:
    """
    Classifies a list of messages and returns results in order.

    Args:
        messages: List of raw text messages.

    Returns:
        List of classification result dictionaries.
    """
    results = []
    for message in messages:
        result = classify_message(message)
        result["original_message"] = message
        results.append(result)
    return results


if __name__ == "__main__":
    # Example usage
    test_messages = [
        "I'd like to schedule a consultation for next week, how much does it cost?",
        "Just browsing, what kind of services do you offer?",
        "I've been in pain since my procedure yesterday, please help.",
        "asdfgh random text here"
    ]

    print("=== Message Intent Classifier ===\n")

    for msg in test_messages:
        print(f"Message: {msg}")
        result = classify_message(msg)
        print(f"Result:  {json.dumps(result, indent=2)}\n")
```
