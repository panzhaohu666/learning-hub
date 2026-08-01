# 阶段四至七 · 每日学习指南

阶段四~七 · 每日学习指南（完整版）
### Agent开发 + 模型定制 + 算法进阶 + 面试（第17-26周）


每一周都是"手机核心知识 + 晚上完整代码 + 周六项目"

### 阶段四 · 大模型智能体开发（第17-19周）


### 第17周 · LangChain 实战
### ── 本周目标：掌握 LangChain 的核心抽象──
### 第17周 · 星期一：LCEL 表达式语言
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：LangChain 的核心设计思想

核心知识点

1. LangChain 解决了什么问题？

阶段一中你直接调 OpenAI API，代码是这样的：
```python
     response = client.chat.completions.create(model="...", messages=[...])
     print(response.choices[0].message.content)
     ```
```

这在小项目中没问题。但当你的应用需要：
- 多种 Prompt 模板切换
- 对话历史管理
- 工具调用（搜索引擎/计算器/数据库查询）
- RAG 检索增强
- 多云模型切换（今天用 DeepSeek，明天换 GPT）
...你会发现代码越来越乱，散落在各处。

LangChain 提供了统一的"积木"来组装这些能力。

2. LCEL（LangChain Expression Language）—— 核心抽象

LCEL 用 Unix 管道的思路串联 LLM 应用：

```
```python
     chain = prompt | llm | output_parser
     ```
```

解释：
- `prompt` 产出格式化的消息
- `|` 把左边的输出传给右边
- `llm` 收到消息后调用大模型
- `output_parser` 把 LLM 的回复转成结构化数据

每一步是一个"Runnable"，管道符 `|` 是 `Runnable.__or__()` 的语法糖。

LCEL 的优势：
① 自动支持 async/streaming/batch
② 中间结果可检查：`chain.invoke()` 每一步都能断点调试
③ 易于组合：`chain1 | chain2 | chain3`

今日思考题
- 如果你不用 LangChain，纯手写一个"Prompt模板+LLM调用+JSON解析"的流水线，
和 LCEL 的 `prompt | llm | output_parser` 相比，代码量差多少？

### 手机摸鱼 · 下午 30 分钟
1. Obsidian：新建 Agent与RAG/LangChain笔记.md
记录 LCEL 的管道思想 + 三个核心概念（Runnable, prompt, output_parser）
2. 今晚计划：搭建第一个 LCEL Chain

### 晚上电脑 · 2h
19:35-20:05  第一个 LCEL Chain（30min）

```
```bash
    pip install langchain langchain-openai
    ```
```

```
```python
    # chain_basics.py —— 你的第一个 LangChain 应用
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
```

```python
# ① 定义 LLM（和阶段一一样，DeepSeek API）
    llm = ChatOpenAI(
        model="deepseek-chat",
        api_key="你的Key",
        base_url="https://api.deepseek.com",
        temperature=0
    )
```

```python
# ② 定义 Prompt 模板
    # 和阶段一的手写模板一样，但这里用类封装了
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是{role}。用{language}回复，不超过{max_words}字。"),
        ("user", "{input}")
    ])
```

```python
# ③ 输出解析器：把 LLM 的 AIMessage 对象提取为纯字符串
    output_parser = StrOutputParser()
```

```python
# ④ 用 LCEL 管道串联
    chain = prompt | llm | output_parser
```

```python
# ⑤ 调用
    result = chain.invoke({
        "role": "Python 专家",
        "language": "中文",
        "max_words": "100",
        "input": "解释什么是装饰器"
    })
    print(result)
    ```
```

运行后你会看到 LLM 用中文、不超过 100 字解释了装饰器。

关键理解：chain.invoke() 触发了整条管道：
prompt.format(**input) → LLM 调用 → StrOutputParser 提取结果
你只写了一行 `prompt | llm | output_parser`，LangChain 帮你处理了
所有的中间传递、异步、错误处理。

20:05-21:00  对比实验（55min）

目标：同一个任务，对比"纯 OpenAI API"和"LangChain LCEL"的代码差异。

任务：做一个翻译器，支持多语言切换。

纯 OpenAI API 写法：
```
```python
    def translate_plain(text, target_lang):
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"你是翻译助手，把输入翻译成{target_lang}"},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    ```
```

LangChain 写法：
```
```python
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是翻译助手，把输入翻译成{target_lang}"),
        ("user", "{text}")
    ])
    chain = prompt | llm | StrOutputParser()
    chain.invoke({"text": "Hello world", "target_lang": "中文"})
    ```
