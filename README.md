# Hold

The agent works overnight. You only approve what spends money.

Hold is a background clerk for a one-person shop. It files inbound work unattended, and when the next step would send money it stops on a Decision Card. The public page has no prompt box and no login.

This entry is for [Agents for Humans](https://agentsforhumans.devpost.com/) (Professional Agents, English / USD).

## What you see in 30 seconds

Open `/` in a browser. There is no account wall.

You should see two silent completions (a packing note filed, a bank CSV logged) and one waiting pay: $412 to Cedar Supply, invoice FN-1042. The card offers Approve, Deny, and Trust this supplier.

## Run locally

Python 3.12 (3.10 or newer). Install from the lockfile and start the adapter on port 8080:

```bash
uv sync --group dev
uv run uvicorn web.app:app --host 127.0.0.1 --port 8080
```

Then open http://127.0.0.1:8080/. The paused card's CSS loads through the adapter at http://127.0.0.1:8080/.

Static Decision Card files remain a fallback if you open them without the adapter:

- Approved or Denied: `web/static/key-resolved.html`
- Canned Path and error: `web/static/key-canned-error.html`

## Demo truth

| Kind | What |
|---|---|
| Built | FastAPI `/` adapter, Decision Card statics (paused, resolved, canned/error) |
| Not yet | Strands Graph, native interrupt on `submit_payment` |
| Mocked | Payment rail and outbound mail, labeled Mocked on the card |
| Synthetic | Ana, Cedar Supply, FN-1042, $412 |
| Hardcoded | Overnight fixture JSON used for Canned Path |

This README will not list an AgentCore URL until a live one exists. Until then, local Strands and the labeled Canned Path are the fallback.

## Layout

```
web/        Public adapter and Decision Card
agent/      Overnight graph, interrupt hook, tools
fixtures/   Canned overnight queue and interrupt envelope
deploy/     AgentCore container and seed job
```

See [ARCHITECTURE.md](ARCHITECTURE.md).

## License

MIT. See [LICENSE](LICENSE).
