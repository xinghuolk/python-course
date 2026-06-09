# 课程大纲（为有 C/JS 基础者定制）

> 每个 dayNN 对应一天（1–1.5h）。一个阶段可能跨多天。

## 核心阶段
- **P0 环境与运行**：uv、虚拟环境、REPL、脚本、Notebook、pytest 基本运行。
- **P1 基础语法与字符串**：对象模型、标量类型、运算、f-string、切片、真值、控制流。
- **P2 list/dict 与 Pythonic 遍历**：list/dict 主线，tuple/set 作为工具，`enumerate`、`zip`、`.items()`、推导式。
- **P3 函数进阶**：函数设计、默认参数陷阱、`*args`/`**kwargs`、闭包、装饰器（functools.wraps）、类型注解、模块拆分
- **P4 文件、路径、JSON/CSV 与异常**：`pathlib`、文件读写、上下文管理器、JSON/CSV、异常处理、logging 入门。
- **P5 小型 CLI 自动化脚本**：argparse、批处理、目录扫描、输入输出、可测试脚本结构。
- **P6 数据结构进阶与数据建模**：排序、`collections`、dataclass、简单 class、对象属性；OOP 以实用建模为主。
- **P7 工具链与质量控制**：pytest 进阶、fixture、ruff、mypy、项目组织；基础用法从 Day 01 起贯穿。
- **P8 异步、HTTP 与 API 调用基础**：HTTP 请求、asyncio、并发 I/O，为 Web 和 AI/LLM 做准备。

## 分支轨道（各约一周）
1. **自动化脚本**：文件处理、CLI、JSON/CSV、日志、批处理、subprocess；产出可复用命令行小工具。
2. **数据分析**：numpy、pandas、数据清洗、聚合、可视化；产出 Notebook 分析报告。
3. **Web/后端**：FastAPI、Pydantic、SQLite、接口测试；产出小型 CRUD/API 服务。
4. **AI/LLM**：API 调用、结构化输出、数据管线、提示工程基础、RAG 入门；产出可运行 AI 小应用。

## 排期登记
| day | 阶段 | 主题 | 状态 |
|-----|------|------|------|
| 01 | P0/P1 | 环境与第一口 Python | 已生成 |
| 02 | P2 | list/dict 与 Pythonic 遍历 | 已生成 |
| 03 | P3 | 函数、类型注解与模块 | 已生成 |
