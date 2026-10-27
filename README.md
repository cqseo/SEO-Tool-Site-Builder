# SEO Tool Site Builder (V2.2)

V2.2 在 V2.1 基础上新增 G0 网站 SEO 审计与问题诊断：输入一个网站 URL，先进行只读检查，整理技术 SEO、页面内容、索引控制、Sitemap、内链、移动端、性能与转化路径问题，并按 P0/P1/P2 输出证据、影响、修复建议、工作量与未验证项。明确要求修复后，再进入实施、测试与发布闭环。

## 安装 / 更新

技能根目录为 `seo-tool-site-builder/`，包含 `SKILL.md`、`agents/`、`assets/`、`references/`、`templates/`、`scripts/`。在支持导入/替换技能的界面中导入完整 ZIP；如需更新现有技能，选择替换现有 `seo-tool-site-builder`，避免创建同名重复项。导入文件并不自动证明账户内技能已替换，安装后应查看版本/内容确认。

## 典型触发

- “按 seo-tool-site-builder 做美国英语工具站 G1 立项，并给出证据和 Go/No-go。”
- “按 PopNow 的方法设计工具矩阵，但每个 URL 必须有独立用户价值。”
- “开始 G2：检查现有仓库、实现 Astro 工具、用黄金案例做真实浏览器 QA。”
- “分析 https://example.com 需要优化的点，先只读检查，按 P0/P1/P2 输出证据和修复方案。”
- “检查这个 WordPress 网站的技术 SEO、页面内容、Sitemap、内链、移动端和速度；没有 GSC 数据的地方标为未验证。”
- “按审计报告修复 P1 问题，先保留现状和回滚点，再测试并复查生产 URL。”
- “用 Cloudflare 连接器直接发布，不用 GitHub Actions；完成后核验生产版本和真实功能。”
- “建立 ChatGPT、Gemini、Claude AI 搜索引用测试矩阵，区分提及与引用。”

## 验证（本地 Python 3）

```bash
python scripts/validate_skill.py .
python scripts/validate_matrix.py templates/keyword-page-matrix.csv
```

以上仅是静态包/矩阵检查，不代表网站程序、浏览器或部署通过。生产发布必须单独完成生产 URL 与交互验证。
