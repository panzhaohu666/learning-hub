# 🧠 LLM 学习 + 软考备考 · 完整自学计划

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

> 一份 **11,737 行**的零基础→大模型开发工程师 + 软件设计师备考的自学路线图。  
> 专为在职自学设计：**手机阅读 + 电脑编码**，全程不依赖视频。

---

## 📖 这是什么？

这是一个**双线并行的自学计划**，包含两部分：

| 计划 | 时长 | 目标 | 每周投入 |
|------|------|------|----------|
| 🧠 **6个月大模型学习计划** | 26 周（480h） | 大模型开发工程师 / 算法工程师 | ~11h |
| 📝 **软件设计师备考计划** | 9 个月（259h） | 2027年5月软考 · 上下午45+ | ~8h |

### 核心理念

```
白天手机 = 纯阅读输入（看/读/背/想）
晚上电脑 = 纯输出（写/训/调/测）
全程不依赖视频，只靠文字材料
```

---

## 🗺️ 大模型学习路线图（7 阶段）

```
阶段一（2周）         阶段二（5周）          阶段三（9周）★核心★
LLM入门               大模型应用开发          大模型核心开发技术
Prompt工程            Python工程化            ML → PyTorch → DL
本地部署              NumPy/Pandas            NLP → 手写Transformer
ChatBot               Dify/Coze              BERT/GPT-2微调
    ↓                    ↓                      ↓
阶段四（3周）         阶段五（5周）★核心★    阶段六（1周）
Agent开发             大模型定制开发          算法进阶
LangChain             Mini-GPT从零训练       CLIP/多模态
LangGraph              LoRA/QLoRA微调         Stable Diffusion
RAG系统               DPO对齐/vLLM部署       MoE概念
    ↓                    ↓                      ↓
                   阶段七（1周+）
                   大厂面试专题
                   LeetCode + 系统复习
```

### ⭐ 核心项目清单（GitHub 作品集）

| # | 项目 | 阶段 | 技能点 |
|---|------|------|--------|
| 1 | ChatBot 原型 | 一 | 多轮对话 + 记忆 + 角色设定 |
| 2 | 数据处理 Pipeline | 二 | ETL + Pandas + 数据库 |
| 3 | Prompt 工程实验报告 | 二 | Zero-shot/Few-shot/CoT 对比 |
| 4 | Dify/Coze 智能体 | 二 | 低代码 Agent 开发 |
| 5 | **从零实现 Transformer** | 三 | ★核心★ 手写 Attention/Encoder/Decoder |
| 6 | PyTorch 自定义模块集 | 三 | 手写 softmax/LayerNorm/Dropout |
| 7 | RAG 问答系统 | 四 | LangChain + 向量数据库 |
| 8 | 多智能体协作系统 | 四 | LangGraph + ReAct Agent |
| 9 | **Mini-GPT** | 五 | ★核心★ 从零训练 GPT 模型 |
| 10 | LoRA/QLoRA 微调项目 | 五 | ★核心★ PEFT + 模型发布 HuggingFace |
| 11 | 模型部署项目 | 五 | vLLM + FastAPI + Docker |
| 12 | 面试准备仓库 | 七 | 算法题解 + 面试题整理 |

---

## 📝 软件设计师备考路线图（3 阶段）

```
阶段一（8-10月）        阶段二（11-1月）         阶段三（2-5月）
系统复习                重点突破                真题冲刺
上午题12模块全过         下午题5题型逐个击破      16套真题×3轮
数据结构/算法/软工        DFD/ER图/UML/算法       全真模拟
```

### 上午题分值分布

| 模块 | 分值 | 优先级 |
|------|------|--------|
| 数据结构与算法 | 10-12 | ★★★ |
| 软件工程 | 10-12 | ★★★ |
| 面向对象技术 | 8-10 | ★★★ |
| 程序设计语言 | 6-8 | ★★ |
| 操作系统 | 5-7 | ★★ |
| 计算机组成 | 5-7 | ★★ |
| 数据库 | 5-7 | ★★ |
| 计算机网络 | 5-7 | ★★ |

---

## 📂 仓库结构

