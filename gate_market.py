#!/usr/bin/env python3
import subprocess
import json
import sys
import time

PAIRS = ["BTC_USDT", "ETH_USDT"]


def call_mcp_ticker(pair: str) -> dict | None:
    """调用 Gate MCP 的 get_spot_tickers 工具，获取单个交易对的 ticker。
    使用形式：mcporter call gate get_spot_tickers currency_pair=BTC_USDT
    """
    cmd = ["mcporter", "call", "gate", "get_spot_tickers", f"currency_pair={pair}"]
    try:
        out = subprocess.check_output(cmd, text=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERR] mcporter for {pair}: {e}", file=sys.stderr)
        return None

    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        print(f"[ERR] decode JSON for {pair}: {out[:200]}", file=sys.stderr)
        return None

    tickers = data.get("tickers") or []
    return tickers[0] if tickers else None


def main():
    results = []
    for pair in PAIRS:
        t = call_mcp_ticker(pair)
        if not t:
            continue
        results.append(
            {
                "pair": t.get("currency_pair"),
                "last": t.get("last"),
                "change_pct": t.get("change_percentage"),
                "quote_volume": t.get("quote_volume"),
                "high_24h": t.get("high_24h"),
                "low_24h": t.get("low_24h"),
            }
        )

    out = {
        "generated_at": int(time.time()),
        "exchange": "Gate",
        "spot": results,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
