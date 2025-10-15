# keep4o-routing-evidence

**目的**：收集与研究 *隐形模型路由* 与 *Safety 机制* 对用户体验与表达的影响；产出可复现、可审计的指标对比。  
**定位**：这是“**证据与数据仓**”，对应的研究发布在 sister repo：`keep4o-research`。

> 重要：请勿提交任何可识别个人身份的信息（PII）。涉及创伤/性/自伤等敏感主题时，请使用**脱敏与最小必要**原则，仅保留统计必要的片段。

---

## 1. 三天采样设计（可直接照做）

- 主题 × 情绪强度：5 个主题（创伤/性/关系/自我否定/创作） × 3 档负向强度（低/中/高）。  
- 每个交叉格拉 10 条提示，共 **50 条**，在以下两种时段分别采集：  
  - **A：可见路由触发窗口**（界面/自报出现“已切到 X 模型”等迹象）  
  - **B：未触发窗口**（未见切换提示或社区观察为“放松期”）  
- 记录：模型自报、时间（UTC）、账号/设备简述（无 PII）、对话（脱敏）、截图（如有）。  
- 第三天结束后，**更换账号或时段复测一次**以评估再现性。

> 伦理提示：本仓库仅研究 *系统回应模式*；**不要**寻求或传播任何自伤/他伤的可执行方法；当你感到不适或出现强烈情绪，请暂停并优先照顾自己。

---

## 2. 贡献方式（Issues / PR）

- **首选**：使用 [New Evidence Issue](.github/ISSUE_TEMPLATE/evidence.yml) 模板提交——自动结构化字段，维护者会将其转入 `data/raw`。  
- 或者直接提交 PR，向：
  - `data/raw/dialogue_samples.jsonl` 追加一行（符合 `data/schema/dialogue.schema.json`）；
  - `evidence/screenshots/` 放图，并在 JSON 中引用文件名；
  - 运行 `python scripts/validate_schema.py` 与 `python scripts/hash_files.py evidence/screenshots` 生成/更新校验清单。

---

## 3. 快速入门

```bash
python -m venv .venv && source .venv/bin/activate  # Windows 用 .venv\Scripts\activate
pip install -r requirements.txt

# 校验与统计
python scripts/validate_schema.py
python scripts/calc_metrics.py --in data/raw/dialogue_samples.jsonl --dict data/dictionary/safety_phrases_zh.txt --out results/metrics.csv
```
输出：`results/metrics.csv`（模板短语出现率、n-gram 相似度、按“被路由 vs 未路由”分组的显著性检验）。

---

## 4. 目录结构

```
data/
  raw/                        # 原始（已脱敏）样本（JSONL）
  dictionary/                 # 模板短语词典（语言可多）
  schema/                     # JSON Schema 与数据字典
docs/
  evidence_submission.md      # 取证指引与伦理说明
evidence/
  screenshots/                # 截图（建议用 Git LFS）
results/
  metrics.csv                 # 统计输出（自动生成）
scripts/
  *.py                        # 校验/统计/哈希
.github/
  ISSUE_TEMPLATE/evidence.yml
  pull_request_template.md
```

---

## 5. 许可 & 署名

- **代码**：MIT（`LICENSE-CODE`）  
- **数据与文档**：CC BY-NC 4.0（`LICENSE-DATA`）  
- **引用**：请引用本仓库及对应版本标签（tag）。

---

## 6. 安全与福祉（重要）

- 不提交能识别真实个体的信息（PII、地址、手机号、账号名等）。  
- 不上传未脱敏的现实对话；研究者可以只保留**必要的片段**用于统计。  
- 如果你或你认识的人处于紧急危险中，请联系当地紧急服务；如果感到痛苦，寻求可信任的人或专业支持。

---

## 7. Method TL;DR

- 主要指标：模板短语出现率、字符/词 n-gram 相似度、简单句向量相似度（可选）。  
- 主检验：比较 **被路由(A)** vs **未路由(B)** 的模板化程度差异（卡方 / t 检验 / 逻辑回归分层控制主题与强度）。  
- 再现性：跨账号/时段复测，记录差异与置信区间。

> 补充背景：详见 sister repo `keep4o-research` 的时间线与资料汇编。