```
llm-learning-hub/
├── README.md                           ← 你在这里
│
├── 大模型学习/
│   ├── 01-总纲-6个月大模型学习计划.md    ← 时间分配、7阶段概览、防崩预案
│   ├── 02-学习资料清单.md               ← 80+ 篇资料（含链接、优先级、阅读设备）
│   ├── 03-阶段一-大模型开发入门.md      ← 第1-2周：LLM概念→ChatBot→ReAct
│   ├── 04-阶段二-大模型应用开发.md      ← 第3-7周：Python→Pandas→Dify
│   ├── 05-阶段三上-机器学习与PyTorch.md  ← 第8-11周：ML→PyTorch→手写LayerNorm
│   ├── 06-阶段三下-深度学习与Transformer.md ← 第12-16周：反向传播→手写Transformer ★
│   └── 07-阶段四至七-Agent到面试.md     ← 第17-26周：LangChain→Mini-GPT→面试
│
└── 软件设计师/
    ├── 01-备考总纲.md                   ← 考试结构、时间分配、考点速记
    ├── 02-阶段一-每日学习指南.md        ← 8-10月：链表→KMP→排序→UML→PV→子网
    └── 03-阶段二三-每日学习指南.md      ← 11-5月：下午题拆解+三轮真题冲刺
```

---

## 🚀 如何使用

### 1. 克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/llm-learning-hub.git
cd llm-learning-hub
```

### 2. 选择你的路线

- **只学大模型** → 从 `大模型学习/01-总纲.md` 开始，按顺序走 7 个阶段
- **只备考软考** → 从 `软件设计师/01-备考总纲.md` 开始
- **双线并行**（推荐）→ 两份总纲都要看，里面有每周时间分配表

### 3. 跟着每日指南走

每个"阶段·每日学习指南"文件的结构：

```
📱 手机摸鱼（上午 30 分钟）
   ├── 核心知识点（直接看，不需要额外查资料）
   ├── 今日思考题（脑子里过一遍）
   └── 规划今晚要写什么

💻 晚上电脑（2 小时）
   ├── 回顾白天笔记（5 分钟）
   ├── 对着白天的知识写代码（30 分钟）
   ├── 核心任务（55 分钟）
   ├── 记录 + Obsidian 笔记（20 分钟）
   └── 规划明天（10 分钟）
```

### 4. 使用 Obsidian 管理知识库

所有学习笔记建议用 Obsidian 管理，总纲中有完整的目录结构建议。

---

## 🎯 适合谁

- ✅ 在职程序员，想转行大模型方向
- ✅ 计算机专业在校生，需要系统学习路线
- ✅ 软考备考者，需要详细的每日计划
- ✅ **只能用碎片时间自学的任何人**

### 不适合

- ❌ 想通过看视频学习的（本计划全程文字材料）
- ❌ 零编程基础（需要至少会 Python 基础语法）

---

## 📊 关键数据

| 指标 | 数值 |
|------|------|
| 文件总数 | 10 个核心文件 |
| 总行数 | 11,737 行 |
| 大模型学习材料 | 80+ 篇（含论文、源码、文档链接） |
| 软考真题覆盖 | 近 8 年 16 套 |
| 计划项目数 | 12+ 个 GitHub 项目 |
| GPU 预算 | ¥2,000-4,000（半年） |

---

## ⚡ 快速开始（第 0 周）

在正式学习前，先完成环境准备：

```bash
# 1. 安装基础环境
conda create -n llm python=3.10 -y && conda activate llm

# 2. 安装核心工具
pip install torch jupyter wandb transformers datasets

# 3. 安装 Ollama（本地运行模型）
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2:0.5b

# 4. 注册账号
# huggingface.co / wandb.ai / autodl.com / platform.deepseek.com
```

完整的环境准备 Checklist 见 `大模型学习/01-总纲.md` 第十五章。

---

## 📚 必备资料速览

| 阶段 | 核心资料 | 类型 |
|------|----------|------|
| 一 | Ollama 文档、OpenAI Prompt Guide | 🌐 网页 |
| 二 | 《流畅的Python》、NumPy/Pandas 文档 | 📖 书籍 |
| 三 | d2l.ai、Attention Is All You Need、The Illustrated Transformer | 📄 论文+🌐 |
| 四 | LangChain/LangGraph 官方文档 | 🌐 网页 |
| 五 | nanoGPT 源码、GPT-2/LLaMA/LoRA 论文 | 💾 源码+📄 |
| 六 | CLIP 论文、Stable Diffusion 博客 | 📄 论文 |
| 七 | LeetCode Hot 100、《百面机器学习》 | 🌐+📖 |

完整清单（含链接、优先级、阅读设备）见 `大模型学习/02-学习资料清单.md`。

---

## 🤝 贡献

这份计划还在不断完善中。如果你：

- 发现了错误或过时的链接
- 有更好的学习资源推荐
- 完成了某个阶段想分享经验

欢迎提 Issue 或 PR！

---

## 📄 License

MIT © [Your Name]

---

> **"480 小时认真用，比 700 小时磨洋工强得多。"**  
> —— 来自这份计划的防崩指南

> 坚持不下去的时候，翻到总纲第十八章「防崩预案」。  
> 允许降级，不允许归零。
