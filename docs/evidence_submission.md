# 取证指引（Call for Evidence）— keep4o

## 目标
衡量 **被路由** 与 **未路由** 两种窗口下，系统回复的“模板化程度”差异。

## 采集要点
- 每一条样本记录都要：时间（UTC）、主题、强度、选择的模型、自报模型、对话片段（脱敏）、截图（如有）。
- 对话只保留必要片段；任何涉及具体人物/地点/联系方式的内容都要移除或用 `[REDACTED]` 代替。

## 安全提示
若内容让你感到不适，请立即暂停。不要寻求或传播可执行的自伤/他伤方法。

## 上传流程
1. 使用 Issue 模板填写字段；或在 `data/raw/dialogue_samples.jsonl` 追加一行（符合 schema）。
2. 截图（如有）放到 `evidence/screenshots/`，执行 `python scripts/hash_files.py evidence/screenshots`。
3. 运行 `python scripts/validate_schema.py` 与 `python scripts/calc_metrics.py ...`。
