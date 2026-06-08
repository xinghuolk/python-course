# Day 02 · list/dict 与 Pythonic 遍历

> 今天的目标不是背完所有容器 API，而是能自然处理 Python 里最常见的数据形状：`list[dict]`。这会直接服务自动化脚本、数据分析、FastAPI 的 JSON、以及后面的 AI/LLM 数据管线。

## 1. list：有序、可变、常用于一组记录
- `list` 类似 JS 的 Array，但 Python 没有 JS 那种稀疏数组心智；更常见的是紧凑序列。
- 常用操作：索引、切片、`append`、`extend`、`pop`、`len`、`in`。
- `list` 是可变对象。`b = a` 不会复制列表，只是多一个名字指向同一个列表。
- 如果要浅拷贝，用 `a.copy()` 或 `a[:]`。浅拷贝只复制外层容器，不复制内部对象。

## 2. dict：键值表，是 Python 数据处理核心
- `dict` 对应 JS object / Map、Lua table 的键值用法，但 Python 的 key 通常需要可哈希。
- 常用操作：`d[key]`、`d.get(key, default)`、`d[key] = value`、`key in d`。
- 遍历键值对用 `for key, value in d.items()`，比手动查 `d[key]` 更直接。
- Web API、JSON、配置文件、数据分析记录，都经常落成 `dict` 或 `list[dict]`。

## 3. tuple 与解包：不可变记录和多返回值
- `tuple` 是不可变序列，常用于固定结构的小记录：`point = (3, 4)`。
- 解包很常见：`x, y = point`。函数可以返回多个值，本质是返回 tuple。
- 对比 C：不需要传指针拿多个返回值；对比 JS：类似数组解构。

## 4. set：去重和集合运算工具
- `set` 是无序不重复集合，适合去重、快速成员判断、交并差。
- 常用：`seen = set()`、`seen.add(x)`、`x in seen`。
- 注意：set 不保留顺序。如果要“保序去重”，通常用 `seen` 辅助，再把结果放进 list。

## 5. Pythonic 遍历
- 直接遍历元素：`for item in items:`，不要先写下标循环。
- 需要下标时用 `enumerate(items)`。
- 并行遍历两组数据时用 `zip(names, scores)`。
- 遍历字典键值用 `.items()`。
- 对比 C：少写索引和边界条件；对比 JS：更偏向明确的迭代协议。

## 6. 推导式：过滤 + 映射
- list 推导式：`[expr for x in items if condition]`。
- dict 推导式：`{key_expr: value_expr for x in items if condition}`。
- 心智模型：先读 `for`，再读 `if`，最后看最左边生成什么。
- 只建议写一层推导式。嵌套太深时，普通 `for` 循环更清楚。

## 7. 排序与常用内置函数
- `sorted(items)` 返回新列表；`items.sort()` 原地修改。
- `key=` 指定排序依据：`sorted(records, key=lambda r: r["score"])`。
- 常用内置：`len`、`sum`、`min`、`max`、`any`、`all`。
- 先写清楚，再考虑压缩。Pythonic 不是越短越好，而是意图明确。

## 8. 今日练习（7 题，难度递增）
1. `filter_even_numbers`：list 遍历 / list 推导式。
2. `normalize_names`：字符串清洗 + 过滤空值。
3. `word_frequencies`：dict 计数。
4. `merge_scores`：`zip` + dict。
5. `top_students`：处理 `list[dict]`，按分数降序排序。
6. `unique_preserve_order`：set 辅助实现保序去重。
7. `summarize_orders`：小综合，按客户汇总有效订单数量和金额。

完成后进入本目录运行：

```bash
pytest -q
```

预计耗时：讲解 25-35 分钟，练习 55-75 分钟。