```

表面看只是"把 f-string 换成了 ChatPromptTemplate"，但实际上：
- LangChain 版本可以轻易加 memory、加 tool、加 streaming
- 可以 `.batch()` 批量翻译 100 句话
- 可以 `.astream()` 做打字机效果

练习：用 `.batch()` 一次翻译 5 句话，看是不是比循环调用快。

21:00-21:30  记录 + 规划
- LCEL 的核心思想：一切皆 Runnable，管道组合
- 明天看：Memory（对话记忆）

- [ ] 今日完成检查
- [ ] `prompt | llm | output_parser` 管道跑通
- [ ] batch() 批量调用成功
### 第17周 · 星期二：Memory（对话记忆）
---
### 手机摸鱼 · 上午 30 分钟
核心知识点

1. LLM 是无状态的

每次调用 API，模型不知道你是谁、之前聊了什么。
阶段一中你在 chatbot_v3.py 用手动维护 messages 列表的方式
解决这个问题——把对话历史 append 到列表里，每次全量发给 LLM。

问题是：对话长了怎么办？100 轮对话 = 几万 token，不仅贵，而且
可能超出模型的上下文窗口（Qwen2-0.5B 只有 32K tokens）。

2. LangChain Memory 的三层抽象

BaseChatMessageHistory：存消息的底层（可以存内存/Redis/数据库）
└── RunnableWithMessageHistory：把 Memory 注入到 Chain 中

你不需要手动管理 messages 列表了，LangChain 帮你做：
- 自动从存储加载历史消息
- 把历史消息和当前输入合并
- 调用 LLM 后自动存储新的回复

3. 对话摘要（ConversationSummaryMemory）

当对话太长时，不存全部消息，而是用 LLM 生成一个"对话摘要"。
下次只需把"摘要 + 最近几轮消息"发给 LLM，大大节省 token。

```
```python
     原对话（2000 token）→ LLM 生成摘要 → "用户在问退货流程，客服已告知..."
                                          （50 token）
     ```
```

今日思考题
- 阶段一的 messages 列表方案和 LangChain Memory 方案，本质上都是
"存历史 → 合并 → 发给 LLM"。那 LangChain 的价值在哪？
答：抽象 + 可替换存储（同上代码换了存储后端不需要改 Chain 代码）。

### 晚上电脑 · 2h
19:35-20:35  带 Memory 的 Chain（60min）

建文件 chain_with_memory.py：

```
```python
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.runnables import RunnableWithMessageHistory
    from langchain_community.chat_message_histories import ChatMessageHistory
    from langchain_core.output_parsers import StrOutputParser
```

llm = ChatOpenAI(model="deepseek-chat", api_key="你的Key",
base_url="https://api.deepseek.com")

```python
# 定义一个带"历史占位符"的 Prompt
    # MessagesPlaceholder：一个"槽位"，运行时会把历史消息插入到这里
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是友好的AI助手，用中文回复"),
        MessagesPlaceholder(variable_name="history"),  # ← 历史消息插这里
        ("user", "{input}")
    ])
```

chain = prompt | llm | StrOutputParser()

```python
# ===== Memory 管理 =====
    # 用一个字典存储不同 session 的历史
    store = {}
```

```python
def get_history(session_id):
        """根据 session_id 获取对应的对话历史对象"""
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]
```

```python
# RunnableWithMessageHistory：把 Memory 包装到 Chain 上
    chain_with_history = RunnableWithMessageHistory(
        chain,              # 原始的 chain
        get_history,        # 获取历史的函数
        input_messages_key="input",    # chain 的输入中哪个字段是用户消息
        history_messages_key="history" # chain 的输入中哪个字段是历史
    )
```

```python
# ===== 测试多轮对话 =====
    session_config = {"configurable": {"session_id": "user_A"}}
```

```python
# 第一轮
    resp = chain_with_history.invoke(
        {"input": "我叫小明，我喜欢打篮球"},
        config=session_config
    )
    print(f"Bot: {resp}")
```

```python
# 第二轮：不用再告诉它名字，它应该记得
    resp = chain_with_history.invoke(
        {"input": "我叫什么名字？我的爱好是什么？"},
        config=session_config
    )
    print(f"Bot: {resp}")
    # 应该输出 "你叫小明，喜欢打篮球"
```

```python
# ===== 验证隔离：另一个 session 不知道小明 =====
    resp = chain_with_history.invoke(
        {"input": "我叫什么名字？"},
        config={"configurable": {"session_id": "user_B"}}
    )
    print(f"Bot(user_B): {resp}")
    # 应该不知道（因为是不同的 session）
    ```
```

理解三层关系：
ChatMessageHistory（底层存储）
→ get_history(session_id)（工厂函数）
→ RunnableWithMessageHistory（把存储注入到 Chain）
→ chain_with_history.invoke()（用户只需关心对话内容）

20:35-21:15  改写阶段一的 ChatBot（40min）
用 LangChain 的 Memory 机制重写阶段一的 smart_assistant.py，
对比代码量：原来手动管理 messages 列表需要约 50 行，
LangChain 版本约 25 行。

21:15-21:30  规划明天
明天看：Tool（让 LLM 调用外部函数）—— LangChain 版比阶段一的
原生 OpenAI function calling 更优雅。

- [ ] 今日完成检查
- [ ] 多轮对话记忆生效
- [ ] 不同 session 之间隔离
- [ ] 理解 MessagesPlaceholder 的作用
### 第17周 · 星期三：Tool 使用（让 LLM 调用外部工具）
---
### 手机摸鱼 · 上午 30 分钟
核心知识点

1. Tool 的底层原理（回顾阶段一的 function calling）

LLM 不执行工具，它只输出"我想调用哪个工具、传什么参数"。
你的代码解析这个请求 → 执行工具 → 把结果发给 LLM → LLM 生成最终回复。

在 LangChain 中，Tool 被封装为一个类，包含：
- name：工具名
- description：工具描述（LLM 据此判断何时调用）
- args_schema：参数格式（Pydantic 模型定义）
- _run()：实际执行逻辑

2. @tool 装饰器

LangChain 提供了 `@tool` 装饰器，把一个普通 Python 函数
变成一个 Tool 对象。你只需写函数逻辑 + docstring，
LangChain 自动从 docstring 提取工具描述和参数文档。

今日思考题
- 阶段一用原生 OpenAI function calling，需要写 tools 参数的 JSON Schema。
LangChain 的 @tool 装饰器自动从 Python 函数的 type hints 和 docstring
生成这个 Schema。这就是"抽象的价值"。

### 晚上电脑 · 2h
19:35-20:35  定义 Tool + bind_tools（60min）

建文件 langchain_tools.py：

```
```python
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, ToolMessage
```

