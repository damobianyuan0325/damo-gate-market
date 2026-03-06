# damo-gate-market

通过 Gate MCP 查询 Gate 上 BTC_USDT 和 ETH_USDT 的实时现货行情，
返回结构化数据供 Agent 使用。

## 能力

- 查询 Gate 现货 BTC_USDT 行情
- 查询 Gate 现货 ETH_USDT 行情
- 返回字段：
  - `pair`：交易对（BTC_USDT / ETH_USDT）
  - `last`：现价
  - `change_pct`：24h 涨跌幅（百分比字符串）
  - `quote_volume`：24h 成交额（USDT）
  - `high_24h` / `low_24h`：24h 高 / 低

## 前置条件

- 已安装 `mcporter` CLI：

  ```bash
  npm install -g mcporter
  ```

- 已配置 Gate MCP：

  ```bash
  mcporter config add gate https://api.gatemcp.ai/mcp --scope home
  mcporter list gate --schema  # 确认工具可用
  ```

## 使用方式（在 OpenClaw 中）

> 下面是预期用法，具体 Skill 接入逻辑可按系统工具调用方式实现。

示例自然语言指令：

-「查询 Gate 上 BTC 和 ETH 的最新价格和 24 小时表现」

预期行为：

1. Skill 调用：

   ```bash
   python3 damo-gate-market/gate_market.py
   ```

2. 解析 JSON 输出
3. Agent 将结果整理成自然语言返回，例如：

> BTC_USDT：现价 70,928.6，24h -1.74%，24h 成交额 11.0 亿 USDT，高/低：73,555 / 70,143  
> ETH_USDT：现价 2,076.76，24h -1.81%，24h 成交额 3.74 亿 USDT，高/低：2,163.86 / 2,054.72
