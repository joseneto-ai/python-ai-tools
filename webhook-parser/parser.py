"""
Webhook Payload Parser
======================
Normalizes incoming webhook payloads from different sources
into a consistent data structure for downstream processing.

Supported sources: whatsapp, webform, generic

Author: José Neto @zNeto.AI
"""

from datetime import datetime, timezone


def parse_whatsapp(payload: dict) -> dict:
    """
    Parses a Meta WhatsApp Business API webhook payload.

    Args:
        payload: Raw webhook payload from Meta.

    Returns:
        Normalized message dictionary.
    """
    try:
        entry = payload["entry"][0]
        change = entry["changes"][0]["value"]
        message = change["messages"][0]

        sender_id = message.get("from", "unknown")
        message_text = message.get("text", {}).get("body", "")
        raw_timestamp = message.get("timestamp", "")

        timestamp = (
            datetime.fromtimestamp(
                int(raw_timestamp), tz=timezone.utc
            ).isoformat()
            if raw_timestamp
            else datetime.now(tz=timezone.utc).isoformat()
        )

        return {
            "source": "whatsapp",
            "sender_id": sender_id,
            "message": message_text,
            "timestamp": timestamp,
            "raw": payload
        }

    except (KeyError, IndexError, ValueError) as e:
        return _error_payload("whatsapp", str(e), payload)


def parse_webform(payload: dict) -> dict:
    """
    Parses a standard web form POST payload.

    Args:
        payload: Flat key-value form data dictionary.

    Returns:
        Normalized message dictionary.
    """
    sender_id = (
        payload.get("email")
        or payload.get("phone")
        or payload.get("sender_id")
        or "unknown"
    )

    message = (
        payload.get("message")
        or payload.get("body")
        or payload.get("text")
        or ""
    )

    return {
        "source": "webform",
        "sender_id": sender_id,
        "message": message,
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "raw": payload
    }


def parse_generic(payload: dict) -> dict:
    """
    Parses a generic flat JSON payload with best-effort field matching.

    Args:
        payload: Any flat JSON dictionary.

    Returns:
        Normalized message dictionary.
    """
    return {
        "source": "generic",
        "sender_id": payload.get("sender_id", "unknown"),
        "message": payload.get("message", ""),
        "timestamp": payload.get(
            "timestamp",
            datetime.now(tz=timezone.utc).isoformat()
        ),
        "raw": payload
    }


def _error_payload(source: str, error: str, raw: dict) -> dict:
    """Returns a safe error payload when parsing fails."""
    return {
        "source": source,
        "sender_id": "parse_error",
        "message": "",
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "error": error,
        "raw": raw
    }


PARSERS = {
    "whatsapp": parse_whatsapp,
    "webform": parse_webform,
    "generic": parse_generic
}


def parse_payload(payload: dict, source: str = "generic") -> dict:
    """
    Main entry point. Routes to the correct parser based on source.

    Args:
        payload: Raw incoming webhook payload.
        source: Origin of the payload. One of: whatsapp, webform, generic.

    Returns:
        Normalized message dictionary with consistent schema.
    """
    parser = PARSERS.get(source, parse_generic)
    return parser(payload)


if __name__ == "__main__":
    # Example usage

    whatsapp_payload = {
        "entry": [{
            "changes": [{
                "value": {
                    "messages": [{
                        "from": "5531999990000",
                        "text": {"body": "I want to schedule a consultation"},
                        "timestamp": "1700000000"
                    }]
                }
            }]
        }]
    }

    webform_payload = {
        "email": "patient@example.com",
        "phone": "5531988880000",
        "message": "Interested in rhinoplasty, can you send pricing?"
    }

    generic_payload = {
        "sender_id": "user_42",
        "message": "Hello, I need information about your services."
    }

    print("=== Webhook Payload Parser ===\n")

    for source, payload in [
        ("whatsapp", whatsapp_payload),
        ("webform", webform_payload),
        ("generic", generic_payload)
    ]:
        result = parse_payload(payload, source=source)
        print(f"Source: {source}")
        print(f"Sender: {result['sender_id']}")
        print(f"Message: {result['message']}")
        print(f"Timestamp: {result['timestamp']}\n")
