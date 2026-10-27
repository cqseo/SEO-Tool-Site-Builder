# Changelog

## 2.2.0 — 2026-10-27

- 新增 G0 网站 SEO 审计与问题诊断模式：输入 URL 后默认只读检查，不擅自修改站点。
- 新增 `references/site-audit-and-diagnosis.md`，覆盖技术 SEO、页面内容、索引控制、Sitemap、内链、移动端、性能、转化和 GSC/GA4 证据边界。
- 新增 `templates/site-audit-report.md`，统一输出 URL 级证据、P0/P1/P2 优先级、修复建议、工作量、状态和未验证项。
- 明确“仅分析”与“实际修复”分离；只有用户明确要求执行时才进入 G2/G3，执行后需复查。

## 2.1.0 — 2026-10-27

- 新增 `references/execution-and-evidence.md`：工具发现、变更前快照、权限边界、测试证据分级、生产发布验收和 AI 搜索实验规范。
- 强化 G2 黄金案例与浏览器交互 QA，要求明确预期值/实际值，不把 DOM 存在或 HTTP 200 当作交互通过。
- 强化 G3 实际 commit/生产版本/路由/流量与正式 URL 的闭环核验。
- 明确尊重用户指定的发布通道；用户指定 Cloudflare 连接器时，不擅自引入 GitHub Actions。
- 增加 ChatGPT/Gemini/Claude 等 AI 搜索引用实验规范，区分品牌提及、裸链接、证据引用与真实引荐访问。
- 更新发布验收清单与安装说明；静态包验证不代表真实站点已通过。

## 2.0.0 — 2026-10-25

- 复用原有 G1/G2/G3、计算器 QA、部署和真实性底线。
- 新增工具矩阵、平台复用、增长/商业化参考与可复用模板。
- 新增静态检查脚本、`agents/openai.yaml` 与 SVG 图标。
