"""Public FastAPI adapter. Serves the paused Decision Card at GET /."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

STATIC_DIR = Path(__file__).resolve().parent / "static"
PAUSED_CARD = STATIC_DIR / "key-paused.html"

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/", response_class=HTMLResponse)
def waiting_pay() -> str:
    return PAUSED_CARD.read_text(encoding="utf-8")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
