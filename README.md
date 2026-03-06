# damo-gate-market

`damo-gate-market` 是一个基于 [Gate MCP](https://github.com/gate/gate-mcp) 的小型行情模块，
用于查询 Gate 上 **BTC_USDT** 和 **ETH_USDT** 的实时现货数据，
方便接入到 Agent / Bot / OpenClaw / Claude 等 AI 系统中。

底层依赖：

- Gate MCP Server：`https://api.gatemcp.ai/mcp`
- [mcporter](https://github.com/modelcontextprotocol/mcporter)（MCP 客户端工具）
- Python 3.9+

---

## 功能概览

当前版本专注一件事：

> 通过 Gate MCP 的 `get_spot_tickers` 工具，查询 Gate 现货 BTC/USDT 与 ETH/USDT 的实时行情，
> 并以统一 JSON 格式输出，方便上层系统消费。

返回结构包括：

- `exchange`：固定为 `Gate`
- `generated_at`：Unix 时间戳（秒）
- `spot`：行情列表（目前包含 BTC_USDT 和 ETH_USDT）

每个行情对象包含：

- `pair`：交易对（如 `BTC_USDT` / `ETH_USDT`）
- `last`：最新成交价
- `change_pct`：24 小时涨跌幅字符串（例如 `"-2.93"`）
- `quote_volume`：24 小时成交额（USDT）
- `high_24h`：24 小时最高价
- `low_24h`：24 小时最低价

示例输出：

```json
{
"generated_at": 1772788424,
"exchange": "Gate",
"spot": [
{
"pair": "BTC_USDT",
"last": "70530.3",
"change_pct": "-2.93",
"quote_volume": "1097242449.7663499",
"high_24h": "73555",
"low_24h": "70143"
},
{
"pair": "ETH_USDT",
"last": "2064.86",
"change_pct": "-2.93",
"quote_volume": "369775046.60013057362",
"high_24h": "2163.86",
"low_24h": "2054.72"
}
]
}
