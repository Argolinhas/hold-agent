"""GET / serves the paused Decision Card; assets and 404s match the waiting-pay matrix."""

from __future__ import annotations

import re
import sys
from html import unescape
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from web.app import app

LOCKED = [
    "Hold",
    "$412",
    "Pay $412 to Cedar Supply",
    "Invoice FN-1042",
    "Filed Cedar Supply packing note",
    "Logged bank CSV — no unmatched debit",
    "Approve",
    "Deny",
    "Trust this supplier",
    "Mocked",
    "Paused — native interrupt",
    "How this pause works",
    "stop_reason=interrupt",
    "then resume",
]


def visible_text(html: str) -> str:
    stripped = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", unescape(stripped))


@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as test_client:
        yield test_client


def test_waiting_pay_returns_locked_card(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    body = visible_text(response.text)
    for phrase in LOCKED:
        assert phrase in body
    assert "<textarea" not in response.text.lower()
    assert "composer" not in response.text.lower()
    assert 'name="ask"' not in response.text.lower()
    assert "contenteditable" not in response.text.lower()
    assert "cognito" not in response.text.lower()
    assert "oauth" not in response.text.lower()
    assert "login" not in response.text.lower()
    assert "/static/hold.css" in response.text


def test_query_string_is_ignored(client: TestClient) -> None:
    response = client.get("/?fixture=overnight")

    assert response.status_code == 200
    assert "Paused — native interrupt" in response.text
    assert "CANNED PATH" not in response.text


def test_adapter_does_not_import_agent() -> None:
    source = Path(__file__).resolve().parents[1] / "web" / "app.py"
    text = source.read_text(encoding="utf-8")
    assert "import agent" not in text
    assert "from agent" not in text
    assert "submit_payment" not in text
    assert "agent" not in sys.modules


def test_static_assets_are_served(client: TestClient) -> None:
    css = client.get("/static/hold.css")
    archivo = client.get("/static/fonts/ArchivoBlack-Regular.ttf")
    franklin = client.get("/static/fonts/LibreFranklin-Regular.ttf")

    assert css.status_code == 200
    assert archivo.status_code == 200
    assert franklin.status_code == 200


def test_invocations_is_not_the_decision_card(client: TestClient) -> None:
    response = client.get("/invocations")

    assert response.status_code == 404
    assert "Pay $412 to Cedar Supply" not in response.text
    assert "Paused — native interrupt" not in response.text


def test_openapi_docs_are_disabled(client: TestClient) -> None:
    assert client.get("/docs").status_code == 404
    assert client.get("/redoc").status_code == 404
    assert client.get("/openapi.json").status_code == 404