```python
# ===== 定义工具 =====
    # @tool 装饰器：把函数变成 Tool 对象
    # docstring 就是工具的 description，LLM 靠这个判断何时调用
```

@tool
```python
def get_weather(city: str) -> str:
        """获取指定城市的天气信息。输入城市名称（如'北京'）。"""
        weather_data = {
            "北京": "晴，25°C，湿度 40%",
            "上海": "阴，28°C，湿度 70%",
            "深圳": "雷阵雨，30°C，湿度 85%",
        }
        return weather_data.get(city, f"暂无{city}的天气数据")
```

@tool
```python
def calculator(expression: str) -> str:
        """计算数学表达式。输入如 '35*12' 或 '(100+200)/3'。"""
        try:
            return str(eval(expression))
        except Exception as e:
            return f"计算错误: {e}"
```

@tool
```python
def search_knowledge(query: str) -> str:
        """在内部知识库中搜索信息。输入搜索关键词。"""
        knowledge = {
            "退货政策": "7天内无理由退货，商品需保持原包装",
            "运费": "满99包邮，不满99运费8元",
        }
        for key, value in knowledge.items():
            if key in query:
                return value
        return f"未找到关于'{query}'的信息"
```

```python
# ===== 绑定工具到 LLM =====
    tools = [get_weather, calculator, search_knowledge]
    llm = ChatOpenAI(model="deepseek-chat", api_key="你的Key",
                     base_url="https://api.deepseek.com")
    llm_with_tools = llm.bind_tools(tools)
```

```python
# ===== 单轮工具调用测试 =====
    messages = [HumanMessage(content="北京今天天气怎么样？")]
    response = llm_with_tools.invoke(messages)
```

```python
# 检查 LLM 是否决定调用工具
    if response.tool_calls:
        for tool_call in response.tool_calls:
            print(f"模型决定调用: {tool_call['name']}({tool_call['args']})")
            # 输出：模型决定调用: get_weather({'city': '北京'})
    else:
        print(f"模型直接回复: {response.content}")
    ```
```

20:35-21:00  多轮工具调用循环（25min）

```
```python
    # ===== 完整的工具调用循环 =====
    def chat_with_tools(user_input):
        messages = [HumanMessage(content=user_input)]
```

```python
# 第一轮：模型决定是否调工具
        response = llm_with_tools.invoke(messages)
        messages.append(response)
```

```python
# 如果模型要调工具，逐个执行
        if response.tool_calls:
            for tool_call in response.tool_calls:
                # 找到对应的工具函数
                tool_func = {t.name: t for t in tools}[tool_call["name"]]
                # 执行工具
                result = tool_func.invoke(tool_call["args"])
                print(f"  执行工具 {tool_call['name']} → {result}")
                # 把工具结果加入消息
                messages.append(ToolMessage(content=result, tool_call_id=tool_call["id"]))
```

```python
# 第二轮：把工具结果发给模型，生成最终回复
            final_response = llm.invoke(messages)
            print(f"Bot: {final_response.content}")
        else:
            print(f"Bot: {response.content}")
```

```python
# 测试
    chat_with_tools("北京天气如何？")
    chat_with_tools("计算 156 * 38")
    chat_with_tools("你们的退货政策是什么？")
    ```
```

21:00-21:30  记录 + 规划
- @tool 装饰器自动生成的工具 Schema 是什么样的？
（打印 tool.get_weather.args_schema.schema() 看看）
- 明天看：Agent —— 让 LLM 自主规划和组合多轮工具调用

### 第17周 · 星期四-六：ReAct Agent + 综合项目
---
### 星期四
ReAct Agent
手机：回顾阶段一的 ReAct 循环（Thought→Action→Observation）
晚上：用 LangGraph 的 create_react_agent 一行创建 Agent
```
```python
    from langgraph.prebuilt import create_react_agent
    agent = create_react_agent(llm, tools)
    result = agent.invoke({"messages": [HumanMessage(content="...")]})
    ```
    对比阶段一：手动实现 ReAct 循环需要约 80 行代码，
    LangGraph 一行搞定。
