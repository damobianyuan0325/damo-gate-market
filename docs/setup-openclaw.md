# 在 OpenClaw 中使用 damo-gate-market

`damo-gate-market` 是一个基于 Gate MCP 的行情模块，用于查询 Gate 上 BTC_USDT 和 ETH_USDT 的实时现货数据。

本文档介绍如何在 [OpenClaw](https://github.com/openclaw/openclaw) 中集成并使用该 skill。

---

## 一、前置条件

1. 已安装 OpenClaw，并有一个 workspace（例如：`~/.openclaw/workspace`）。
2. 已安装 `mcporter` CLI：

   ```bash
   npm install -g mcporter
   ```

3. 已配置 Gate MCP 服务器：

   ```bash
   mcporter config add gate https://api.gatemcp.ai/mcp --scope home
   mcporter list gate --schema
   ```

   确认输出中包含 `get_spot_tickers` 等工具，说明 Gate MCP 配置成功。

---

## 二、安装 damo-gate-market Skill

1. 将仓库克隆到 OpenClaw workspace：

   ```bash
   cd ~/.openclaw/workspace
   git clone https://github.com/damobianyuan0325/damo-gate-market.git
   ```

2. 确认目录结构：

   ```bash
   ls damo-gate-market
   # gate_market.py  SKILL.md  README.md  docs/
   ```

---

## 三、在对话中使用（示例流程）

下面是假设你的 Agent 已支持：
- 调用本地脚本
- 解析 JSON 输出

### 示例：查询 Gate 上 BTC/USDT 与 ETH/USDT 行情

**用户：**

> 查询 Gate 上 BTC 和 ETH 的最新价格以及 24 小时涨跌情况。

**Agent 内部步骤（逻辑示例）：**

1. 运行脚本获取行情 JSON：

   ```bash
   python3 damo-gate-market/gate_market.py
   ```

2. 解析脚本输出，例如：

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
   ```

3. Agent 根据 JSON 生成自然语言回复，例如：

> Gate 现货行情：  
> - BTC_USDT：现价 70,530.3，24h 涨跌 -2.93%，24h 成交额约 11.0 亿 USDT，高/低：73,555 / 70,143  
> - ETH_USDT：现价 2,064.86，24h 涨跌 -2.93%，24h 成交额约 3.70 亿 USDT，高/低：2,163.86 / 2,054.72

---

## 四、在早/晚报或 Agent 流程中的常见用法

你可以将 `gate_market.py` 嵌入现有的情报/简报生成流程中，例如：

1. 在生成早报/晚报之前先拉一次 Gate 行情：

   ```bash
   python3 damo-gate-market/gate_market.py > gate_spot_latest.json
   ```

2. 在简报脚本中读取 `gate_spot_latest.json`，生成一个【Gate 行情】板块。

   文本示例：

   ```text
   【Gate 行情（MCP）】

   BTC_USDT：现价 70,530.3，24h 涨跌 -2.93%，24h 成交额约 11.0 亿 USDT，高/低：73,555 / 70,143
   ETH_USDT：现价 2,064.86，24h 涨跌 -2.93%，24h 成交额约 3.70 亿 USDT，高/低：2,163.86 / 2,054.72
   ```

---

## 五、提示与扩展建议

- 当前版本只调用 Gate MCP 的公开市场数据工具，不需要 Gate 账号或 API Key。
- 如果你希望扩展更多交易对，可以修改 `gate_market.py` 中的 `PAIRS` 列表。  
- 如果希望加入合约行情（例如 BTC_USDT 永续）、资金费率、强平历史，可基于 Gate MCP 的期货工具进一步扩展脚本逻辑。

---

## 参考链接

- Gate MCP Server: <https://github.com/gate/gate-mcp>
- mcporter: <https://github.com/modelcontextprotocol/mcporter>
- OpenClaw: <https://github.com/openclaw/openclaw>
