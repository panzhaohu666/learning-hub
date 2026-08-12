# Python 全栈工程师完整学习计划

> **路线**：后端 API → 全栈 Web → DevOps → 微服务
> **目标岗位**：Python 全栈工程师 / 后端开发工程师
> **时间**：全职 4-6 个月 / 在职 8-12 个月（每天 3-4h）
> **核心思路**：学 60% 就开始做项目，项目驱动学习，不追求"学完再动手"

---

## 📋 总览

```
阶段1: Python基础       ████░░░░░░░░░░░░░░░░  3周
阶段2: Python进阶+网络   ██████░░░░░░░░░░░░░░  3周
阶段3: 数据库            ██████████░░░░░░░░░░  3周
阶段4: 后端框架          ██████████████░░░░░░  4周
阶段5: 前端框架          ██████████████████░░  5周
阶段6: DevOps           ████████████████████  3周
阶段7: 微服务            ████████████████████  3周
阶段8: 全栈项目实战       ████████████████████  4周
阶段9: 面试准备           ████████████████████  持续
```

**每个阶段学习完成后做一个小项目，不要等到最后。**

> 🔖 **图例说明**：标记为 `🔷 选学` 的内容可按精力和目标取舍（如目标是中小公司可跳过 K8s、gRPC；目标大厂则建议全学）。

---

## 🟢 阶段 1：Python 语言基础（3 周）

> **目标**：能用 Python 独立写命令行工具、处理数据、理解面向对象
> **检验标准**：LeetCode 简单题 30+ 道独立完成

### 核心教程