```

### 星期五
Agent + Memory 整合
把 Memory 和 Tool 组合到一个链中，做一个"有记忆、能调工具"的智能助手。

### 星期六 · 3.5h
综合项目
14:00-17:00：智能客服系统
- 知识库搜索工具（查退货政策/运费/营业时间）
- 订单查询工具（根据订单号查状态）
- 对话记忆（记住客户名字和历史问题）
- 如果工具找不到答案，回退到 LLM 自由回答
17:00-17:30：push GitHub + README

- [ ] 第17周完成检查
- [ ] LCEL 管道能独立搭建
- [ ] Memory 多轮对话 + session 隔离
- [ ] @tool 定义三个以上工具
- [ ] ReAct Agent 一行创建
### 第18周 · RAG 全流程 + LangGraph
### ── 本周目标：搭建完整 RAG 系统 + 掌握 LangGraph 工作流 ──
### 第18周 · 星期一-二：Embedding + 向量数据库
---
### 手机摸鱼 · 星期一
核心知识点

1. RAG 解决什么问题？

LLM 有两个痛点：
① 知识截止日期（训练数据有截止时间，不知道之后发生的事）
② 幻觉（没有的知识会瞎编）

RAG 的思路：回答前先去"翻资料"，把相关资料拼到 Prompt 里，
让 LLM 基于资料回答。LLM 变成了"阅读理解+总结"而不是"记忆"。

2. Embedding（向量嵌入）是什么？

把一段文字变成一个固定维度的浮点数向量（如 768 维）。
核心性质：语义相近的文字，向量也相近。

"我喜欢猫" embedding → [0.23, -0.45, 0.67, ...]（768维）
"我喜爱猫咪" embedding → [0.25, -0.44, 0.65, ...]（非常接近！）
"今天天气很好" embedding → [-0.12, 0.89, -0.33, ...]（差异很大）

cos("喜欢猫","喜爱猫咪") ≈ 0.95 → 高度相似
cos("喜欢猫","天气很好") ≈ 0.12 → 不相关

3. 向量数据库

普通数据库存的是"精确值"（name='张三'），查的是"相等"。
向量数据库存的是"向量"，查的是"相似"（余弦距离最小的前K个）。

工作流程：
① 把文档切成小块(chunk)
② 每块用 Embedding 模型转成向量
③ 存入向量数据库
④ 用户提问 → 转成向量 → 数据库找最相似的K块 → 拼到Prompt → LLM回答

### 手机摸鱼 · 星期二
阅读主题：Chunking 策略

文本分割是 RAG 最关键的一步。切得不好，检索就不准。

Chunk Size 的选择：
太小（100字）：信息不完整，LLM 看不懂上下文
太大（2000字）：噪声多，检索不精准
经验值：中文 300-800 字，英文 500-1500 字符

Chunk Overlap（重叠）：
相邻两块之间重叠一部分，防止关键信息被"切断"在边界上。
经验值：Chunk Size 的 10-20%

分隔符优先级（RecursiveCharacterTextSplitter）：
["\n\n" → "\n" → "。" → "." → " " → ""]
先按段落分 → 太大就按句子分 → 还大就按词分 → 再大就按字符强制截断

### 晚上电脑 · 星期一
19:35-21:00  搭建 RAG 全流程

```
```bash
    pip install langchain langchain-community chromadb sentence-transformers
    ```
```

```
```python
    # rag_pipeline.py —— 从文档到问答的完整 RAG
```

```python
# === 1. 加载文档 ===
    from langchain_community.document_loaders import TextLoader
    loader = TextLoader("company_faq.txt", encoding="utf-8")
    docs = loader.load()
    print(f"加载 {len(docs)} 个文档")
```

```python
# === 2. 文本分割 ===
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,        # 每块最多 500 字
        chunk_overlap=50,      # 相邻块重叠 50 字
        separators=["\n\n", "\n", "。", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(docs)
    print(f"分割为 {len(chunks)} 个文本块")
```

```python
# === 3. Embedding 模型 ===
    from langchain_community.embeddings import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-zh-v1.5",  # 中文友好，轻量
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}  # 归一化后余弦=内积
    )
```

```python
# === 4. 向量数据库存储 ===
    from langchain_community.vectorstores import Chroma
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"  # 持久化到磁盘
    )
    print(f"存入 {vectorstore._collection.count()} 条向量")
```

```python
# === 5. 检索器 ===
    retriever = vectorstore.as_retriever(
        search_type="similarity",  # 相似度检索
        search_kwargs={"k": 3}     # 返回最相似的 3 块
    )
```

```python
# === 6. 测试检索 ===
    query = "如何退货？"
    relevant_docs = retriever.invoke(query)
    for i, doc in enumerate(relevant_docs):
        print(f"\n--- 相关文档 {i+1} ---")
        print(doc.page_content[:200])
    ```
```

### 晚上电脑 · 星期二
19:35-21:00  RAG Chain 完整搭建

```
```python
    # === 7. RAG Chain ===
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate
```

```python
# Prompt：告诉 LLM 如何利用检索到的资料
    system_prompt = """你是一个专业的客服助手。请严格根据以下资料回答问题。
    如果资料中没有相关信息，如实说"根据现有资料，我无法回答这个问题"，
    不要编造任何信息。
```