以 [Python-100-Days Day01-20](https://github.com/jackfrued/Python-100-Days) 为主线：

| 周数 | 内容 | 天数 | 重点 | 练习 |
|------|------|------|------|------|
| 第1周 | Day01-07 | 基础语法、变量、运算符、分支、循环 | 循环是核心 | LeetCode 5题/天 |
| 第2周 | Day08-13 | 列表、元组、字符串、集合、字典 | **列表和字典是重中之重** | LeetCode 5题/天 |
| 第3周 | Day14-20 | 函数、模块、面向对象（OOP） | **装饰器、OOP 必吃透** | 实战：命令行 TODO 工具 |

### 补充资源

| 资源 | 用途 | 何时看 |
|------|------|--------|
| [Python 官方教程](https://docs.python.org/zh-cn/3/tutorial/) | 查漏补缺 | 遇到不懂的回来翻 |
| [《流畅的 Python》](https://book.douban.com/subject/27028517/) | 进阶理解 | 阶段3之后翻，不要一开始看 |
| LeetCode | 算法手感 | 每天做，保持到面试 |

### 第3周实战项目：命令行 TODO 工具

```
功能要求：
- 添加/删除/修改/查看任务
- 数据持久化到 JSON 文件
- 支持命令行参数（argparse）
- 面向对象设计（Task 类 + TaskManager 类）
- 有 README.md 和注释

技术点：
- 文件读写（Day21）
- JSON 序列化（Day22）
- OOP（Day18-20）
- argparse 标准库
```

### 📅 第1-3周 每日安排

> 以下安排可按实际节奏调整，核心原则：**每天写代码的时间 > 看教程的时间**。

**第1周（基础语法）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Python-100-Days Day01：变量、运算符、数据类型 | LeetCode 2 题（两数之和、回文数） | 2h |
| 周二 | Day02-03：分支结构（if/elif/else） | LeetCode 2 题 + 写一个成绩评级程序 | 2.5h |
| 周三 | Day04-05：循环结构（for/while） | LeetCode 2 题 + 打印九九乘法表/斐波那契 | 2.5h |
| 周四 | Day06：函数定义、参数、返回值 | LeetCode 2 题 + 把之前的代码重构成函数 | 2.5h |
| 周五 | Day07：字符串常用操作 | LeetCode 2 题 + 写一个密码强度检测器 | 2h |
| 周六 | 复习 + 综合练习 | LeetCode 5 题 + 写一个猜数字游戏（带计分） | 3h |
| 周日 | 休息或查漏补缺 | 把你觉得模糊的概念用代码验证一遍 | 1h |

**第2周（数据结构）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day08-09：列表（增删改查、切片、推导式） | LeetCode 3 题（数组类） | 2.5h |
| 周二 | Day10：元组、集合 | LeetCode 2 题 + 用集合做去重/交集/差集 | 2h |
| 周三 | Day11-12：字典（遍历、嵌套、推导式） | LeetCode 3 题（哈希表类） | 2.5h |
| 周四 | Day13：字符串深入（格式化、编码） | LeetCode 2 题 + 写一个日志解析器 | 2.5h |
| 周五 | 综合：列表+字典嵌套处理 | 实战：解析一个 JSON 文件（用 Python 内置 json 库） | 2h |
| 周六 | 复习 + LeetCode 专项 | LeetCode 5 题（数组+哈希表） | 3h |
| 周日 | 休息 | — | — |

**第3周（OOP + 实战）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day14-15：类、对象、`__init__`、实例方法 | 写一个 BankAccount 类（存款/取款/查余额） | 2.5h |
| 周二 | Day16-17：继承、多态、`@property` | 写一个 Animal → Dog/Cat 继承体系 | 2.5h |
| 周三 | Day18：模块与包、`__name__` | 把之前的代码拆成多个 .py 文件，学会 import | 2h |
| 周四 | Day19-20：文件读写、异常处理 | 读取一个大文件，统计词频 | 2.5h |
| 周五 | 命令行参数：argparse 深入 | 写一个带 `--help`、`--verbose` 的 CLI 程序 | 2h |
| 周六 | **开始 CLI TODO 项目**（见下方详细规格） | 项目 Day 1：设计类结构 + 实现基础功能 | 4h |
| 周日 | **CLI TODO 项目 Day 2** | 完成全功能 + README + 推到 GitHub | 4h |

### 🔧 阶段 1 实战项目：命令行 TODO 工具（详细规格）

```
项目名称：py-todo
目标：一个能在终端使用的完整 TODO 管理工具
时间：周末 2 天（约 8h）

═══════════════════════════════════════
第一步：命令行接口设计
═══════════════════════════════════════

$ python todo.py add "买牛奶" --priority high --due 2025-12-20
  ✓ 已添加任务 #1: 买牛奶 [高优先级] 截止 2025-12-20

$ python todo.py list
  #1 [ ] 买牛奶          高优先级  截止 2025-12-20  创建: 2025-12-15
  #2 [✓] 写作业          中优先级  无截止日期        创建: 2025-12-14
  #3 [ ] 运动30分钟      低优先级  截止 2025-12-16  创建: 2025-12-15

$ python todo.py list --filter pending    # 只看未完成
$ python todo.py list --filter done       # 只看已完成
$ python todo.py list --priority high     # 只看高优先级
$ python todo.py list --sort due          # 按截止日期排序

$ python todo.py done 1     # 标记任务1为完成
$ python todo.py delete 3   # 删除任务3
$ python todo.py edit 2 --content "写数学作业" --priority high
$ python todo.py search "牛奶"   # 模糊搜索任务内容
$ python todo.py stats           # 统计：总计5个，已完成2个，完成率40%

═══════════════════════════════════════
第二步：面向对象设计
═══════════════════════════════════════

文件结构：
todo.py                 # 程序入口（argparse 解析）
├── models.py           # Task 类（数据模型）
├── storage.py          # TaskStorage 类（JSON 文件的读写）
└── manager.py          # TaskManager 类（业务逻辑：添加/删除/搜索/统计）

class Task:
    def __init__(self, id, content, priority="medium", due=None, 
                 created=None, done=False):
        self.id = id
        self.content = content
        self.priority = priority          # high/medium/low
        self.due = due                    # 截止日期（可选）
        self.created = created or datetime.now().strftime("%Y-%m-%d")
        self.done = done
    
    def to_dict(self) -> dict:
        """转为字典，用于 JSON 序列化"""
    
    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """从字典创建 Task 对象"""

class TaskStorage:
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
    
    def load(self) -> list[Task]:
        """从 JSON 文件加载所有任务，文件不存在则返回空列表"""
    
    def save(self, tasks: list[Task]) -> None:
        """将所有任务保存到 JSON 文件"""

class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load()
        self._next_id = self._calculate_next_id()
    
    def add(self, content, priority="medium", due=None) -> Task:
    def delete(self, task_id) -> bool:
    def mark_done(self, task_id) -> bool:
    def edit(self, task_id, **kwargs) -> bool:
    def list(self, filter=None, sort=None, priority=None) -> list[Task]:
    def search(self, keyword) -> list[Task]:
    def stats(self) -> dict:
    def _save(self):
        """每次修改后自动保存到文件"""

═══════════════════════════════════════
第三步：额外加分任务（不强制）
═══════════════════════════════════════
□ 彩色输出：高优先级红色、完成的任务绿色打勾（用 colorama 库）
□ タスク分组：支持 --tag "工作" --tag "个人" 的分类标签
□ 数据导出：python todo.py export --format csv
□ 定时提醒：python todo.py remind（列出今天截止的任务）
□ 单元测试：用 unittest 写至少 5 个测试用例
```

### 🐛 阶段 1 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **可变默认参数** | `def add_item(item, lst=[])` 多次调用共享同一个列表 | Python 默认参数只在函数定义时求值一次 | 用 `lst=None`，函数内 `if lst is None: lst = []` |
| **浅拷贝陷阱** | 修改 `list2` 居然影响了 `list1` | `list2 = list1` 是引用，不是拷贝 | 用 `list1.copy()` 或 `list(list1)` 或 `copy.deepcopy()` |
| **循环中修改列表** | `for item in lst: lst.remove(item)` 跳过元素 | 迭代时修改列表导致索引错位 | 用列表推导式创建新列表，或倒序遍历 |
| **文件没关闭** | 写入的内容没保存到文件 | 忘记 `f.close()` 或没用 context manager | 始终用 `with open(...) as f:` |
| **`__init__` vs `__new__`** | 搞不清构造时谁先调用 | `__new__` 创建实例，`__init__` 初始化它 | `__new__` 先于 `__init__` 执行，单例模式才需要覆写 `__new__` |
| **`is` vs `==`** | 判断相等结果不符合预期 | `is` 判身份（同一对象），`==` 判值相等 | 除了与 `None` 比较用 `is`，其余用 `==` |
| **UnicodeEncodeError** | 文件写入报编码错误 | Windows 默认 GBK 编码 | `open(file, 'w', encoding='utf-8')` 明确指定编码 |

### 📋 阶段 1 完成检查清单 + 自测问题

```
□ 语法基础
  □ 能闭卷写出 for/while 循环的各种变体（break/continue/else）
  □ 能解释 Python 中一切皆对象是什么意思
  □ 知道 list/dict/tuple/set 的区别和各自适用场景
  □ 能用列表推导式替代简单的 for 循环

□ 函数
  □ 能写带默认参数、*args、**kwargs 的函数
  □ 理解 LEGB 变量作用域规则（Local → Enclosing → Global → Built-in）
  □ 能写一个返回函数的函数（闭包概念）

□ 面向对象
  □ 能自写 `__init__`、`__str__`、`__repr__` 方法
  □ 能解释继承和多态，能举出自己的例子
  □ 理解 `self` 是什么（不是关键字，是约定）
  □ 知道 `@staticmethod` 和 `@classmethod` 的区别

□ 实战
  □ [ ] CLI TODO 工具完整可用，代码 > 300 行
  □ [ ] LeetCode 简单题独立完成 30+ 道
  □ [ ] 代码有适当注释，README 能让人看懂怎么用

自测问题（尝试不查资料回答）：
1. Python 中 mutable 和 immutable 类型各举 3 个例子
2. 装饰器在什么时候执行？被装饰函数定义时还是调用时？
3. 怎么在 for 循环中获取索引？（至少 2 种方法）
4. `try/except/else/finally` 的执行顺序是什么？
```

### 🎤 阶段 1 面试关联

> Python 基础是面试第一关，挂在这上面基本没下文了。

**高频面试题：**
- "Python 是解释型还是编译型？" → 答：生成字节码（.pyc），由 PVM 解释执行，是混合型
- "深拷贝和浅拷贝的区别？什么场景用哪个？"
- "装饰器的原理是什么？写一个计时装饰器"
- "Python 的垃圾回收机制？引用计数 + 标记清除 + 分代回收"
- "GIL 是什么？多线程在 Python 中有什么用？"（阶段2深入）

**回答技巧：** 每个问题都准备两段回答——一句话概括 + 一个具体代码例子。面试官不满足于背定义，他要看你"真用过"。

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [Python 官方教程前 6 章](https://docs.python.org/zh-cn/3/tutorial/) | 用手机浏览，记下有疑问的点 | 每天 15min |
| Python-100-Days Day01-20 的 README | 只看概念解释，跳过代码 | 每天 10min |
| LeetCode 题解区的"精选题解" | 看别人怎么用简洁语法解题 | 每天 2-3 篇 |
| [Python 之禅](https://peps.python.org/pep-0020/)（`import this`）| 每天读一遍，慢慢理解每句话 | 2min |
| [Real Python 博客](https://realpython.com/) 的基础文章 | 英文阅读 + 技术学习双重收益 | 每天 1 篇 |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| LeetCode 刷题 | 每天至少 3 题，从「简单」开始，不看答案写 | 每天 |
| Python 交互式环境实验 | 不确定的行为直接在 `python` REPL 里试（比翻文档快） | 随时 |
| 重构旧代码 | 把第1周的练习用函数重写，把第2周的用类重写 | 周末 |
| 写一个自己的工具 | 比如重命名工具、文件整理脚本——需求来自你自己的生活 | 1-2 个 |
| 看报错学 Python | 遇到报错不要直接搜答案，先自己读 Traceback 最后一行 | 每次报错 |

---

## 🟡 阶段 2：Python 进阶 + 计算机网络基础（3 周）

> **目标**：理解 HTTP 协议、能调 API、能处理文件、懂 Linux 基本操作
> **检验标准**：能独立请求第三方 API 并处理返回数据

### 核心教程

Python-100-Days Day21-35 + 额外补课：

| 周数 | 内容 | 来源 |
|------|------|------|
| 第4周 | 文件读写、JSON、CSV、异常处理 | Day21-23 |
| 第4周 | **HTTP 协议补课**（GET/POST/PUT/DELETE、状态码、请求头、Cookie） | [MDN HTTP 教程](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) |
| 第5周 | Excel/Word/PDF/图像处理、发邮件、正则表达式 | Day24-30 |
| 第5周 | Linux 基础 + Shell | Day34-35 |
| 第6周 | Python 进阶：迭代器、生成器、并发基础 | Day31 |

### ⚠️ 额外必补：计算机网络基础（自学，教程里没有）

| 主题 | 资源 | 时间 | 重要程度 |
|------|------|------|---------|
| HTTP 协议 | [MDN HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) | 2天 | ⭐⭐⭐⭐⭐ |
| TCP/IP 三次握手四次挥手、拥塞控制 | [《图解 TCP/IP》](https://book.douban.com/subject/24737674/) 前 5 章 | 3天 | ⭐⭐⭐⭐ |
| HTTP/2、HTTPS/TLS 原理 | 博客 + [《图解 HTTP》](https://book.douban.com/subject/25863515/) | 1天 | ⭐⭐⭐ |
| RESTful API 设计规范 | [阮一峰 RESTful API 指南](https://www.ruanyifeng.com/blog/2014/05/restful_api.html) | 1天 | ⭐⭐⭐⭐⭐ |
| JSON/XML 数据格式 | 看文档 + 动手实践 | 1天 | ⭐⭐⭐⭐ |
| DNS 解析原理 | 任意一篇博客即可 | 1天 | ⭐⭐⭐ |
| WebSocket 基础概念 🔷选学 | 了解即可，阶段7深入 | 0.5天 | ⭐⭐ |

### 第6周实战项目：天气查询 CLI + API

```
功能要求：
- 调用公开天气 API（如 OpenWeatherMap / 和风天气）
- 支持城市搜索
- 显示当前天气 + 未来3天预报
- 结果保存为 CSV
- 用 requests + JSON 处理
- 异常处理完善（网络错误、城市不存在等）
```

### 📅 第4-6周 每日安排

**第4周（文件处理 + HTTP 协议）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day21：文件打开模式（r/w/a/r+/rb）| 写一个日志文件轮转脚本 | 2.5h |
| 周二 | Day22：JSON 序列化/反序列化，CSV 读写 | 写一个 JSON ↔ CSV 转换器 | 2.5h |
| 周三 | Day23：异常处理（try/except/finally/自定义异常）| 改造第3周的 TODO 工具，加入完善的异常处理 | 2h |
| 周四 | **HTTP 协议补课 Day 1**：URL 结构、HTTP 请求方法、状态码 | 用 `curl -v` 发请求，逐行看响应头 | 2.5h |
| 周五 | **HTTP 协议补课 Day 2**：请求头/响应头、Cookie/Session | 用 Chrome DevTools Network 面板分析任意网站 | 2h |
| 周六 | **HTTP 实操 Day 1**：用 `requests` 库调用公开 API | 调用 GitHub API 查仓库信息，解析 JSON 返回 | 3h |
| 周日 | **HTTP 实操 Day 2**：处理分页、限流、超时重试 | 调用一个有分页的 API，爬取全部数据 | 2h |

**第5周（办公自动化 + Linux 基础）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day24-25：Excel 读写（openpyxl）| 从 Excel 读数据 → 处理后 → 写回新 Excel | 2.5h |
| 周二 | Day26-27：Word/PDF 处理 | 自动生成简历 PDF | 2.5h |
| 周三 | Day28-29：发邮件（SMTP）、正则表达式 | 写一个监控脚本，异常时发邮件告警 | 2.5h |
| 周四 | Day30：图像处理（Pillow 基础）| 批量压缩/加水印 | 2h |
| 周五 | Day34-35：Linux 基础命令（ls/cd/mv/chmod/ps/grep）| 在 WSL/虚拟机里完成 20 个常用命令练习 | 2.5h |
| 周六 | TCP/IP 补课 Day 1：OSI 模型、TCP 三次握手/四次挥手 | 用 Wireshark 抓包看一次 HTTP 请求的完整 TCP 流程 | 3h |
| 周日 | TCP/IP 补课 Day 2：UDP、拥塞控制、可靠传输机制 | 画一张 TCP 状态转移图 | 2h |

**第6周（并发基础 + 实战项目）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day31：迭代器、生成器、`yield` 关键字 | 写一个生成器版本的斐波那契数列 | 2.5h |
| 周二 | 并发基础：`threading` 模块、GIL 的理解 | 写一个多线程下载器，观察 GIL 对 CPU 密集型的影响 | 2.5h |
| 周三 | 并发基础：`asyncio` 入门（async/await）| 对比多线程和协程下载同一批 URL 的速度 | 2.5h |
| 周四 | RESTful API 设计规范 | 设计一个博客系统的 API 接口（只设计不实现） | 2h |
| 周五 | DNS 原理 + HTTPS/TLS 握手 | 用 `dig` + `openssl s_client` 分析域名解析和证书 | 2h |
| 周六 | **天气查询项目 Day 1** | 实现核心功能（API 调用+解析+展示） | 4h |
| 周日 | **天气查询项目 Day 2** | 完善异常处理+CSV 导出+README+推 GitHub | 4h |

### 🔍 HTTP 调试动手实验（第4周重点）

> 这些实验是理解 HTTP 最快的方式——别光看，一个一个敲。

**实验 1：用 `curl -v` 观察完整 HTTP 交互**

```bash
# 看一次完整的 HTTP 请求-响应过程
curl -v https://api.github.com/users/octocat

# 重点关注输出中的这几行：
# > GET /users/octocat HTTP/1.1       ← 请求行
# > Host: api.github.com               ← 请求头
# > User-Agent: curl/8.x.x
# < HTTP/1.1 200 OK                    ← 响应状态行
# < Content-Type: application/json     ← 响应头
# < ...                                ← 空行分隔，然后是响应体
```

**实验 2：用 `requests` 模拟浏览器行为**

```python
import requests

# 基础 GET
r = requests.get("https://httpbin.org/get", params={"key": "value"})
print(r.status_code, r.json())

# POST JSON 数据
r = requests.post("https://httpbin.org/post", 
                   json={"name": "张三", "age": 25})
print(r.json())

# 带自定义 Header
r = requests.get("https://httpbin.org/headers",
                  headers={"X-Custom-Header": "hello"})

# 处理超时和异常
try:
    r = requests.get("https://httpbin.org/delay/5", timeout=2)
except requests.exceptions.Timeout:
    print("请求超时！")
except requests.exceptions.ConnectionError:
    print("网络不通！")
```

**实验 3：用 Chrome DevTools 分析真实网站**

```
打开任意网站 → F12 → Network 标签 → 刷新页面

逐个点击请求，观察：
1. Request Headers：哪些头是浏览器自动加的？
2. Response Headers：Set-Cookie 怎么工作的？
3. Timing：DNS Lookup → TCP连接 → TLS握手 → 发送 → 等待 → 下载
   每个阶段花了多少毫秒？
4. 找一找：哪些请求返回了 301/302？哪些是 304 Not Modified？
```

**实验 4：用 Python 实现一个简单的 HTTP 客户端（socket 直连）**

```python
import socket

# 用 socket 直接发 HTTP 请求（理解底层）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("httpbin.org", 80))
request = (
    "GET /get?name=test HTTP/1.1\r\n"
    "Host: httpbin.org\r\n"
    "Connection: close\r\n"
    "\r\n"
)
sock.send(request.encode())
response = b""
while True:
    chunk = sock.recv(4096)
    if not chunk:
        break
    response += chunk
sock.close()

# 手动解析响应
header_part, _, body = response.partition(b"\r\n\r\n")
print("=== 响应头 ===")
print(header_part.decode())
print("=== 响应体 ===")
print(body.decode())
```

### 🐛 阶段 2 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **requests 超时没设** | 程序卡死不动 | `requests.get()` 默认永不超时 | **永远传 `timeout=` 参数**，生产代码不加 timeout 是事故隐患 |
| **编码问题：response.text 乱码** | 中文全是乱码 | `response.encoding` 自动检测不准 | 先 `response.encoding = 'utf-8'` 或直接用 `response.content.decode('utf-8')` |
| **大文件下载内存爆了** | 下载 500MB 文件程序报 MemoryError | `response.content` 一次性读入内存 | 用 `response.iter_content(chunk_size=8192)` 流式写入文件 |
| **JSON 解析报错** | `json.loads()` 报 JSONDecodeError | API 返回的不是合法 JSON（可能 HTML 错误页） | 先检查 `response.status_code`，确认是 200 再解析，加 try/except |
| **相对路径 vs 绝对路径** | `open("data/file.txt")` 报 FileNotFoundError | 当前工作目录不是你预期的 | 用 `os.path.join(os.path.dirname(__file__), "data/file.txt")` 或 `pathlib.Path(__file__).parent / "data/file.txt"` |
| **`yield` 理解偏差** | 以为生成器可以多次迭代 | 生成器只能遍历一次，耗尽后为空 | 需要多次遍历时用 `list(gen)` 转为列表，或重新创建生成器 |
| **GIL 的误解** | "Python 多线程没用" — 不完全对 | IO 密集型（网络请求/文件读写）GIL 自动释放，多线程有效 | CPU 密集型用多进程（`multiprocessing`），IO 密集型用多线程/协程 |

### 📋 阶段 2 完成检查清单 + 自测问题

```
□ 文件与数据处理
  □ 能正确处理文件路径（pathlib 优先于 os.path）
  □ 能用 json/csv 模块做数据序列化和反序列化
  □ 能用 with 语句管理资源，理解上下文管理器协议

□ HTTP 协议
  □ 能从 URL 输入到页面显示完整描述整个过程（DNS→TCP→TLS→HTTP→渲染）
  □ 能口述 GET/POST/PUT/DELETE/PATCH 的语义区别
  □ 能解释 200/301/302/400/401/403/404/500 各状态码的含义
  □ 能说清 Cookie 和 Session 的区别，知道为什么需要 Token

□ 网络基础
  □ 能画出 TCP 三次握手和四次挥手的时序图
  □ 知道 TCP 和 UDP 的区别（可靠 vs 快速、面向连接 vs 无连接）
  □ 能解释什么是 DNS 解析，递归查询和迭代查询的区别

□ Python 进阶
  □ 能写一个生成器函数并用 for 循环消费它
  □ 理解 yield 和 return 的区别
  □ 知道基本异常处理语法和自定义异常类

□ 实战
  □ [ ] 天气查询 CLI 完整可用
  □ [ ] 代码中有完善的异常处理（网络错误、API 限流、城市不存在等）
  □ [ ] 能独立对接 3 个不同的第三方 API

自测问题：
1. 浏览器输入 URL 后发生了什么？（试着讲满 2 分钟）
2. requests.get(url, timeout=5) 不传 timeout 有什么后果？
3. 生成器（Generator）和列表（List）在处理大文件时哪个更好？为什么？
4. TCP 为什么要三次握手而不是两次？
```

### 🎤 阶段 2 面试关联

> 网络基础是后端面试的"隐形门槛"——前端面试问得少，后端面试几乎必问。

**高频面试题：**
- "从输入 URL 到页面显示，发生了什么？" — 经典开放题，考察知识广度。答案要分层：DNS → TCP → TLS → HTTP → 服务器处理 → 浏览器渲染
- "GET 和 POST 的区别？" — 表面简单，深坑：语义、幂等性、参数位置、缓存、安全性
- "HTTP 和 HTTPS 的区别？TLS 握手过程？"
- "Cookie、Session、Token（JWT）的区别和使用场景？"
- "TCP 和 UDP 的区别？为什么视频通话用 UDP 而不是 TCP？"

**回答框架**：先一句话结论 → 展开原理 → 联系实际场景。比如："GET 和 POST 本质区别是语义——GET 用于获取资源，是幂等的；POST 用于创建资源，不是幂等的。在实际中，GET 参数在 URL 中所以有长度限制且会被浏览器缓存..."

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [MDN HTTP 概览](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Overview) | HTTP 协议全貌，手机看纯文字部分 | 30min |
| [阮一峰 RESTful API 指南](https://www.ruanyifeng.com/blog/2014/05/restful_api.html) | REST 设计规范，短小精悍 | 15min |
| 《图解 HTTP》1-6 章 | 图解形式，手机上翻一遍很快 | 每天 15min |
| [HTTP 状态码速查](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status) | 没事就翻，混个眼熟 | 碎片时间 |
| [Cloudflare 学习中心](https://www.cloudflare.com/zh-cn/learning/) | DNS/CDN/TLS 通俗解释 | 每天 1 篇 |
| Python-100-Days Day21-35 的 README | 只看概念解释，跳过代码 | 每天 10min |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| `curl -v` 调试 | 遇到任何 API 问题，先用 curl 发请求看原始响应 | 每次调试 |
| 写 API 调用脚本 | 从 GitHub、天气、翻译等公开 API 任选，每天调一个不同的 | 每天 1 个 |
| Wireshark 抓包 | 抓一次浏览器访问网页的完整流程，过滤 http/tls/dns | 至少 2 次 |
| 写文件处理工具 | 自动整理下载文件夹、批量重命名图片、生成 Excel 报表 | 1-2 个 |
| 手写 HTTP 状态机 | 用 socket 实现一个能解析 HTTP 响应的简单客户端 | 1 次 |

---

## 🟠 阶段 3：数据库（3 周）

> **目标**：能手写复杂 SQL、理解索引原理、能用 Python 操作数据库
> **检验标准**：LeetCode SQL 题 50+，能手写多表 JOIN + 子查询 + 窗口函数

### 核心教程

Python-100-Days Day36-45：

| 周数 | 内容 | 天数 | 重点 |
|------|------|------|------|
| 第7周 | MySQL 安装、DDL 建表、DML 增删改 | Day36-38 | 表设计（字段类型、约束） |
| 第7周 | DQL 查询：SELECT/JOIN/子查询/聚合/窗口函数 | Day39 | **面试核心，每天刷 SQL 题** |
| 第8周 | DCL 权限、索引（原理/类型/EXPLAIN） | Day40, Day43 | **索引是面试必问，必吃透** |
| 第8周 | Python 操作 MySQL（pymysql / SQLAlchemy） | Day44 | 写 CRUD 脚本 |
| 第9周 | 视图/函数/存储过程/Redis 入门 | Day41-42 + 补 | 了解即可 |

### 额外必补：Redis

| 主题 | 资源 | 时间 |
|------|------|------|
| Redis 基础（string/hash/list/set/zset） | [Redis 官方教程](https://try.redis.io/) | 2天 |
| Redis 缓存策略（穿透/击穿/雪崩） | 掘金/博客搜"Redis 缓存三大问题" | 1天 |
| Python 操作 Redis（redis-py） | 官方文档 | 1天 |

### SQL 刷题资源

| 平台 | 说明 |
|------|------|
| [LeetCode Database](https://leetcode.cn/problemset/database/) | 从简单到困难，50+ 题 |
| [SQLZoo](https://sqlzoo.net/) | 交互式学习 |
| [牛客网 SQL](https://www.nowcoder.com/exam/oj) | 国内面试高频题 |

### 第9周实战项目：图书管理系统

```
功能要求：
- 图书表、用户表、借阅记录表（三表关联设计）
- 建表 SQL + 索引设计
- Python CLI 实现：增删改查图书、借阅/归还
- 使用 pymysql 直连（先不用 ORM）
- 使用 Redis 缓存热门图书查询结果
- 至少 3 个多表 JOIN 查询 + 1 个窗口函数查询
```

### 📅 第7-9周 每日安排

**第7周（SQL 基础 + 查询能力）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day36：MySQL 安装、连接、基本概念 | 安装 MySQL，创建第一个数据库和表 | 2.5h |
| 周二 | Day37：DDL（CREATE/ALTER/DROP）、字段类型选择 | 设计一个学生管理系统的表结构 | 2.5h |
| 周三 | Day38：DML（INSERT/UPDATE/DELETE）、约束 | 向表中插入 100 条数据（用脚本批量生成） | 2.5h |
| 周四 | Day39 上：SELECT、WHERE、ORDER BY、LIMIT | SQLZoo 完成 SELECT basics + SELECT from world | 2.5h |
| 周五 | Day39 中：JOIN（INNER/LEFT/RIGHT）、子查询 | LeetCode SQL 5 题（JOIN 专题）+ 画表关联图 | 2.5h |
| 周六 | Day39 下：GROUP BY、HAVING、聚合函数 | LeetCode SQL 5 题（聚合专题） | 3h |
| 周日 | 复习 + SQLZoo 通关 | 至少完成 SQLZoo 6 个教程 | 2h |

**第8周（索引 + Python 操作 DB）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day40：索引原理（B+ 树结构、聚集索引 vs 二级索引）| 用 EXPLAIN 分析至少 10 条查询 | 2.5h |
| 周二 | Day43：索引优化（最左前缀、覆盖索引、索引下推）| 给一张百万行数据表建索引，对比查询耗时 | 2.5h |
| 周三 | 索引实战：设计一张订单表，针对不同查询场景加不同索引 | 见下方「索引设计挑战」 | 2.5h |
| 周四 | Day44：pymysql 基础 CRUD | 用 Python 脚本操作 MySQL（连接池/参数化查询） | 2.5h |
| 周五 | Day44 深入：SQLAlchemy Core（不用 ORM，用表达式语言）| 对比 pymysql 原生 SQL 和 SQLAlchemy Core | 2h |
| 周六 | 综合实战：用 Python 写一个数据分析脚本（SQL + 可视化） | 查询数据 → pandas 处理 → matplotlib 画图 | 3h |
| 周日 | 本周复习 + LeetCode SQL 10 题 | 重点做 JOIN + 子查询 + 窗口函数 | 2h |

**第9周（高级特性 + Redis + 实战项目）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Day41-42：视图、存储过程、触发器（了解即可）| 创建一个视图简化复杂查询 | 2h |
| 周二 | 窗口函数深入学习（ROW_NUMBER/RANK/DENSE_RANK/LAG/LEAD）| LeetCode SQL 窗口函数专题 5 题 | 2.5h |
| 周三 | 查询优化实战：见下方「查询优化练习」 | 优化 3 条慢查询，对比前后 EXPLAIN | 2.5h |
| 周四 | Redis 基础：string/hash/list/set/zset 命令 | 跟着 try.redis.io 做完全部练习 | 2.5h |
| 周五 | Python 操作 Redis（redis-py）+ 缓存策略 | 写一个带 Redis 缓存的查询函数 | 2.5h |
| 周六 | **图书管理系统项目 Day 1** | 建表 + 索引 + 基础 CRUD | 4h |
| 周日 | **图书管理系统项目 Day 2** | Redis 缓存 + 复杂查询 + README | 4h |

### 📊 查询优化动手练习

> 创建一个有 100 万行数据的测试表，真实感受索引的威力。

**准备测试数据：**

```sql
-- 创建一张订单表
CREATE TABLE orders (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending','paid','shipped','cancelled') NOT NULL DEFAULT 'pending',
    created_at DATETIME NOT NULL,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 用存储过程插入 100 万行测试数据
DELIMITER $$
CREATE PROCEDURE generate_orders()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 1000000 DO
        INSERT INTO orders (user_id, product_name, amount, status, created_at)
        VALUES (
            FLOOR(1 + RAND() * 10000),
            CONCAT('商品_', FLOOR(1 + RAND() * 5000)),
            ROUND(RAND() * 1000, 2),
            ELT(FLOOR(1 + RAND() * 4), 'pending', 'paid', 'shipped', 'cancelled'),
            DATE_ADD('2024-01-01', INTERVAL FLOOR(RAND() * 730) DAY)
        );
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;

CALL generate_orders();
```

**练习 1：EXPLAIN 分析——观察索引如何改变查询方式**

```sql
-- 无索引范围查询 — 全表扫描
EXPLAIN SELECT * FROM orders WHERE user_id = 5000;
-- 看 type 列：ALL = 全表扫描, ref = 索引查找

-- 复合条件查询
EXPLAIN SELECT * FROM orders 
WHERE user_id = 5000 AND status = 'paid';
-- 第1步：看 key 列，用到了哪个索引？
-- 第2步：看 rows 列，预估扫描多少行？

-- 排序 + 范围查询
EXPLAIN SELECT * FROM orders 
WHERE user_id BETWEEN 1000 AND 2000 
ORDER BY created_at DESC LIMIT 20;
-- 第3步：看 Extra 列有没有 Using filesort（文件排序 → 慢！）
```

**练习 2：索引设计挑战赛**

```sql
-- 挑战：针对以下 4 种查询，设计最优索引组合
-- （加分：每个查询都能用上索引，type 至少达到 ref 级别）

-- 查询A：按用户查订单（高频）
SELECT * FROM orders WHERE user_id = ?;

-- 查询B：按用户 + 状态查订单
SELECT * FROM orders WHERE user_id = ? AND status = ?;

-- 查询C：按时间范围统计用户订单金额
SELECT user_id, SUM(amount) as total 
FROM orders 
WHERE created_at BETWEEN ? AND ? 
GROUP BY user_id;

-- 查询D：分页查某状态订单，按创建时间排序
SELECT * FROM orders 
WHERE status = ? 
ORDER BY created_at DESC 
LIMIT 20 OFFSET 0;

-- 参考答案（自己先想！）
-- A: INDEX idx_uid (user_id) ✓
-- B: INDEX idx_uid_status (user_id, status) — 联合索引，注意列顺序
-- C: INDEX idx_created (created_at) — 覆盖索引可加速回表
-- D: INDEX idx_status_created (status, created_at) — 等值在前，范围在后
```

**练习 3：慢查询定位与优化**

```sql
-- 先开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 0.1;  -- 超过 100ms 就记录

-- 模拟一条慢查询（没有合适索引的大范围扫描）
SELECT * FROM orders WHERE amount > 900;

-- 优化思路：
-- 1. 用 EXPLAIN 看 type 和 rows
-- 2. 确认是否需要加索引？amount 适合建索引吗？（不适合！离散度高）
-- 3. 如果是统计需求，考虑用汇总表或物化视图
-- 4. 如果必须实时查，考虑分区表（按 created_at 分区）
```

### 🐛 阶段 3 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **忘了 WHERE 条件** | 更新/删除了整张表的数据 | `UPDATE users SET status='deleted'` 少写了 WHERE | 先用 `SELECT` 确认 WHERE 条件，再改成 UPDATE/DELETE；开启 `sql_safe_updates` |
| **索引不生效** | EXPLAIN 显示 type=ALL | WHERE 条件左边用了函数（`WHERE YEAR(created_at)=2024`），索引失效 | 改写为范围查询（`WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31'`） |
| **最左前缀不匹配** | 联合索引 (a,b,c) 查 b=1 不走索引 | 联合索引从最左列开始匹配，跳过第一列无法使用 | 调整索引列顺序，把等值查询的列放前面 |
| **隐式类型转换** | 查询慢，EXPLAIN 显示全表扫描 | 字段是 VARCHAR，查询写了 `WHERE user_id = 123`（数字），索引失效 | 保持类型一致，`WHERE user_id = '123'` |
| **SELECT \* 用太多** | 查询慢，网络传输大 | 返回了不需要的列，且不能使用覆盖索引 | 只 SELECT 需要的列 |
| **连接池耗尽** | 程序报 `Too many connections` | 每次请求新开连接，忘了关闭或归还连接池 | 使用连接池（如 SQLAlchemy 的 QueuePool），设置 pool_size 和 max_overflow |
| **Redis 缓存雪崩** | 缓存同时过期，请求全部打到 DB | 大量 key 设置了相同的过期时间 | 过期时间加随机值（如 300 ± random(0, 60) 秒） |
| **SQL 注入风险** | — | 用字符串拼接 SQL：`f"SELECT * FROM users WHERE name='{user_input}'"` | **永远用参数化查询**：`cursor.execute("SELECT * FROM users WHERE name=%s", (name,))` |

### 📋 阶段 3 完成检查清单 + 自测问题

```
□ SQL 能力
  □ 能闭卷写出 INNER JOIN、LEFT JOIN、RIGHT JOIN 的区别和各自使用场景
  □ 能手写至少 3 种窗口函数（ROW_NUMBER/RANK/LAG）
  □ 能解释 GROUP BY 和 DISTINCT 在使用上的区别
  □ 知道 HAVING 和 WHERE 的区别（过滤分组 vs 过滤行）

□ 索引
  □ 能画出 B+ 树的基本结构（根节点/内部节点/叶子节点链表）
  □ 能解释为什么用 B+ 树而不是红黑树（磁盘 IO、范围查询）
  □ 能说出联合索引「最左前缀」原则并举例
  □ 能自己建一张表，设计索引，用 EXPLAIN 验证是否走索引

□ 数据库设计
  □ 能设计一个三表关联的系统（如用户-订单-商品）
  □ 知道什么时候该用外键，什么时候不该用（高并发下外键影响性能）
  □ 能说出三大范式的核心思想（1NF：原子性、2NF：完全依赖、3NF：无传递依赖）

□ Python 操作
  □ 能写参数化查询（防 SQL 注入）
  □ 能用上下文管理器管理数据库连接
  □ 能实现一个简单的 Redis 缓存装饰器

□ 实战
  □ [ ] 图书管理系统完整可用（至少 3 表关联 + Redis 缓存）
  □ [ ] LeetCode SQL 题 50+ 道独立完成
  □ [ ] 至少 5 张表有过 EXPLAIN 分析经验

自测问题：
1. 一张 1000 万行的表，`SELECT * WHERE status='done'` 慢，怎么优化？
2. `(a,b,c)` 联合索引，哪些查询能用上索引？
3. 什么是回表查询？覆盖索引如何避免回表？
4. Redis 缓存穿透、击穿、雪崩分别是什么意思？怎么解决？
```

### 🎤 阶段 3 面试关联

> 数据库是后端面试的"高权重模块"——比语言基础和框架加起来还要重要。

**高频面试题（按出现频率排序）：**
1. "MySQL 索引底层为什么用 B+ 树？"（索引原理 = 第一名）
2. "最左前缀原则是什么？设计一个联合索引 (a,b,c)，哪些查询能走索引？"
3. "慢查询怎么定位？怎么优化？"（开放题，从定位到解决全链路）
4. "事务隔离级别有哪些？MySQL 默认是哪个？什么是 MVCC？"
5. "SQL 注入是什么？怎么防范？"（安全基础，必须秒答）
6. "分库分表怎么做？什么时候需要分？"
7. "Redis 和 MySQL 如何保证数据一致性？"

**回答技巧**：数据库面试题容易从"背答案"变成"真理解"的分水岭是——你能不能在白板上画出 B+ 树结构并解释为什么适合磁盘 IO。

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [《SQL 必知必会》](https://book.douban.com/subject/35167224/) | 短小精悍的 SQL 入门书，手机上看很适合 | 每天 10min |
| [MySQL 索引连环问](https://xiaolincoding.com/mysql/index_interview.html)（小林 coding）| 图解索引，面试必看 | 每天 15min |
| [LeetCode SQL 题解](https://leetcode.cn/problemset/database/) 的官方题解 | 每道题看题解区的分析思路 | 每天 2 题 |
| [Redis 核心技术与实战](https://time.geekbang.org/column/intro/100056701) 前 10 讲 | 极客时间专栏，碎片时间听/看 | 每天 1 讲 |
| [MySQL 实战 45 讲](https://time.geekbang.org/column/intro/100020801) 前 20 讲 | 极客时间专栏，丁奇讲 MySQL 最好的中文资料 | 每天 1 讲 |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| LeetCode SQL 刷题 | 每天至少 3 题，重点做 JOIN + 窗口函数 | 每天 |
| EXPLAIN 分析 | 每写一条查询都 EXPLAIN 看一下，养成习惯 | 每次查询 |
| 造测试数据 | 用存储过程生成 10 万+ 行数据，练习索引优化 | 1 次 |
| 慢查询优化实战 | 从慢查询日志中找 3 条查询，逐一优化到 < 50ms | 1 次 |
| Redis 动手 | 5 种数据结构每种写 10 个命令，感受各自适用场景 | 1 次 |

---

## 🟣 阶段 4：后端框架（4 周）

> **目标**：能用 FastAPI 写生产级 REST API，知道 Django 能干什么
> **检验标准**：独立完成一套完整的 REST API（CRUD + 认证 + 分页 + 文件上传）

### FastAPI 主线（3 周）

> **框架选择**：FastAPI 为主（现代、异步、类型安全），Django 为了解面试和接老项目

| 周数 | 主题 | 资源 |
|------|------|------|
| 第10周 | 快速上手 + 路径参数 + 请求体 + Pydantic 校验 | [FastAPI 官方教程](https://fastapi.tiangolo.com/zh/tutorial/) 第1-10章 |
| 第10周 | 依赖注入（Depends）、中间件、异常处理 | 官方教程续 |
| 第11周 | 数据库集成（SQLAlchemy + Alembic 迁移） | [SQLAlchemy 2.0 文档](https://docs.sqlalchemy.org/en/20/) |
| 第11周 | **JWT 认证 + OAuth2** | FastAPI 安全章节 |
| 第12周 | **asyncio 速通**（事件循环/协程/await 原理/asyncio.gather vs create_task） | [Python 官方 asyncio 文档](https://docs.python.org/zh-cn/3/library/asyncio.html) |
| 第12周 | 文件上传、后台任务（BackgroundTasks）、测试 | 官方教程续 |

### FastAPI 详细学习清单

```
□ 路径操作（@app.get/post/put/delete）
□ 路径参数与查询参数
□ 请求体（BaseModel / Pydantic）
□ 响应模型（response_model）
□ 依赖注入（Depends）—— 这是 FastAPI 的灵魂
□ 中间件（CORS / 日志 / 限流）
□ 异常处理（HTTPException / 自定义异常处理器）
□ SQLAlchemy 2.0 ORM（session/async/relationship）
□ Alembic 数据库迁移
□ JWT 认证（python-jose + passlib）
□ asyncio 核心：事件循环、协程、await 原理、asyncio.gather vs create_task
□ 文件上传（UploadFile）
□ 后台任务（BackgroundTasks / Celery）
□ 分页（limit-offset / cursor-based）
□ 单元测试（pytest + httpx TestClient）
□ 集成测试（pytest 测 API 全链路：请求→数据库→响应）
□ 自动生成的 Swagger 文档
□ 项目结构组织（分层架构）
```

### Django 了解 + 框架对比（1 周，第13周）

> 只学核心概念，能看懂 Django 代码即可，不做主力框架。

| 主题 | 来源 | 时间 |
|------|------|------|
| MVT 架构、路由、模型 ORM | Python-100-Days Day46-47 | 1天 |
| Django Admin 管理后台 | 同上 | 0.5天 |
| Django REST Framework（DRF） | Python-100-Days Day54-55 | 2天 |
| Django 中间件、Celery | Python-100-Days Day52,58 | 1天 |
| **FastAPI vs Flask vs Django 设计哲学对比** | 自己整理对比表 | 0.5天 |

### 第13周实战项目：RESTful 博客 API

```
技术栈：FastAPI + SQLAlchemy + PostgreSQL + Redis + JWT

功能要求：
□ 用户注册/登录（JWT 认证）
□ 文章的 CRUD（创建/阅读/更新/删除）
□ 文章分类和标签
□ 评论功能
□ 分页查询
□ 搜索（标题模糊匹配）
□ 热门文章缓存（Redis）
□ 单元测试覆盖率 > 70%
□ Swagger API 文档自动生成
□ Docker 部署

目录结构参考：
app/
├── main.py          # FastAPI 应用入口
├── config.py        # 配置管理
├── database.py      # 数据库连接
├── models/          # SQLAlchemy 模型
├── schemas/         # Pydantic 请求/响应模型
├── api/             # 路由（按模块分）
├── services/        # 业务逻辑层
├── utils/           # 工具函数（JWT/密码哈希）
└── tests/           # 测试
```

### ⚡ 阶段 4 附加：设计模式速通（第13周穿插，约 1 周）

> **为什么要学**：这是从"能写代码"到"能设计代码"的质变。用 Python 实现，不堆理论。

| 模式 | 场景 | Python 实现要点 |
|------|------|---------------|
| **工厂模式** | 根据配置创建不同数据库连接、支付渠道 | `def create_conn(db_type: str) -> Connection` |
| **策略模式** | 切换不同排序算法、缓存淘汰策略 | 把算法封装为可替换的函数/类，注入调用方 |
| **单例模式** | 全局配置管理、数据库连接池 | `__new__` + 模块级别单例（Python 模块天然单例） |
| **观察者模式** | 事件系统、消息通知（订单状态变更→发邮件+发短信） | 用 `__call__` 或回调函数实现 |
| **装饰器模式** | 日志、计时、权限校验 | Python 天然支持（`@decorator`），重点讲如何写带参数的装饰器 |

**检验标准**：能在博客 API 中至少应用 2 种模式（如装饰器做日志、策略模式做排序），讲清楚为什么用、不用会怎样。

> 🎓 **面试价值**："你用过哪些设计模式？"是高级/资深岗位的高频题。每种模式准备 1 句话场景 + 1 段代码即可。

### 📅 第10-13周 每日安排

**第10周（FastAPI 入门 + 依赖注入）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | FastAPI 安装、第一个 API、路径参数 | 写 3 个 GET 端点（hello、获取用户、计算器） | 2.5h |
| 周二 | 查询参数、请求体（BaseModel/Pydantic）| 写 POST 端点，用 Pydantic 校验请求数据 | 2.5h |
| 周三 | 响应模型（response_model）、状态码 | 设计一个创建用户的完整 API（请求校验→响应模型→错误状态） | 2.5h |
| 周四 | 依赖注入（Depends）Day 1：基础用法 | 把数据库连接和配置提取为依赖项 | 2.5h |
| 周五 | 依赖注入 Day 2：可复用的依赖、依赖嵌套 | 写一个「当前用户」依赖（从 Header 获取 token） | 2.5h |
| 周六 | 中间件：CORS、日志、请求计时 | 写 3 个中间件，理解执行顺序 | 3h |
| 周日 | 异常处理：HTTPException、自定义异常处理器 | 为 API 设计一套统一的错误响应格式 | 2h |

**第11周（数据库集成 + 认证）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | SQLAlchemy 2.0 入门：引擎、Session、声明式基类 | 定义 3 个模型（User/Article/Comment），建表 | 2.5h |
| 周二 | SQLAlchemy relationship + 增删改查 | 写文章的 CRUD API，关联用户 | 2.5h |
| 周三 | Alembic 数据库迁移 | 创建第一次迁移，修改表结构后生成新迁移 | 2h |
| 周四 | JWT 认证 Day 1：注册、密码哈希、生成 Token | 用 python-jose + passlib 实现注册/登录 | 2.5h |
| 周五 | JWT 认证 Day 2：Token 验证依赖、刷新 Token | 保护需要认证的路由，实现 refresh token | 2.5h |
| 周六 | OAuth2 密码流 + Swagger 授权 | 让 Swagger 文档支持「先登录再调 API」 | 3h |
| 周日 | 本周复习 + 集成测试 | 用 pytest + httpx 测完整的认证流程 | 2h |

**第12周（asyncio + 高级特性）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | asyncio Day 1：事件循环、协程对象、await | 写 3 个协程，理解 await 挂起和恢复 | 2.5h |
| 周二 | asyncio Day 2：gather vs create_task、同步原语 | 并发调用 3 个外部 API，对比串行耗时 | 2.5h |
| 周三 | asyncio Day 3：异步上下文管理器、异步生成器 | 改造成数据库连接为异步的 | 2h |
| 周四 | 文件上传（UploadFile）、静态文件服务 | 实现图片上传 + 缩略图生成（Pillow） | 2.5h |
| 周五 | 后台任务（BackgroundTasks）+ Celery 入门 | 发送邮件验证码（后台任务）vs 报表生成（Celery） | 2.5h |
| 周六 | 分页（limit-offset + cursor-based）+ 搜索/筛选 | 为文章列表实现完整的分页+搜索+排序 | 3h |
| 周日 | 测试 Day：单元测试 + 集成测试 + 覆盖率 | pytest + pytest-cov，目标 70%+ | 2h |

**第13周（Django 了解 + 设计模式 + 博客项目）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Django 快速上手：MVT、Admin、模型 ORM | 用 Django 搭一个博客，对比 FastAPI 的差异 | 2.5h |
| 周二 | Django REST Framework（DRF）：序列化器、视图集 | 用 DRF 写一套 API，对比 FastAPI 的差异 | 2.5h |
| 周三 | 框架对比：FastAPI vs Django vs Flask 设计哲学 | 整理一张三方对比表（性能/生态/学习曲线/适合场景） | 2h |
| 周四 | 设计模式 Day 1：工厂模式 + 单例模式 | 在博客 API 中实现「根据配置切换缓存后端」 | 2.5h |
| 周五 | 设计模式 Day 2：策略模式 + 观察者模式 | 在博客 API 中实现「文章排序策略可切换」 | 2.5h |
| 周六 | **博客 API 项目 Day 1** | 实现用户+文章+评论的基础 CRUD + JWT | 5h |
| 周日 | **博客 API 项目 Day 2** | 完善分页+搜索+缓存+测试+Swagger+Dockerfile | 5h |

### 🔧 FastAPI 深度实战：错误处理最佳实践

> FastAPI 的错误处理不是 `try/except` 一包了之，需要分层设计。

**模式 1：统一错误响应格式**

```python
# schemas/error.py
from pydantic import BaseModel
from typing import Optional, Any

class ErrorResponse(BaseModel):
    success: bool = False
    error_code: str          # "USER_NOT_FOUND", "VALIDATION_ERROR"
    message: str             # 用户可读的错误描述
    detail: Optional[Any] = None   # 调试信息（生产环境别放敏感数据）

# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            error_code="INVALID_INPUT",
            message=str(exc)
        ).model_dump()
    )
```

**模式 2：自定义异常层次**

```python
# exceptions.py
class AppException(Exception):
    """应用异常基类"""
    def __init__(self, error_code: str, message: str, status_code: int = 400):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code

class NotFoundException(AppException):
    def __init__(self, resource: str, identifier: str):
        super().__init__(
            error_code=f"{resource.upper()}_NOT_FOUND",
            message=f"{resource} {identifier} 不存在",
            status_code=404
        )

class UnauthorizedException(AppException):
    def __init__(self):
        super().__init__(
            error_code="UNAUTHORIZED",
            message="未登录或 Token 已过期",
            status_code=401
        )

# 在路由中抛出
@app.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise NotFoundException("用户", str(user_id))
    return user

# 全局异常处理器
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error_code=exc.error_code,
            message=exc.message
        ).model_dump()
    )
```

**模式 3：Pydantic 校验陷阱与解决方案**

```python
# 常见错误：校验失败时 FastAPI 自动返回 422，格式不是你想要的
# 解决方案：重写校验异常处理器

from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"]
        })
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            error_code="VALIDATION_ERROR",
            message="输入参数校验失败",
            detail=errors
        ).model_dump()
    )
```

**生产级 API 的错误处理检查表：**

```
□ 有全局异常处理器（捕获未预期的 500 错误）
□ 业务异常有清晰的错误码（不是 "ERROR" 这种模糊命名）
□ 校验错误返回具体字段信息（哪个字段、什么原因）
□ 生产环境不暴露堆栈信息
□ 404/401/403 有不同处理
□ 日志记录（异常时打印 traceback，方便排查）
```

### 🐛 阶段 4 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **async 路由里用了同步 IO** | 系统并发吞吐量始终上不去 | 在 async 函数里调用了 `time.sleep()` 或同步 `requests.get()`，阻塞了事件循环 | async 路由中用 `await asyncio.sleep()` 和 `httpx.AsyncClient`；CPU 密集型用 `run_in_executor` |
| **Depends 循环依赖** | FastAPI 启动报错 | A 依赖 B，B 又依赖 A | 重构：提取公共逻辑到第三个依赖，或使用 `Depends(lambda:)` 延迟加载 |
| **SQLAlchemy Session 跨请求共用** | 偶尔报 `Instance is detached` 或脏数据 | Session 不是线程安全的，跨请求共用一个 Session 会出问题 | 每个请求创建新 Session（用 `Depends(get_db)` + `yield`） |
| **JWT Token 没有过期机制** | Token 泄露后无法撤销 | Token 设置了 `exp` 但没实现黑名单或 refresh 机制 | access token 设置短过期（15min）+ refresh token（7天）+ Redis 黑名单 |
| **密码明文存储** | 安全隐患 | 以为哈希了但用了 md5（不安全）| 用 passlib 的 `bcrypt`，`hash()` 和 `verify()` |
| **N+1 查询问题** | 查 100 个用户 + 每人 10 篇文章 = 1001 次查询 | relationship 默认懒加载（lazy="select"） | 用 `selectinload()` 或 `joinedload()` 预加载关联数据 |
| **Alembic 迁移冲突** | 两个分支都生成了迁移，合并时冲突 | 多人开发时迁移生成顺序不一致 | 合并迁移文件时检查 `down_revision`，用 `alembic merge` 创建合并迁移 |
| **CORS 配置不当** | 前端调用报 CORS 错误 | 只允许了特定 origin 但前端用了不同端口 | 开发环境用 `allow_origins=["*"]`，生产环境精确配置 |

### 📋 阶段 4 完成检查清单 + 自测问题

```
□ FastAPI 核心
  □ 能用路径参数/查询参数/请求体写完整的 REST API
  □ 理解 Depends 的执行原理（请求进来时解析依赖树）
  □ 能写自定义中间件并理解执行顺序
  □ 能自定义异常处理器，统一 API 错误格式

□ 数据库集成
  □ 能用 SQLAlchemy 2.0 定义模型和 relationship
  □ 能用 Alembic 管理数据库版本（创建/升级/回滚迁移）
  □ 能识别并解决 N+1 查询问题
  □ 能用 selectinload/joinedload 优化查询

□ 认证
  □ 能实现 JWT 认证（access + refresh token 双令牌机制）
  □ 能实现基于角色的权限控制（普通用户 vs 管理员）
  □ 知道密码哈希为什么不能用 md5（用 bcrypt）

□ asyncio
  □ 能解释事件循环的工作原理（单线程 + 协程调度）
  □ 能判断何时用 asyncio.gather、何时用 asyncio.create_task
  □ 知道 async def 函数里不能调用同步阻塞 IO 的原因

□ Django（了解即可）
  □ 能搭建一个基本的 Django 项目（模型 + 视图 + 模板 + Admin）
  □ 能说出 FastAPI 和 Django 各适合什么场景
  □ 知道 DRF 的核心概念（Serializer/ViewSet/Router）

□ 设计模式
  □ 能用 Python 实现至少 4 种设计模式
  □ 能在自己项目中找到至少 2 个可应用设计模式的地方

□ 实战
  □ [ ] RESTful 博客 API 完整可用，有 Swagger 文档
  □ [ ] 单元测试覆盖率 > 70%
  □ [ ] 有 Dockerfile + docker-compose.yml
  □ [ ] API 错误响应格式统一

自测问题：
1. FastAPI 的 Depends 是怎么工作的？和 Flask/Django 的中间件有什么区别？
2. async def 和 def 在 FastAPI 路由中有什么区别？什么时候必须用 async def？
3. 一个 API 请求进来，SQLAlchemy Session 的生命周期是怎样的？
4. N+1 查询是什么？怎么发现？怎么解决？
```

### 🎤 阶段 4 面试关联

> 后端框架面试 = 原理理解 + 项目经验。光说"我用了 FastAPI"不够，要说"我为什么选 FastAPI"。

**高频面试题：**
- "FastAPI 为什么快？" → Starlette（异步）+ Pydantic（类型校验自动文档）+ uvloop
- "FastAPI 的 Depends（依赖注入）和 Flask 的装饰器有什么区别？"
- "asyncio 原理：什么是事件循环？async/await 底层怎么实现的？"
- "你做过哪些性能优化？" → N+1 查询、数据库连接池、Redis 缓存、分页、异步化
- "JWT 和 Session 的区别？Token 泄露了怎么办？"
- "Django 和 FastAPI 你分别用在什么场景？" → Django：CMS/管理后台；FastAPI：API 服务/微服务

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [FastAPI 官方教程](https://fastapi.tiangolo.com/zh/tutorial/) 逐章阅读 | 手机上阅读，晚上电脑动手 | 每天 20min |
| [SQLAlchemy 2.0 迁移指南](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html) | 了解 1.x → 2.0 的变化 | 30min |
| [JWT 深入理解](https://jwt.io/introduction) | JWT 结构、签名、Claims 详解 | 20min |
| 《流畅的 Python》第 17-18 章（协程）| 最好的 asyncio 入门材料 | 每天 15min |
| [设计模式 Python 版](https://refactoringguru.cn/design-patterns/python) | 每个模式 10 分钟看完 | 每天 1-2 个 |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| 每天写一个 API 端点 | 从最基础的 CRUD 开始，逐步加认证/分页/过滤 | 每天 |
| 对比实验 | 同样的功能分别用同步和异步实现，用 ab/wrk 压测对比 | 1-2 次 |
| 阅读源代码 | 看 FastAPI 的 `APIRouter.add_api_route` 是怎么注册路由的 | 1 次 |
| 写中间件 | 限流中间件、请求日志中间件、IP 白名单中间件 | 3 个 |
| Django 对比实践 | 同一个「博客」需求分别用 FastAPI 和 Django 实现 | 1 次 |

---

## 🔵 阶段 5：前端框架（5 周）

> **目标**：能用 React + Next.js + TypeScript 开发完整的前端应用
> **检验标准**：独立完成后台管理系统前端（登录 + 列表 + 表单 + 图表）

> 🧭 **前端框架选择指南**：本计划主线使用 **React + Next.js + TypeScript**（国际市场最大、岗位最多）。如果你主要面向**国内中小型公司**，可以考虑 **Vue 3 + Nuxt**（国内流行度极高，学习曲线更平缓，Python-100-Days 自带 Vue 入门）。核心 JS/TS/CSS 基础同样适用，切换成本可控。**建议按主线走 React，如果后续发现国内岗位普遍要求 Vue，补 2 周即可切换。**

### 子阶段 5A：Web 前端基础 + TypeScript 入门（1.5 周）

| 周数 | 主题 | 资源 | 时间 |
|------|------|------|------|
| 第14周 | HTML5 语义化标签 | [MDN HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML) | 1天 |
| 第14周 | CSS3（盒模型/Flex/Grid/响应式） | [MDN CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS) | 3天 |
| 第14周 | **JavaScript 核心**（变量/函数/闭包/异步/Promise） | [现代 JavaScript 教程](https://zh.javascript.info/) | 3天 |
| 第14周 | **TypeScript 速通**（基础类型/接口/泛型/工具类型） | [TypeScript 官方 handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | 1天 |

> ⚠️ **JS 基础必须打牢，TS 从第一天就写。** Promise、async/await、数组方法（map/filter/reduce）、解构赋值、模块化（ESM）必须熟练。TypeScript 只需 1 天过基础语法，后续边写 React 边深入，不要试图"学完再写"。

### 子阶段 5B：React 核心（TypeScript 全程）（2 周）

> ⚠️ **所有 React 代码都用 `.tsx`，props/state/hooks 必须带类型。**

| 周数 | 主题 | 资源 |
|------|------|------|
| 第15周 | 组件/JSX/Props/State/Hooks（TypeScript 版） | [React 官方文档](https://react.dev/) Quick Start + 教程 |
| 第15周 | **核心 Hooks**：useState/useEffect/useContext/useRef/useMemo/useCallback | 官方文档 + 练习 |
| 第15周 | 状态管理：Zustand（TS 版，比 Redux 简单 10 倍） | [Zustand 文档](https://docs.pmnd.rs/zustand) |
| 第16周 | React Router（路由，TS 类型推导） | [React Router 文档](https://reactrouter.com/) |
| 第16周 | **数据请求**：TanStack Query（React Query，TS 泛型加持） | [TanStack Query 文档](https://tanstack.com/query) |
| 第16周 | 表单处理：React Hook Form + Zod 校验（TS 类型安全） | 各自官方文档 |

### 子阶段 5C：Next.js + UI 组件库（1.5 周）

| 周数 | 主题 | 资源 |
|------|------|------|
| 第17周 | Next.js App Router / SSR/SSG/ISR（TS 全栈） | [Next.js 官方教程](https://nextjs.org/learn) |
| 第17周 | API Routes / Server Actions | 同上 |
| 第17周 | **TypeScript 深入**（泛型约束/条件类型/类型体操入门） | 边写 Next.js 边查 TS 文档 |
| 第18周 | UI 库：**Ant Design**（国内首选）或 **Shadcn/ui**（国际化） | 各自文档 |
| 第18周 | 图表：**ECharts** 或 Recharts | 文档 |

### 前端学习资源汇总

| 资源 | 用途 |
|------|------|
| [现代 JavaScript 教程](https://zh.javascript.info/) | JS 基础必看，最好的中文 JS 教程 |
| [TypeScript 官方 handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | TS 基础 1 天速通，之后边写边查 |
| [React 官方文档](https://react.dev/) | 新版文档极好，直接看英文版（代码示例切到 TS） |
| [Next.js 官方教程](https://nextjs.org/learn) | 做 Dashboard 项目就是最好的练习 |
| [Zustand](https://docs.pmnd.rs/zustand) | 10 分钟学会的状态管理 |
| [Tailwind CSS](https://tailwindcss.com/) | 🔷选学，写样式极快 |

### 第18周实战项目：后台管理系统前端

```
技术栈：React + TypeScript + Next.js + Ant Design + Zustand + TanStack Query

功能要求：
□ 登录/注册页面（对接后端 JWT）
□ 仪表盘（ECharts 图表）
□ 数据列表页（分页/搜索/排序/筛选）
□ 表单页（新增/编辑，含文件上传）
□ 侧边栏导航 + 面包屑
□ Token 自动刷新
□ 路由守卫（未登录跳转）

对接你自己的阶段4博客 API 后端
```

### 📅 第14-18周 每日安排

**第14周（Web 基础 + TypeScript 速通）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | HTML5：语义化标签、表单元素、SEO 基础 | 手写一个 HTML 简历页面（不用 CSS） | 2.5h |
| 周二 | CSS3 Day 1：盒模型、选择器、定位（relative/absolute/fixed） | 仿写一个卡片布局 | 2.5h |
| 周三 | CSS3 Day 2：Flexbox 布局 | 用 Flexbox 仿一个导航栏 + 三栏布局 | 2.5h |
| 周四 | CSS3 Day 3：Grid 布局 + 响应式（@media） | 用 Grid 仿一个 Dashboard 布局 | 2.5h |
| 周五 | JavaScript Day 1：变量、函数、闭包、this | 写一个计数器、一个防抖函数 | 2.5h |
| 周六 | JavaScript Day 2：异步（Promise/async/await） | 用 fetch 调一个公开 API 并渲染到页面 | 3h |
| 周日 | JavaScript Day 3：数组方法（map/filter/reduce）+ 解构 | LeetCode JS 简单题 5 题 | 2h |

**第15周（React 基础 + Hooks）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | TypeScript 速通：基础类型、接口、泛型 | 把昨天的 JS 练习全部改为 `.ts` | 2h |
| 周二 | React Day 1：JSX、组件、Props（全部 .tsx） | 写 5 个小组件（Button/Input/Card/Badge/Avatar） | 2.5h |
| 周三 | React Day 2：useState、事件处理 | 写一个计数器 + 待办列表 | 2.5h |
| 周四 | React Day 3：useEffect、副作用清理 | 写一个实时搜索框（防抖 + API 调用） | 2.5h |
| 周五 | React Day 4：useContext + useReducer | 用 Context 实现全局主题切换 | 2.5h |
| 周六 | React Day 5：useRef/useMemo/useCallback | 写一个表单，优化重渲染 | 3h |
| 周日 | 状态管理：Zustand 入门 | 用 Zustand 重构待办列表的状态管理 | 2h |

**第16周（路由 + 数据请求）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | React Router Day 1：路由配置、Link/Navigate | 搭一个 3 页面的路由（首页/列表/详情页） | 2.5h |
| 周二 | React Router Day 2：嵌套路由、路由守卫 | 实现「未登录跳转登录页」的逻辑 | 2.5h |
| 周三 | TanStack Query Day 1：useQuery、缓存 | 对接你的博客 API，展示文章列表 | 2.5h |
| 周四 | TanStack Query Day 2：useMutation、乐观更新 | 实现文章的创建和删除（乐观更新） | 2.5h |
| 周五 | 表单：React Hook Form + Zod 校验 | 写一个注册表单，完整的前后端校验 | 2.5h |
| 周六 | 综合 Day 1：写一个完整的 CRUD 页面 | 文章列表 + 新增 + 编辑 + 删除，全程 TypeScript | 3h |
| 周日 | 综合 Day 2：TypeScript 类型体操练习 | 手写几个常用工具类型（Partial/Pick/Omit 的实现） | 2h |

**第17周（Next.js + 服务端渲染）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Next.js Day 1：App Router、文件路由、布局 | 创建 Next.js 项目，搭好基础路由 | 2.5h |
| 周二 | Next.js Day 2：Server Components vs Client Components | 理解 RSC 边界，改写组件 | 2.5h |
| 周三 | Next.js Day 3：数据获取（fetch/Server Actions） | 用 Server Components 渲染文章列表 | 2.5h |
| 周四 | Next.js Day 4：SSR/SSG/ISR 三种渲染策略 | 对比三种策略的构建输出和首屏性能 | 2.5h |
| 周五 | API Routes + Server Actions | 在 Next.js 里写 API，对接你的 FastAPI 后端 | 2.5h |
| 周六 | 实战 Day 1：迁移 React 项目到 Next.js | 把第16周的 CRUD 页面迁移到 Next.js App Router | 3h |
| 周日 | 实战 Day 2：TypeScript 深入 | 泛型约束/条件类型/模板字面量类型的实战练习 | 2h |

**第18周（UI 库 + 图表 + 后台管理项目）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Ant Design：布局、表格、表单、通知 | 用 Ant Design 组件替换手写组件 | 2.5h |
| 周二 | Ant Design ProComponents（ProTable/ProForm）| 用 ProTable 做一个带搜索/分页/排序的列表 | 2.5h |
| 周三 | ECharts：折线图、柱状图、饼图、仪表盘 | 写一个数据看板（4 个图表） | 2h |
| 周四 | Token 自动刷新 + 路由守卫 | 实现完整的认证流程（401 → refresh → 重试） | 2.5h |
| 周五 | 文件上传（前端）+ 进度条 | 对接 FastAPI 的文件上传 API | 2h |
| 周六 | **后台管理系统项目 Day 1** | 登录页 + 仪表盘 + 列表页 | 5h |
| 周日 | **后台管理系统项目 Day 2** | 表单页 + 路由守卫 + 完善细节 + 推到 GitHub | 5h |

### 🎨 React 组件设计模式

**模式 1：Compound Components（复合组件）**

```tsx
// 应用场景：Tab、Select、Dropdown 等需要「父子组件通信」的场景
// 优势：组件使用者自由组合，不需要传几十个 props

// 定义
interface TabsContextType {
  activeKey: string;
  setActiveKey: (key: string) => void;
}
const TabsContext = createContext<TabsContextType | null>(null);

const Tabs = ({ children, defaultKey }: { children: ReactNode; defaultKey: string }) => {
  const [activeKey, setActiveKey] = useState(defaultKey);
  return (
    <TabsContext.Provider value={{ activeKey, setActiveKey }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
};

const TabPane = ({ tabKey, label, children }: { tabKey: string; label: string; children: ReactNode }) => {
  const ctx = useContext(TabsContext);
  if (!ctx) throw new Error("TabPane must be used inside Tabs");
  return ctx.activeKey === tabKey ? <div>{children}</div> : null;
};

// 使用
<Tabs defaultKey="info">
  <TabPane tabKey="info" label="基本信息"><UserInfo /></TabPane>
  <TabPane tabKey="orders" label="订单列表"><OrderList /></TabPane>
</Tabs>
```

**模式 2：Render Props / 函数子组件**

```tsx
// 应用场景：列表/表格组件，让使用者自定义每行的渲染
interface ListProps<T> {
  items: T[];
  renderItem: (item: T, index: number) => ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map((item, i) => <li key={i}>{renderItem(item, i)}</li>)}</ul>;
}

// 使用（泛型自动推导！）
<List items={users} renderItem={(user) => <UserCard user={user} />} />
```

**模式 3：Custom Hook 提取逻辑**

```tsx
// 原则：组件只负责渲染，逻辑放在 Hook 里

// 不好的写法：组件里混了数据请求逻辑
function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => { /* 一大堆请求逻辑... */ }, []);
  return (/* 渲染 */);
}

// 好的写法：逻辑抽到 Hook
function useArticles(page: number) {
  return useQuery({
    queryKey: ['articles', page],
    queryFn: () => fetchArticles(page),
  });
}

function ArticleList() {
  const { data, isLoading, error } = useArticles(1);
  if (isLoading) return <Skeleton />;
  if (error) return <Error message={error.message} />;
  return <ArticleCards articles={data} />;
}
```

### 🧩 前端状态管理分层策略

> 不是所有状态都放 Zustand/Redux。分清三类状态，代码清爽十倍。

```
┌─────────────────────────────────────────────────┐
│  服务器状态                                       │
│  来源：API 返回的数据                              │
│  工具：TanStack Query / SWR                      │
│  特点：有缓存、有过期、需要重新请求                 │
│  示例：文章列表、用户信息、下拉选项                  │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│  客户端状态                                       │
│  来源：用户交互产生的                              │
│  工具：Zustand / useContext                       │
│  特点：纯前端状态，不涉及服务端                     │
│  示例：主题、侧边栏展开、表单草稿、购物车            │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│  URL 状态                                        │
│  来源：URL 参数（searchParams / pathParams）       │
│  工具：Next.js useSearchParams / React Router      │
│  特点：可分享、可书签、可前进后退                    │
│  示例：搜索关键词、分页页码、筛选条件、Tab 切换      │
└─────────────────────────────────────────────────┘
```

**判断法则**：一个状态要不要放 URL？—— 如果你希望用户刷新页面后状态还在，就放 URL。

### 🐛 阶段 5 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **useEffect 无限循环** | 页面卡死，请求不停发 | 依赖数组里放了对象/数组（每次渲染都是新引用） | 依赖数组只放基本类型值；对象用 useMemo 稳定引用 |
| **闭包陷阱** | useEffect 里拿到的 state 是旧值 | 闭包捕获了创建时的变量值 | 用 `useRef` 保存最新值，或用函数式更新 `setState(prev => prev + 1)` |
| **Server Component 里用了 useState** | Next.js 报错 | RSC 不能有交互状态 | 在文件顶部加 `"use client"`，或把交互逻辑抽到单独的 Client Component |
| **TypeScript 报 `possibly undefined`** | 访问 API 返回值时报错 | 未处理数据加载中/空状态/错误状态 | 始终写 `if (isLoading) return <Loading />`，类型守卫后使用数据 |
| **CSS Module 样式不生效** | 样式写了但没变化 | 类名被哈希了，用字符串拼的不对 | 使用 CSS Module 时写成 `styles.myClass`，不要用字符串 |
| **Token 过期后请求 401 不处理** | 用户突然被登出 | TanStack Query 没有全局的 401 重试逻辑 | 在 QueryClient 配置全局 `onError`，检测 401 后刷新 token 或跳转登录 |

### 📋 阶段 5 完成检查清单 + 自测问题

```
□ Web 基础
  □ 能独立手写一个响应式布局页面（Flex + Grid + 媒体查询）
  □ 能解释 CSS 盒模型、BFC、层叠上下文
  □ 能解释 JS 事件循环（宏任务/微任务）

□ React
  □ 能解释 Virtual DOM 的作用和 diff 算法的基本思路
  □ 能列出至少 5 个 React Hooks 并说出各自使用场景
  □ 理解「组件只负责渲染」原则 —— 逻辑在 Hook，渲染在 JSX

□ TypeScript（全程使用）
  □ 能为组件 Props 定义准确的类型（不用 any）
  □ 理解泛型在 React 中的应用（如 useQuery<T>）
  □ 能手写常用的工具类型（Partial/Required/Pick/Omit/Record）

□ Next.js
  □ 知道什么时候用 Server Component，什么时候用 Client Component
  □ 能区分 SSR/SSG/ISR 并选择合适的一种
  □ 能用 Server Actions 做数据变更

□ 状态管理
  □ 能分清服务器状态、客户端状态、URL 状态，各用各的工具
  □ 能用 Zustand + TanStack Query 完成一个完整的功能

□ 实战
  □ [ ] 后台管理系统前端完整可用（对接后端 API）
  □ [ ] 所有组件有 TypeScript 类型标注
  □ [ ] 有 Loading/Empty/Error 三种状态处理
  □ [ ] 有路由守卫和 Token 自动刷新

自测问题：
1. React 的 useEffect 和 useLayoutEffect 有什么区别？
2. 为什么 React 需要 key 属性？用 index 做 key 有什么问题？
3. Next.js App Router 中，一个页面怎么混合使用 Server Component 和 Client Component？
4. zustand 和 Redux 的本质区别是什么？（不需要背，理解 pub/sub 模式）
```

### 🎤 阶段 5 面试关联

> 全栈面试中的前端部分一般不会问太深，但 React 核心原理和 TypeScript 必问。

**高频面试题：**
- "React 的 Virtual DOM 是什么？Diff 算法做了什么优化？"
- "useEffect 的依赖数组怎么用？有什么坑？"
- "React 18 的 Concurrent Mode 做了什么？"
- "TypeScript 的泛型是什么？你在项目中怎么用的？"（举具体例子）
- "Next.js 的 Server Components 和 Client Components 怎么区分？为什么要分？"

**回答建议：** 前端面试题偏「用过没」而非「背过没」。每个问题准备一个你项目中的真实例子。

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [React 官方文档](https://react.dev/)（英文版） | 新版文档极好，阅读就是学习 | 每天 20min |
| [现代 JavaScript 教程](https://zh.javascript.info/) 第二部分（浏览器） | DOM 操作/事件/表单/网络请求 | 每天 15min |
| [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | 核心章节反复读 | 每天 10min |
| [Next.js 官方教程](https://nextjs.org/learn) 文字版 | 手机上看概念，电脑上做练习 | 每天 15min |
| [Josh W Comeau 博客](https://www.joshwcomeau.com/) | CSS/React 交互式教程，手机上也能看 | 碎片时间 |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| 仿写组件 | 看到好看的 UI 组件，自己用 React 实现一个 | 每周 2 个 |
| 读组件库源码 | 看 Ant Design 的一个简单组件（如 Button）是怎么写的 | 1 次 |
| 性能优化实战 | 用 React DevTools Profiler 找到重渲染的组件，用 memo/useMemo 优化 | 1 次 |
| 类型体操 | 每天做 1 个 TypeScript 类型挑战（type-challenges 仓库） | 每天 |
| 写一个 NPM 包 | 把你自己写的 Hook（如 useDebounce）发布到 npm | 1 次 |

---

## 🟤 阶段 6：DevOps（3 周）

> **目标**：能把全栈项目部署到服务器，配置 CI/CD 自动部署
> **检验标准**：访问一个公网域名能看到你的项目运行

### 学习清单

| 周数 | 主题 | 资源 | 时间 |
|------|------|------|------|
| 第19周 | **Docker** | [Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/) | 3天 |
| 第19周 | Dockerfile 编写 + Docker Compose 多容器编排 | 同上 | 2天 |
| 第19周 | **Git 深入**（分支策略/rebase/cherry-pick/冲突解决） | [Pro Git](https://git-scm.com/book/zh/v2) | 1天 |
| 第20周 | **Linux 深入**（systemd/日志/进程/权限/定时任务） | Python-100-Days Day34-35 + [鸟哥的 Linux 私房菜](https://linux.vbird.org/) | 2天 |
| 第20周 | **Linux 进程/线程模型实践**（为什么 Nginx 用多进程、Node.js 用单线程、Python GIL 的影响） | 博客 + 动手验证 | 0.5天 |
| 第20周 | **Nginx**（反向代理/负载均衡/HTTPS/静态资源） | [Nginx 官方文档](https://nginx.org/en/docs/) + 博客 | 2.5天 |
| 第21周 | **CI/CD**（GitHub Actions 自动测试/构建/部署） | [GitHub Actions 文档](https://docs.github.com/en/actions) | 2天 |
| 第21周 | **监控与日志**：Prometheus + Grafana（1天）、Python 结构化日志（logging + JSON 格式，0.5天） | [Prometheus 官方文档](https://prometheus.io/docs/) + [Grafana 教程](https://grafana.com/tutorials/) | 1.5天 |
| 第21周 | **云服务**（阿里云/AWS EC2 基础使用） | 各自控制台文档 + 动手 | 1天 |

### DevOps 详细技能清单

```
□ Docker：镜像构建、容器运行、Dockerfile、docker-compose
□ Docker：多阶段构建、卷挂载、网络模式
□ Git：分支管理（Git Flow/GitHub Flow）
□ Git：rebase 合并、cherry-pick、tag 打版本
□ Linux：用户管理、权限(chmod/chown)、进程(ps/top/systemctl)
□ Linux：日志查看(journalctl/tail)、cron 定时任务、磁盘管理(df/du)
□ Linux：进程/线程模型（多进程 vs 多线程 vs 异步，联系 Nginx/Gunicorn）
□ Linux：防火墙(iptables/ufw)、SSH 密钥登录
□ Nginx：反向代理配置、location 匹配规则
□ Nginx：SSL/HTTPS 证书配置（Let's Encrypt）
□ Nginx：负载均衡（upstream）、静态资源缓存
□ 监控：Prometheus 指标采集 + Grafana 仪表盘搭建
□ 日志：Python 结构化日志（logging + JSON 格式），了解 Loki 概念（轻量替代 ELK）
□ ELK Stack 🔷选学：Elasticsearch + Logstash + Kibana 日志收集分析
□ GitHub Actions：workflow 编写、secrets 管理
□ GitHub Actions：自动跑测试、自动构建镜像、自动部署
□ 云服务：购买 ECS、安全组配置、域名解析
```

### 第21周实战项目：一键部署

```
将之前做的博客 API + 后台管理前端，完整部署上线：

1. 后端 FastAPI 用 Docker 打包
2. 前端 Next.js 用 Docker 打包（或静态导出）
3. docker-compose 编排（API + DB + Redis + Nginx）
4. Nginx 反代 API + 前端静态资源
5. 配置 HTTPS（Let's Encrypt 免费证书）
6. GitHub Actions：push 代码自动测试 → 构建镜像 → 部署到服务器
7. 最终效果：浏览器访问 https://你的域名.com 能正常使用
```

### 📅 第19-21周 每日安排

**第19周（Docker + Git 深入）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Docker Day 1：安装、镜像、容器、基本命令 | pull nginx 镜像，跑一个容器，访问默认页 | 2.5h |
| 周二 | Docker Day 2：Dockerfile 编写（FROM/RUN/COPY/CMD） | 把你的 FastAPI 项目打包成 Docker 镜像 | 2.5h |
| 周三 | Docker Day 3：多阶段构建、镜像优化（减少体积） | 优化你的镜像，目标：< 200MB | 2.5h |
| 周四 | Docker Compose Day 1：多容器编排（API + DB + Redis） | docker-compose.yml 编排博客系统的 3 个服务 | 2.5h |
| 周五 | Docker Compose Day 2：卷挂载、网络、环境变量 | 实现数据库数据持久化（volume），服务间通过服务名通信 | 2h |
| 周六 | Git Day 1：分支策略、merge vs rebase、冲突解决 | 模拟一个多人协作场景（自己开两个分支改同一个文件） | 2h |
| 周日 | Git Day 2：cherry-pick、交互式 rebase、tag 打版本 | 整理一段混乱的提交历史，学用 `git reflog` 救命 | 2h |

**第20周（Linux + Nginx）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Linux Day 1：用户/权限（useradd/chmod/chown/sudo） | 创建用户、配置 SSH 密钥登录、禁用密码登录 | 2.5h |
| 周二 | Linux Day 2：进程（ps/top/systemctl）、日志（journalctl） | 部署 FastAPI 到服务器，用 systemd 管理进程 | 2.5h |
| 周三 | Linux Day 3：磁盘（df/du）、cron、防火墙（ufw） | 配置自动备份脚本（cron）+ 打开/关闭端口 | 2h |
| 周四 | Nginx Day 1：反向代理、location 匹配规则 | 配置 Nginx 反代到 FastAPI，理解 upstream | 2.5h |
| 周五 | Nginx Day 2：静态资源服务、gzip、缓存头 | 前端 Next.js 构建后由 Nginx 直接提供静态文件 | 2.5h |
| 周六 | Nginx Day 3 + HTTPS：Let's Encrypt 配置 + HTTPS 原理复习 | 用 certbot 申请免费证书，配置 HTTPS 自动续期 | 3h |
| 周日 | 综合：进程/线程模型实践 | 验证 Nginx 多进程 vs Gunicorn 多进程 vs FastAPI 单进程+异步 | 2h |

**第21周（CI/CD + 监控 + 综合部署）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | GitHub Actions Day 1：workflow 语法、自动跑测试 | 写一个 `.github/workflows/test.yml`，push 自动跑 pytest | 2.5h |
| 周二 | GitHub Actions Day 2：构建 Docker 镜像 + 推送到 Registry | 自动构建镜像 + 推送到 Docker Hub 或阿里云容器镜像服务 | 2.5h |
| 周三 | GitHub Actions Day 3：自动部署到服务器（SSH Deploy） | push → 测试通过 → 构建镜像 → SSH 服务器 → docker-compose up | 2.5h |
| 周四 | 监控 Day 1：Prometheus 指标采集 + 应用指标暴露 | FastAPI 集成 prometheus_client，暴露 `/metrics` 端点 | 2.5h |
| 周五 | 监控 Day 2：Grafana 仪表盘搭建 | 导入 FastAPI 的 Grafana 模板，看 QPS/延迟/错误率 | 2.5h |
| 周六 | Python 结构化日志 + 日志汇聚概念 | 用 `structlog` 输出 JSON 日志，了解 Loki 轻量方案 | 2h |
| 周日 | **一键部署项目 Day 1-2** | 完整部署上线：Docker + Nginx + HTTPS + CI/CD + 监控 | 6h |

### 🚀 详细部署场景演练

**场景 1：首次部署到阿里云 ECS**

```bash
# 第1步：购买 ECS（最低配置：2核2G，CentOS 7.9 或 Ubuntu 22.04）
# 第2步：安全组开放端口：22（SSH）、80（HTTP）、443（HTTPS）

# 第3步：SSH 登录，安装基础环境
ssh root@你的服务器IP

# Ubuntu 示例
apt update && apt install -y docker.io docker-compose nginx certbot python3-certbot-nginx

# 第4步：克隆项目代码
git clone https://github.com/你的用户名/你的项目.git
cd 你的项目

# 第5步：启动服务
docker-compose up -d   # -d 后台运行

# 第6步：验证
docker-compose ps       # 所有服务都是 Up 状态
curl http://localhost:8000/health  # API 健康检查

# 第7步：配置 Nginx（见场景3）
# 第8步：配置 HTTPS（见场景2）
```

**场景 2：HTTPS 证书配置（Let's Encrypt）**

```bash
# 前提：域名已解析到服务器 IP

# 方法1：certbot 自动配置 Nginx
certbot --nginx -d 你的域名.com -d www.你的域名.com
# 自动获取证书、修改 Nginx 配置、设置自动续期

# 方法2：手动配置
certbot certonly --nginx -d 你的域名.com
# 然后在 Nginx 配置里手动引用证书路径：
# ssl_certificate /etc/letsencrypt/live/你的域名.com/fullchain.pem;
# ssl_certificate_key /etc/letsencrypt/live/你的域名.com/privkey.pem;

# 验证自动续期
certbot renew --dry-run
```

**场景 3：Nginx 完整的生产配置模板**

```nginx
# /etc/nginx/sites-available/myapp
server {
    listen 80;
    server_name 你的域名.com;
    return 301 https://$host$request_uri;  # HTTP 强制跳转 HTTPS
}

server {
    listen 443 ssl http2;
    server_name 你的域名.com;

    ssl_certificate     /etc/letsencrypt/live/你的域名.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/你的域名.com/privkey.pem;

    # 安全 Headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # 前端静态资源（Next.js 导出）
    location / {
        root /var/www/frontend;
        try_files $uri $uri/ /index.html;
        expires 7d;
    }

    # API 反向代理
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
    }

    # 静态文件（上传的图片等）
    location /static/ {
        alias /var/www/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # 限制请求速率（防 DDoS）
    limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
    location /api/ {
        limit_req zone=api burst=20 nodelay;
        # ... proxy_pass 配置同上
    }
}
```

### 🔧 部署故障排查手册

| 问题 | 排查命令 | 常见原因 |
|------|---------|---------|
| 网站 502 Bad Gateway | `docker-compose ps` 看 API 是否运行；`docker-compose logs api` 看错误日志 | 后端挂了或端口不对 |
| 静态资源 404 | `ls /var/www/frontend` 确认文件存在；Nginx 的 `root` 指令路径对不对 | 路径配置错误 |
| HTTPS 证书无效 | `certbot certificates` 看证书状态；`openssl s_client -connect 域名:443` 看证书链 | 证书过期或域名不匹配 |
| 数据库连接拒绝 | `docker-compose exec api ping db` 测试网络连通性 | docker-compose 网络没配好，或者 db 没 ready |
| 更新代码后没生效 | `docker-compose build --no-cache api` 重新构建镜像 | 镜像缓存导致用了旧的代码 |
| 磁盘满了 | `df -h` 看磁盘；`docker system prune -a` 清理无用镜像 | Docker 镜像堆积、日志文件过大 |

### 🐛 阶段 6 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **alpine 镜像装不了某些 Python 包** | `pip install` 编译失败 | alpine 用 musl libc 而非 glibc，某些 C 扩展不兼容 | 用 `python:3.x-slim`（Debian 基础），别为了省 50MB 折腾一整天 |
| **docker-compose 里连不上数据库** | `Connection refused` | 数据库容器启动需要时间，API 容器启动时数据库还没 ready | 加 `depends_on` + `healthcheck`，或 API 启动时加重试逻辑 |
| **环境变量没生效** | 代码里读到的值是旧的 | docker-compose 修改了 `environment` 但没重建容器 | 修改环境变量后 `docker-compose up -d --force-recreate` |
| **静态文件 404** | Nginx 配置了但访问不到 | `root` 和 `alias` 搞混了，或者路径末尾少了 `/` | `root /var/www/frontend;` → 拼成 `/var/www/frontend/...` ; `alias /var/www/static/;` → 直接替换匹配到的路径 |
| **.gitignore 漏了 .env** | 数据库密码被推到 GitHub | `.env` 文件没在 `.gitignore` 里 | `.gitignore` 加 `.env`，已在 Git 里的用 `git rm --cached .env` 移除 |
| **docker build 上下文太大** | 构建很慢 | `docker build .` 把整个目录当 build context 发给 Docker daemon | 加 `.dockerignore` 文件，排除 `node_modules/`、`.git/`、`__pycache__/` |

### 📋 阶段 6 完成检查清单 + 自测问题

```
□ Docker
  □ 能独立编写 Dockerfile，理解每一层的含义
  □ 能编写 docker-compose.yml 编排 3+ 个服务
  □ 理解镜像层缓存原理（先 COPY 依赖文件，再 COPY 源码）
  □ 能用多阶段构建减小镜像体积

□ Linux
  □ 能在没有桌面环境的服务器上完成基本操作
  □ 能用 systemd 管理服务（启动/停止/重启/开机自启/看日志）
  □ 理解文件权限和用户/组的关系
  □ 能用 ufw/iptables 管理防火墙规则

□ Nginx
  □ 能写反向代理配置（proxy_pass + proxy_set_header）
  □ 能配置 HTTPS（Let's Encrypt 证书 + 自动续期）
  □ 理解 location 的匹配优先级（精确 > 前缀 > 正则）
  □ 能配置静态资源缓存和 gzip 压缩

□ CI/CD
  □ 能写 GitHub Actions workflow（测试 + 构建 + 部署）
  □ 理解 CI/CD 三阶段：Continuous Integration（自动化测试）→ 
    Continuous Delivery（自动化构建镜像）→ Continuous Deployment（自动化部署）

□ 监控
  □ 能搭建 Prometheus + Grafana 基础监控
  □ 知道 QPS（每秒请求数）、P99 延迟、错误率这几个核心指标
  □ 应用日志输出为 JSON 格式（方便日志系统解析）

□ 实战
  □ [ ] 公网域名能访问你的全栈项目
  □ [ ] HTTPS 证书有效
  □ [ ] Git push → 自动测试 → 自动部署 跑通一次
  □ [ ] Prometheus + Grafana 仪表盘能看到 API 的 QPS

自测问题：
1. Docker 镜像和容器的关系是什么？Dockerfile 的 RUN/COPY/CMD 有什么区别？
2. Nginx 做反代时，为什么需要 proxy_set_header？
3. Let's Encrypt 证书为什么只有 90 天有效期？自动续期怎么实现的？
4. 你 push 代码后，生产环境怎么自动更新的？描述完整链路。
```

### 🎤 阶段 6 面试关联

> DevOps 能力在面试中的定位是「加分项」——中小公司可能不问，中大公司会考察基础。

**高频面试题：**
- "Docker 是怎么实现隔离的？"（Namespace + Cgroups）
- "镜像构建过程中，怎么减小镜像体积？"（多阶段构建、.dockerignore、选 slim 基础镜像）
- "CI/CD 流水线你是怎么设计的？"（画图：push → test → build → deploy）
- "你们线上出问题了怎么排查？"（看监控 → 看日志 → 回滚 → 复盘）

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [Docker 从入门到实践](https://yeasy.gitbook.io/docker_practice/) | 中文 Docker 最好的入门书 | 每天 15min |
| [Pro Git 中文版](https://git-scm.com/book/zh/v2) 第1-3章 | Git 基础和分支 | 每天 10min |
| [Nginx 入门指南](https://nginx.org/en/docs/beginners_guide.html) | 官方入门，很短但信息量大 | 30min 看完 |
| [GitHub Actions 文档](https://docs.github.com/en/actions) | 看 Quickstart + workflow 语法 | 每天 15min |
| [鸟哥的 Linux 私房菜](https://linux.vbird.org/) 第5-7章 | 文件权限与目录配置 | 每天 10min |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| Docker 化你的项目 | 每个项目都写 Dockerfile + docker-compose.yml | 所有项目 |
| 买一台云服务器 | 阿里云/腾讯云最低配（~50元/月），真实环境练习 | 1 台 |
| 配置一次完整的部署 | 从买服务器到 HTTPS 访问，中间不跳过任何步骤 | 至少 1 次 |
| 模拟故障 + 恢复 | 故意 kill 容器、停了 Nginx、删了数据库，练习恢复 | 1 次 |
| 写 GitHub Actions | 至少一个项目有 CI/CD 流水线 | 至少 1 个 |

---

## 🔴 阶段 7：微服务架构（3 周）

> **目标**：理解微服务设计原则，能拆分单体应用，掌握核心中间件
> **检验标准**：将一个单体应用拆分为 2-3 个微服务并正常运行

### 学习清单

| 周数 | 主题 | 资源 | 时间 |
|------|------|------|------|
| 第22周 | **微服务理论**：拆分原则、CAP 理论、服务发现 | [Microservices.io](https://microservices.io/) + [system-design-primer](https://github.com/donnemartin/system-design-primer) | 2天 |
| 第22周 | **消息队列 RabbitMQ**（生产者/消费者/交换机/队列） | [RabbitMQ 官方教程](https://www.rabbitmq.com/tutorials) | 3天 |
| 第23周 | **Celery 异步任务**（与 FastAPI 集成） | [Celery 文档](https://docs.celeryq.dev/) | 2天 |
| 第23周 | **gRPC** 🔷选学（Protocol Buffers + Python 实现） | [gRPC 官方教程](https://grpc.io/docs/languages/python/) | 2天 |
| 第24周 | **API 网关**（Nginx / Kong 概念） | 博客 + 动手 | 1天 |
| 第24周 | **Docker Compose 编排微服务** | 动手实践 | 2天 |
| 第24周 | K8s 入门 🔷选学（Pod/Service/Deployment/Ingress） | [Kubernetes 官方教程](https://kubernetes.io/docs/tutorials/) | 2天 |

### 微服务详细技能清单

```
□ 理解单体 vs 微服务的优缺点
□ 服务拆分原则（按业务领域，不是按技术层）
□ 服务间通信：同步（HTTP）vs 异步（消息队列）
□ RabbitMQ：Direct/Topic/Fanout 交换机
□ RabbitMQ：消息确认、持久化、死信队列
□ Celery：任务定义、调度、重试机制
□ gRPC 🔷选学：.proto 定义、代码生成、四种通信模式
□ 分布式追踪基础（了解 Jaeger/Zipkin）
□ Docker Compose 编排多服务
□ K8s 核心概念 🔷选学（Pod/Deployment/Service/ConfigMap/Secret）
```

### 第24周实战项目：电商微服务拆分

```
将电商系统拆分为 3 个微服务：

服务划分：
├── user-service（用户注册/登录/信息）
├── product-service（商品 CRUD/库存）
└── order-service（下单/支付回调）

通信：
- user-service ↔ order-service：HTTP（REST API）
- order-service ↔ product-service：gRPC（减库存）
- 订单创建后 → 消息队列 → 发邮件通知（异步解耦）

部署：
docker-compose 编排所有服务 + MySQL + Redis + RabbitMQ
```

### 📅 第22-24周 每日安排

**第22周（微服务理论 + RabbitMQ）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | 微服务理论：单体 vs 微服务、拆分原则、CAP 理论 | 画一张「电商系统」拆分为 3 个服务的架构图 | 2.5h |
| 周二 | 服务间通信：同步（REST API）vs 异步（消息队列）对比 | 整理两种通信方式的适用场景对比表 | 2h |
| 周三 | RabbitMQ Day 1：安装、Web 管理界面、基本概念 | 安装 RabbitMQ（Docker），用管理界面创建队列 | 2.5h |
| 周四 | RabbitMQ Day 2：直连交换机（Direct）、工作队列 | Python 写生产者和消费者，发消息+消费 | 2.5h |
| 周五 | RabbitMQ Day 3：Topic/Fanout 交换机、消息确认 | 实现一个「订单创建后发邮件+发短信」的广播场景 | 2.5h |
| 周六 | RabbitMQ Day 4：消息持久化、死信队列、延迟队列 | 实现订单超时自动取消（延迟队列） | 3h |
| 周日 | 复习：画服务通信图（哪些用 HTTP，哪些用 MQ） | — | 2h |

**第23周（Celery + gRPC）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | Celery Day 1：任务定义、Worker 启动、与 FastAPI 集成 | 用 Celery 异步发送邮件验证码 | 2.5h |
| 周二 | Celery Day 2：定时任务（Beat）、任务重试、监控（Flower） | 配置一个每天早上 8 点的数据统计定时任务 | 2.5h |
| 周三 | gRPC 🔷选学 Day 1：Protocol Buffers、.proto 定义 | 定义一个 UserService 的 .proto 文件 | 2.5h |
| 周四 | gRPC 🔷选学 Day 2：Python 客户端/服务端实现、四种通信模式 | 实现 Unary + Server Streaming 两种模式 | 2.5h |
| 周五 | API 网关概念：Nginx 反代 → 路由到不同微服务 | 配置 Nginx 根据 `/api/users` vs `/api/orders` 路由到不同服务 | 2h |
| 周六 | Docker Compose 编排微服务 | docker-compose 编排 3 个 Python 微服务 + MySQL + Redis + RabbitMQ | 3h |
| 周日 | 本周复习 | — | 2h |

**第24周（K8s 入门 + 微服务项目）：**

| 天 | 学习内容 | 练习 | 时间 |
|----|---------|------|------|
| 周一 | K8s 🔷选学：Pod、Deployment、Service、Ingress | minikube 本地搭 K8s，部署一个简单的 FastAPI 应用 | 2.5h |
| 周二 | K8s 🔷选学：ConfigMap、Secret、健康检查（liveness/readiness）| 把环境变量和数据库密码迁移到 ConfigMap/Secret | 2.5h |
| 周三 | 分布式追踪基础：了解 Jaeger/OpenTelemetry 概念 | 在微服务间传递 trace_id，看一次请求跨服务的完整链路 | 2h |
| 周四 | **微服务拆分项目 Day 1** | 拆分用户服务 + 商品服务，实现 HTTP 通信 | 3h |
| 周五 | **微服务拆分项目 Day 2** | 拆分订单服务，实现 RabbitMQ 异步通信 | 3h |
| 周六 | **微服务拆分项目 Day 3** | docker-compose 编排全部服务，端到端测试 | 4h |
| 周日 | 项目收尾，README + 架构图 | 用 draw.io 画一张服务架构图，放到 README | 3h |

### 🌐 服务网格（Service Mesh）概念速览 🔷选学

> 不需要深入，但面试时提到能加分。

```
┌─────────────────────────────────────────────────────┐
│              传统微服务通信                            │
│                                                       │
│  Service A ──HTTP──▶ Service B                        │
│              │                                        │
│              ├── 重试逻辑（A 自己写）                   │
│              ├── 超时设置（A 自己写）                   │
│              └── 熔断降级（A 自己写）                   │
│                                                       │
│  问题：每个服务都要写这些，逻辑散落各处                   │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│              Service Mesh（以 Istio 为例）             │
│                                                       │
│  Service A ──▶ Sidecar Proxy ──▶ Sidecar Proxy ──▶ Service B
│                  (Envoy)            (Envoy)           │
│                                                       │
│  所有流量经过 Sidecar，由它处理：                        │
│  □ 自动重试        □ 超时控制                          │
│  □ 熔断降级        □ 负载均衡                          │
│  □ TLS 加密通信    □ 流量镜像（灰度发布）               │
│  □ 分布式追踪      □ 指标采集（Prometheus）             │
│                                                       │
│  核心概念：把「通信的横切关注点」从业务代码中剥离         │
└─────────────────────────────────────────────────────┘
```

**面试时这么说**："微服务多了之后，服务间通信的可靠性问题变得突出。Service Mesh 通过 Sidecar 模式把重试、熔断、限流这些逻辑从业务代码中抽离出来，由基础设施层统一处理。我们团队规模小时直接用 Nginx + 应用层重试就够了，服务超过 10 个才考虑引入 Istio。"

### 📊 微服务可观测性三大支柱

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│    Logging   │  │   Metrics    │  │   Tracing    │
│    日志       │  │   指标        │  │   链路追踪    │
├──────────────┤  ├──────────────┤  ├──────────────┤
│ 发生了什么     │  │ 量化指标       │  │ 请求怎么走的  │
│ "用户登录失败" │  │ "QPS 下降了30%"│  │ "A→B→C→DB"  │
├──────────────┤  ├──────────────┤  ├──────────────┤
│ 工具：        │  │ 工具：        │  │ 工具：        │
│ structlog    │  │ Prometheus   │  │ Jaeger       │
│ + Loki       │  │ + Grafana    │  │ / Zipkin     │
└──────────────┘  └──────────────┘  └──────────────┘

一个请求出问题时，排查路径：
1. Metrics → 看到 QPS 突降 / P99 延迟飙升（发现异常）
2. Tracing → 找到具体哪个服务调用慢（定位瓶颈）
3. Logging → 看那个服务的错误日志（找到根因）
```

### 🐛 阶段 7 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **消息丢失** | 消费者挂了重启后消息不见了 | 没开消息确认（auto_ack=True） | 手动确认（`auto_ack=False`）+ 消息持久化（`delivery_mode=2`） |
| **消息重复消费** | 同一条消息被处理了两次 | 网络抖动导致确认超时，消息被重新投递 | 消费端实现幂等性（用数据库唯一约束或 Redis 记录已处理的消息 ID） |
| **微服务拆分过细** | 开发效率反而下降 | 拆成了几十个微服务，调试需要同时启动一堆服务 | 按业务领域拆，初期 2-5 个服务就够了，等团队规模上去了再细拆 |
| **分布式事务噩梦** | 下单成功但扣库存失败 | 两个服务各自操作自己的数据库，没有事务保证 | TCC/Saga 模式，或者尽量设计为「最终一致性」而不要追求强一致性 |
| **Celery 任务不执行** | 任务发了但 Worker 没反应 | Worker 没启动，或 Worker 代码没同步更新 | 确认 Worker 运行中，修改任务代码后重启 Worker |

### 📋 阶段 7 完成检查清单 + 自测问题

```
□ 微服务理论
  □ 能解释单体应用和微服务的各自优缺点
  □ 知道何时不应该用微服务（团队小/业务简单/基础设施弱）
  □ 能说出服务拆分的核心原则：按业务领域，不按技术层

□ 消息队列
  □ 能解释为什么需要消息队列（削峰/解耦/异步）
  □ 能区分 Direct/Topic/Fanout 交换机的使用场景
  □ 知道如何处理消息丢失和重复消费

□ Celery
  □ 能在 FastAPI 中集成 Celery 做异步任务
  □ 能配置定时任务和任务重试

□ 实战
  □ [ ] 3 个微服务能独立运行并互相通信
  □ [ ] 至少一个场景使用了消息队列异步通信
  □ [ ] docker-compose 一键启动所有服务
  □ [ ] README 中有架构图（用 draw.io 或 Mermaid 画）

自测问题：
1. 什么时候该用微服务？什么时候不该用？（至少各说 2 条）
2. 微服务间怎么保证数据一致性？（最终一致性 vs 强一致性）
3. RabbitMQ 怎么保证消息不丢？（生产者确认 + 持久化 + 消费者手动确认）
4. 分布式追踪 Trace ID 是怎么传递的？（Header 注入 + 提取）
```

### 🎤 阶段 7 面试关联

> 微服务在面试中的考察取决于目标公司——中小公司不一定会问，中大公司会问基础原理。

**高频面试题：**
- "你们微服务怎么拆的？按什么原则拆的？"（必问！重点讲「为什么这么拆」）
- "服务间通信选 HTTP 还是 RPC？为什么？"
- "RabbitMQ 和 Kafka 的区别？各自适合什么场景？"
- "分布式事务怎么处理？"（TCC / Saga / 本地消息表 / 最终一致性）

**回答技巧**：不要只回答「我们用了 RabbitMQ」，而要解释「为什么订单创建后发邮件不用 HTTP 同步调用，而用 MQ 异步解耦」。

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [Microservices.io](https://microservices.io/patterns/) 的前 5 个模式 | 核心的微服务设计模式 | 每天 20min |
| [RabbitMQ 官方教程](https://www.rabbitmq.com/tutorials) 的 1-4 教程 | Python 版，手机看概念 | 每天 15min |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) 的 README | 系统设计入门，通勤时浏览 | 碎片时间 |
| 《数据密集型应用系统设计》(DDIA) 第 4 章 | 编码与演化 | 每天 15min |
| [Celery 官方文档](https://docs.celeryq.dev/) Getting Started | 手机看概念，电脑动手 | 每天 10min |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| 拆分练习 | 把一个单体项目拆成 2-3 个服务，感受拆分的代价和收益 | 1 次 |
| RabbitMQ 动手 | 实现 Pub/Sub、RPC、延迟队列三种模式 | 3 个场景 |
| 模拟故障 | 关掉一个微服务，观察另一个服务的表现（超时？报错？降级？） | 1 次 |
| 画架构图 | 用 draw.io 画一个微服务架构图，标注通信方式和数据流向 | 至少 1 张 |

---

## 🟢 阶段 8：全栈项目实战（4 周）

> **目标**：GitHub 上有 3 个能拿出手的全栈项目
> **检验标准**：代码结构清晰、有测试、有 README、能一键 Docker 部署

### 项目 1：在线博客/内容平台（第25周）

```
难度：⭐⭐
周期：1 周（复习性项目，把之前的博客 API + 前端完善）

技术栈：FastAPI + React + TypeScript + PostgreSQL + Redis + Docker
基础功能：
- Markdown 编辑器
- 标签/分类体系
- RSS 订阅
- 访问统计
- GitHub Actions CI/CD 自动部署

★ 深度亮点（至少做 1 个）：
□ 全文搜索方案对比：分别用 LIKE、PostgreSQL tsvector、Elasticsearch
   实现搜索，对比性能差异（QPS/延迟/准确率），写一篇技术博客记录
□ 集成测试 + E2E 测试：pytest 测 API 全链路，Playwright 模拟用户
   登录→写文章→发布→搜索→阅读全流程
```

### 项目 2：企业级后台管理系统（第26周）

```
难度：⭐⭐⭐
周期：1 周

技术栈：FastAPI + Next.js + TypeScript + Ant Design + PostgreSQL + Redis
基础功能：
- RBAC 权限管理（用户/角色/权限 三表）
- 动态路由（根据权限显示菜单）
- 数据导入导出（Excel/CSV）
- 操作日志审计
- 数据看板（ECharts 图表）
- 响应式布局

★ 深度亮点（至少做 1 个）：
□ 设计模式实践：在项目中应用至少 2 种模式，在 README 中说明
   "为什么这里用策略模式而不是 if-else"，附带前后对比代码
□ 权限模型进阶：实现数据权限（同级只能看自己部门数据），
   不止页面权限。这是面试时区分"做过项目"和"理解权限"的关键
```

### 项目 3：电商/在线交易平台（第27-28周）

```
难度：⭐⭐⭐⭐
周期：2 周

技术栈：FastAPI 微服务 + Next.js + TypeScript + PostgreSQL + Redis + RabbitMQ + Docker
基础功能：
- 商品搜索（Elasticsearch 或 PostgreSQL 全文搜索）
- 购物车（Redis 实现）
- 订单系统
- 支付集成（支付宝/微信支付沙箱）
- 秒杀场景（Redis + 消息队列削峰）
- WebSocket 实时通知
- 压力测试（Locust / wrk）

★ 深度亮点（至少做 2 个）：
□ 分布式事务方案对比：下单扣库存场景，分别用 TCC（Try-Confirm-Cancel）
   和 Saga 模式实现，对比事务成功率/回滚复杂度，记录选择理由
□ 秒杀深度优化：用 Redis 预扣库存 → 消息队列异步下单，
   对比直连 MySQL 方案的 QPS 差距，画出架构对比图
□ E2E 测试：Playwright 录制用户完整购买流程（浏览→加购→下单→支付），
   自动回归测试
```

### 每个项目的完成标准

```
□ 代码托管 GitHub，README 完整（项目介绍/技术栈/如何运行/API 文档截图）
□ 前后端分离，独立仓库或 monorepo
□ 后端有单元测试（pytest），覆盖率 > 60%
□ 后端有集成测试（测试 API 全链路：请求→中间件→数据库→响应）
□ 关键业务流程有 E2E 测试（Playwright，至少 2 个核心场景）
□ Docker Compose 一键启动
□ API 文档自动生成（Swagger）
□ 前端有 Loading/Empty/Error 状态处理
□ 至少处理了 3 种异常场景
□ README 中有"技术亮点"章节（写清楚你在这个项目中深入解决了什么问题）
```

### 📅 第25-28周 每日安排

**第25周（项目1：博客平台）：**

| 天 | 任务 | 重点 |
|----|------|------|
| 周一 | 项目初始化：仓库创建、FastAPI 项目结构搭建、数据库模型设计 | 分层架构（api/services/models） |
| 周二 | 后端 API 完善：用户认证（JWT）+ 文章 CRUD + 评论 | 完善异常处理（统一 ErrorResponse 格式） |
| 周三 | 后端深度功能：Markdown 渲染、标签/分类、RSS 订阅 | 集成 python-markdown 库 |
| 周四 | 前端搭建：Next.js 项目 + 文章列表/详情页 + Markdown 编辑器 | 对接后端 API |
| 周五 | 深度亮点 1：搜索方案对比 | 实现 LIKE → PostgreSQL tsvector → Elasticsearch 三种搜索，压测对比 |
| 周六 | 深度亮点 2：E2E 测试 | Playwright 录制完整用户流程 |
| 周日 | 收尾：README 编写（含技术亮点章节）、Docker 部署验证、推 GitHub | README 截图 + 架构图 |

**第26周（项目2：后台管理系统）：**

| 天 | 任务 | 重点 |
|----|------|------|
| 周一 | 项目初始化：RBAC 权限模型设计（用户/角色/权限三表 + 中间表） | 权限表和关系设计是关键 |
| 周二 | 后端：认证 + RBAC 中间件 + 动态菜单 API | 根据用户角色返回不同的菜单树 |
| 周三 | 前端：Ant Design Pro 布局 + 动态路由生成 | 前端根据权限隐藏/显示菜单 |
| 周四 | 数据导入导出（Excel/CSV）+ 操作日志 | openpyxl 导出 + 中间件记录操作 |
| 周五 | 数据看板（ECharts：折线图 + 饼图 + 柱状图） | 后端提供聚合统计 API |
| 周六 | 深度亮点 1：设计模式实践 | 策略模式做导出（Excel vs CSV vs PDF），README 中写前后对比 |
| 周日 | 深度亮点 2：数据权限 | 部门管理员只能看自己部门数据（SQL 层面拦截） |

**第27周（项目3：电商平台 Part 1）：**

| 天 | 任务 | 重点 |
|----|------|------|
| 周一 | 微服务脚手架：3 个服务（user/product/order）的项目结构 | 统一的 Dockerfile 和配置管理 |
| 周二 | user-service + product-service 基础 CRUD | 每个服务独立数据库 |
| 周三 | 商品搜索：PostgreSQL 全文搜索 + Redis 缓存 | GIN 索引 + tsvector |
| 周四 | 购物车：Redis Hash 实现（用户ID → {商品ID: 数量}） | Redis 数据结构选型 |
| 周五 | 订单系统：创建订单 + 减库存（分布式事务第一版：直接调用） | 发现问题：网络抖动导致不一致 |
| 周六 | 深度亮点 1：分布式事务 TCC 实现 | Try（预留）→ Confirm（确认）→ Cancel（回滚） |
| 周日 | 消息队列集成：订单创建 → RabbitMQ → 发邮件 + 减库存（异步） | 对比同步和异步两种方式的代码 |

**第28周（项目3：电商平台 Part 2）：**

| 天 | 任务 | 重点 |
|----|------|------|
| 周一 | 支付集成：支付宝沙箱/微信支付沙箱 | 签名验证、回调处理 |
| 周二 | 秒杀系统基础版：Redis 预扣库存 + MQ 异步下单 | Lua 脚本保证原子性 |
| 周三 | 深度亮点 2：秒杀压测对比 | Locust 模拟 1000 并发，对比优化前后 QPS |
| 周四 | WebSocket 实时通知：支付成功推送 | FastAPI WebSocket + 前端连接管理 |
| 周五 | docker-compose 编排全部微服务 | 一键启动 6+ 个容器 |
| 周六 | E2E 测试：Playwright 录制购买全流程 | 浏览→加购→下单→支付 |
| 周日 | 项目收尾：README（含架构图、技术亮点、压测对比图）、推 GitHub | 这是你的面试王牌 |

### 🏗️ 项目 1 详细实现指导：博客平台

**数据库设计（项目1的重点是搜索方案对比）：**

```sql
-- 文章表
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    author_id INT NOT NULL REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    content TEXT NOT NULL,
    content_vector tsvector,  -- PostgreSQL 全文搜索字段
    status VARCHAR(20) DEFAULT 'draft',
    view_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 为全文搜索创建 GIN 索引
CREATE INDEX idx_articles_content_vector ON articles USING GIN(content_vector);

-- 自动更新 tsvector（触发器）
CREATE TRIGGER trg_articles_vector 
BEFORE INSERT OR UPDATE ON articles
FOR EACH ROW EXECUTE FUNCTION
tsvector_update_trigger(content_vector, 'pg_catalog.simple', content);
```

**搜索实现对比（面试时的技术亮点素材）：**

```python
# 方案1：LIKE 模糊匹配（最差）
SELECT * FROM articles WHERE title LIKE '%关键词%' OR content LIKE '%关键词%';
# 问题：全表扫描，中文分词不支持，准确率低

# 方案2：PostgreSQL tsvector（中等，推荐先用这个）
SELECT *, ts_rank(content_vector, query) AS rank
FROM articles, plainto_tsquery('simple', '关键词') AS query
WHERE content_vector @@ query
ORDER BY rank DESC;
# 优点：数据库自带，无需额外组件，支持中文分词（需安装 zhparser 扩展）
# 缺点：大数据量（千万级）时性能下降

# 方案3：Elasticsearch（最优，但运维成本高）
# 优点：分布式搜索、高亮、聚合分析、模糊纠错
# 缺点：需要额外部署 ES 集群，数据同步（Logstash/Canal）
```

**README 技术亮点章节模板（项目1）：**

> ## 技术亮点
> 
> ### 1. 全文搜索方案选型与性能对比
> 
> 为博客的搜索功能，我分别用三种方案实现并进行了性能测试（2000 篇文章）：
> 
> | 方案 | 平均响应时间 | QPS | 中文分词准确率 | 运维成本 |
> |------|------------|-----|--------------|---------|
> | LIKE | 850ms | 12 | 低 | 无 |
> | PostgreSQL tsvector | 45ms | 220 | 中（需 zhparser） | 低 |
> | Elasticsearch | 8ms | 1200 | 高 | 高（独立集群） |
> 
> **选择理由**：初期数据量小（< 10 万篇），选择 PostgreSQL tsvector 方案，零额外运维成本。当数据量增长后，预留了迁移到 ES 的接口（搜索服务抽离为独立模块）。
> 
> ### 2. 全链路 E2E 测试
> 
> 使用 Playwright 模拟真实用户操作：登录 → 写文章(Markdown) → 发布 → 搜索 → 阅读。每次 PR 自动运行，保证核心流程不被破坏。

### 🏗️ 项目 2 详细实现指导：后台管理系统

**RBAC 数据库设计（用户-角色-权限 经典五表）：**

```sql
-- 用户表
CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE, ...);

-- 角色表
CREATE TABLE roles (id SERIAL PRIMARY KEY, name VARCHAR(50) UNIQUE, description TEXT);
-- 预设角色：admin（超级管理员）、editor（编辑）、viewer（只读）

-- 权限表
CREATE TABLE permissions (id SERIAL PRIMARY KEY, code VARCHAR(100) UNIQUE, name VARCHAR(100));
-- 预设权限：article:create, article:edit, article:delete, user:manage, system:config

-- 用户-角色关联表（多对多）
CREATE TABLE user_roles (
    user_id INT REFERENCES users(id),
    role_id INT REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);

-- 角色-权限关联表（多对多）
CREATE TABLE role_permissions (
    role_id INT REFERENCES roles(id),
    permission_id INT REFERENCES permissions(id),
    PRIMARY KEY (role_id, permission_id)
);
```

**数据权限实现（项目2的深度亮点）：**

```python
# 需求：部门经理只能看到本部门的数据
# 实现：在 SQL 查询层面自动注入部门过滤条件

# 不好的做法：在路由里手动加过滤
@app.get("/orders")
async def get_orders(current_user = Depends(get_current_user)):
    if current_user.role == "dept_manager":
        orders = db.query(Order).filter(Order.dept_id == current_user.dept_id).all()
    else:
        orders = db.query(Order).all()

# 好的做法：SQLAlchemy 事件拦截（对业务代码透明）
from sqlalchemy import event

class DeptFilterQuery:
    """自动为查询添加部门过滤"""
    def __init__(self, user):
        self.user = user
    
    def apply(self, query, model):
        if hasattr(model, 'dept_id') and self.user.role == 'dept_manager':
            return query.filter(model.dept_id == self.user.dept_id)
        return query

# 使用时：
orders = dept_filter.apply(db.query(Order), Order).all()
# 业务代码不知道数据权限的存在，但查询结果已被过滤
```

### 🏗️ 项目 3 详细实现指导：电商平台

**购物车 Redis 数据结构设计：**

```python
# Hash: cart:{user_id} → {product_id: quantity}
# Key: cart:1001
# Fields: { "101": "2", "205": "1", "309": "3" }
# 含义：用户 1001 的购物车里有 商品 101 ×2、205 ×1、309 ×3

import redis
r = redis.Redis()

# 添加商品
def add_to_cart(user_id: int, product_id: int, quantity: int = 1):
    r.hincrby(f"cart:{user_id}", str(product_id), quantity)

# 查看购物车
def get_cart(user_id: int) -> dict:
    cart = r.hgetall(f"cart:{user_id}")
    return {int(k): int(v) for k, v in cart.items()}

# 删除商品
def remove_from_cart(user_id: int, product_id: int):
    r.hdel(f"cart:{user_id}", str(product_id))
```

**秒杀系统简化实现（面试重点）：**

```python
# 核心思路：Redis 预扣库存 → 消息队列异步下单
# 瓶颈在 MySQL 写入，不在 Redis

import redis
import json

r = redis.Redis()

# 1. 活动开始前：预热库存到 Redis
r.set("seckill:stock:product_123", 100)  # 100 件秒杀商品

# 2. 秒杀接口（FastAPI）
@app.post("/seckill/{product_id}")
async def seckill(product_id: str, current_user = Depends(get_current_user)):
    # 用 Lua 脚本保证「判断库存 + 扣减」的原子性
    lua_script = """
    local key = KEYS[1]
    local stock = tonumber(redis.call('get', key))
    if stock and stock > 0 then
        redis.call('decr', key)
        return 1
    else
        return 0
    end
    """
    result = r.eval(lua_script, 1, f"seckill:stock:{product_id}")
    
    if result == 0:
        raise HTTPException(400, "已抢光")
    
    # 3. 发送到 MQ，异步创建订单（削峰）
    channel.basic_publish(
        exchange='seckill',
        routing_key='order.create',
        body=json.dumps({"user_id": current_user.id, "product_id": product_id})
    )
    
    return {"message": "抢购成功，订单处理中"}
```

**压测对比（README 中放这张表，面试官会眼睛一亮）：**

| 方案 | QPS | 平均延迟 | 超卖情况 | MySQL 压力 |
|------|-----|---------|---------|-----------|
| 直连 MySQL（无优化） | 150 | 600ms | 严重（超卖 23 件） | CPU 100% |
| MySQL + 悲观锁（SELECT FOR UPDATE） | 80 | 1200ms | 无超卖 | CPU 100% |
| Redis 预扣 + MQ 异步 | 5000 | 8ms | 无超卖 | CPU 20% |

### 🐛 阶段 8 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **大项目开头难** | 面对空白项目不知道从哪开始 | 没有分解任务 | 先建数据库模型（最确定的部分），再写 API，最后写前端 |
| **README 写成流水账** | 面试官看了一眼就跳过 | 只写了「使用了 FastAPI + React」，没写「为什么这么选」「解决了什么问题」 | README 必须有：技术选型理由 + 架构图 + 性能对比 + 踩坑记录 |
| **搜索直接用 LIKE** | 搜索 3 秒才返回结果 | 没建索引，全表扫描 | 至少用 PostgreSQL tsvector，做成一个对比实验就是技术亮点 |
| **Redis 和 MySQL 数据不一致** | 缓存里的文章列表和数据库里的不一样 | 更新数据库后没同步更新缓存 | Cache Aside 模式：先更新 DB，再删除缓存（而不是更新缓存） |
| **提交信息全是 "update"** | commit log 像垃圾堆 | 没有写有意义的 commit message | 用约定式提交：`feat: 添加全文搜索` `fix: 修复分页偏移错误` `perf: 购物车 Redis 优化` |

### 📋 阶段 8 完成检查清单 + 自测问题

```
□ 项目1（博客）
  □ [ ] Markdown 编辑器可用
  □ [ ] 搜索功能实现（至少有 LIKE 和 tsvector 两种方式）
  □ [ ] 有 E2E 测试（Playwright 录制）
  □ [ ] README 中有「搜索方案对比」的技术亮点章节

□ 项目2（后台管理）
  □ [ ] RBAC 权限（用户/角色/权限 三表设计正确）
  □ [ ] 动态路由（不同角色看到不同菜单）
  □ [ ] 数据导入导出可用
  □ [ ] README 中有「设计模式实践」或「数据权限」的技术亮点

□ 项目3（电商）
  □ [ ] 购物车用 Redis 实现
  □ [ ] 订单创建是异步的（MQ）
  □ [ ] 秒杀方案有 Redis 预扣库存
  □ [ ] 有压力测试对比数据
  □ [ ] README 中有架构图 + 压测对比表

□ 通用标准
  □ [ ] 每个项目有完整的 README（项目介绍/技术栈/如何运行/API 截图/架构图/技术亮点）
  □ [ ] 每个项目有 Dockerfile + docker-compose.yml
  □ [ ] 每个项目有单元测试（pytest）+ 集成测试
  □ [ ] GitHub 绿墙连续 4 周有提交

自测问题：
1. 如果让你技术支持一个新入职的同事运行你的项目，他能在 10 分钟内跑起来吗？（Docker 一键启动）
2. 你的三个项目中，哪一个「技术深度」最深？你能围绕它讲 10 分钟吗？
3. 你对每个项目的技术选型都能说出理由吗？（为什么用 FastAPI 而不是 Django？为什么用 Redis 存购物车而不是 MySQL？）
```

### 🎤 阶段 8 面试关联

> 项目是面试的"主战场"——前 10 分钟自我介绍讲项目，表现好就已经赢了 50%。

**面试官必问：**
- "你最有挑战的项目是哪个？你遇到了什么问题，怎么解决的？"
- "你为什么选择这个技术栈？有没有考虑过其他方案？"
- "你的项目如果用户量增长 10 倍，哪些地方会出问题？你打算怎么优化？"

**STAR 法则准备每个项目：**
- **S**ituation：这个项目要解决什么问题？（1 句）
- **T**ask：你的角色和任务是什么？（1 句）
- **A**ction：你具体做了什么？怎么做的？（核心，3-4 句，突出技术决策）
- **R**esult：成果是什么？学到了什么？（性能提升多少、解决了什么痛点）

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|------|
| 别人的 GitHub 项目 README | 搜索 "fastapi react blog"，看高星项目的 README 怎么写的 | 碎片时间 |
| [system-design-primer](https://github.com/donnemartin/system-design-primer) 的案例 | 看短链接/秒杀/消息推送的设计 | 每天 1 个案例 |
| [阿里巴巴 Java 开发手册](https://github.com/alibaba/p3c) | 虽然是 Java 的，但设计思想和规范通用 | 每天 10min |
| 《数据密集型应用系统设计》(DDIA) 第 5-7 章 | 复制、分区、事务 | 每天 15min |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| 写 README | 先写 README 再写代码（README-driven development） | 每个项目 |
| 画架构图 | 用 draw.io 或 Excalidraw 画项目架构图，放到 README | 每个项目 |
| 压测 | 用 wrk/Locust 压自己的 API，找到瓶颈并优化 | 至少 1 个 |
| 代码评审 | 完成一个功能后，自己在 GitHub 上提一个 PR，自己 review 自己的代码 | 每个功能 |
| 写技术博客 | 把项目中深入研究的点写成博客（搜索方案对比、秒杀优化、RBAC 设计等），面试时直接发给面试官 | 3 篇 |

---

## 🔵 阶段 9：面试准备（持续 + 最后冲刺 2 周）

> **目标**：通过大厂/中厂 Python 全栈面试
> **检验标准**：模拟面试能答出 80% 的问题

### 十大面试模块

| 模块 | 核心内容 | 资源 |
|------|---------|------|
| **1. Python 基础** | GIL/装饰器/生成器/上下文管理器/内存管理/深浅拷贝/可变不可变 | Python-100-Days Day99 + [Python 面试题合集](https://github.com/taizilongxu/interview_python) |
| **2. 数据库** | 索引原理/最左前缀/慢查询优化/事务隔离级别/MVCC/分库分表 | Day93 + [MySQL 面试题](https://github.com/0voice/interview_internal_reference) |
| **3. 网络** | TCP/UDP/HTTP/HTTPS/DNS/CDN/WebSocket/跨域/HTTP2/TCP拥塞控制 | 阶段2+6 所学内容复习 |
| **4. 操作系统** | 进程/线程/协程、IO模型（阻塞/非阻塞/多路复用）、内存管理、文件系统 | [CS-Notes](http://www.cyc2018.xyz/) + 阶段6 Linux 实践联系 |
| **5. Redis** | 数据结构/持久化/集群/缓存问题/分布式锁 | [Redis 面试题](https://github.com/CyC2018/CS-Notes/blob/master/notes/Redis.md) |
| **6. 后端框架** | FastAPI 原理/中间件/依赖注入/ASGI/ORM N+1 问题 | 官方文档 + 源码阅读 |
| **7. 前端** | React 原理（Virtual DOM/Fiber/Hooks）/Next.js SSR/TS 类型体操入门 | React 源码解析博客 + TS 文档 |
| **8. 系统设计** | 短链接/秒杀/消息推送/IM/排行榜/限流 | [system-design-primer](https://github.com/donnemartin/system-design-primer) |
| **9. 算法** | 数组/链表/栈/队列/树/排序/动态规划 | LeetCode 高频 100 题 |
| **10. 软技能** | 项目阐述（STAR法则）/技术选型理由/设计模式场景/团队协作/代码评审 | 自己整理 + 模拟面试 |

### 面试准备时间线

```
阶段1到阶段7期间：
  - 每天 1 道 LeetCode 算法题（保持手感）
  - 每天 1 道 SQL 题
  - 每周复习一个面试模块

阶段9最后冲刺（项目做完后 2 周）：
  - 系统设计：每天 1 个设计题（口头 + 画图练习）
  - 算法：回顾已刷的题，重点看做过的难题
  - 项目：整理 STAR 描述（每个项目 3-5 分钟讲清楚）
  - 软技能：整理技术选型理由、设计模式应用场景、团队协作案例
   - 模拟面试：找朋友或 AI 模拟 3-5 次（包含行为面试环节）
```

### 🎯 模拟面试题库 + 答案框架

#### Python 基础（必问 3 题）

**1. "Python 的 GIL 是什么？多线程在 Python 中有什么用？"**

> 答案框架：
> GIL（Global Interpreter Lock，全局解释器锁）是 CPython 的一个机制，它保证同一时刻只有一个线程在执行 Python 字节码。这导致 Python 多线程无法利用多核 CPU 做真正的并行计算。
> 
> 但多线程在 Python 中并非无用：
> - **IO 密集型任务**（网络请求、文件读写）：线程在等待 IO 时 GIL 会释放，其他线程可以运行，所以多线程对 IO 密集型有效。
> - **CPU 密集型任务**：应该用 `multiprocessing`（多进程）来绕过 GIL。
> - 我做过一个对比实验：用 10 个线程并发下载 100 个 URL，比串行快了约 8 倍。
>
> 追问：那 asyncio 和 threading 有什么区别？
> → asyncio 是单线程内的协程调度，适合 IO 密集型且连接数很大（>1000）的场景；threading 是操作系统级线程切换，开销更大。我在 FastAPI 项目中统一用 asyncio + httpx.AsyncClient。

**2. "装饰器的原理是什么？写一个带参数的装饰器"**

> 答案框架：
> 装饰器本质是一个接受函数作为参数、返回新函数的高阶函数。Python 的 `@decorator` 语法糖等价于 `func = decorator(func)`。
> 
> 我在项目中用装饰器做了：
> - 计时器：`@timer` 自动记录函数执行时间
> - 重试：`@retry(max=3, delay=1)` 处理临时性的网络错误
> - 权限校验：`@require_permission("article:edit")` 在 FastAPI 路由上做 RBAC
>
> 白板写代码：
> ```python
> def retry(max_attempts=3, delay=1):
>     def decorator(func):
>         def wrapper(*args, **kwargs):
>             for i in range(max_attempts):
>                 try:
>                     return func(*args, **kwargs)
>                 except Exception as e:
>                     if i == max_attempts - 1:
>                         raise
>                     time.sleep(delay)
>         return wrapper
>     return decorator
> ```

**3. "Python 的 `__new__` 和 `__init__` 有什么区别？"**

> 答案框架：
> `__new__` 创建实例（分配内存），`__init__` 初始化实例（设置属性）。`__new__` 先于 `__init__` 执行。
> 
> 实际中用到的场景：
> - **单例模式**：在 `__new__` 里控制只创建一个实例
> - **继承不可变类型**：如 `class UpperStr(str): def __new__(cls, value): return super().__new__(cls, value.upper())`
> 
> 我在项目中的配置管理用了模块级单例（Python 模块天然单例），比覆写 `__new__` 更 Pythonic。

#### 数据库（必问 3 题）

**4. "MySQL 索引底层为什么用 B+ 树？"**

> 答案框架：
> B+ 树相比其他数据结构的优势在于适合磁盘 IO：
> 1. **高度低**：百万级数据 B+ 树只有 3-4 层，查找只需 3-4 次磁盘 IO
> 2. **叶子节点有序链表**：范围查询非常高效（比如 `WHERE id BETWEEN 1000 AND 2000`）
> 3. **数据都在叶子节点**：查询任何数据 IO 次数稳定
> 
> 对比：
> - 红黑树：高度高（百万数据 ~20 层），磁盘 IO 多
> - Hash：不支持范围查询，且 Hash 冲突时退化为链表
> - B 树：非叶子节点也存数据，非叶子节点存储的索引条目更少，树更高
>
> 我在项目中设计索引时，会先用 EXPLAIN 看 type 和 rows，确保至少达到 ref 级别。

**5. "慢查询怎么定位和优化？"**

> 答案框架（全链路）：
> 1. **定位**：开启慢查询日志（`long_query_time=0.1`），或通过监控（Prometheus+Grafana）发现 QPS 下降
> 2. **分析**：`EXPLAIN SELECT ...` 看 type（ALL/index/ref）、rows、Extra（Using filesort/Using temporary）
> 3. **优化**（按优先级）：
>    - 加合适的索引（最左前缀原则）
>    - 减少 `SELECT *`，只查需要的列（覆盖索引）
>    - 避免在 WHERE 条件左边用函数（`WHERE YEAR(date)=2024` → `WHERE date BETWEEN ...`）
>    - 大表做分区（按时间分区）
>    - 如果是统计需求，用汇总表
>    - 如果是高并发读，加 Redis 缓存
>
> 我在图书管理项目中做过一次优化：把 `WHERE status=1 ORDER BY created_at` 的查询从 2.3s 优化到 15ms，方法是建了 `(status, created_at)` 联合索引。

**6. "什么是事务隔离级别？MySQL 默认是什么？"**

> 答案框架：
> 四个隔离级别：读未提交 → 读已提交 → 可重复读 → 串行化（隔离性递增，性能递减）。
> 
> MySQL InnoDB 默认是**可重复读**（REPEATABLE READ），通过 MVCC（多版本并发控制）实现。
> 
> 常见问题：
> - 脏读（Dirty Read）：读到未提交的数据 — 可重复读已解决
> - 不可重复读：同一事务两次读结果不同 — 可重复读已解决
> - 幻读：同一事务两次范围查询结果集不同 — MySQL 用 Next-Key Lock（间隙锁）部分解决
>
> 我在电商项目中，订单创建和库存扣减需要在同一个事务中，用了 `SERIALIZABLE` 隔离级别（或用 SELECT FOR UPDATE 悲观锁）。

#### 系统设计（中等公司常考 2 题）

**7. "设计一个短链接系统（如 t.cn）"**

> 答案框架（分步展开）：
> 1. **核心流程**：长 URL → 生成唯一短码 → 存储映射 → 短链接访问时 301 跳转
> 2. **短码生成**：Base62 编码（0-9a-zA-Z）。用发号器预生成 ID，然后 Base62 编码。比如 ID=100000 → Base62 → "q0U"
> 3. **存储**：MySQL 存 `(id, short_code, long_url, created_at, expire_at)`，short_code 加唯一索引
> 4. **高并发优化**：Redis 缓存热点短链接的映射，Bloom Filter 快速判断短码是否存在
> 5. **扩展**：发号器可以用 Snowflake 分布式 ID；数据分片按 short_code 哈希
>
> 画图：用户 → API → 发号器 → Base62编码 → MySQL → 返回短链接

**8. "设计一个秒杀系统"**

> 答案框架：
> 秒杀的核心矛盾：**瞬时极高并发 vs 有限库存**。
> 
> 优化路径（分层解耦）：
> 1. **前端**：按钮置灰、倒计时、验证码（分散用户点击时间）
> 2. **网关层**：Nginx 限流（limit_req），直接拒绝超出容量的请求
> 3. **应用层**：Redis 预扣库存 + Lua 脚本保证原子性（核心）
> 4. **异步化**：扣库存成功后发 MQ → 异步创建订单（削峰填谷）
> 5. **数据库**：最终同步 Redis 的扣减结果到 MySQL
> 
> 我的项目中对比了三种方案：直连 MySQL（QPS 150）、MySQL+悲观锁（QPS 80）、Redis+MQ（QPS 5000），优化了 33 倍。这里面最关键的是把「同步写 MySQL」变成了「先 Redis 扣库存 + 异步写 MySQL」。

#### 项目阐述（STAR 法则）

**9. "介绍一个你觉得最有挑战的项目"**

> STAR 答案框架：
>
> **S**（背景）：我做的电商平台的秒杀功能，需要支持 1000 人同时抢 100 件商品。
>
> **T**（任务）：我是这个功能的负责人，需要保证不超卖、系统不崩溃、用户体验好。
>
> **A**（行动 —— 这是重点，讲 3-4 个具体决策）：
> - 第一版用 MySQL `SELECT FOR UPDATE` 悲观锁，压测 QPS 只有 80，不满足要求
> - 改用 Redis 预扣库存：秒杀开始前把库存预热到 Redis，用 Lua 脚本保证「判断+扣减」原子性
> - 扣库存成功后不直接写数据库，而是发到 RabbitMQ，由消费者异步创建订单，QPS 提升到 5000
> - 前端加了倒计时和验证码，把瞬时并发从 2000 降到 500
>
> **R**（结果）：QPS 从 150 提升到 5000，没有超卖。最大的收获是理解了「缓存 + 异步消峰」在处理高并发场景中的重要性。

#### 软技能

**10. "你为什么选择 FastAPI 而不是 Django？"**

> 答案框架：
> 每个技术选型都要结合**具体场景**来说，不存在绝对的好坏。
> 
> 我的项目是 API 服务（博客后台、电商微服务），需要：
> - 高性能异步（FastAPI 基于 Starlette + asyncio）
> - 自动 API 文档（Swagger 自动生成，前后端协作方便）
> - 类型安全（Pydantic 校验 + TypeScript 前端类型打通）
> 
> Django 更适合「内容管理系统」「后台管理」这类需要快速出页面的场景（Admin 后台开箱即用）。
> 我的后台管理前端用的是 Next.js + Ant Design，不需要 Django 的模板系统，所以选 FastAPI。
> 
> **核心原则**：选择适合项目需求的技术，不是选「最新的」或「最流行的」。

### 🐛 阶段 9 常见踩坑记录

| 坑 | 现象 | 原因 | 解决 |
|----|------|------|------|
| **自我介绍像背简历** | 面试官低头看手机 | 只是罗列年龄/学历/公司，没有亮点 | 30 秒版：我叫 XX，3 年 Python 经验，擅长 FastAPI 和数据库优化，最近做了一套微服务电商系统。面试官想听的是"我能干什么" |
| **项目讲成流水账** | 面试官追问：你在这个项目中的角色是什么？ | 讲了"我们用了 XX 技术"，但没说"我做了什么技术决策" | STAR 法则，重点讲 Action——你做的那部分 |
| **不知道就说不知道** | 强行瞎编，被追问露馅 | 怕显得自己不懂 | 说"这个我不太了解，但我了解一个类似的..."，把话题拉回你熟悉的范围 |
| **算法题写了但跑不通** | 代码有 bug 但没发现 | 紧张 + 没养成自测习惯 | 写完代码后，口头跑一个简单测试用例（input → 每一步的值 → output） |
| **反问环节问工资** | 面试官沉默 | 技术面问薪资太早 | 技术面反问：团队技术栈、项目流程、技术挑战。HR 面再谈薪资 |

### 📋 阶段 9 完成检查清单 + 自测问题

```
□ 算法
  □ [ ] LeetCode 高频 100 题独立完成（重点：数组/链表/树/DP）
  □ [ ] 每道题能口头讲清思路（时间复杂度、空间复杂度、优化方向）

□ 八股文（每个模块准备 5 个核心问题）
  □ [ ] Python 基础：GIL / 装饰器 / 生成器 / 深浅拷贝 / 垃圾回收
  □ [ ] 数据库：索引原理 / 慢查询 / 事务隔离 / MVCC / SQL 优化
  □ [ ] 网络：HTTP/HTTPS / TCP / DNS / 跨域 / 从 URL 到页面
  □ [ ] Redis：数据结构 / 持久化 / 缓存三问题 / 分布式锁
  □ [ ] 操作系统：进程/线程/协程 / IO 模型 / 内存管理

□ 系统设计（至少准备 3 个设计题）
  □ [ ] 短链接系统（能画架构图 + 讲清核心流程）
  □ [ ] 秒杀系统（能分层讲清优化策略）
  □ [ ] 消息推送系统（WebSocket + MQ + 离线消息存储）

□ 项目
  □ [ ] 每个项目准备 3-5 分钟的 STAR 描述
  □ [ ] 能解释每个技术选型的理由
  □ [ ] 准备 3 个"遇到了什么问题→怎么解决"的故事

□ 模拟面试
  □ [ ] 至少 3 次完整的模拟面试（包含自我介绍 + 技术提问 + 算法 + 反问）
  □ [ ] 录下来回看，观察语速、表情、是否频繁说"嗯...那个..."

自测问题：
1. 你能在 30 秒内讲清楚"我是谁、我为什么适合这个岗位"吗？
2. 你的三个项目中，哪一个最能体现你的技术深度？你能围绕它讲 10 分钟吗？
3. 如果面试官问"你的项目有什么可以改进的地方"，你能不假思索说出 3 点吗？
4. 你能在白板上画出电商系统的架构图吗？（不需要完美，但逻辑要通顺）
```

### 📱 手机阅读材料（通勤/排队时看）

| 材料 | 内容 | 预计时间 |
|------|------|---------|
| [CS-Notes](http://www.cyc2018.xyz/) | 国内面试八股文合集，手机上看很方便 | 每天 20min |
| [小林 coding 图解系列](https://xiaolincoding.com/) | 图解 MySQL/Redis/网络，面试前必看 | 每天 15min |
| [LeetCode Hot 100 题解](https://leetcode.cn/problem-list/2cktkvj/) | 看高票题解，学别人怎么写注释和思路 | 每天 3 题 |
| [system-design-primer 的 Anki](https://github.com/donnemartin/system-design-primer) | 系统设计 Flashcard，碎片时间刷 | 碎片时间 |
| 你自己的 GitHub README | 反复读自己写的技术文章和 README，直到能脱稿讲 | 每天 |

### 💻 动手练习（在电脑前做的事）

| 练习 | 说明 | 频率 |
|------|------|------|
| LeetCode 刷题 | 每天 3 题（简单 2 + 中等 1），重点做高频 100 | 每天 |
| 白板写代码 | 关掉 IDE，在纸上或白板上写代码（模拟面试场景） | 每周 2 次 |
| 模拟面试 | 用 ChatGPT 或找朋友模拟面试，录下来回看 | 每周 1 次 |
| 整理面经 | 把你投递的目标公司近 3 个月的面经整理成文档，逐题准备 | 1 次 |
| 更新简历 | 把每个项目的技术亮点提炼成简历上的 1-2 条 bullet point | 1 次 |

---

## 📚 完整资源索引

### 必读教程

| 资源 | 链接 | 阶段 |
|------|------|------|
| Python-100-Days | https://github.com/jackfrued/Python-100-Days | 1-3 |
| FastAPI 官方教程 | https://fastapi.tiangolo.com/zh/tutorial/ | 4 |
| React 官方文档 | https://react.dev/ | 5 |
| Next.js 官方教程 | https://nextjs.org/learn | 5 |
| 现代 JavaScript 教程 | https://zh.javascript.info/ | 5 |
| Docker 从入门到实践 | https://yeasy.gitbook.io/docker_practice/ | 6 |

### 刷题平台

| 平台 | 用途 |
|------|------|
| LeetCode | 算法 + SQL |
| 牛客网 | 国内面试高频 |
| SQLZoo | SQL 入门练习 |

### 书籍推荐（按阅读顺序）

| 序号 | 书名 | 何时读 | 重要程度 |
|------|------|--------|---------|
| 1 | 《Python 编程：从入门到实践》 | 阶段1 同步 | ⭐⭐⭐⭐⭐ |
| 2 | 《图解 HTTP》 / 《图解 TCP/IP》 | 阶段2 | ⭐⭐⭐⭐ |
| 3 | 《SQL 必知必会》 | 阶段3 | ⭐⭐⭐⭐ |
| 4 | 《流畅的 Python》 | 阶段4 之后 | ⭐⭐⭐⭐⭐ |
| 5 | 《鸟哥的 Linux 私房菜》 | 阶段6 | ⭐⭐⭐ |
| 6 | 《数据密集型应用系统设计》(DDIA) | 阶段7-8 | ⭐⭐⭐⭐⭐ |

### 系统设计

| 资源 | 说明 |
|------|------|
| [system-design-primer](https://github.com/donnemartin/system-design-primer) | 最全系统设计学习资源 |
| [CS-Notes](http://www.cyc2018.xyz/) | 国内面试八股文合集 |
| [架构师之路](https://www.w3cschool.cn/architectroad/) | 中文系统设计文章 |

---

## ⏰ 每日时间安排参考

### 在职版（每天 3h，推荐）

```
19:00-20:00  学新知识（看教程/文档，记笔记）
20:00-21:30  写代码（练习 + 项目推进，最重要的 1.5h）
21:30-22:00  复习今日 + 1道算法题
```

### 全职版（每天 6h）

```
09:00-11:00  学新知识（2h，精力最好时）
11:00-12:00  写代码练习
12:00-13:30  午饭+休息
13:30-16:30  写代码/做项目（3h，大块时间）
16:30-17:00  算法题（1-2道）
17:00-17:30  复习今日 + 整理笔记
```

### 周末（在职版）

```
周六：
09:00-12:00  攻克本周难点 + 集中写项目代码
14:00-17:00  继续项目 + 刷题

周日：
上午  复习本周所有内容 + 完善笔记
下午  推进项目 + 1道算法题（轻松）
```

---

## ✅ 检查点清单

每完成一个阶段，对照确认：

```
[ ] 阶段1：Python 基础
    [ ] 能独立写命令行工具（argparse + OOP + 文件读写）
    [ ] LeetCode 简单题 30+ 道
    [ ] 理解装饰器、生成器、面向对象三大特性

[ ] 阶段2：Python 进阶 + 网络
    [ ] 理解 HTTP 请求完整流程（DNS → TCP → TLS → HTTP → 响应）
    [ ] 能独立调用第三方 API 并处理异常
    [ ] Linux 基本操作熟练

[ ] 阶段3：数据库
    [ ] 能手写复杂 SQL（3表 JOIN + 子查询 + 窗口函数）
    [ ] 能看懂 EXPLAIN 执行计划
    [ ] 理解 B+ 树索引原理
    [ ] 能用 Python 操作数据库 + Redis

[ ] 阶段4：后端框架
    [ ] 能用 FastAPI 写一套 REST API（CRUD + JWT + 分页）
    [ ] 理解 asyncio 事件循环和协程原理
    [ ] 能用 Django 搭建基本项目（了解即可）
    [ ] 能用 Python 实现 5 种常见设计模式，说清应用场景
    [ ] 有完整的 Swagger 文档
    [ ] 有单元测试 + 集成测试

[ ] 阶段5：前端框架
    [ ] 理解 React 核心概念（组件/状态/副作用/Hooks）
    [ ] 能独立完成后台管理系统前端（全程 TypeScript）
    [ ] 能对接后端 API（登录/列表/表单/文件上传）
    [ ] TypeScript 泛型、工具类型使用熟练

[ ] 阶段6：DevOps
    [ ] 能把项目 Docker 化（Dockerfile + docker-compose）
    [ ] 能配置 Nginx 反向代理 + HTTPS
    [ ] 能用 GitHub Actions 自动部署
    [ ] 能在云服务器上跑通全栈项目
    [ ] 能搭建 Prometheus + Grafana 基础监控
    [ ] 理解进程/线程模型（多进程 vs 多线程 vs 异步）

[ ] 阶段7：微服务
    [ ] 理解微服务拆分原则
    [ ] 能使用 RabbitMQ 做异步通信
    [ ] 了解 gRPC 基础（选学）
    [ ] 能 docker-compose 编排多个服务

[ ] 阶段8：项目实战
    [ ] GitHub 上有 3 个完整的全栈项目
    [ ] 每个项目有 README + 单元测试 + 集成测试 + E2E 测试 + Docker 部署
    [ ] 每个项目 README 有"技术亮点"章节
    [ ] 代码结构清晰，有分层架构

[ ] 阶段9：面试准备
    [ ] 算法：LeetCode 高频 100 题能独立完成
    [ ] SQL：复杂查询能秒写
    [ ] 系统设计：能画出 3 个常见系统的架构图
    [ ] 项目：每个项目能用 STAR 法则 5 分钟讲清楚
    [ ] 软技能：能说清每个技术选型理由 + 设计模式应用场景 + 团队协作案例
```

---

## 🎯 最后提醒

1. **不要跳过基础直接学框架**——会写 API 但不懂 HTTP，面试一问就倒。
2. **项目驱动，不要"学完再动手"**——学到阶段4就开始做博客项目，边做边学后面阶段的内容。
3. **每天 commit**——GitHub 绿墙是最好的简历。
4. **每个阶段结束做复盘**——写一篇技术博客或发布 GitHub Release，固化所学。CS 基础（OS/网络/算法）不要堆到最后突击，分散到各阶段结合实践消化。
5. **SQL 和 Linux 是隐性加分项**——很多人只重视 Python，后端面试 SQL 问得更多。
6. **不要追新工具**——专注 FastAPI + React + PostgreSQL + Docker + Redis 这五个核心，其他按需补。
7. **面试是水到渠成的事**——项目做好了、基础扎实了，面试准备 2 周就够了。别忘了准备软技能：能用 STAR 法则讲清项目，能说明每个技术选型的理由。
8. **🔷 选学标记**：本计划中标注 🔷选学 的内容（gRPC、K8s、WebSocket、ELK 等）可按精力和目标取舍。目标是中小型公司可跳过，目标是大型公司/基础架构方向建议全部学习。

---

需要我把某个阶段展开得更细（比如精确到每天的安排），或者补充某个具体主题的学习资源吗？