参考资料：
{context}"""

prompt = ChatPromptTemplate.from_messages([
("system", system_prompt),
MessagesPlaceholder(variable_name="chat_history"),
("user", "{input}")
])

```python
# combine_docs_chain：把检索到的多篇文档拼接起来 + LLM 生成答案
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
```

```python
# retrieval_chain：检索 + 生成 的完整链条
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)
```

```python
# 测试
    result = rag_chain.invoke({"input": "退货需要什么条件？"})
    print(result["answer"])
    # 输出应基于 company_faq.txt 的内容回答
    ```
```

- [ ] 完成检查
- [ ] 文档→分割→Embedding→向量库→检索→生成，全流程跑通
- [ ] 理解 Chunk Size 对检索结果的影响
### 第18周 · 星期三-四：RAG 优化 + LangGraph 入门
---
### 星期三
RAG 优化技巧
手机摸鱼：
① Reranker：检索后用更精确的模型对 top-k 结果重新排序。
为什么需要？向量相似度高≠语义上真正相关。
常用：BGE-Reranker、Cohere Rerank API。
② 混合检索：关键词匹配(BM25) + 向量检索，二者取并集。
为什么需要？向量检索对专有名词/缩写（如"API""SDK"）不够敏感，
关键词检索可以补上这块。

晚上：给 RAG 加上 Reranker（pip install sentence-transformers 后用
CrossEncoder 做重排序）

### 星期四
LangGraph 工作流
手机摸鱼：
LangChain 的 Chain 是"直线"流水线：A→B→C→D
LangGraph 的 Graph 是"有分支的图"：A→B→条件判断→C或D→E

适合场景：
- 复杂 Agent：先分析用户意图 → 意图A走检索 → 意图B走计算 → 最后汇总
- 多步推理：查天气→如果下雨→查室内活动→推荐
- RAG with fallback：先检索→如果答案不够好→改写查询→再检索

晚上代码：

```
```python
    from typing import TypedDict, Literal
    from langgraph.graph import StateGraph, END
```

```python
# 定义状态（工作流中流转的数据结构）
    class RAGState(TypedDict):
        query: str
        documents: list
        answer: str
        need_rewrite: bool
```

```python
# 定义节点（每个处理步骤）
    def retrieve(state: RAGState):
        docs = retriever.invoke(state["query"])
        return {"documents": docs}
```

```python
def check_quality(state: RAGState):
        # 检查检索质量：如果文档太短或太少，需要改写查询
        if len(state["documents"]) < 2 or all(len(d.page_content) < 100 for d in state["documents"]):
            return {"need_rewrite": True}
        return {"need_rewrite": False}
```

```python
def rewrite_query(state: RAGState):
        # 用 LLM 把用户查询改写成更精准的形式
        new_query = llm.invoke(f"把以下问题改写得更具体以便检索：{state['query']}")
        return {"query": new_query.content}
```

```python
def generate(state: RAGState):
        response = rag_chain.invoke({"input": state["query"]})
        return {"answer": response["answer"]}
```

```python
# 构建图
    workflow = StateGraph(RAGState)
```

```python
# 添加节点
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("check_quality", check_quality)
    workflow.add_node("rewrite_query", rewrite_query)
    workflow.add_node("generate", generate)
```

```python
# 添加边（连接节点）
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "check_quality")
```

```python
# 条件边：根据 need_rewrite 决定走哪条路
    workflow.add_conditional_edges(
        "check_quality",
        lambda s: "rewrite_query" if s["need_rewrite"] else "generate",
        {"rewrite_query": "rewrite_query", "generate": "generate"}
    )
    workflow.add_edge("rewrite_query", "retrieve")  # 改写后重新检索
    workflow.add_edge("generate", END)
```

app = workflow.compile()
result = app.invoke({"query": "怎么退？"})
```python
print(result["answer"])
    ```
```

这个工作流做的事：检索→检查质量→如果不好就改写查询→重新检索→生成
比单纯的"检索→生成"智能得多。这就是 Agent 的核心思想。

- [ ] 完成检查
- [ ] Reranker 重排序跑通
- [ ] LangGraph 状态图理解（State/Node/Edge）
### 第18周 · 星期五-六：RAG 优化评估 + 综合项目
---
### 星期五
RAG 评估
准备 10 个问答对（问题+标准答案），用 RAG 回答后，
用另一个 LLM 打分（1-5 分），评估检索质量。

### 星期六
综合项目
做一个"智能知识库问答系统"
- 上传你的 Obsidian 笔记作为知识库
- RAG + Reranker + 查询改写
- 前端用 Gradio 搭一个简单的 Web UI
- push GitHub

- [ ] 第18周完成检查
- [ ] 从零搭建 RAG 全流程
- [ ] LangGraph 工作流能独立设计
- [ ] RAG 有检索质量评估
### 第19周 · Agent 开发 + 多智能体协作
---
### 星期一-二
ReAct Agent 深度（手机+晚上）
手机摸鱼：
ReAct(Reasoning+Acting) = LLM 在思考和行动之间交替循环
Thought: "我需要先查天气"
Action: get_weather("北京")
Observation: "晴，25°C"
Thought: "还需要查空气质量"
Action: get_air_quality("北京")
Observation: "优"
Thought: "信息够了，可以回答了"
Final Answer: "北京今天晴..."

和单纯 Function Calling 的区别：
单次 FC：用户问→模型决定调1个工具→拿到结果→回答（一次往返）
ReAct：模型可以多轮调用工具、分析中间结果、调整计划（多次往返）

晚上：手写一个 ReAct 循环（不调 LangGraph），理解底层逻辑
```
```python
    def react_agent(user_query, max_iterations=5):
        messages = [HumanMessage(content=user_query)]
        for i in range(max_iterations):
            response = llm_with_tools.invoke(messages)
            messages.append(response)
            if not response.tool_calls:
                return response.content  # 没有工具调用，说明推理完成
            # 执行工具
            for tc in response.tool_calls:
                result = tool_map[tc["name"]].invoke(tc["args"])
                messages.append(ToolMessage(content=result, tool_call_id=tc["id"]))
        return "达到最大迭代次数"
    ```
```

### 星期三-四
多智能体协作
手机摸鱼：
单 Agent：一个人做所有事（检索+推理+生成）
多 Agent：多个"专家"各司其职，互相协作

常见多 Agent 模式：
- 研究员→写手→审稿（流水线）
- 辩论模式：两个 Agent 从正反方辩论，第三个 Agent 裁判
- 层级模式：Manager Agent 分配任务给 Worker Agents

晚上：用 LangGraph 实现"研究员→写手→审稿"三 Agent 协作
```
```python
    # 三个 Agent 各有自己的 prompt 和工具
    researcher = create_react_agent(llm, [search_tool])
    writer = create_react_agent(llm, [])
    reviewer = create_react_agent(llm, [])
```

```python
# LangGraph 编排三者
    workflow = StateGraph(TeamState)
    workflow.add_node("research", researcher_node)
    workflow.add_node("write", writer_node)
    workflow.add_node("review", reviewer_node)
    workflow.add_conditional_edges("review",
        lambda s: "write" if s["needs_revision"] else END)
    ```
```

### 星期五-六
综合项目 + 阶段四复盘
综合项目：做一个"自动化技术博客写作系统"
1. 研究员 Agent：搜索 GitHub trending + 技术博客，整理素材
2. 写手 Agent：基于素材写出初稿
3. 审稿 Agent：检查错误、优化表达
4. 用户可以反馈"再详细一点/简化"，触发重新写作

- [ ] 第19周完成检查
- [ ] ReAct 循环能手动实现
- [ ] 多 Agent 协作系统完整运行
- [ ] 综合项目 push GitHub
### 阶段五 · 大模型定制开发（第20-24周）


### 第20周 · Mini-GPT 构建 ★核心周★
---
### 手机摸鱼 · 贯穿全周
nanoGPT 源码精读
在 GitHub 手机客户端上打开 karpathy/nanoGPT/model.py（约 300 行）。
按以下顺序读（每天 30 分钟）：

星期一：看整体结构
打开 model.py，从上到下扫一遍，标记以下类：
- LayerNorm
- CausalSelfAttention
- MLP
- Block
- GPT
理解它们之间的调用关系：GPT → n×Block → CausalSelfAttention + MLP

星期二：逐个 Block 深入
MLP 做了什么？Linear→GELU→Linear（先扩展 4 倍再压缩回来）
Block 做了什么？x = x + attn(ln1(x)); x = x + mlp(ln2(x))
这就是 Pre-LN 风格（阶段三手写的是 Post-LN，对比着看）

星期三：Attention 的细节
Q,K,V 是怎么投影的？c_attn = Linear(d_model, 3*d_model)
为什么合在一个 Linear 里？一次矩阵乘法比三次快
causal mask 怎么构造？torch.tril（下三角矩阵），注册为 buffer

星期四：训练代码 train.py
- get_batch() 怎么采样数据？
- estimate_loss() 做了什么？
- 学习率调度：warmup + cosine decay

星期五：生成代码
model.generate() 的自回归过程：
输入 idx → 拿到 logits → 取最后一个位置的输出 → softmax→sample→拼接→循环

### 晚上电脑 · 星期一-三
手写 Mini-GPT
星期一：CausalSelfAttention
```
```python
    class CausalSelfAttention(nn.Module):
        def __init__(self, d_model, n_heads, block_size, dropout):
            super().__init__()
            # Q,K,V 三个投影合并为一个 Linear，效率更高
            self.c_attn = nn.Linear(d_model, 3 * d_model)
            self.c_proj = nn.Linear(d_model, d_model)  # 输出投影
            self.n_heads = n_heads
            self.d_k = d_model // n_heads
            # causal mask：上三角为0，下三角为1（注册为buffer不参与训练）
            self.register_buffer("mask",
                torch.tril(torch.ones(block_size, block_size))
                .view(1, 1, block_size, block_size))
```

```python
def forward(self, x):
            B, T, C = x.shape  # batch, seq_len, d_model
            qkv = self.c_attn(x)  # (B, T, 3*C)
            q, k, v = qkv.split(C, dim=2)  # 三个 (B, T, C)
            # 拆头：把 d_model 拆成 n_heads × d_k
            q = q.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
            k = k.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
            v = v.view(B, T, self.n_heads, self.d_k).transpose(1, 2)
            # Attention
            att = (q @ k.transpose(-2, -1)) / math.sqrt(self.d_k)
            att = att.masked_fill(self.mask[:,:,:T,:T] == 0, float('-inf'))
            att = F.softmax(att, dim=-1)
            att = self.dropout(att)
            # 合并多头
            y = att @ v
            y = y.transpose(1, 2).contiguous().view(B, T, C)
            return self.c_proj(y)
    ```
```

星期二：MLP + Block
```
```python
    class MLP(nn.Module):
        def __init__(self, d_model, dropout):
            super().__init__()
            self.c_fc = nn.Linear(d_model, 4 * d_model)   # 扩展
            self.gelu = nn.GELU()
            self.c_proj = nn.Linear(4 * d_model, d_model)  # 压缩
            self.dropout = nn.Dropout(dropout)
        def forward(self, x):
            return self.c_proj(self.gelu(self.c_fc(x)))
```

```python
class Block(nn.Module):
        def __init__(self, d_model, n_heads, block_size, dropout):
            super().__init__()
            self.ln_1 = nn.LayerNorm(d_model)
            self.attn = CausalSelfAttention(d_model, n_heads, block_size, dropout)
            self.ln_2 = nn.LayerNorm(d_model)
            self.mlp = MLP(d_model, dropout)
        def forward(self, x):
            # Pre-LN：先Norm再做Attention/MLP，再加回残差
            x = x + self.attn(self.ln_1(x))
            x = x + self.mlp(self.ln_2(x))
            return x
    ```
```

星期三：GPT 完整组装修
```
```python
    class GPT(nn.Module):
        def __init__(self, vocab_size, d_model, n_heads, n_layers, block_size, dropout):
            super().__init__()
            self.token_embedding = nn.Embedding(vocab_size, d_model)
            self.position_embedding = nn.Embedding(block_size, d_model)
            self.blocks = nn.Sequential(*[
                Block(d_model, n_heads, block_size, dropout) for _ in range(n_layers)
            ])
            self.ln_f = nn.LayerNorm(d_model)
            self.lm_head = nn.Linear(d_model, vocab_size)  # 输出词表维度
            self.block_size = block_size
```

```python
def forward(self, idx):
            B, T = idx.shape
            tok_emb = self.token_embedding(idx)  # (B,T,d_model)
            pos = torch.arange(0, T, device=idx.device)
            pos_emb = self.position_embedding(pos)  # (T,d_model)
            x = tok_emb + pos_emb
            x = self.blocks(x)
            x = self.ln_f(x)
            return self.lm_head(x)  # (B,T,vocab_size) 每个位置预测下一个token
```

```python
def generate(self, idx, max_new_tokens):
            """自回归生成：输入初始token，逐个预测下一个"""
            for _ in range(max_new_tokens):
                # 截断到 block_size
                idx_cond = idx[:, -self.block_size:]
                logits = self(idx_cond)
                logits_last = logits[:, -1, :]  # 只取最后一个位置
                probs = F.softmax(logits_last, dim=-1)
                idx_next = torch.multinomial(probs, num_samples=1)
                idx = torch.cat((idx, idx_next), dim=1)
            return idx
    ```
```

验证：用随机输入跑 forward，确认所有维度正确。

### 星期四-五
训练 Mini-GPT
星期四：数据准备
- 下载 Shakespeare 或中文维基小数据集
- 训练一个简单的 BPE Tokenizer（或用 karpathy/minbpe）
- 构建 DataLoader

星期五：训练循环
```
```python
    model = GPT(vocab_size=50257, d_model=256, n_heads=8, n_layers=6,
                block_size=256, dropout=0.1)
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
    for step in range(5000):
        x, y = get_batch('train')
        logits = model(x)
        loss = F.cross_entropy(logits.view(-1, vocab_size), y.view(-1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if step % 500 == 0:
            print(f"step {step}: loss {loss.item():.4f}")
    ```
```

> ⚠️ ️ GPU 需求：Shakespeare 数据集在 RTX 3090 上约 30 分钟完成 5000 步。
如果在 CPU 上跑，d_model 降到 128，n_layers 降到 4。

### 星期六
训练 + 生成
14:00-15:30 跑完整训练（盯着 loss 曲线下降）
15:30-17:00 用不同 temperature/top-p 生成文本，对比质量
17:00-17:30 复盘

- [ ] 第20周完成检查
- [ ] CausalSelfAttention 手写完成
- [ ] Mini-GPT forward 跑通，维度全部核对
- [ ] 训练 loss 正常下降（至少降到 2.0 以下）
- [ ] generate() 能生成连贯文本
### 第21-22周 · 微调实战（LoRA + QLoRA）
---
### 第21周
Mini-GPT 完整训练 + 调参
星期一-三：数据清洗 + tokenize pipeline
星期四-五：调参实验（lr × batch_size × n_layers）
每次只变一个参数，记录 loss 曲线和最终 perplexity

星期六：最佳模型保存 + 生成评测

### 第22周
LoRA / QLoRA 微调
手机摸鱼 · 星期一-二：
LoRA 核心思想——低秩分解
预训练权重矩阵 W ∈ R^(d×k) 在微调时的变化 ΔW 是"低秩"的：
ΔW = B × A，其中 B∈R^(d×r)，A∈R^(r×k)，r << min(d,k)

为什么有效？预训练模型已经学会了"语言"，微调只需要在
一个低维子空间中调整参数即可。r=8 时，参数量只有原来的 1/500。

对哪些矩阵加 LoRA？通常只对 Attention 的 Q 和 V 投影矩阵加。
因为 Attention 是决定"关注什么"的核心机制，微调最需要调整它。

晚上 · 星期二：
```
```python
    from peft import LoraConfig, get_peft_model, TaskType
    from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
```

```python
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B")
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=8,                # 秩：越大表示越"灵活"，但参数多
        lora_alpha=32,      # 缩放因子（实际学习率按 alpha/r 缩放）
        target_modules=["q_proj", "v_proj"],  # 只对 Q/V 加 LoRA
        lora_dropout=0.1
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    # 输出：trainable params: 2.1M || all params: 495M || trainable%: 0.42%
    # 只训练 0.42% 的参数！
    ```
```

星期三：构造 SFT 数据集（指令-回答对）
```
```json
    {"instruction": "写一个Python冒泡排序", "output": "def bubble_sort...", "input": ""}
    ```
```

星期四：QLoRA（4-bit 量化 + LoRA，在 8GB 显存上微调 7B 模型！）
```
```python
    from transformers import BitsAndBytesConfig
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",       # NF4 量化（比普通4bit更精确）
        bnb_4bit_compute_dtype=torch.bfloat16,  # 计算时用 bf16
        bnb_4bit_use_double_quant=True   # 双重量化（再省 0.4 bit/参数）
    )
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2-0.5B", quantization_config=bnb_config
    )
    model = get_peft_model(model, lora_config)
    ```
```

星期五-六：r=4/8/16/32 对比实验
同一个数据集、同一个训练配置，只改变 r 值。
对比：可训练参数量、训练时间、最终 loss、生成质量。
结论：通常 r=8 就是性价比最优的甜点区。

- [ ] 第21-22周完成检查
- [ ] LoRA 微调成功，可训练参数 < 1%
- [ ] QLoRA 成功（4bit量化+LoRA）
- [ ] r值对比实验有结论
### 第23-24周 · DPO + 量化 + vLLM 部署
---
### 第23周
DPO 对齐训练
手机摸鱼：
SFT（监督微调）后模型知道"怎么回答"，但不知道"什么回答好"。
DPO 教模型区分"好回答"和"坏回答"。

DPO 数据格式：每条包含 prompt + chosen（好答案）+ rejected（坏答案）
DPO 损失函数直觉：让 chosen 的概率上升，rejected 的概率下降。

晚上：
```
```python
    from trl import DPOTrainer
    dpo_trainer = DPOTrainer(
        model=model, ref_model=ref_model,
        beta=0.1,  # DPO 温度：越大越保守
        train_dataset=dpo_dataset,
        tokenizer=tokenizer,
        args=TrainingArguments(output_dir="./dpo", per_device_train_batch_size=2)
    )
    dpo_trainer.train()
    ```
```

对比：DPO 前和 DPO 后的模型对同一问题的回答差异。

量化实验：
```
```python
    # 对比原模型/8bit/4bit的速度和显存
    for quant in ["fp32", "8bit", "4bit"]:
        model = load_model_with_quant(quant)
        speed, memory = benchmark(model)
        print(f"{quant}: {speed:.1f} tok/s, {memory:.2f} GB")
    ```
```

### 第24周
vLLM 部署 + 吞吐压测 + 最终项目
vLLM 的核心创新 PagedAttention：
传统方式为每个请求分配连续显存存 KV Cache → 碎片化，利用率低
PagedAttention 像操作系统的分页一样，把 KV Cache 分成小块(block)管理
→ 显存利用率从 30% 提升到 90%+

部署 + 压测：
```
```bash
    python -m vllm.entrypoints.openai.api_server --model ./my-model --port 8000
    ```
    ```python
    # 压测脚本：100 并发请求，测 P50/P99 延迟和吞吐
    async def benchmark(url, prompt, n=100, concurrency=10):
        ...
        print(f"吞吐: {throughput:.1f} req/s, P99: {p99:.3f}s")
    ```
```

Docker 部署 + docker-compose.yml + 最终 README 补全
模型 push 到 HuggingFace（写 Model Card：描述训练数据/参数/评估指标）

- [ ] 阶段五完成检查
- [ ] Mini-GPT 训练完 + 代码 push
- [ ] LoRA/QLoRA 微调 + r值对比
- [ ] DPO 对齐训练成功
- [ ] vLLM 吞吐压测完成
- [ ] HuggingFace 发布模型
### 阶段六 · 算法进阶（第25周）


本周以"理解概念+Run Demo"为主，不要求从零训练。

星期一-二：CLIP
核心思想：4 亿图文对做对比学习
同一个图文对的 embedding 距离近（正例），不同的距离远（负例）
结果：模型学会了通用的图文理解能力（zero-shot 图像分类）

Demo：用 OpenAI CLIP 或 Chinese-CLIP 做图文检索

星期三-四：多模态大模型
Qwen-VL / GPT-4V API 调用
理解 BLIP-2 Q-Former：把图像特征"翻译"成 LLM 能理解的 token

星期五-六：Stable Diffusion 体验 + MoE 概念
ComfyUI 搭建文生图工作流
MoE（混合专家）：每个 token 只走 2 个"专家"子网络，省算力

- [ ] 阶段六完成检查
- [ ] CLIP 图文检索 Demo
- [ ] 多模态模型 API 调通
- [ ] 对 MoE 有基本概念
### 阶段七 · 面试专题（第26周 + 全程）


-  面试不是最后一周才准备 ──
前面 25 周每周末花 20 分钟整理"电梯演讲"：
每个核心概念准备 1 分钟的口头解释。

### 第26周集中冲刺
ML/DL 面试题：
- [ ] 过拟合/欠拟合：原因+解决方法（L1/L2/Dropout/早停/数据增强）
- [ ] BN vs LN：各自适用场景、为什么 Transformer 用 LN 不用 BN
- [ ] 激活函数演进：Sigmoid→ReLU→GELU→SiLU/SwiGLU 的动机

Transformer 专题 ★面试必考★：
- [ ] Attention 公式默写 + QKV 维度推导
- [ ] Multi-Head 计算流程（拆分→各自Attention→拼接→投影）
- [ ] Pre-LN vs Post-LN 的区别和各自优缺点
- [ ] BERT vs GPT vs T5 三架构对比

大模型专题：
- [ ] GPT 训练三阶段：Pre-training → SFT → RLHF/DPO
- [ ] LoRA 原理：为什么低秩分解有效？r 参数怎么选？
- [ ] KV Cache：为什么能加速？空间复杂度 O(batch×layers×heads×seq×d_head)
- [ ] Flash Attention：分块计算 + IO-Awareness（不展开推导，但要能讲核心思想）
- [ ] vLLM PagedAttention：类比 OS 分页管理 KV Cache

LeetCode Hot 100（手机刷题，电脑写代码）：
重点：数组/链表/栈/队列/哈希/二叉树/DP/DFS/BFS

GitHub 项目总结：
每个项目 3 句话亮点 + 1 个踩过的坑
简历更新，至少准备 3 个"可以深聊"的项目

- [ ] 阶段七完成检查
- [ ] LeetCode Hot 100 刷完
- [ ] Transformer 架构图能默写 + 完整解释
- [ ] 每个 GitHub 项目有完整 README
- [ ] 简历完成，有 3+ 可深聊项目
### END · 全部阶段完毕


```