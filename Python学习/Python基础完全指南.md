# Python 基础完全指南（零基础到进阶）

> 适用对象：零编程经验，或学过但从未独立写过完整 Python 项目的初学者
> 涵盖：环境安装、变量与类型、字符串、列表元组、字典集合、条件与循环、函数、面向对象、异常处理、文件读写、模块与包、虚拟环境、常用标准库、PEP8 风格、命令行 TODO 实战项目、章节练习题
> 学习方式：全程文字，不依赖任何视频。手机碎片阅读 + 电脑编码输出，允许降级不允许归零
> 环境要求：Python 3.10+（推荐 3.10.11 或 3.11.x），所有示例均在 Python 3.10/3.11 下验证可运行
> 学完目标：能独立阅读并写出 learning-hub 中「大模型学习/阶段一」的全部示例代码，并能无缝衔接「阶段二第 3 周」的装饰器、生成器、OOP、asyncio 学习

> **为什么需要这本指南**：本仓库（learning-hub）的所有大模型课程都默认你已经会 Python，但此前仓库里并没有对应的 Python 基础教材。这一课就是补上这个缺口。你不需要任何其他视频课程，照着这份指南一步步走完，就能直接进入大模型学习。

> **如何使用**：
> 1. 白天用手机读标记为 📱 的概念小节，在脑子里把当晚会写的代码先想清楚
> 2. 晚上在电脑上照着标记为 💻 的小节敲代码，每个示例必须自己敲一遍，禁止只读不敲
> 3. 卡住了就倒退到上一小节重读，中断几天了就直接从上次的进度继续，允许降级不允许归零
> 4. 每章结尾动手完成「本章练习题」，第十六章有汇总和参考答案，做完再进入下一章

---

## 目录

1. [环境安装与开发工具](#一环境安装与开发工具)
2. [变量与基本数据类型](#二变量与基本数据类型)
3. [字符串操作](#三字符串操作)
4. [列表与元组](#四列表与元组)
5. [字典与集合](#五字典与集合)
6. [条件判断与循环](#六条件判断与循环)
7. [函数](#七函数)
8. [面向对象编程](#八面向对象编程)
9. [异常处理](#九异常处理)
10. [文件读写与序列化](#十文件读写与序列化)
11. [模块与包](#十一模块与包)
12. [虚拟环境](#十二虚拟环境)
13. [常用标准库](#十三常用标准库)
14. [PEP8 代码风格](#十四pep8-代码风格)
15. [实战项目：命令行 TODO 工具](#十五实战项目命令行-todo-工具)
16. [章节练习题汇总](#十六章节练习题汇总)
17. [衔接说明：进入大模型学习](#十七衔接说明进入大模型学习)

---

### 图例说明

| 标记 | 含义 |
|------|------|
| 📱 | 适合手机碎片阅读，以概念为主，代码短 |
| 💻 | 必须电脑实操，每个示例都要动手敲 |
| ⚠️ | 新手最容易踩的坑，务必注意 |
| 💡 | 提示或简化理解 |
| 🔥 | 进阶内容，了解即可，用到再回来深入 |

> ⏱️ **时间预算**：按每天 1 小时手机阅读 + 2 小时电脑编码，约 15 天学完。如果时间紧张，跳过的章节可以只读手机部分，电脑实操放到周末补。任何一章都不依赖前面的未学内容，放心跳读。

---

## 一、环境安装与开发工具

> 💻 本章必须电脑实操，后面的所有章节都依赖本章搭好的环境。

### 1.1 你需要装哪些东西

先看总览，知道每个工具是干什么的，再动手装。

| 工具 | 用途 | 必须装？ | 说明 |
|------|------|---------|------|
| Miniconda | Python 发行版 + 环境管理 | ✅ 必须 | 自带 python、pip、conda 命令 |
| Python 3.10+ | 语言解释器 | ✅ 必须 | 由 Miniconda 提供，不必单独装 |
| VS Code | 代码编辑器（IDE） | ✅ 强烈推荐 | 免费、跨平台、插件生态好 |
| Git | 版本控制 | ⭐ 推荐 | 本仓库后续课程会用到 |
| Ollama | 本地跑大模型 | 先不用 | 大模型学习「第 0 周环境准备」再装 |

> ⚠️ **不要把 Python 理解成"安装一个软件"**。更准确的说法是：Python 是一套语言规范，你安装的是一套实现（解释器）。解释器读你的 `.py` 文件，一句一句翻译成计算机能执行的指令。后面所有代码都要靠这个解释器来跑。

### 1.2 安装 Miniconda

Miniconda 是 Anaconda 的精简版。它做两件事：提供一个干净的 Python 3.10，以及一个叫 conda 的环境管理工具。**大模型学习第 0 周的环境准备用的就是 `conda create -n llm python=3.10`，你现在装好它，到时候照抄命令即可。**

#### Windows

1. 打开官网 https://docs.conda.io/en/latest/miniconda.html
2. 下载 `Miniconda3-latest-Windows-x86_64.exe`（64 位）
3. 双击安装，全部默认选项即可
4. 安装完成后，打开开始菜单里的 **Anaconda Prompt**（conda 专用终端）

#### macOS

```bash
# 用 Homebrew 安装（如果没有，先装：/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)")
brew install miniconda
conda init "$(basename "$SHELL")"   # 初始化 conda 命令
```

#### Linux（Ubuntu / Debian 系）

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh   # 一路回车 + 输入 yes
source ~/.bashrc                          # 重新加载配置，让 conda 生效
```

> 💡 国内网络下载慢时可用清华镜像源：`https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/`，文件名同样找 `Miniconda3-latest-...`。

### 1.3 创建你的 Python 环境

装好 Miniconda 后，打开终端（Windows 用 Anaconda Prompt），依次执行：

```bash
# 创建一个名为 py310 的环境，Python 版本 3.10
conda create -n py310 python=3.10
# 激活这个环境
conda activate py310
# 查看 Python 版本，确认安装成功
python --version
```

三条命令的含义：

| 命令 | 含义 |
|------|------|
| `conda create -n py310 python=3.10` | 创建独立环境，环境名 py310，里面装 Python 3.10 |
| `conda activate py310` | 进入 py310 环境，之后所有 python/pip 命令都指向它 |
| `python --version` | 显示当前 Python 版本，验证环境生效 |

期望输出类似：`Python 3.10.11`。如果你的终端显示的是 `Python 3.10.x`（x 是任意小版本号），就算成功。

> ⚠️ **小版本号不重要**。3.10.0 到 3.10.14 都满足要求，只要大版本是 3.10 或更高（3.11、3.12 也行）。本指南所有示例都用 Python 3.10+ 的语法，向下兼容到 3.8 的语法会额外标注。

> 💡 如果你已经装过 Anaconda 或者系统自带 Python，也建议再建一个独立的 conda 环境。后面学大模型时要装 PyTorch、transformers 等几十个依赖包，把它们和系统 Python 隔离开，能避免 90% 的环境冲突问题。

### 1.4 认识 pip

pip 是 Python 的包管理器，用来安装第三方库。你之后要用的 `openai`、`requests`、`pandas` 全靠它安装。它跟着 Python 一起装好，不需要单独安装。

```bash
# 查看 pip 版本
pip --version
# 安装一个包（requests 是 HTTP 请求库，后面章节会用到）
pip install requests
# 安装指定版本
pip install requests==2.32.3
# 卸载
pip uninstall requests
# 查看已安装的包
pip list
```

> ⚠️ 如果你的电脑上同时有多个 Python，敲 `pip` 可能装到了别的环境。**先 `conda activate py310` 再敲 `pip`**，永远在激活后的环境里操作，就不会装错。

### 1.5 安装 VS Code

1. 打开 https://code.visualstudio.com/ 下载对应系统的安装包并安装
2. 打开 VS Code，安装 4 个必备插件：

| 插件名 | 作用 |
|--------|------|
| Python（发布者 ms-python） | 语法高亮、代码补全、调试、运行按钮 |
| Pylance（通常随 Python 插件自动装） | 类型检查、智能提示 |
| Jupyter（ms-toolsai.jupyter） | 运行 .ipynb 笔记本（大模型学习阶段一大量使用） |
| Markdown Preview Enhanced | 预览本仓库这类 .md 教程 |

安装方法：点左侧边栏的「扩展」图标（方块加四格的形状），在搜索框输入插件名，点「安装」。

> 💡 这 4 个插件和「大模型学习第 0 周环境准备」章节要求的 VS Code 插件清单完全一致，你现在装好，后面直接复用。

### 1.6 你的第一个 Python 程序

环境搭好了，现在跑第一个程序。有两种方式。

#### 方式一：交互式解释器（REPL）

在终端输入 `python` 回车，进入交互模式：

```text
Python 3.10.11 (main, ...)
[GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
>>>
```

`>>>` 提示符表示等待你输入代码。输入 `print("Hello, World!")` 回车，立刻输出结果。输入 `exit()` 或按 `Ctrl+D`（Windows 是 `Ctrl+Z` 回车）退出。

#### 方式二：写脚本文件

交互模式适合试一句两句。正式写代码要放进 `.py` 文件：

1. 在 VS Code 里点「文件 → 打开文件夹」，随便建一个 `python-basics` 文件夹并打开
2. 新建文件 `hello.py`，输入：

```python
# hello.py 这是我的第一个 Python 程序
print("Hello, World!")
print("我在学 Python，目标是大模型开发")
```

3. 保存（`Ctrl+S`），点右上角三角形「运行」按钮，或者在终端执行：

```bash
python hello.py
```

终端输出：

```text
Hello, World!
我在学 Python，目标是大模型开发
```

> 💡 **print 函数**：`print()` 是 Python 内置函数，作用是把内容打印到屏幕上。`"..."` 之间的内容是字符串（文本）。括号里写什么，屏幕上就显示什么。

### 1.7 两种运行方式的区别

- **交互式 `python`**：试一句代码、查函数行为，即时反馈但不保存
- **脚本文件 `python xxx.py`**：正式写程序，可保存、可复用、可交给别人

**养成习惯：所有练习都写成 `.py` 文件保存**。你的电脑时间每一分钟都应该在产出可运行、可回看的代码文件，而不是在交互窗口里敲完就丢。

### 1.8 常见问题排查

| 报错信息 | 原因 | 解决方法 |
|---------|------|---------|
| `'conda' 不是内部或外部命令` | conda 未加入 PATH | Windows 用 Anaconda Prompt；macOS/Linux 执行 `source ~/.bashrc` 或重开终端 |
| `command not found: python` | Python 不在环境里 | 先 `conda activate py310` 再试 |
| `ModuleNotFoundError: No module named 'xxx'` | 包没装或装错了环境 | `pip install xxx`，确认当前在 py310 环境 |
| 运行没反应 | 可能进了交互模式 | 输入 `exit()` 退出，或用 `python hello.py` 运行文件 |
| VS Code 运行按钮报错 | 没选对解释器 | `Ctrl+Shift+P` 输入 `Python: Select Interpreter`，选择 py310 环境的 Python |

### 1.9 环境检查清单

完成本章后，逐项打勾确认：

- [ ] Miniconda 安装完成，`conda --version` 有输出
- [ ] `conda create -n py310 python=3.10` 成功，`python --version` 显示 3.10.x
- [ ] `pip --version` 正常，能安装和卸载 requests
- [ ] VS Code 装好 Python + Jupyter + Markdown Preview Enhanced 插件
- [ ] 在 VS Code 里新建 `hello.py` 并成功运行，屏幕打印出两行文字
- [ ] 能区分交互式运行和脚本文件运行

> 💡 本章的命令看起来多，其实核心只有一条链路：**conda create 建环境 → activate 激活 → python hello.py 跑代码**。把它走通，你的 Python 生涯就正式开始了。

---

## 二、变量与基本数据类型

> 📱 本章以概念为主，适合先手机通读一遍；⚠️ 标注的小节必须上机验证。

### 2.1 什么是变量

变量是给数据起的一个名字。你把数据放进"盒子"里，给盒子贴个标签，之后用标签就能取用里面的数据。

```python
# 把整数 18 存进变量 age
age = 18
# 把字符串 "小明" 存进变量 name
name = "小明"
# 用变量
print(age)      # 输出 18
print(name)     # 输出 小明
print(age + 1)  # 输出 19，变量可以做运算
```

Python 里等号 `=` 是赋值运算符，意思是"把右边的值绑定到左边的名字上"。这不是数学里的"相等"，而是"起名 + 绑定"。

```python
x = 10
x = x + 5   # 先把 x 当前值取出来加 5，再把新值绑回 x，结果 x = 15
print(x)    # 15
```

> 💡 Python 是**动态类型**语言：同一个变量名可以先后绑定不同类型的数据（`x = 10` 后 `x = "hello"` 完全合法）。但这不代表可以乱用。写代码时心里要清楚每个变量"此刻"是什么类型，Python 不会帮你检查。

### 2.2 变量命名规则

| 规则 | 示例 | 说明 |
|------|------|------|
| 只能由字母、数字、下划线组成 | `my_var1` | 中文变量名也能用但不推荐 |
| 不能以数字开头 | `1var` ❌ | `var1` ✅ |
| 不能是 Python 关键字 | `if`、`for`、`class` ❌ | 关键字有专门用途 |
| 区分大小写 | `Name` ≠ `name` | 两个是不同变量 |

**命名规范（PEP8 推荐）**：

| 场景 | 规范 | 示例 |
|------|------|------|
| 普通变量 | 全小写，单词用下划线分隔 | `user_name`、`total_price` |
| 常量（值不变） | 全大写，下划线分隔 | `MAX_SIZE`、`PI` |
| 类名 | 每个单词首字母大写 | `TaskManager` |
| 函数名 | 全小写下划线 | `get_user_name()` |

> ⚠️ 命名是代码质量的第一道关。变量名 `a`、`b`、`x1` 在 10 行的小脚本里还行，在 300 行的项目里就是灾难。**宁可名字长一点，也要见名知义**。

### 2.3 整数 int

整数是不带小数点的数字，可正可负可为零，且没有大小上限（只受内存限制）。

```python
a = 42
b = -7
huge = 10 ** 100       # 10 的 100 次方，Python 3 的整数没有溢出
print(huge)
print(0b1010)          # 二进制 1010，输出 10
print(0x1F)            # 十六进制 1F，输出 31
print(1_000_000)       # 数字间可用下划线分隔提高可读性，输出 1000000
```

### 2.4 浮点数 float

浮点数就是带小数点的数，底层用 IEEE 754 二进制存储。

```python
pi = 3.14159
temp = -0.5
speed = 1.2e6   # 科学计数法，等于 1.2 * 10^6 = 1200000.0
```

> ⚠️ **浮点数精度问题**：二进制无法精确表示很多十进制小数。
>
> ```python
> print(0.1 + 0.2)   # 输出 0.30000000000000004，不是 0.3！
> ```
>
> 这不是 Python 的 bug，所有编程语言都这样。判断两个浮点数是否相等，不要用 `==`，改用"差的绝对值小于一个极小值"：
>
> ```python
> print(abs(0.1 + 0.2 - 0.3) < 1e-9)   # True
> ```
>
> 需要精确的小数计算（比如金钱）时，用标准库 `decimal`，第十三章会讲到。

### 2.5 布尔类型 bool

布尔只有两个值：`True` 和 `False`。它是条件判断的基础。

```python
is_raining = True
is_sunny = False
# 逻辑运算
print(True and False)   # False，与：两个都真才真
print(True or False)    # True，或：一个为真即真
print(not True)         # False，非：取反
```

> 💡 布尔值可以参与整数运算：`True` 按 1 算，`False` 按 0 算。`True + True` 结果是 2。知道即可，实际代码中不要这么写。

### 2.6 字符串 str（入门）

字符串是文本数据，用单引号、双引号或三引号包裹。

```python
s1 = 'hello'
s2 = "world"
s3 = '''可以跨行
的字符串'''
s4 = """也可以这样"""
print(s1, s2)
```

字符串的详细操作（拼接、查找、格式化）在第三章展开。这里先记住：**字符串是一串字符的有序序列**，这句话是理解字符串一切操作的总纲。

### 2.7 类型转换

四种基本类型之间可以互相转换，用内置函数 `int()`、`float()`、`str()`、`bool()`。

```python
# 字符串转数字
s = "123"
n = int(s)        # 123
f = float("3.14") # 3.14
# 数字转字符串
age = 18
text = str(age)   # "18"，注意这是文本，不能再做加减法
# 数字转数字
i = int(3.99)     # 3，直接截断小数部分，不是四舍五入
f2 = float(7)     # 7.0
# 任意值转布尔
print(bool(0))        # False，0 转布尔是 False
print(bool(""))       # False，空字符串也是 False
print(bool("abc"))    # True，非空字符串是 True
print(bool([1, 2]))   # True，非空列表是 True
```

> ⚠️ 转换失败会抛异常：
>
> ```python
> int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
> ```
>
> 什么时候会需要类型转换？`input()` 读进来的永远是字符串，想当数字用就必须转换。这个在 2.11 会看到。

### 2.8 查看类型 type() 与判断 isinstance()

```python
print(type(18))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>
print(type("hi"))        # <class 'str'>
# isinstance 判断某个值是否属于某类型，返回布尔
print(isinstance(18, int))      # True
print(isinstance("18", int))    # False
print(isinstance(3.0, (int, float)))  # True，可以传类型元组
```

> 💡 判断类型用 `isinstance` 比直接比较 `type(x) == int` 更好，因为 isinstance 能正确处理继承关系，这一点在第八章学完继承后会更有体会。

### 2.9 运算符

| 类别 | 运算符 | 说明 | 示例结果 |
|------|--------|------|---------|
| 算术 | `+ - * /` | 加 减 乘 除 | `7 / 2` = 3.5 |
| 整除 | `//` | 向下取整的除法 | `7 // 2` = 3，`-7 // 2` = -4 |
| 取余 | `%` | 除法的余数 | `7 % 2` = 1 |
| 幂 | `**` | 乘方 | `2 ** 3` = 8 |
| 比较 | `== != > < >= <=` | 返回布尔 | `3 > 2` = True |
| 逻辑 | `and or not` | 与 或 非 | `True and False` = False |
| 成员 | `in not in` | 是否在容器里 | `"a" in "cat"` = True |
| 赋值 | `= += -= *= /=` | 简化赋值 | `x += 1` 等价 `x = x + 1` |

几个值得注意的点：

```python
# / 永远返回浮点数
print(7 / 2)     # 3.5
print(4 / 2)     # 2.0，注意是浮点
# % 判断整除很常用
print(10 % 2 == 0)   # True，10 是偶数
# 字符串也可以做 + 和 *（拼接与重复）
print("ab" + "cd")   # abcd
print("ha" * 3)      # hahaha
# 链式比较
x = 5
print(1 < x < 10)    # True，等价于 (1 < x) and (x < 10)
```

### 2.10 注释

注释是写给程序员看的说明，Python 解释器会忽略它们。

```python
# 这是单行注释，井号开头
# 多行字符串 """...""" 常被当作多行注释使用，但它只是没被赋值的字符串

def add(a, b):
    """函数文档字符串（docstring）：描述函数用途，用 help() 可查看"""
    return a + b
```

| 写法 | 用途 |
|------|------|
| `# 单行注释` | 解释一行代码"为什么"这么写 |
| `"""docstring"""` | 放在函数/类/模块开头，描述其功能，用 `help()` 可查看 |

> 💡 注释写"为什么"不写"是什么"。`x = x + 1  # 让 x 加 1` 这种注释是废话，代码本身已经说明了。`# 为什么不是乘 2？因为翻倍后浮点数会溢出` 这种才有价值。

### 2.11 输入 input() 与输出 print()

程序和人交互的两个基本动作：`input()` 从键盘读入，`print()` 输出到屏幕。

```python
name = input("请输入你的名字：")   # 用户输入回车后，字符串存进 name
print("你好，" + name)
age_str = input("请输入你的年龄：")
age = int(age_str)                 # 关键：input 返回字符串，需要转成 int
print("明年你就", age + 1, "岁了")
```

运行效果：

```text
请输入你的名字：小明
你好，小明
请输入你的年龄：18
明年你就 19 岁了
```

`print()` 的常用参数：`sep` 指定多个值之间的分隔符（默认空格），`end` 指定结尾字符（默认换行）。

```python
print("2026", "08", "26", sep="-")   # 2026-08-26
print("第一行", end="")
print("第二行")                      # 第一行第二行（不换行）
print("A", 1, True)                  # A 1 True，多个值用空格分隔
```

> ⚠️ 用户输入永远是不可信的。用户可能输 `abc` 而你的代码转 `int`，就会崩。处理这种"输入错误导致崩溃"的办法在第九章异常处理，先记住这个坑。

---

## 三、字符串操作

> 📱 本章 3.1 到 3.4 适合手机阅读记忆，3.5 的 f-string 是重中之重必须上机敲熟。

### 3.1 字符串是一串字符的有序序列

这句话拆开看三件事：

1. **一串字符**：字符串由单个字符组成，`"hello"` 就是 `h e l l o` 五个字符排成一串
2. **有序**：每个字符有一个位置编号，叫索引（index），从 0 开始数
3. **序列**：序列类型的通用操作（索引、切片、遍历、`in` 判断）字符串全部支持，后面学的列表、元组也支持

```python
s = "hello"
print(len(s))       # 5，len() 求长度
print(s[0])         # h，第 0 个字符
print(s[4])         # o，第 4 个字符
print("he" in s)    # True，子串判断
```

### 3.2 索引与切片

**索引（index）**：用 `字符串[编号]` 取一个字符。编号从左往右从 0 开始，也可以从右往左用负数。

```python
s = "python"
print(s[0])    # p
print(s[3])    # h
print(s[-1])   # n，-1 是最后一个字符
print(s[-2])   # o，倒数第二个
```

**切片（slice）**：用 `字符串[起始:结束:步长]` 取一段。**含起始，不含结束**，这是最容易记混的点。

```python
s = "python"
print(s[0:2])     # py，取索引 0 和 1，不含索引 2
print(s[2:])      # thon，从索引 2 到末尾（省略结束）
print(s[:3])      # pyt，从开头到索引 2（省略起始）
print(s[:])       # python，整个字符串（都省略）
print(s[::2])     # pto，步长 2，隔一个取一个
print(s[::-1])    # nohtyp，步长 -1 反向，字符串反转的技巧
print(s[1:5:2])   # yh，从 1 到 4，每 2 步取一个
```

切片越界不会报错，Python 会自动截断：

```python
s = "abc"
print(s[0:100])   # abc，结束超出长度，自动取到末尾
print(s[100:])    # （空字符串），起始超出长度，返回空
```

> ⚠️ **一个口诀：顾头不顾尾。** `[1:3]` 取到索引 2，不包括索引 3。这个规则在列表、元组、range 里通用，一次记牢省下所有混乱。

### 3.3 字符串方法速查表

方法是"挂在对象上的函数"，用 `字符串.方法名()` 调用。字符串的方法不会修改原字符串，而是返回新字符串（字符串不可变，见 3.9）。

| 方法 | 作用 | 示例 |
|------|------|------|
| `upper()` / `lower()` | 转大写 / 小写 | `"Abc".upper()` → `"ABC"` |
| `strip()` | 去掉两端空白 | `"  hi  ".strip()` → `"hi"` |
| `lstrip()` / `rstrip()` | 去左 / 去右空白 | `"  hi".lstrip()` → `"hi"` |
| `replace(a, b)` | 把 a 替换成 b | `"a-b".replace("-", "+")` → `"a+b"` |
| `split(sep)` | 按 sep 分割成列表 | `"a,b,c".split(",")` → `["a","b","c"]` |
| `join(iterable)` | 用字符串拼接序列 | `"-".join(["a","b"])` → `"a-b"` |
| `find(sub)` | 找子串位置，找不到返回 -1 | `"hello".find("l")` → 2 |
| `index(sub)` | 找子串位置，找不到抛异常 | `"hello".index("l")` → 2 |
| `startswith(prefix)` | 是否以某串开头 | `"file.py".startswith("file")` → True |
| `endswith(suffix)` | 是否以某串结尾 | `"file.py".endswith(".py")` → True |
| `count(sub)` | 统计子串出现次数 | `"aaa".count("a")` → 3 |
| `isdigit()` | 是否全为数字 | `"123".isdigit()` → True |
| `isalpha()` | 是否全为字母 | `"abc".isalpha()` → True |
| `isalnum()` | 是否全为字母或数字 | `"ab1".isalnum()` → True |
| `isupper()` / `islower()` | 大小写检查 | `"AB".isupper()` → True |

### 3.4 常用方法详解（上机）

```python
# split 和 join 是数据处理的黄金搭档
text = "apple,banana,orange"
fruits = text.split(",")       # ['apple', 'banana', 'orange']
print(fruits)
back = "-".join(fruits)        # 'apple-banana-orange'
print(back)
# strip 清洗用户输入
raw = input("请输入数字：").strip()   # 去掉用户多敲的空格
# replace 清理文本
msg = "I hate Python"
print(msg.replace("hate", "love"))   # I love Python
# find 与切片配合提取子串
url = "https://api.github.com/repos"
idx = url.find("api.")
print(url[idx:])               # api.github.com/repos
```

> 💡 `split` 返回的是**列表**，join 接收的是**列表**。列表是第四章的内容，你现在只需要知道：它们是字符串和列表互相转换的桥梁，会在 99% 的文本处理任务里出现。

### 3.5 f-string 字符串格式化（重中之重）

f-string 是 Python 3.6 加入的格式化语法，在字符串前面加 `f`，用 `{}` 直接嵌入变量或表达式。**它是后续所有章节（包括大模型课程代码）里出现频率最高的语法，必须敲熟。**

```python
name = "小明"
age = 18
score = 92.5
print(f"我叫{name}，今年{age}岁")
# 我叫小明，今年18岁
print(f"明年{age + 1}岁")      # {} 里可以放表达式
# 明年19岁
print(f"分数：{score:.1f}")    # 保留 1 位小数
# 分数：92.5
print(f"分数：{score:.0f}")    # 保留 0 位小数
# 分数：92
price = 3.14159
print(f"价格 {price:.2f} 元")  # 价格 3.14 元
```

格式化数字的常用格式：

| 写法 | 效果 | 示例 |
|------|------|------|
| `{x:.2f}` | 保留 2 位小数 | `{3.14159:.2f}` → `3.14` |
| `{x:,}` | 千分位分隔 | `{1000000:,}` → `1,000,000` |
| `{x:>5}` | 右对齐宽 5 | `{7:>5}` → `    7` |
| `{x:<5}` | 左对齐宽 5 | `{7:<5}` → `7    ` |
| `{x:^5}` | 居中宽 5 | `{7:^5}` → `  7  ` |
| `{x:05d}` | 补零到 5 位 | `{7:05d}` → `00007` |
| `{x:.0%}` | 百分比 | `{0.25:.0%}` → `25%` |

对齐格式在打印表格、生成报告时非常常用（第十三章和第十五章实战项目都会用到）。

> 💡 **f-string 能放表达式但不能放语句**。`f"{x:}"` 里写 `if` 语句会报错，需要条件取值时，先在外面算好放进变量，或者用三元表达式：`f"结果是{('大' if x > 10 else '小')}"`。三元表达式第六章会讲。

### 3.6 其他格式化方式（了解即可）

老代码里还会见到 `%` 格式化和 `.format()` 方法：`"分数是 %d 分" % 92`、`"我叫{}".format("小明")`。**新代码一律用 f-string**，认识这两种写法只是为了能读懂别人的旧代码。

### 3.7 转义字符与原始字符串

```python
# 转义字符：反斜杠开头的特殊字符
print("第一行\n第二行")     # \n 换行
print("制表符\t在这里")     # \t 制表符
print("她说：\"你好\"")     # \" 输出双引号
print("反斜杠\\")           # \\ 输出一个反斜杠
# 原始字符串：r 前缀，不处理转义，路径常用
path = r"C:\Users\pzh\python-basics"
print(path)   # C:\Users\pzh\python-basics
```

> ⚠️ Windows 文件路径里的反斜杠经常引发转义问题，**写路径一律用原始字符串 `r"..."` 或正斜杠 `"C:/Users/..."`**。第十、十三章的路径操作还会再强调。

### 3.8 多行字符串

```python
# 三引号保留换行和缩进
poem = """
床前明月光
疑是地上霜
"""
print(poem)
```

> 💡 三引号字符串也常被用作 docstring（第七章会正式介绍）。

### 3.9 字符串是不可变的

字符串一旦创建就不能修改。`s[0] = "x"` 会直接报错 `TypeError`。所有"修改"操作（upper、replace 等）都是**创建了一个新字符串**，原字符串没动。

```python
s = "hello"
s_upper = s.upper()
print(s)         # hello，原字符串没变
print(s_upper)   # HELLO，新字符串
```

> 💡 这个特性对性能有个暗示：在循环里反复 `+=` 拼接字符串效率低，需要频繁拼接时用 `join`：
>
> ```python
> words = ["a", "b", "c"]
> result = "".join(words)   # 推荐；等价于 result = "" 再逐个 +=
> ```
> 🔥 进阶链接：字符编码（Unicode / UTF-8）是字符串底层的核心知识，但不影响你现在写代码。到「文件读写」和「大模型数据处理」章节遇到乱码时再回头补。届时重点理解：Python 3 的字符串在内存里是 Unicode，存到文件或网络时需要编码成 UTF-8 字节。
---
## 四、列表与元组
> 📱 4.1 到 4.5 适合手机通读；4.8 的复制坑和 4.9 的内置函数必须上机。
### 4.1 列表：可以改动的有序容器
列表用方括号 `[]` 定义，元素用逗号分隔，可以装任意类型，也可以混合类型。它和字符串一样是**有序序列**，索引、切片、`in`、`len()` 全部通用。
```python
# 空列表
empty = []

# 纯数字
scores = [90, 85, 99, 76]

# 混合类型
mixed = [1, "two", 3.0, True, [1, 2]]   # 列表里还能装列表

# 访问
print(scores[0])     # 90
print(scores[-1])    # 76
print(scores[1:3])   # [85, 99]

# 长度
print(len(scores))   # 4

# 成员判断
print(99 in scores)  # True
```
### 4.2 列表的增删改查
列表和字符串最大的区别：**列表可变**。可以就地添加、删除、修改元素。
```python
tasks = ["写报告", "开会"]

# 增
tasks.append("学Python")          # 尾部追加一个
print(tasks)                       # ['写报告', '开会', '学Python']

tasks.insert(1, "回邮件")          # 指定位置插入
print(tasks)                       # ['写报告', '回邮件', '开会', '学Python']

tasks.extend(["买菜", "做饭"])     # 追加一个列表（把多个元素展开追加）
print(tasks)                       # ['写报告', '回邮件', '开会', '学Python', '买菜', '做饭']

# 删
tasks.remove("开会")               # 按值删除第一个匹配项，不存在会抛 ValueError
print(tasks)

popped = tasks.pop()               # 弹出并返回最后一个元素
print(popped, tasks)

first = tasks.pop(0)               # 弹出指定索引
print(first)

# 改
tasks[0] = "写季度报告"            # 按索引改
print(tasks)

# 查
print(tasks.index("买菜"))         # 找值的索引
print(tasks.count("买菜"))         # 统计出现次数
```
### 4.3 列表方法速查表
| 方法 | 作用 | 示例 |
|------|------|------|
| `append(x)` | 尾部加一个元素 | `[1].append(2)` → `[1,2]` |
| `extend(iterable)` | 展开追加多个元素 | `[1].extend([2,3])` → `[1,2,3]` |
| `insert(i, x)` | 在索引 i 处插入 x | `[1,3].insert(1,2)` → `[1,2,3]` |
| `remove(x)` | 按值删除第一个 | `[1,2,1].remove(1)` → `[2,1]` |
| `pop(i=-1)` | 弹出并返回索引 i 处元素 | `[1,2,3].pop()` → 3 |
| `index(x)` | 返回 x 第一次出现的索引 | `[5,6].index(6)` → 1 |
| `count(x)` | x 出现的次数 | `[1,1].count(1)` → 2 |
| `sort()` | 就地排序 | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | 就地反转 | `[1,2,3].reverse()` → `[3,2,1]` |
| `clear()` | 清空所有元素 | `[1,2].clear()` → `[]` |
| `copy()` | 返回浅拷贝新列表 | `a.copy()` |
`sort()` 的进阶用法（重点，后面数据处理天天用）：
```python
nums = [5, 2, 9, 1]
nums.sort()                # 升序
print(nums)                # [1, 2, 5, 9]

nums.sort(reverse=True)    # 降序
print(nums)                # [9, 5, 2, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)        # 按长度排序
print(words)               # ['apple', 'banana', 'cherry']

# 不修改原列表的排序：sorted()
nums = [3, 1, 2]
sorted_nums = sorted(nums)   # 返回新列表
print(nums, sorted_nums)     # [3, 1, 2] [1, 2, 3]
```
### 4.4 列表切片与复制（重要陷阱）
切片在列表上同样是"顾头不顾尾"，而且**切片总是返回新列表**：
```python
a = [1, 2, 3, 4, 5]
print(a[1:3])     # [2, 3]
print(a[::-1])    # [5, 4, 3, 2, 1]，反转
print(a[::2])     # [1, 3, 5]
```
> ⚠️ **复制陷阱：`b = a` 不是复制！**
>
> ```python
> a = [1, 2, 3]
> b = a            # 这只是让 b 和 a 指向同一个列表
> b.append(4)
> print(a)         # [1, 2, 3, 4]，a 也被改了！
> ```
>
> 正确复制有两种方式：
>
> ```python
> b = a.copy()          # 方法一
> c = a[:]              # 方法二，全切片
> c.append(99)
> print(a)              # [1, 2, 3, 4]，不受影响
> ```
>
> 深层陷阱：列表里装的是可变对象时，`copy()` 也只是浅拷贝，内层列表仍然共享。这个坑在 4.6 嵌套列表里会再演示。
### 4.5 嵌套列表
列表的元素可以是列表，形成二维结构，适合表示表格、矩阵。
```python
# 学生成绩表：每行是一个学生的 [姓名, 语文, 数学]
scores = [
    ["小明", 90, 85],
    ["小红", 78, 92],
    ["小刚", 88, 88],
]

print(scores[0])         # ['小明', 90, 85]，第一行
print(scores[0][1])      # 90，第一行第二列
print(scores[2][2])      # 88，第三行第三列

# 修改
scores[1][1] = 82
print(scores)

# 遍历（第六章会系统讲 for，这里先看）
for row in scores:
    print(f"{row[0]} 语文{row[1]} 数学{row[2]}")
```
> ⚠️ 嵌套列表的浅拷贝陷阱：
>
> ```python
> board = [[0] * 3] * 3   # 看起来是 3 行 3 列
> print(board)            # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
> board[0][0] = 1
> print(board)            # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]，三行一起变了！
> ```
>
> 原因：`[[0]*3] * 3` 把同一个内层列表复制了三份引用。正确写法是用推导式（第六章讲）：
>
> ```python
> board = [[0] * 3 for _ in range(3)]
> board[0][0] = 1
> print(board)            # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]，正常
> ```
### 4.6 元组：不可变的有序序列
元组用圆括号 `()` 定义，和列表几乎一样，唯一的区别是**创建后不能修改**（不能增删改）。
```python
point = (3, 5)          # 二维坐标
rgb = (255, 0, 0)       # 颜色
empty_tuple = ()
one_item = (42,)        # ⚠️ 单个元素必须有逗号！(42) 只是数字

print(point[0])         # 3
print(point[1:])        # (5,)
print(3 in point)       # True
print(len(rgb))         # 3
```
元组不能修改：
```python
t = (1, 2, 3)
# t[0] = 100   # 会报 TypeError：tuple 不支持元素赋值
```
**元组的两个经典用途：**
```python
# 1. 元组解包：一行代码交换变量
a, b = 10, 20
a, b = b, a
print(a, b)              # 20 10

# 2. 函数返回多个值（第七章会细讲）
def get_min_max(nums):
    return min(nums), max(nums)   # 返回元组，调用方自动解包

lo, hi = get_min_max([3, 1, 4, 1, 5])
print(lo, hi)            # 1 5
```
### 4.7 列表 vs 元组：怎么选
| 对比 | 列表 list | 元组 tuple |
|------|-----------|-----------|
| 写法 | `[]` | `()` |
| 可变性 | 可变 | 不可变 |
| 内存 | 稍大 | 稍小 |
| 适合场景 | 数据会增删改、数量不确定 | 数据固定、作为字典的键、函数多返回值 |
> 💡 经验法则：**"这个集合的内容会变吗？会变用列表，不会变用元组。"** 另外元组因为不可变，可以作为字典的键（第五章），列表不行（会报 `unhashable` 错误）。
### 4.8 序列通用内置函数
这些函数对字符串、列表、元组、range 都通用：
```python
nums = [5, 2, 9, 1, 7]

print(len(nums))     # 5，长度
print(max(nums))     # 9，最大值
print(min(nums))     # 1，最小值
print(sum(nums))     # 24，求和（元素必须是数字，字符串会报错）

# sorted：返回排序后的新列表，不修改原序列
print(sorted(nums))           # [1, 2, 5, 7, 9]
print(sorted(nums, reverse=True))  # [9, 7, 5, 2, 1]

# 字符串版本
s = "python"
print(sorted(s))      # ['h', 'n', 'o', 'p', 't', 'y']
print("".join(sorted(s)))   # hnopty
```
**enumerate：同时拿到索引和值**（遍历时的好伙伴，第六章还会用到）
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```
**zip：并行打包多个序列**
```python
names = ["小明", "小红", "小刚"]
scores = [88, 95, 79]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# 小明: 88
# 小红: 95
# 小刚: 79

# zip 结果也可以变成列表
pairs = list(zip(names, scores))
print(pairs)   # [('小明', 88), ('小红', 95), ('小刚', 79)]
```
### 4.9 综合小练习：平均分计算器
把本章内容串起来，写一个能算平均分的脚本 `avg_score.py`：
```python
# avg_score.py 计算平均分
scores = [90, 85, 99, 76, 88]

# 和与平均
total = sum(scores)
avg = total / len(scores)
print(f"总分：{total}，平均分：{avg:.1f}")

# 最高分和最低分
print(f"最高分：{max(scores)}，最低分：{min(scores)}")

# 显示排名（从高到低）
ranked = sorted(scores, reverse=True)
print("排名：", ranked)
```
运行 `python avg_score.py`：
```text
总分：438，平均分：87.6
最高分：99，最低分：76
排名： [99, 90, 88, 85, 76]
```
---
## 五、字典与集合
> 📱 本章概念适合手机通读；嵌套字典（5.6）是理解大模型 API 数据结构的钥匙，建议上机对照敲一遍。
### 5.1 为什么需要字典
列表用索引访问元素，但索引 0、1、2 没有含义。你想通过"名字"找"电话号码"，通过"城市"找"天气"，这种**键值对**的关系，就是字典的用武之地。
```python
# 列表的局限：phone[0] 是名字还是号码？看代码的人要猜
phone = ["小明", "13800000000"]

# 字典：键 -> 值，一一对应，直白
phone = {
    "小明": "13800000000",
    "小红": "13900000000",
}
print(phone["小明"])   # 13800000000
```
字典是 Python 里用得最多的数据结构之一。大模型 API 的请求体就是嵌套字典，5.6 会看到。
### 5.2 创建与访问
```python
# 空字典
empty = {}
empty2 = dict()

# 字面量
person = {
    "name": "小明",
    "age": 18,
    "city": "北京",
}

# 用键访问
print(person["name"])      # 小明
print(person["age"])       # 18

# dict() 构造
d = dict(name="小红", age=20)   # 键会自动变成字符串
print(d)                   # {'name': '小红', 'age': 20}
```
> ⚠️ 用 `d["不存在的键"]` 会抛 `KeyError`。安全的访问方式是用 `get()`，见 5.4。
### 5.3 增删改
```python
person = {"name": "小明", "age": 18}

# 增：直接赋新键
person["city"] = "北京"
print(person)   # {'name': '小明', 'age': 18, 'city': '北京'}

# 改：给已有键赋新值
person["age"] = 19
print(person)   # {'name': '小明', 'age': 19, 'city': '北京'}

# 删
del person["city"]          # 删除指定键，不存在会抛 KeyError
print(person)

age = person.pop("age")     # 弹出并返回，不存在会抛 KeyError
print(age, person)          # 19 {'name': '小明'}

person.clear()              # 清空
print(person)               # {}
```
### 5.4 字典方法速查表
| 方法 | 作用 | 示例 |
|------|------|------|
| `d.get(k, default)` | 取键 k 的值，没有返回 default（不抛错） | `d.get("x", 0)` |
| `d.keys()` | 所有键的视图 | `list(d.keys())` |
| `d.values()` | 所有值的视图 | `list(d.values())` |
| `d.items()` | 所有键值对视图 | `list(d.items())` |
| `d.setdefault(k, v)` | 键不存在则设置默认值并返回 | `d.setdefault("x", 1)` |
| `d.pop(k, default)` | 弹出键 k，没有返回 default | `d.pop("x", None)` |
| `d.update(other)` | 合并另一个字典 | `d.update({"y": 2})` |
| `k in d` | 键是否存在 | `"name" in d` |
**get 是最高频的方法**，数据清洗里天天用：
```python
scores = {"小明": 90, "小红": 95}

# 直接访问可能崩
# print(scores["小刚"])   # KeyError

# get 安全访问
print(scores.get("小刚"))          # None，没有默认值返回 None
print(scores.get("小刚", 0))       # 0，指定默认值
print(scores.get("小明", 0))       # 90
```
### 5.5 遍历字典
```python
person = {"name": "小明", "age": 18, "city": "北京"}

# 遍历键
for key in person:
    print(key)              # name age city

# 遍历键值对（最常用）
for key, value in person.items():
    print(f"{key}: {value}")

# 遍历值
for value in person.values():
    print(value)
```
> 💡 大模型 API 的 messages 就是列表套字典：
>
> ```python
> messages = [
>     {"role": "system", "content": "你是一个乐于助人的助手"},
>     {"role": "user", "content": "你好"},
> ]
> ```
>
> 你会发现阶段一课程里大量出现 `for msg in messages:` 加 `msg["role"]`、`msg["content"]` 的写法，正是这里的遍历。
### 5.6 嵌套字典
字典的值可以是任意类型，包括列表和字典。真实世界的数据几乎都是嵌套的。
```python
# 学生信息
students = {
    "小明": {"age": 18, "scores": [90, 85, 99]},
    "小红": {"age": 19, "scores": [78, 92, 88]},
}

# 多级访问：一层一层剥
print(students["小明"]["age"])            # 18
print(students["小明"]["scores"][1])      # 85
print(students["小红"]["scores"][-1])     # 88

# 安全的多级访问（用 get 逐层保护）
score = students.get("小刚", {}).get("scores", [])
print(score)   # []

# 修改嵌套值
students["小明"]["scores"][0] = 95
print(students["小明"]["scores"])         # [95, 85, 99]

# 遍历嵌套结构
for name, info in students.items():
    total = sum(info["scores"])
    avg = total / len(info["scores"])
    print(f"{name} 平均分 {avg:.1f}")
# 小明 平均分 93.0
# 小红 平均分 86.0
```
> ⚠️ 嵌套越深，越要小心「键不存在」的连锁崩溃。多级字典一律用 `get()` 逐层取，或者拿到 `{}` 默认值再往下走。
### 5.7 集合：不重复且无序的容器
集合用花括号 `{}` 定义（注意：空集合必须用 `set()`，`{}` 是空字典），特点：
1. **元素不重复**：重复元素自动去重
2. **无序**：没有索引，不能 `s[0]`
3. 元素必须是可哈希的（数字、字符串、元组可以；列表、字典不行）
```python
# 定义
s = {1, 2, 2, 3, 3, 3}
print(s)              # {1, 2, 3}，自动去重

# 空集合
empty = set()

# 从列表去重（最常用）
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)
print(unique)         # {1, 2, 3, 4}
back = list(unique)   # 再变回列表
print(back)           # [1, 2, 3, 4]
```
增删：
```python
s = {1, 2, 3}
s.add(4)
print(s)            # {1, 2, 3, 4}

s.add(4)            # 重复添加没效果
print(s)            # {1, 2, 3, 4}

s.discard(99)       # 删除，不存在也不报错（用 remove 会抛 KeyError）
s.remove(3)         # 删除，不存在会抛 KeyError
print(s)            # {1, 2, 4}
```
### 5.8 集合运算
集合的独门绝技是数学集合运算，找交集、并集、差集一行搞定：
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)     # 并集：{1, 2, 3, 4, 5, 6}
print(a & b)     # 交集：{3, 4}
print(a - b)     # 差集：在 a 不在 b：{1, 2}
print(b - a)     # {5, 6}
print(a ^ b)     # 对称差：只在一个集合里：{1, 2, 5, 6}

# 子集判断
print({1, 2} <= a)     # True，{1,2} 是 a 的子集
```
经典场景示例：
```python
# 找出两个班都报了的同学
class_a = {"小明", "小红", "小刚"}
class_b = {"小红", "小丽"}

print(class_a & class_b)     # {'小红'}

# 检查某元素是否在集合里（比列表的 in 快很多）
print("小红" in class_a)     # True
```

> 🔥 进阶链接：字典的键要求可哈希，背后是哈希表的数据结构（平均 O(1) 查找）。这在「软考」数据结构和「大模型」词表构建里都会出现。现在只需要记住结论：键用字符串或数字，别用列表。

---
## 六、条件判断与循环
> 💻 本章是编程的三大支柱（顺序、分支、循环）之二，必须每个示例都上机敲一遍。推导式（6.8）是后续大模型数据处理的高频语法。
### 6.1 if / elif / else
程序默认从上到下顺序执行。if 语句让程序"分岔"：条件满足走这条路，不满足走另一条。
```python
age = 18

if age >= 18:
    print("成年了")
else:
    print("未成年")
```
多分支用 `elif`（else if 的缩写）：
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"

print(f"等级：{grade}")
```
**语法要点**：
1. 条件后面必须有冒号 `:`
2. 条件成立的代码块必须**缩进**（通常 4 个空格）
3. Python 用缩进表示代码块，不靠花括号。缩进错误会直接报 `IndentationError`
4. `if` 可以单独存在，`else` 和 `elif` 不能脱离 if
```python
# 单分支
x = -3
if x > 0:
    print("正数")

# 条件可以是任何能算出布尔值的表达式
if 3 > 2 and "a" in "abc":
    print("两个条件都满足")
```
### 6.2 真值判断
`if` 后面的条件不要求一定是布尔值，Python 会把任意值自动转成布尔来判断。记住一句话：**空的东西是 False，非空是 True。**
| 值是 False 的情况 | 示例 |
|------------------|------|
| 数值 0 | `0`、`0.0` |
| 空字符串 | `""` |
| 空容器 | `[]`、`()`、`{}`、`set()` |
| `None` | 表示"什么都没有"的特殊值 |
| 布尔 False | `False` |
```python
# 判断列表是否为空，两种写法效果相同
items = []

# 写法一（新手常见）：
if len(items) == 0:
    print("列表是空的")

# 写法二（Pythonic，推荐）：
if not items:
    print("列表是空的")

# 判断字符串是否有内容
name = input("请输入名字：").strip()
if name:                      # 非空才往下走
    print(f"你好，{name}")
else:
    print("你什么都没输入")
```
### 6.3 三元表达式
`if...else` 可以压缩成一行，用于"根据条件选值"：
```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)   # 成年
```
> 💡 三元表达式适合"二选一赋值"。超过两个分支或者逻辑复杂，老老实实写完整 if 块，可读性优先。
### 6.4 while 循环
`while` 在条件为真时反复执行代码块，每次执行前检查条件。
```python
# 数到 5
count = 1
while count <= 5:
    print(count)
    count += 1        # 一定要有让条件最终变为假的语句，否则死循环
```
> ⚠️ **死循环**：如果条件永远为真，程序会无限循环。最典型的错误是忘记在循环里更新变量。万一程序卡死，按 `Ctrl+C` 终止。
```python
# 经典用法：直到用户输入正确才退出
while True:
    answer = input("请输入 y 或 n：").strip()
    if answer in ("y", "n"):
        break          # 满足条件跳出循环
    print("输入无效，请重新输入")
```
### 6.5 for 循环与 range
`for` 用于遍历序列（字符串、列表、元组、字典、集合）中的每个元素。这是**最常用的循环**。
```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for ch in "python":
    print(ch)

# 遍历字典（遍历键）
person = {"name": "小明", "age": 18}
for key in person:
    print(key)

# 遍历字典键值对
for key, value in person.items():
    print(f"{key}: {value}")
```
**range()：生成数字序列**，用于"循环固定次数"或"按数字循环"。
```python
# range(停止)：0 到 n-1
for i in range(5):
    print(i)            # 0 1 2 3 4

# range(起始, 停止)：顾头不顾尾；可加第三参数步长，负数步长实现倒序
for i in range(2, 6):
    print(i)            # 2 3 4 5
for i in range(0, 10, 2):
    print(i)            # 0 2 4 6 8
for i in range(5, 0, -1):
    print(i)            # 5 4 3 2 1

# 循环固定次数（_ 是"用不到这个值"的惯例写法）
for _ in range(3):
    print("执行三次")
```
### 6.6 break 与 continue
- `break`：立即**退出整个循环**
- `continue`：跳过本次迭代，**进入下一次**
```python
# break：找到目标就停
for num in [3, 7, 1, 9, 4]:
    if num > 5:
        print(f"找到第一个大于5的数：{num}")
        break

# continue：跳过满足条件的
for num in range(1, 11):
    if num % 2 == 0:
        continue       # 偶数直接跳过
    print(num)         # 打印 1 3 5 7 9（奇数）

# 嵌套循环：break 只退出最近的一层
for i in range(3):
    for j in range(3):
        if j == 2:
            break      # 只跳出内层
        print(i, j)
```
### 6.7 循环的 else 子句（了解）
`for` 和 `while` 后面可以跟 `else`：**循环正常结束（没有被 break 打断）时执行**。
```python
# 经典场景：查找失败
numbers = [1, 3, 5, 7]

for n in numbers:
    if n == 4:
        print("找到了")
        break
else:
    print("没找到 4")
```
> 💡 这个 `else` 写法在"查找是否成功"的场景很优雅，但可读性对新手稍差。写不出来时可以用标志变量代替：`found = False`，命中时 `found = True` 并 `break`，循环结束后 `if not found:` 再提示。
### 6.8 列表推导式（重点）
列表推导式用一行代码生成列表，取代"先建空列表再 for 循环 append"的三行模式。它是 Python 最招牌的语法之一，大模型数据预处理里无处不在。
```python
# 传统写法
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)     # [1, 4, 9, 16, 25]

# 推导式写法
squares = [i * i for i in range(1, 6)]
print(squares)     # [1, 4, 9, 16, 25]
```
结构拆解：
```text
[表达式 for 变量 in 可迭代对象 if 条件]
 └─输出值─┘ └─循环─┘ └─筛选（可选）─┘
```
```python
# 只保留偶数
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)       # [2, 4, 6, 8, 10]

# 对元素做处理
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words) # ['HELLO', 'WORLD', 'PYTHON']

# 提取嵌套数据
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 78},
]
names = [s["name"] for s in students]
scores = [s["score"] for s in students]
print(names)       # ['小明', '小红', '小刚']
print(scores)      # [90, 95, 78]

# 过滤 + 变换组合
passed = [s["name"] for s in students if s["score"] >= 90]
print(passed)      # ['小明', '小红']
```
### 6.9 字典与集合推导式
同样的语法，只是外层括号不同：
```python
# 字典推导式
squares = {x: x * x for x in range(1, 6)}
print(squares)     # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 集合推导式
words = ["apple", "banana", "apple"]
unique_len = {len(w) for w in words}
print(unique_len)  # {5, 6}

# 实际场景：把列表变成字典
fruits = ["apple", "banana", "cherry"]
fruit_dict = {f: len(f) for f in fruits}
print(fruit_dict)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```
> ⚠️ 推导式不要写太复杂。嵌套两层以上或逻辑超过一行，就用普通 for 循环。可读性永远优先，代码是写给人看的，顺便给机器执行。
### 6.10 遍历技巧汇总
```python
# enumerate：同时要索引和值
names = ["小明", "小红"]
for i, name in enumerate(names, start=1):
    print(f"第{i}名：{name}")

# zip：并行遍历多个列表
scores_a = [90, 85]
scores_b = [88, 92]
for a, b in zip(scores_a, scores_b):
    print(f"两次成绩：{a} 和 {b}")

# reversed：反向遍历
for x in reversed([1, 2, 3]):
    print(x)       # 3 2 1

# sorted：排序后遍历（不修改原列表）
nums = [3, 1, 2]
for n in sorted(nums):
    print(n)       # 1 2 3
print(nums)        # [3, 1, 2]，原列表没动
```
### 6.11 综合练习：猜数字游戏
把本章内容全部串起来的练习。新建 `guess.py`：
```python
# guess.py 猜数字游戏
import random

secret = random.randint(1, 100)   # 随机 1 到 100 的整数
attempts = 0

print("我心里想了一个 1 到 100 的数字，猜猜看！")

while True:
    text = input("请输入你的猜测：").strip()

    if not text.isdigit():        # 非数字输入
        print("请输入数字！")
        continue

    guess = int(text)
    attempts += 1

    if guess < secret:
        print("太小了")
    elif guess > secret:
        print("太大了")
    else:
        print(f"恭喜！猜对了，答案是 {secret}，你用了 {attempts} 次")
        break
```
运行几次，体会 while、if、break、continue、isdigit、f-string 的配合。
---
## 七、函数
> 📱 7.1 到 7.6 是函数的核心，手机通读；7.7 的 `*args/**kwargs` 是理解大模型 API 参数的关键，必须上机。
### 7.1 为什么需要函数
重复的代码写两遍叫复制，写十遍就是灾难。函数把一段逻辑打包成一个"工具"，给它起名字、传参数，需要时调用。
```python
# 不写函数：每个地方都要重复这段逻辑
a_scores = [90, 85, 99]
print(sum(a_scores) / len(a_scores))

b_scores = [78, 92, 88]
print(sum(b_scores) / len(b_scores))
# 如果哪天要改成"四舍五入保留一位"，每个地方都要改

# 写函数：逻辑只写一遍
def average(scores):
    return sum(scores) / len(scores)

print(average(a_scores))   # 91.33333333333333
print(average(b_scores))   # 86.0
# 要改格式，只改函数内部一处
```
### 7.2 定义与调用
```python
def greet(name):
    """打印问候语"""
    print(f"你好，{name}！")

# 调用
greet("小明")     # 你好，小明！
```
结构拆解：
```text
def 函数名(参数列表):
    """文档字符串（可选）"""
    函数体
    return 返回值（可选）
```
### 7.3 return 返回值
函数可以返回一个值给调用方。没有 `return` 的函数返回 `None`。
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)     # 8

def nothing():
    print("这个函数没有 return")

print(nothing())  # 先打印"这个函数没有 return"，然后打印 None

# 返回多个值：实际返回的是元组，自动解包
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])
print(lo, hi)     # 1 4
```
> 💡 **return 会立即结束函数**。return 之后的代码不会执行。
>
> ```python
> def check(x):
>     if x < 0:
>         return "负数"     # 提前返回
>     return "非负数"       # 只有没进上面的 if 才会走到
> ```
### 7.4 参数传递：值 vs 引用
这是新手最容易困惑的点。记住一句话：**参数传的是"引用"（对象在内存中的地址），可变对象在函数内被修改会影响外面。**
```python
def change_num(x):
    x = x + 10            # 重新绑定，不影响外部
    return x

a = 5
change_num(a)
print(a)                  # 5，整数不可变，外部不受影响

def add_item(lst):
    lst.append(99)        # 就地修改列表，影响外部

nums = [1, 2, 3]
add_item(nums)
print(nums)               # [1, 2, 3, 99]，被改了！
# 注意：如果函数内部重新绑定（lst = [...]），则不影响外部
```
> ⚠️ 经验法则：函数内部要修改一个列表/字典，直接改；要重新赋值一个新的，那就 return 出来再赋给外部变量。别让函数偷偷改外部数据（副作用），改了就打印出来验证。
### 7.5 位置参数与关键字参数
```python
def introduce(name, age, city):
    print(f"{name}，{age}岁，来自{city}")

# 位置参数：按顺序传
introduce("小明", 18, "北京")

# 关键字参数：指名道姓，顺序无所谓
introduce(city="上海", name="小红", age=20)

# 混用：位置参数必须在关键字参数前面
introduce("小刚", city="广州", age=22)
# introduce(city="广州", "小刚", 22)   # 语法错误
```
### 7.6 默认参数
```python
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("小明")            # 你好，小明！用默认值
greet("小明", "早上好")   # 早上好，小明！覆盖默认值
```
> ⚠️ **可变默认参数陷阱**：默认参数只在函数定义时计算一次。如果默认值是列表/字典这种可变对象，多次调用会共享同一个对象，产生诡异 bug。
>
> ```python
> # 错误示范
> def add_task(name, tasks=[]):
>     tasks.append(name)
>     return tasks
>
> print(add_task("写报告"))     # ['写报告']
> print(add_task("开会"))       # ['写报告', '开会']，上次的结果还在！
>
> # 正确做法：默认值用 None，函数内再创建
> def add_task(name, tasks=None):
>     if tasks is None:
>         tasks = []
>     tasks.append(name)
>     return tasks
>
> print(add_task("写报告"))     # ['写报告']
> print(add_task("开会"))       # ['开会']
> ```
>
> 记住规则：**默认参数用不可变对象（数字、字符串、None）**。
### 7.7 *args：任意数量的位置参数
`*args` 把传入的**所有位置参数**打包成一个元组。函数体里用 `args` 遍历。
```python
def total(*nums):
    print(type(nums))        # <class 'tuple'>
    return sum(nums)

print(total(1, 2, 3))        # 6
print(total(1, 2, 3, 4, 5))  # 15
print(total())               # 0，可以传零个

# 实际场景：日志函数、格式化函数
def log(level, *messages):
    for msg in messages:
        print(f"[{level}] {msg}")

log("INFO", "启动完成")
log("ERROR", "文件不存在", "第 3 行", "请检查路径")
```
**反向使用：调用时用 `*` 解包序列**。
```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))     # 6，把列表拆开按位置传参
```
### 7.8 **kwargs：任意数量的关键字参数
`**kwargs` 把传入的**所有关键字参数**打包成一个字典。
```python
def make_profile(**kwargs):
    print(type(kwargs))      # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

make_profile(name="小明", age=18, city="北京")
# name: 小明
# age: 18
# city: 北京

# 实际场景：把参数原样转发给另一个函数
def api_request(url, **kwargs):
    print(f"请求 {url}")
    print(f"额外参数：{kwargs}")
    # 这里可以 requests.get(url, **kwargs)

api_request("https://api.example.com", timeout=10, headers={"A": "B"})
```
**反向使用：调用时用 `**` 解包字典**。
```python
def describe(name, age):
    print(f"{name} {age}岁")

info = {"name": "小红", "age": 20}
describe(**info)     # 小红 20岁
```
> 💡 **为什么学这个**：大模型 API（openai 库）的调用签名形如 `client.chat.completions.create(model=..., messages=..., temperature=...)`。阶段二第 3 周的 `LLMClient.chat(self, messages, **kwargs)` 就是用 `**kwargs` 把 temperature、max_tokens 等参数透传给底层 API。你现在懂了 `**kwargs`，那个类就看得懂了。
### 7.9 lambda 匿名函数
`lambda` 创建没有名字的一次性小函数，适合传给 `sorted`、`filter` 等需要回调的场景。
```python
# 语法：lambda 参数: 表达式
square = lambda x: x * x
print(square(5))     # 25

# 等价于
def square(x):
    return x * x
```
lambda 的典型用法：作为排序的 key。
```python
students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 78},
]

# 按成绩排序
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for s in by_score:
    print(s["name"], s["score"])

# 按名字长度排序
words = ["banana", "apple", "kiwi"]
print(sorted(words, key=lambda w: len(w)))   # ['kiwi', 'apple', 'banana']
```
> 💡 lambda 只适合一句话能写完的逻辑。逻辑复杂就写普通函数。`lambda x: ...` 里的 `...` 只能是一个表达式，不能有 if 语句块、不能有赋值（但可以有三元表达式）。
### 7.10 作用域：LEGB 规则
变量在哪个范围生效，由作用域决定。Python 按 **L-E-G-B** 四层由内向外查找名字：
| 层级 | 全称 | 位置 |
|------|------|------|
| L | Local | 当前函数内部 |
| E | Enclosing | 外层嵌套函数的局部作用域（闭包相关） |
| G | Global | 模块顶层（当前 .py 文件） |
| B | Built-in | Python 内置名字（print、len 等） |
```python
x = 10            # 全局变量

def show():
    y = 20        # 局部变量
    print(x)      # 能读到全局的 x，输出 10
    print(y)      # 20

show()
# print(y)        # 报错：函数外的代码读不到局部变量 y
```
**global 关键字**：函数内部要修改全局变量，必须先声明。
```python
count = 0

def increment():
    global count     # 声明：我要改的是全局的 count
    count += 1

increment()
increment()
print(count)         # 2
```
> ⚠️ 新手常见错误：函数内 `x += 1` 但 x 是全局变量，会报 `UnboundLocalError`。这是因为赋值让 Python 认为 x 是局部变量。**要么函数内用 global 声明，要么把值传进函数并 return 出来**。后者更干净。
### 7.11 闭包（一句话带过）
函数内部定义函数，并且内层函数使用了外层函数的局部变量，这个内层函数就是闭包。它是装饰器的实现基础，此处只留一个概念，**详细内容在「大模型学习/04-阶段二-大模型应用开发.md」第 3 周星期一（装饰器）展开**。
```python
def make_adder(n):
    def adder(x):        # 内层函数用了外层变量 n
        return x + n
    return adder

add5 = make_adder(5)
print(add5(10))          # 15
```
你能看懂这段代码即可，不需要深入。记住：`n` 在 `make_adder` 返回后依然被 `adder` 记住，这就是闭包。
### 7.12 文档字符串 docstring
写在函数第一行的三引号字符串，描述函数用途。用 `help()` 或 IDE 悬停可以查看。
```python
def calculate_bmi(weight_kg, height_m):
    """计算 BMI 指数。

    参数：
        weight_kg: 体重，单位千克
        height_m: 身高，单位米

    返回：
        浮点数 BMI 值
    """
    return weight_kg / (height_m ** 2)

print(calculate_bmi(65, 1.75))   # 21.224489795918366
```
### 7.13 递归（了解）
函数调用自己，叫递归。必须有两个要素：**基线条件**（什么时候停止）和**递归推进**（每次向基线靠近）。
```python
def factorial(n):
    """计算 n! = n * (n-1) * ... * 1"""
    if n <= 1:          # 基线条件
        return 1
    return n * factorial(n - 1)   # 递归调用

print(factorial(5))    # 120
```
```python
# 斐波那契数列
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(8):
    print(fib(i), end=" ")   # 0 1 1 2 3 5 8 13
print()
```
> 💡 递归适合"问题可以分解成同构子问题"的场景（树的遍历、目录扫描）。新手阶段会用 for 循环解决的问题不要硬上递归。Python 默认递归深度上限约 1000，超了会报 `RecursionError`。
---
## 八、面向对象编程
> 📱 8.1 到 8.6 是 OOP 主干，手机通读；8.10 的 LLMClient 雏形是阶段二第 3 周的预告，必须上机敲出来。
### 8.1 类和对象：模板与成品
面向对象编程（OOP，Object-Oriented Programming）用"类"和"对象"组织代码。
- **类（class）**：模板，定义数据和行为的蓝图
- **对象（object / 实例）**：按模板做出的具体成品
做饭类比：类是菜谱（宫保鸡丁的做法），对象是照菜谱做出来的一盘盘菜。同一个菜谱可以做出很多盘，每盘的辣度、分量可以不同。
```python
class Student:
    """学生模板"""
    def __init__(self, name, age):
        self.name = name      # 实例属性
        self.age = age

    def introduce(self):      # 实例方法
        print(f"我是{self.name}，{self.age}岁")

# 创建两个"实例"
s1 = Student("小明", 18)
s2 = Student("小红", 19)

s1.introduce()    # 我是小明，18岁
s2.introduce()    # 我是小红，19岁
```
### 8.2 __init__ 与 self
`__init__` 是**构造方法**：创建实例时自动调用，用来初始化实例的数据。
`self` 是实例本身的引用。**调用方法时 Python 自动把实例传进去**，所以定义方法时第一个参数必须是 self（名字是惯例，用什么都可以，但没人会改它）。
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name          # 每个实例有自己的名字
        self.breed = breed
        self.energy = 100         # 默认值，不用传

    def bark(self):
        print(f"{self.name}：汪汪！")

    def run(self):
        self.energy -= 10
        print(f"{self.name} 跑了，能量还剩 {self.energy}")

d = Dog("旺财", "金毛")
d.bark()          # 旺财：汪汪！
d.run()           # 旺财 跑了，能量还剩 90
d.run()           # 旺财 跑了，能量还剩 80
```
> ⚠️ 三个对象之间的关系要分清：`d` 是实例，`Dog` 是类，`d.name` 是实例属性，`d.bark` 是实例方法。实例和类通过"点号"连接。
### 8.3 实例属性 / 类属性 / 类方法 / 静态方法
| 种类 | 定义位置 | 访问方式 | 典型用途 |
|------|---------|---------|---------|
| 实例属性 | `__init__` 里 `self.xxx` | `实例.xxx` | 每个对象自己的数据 |
| 类属性 | 类体内直接赋值 | `类.xxx` 或 `实例.xxx` | 所有对象共享的数据 |
| 实例方法 | 普通方法，第一个参数 self | `实例.方法()` | 操作实例数据 |
| 类方法 | `@classmethod`，第一个参数 cls | `类.方法()` | 不依赖实例，操作类数据 |
| 静态方法 | `@staticmethod` | `类.方法()` | 和类逻辑相关但不需要任何实例/类数据 |
```python
class Circle:
    pi = 3.14159          # 类属性：所有圆共享

    def __init__(self, radius):
        self.radius = radius      # 实例属性：每个圆自己的

    def area(self):               # 实例方法
        return Circle.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, d):    # 类方法：用直径创建圆
        return cls(d / 2)

    @staticmethod
    def is_valid(r):              # 静态方法：工具函数
        return r > 0

c1 = Circle(1)
c2 = Circle.from_diameter(4)      # 类方法创建，半径 2

print(c1.area())                  # 3.14159
print(c2.radius)                  # 2.0
print(Circle.is_valid(-1))        # False
print(Circle.pi)                  # 3.14159，类属性
```
> 💡 什么时候用类方法/静态方法？函数逻辑和类强相关（比如"用不同单位构造实例"、"检查参数合法性"），但不需要具体实例时，就放进类里。否则写普通函数就好，不要为了用而用。
### 8.4 魔术方法（dunder 方法）
以双下划线开头结尾的方法，叫魔术方法。它们不用你手动调用，Python 在特定时机自动触发。**记住一个原则：魔术方法决定"这个类的对象在语言层面表现为什么样子"。**
| 魔术方法 | 触发时机 | 示例场景 |
|---------|---------|---------|
| `__init__(self, ...)` | 创建实例时 | 初始化数据 |
| `__str__(self)` | `print(对象)` / `str(对象)` | 给人看的描述 |
| `__repr__(self)` | 交互环境显示对象 | 给开发者看的描述 |
| `__len__(self)` | `len(对象)` | 自定义容器 |
| `__getitem__(self, key)` | `对象[key]` | 支持下标访问 |
| `__setitem__(self, key, value)` | `对象[key] = v` | 支持下标赋值 |
| `__contains__(self, item)` | `item in 对象` | 支持 in 判断 |
| `__eq__(self, other)` | `对象 == other` | 自定义相等比较 |
| `__lt__(self, other)` | `对象 < other` | 自定义排序 |
| `__call__(self, ...)` | `对象(...)` | 让实例像函数一样调用 |
| `__add__(self, other)` | `对象 + other` | 自定义加法 |
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"{self.owner}的账户，余额 {self.balance} 元"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

    def __len__(self):            # 也许想知道账户里有几笔…此处模拟
        return int(self.balance)

    def __eq__(self, other):
        return self.balance == other.balance

a = BankAccount("小明", 100)
b = BankAccount("小红", 200)

print(a)                  # __str__：小明 的账户，余额 100 元
print([a])                # __repr__：BankAccount('小明', 100)
print(len(a))             # __len__：100
print(a == b)             # __eq__：False
```
> 💡 `__str__` 和 `__repr__` 是最常写的两个：**`__str__` 面向用户，`__repr__` 面向开发者调试**。写类时至少实现 `__str__`，否则 `print(对象)` 只会输出 `<__main__.Xxx object at 0x...>` 这种无意义地址。
### 8.5 继承
继承让一个新类（子类）复用已有类（父类）的属性和方法，然后扩展或改写。**继承表达"is-a"关系**：金毛是狗，QwenClient 是 LLMClient。
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} 在吃东西")

    def speak(self):
        print("...")      # 父类默认实现，子类会覆盖

class Dog(Animal):        # 括号里写父类
    def speak(self):      # 方法覆盖（override）
        print(f"{self.name}：汪汪！")

    def fetch(self):      # 子类新方法
        print(f"{self.name} 捡回飞盘")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}：喵~")

dog = Dog("旺财")
cat = Cat("咪咪")

dog.eat()       # 旺财 在吃东西（继承自父类）
dog.speak()     # 旺财：汪汪！（子类覆盖）
dog.fetch()     # 旺财 捡回飞盘（子类新增）
cat.speak()     # 咪咪：喵~
```
> ⚠️ 子类的 `__init__` 不会自动调用父类的 `__init__`。如果子类定义了 `__init__` 且需要父类的初始化逻辑，必须显式调用 `super().__init__(...)`（下一节）。
### 8.6 super()：调用父类的方法
`super()` 返回父类的代理，用来调用父类的方法。最典型场景：子类的 `__init__` 先初始化父类部分，再初始化自己独有的部分。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我叫{self.name}，{self.age}岁")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)   # 先让父类处理 name、age
        self.school = school          # 再处理自己的 school

    def intro(self):                  # 覆盖父类方法，但复用父类逻辑
        super().intro()               # 调用父类的 intro
        print(f"我在{self.school}上学")  # 再补充自己的内容

s = Student("小明", 18, "北京一中")
s.intro()
# 我叫小明，18岁
# 我在北京一中上学
```
> 💡 **super() 的另一个价值**：父类逻辑变更时，子类不需要跟着改。这在大模型课程的 LLMClient 体系里就是「基类提供 `chat_with_retry` 通用逻辑，子类只用 super 初始化各自配置」的用法。
### 8.7 多态（一句话理解）

多态的意思是：**同一个方法名，在不同类的对象上表现出不同行为**。调用方不需要关心对象具体是什么类。

```python
class Dog:
    def speak(self):
        print("旺财：汪汪！")

class Cat:
    def speak(self):
        print("咪咪：喵~")

def make_speak(animal):
    animal.speak()          # 不关心具体类型，只要求有 speak 方法

make_speak(Dog())           # 旺财：汪汪！
make_speak(Cat())           # 咪咪：喵~
```
> 💡 阶段二第 3 周的 `LLMClient` / `QwenClient` / `DeepSeekClient` 就是典型的多态：统一调用 `llm.chat(...)`，换模型只换实例不换代码。这是大模型开发里最核心的设计思想之一。
### 8.8 封装与私有属性
封装的思路：**把内部细节藏起来，只暴露必要接口**。Python 用名字前面加双下划线 `__` 表示"私有"，外部不能直接访问。
```python
class Wallet:
    def __init__(self, owner, amount):
        self.owner = owner
        self.__amount = amount    # 私有属性，外部不能直接读

    def deposit(self, money):
        if money <= 0:
            print("金额必须为正")
            return
        self.__amount += money

    def withdraw(self, money):
        if money > self.__amount:
            print("余额不足")
            return
        self.__amount -= money

    def get_balance(self):
        return self.__amount

w = Wallet("小明", 500)
w.deposit(100)
w.withdraw(50)
print(w.get_balance())     # 550
# print(w.__amount)        # AttributeError，外部访问不到私有属性
```
> ⚠️ 注意：Python 的"私有"只是约定 + 改名机制（`_Wallet__amount`），不是强制的安全隔离。它的意义是**告诉其他程序员"这是内部实现，别碰"**。不要试图绕过，更不要依赖它防攻击。
### 8.9 property：把方法包装成属性
`@property` 让方法用"属性"的语法访问，可以加校验逻辑，同时保持调用方的简洁。
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # 下划线开头：约定"内部使用"

    @property
    def celsius(self):            # 像属性一样读取
        return self._celsius

    @property
    def fahrenheit(self):         # 计算属性：不存储，实时算
        return self._celsius * 9 / 5 + 32

    @celsius.setter               # 像属性一样赋值，附带校验
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value

t = Temperature(25)
print(t.celsius)          # 25，像属性，不是方法调用
print(t.fahrenheit)       # 77.0
t.celsius = 30            # 像属性赋值，走 setter
print(t.celsius)          # 30
```
### 8.10 预告实战：设计一个 LLMClient 雏形
这是阶段二第 3 周星期三主题的**缩小版预告**。我们用 OOP 设计一个"统一聊天客户端"：基类定义统一接口，子类实现各自逻辑。看懂并敲出这段代码，第 3 周你会轻松得多。
```python
# llm_preview.py OOP 预告：统一聊天客户端
# 说明：真正的实现会调用 openai 库访问大模型 API，这里用 print 模拟，保证可运行。

class LLMClient:
    """LLM 客户端基类：定义统一接口"""

    def chat(self, messages, **kwargs):
        """子类必须实现 chat 方法，否则调用时报错"""
        raise NotImplementedError("子类必须实现 chat 方法")

    def chat_with_retry(self, messages, max_retries=3, **kwargs):
        """带重试的 chat（所有子类自动继承这段通用逻辑）"""
        import time
        for attempt in range(1, max_retries + 1):
            try:
                return self.chat(messages, **kwargs)
            except Exception as e:
                print(f"第 {attempt} 次尝试失败：{e}")
                if attempt < max_retries:
                    time.sleep(1)
        raise RuntimeError(f"重试 {max_retries} 次仍然失败")


class QwenClient(LLMClient):
    """本地 Qwen 模型客户端（模拟）"""

    def __init__(self, host="localhost", port=11434):
        self.host = host
        self.port = port

    def chat(self, messages, model="qwen2:0.5b", **kwargs):
        # 真实代码：client.chat.completions.create(model=..., messages=...)
        user_msg = messages[-1]["content"] if messages else ""
        return f"[Qwen/{model}] 你说了：{user_msg}"


class DeepSeekClient(LLMClient):
    """DeepSeek API 客户端（模拟）"""

    def __init__(self, api_key):
        self.api_key = api_key

    def chat(self, messages, model="deepseek-v4-flash", **kwargs):
        user_msg = messages[-1]["content"] if messages else ""
        return f"[DeepSeek/{model}] 你说了：{user_msg}"


# 使用：切换模型只需改一行
llm = QwenClient()
# llm = DeepSeekClient(api_key="sk-xxx")

reply = llm.chat_with_retry([{"role": "user", "content": "你好"}])
print(reply)
```
运行 `python llm_preview.py`：
```text
[Qwen/qwen2:0.5b] 你说了：你好
```
**这段代码用到了本章的什么？**
| 语法 | 出现在哪 |
|------|---------|
| 类定义 + `__init__` | `class LLMClient`、`class QwenClient` |
| 继承 | `class QwenClient(LLMClient)` |
| 方法覆盖 | 子类各自实现 `chat` |
| super 的影子 | 基类的通用逻辑被子类复用 |
| `**kwargs` | `chat(self, messages, **kwargs)` 透传参数 |
| 异常处理 | `raise NotImplementedError`、`try/except` |
> 🔥 这就是阶段二第 3 周要精通的模式。你现在能看懂它，到那一周你要做的只是把模拟部分换成真实的 openai API 调用，其余骨架完全一样。**请把这份代码放进你的知识库，第 3 周你会回来找它。**
---
## 九、异常处理
> 📱 本章篇幅短，概念为主，适合手机通读，然后上机把每个示例故意写错再看报错，你会比背十遍记得牢。
### 9.1 什么是异常
程序运行时出错，Python 会抛出一个**异常（Exception）**，并打印一段"报错信息"（traceback）。不处理的话，程序直接崩溃停止。
```python
print("开始")
nums = [1, 2, 3]
print(nums[10])      # IndexError: list index out of range
print("结束")        # 这行永远不会执行，程序在上面就崩了
```
报错信息里最有价值的三部分：
```text
Traceback (most recent call last):
  File "demo.py", line 3, in <module>
    print(nums[10])                    ← 出错的那行代码
IndexError: list index out of range    ← 异常类型：原因描述
```
### 9.2 try / except：捕获并处理
用 `try/except` 把可能出错的代码包起来，出错时执行 except 分支，程序不崩溃。
```python
try:
    text = input("请输入数字：")
    num = int(text)
    print(f"你输入的是 {num}，翻倍后 {num * 2}")
except ValueError:
    print("输入的不是数字，请重新运行")
```
**执行流程**：
```text
try 里的代码
  ├─ 没出错 → 跳过 except，继续往下走
  └─ 出错了 → 跳进匹配的 except，执行处理代码
```
### 9.3 捕获多个异常
不同的异常可以分别处理，也可以合并处理。
```python
try:
    nums = [1, 2, 3]
    idx = int(input("输入索引："))
    print(nums[idx])
except ValueError:
    print("索引必须是数字")
except IndexError:
    print("索引超出范围")
except Exception as e:
    print(f"其他错误：{e}")
```
| 写法 | 效果 |
|------|------|
| `except ValueError:` | 只捕获指定类型 |
| `except (ValueError, IndexError):` | 捕获多种类型，统一处理 |
| `except Exception as e:` | 捕获所有常规异常，e 是异常对象 |
| `except:` | 捕获一切（连 KeyboardInterrupt 也抓），不推荐 |
> ⚠️ **两个坑**：
> 1. 别用裸 `except:` 吞掉所有错误，程序"看起来没崩"但其实是带病运行，bug 更难查
> 2. `except Exception` 时把异常对象绑出来 `as e`，打印 `e` 至少留下线索
>
> ```python
> try:
>     x = int("abc")
> except Exception as e:
>     print(f"出错了：{e}")     # 出错了：invalid literal for int()...
> ```
### 9.4 else 与 finally
`try/except` 还可以挂两个附加块：
- `else`：**没出错时**执行（出错则不执行）
- `finally`：**无论是否出错都执行**（回收资源用）
```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("文件不存在")
else:
    print(f"读到了 {len(content)} 个字符")   # 只有没异常才执行
finally:
    print("清理：无论结果如何都会走到这")      # 最常用于关闭资源
```
> 💡 `finally` 的典型用途是关文件、关数据库连接。不过文件操作有 `with` 语句自动处理（第十章），`finally` 更多用于更复杂的资源场景。
### 9.5 常见内置异常速查
| 异常 | 触发场景 |
|------|---------|
| `ValueError` | 值不合法：`int("abc")` |
| `TypeError` | 类型不匹配：`"a" + 1`、`len(123)` |
| `IndexError` | 索引越界：`[1,2][5]` |
| `KeyError` | 字典键不存在：`{"a":1}["b"]` |
| `NameError` | 用了未定义的变量 |
| `AttributeError` | 访问不存在的属性：`None.xxx` |
| `ZeroDivisionError` | 除以零 |
| `FileNotFoundError` | 打开不存在的文件 |
| `ModuleNotFoundError` | import 不存在的模块 |
| `StopIteration` | 迭代器耗尽（阶段二生成器会用到） |
| `UnboundLocalError` | 函数内用未声明的全局变量 |
| `AssertionError` | `assert` 断言失败 |
> 💡 记住大多数异常的**类名本身就是英文描述**。报错第一行看到 `ValueError`，大概率是"某个值不合法"，先检查传给函数的值。
### 9.6 raise：主动抛出异常
除了"被动等出错"，你还可以主动抛出异常，用来拦截非法输入、表达"这个操作不被支持"。
```python
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 调用
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"出错了：{e}")

# 常用模式：先校验，非法就 raise
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"年龄不合法：{age}")
    print(f"年龄设为 {age}")

set_age(20)      # 年龄设为 20
# set_age(200)   # 抛 ValueError
```
### 9.7 自定义异常
内置异常不够表达业务语义时，继承 `Exception` 定义自己的异常类。**这是阶段二第 3 周（OOP 章节的 NotImplementedError 用法）的自然延伸**。
```python
class BalanceNotEnoughError(Exception):
    """余额不足异常"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise BalanceNotEnoughError(
                f"余额 {self.balance} 元，取款 {amount} 元，不足"
            )
        self.balance -= amount
        return amount

account = BankAccount(100)
try:
    account.withdraw(500)
except BalanceNotEnoughError as e:
    print(f"取款失败：{e}")
```
自定义异常的套路：
1. `class 名字(Exception):` 继承 Exception
2. 通常只写 `pass`，语义靠类名和消息表达
3. 抛的时候 `raise 名字("人类能读懂的消息")`
### 9.8 异常处理的最佳实践
| 建议 | 说明 |
|------|------|
| 异常要"精确" | 能捕获 ValueError 就别写裸 except |
| 异常要"就近" | 把可能出错的代码尽量缩小到 try 块内 |
| 别吞异常 | 捕获后至少打印或记录，不要 `except: pass` |
| 消息要有信息量 | `raise ValueError(f"余额不足：{balance}")` 而不是 `raise ValueError("error")` |
| 用异常处理"真正的意外" | 用户输入、文件缺失、网络失败该用；正常流程控制尽量别用 |
### 9.9 综合练习：健壮的数字输入
把本章串起来，做一个"无论用户怎么乱输都不会崩"的输入函数：
```python
# safe_input.py
def get_number(prompt):
    """不断询问，直到用户输入合法的数字"""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("输入无效，请输入数字")

# 测试
price = get_number("输入价格：")
quantity = get_number("输入数量：")
print(f"总价：{price * quantity:.2f} 元")
```
---
## 十、文件读写与序列化
> 💻 本章实操性强，每个示例都要建真实文件跑一遍。json（10.6）和 with（10.4）是后面 TODO 项目和阶段一 ChatBot 记忆功能的直接依赖。
### 10.1 open()：打开文件
读写文件的第一步是 `open()` 打开它，返回一个**文件对象**。

> ⚠️ **先建文件**：下面的示例读的是 `hello.txt`，请先在工作目录创建它（`echo "你好，世界" > hello.txt`，或用 `Path("hello.txt").write_text("你好，世界", encoding="utf-8")`）。否则第一次照抄会抛 `FileNotFoundError`。

```python
# 语法：open(路径, 模式, encoding=编码)
f = open("hello.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()          # 用完必须关闭，释放资源
```
**模式（mode）**：
| 模式 | 含义 | 文件不存在时 | 指针位置 |
|------|------|-------------|---------|
| `"r"` | 只读 | 报错 | 开头 |
| `"w"` | 只写（覆盖） | 创建 | 开头 |
| `"a"` | 追加 | 创建 | 末尾 |
| `"x"` | 只写（存在即报错） | 创建 | 开头 |
| `"r+"` | 读写 | 报错 | 开头 |
| `"b"` | 二进制模式（配合上面用） | - | - |
```python
# 二进制模式读图片（换成任何真实存在的文件都行）
with open("hello.txt", "rb") as f:
    data = f.read()
```
> ⚠️ **"w" 模式会清空原有内容**！每次打开都会从头写，旧内容直接没了。想保留旧内容用 "a" 追加。
### 10.2 读取文件的四种方式
```python
# 一次性全部读成字符串
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 按行读成列表（每行带 \n）
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 逐行读取（大文件首选：一次只占一行内存）
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())     # strip 去掉行尾换行符
# f.read(10) 可以读指定数量的字符
```
> 💡 处理大文件（几百 MB 甚至几 GB 的日志）时，**永远用 `for line in f` 逐行读**。用 `read()` 会一次性把整个文件塞进内存，直接撑爆。阶段二第 3 周星期二的生成器课程会把这个技巧升级成生成器版本。
### 10.3 写入文件
```python
# 覆盖写入
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")          # write 不会自动加换行
    f.write("第二行\n")

# 追加写入（"a" 模式）
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("追加的第三行\n")
# 多行一次写入用 writelines(["A\n", "B\n"])，注意每行自带换行
```
### 10.4 with 语句：自动关闭
`with` 是上下文管理器语法，**进入时打开，退出时自动 close()**。即使中间抛了异常也会正确关闭。
```python
# 推荐写法：不用手动 close
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
# 到这里文件已自动关闭
```
> ⚠️ **永远用 with 打开文件，不要裸 open + 手动 close**。忘写 close 会导致文件句柄泄漏，Windows 上还会出现"文件被占用无法删除"。记住：文件操作的模板就是 `with open(...) as f:` 三行起。
### 10.5 编码问题
文件里的字节怎么解释成字符，由编码决定。现代标准是 **UTF-8**。Python 3 里 `open()` 的默认编码跟随操作系统，Windows 默认可能是 GBK，这就是乱码的根源。
```python
# 统一显式指定 utf-8，杜绝跨平台乱码
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("中文内容")

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```
> 💡 三条铁律：
> 1. 写文件一律 `encoding="utf-8"`
> 2. 读文件先试 utf-8，乱码了再考虑源文件的真实编码（通常 GBK）
> 3. 跨平台传递文本文件，一律 UTF-8
### 10.6 JSON：程序间交换数据的标准格式
JSON 是纯文本的数据格式，结构上就是"嵌套的字典和列表"。**大模型 API 的请求和响应几乎全是 JSON**，阶段一课程里你会反复见到它。
```python
import json

# Python 数据 -> JSON 字符串
data = {
    "name": "小明",
    "age": 18,
    "scores": [90, 85, 99],
    "is_active": True,
    "address": None,
}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON 字符串 -> Python 数据
loaded = json.loads(json_str)
print(loaded["name"])           # 小明
print(loaded["scores"][0])      # 90
```
**和文件结合：JSON 持久化**（TODO 项目的核心机制）：
```python
import json

# 写入 JSON 文件
data = {"tasks": ["写报告", "学Python"], "count": 2}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON 文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)          # {'tasks': ['写报告', '学Python'], 'count': 2}
```
| 函数 | 作用 | 说明 |
|------|------|------|
| `json.dumps(obj)` | 对象转字符串 | 传给 API / 存文件 |
| `json.loads(s)` | 字符串转对象 | 解析 API 响应 |
| `json.dump(obj, f)` | 对象直接写入文件 | 持久化 |
| `json.load(f)` | 从文件读入并转对象 | 恢复数据 |
| `json.dump` 的 `indent=2` | 缩进美化 | 人眼可读 |
| `ensure_ascii=False` | 中文不转成 `\uXXXX` | 文件里显示中文 |
> ⚠️ JSON 能表示的只有：数字、字符串、布尔、null、数组、对象。**Python 的元组会变列表，set 会报错**。需要存 set 就转成列表，读回来再 set()。
### 10.7 CSV：表格数据的通用格式
CSV（逗号分隔值）是 Excel、数据库导出的通用表格格式。用标准库 `csv` 处理。
```python
import csv

# 写入
rows = [
    ["姓名", "语文", "数学"],
    ["小明", 90, 85],
    ["小红", 78, 92],
]
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# 读取：每行是一个列表
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['姓名', '语文', '数学']
# ['小明', '90', '85']
# ['小红', '78', '92']

# 用 DictReader：第一行自动成为字段名，按列名取值
with open("scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["姓名"], row["数学"])
# 小明 85
# 小红 92
```
> ⚠️ CSV 里的数字读出来全是**字符串**。要做运算，先 `int(row["数学"])`。写入时 `newline=""` 是标准库文档要求，避免 Windows 上多出空行。
### 10.8 pathlib：现代化的路径操作
`pathlib` 用面向对象的方式操作路径，比字符串拼接路径优雅得多（第十三章还会系统讲）。
```python
from pathlib import Path

# 路径对象
p = Path("data") / "sub" / "file.txt"   # 用 / 拼接，跨平台自动处理分隔符
print(p)                    # data/sub/file.txt

# 常用操作
home = Path.home()          # 用户主目录
cwd = Path.cwd()            # 当前目录

print(home)
print(cwd.exists())         # 路径是否存在
print(p.parent)             # data/sub
print(p.name)               # file.txt
print(p.stem)               # file（不带扩展名）
print(p.suffix)             # .txt

# 读写一步到位
Path("note.txt").write_text("内容", encoding="utf-8")
content = Path("note.txt").read_text(encoding="utf-8")
print(content)

# 目录操作
d = Path("myfolder")
d.mkdir(exist_ok=True)      # 创建目录，存在也不报错
Path("myfolder/a.txt").touch()   # 创建空文件
for f in d.iterdir():       # 遍历目录内容
    print(f)
```
---
## 十一、模块与包
> 📱 11.1 到 11.5 是模块化的核心，手机通读；11.7 的 pip 安装第三方包必须上机。
### 11.1 什么是模块
一个 `.py` 文件就是一个**模块（module）**。模块里的变量、函数、类可以被其他文件复用。把代码拆进模块，是为了：控制文件长度、逻辑分组、方便复用。
```text
python-basics/
├── main.py          # 入口文件
├── utils.py         # 工具函数模块
└── models.py        # 数据模型模块
```
### 11.2 import 的三种写法
```python
# 写法一：import 模块名，用 模块名.xxx 访问
import math
print(math.sqrt(16))          # 4.0

# 写法二：from 模块 import 名字，直接用
from math import sqrt
print(sqrt(16))               # 4.0

# 写法三：from 模块 import 名字 as 别名
from math import sqrt as sq
print(sq(16))                 # 4.0

# 导入多个名字
from math import sqrt, pi, floor
```
| 写法 | 优点 | 缺点 |
|------|------|------|
| `import math` | 命名空间清晰，不会冲突 | 写起来长 |
| `from math import sqrt` | 写起来短 | 多个模块同名函数会冲突 |
| `import math as m` | 短且有命名空间 | 别名影响可读性 |
> 💡 推荐规则：**常用标准库用 `import math` 式，需要导入的具体函数名不多时用 `from ... import ...`**。项目内自己写的模块，用 `import` 加完整模块名，代码更可追溯。
### 11.3 import 时发生了什么
`import` 的时候 Python 做了三件事：
1. 找到模块文件（`math` → 标准库目录，`utils` → 当前目录）
2. **执行一遍模块代码**（模块顶层的代码会运行）
3. 把模块对象放进命名空间
```python
# utils.py 文件内容
print("utils 被导入了")        # 顶层代码：import 时就会执行

def add(a, b):
    return a + b
```
```python
# main.py 文件内容
import utils                  # 输出：utils 被导入了
print(utils.add(1, 2))        # 3
```
> ⚠️ **模块顶层不要放"有副作用的代码"**（比如 input、print 大段内容、启动服务器）。顶层只放：import、常量、函数/类定义。需要执行的逻辑放进函数，或放进 `if __name__ == "__main__"` 块（11.5）。
### 11.4 创建和使用你自己的模块
在 `python-basics` 目录下建两个文件，跑 `main.py`：
```python
# utils.py 工具模块
TAX_RATE = 0.13                     # 模块级常量

def price_with_tax(price):
    """计算含税价格"""
    return price * (1 + TAX_RATE)

def discount(price, rate):
    """按折扣率计算价格"""
    return price * (1 - rate)
```
```python
# main.py 入口
import utils
from utils import price_with_tax

print(utils.TAX_RATE)               # 0.13
print(price_with_tax(100))          # 112.99999999999999（浮点精度，见 2.4）
print(utils.discount(100, 0.2))     # 80.0
```
### 11.5 if __name__ == "__main__"：区分"被导入"和"直接运行"
每个模块都有一个内置变量 `__name__`：
- 模块**直接运行**时，`__name__` 等于 `"__main__"`
- 模块**被 import** 时，`__name__` 等于模块名
```python
# say_hi.py
def say_hi(name):
    print(f"你好，{name}")

print(f"__name__ 的值是：{__name__}")

if __name__ == "__main__":
    # 只有直接运行 python say_hi.py 时才执行
    print("作为主程序运行")
    say_hi("小明")
```
```python
# other.py 导入 say_hi
import say_hi     # 输出：__name__ 的值是：say_hi
                  # 不会执行 if 块里的内容
```
> 💡 **这就是你每个项目入口文件的固定模板**：
>
> ```python
> def main():
>     # 程序主逻辑
>     pass
>
> if __name__ == "__main__":
>     main()
> ```
>
> 大模型课程里的 smart_assistant.py、chatbot.py 全部采用这个结构。**"直接在模块顶层写执行逻辑"是新手最常见的坏习惯**，从今天起统一用 `main()` 函数 + 这个判断。
### 11.6 包：组织模块的目录
多个相关模块放进一个带 `__init__.py` 的目录，就形成**包（package）**。
```text
myproject/
├── main.py
└── mypackage/              # 包：一个目录
    ├── __init__.py         # 标记这个目录是包（可为空）
    ├── tools.py
    └── config.py
```
```python
# main.py
from mypackage import tools
from mypackage.tools import format_name
import mypackage.config as config
```
> 💡 现阶段只需要知道包的结构规则。你后续用 FastAPI、Django 时，`app/models/`、`app/api/` 这种目录结构就是包的应用。`__init__.py` 可以写包的初始化逻辑，也可以留空。
### 11.7 pip 安装第三方包
Python 生态里几十万个第三方包都通过 pip 安装。示例：安装 requests 发 HTTP 请求。
```bash
# 在 py310 环境里安装（先 conda activate py310）
pip install requests

# 或指定版本（推荐：版本确定，行为可复现）
pip install requests==2.32.3

# 查看已安装
pip show requests
```
安装后测试：
```python
# 本示例依赖第三方包 requests（2.32.x）
import requests

resp = requests.get("https://httpbin.org/get")
print(resp.status_code)          # 200
data = resp.json()               # 响应自动转成字典
print(data["origin"])            # 你的 IP
```
> ⚠️ **本指南中只有带「依赖第三方包」注释的示例需要先 pip install**。其余全部是标准库，开箱即用。requests 的详细用法（参数、超时、异常）会在大模型阶段一课程中大量出现，届时 `pip install openai` 调用大模型 API 的套路完全一致。
### 11.8 常用第三方包推荐表
| 包名 | 用途 | 学习时机 |
|------|------|---------|
| `requests` | HTTP 请求 | 阶段一 |
| `openai` | 调用大模型 API | 阶段一 |
| `jupyterlab` | 交互式笔记本 | 第 0 周环境准备 |
| `numpy` / `pandas` | 数值计算 / 数据分析 | 阶段二第 4 周 |
| `rich` | 终端美化输出 | 有需要再装 |
| `pytest` | 单元测试 | 阶段二之后 |
| `fastapi` / `uvicorn` | Web 框架 | Django学习路线 |
### 11.9 import 顺序规范
PEP8 约定 import 分组，组间空一行：
```python
# 第一组：标准库
import os
import sys
from pathlib import Path

# 第二组：第三方库
import requests

# 第三组：自己项目的模块
from mypackage import tools
```
---
## 十二、虚拟环境
> 📱 本章短，核心就一句话：**每个项目一个独立环境**。手机通读 + 上机走一遍流程。
### 12.1 为什么需要虚拟环境
项目 A 要 `requests 2.x`，项目 B 要 `requests 1.x`。都装进同一个环境，就会互相打架。虚拟环境给每个项目一套独立的 Python + 依赖库，互相隔离。
你已经见过一种虚拟环境：**conda 环境**（第一章建的 py310）。Python 官方还自带 `venv` 模块，两者的关系如下：
| 对比 | conda env | python -m venv |
|------|-----------|----------------|
| 谁提供 | Miniconda / Anaconda | Python 自带 |
| 创建命令 | `conda create -n 名字` | `python -m venv 名字` |
| 能指定 Python 版本 | 能 | 用当前 python |
| 适合场景 | 全栈数据科学、大模型 | 普通 Python 项目 |
### 12.2 venv 的使用
```bash
# 进入项目目录，创建虚拟环境（名字叫 .venv 是惯例）
cd myproject
python -m venv .venv

# 激活
# Windows：
.venv\Scripts\activate
# macOS / Linux：
source .venv/bin/activate

# 激活后，命令行提示符前会多出 (.venv)
# 之后所有 pip install 都装进这个环境
pip install requests

# 退出环境
deactivate
```
### 12.3 用 requirements.txt 锁定依赖
项目分享给别人时，把依赖清单写进 `requirements.txt`，别人一行命令装齐。
```bash
# 导出当前环境的依赖清单
pip freeze > requirements.txt
```
```text
# requirements.txt 内容示例
requests==2.32.3
openai==1.35.0
```
```bash
# 别人拿到项目后，一键安装所有依赖
pip install -r requirements.txt
```
> 💡 大模型课程第 0 周会让你 `pip install torch transformers datasets accelerate` 装一堆东西。装之前先创建 conda 环境（`conda create -n llm python=3.10`），再进环境安装，就能和系统其他 Python 完全隔离。这就是你现在学虚拟环境的价值。

---

## 十三、常用标准库
> 📱 本章是"工具箱"型章节：先手机通读知道每个工具干什么，上机时用「场景 → 函数」对照表速查即可，不需要背。
### 13.1 os：操作系统交互
```python
import os

# 目录操作
print(os.getcwd())            # 当前工作目录
os.mkdir("newdir")            # 创建目录（已存在会报错）
os.makedirs("a/b/c", exist_ok=True)   # 递归创建，存在也不报错
print(os.listdir("."))        # 列出当前目录内容

# 路径拼接（老式做法，新代码推荐 pathlib）
path = os.path.join("a", "b", "c.txt")
print(path)                   # a/b/c.txt

# 文件操作
print(os.path.exists("hello.txt"))   # 判断路径是否存在
print(os.path.getsize("hello.txt"))  # 文件大小（字节）
# 删除 os.remove("tmp.txt")，重命名 os.rename("旧名", "新名")
```
### 13.2 sys：与 Python 解释器交互
```python
import sys

# 命令行参数
print(sys.argv)
# 运行 python main.py hello 42
# 输出：['main.py', 'hello', '42']

# 退出程序
sys.exit("程序结束")     # 打印消息并以退出码 1 退出
# sys.exit(0)           # 正常退出

# 模块搜索路径
print(sys.path)          # Python 找模块的路径列表
```
> 💡 `sys.argv[0]` 永远是脚本文件名，真正的参数从 `sys.argv[1]` 开始。命令行参数更专业的处理用 argparse（13.8）。
### 13.3 json 回顾与深化
第十章已学基础。这里补充两个高频场景：
```python
import json

# 场景一：解析 API 返回的 JSON 字符串
api_response = '{"code": 0, "data": {"city": "北京", "temp": 25}}'
parsed = json.loads(api_response)
print(parsed["data"]["temp"])      # 25

# 场景二：保存和恢复配置
config = {
    "model": "deepseek-v4-flash",
    "temperature": 0.7,
    "max_tokens": 2048,
}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)
print(cfg["model"])                # deepseek-v4-flash
```
### 13.4 datetime：日期与时间
```python
from datetime import datetime, date, timedelta

# 获取当前时间
now = datetime.now()
print(now.year, now.month, now.day)   # 2026 8 26

# 格式化（ISO 8601 是 API 世界的日期标准）
print(now.strftime("%Y-%m-%d %H:%M:%S"))    # 2026-08-26 14:30:00
print(now.isoformat())                       # 2026-08-26T14:30:00.123456

# 字符串解析成 datetime：datetime.strptime("2026-08-26 14:30", "%Y-%m-%d %H:%M")

# 日期运算
tomorrow = date.today() + timedelta(days=1)
print(tomorrow)
```
| 格式符 | 含义 | 示例 |
|--------|------|------|
| `%Y` | 四位年份 | 2026 |
| `%m` | 两位月份 | 08 |
| `%d` | 两位日期 | 26 |
| `%H:%M:%S` | 时:分:秒 | 14:30:00 |
> 💡 **`isoformat()` 是重点**。大模型阶段二第 3 周的 compare_models 报告里就有 `"timestamp": datetime.now().isoformat()`，你现在认识它了。
### 13.5 pathlib：路径处理的现代方式
第十章已入门，这里补足常用操作：
```python
from pathlib import Path

base = Path("data")
base.mkdir(exist_ok=True)

# 批量处理目录下所有文件
for p in base.glob("*.txt"):           # 匹配当前层 *.txt
    print(p.name, p.read_text(encoding="utf-8"))

for p in base.rglob("*.json"):         # rglob 递归匹配所有层
    print(p)

# 判断与统计
print(base.is_dir())                   # True
print(Path("hello.txt").is_file())     # True

# 复制文件（用 shutil 配合）
import shutil
shutil.copy("hello.txt", "data/hello_copy.txt")
```
### 13.6 random：随机数
```python
import random

print(random.random())              # 0.0 到 1.0 的随机浮点数
print(random.randint(1, 100))       # 1 到 100 的随机整数（含两端）
print(random.uniform(1.5, 2.5))     # 指定范围的随机浮点数

# 从序列随机选
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))        # 随机选一个
print(random.sample(fruits, 2))     # 随机选 2 个不重复

# 打乱顺序（就地）
cards = list(range(10))
random.shuffle(cards)
print(cards)
```
> ⚠️ `random` 模块用于游戏、抽样、演示足够，但**不能用于安全场景**（密码、token）。安全随机用 `secrets` 模块。
### 13.7 collections：增强的数据结构
```python
from collections import Counter, defaultdict, deque

# Counter：统计出现次数
words = ["apple", "banana", "apple", "apple", "cherry"]
counts = Counter(words)
print(counts)                       # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(counts["apple"])              # 3
print(counts.most_common(2))        # [('apple', 3), ('banana', 1)]

# defaultdict：访问不存在的键时自动给默认值
d = defaultdict(list)               # 默认值是空列表
d["a"].append(1)                    # 无需先检查键是否存在
d["a"].append(2)
d["b"].append(3)
print(d)                            # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# deque：双端队列，两端都能高效增删
q = deque([1, 2, 3])
q.append(4)                         # 右侧加
q.appendleft(0)                     # 左侧加
print(q)                            # deque([0, 1, 2, 3, 4])
print(q.popleft())                  # 0，左侧弹出
```
> 💡 `defaultdict` 是数据分组的神器：`for cls, name in students: groups[cls].append(name)` 直接把 `[("一班","小明"),("二班","小红"),("一班","小刚")]` 分成 `{'一班': ['小明','小刚'], '二班': ['小红']}`，不用先判键是否存在。
### 13.8 argparse：命令行参数解析
给脚本加专业命令行参数，是 TODO 项目（第十五章）的核心。
```python
# cli_demo.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="示例命令行工具")
    parser.add_argument("name", help="你的名字")                  # 位置参数，必填
    parser.add_argument("--times", type=int, default=1, help="重复次数")  # 可选参数
    parser.add_argument("--verbose", action="store_true", help="详细模式")  # 开关

    args = parser.parse_args()

    for _ in range(args.times):
        print(f"你好，{args.name}")
    if args.verbose:
        print(f"参数详情：{args}")

if __name__ == "__main__":
    main()
```
运行：
```bash
python cli_demo.py 小明
python cli_demo.py 小红 --times 3
python cli_demo.py 小刚 --times 2 --verbose
python cli_demo.py --help      # 自动生成帮助文档
```
| 参数类型 | 写法 | 说明 |
|---------|------|------|
| 位置参数 | `add_argument("name")` | 必填，按位置传 |
| 可选参数 | `add_argument("--times")` | 带 `--` 前缀，可省略 |
| 类型转换 | `type=int` | 自动把字符串转 int |
| 默认值 | `default=1` | 没传时用默认 |
| 开关 | `action="store_true"` | 出现即为 True |
### 13.9 time 与 logging（了解）
```python
import time

# 计时
start = time.perf_counter()
time.sleep(0.5)                    # 暂停 0.5 秒
elapsed = time.perf_counter() - start
print(f"耗时：{elapsed:.3f} 秒")

# 时间戳
print(time.time())                 # 当前 Unix 时间戳（秒）
```
```python
# logging：比 print 专业的日志记录
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("程序启动")
logging.warning("磁盘空间不足")
logging.error("连接失败")
```
> 💡 阶段二第 3 周装饰器课程会做"计时装饰器"，用的正是 `time.perf_counter()` 和 `logging`。你现在知道这两个工具怎么用，到时直接照着写。
---
## 十四、PEP8 代码风格
> 📱 本章手机通读一遍，之后写代码时有意识地遵守。不必背，用工具自动检查（14.7）。
### 14.1 为什么要有代码规范
代码写出来不止给机器执行，还要给（未来的）人看。PEP8 是 Python 官方推荐的代码风格指南，统一风格的好处：整个社区代码长得差不多，你读别人代码、别人读你的代码都更快。
### 14.2 命名规范速查
| 对象 | 风格 | 示例 |
|------|------|------|
| 变量 / 函数 | snake_case 全小写下划线 | `user_name`、`get_name()` |
| 类 | PascalCase 单词首字母大写 | `TaskManager`、`LLMClient` |
| 常量 | 全大写下划线 | `MAX_RETRIES`、`TAX_RATE` |
| 私有变量 | 前导下划线 | `_internal` |
| 模块名 | 全小写下划线 | `my_module.py` |
| 包名 | 全小写（不用下划线） | `mypackage` |
### 14.3 布局规则
| 规则 | 说明 |
|------|------|
| 缩进 | 4 个空格，不用 Tab |
| 行宽 | 每行不超过 79（建议 100 以内）字符 |
| 空行 | 顶层函数/类之间空 2 行，类内方法之间空 1 行 |
| 引号 | 字符串单双引号均可，保持一致 |
| 行尾 | 不要有行尾空格 |
| 编码 | 文件统一 UTF-8（Python 3 默认） |
```python
# 顶层函数之间空两行
def first():
    pass


def second():
    pass


class MyClass:
    """类内方法之间空一行"""

    def method_a(self):
        pass

    def method_b(self):
        pass
```
### 14.4 空格规则
```python
# 运算符两侧加空格
x = 1 + 2

# 逗号、冒号后加空格
items = [1, 2, 3]
d = {"key": "value"}

# 冒号前不加空格（函数/类定义）
def func(a, b):
    pass

# 索引/切片不加空格
print(items[0])

# 默认参数等号两侧不加空格
def greet(name="小明"):
    pass
```
### 14.5 注释与 docstring
```python
# 单行注释：# 号后跟一个空格
# 计算税后价格

# 块注释
# 以下逻辑处理两种场景：
# 1. 会员价
# 2. 促销价

def function():
    """docstring：说明功能、参数、返回值。"""
    pass
```
### 14.6 坏代码 vs 好代码
```python
# ❌ 坏代码：缩进混乱、命名随意、魔法数字
def calc(a,b,c):
  t=a*0.13
  if c>100:
    return a+b+t-c
  else:
   return a+b+t

# ✅ 好代码：清晰缩进、见名知义、常量有名字
TAX_RATE = 0.13

def calc_total(price, shipping, discount=0):
    """计算订单总价：商品价 + 运费 - 折扣 + 税费"""
    tax = price * TAX_RATE
    total = price + shipping + tax - discount
    return total
```
### 14.7 工具：自动检查与格式化
| 工具 | 作用 | 使用 |
|------|------|------|
| ruff | 快速检查 PEP8 违规 | `pip install ruff` 然后 `ruff check .` |
| black | 自动格式化代码 | `pip install black` 然后 `black 文件.py` |
```bash
pip install ruff black
ruff check myproject/           # 检查问题
black myproject/                # 自动改格式
```
> 💡 现在不需要装。等你写完第十五章的 TODO 项目，用 `black todo.py` 格式化一遍，再 `ruff check todo.py` 检查一遍，你会直观感受到规范工具的价值。
---
## 十五、实战项目：命令行 TODO 工具
> 💻 本章是整本指南的验收项目，必须亲手敲完。建议留出完整的 2 到 3 小时：先看思路，再独立写，最后对照完整代码查漏。
### 15.1 项目需求
做一个命令行 TODO 工具，支持五种操作：
```text
python todo.py add 学Python基础      # 添加任务
python todo.py list                  # 查看所有任务
python todo.py done 2                # 把第 2 条任务标记为完成
python todo.py delete 1              # 删除第 1 条任务
python todo.py clear                 # 清空所有任务
```
**功能要求**：
| 功能 | 说明 |
|------|------|
| 数据持久化 | 任务保存到 `tasks.json`，程序退出后数据不丢 |
| 任务状态 | 每条任务有 标题 / 是否完成 / 创建时间 |
| 命令行参数 | 用 argparse 解析 |
| 面向对象 | Task 类 + TaskManager 类 |
| 优雅报错 | 删除不存在的任务、参数缺失时给出友好提示 |
**这个项目覆盖了本指南哪些内容**：OOP（第八章）、异常处理（第九章）、文件与 json（第十章）、模块结构（第十一章）、argparse（第十三章）、PEP8（第十四章）。全部写完后，你还剩 `if __name__ == "__main__"` 这个固定模板没串起来，现在串上。
### 15.2 设计思路

三层分工：**main() 解析命令行参数并分发操作 → TaskManager 管理任务列表（加载/保存/增删改查）→ Task 描述单条任务（标题/状态/时间，负责与 json 互转）**。

**数据流**：命令行参数 → 操作分发 → TaskManager 改内存里的任务列表 → 每次改动后 `_save()` 同步到 tasks.json，程序退出数据不丢。
### 15.3 完整代码：todo.py
```python
# todo.py 命令行 TODO 工具
# 用法：
#   python todo.py add 任务内容     添加任务
#   python todo.py list             查看任务
#   python todo.py done 编号        完成任务
#   python todo.py delete 编号      删除任务
#   python todo.py clear            清空任务
import argparse
import json
from datetime import datetime
from pathlib import Path


class Task:
    """单个任务的数据模型"""

    def __init__(self, title, done=False, created_at=None):
        self.title = title
        self.done = done
        self.created_at = created_at or datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        """转成字典，方便 json 序列化"""
        return {
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        """从字典恢复 Task 实例"""
        return cls(data["title"], data["done"], data["created_at"])

    def __str__(self):
        status = "✓" if self.done else " "
        return f"[{status}] {self.title}（{self.created_at}）"


class TaskManager:
    """任务管理器：负责加载、保存、增删改查"""

    def __init__(self, path="tasks.json"):
        self.path = Path(path)
        self.tasks = self._load()

    def _load(self):
        """从文件加载任务列表，文件不存在时返回空列表"""
        if not self.path.exists():
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Task.from_dict(item) for item in data]

    def _save(self):
        """把当前任务列表写回文件"""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=2)

    def add(self, title):
        """添加任务"""
        self.tasks.append(Task(title))
        self._save()
        print(f"已添加任务：{title}")

    def list_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("任务列表是空的，用 add 添加第一条吧")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def done(self, index):
        """按编号把任务标记为完成"""
        try:
            task = self.tasks[index - 1]
        except IndexError:
            print(f"没有第 {index} 个任务")
            return
        task.done = True
        self._save()
        print(f"已完成：{task.title}")

    def delete(self, index):
        """按编号删除任务"""
        try:
            task = self.tasks.pop(index - 1)
        except IndexError:
            print(f"没有第 {index} 个任务")
            return
        self._save()
        print(f"已删除：{task.title}")

    def clear(self):
        """清空所有任务"""
        self.tasks.clear()
        self._save()
        print("已清空所有任务")


def main():
    parser = argparse.ArgumentParser(description="命令行 TODO 工具")
    parser.add_argument("action", choices=["add", "list", "done", "delete", "clear"],
                        help="要执行的操作")
    parser.add_argument("args", nargs="*", help="操作参数（任务内容或编号）")
    args = parser.parse_args()

    manager = TaskManager()

    if args.action == "add":
        title = " ".join(args.args).strip()
        if not title:
            print("用法：python todo.py add 任务内容")
            return
        manager.add(title)
    elif args.action == "list":
        manager.list_tasks()
    elif args.action == "done":
        if not args.args:
            print("用法：python todo.py done 编号")
            return
        manager.done(int(args.args[0]))
    elif args.action == "delete":
        if not args.args:
            print("用法：python todo.py delete 编号")
            return
        manager.delete(int(args.args[0]))
    elif args.action == "clear":
        manager.clear()


if __name__ == "__main__":
    main()
```
### 15.4 运行演示
在项目目录执行：
```bash
python todo.py add 学完Python基础指南
python todo.py add 安装Ollama
python todo.py add 跑通DeepSeek API
python todo.py list
```
输出：
```text
已添加任务：学完Python基础指南
已添加任务：安装Ollama
已添加任务：跑通DeepSeek API
1. [ ] 学完Python基础指南（2026-08-26T15:10:22）
2. [ ] 安装Ollama（2026-08-26T15:10:25）
3. [ ] 跑通DeepSeek API（2026-08-26T15:10:28）
```
继续：
```bash
python todo.py done 2
python todo.py list
python todo.py delete 1
python todo.py list
```
输出：
```text
已完成：安装Ollama
1. [ ] 学完Python基础指南（2026-08-26T15:10:22）
2. [✓] 安装Ollama（2026-08-26T15:10:25）
3. [ ] 跑通DeepSeek API（2026-08-26T15:10:28）
已删除：学完Python基础指南
1. [✓] 安装Ollama（2026-08-26T15:10:25）
2. [ ] 跑通DeepSeek API（2026-08-26T15:10:28）
```
看一眼生成的 `tasks.json`：
```json
[
  {
    "title": "安装Ollama",
    "done": true,
    "created_at": "2026-08-26T15:10:25"
  },
  {
    "title": "跑通DeepSeek API",
    "done": false,
    "created_at": "2026-08-26T15:10:28"
  }
]
```
**异常测试**（故意乱操作，验证不会崩）：`python todo.py done 99` 提示"没有第 99 个任务"；`python todo.py add` 提示用法；`python todo.py 乱来` 报 argparse 错误并提示合法操作。
### 15.5 代码复盘：每一块为什么这么写
| 代码 | 为什么 |
|------|--------|
| `class Task` | 数据模型：描述"一条任务长什么样" |
| `to_dict` / `from_dict` | 对象和字典互转的桥，字典才能存进 json |
| `@classmethod from_dict` | 用类方法做"从字典构造"，比直接改 `__init__` 干净 |
| `datetime.now().isoformat()` | 生成创建时间戳，`timespec="seconds"` 去掉毫秒 |
| `self._load()` 在 `__init__` 里调用 | 创建 manager 时任务已就位，后面方法直接操作 `self.tasks` |
| `_save()` 每次改动后调用 | 保证数据不丢，这是"持久化"的全部秘密 |
| `try/except IndexError` | 用户可能给不存在的编号，异常处理让它优雅降级 |
| `nargs="*"` | add 的任务内容可能含空格，`join` 还原完整句子 |
| `if __name__ == "__main__":` | 只有直接运行时才执行 main，被 import 时不触发 |
### 15.6 扩展挑战（选做）
完成基础版后，选 1 到 2 个扩展，把本领长实：
```text
□ 统计：list 时显示「共 N 条，M 条未完成」
□ 优先级：任务支持 high/medium/low，list 时高优先级排前面
□ 日期筛选：list --today 只看今天的任务
□ 分类：add --tag 工作/生活，按 tag 筛选
□ 交互模式：不带参数运行进入交互式界面（while + input）
□ 单元测试：用 pytest 给 TaskManager 写 3 个测试用例
```
> 🏆 **里程碑达成**：你现在拥有一个自己写出来的、能持久化数据的命令行工具。这个项目对应的正是 Django 学习路线里「阶段 1 第 3 周实战项目：命令行 TODO 工具」的要求。你已经有资格进入大模型学习了。
---
## 十六、章节练习题汇总
> 💻 每题先在电脑上独立完成，再对照 16.18 的参考答案。**参考答案不是标准答案**，思路合理、结果正确就是好代码。
### 16.1 环境与工具（第一章）
1. 用一条命令创建名为 `test_env`、Python 3.10 的 conda 环境并激活
2. 写出你电脑上 `python --version` 的输出
3. 新建 `hello.py`，让用户输入名字后打印 `你好，名字，Python 欢迎你`
4. 用 pip 安装 `requests==2.32.3`，再用 `pip show requests` 确认
### 16.2 变量与类型（第二章）
1. 交换两个变量的值（要求：不用第三个变量）
2. 计算摄氏温度 37 度对应的华氏温度，公式 `F = C * 9/5 + 32`
3. 分别计算 `7 // 2`、`-7 // 2`、`7 % 2`、`2 ** 10` 并说出含义
4. 写代码验证：`0.1 + 0.2` 不等于 `0.3`，然后用"差的绝对值小于 1e-9"的方式判断它们近似相等
5. 用 `input()` 读入两个数字并输出它们的和（注意类型转换）
### 16.3 字符串（第三章）
1. 把字符串 `"Hello, World"` 中的 `World` 替换成 `Python`
2. 输入一行逗号分隔的名字 `"小明,小红,小刚"`，用 split 拆成列表并打印
3. 用 f-string 打印九九乘法表的其中一行：`3 x 7 = 21`
4. 把一个字符串反转（提示：切片）
5. 判断用户输入的字符串是否全部是数字，是则转 int 输出，否则提示
### 16.4 列表与元组（第四章）
1. 生成 1 到 100 的整数列表，输出其中能被 7 整除的所有数
2. 求列表 `[72, 88, 95, 60, 41]` 的最高分、最低分、平均分（保留一位小数）
3. 用 `b = a.copy()` 复制一个列表，修改其中一个，确认另一个不受影响
4. 已知 `names = ["小明", "小红"]` 和 `scores = [90, 85]`，用 zip 打印 `小明: 90` 格式
5. 元组 `(1, 2, 3)` 转成列表，再转回元组
### 16.5 字典与集合（第五章）
1. 建一个"姓名 -> 电话"字典，添加两个联系人，删除一个，用 get 查一个不存在的联系人
2. 统计字符串 `"hello world hello python hello"` 中每个单词出现的次数（用字典）
3. 有两个列表 `a = [1, 2, 2, 3]` 和 `b = [2, 3, 4]`，找出 a 有 b 没有的元素
4. 模拟大模型 messages：构造一个包含 system 和 user 两条消息的列表，遍历打印 role 和 content
### 16.6 条件与循环（第六章）
1. 输入一个成绩，输出等级（90+ 为 A，80+ 为 B，60+ 为 C，否则 D）
2. 用 while 实现：不断让用户输入，直到输入 `quit` 才退出
3. 用 for 循环计算 1 到 100 所有奇数的和
4. 用列表推导式生成 1 到 20 中能被 3 整除的数的平方
5. 打印一个 5 行 5 列的乘法表（嵌套循环）
### 16.7 函数（第七章）
1. 写 `is_prime(n)` 判断质数，返回布尔
2. 写 `fizzbuzz(n)`：1 到 n，能被 3 整除打印 Fizz，能被 5 整除打印 Buzz，都能打印 FizzBuzz
3. 写一个 `sum_all(*nums)` 求任意个数的和
4. 用 lambda 配合 sorted 按字典的 value 排序
5. 写 `make_multiplier(n)` 返回一个函数，这个函数把输入乘以 n（闭包练习）
### 16.8 面向对象（第八章）
1. 定义 `Rectangle` 类：属性宽高，方法 `area()` 和 `perimeter()`
2. 给 Rectangle 加 `__str__` 和 `__eq__`（面积相等则相等）
3. 定义 `Square(Rectangle)`，初始化只传边长，复用父类方法
4. 用 property 实现 `Circle`：属性 `radius`，只读属性 `area`
5. 设计 `BankAccount`：存款、取款（余额不足抛自定义异常）、查询余额
### 16.9 异常处理（第九章）
1. 写一个函数 `safe_divide(a, b)`：b 为 0 时返回 `"不能除以零"`，否则返回结果
2. 让用户输入一个整数，循环直到合法（提示：try/except + while）
3. 打开一个不存在的文件，捕获 FileNotFoundError 并打印友好信息
4. 写自定义异常 `NegativeError`，在负数输入时抛出
### 16.10 文件读写（第十章）
1. 写程序把 1 到 100 的数字每行一个写进 `numbers.txt`
2. 读回 `numbers.txt`，求和并打印
3. 把字典 `{"name": "小明", "age": 18}` 存成 JSON 文件，再读回来验证
4. 生成一个学生成绩 CSV（3 人 × 3 科），用 DictReader 读取并打印每个人的总分
5. 用 pathlib 判断 `numbers.txt` 是否存在、大小多少、扩展名是什么
### 16.11 模块与包（第十一章）
1. 建一个 `math_utils.py`，放 `add`、`mul` 两个函数和 `PI` 常量
2. 建 `main.py` 从 `math_utils` 导入并使用
3. 在 `math_utils.py` 里加 `if __name__ == "__main__":` 打印一段说明，分别用直接运行和 import 两种方式观察行为
4. 用 pip 安装 `rich`，运行 `python -m rich` 确认安装成功
### 16.12 虚拟环境（第十二章）
1. 为一个新项目创建 venv 并激活，确认提示符出现环境名
2. 在环境里安装 `requests`，`pip freeze > requirements.txt`，查看文件内容
3. 新建一个 conda 环境 `demo`，对比 venv 和 conda 环境的创建命令差异
### 16.13 标准库（第十三章）
1. 用 datetime 打印 `今天是 2026年08月26日 星期三` 格式的今天日期
2. 用 Counter 统计一篇文章（字符串）中每个字母的出现次数
3. 用 argparse 写一个工具：`tool.py greet 名字 --times 次数`
4. 用 pathlib 遍历当前目录，打印所有 .py 文件的文件名和大小
5. 用 random 实现：从 1 到 100 随机抽 5 个不重复的数字
### 16.14 PEP8（第十四章）
1. 找出并修正下面代码的所有风格问题（命名、缩进、空格、魔法数字）：
```python
def Area(r):
  return 3.14159*r*r

x=[1,2,3]
for i in x:print(i)
```
2. 用 `black` 和 `ruff` 检查你自己写的某个练习文件
### 16.15 实战项目验收（第十五章）
1. 独立完成 todo.py（不看答案），并跑通五种操作
2. 验证数据持久化：add 后退出程序，再 list 任务还在
3. 验证容错：`done 999`、`add`（缺参数）都不崩溃，并选做扩展挑战中的任意 2 项
### 16.16 综合题：学生成绩管理系统
把全指南内容串成一个综合小项目，模拟第八章到第十四章的综合验收：
```text
功能要求：
- Student 类：name、scores（字典：科目 -> 分数）
- 支持：添加学生、输入成绩、查询某学生的平均分、按平均分排名、保存到 JSON
- 数据文件 students.json，重启后数据不丢
- 命令行交互式界面（while + input），输入 quit 退出
```
### 16.17 综合题：日志分析小工具
```text
功能要求：
- 读入一个日志文件（每行形如：2026-08-26 15:00:12 INFO 用户登录成功）
- 统计每种级别的条数（INFO / WARNING / ERROR）
- 输出 ERROR 级别日志的行数
- 把统计结果写入 report.txt
- 用函数组织代码，每个函数有 docstring
```
### 16.18 参考答案（精选）
> 只给出重点题的参考实现。其余题目用「打印中间结果、逐步拆解」的方式自行验证，这本身就是编程能力。
**16.5 第 2 题：单词计数**
```python
text = "hello world hello python hello"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)   # {'hello': 3, 'world': 1, 'python': 1}

# 或用 Counter 一行
from collections import Counter
print(Counter(text.split()))
```
**16.7 第 1 题：质数判断**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))   # True
print(is_prime(15))   # False
```
**16.7 第 5 题：闭包**
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))   # 20
print(triple(10))   # 30
```
**16.8 第 1 + 2 题：Rectangle**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

    def __eq__(self, other):
        return self.area() == other.area()

r1 = Rectangle(2, 3)
r2 = Rectangle(1, 6)
print(r1.area())        # 6
print(r1.perimeter())   # 10
print(r1 == r2)         # True，面积相等
```
**16.8 第 3 题：Square 继承**
```python
# 依赖上一个答案中的 Rectangle 类（写在同一文件里）
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

s = Square(4)
print(s.area())         # 16
print(s.perimeter())    # 16
```
**16.8 第 5 题：BankAccount**
```python
class BalanceNotEnoughError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须为正")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise BalanceNotEnoughError(
                f"余额不足：需要 {amount}，现有 {self.balance}"
            )
        self.balance -= amount

    def get_balance(self):
        return self.balance

acct = BankAccount("小明", 100)
acct.deposit(50)
acct.withdraw(30)
print(acct.get_balance())   # 120
```

> 💡 16.16 综合题没有参考答案，因为它的套路与第十五章 todo.py 完全一致：Student 类对应 Task 类，StudentManager 对应 TaskManager，JSON 持久化和命令行交互直接照搬。独立完成它，就是你打通本指南的毕业作品。

---
## 十七、衔接说明：进入大模型学习
### 17.1 你现在已经掌握了什么
对照这份能力清单，逐项确认。全部能独立做到，就具备了仓库里所有大模型课程的前提。
| 能力 | 对应章节 | 自检方式 |
|------|---------|---------|
| 搭好 Python 3.10 环境 | 一 | 能新建 conda 环境并跑 .py 文件 |
| 熟练使用基本类型和运算符 | 二 | 不看笔记写出温度换算 |
| 字符串处理与格式化 | 三 | 不用 f-string 以外的方式拼出报告文本 |
| 列表、元组、字典、集合 | 四、五 | 能从嵌套字典里安全取到值 |
| 分支、循环、推导式 | 六 | 推导式生成筛选后的列表 |
| 函数、args、kwargs、lambda | 七 | 能解释 `**kwargs` 透传参数 |
| 面向对象、继承、super | 八 | 能设计"基类 + 子类"并切换实现 |
| 异常处理与自定义异常 | 九 | 输入错误、文件缺失都不崩 |
| 文件、json、csv 读写 | 十 | 能把对象存进 json 再读回来 |
| 模块化与 __main__ 守卫 | 十一 | 每个脚本用 `main()` + 守卫收尾 |
| 虚拟环境与依赖管理 | 十二 | 新建 venv、导出 requirements.txt |
| 标准库常用模块 | 十三 | datetime、Counter、argparse 随手能用 |
| 代码风格 | 十四 | 命名规范、4 空格缩进成为习惯 |
| 完整项目 | 十五 | 独立完成 todo.py 五种操作 |
### 17.2 下一步：走仓库的官方路线
现在回到 learning-hub 仓库的根目录，按顺序进入大模型学习：
**第一步：环境准备（第 0 周）**
打开 `大模型学习/01-总纲-6个月大模型学习计划.md` 的第 2 节「环境准备（第 0 周）」。
> 你在本指南第一章已经装好 Miniconda 并建过 py310 环境，这里的命令你会非常眼熟：
>
> ```bash
> conda create -n llm python=3.10
> conda activate llm
> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
> pip install wandb transformers datasets accelerate
> pip install jupyterlab
> ```
>
> 照着 2.1 到 2.4 的清单逐项完成即可，无需任何额外学习。
**第二步：阶段一（第 1-2 周）**
打开 `大模型学习/03-阶段一-大模型开发入门.md`。
> 阶段一教你部署本地模型、写 Prompt、调 API、搭带记忆的 ChatBot。它使用的 Python 语法全部在本指南覆盖范围内：
>
> | 阶段一会出现 | 你在本指南哪里学过 |
> |-------------|------------------|
> | `messages = [{"role": "user", "content": ...}]` | 5.6 嵌套字典 |
> | `for msg in messages:` | 5.5 字典遍历 |
> | `client.chat.completions.create(model=..., messages=..., **kwargs)` | 7.8 **kwargs |
> | `if __name__ == "__main__":` 循环 ChatBot | 11.5 主程序守卫 |
> | `json.dump / json.load` 保存对话历史 | 10.6 JSON 持久化 |
> | `datetime.now().isoformat()` | 13.4 datetime |
**第三步：阶段二第 3 周（Python 工程化强化）**
打开 `大模型学习/04-阶段二-大模型应用开发.md`，进入第 3 周。
> 第 3 周共有四个主题：装饰器、迭代器与生成器、面向对象设计 LLM Client、asyncio。其中三个你已经打好地基：
>
> | 第 3 周主题 | 你的地基 | 你还需要新学的 |
> |------------|---------|--------------|
> | 星期一 装饰器 | 7.11 闭包、第七章函数 | @ 语法糖、@wraps |
> | 星期二 迭代器/生成器 | 6.5 for 循环、10.2 逐行读文件 | yield、next() |
> | 星期三 OOP 设计 LLM Client | 8.10 预告实战、8.5/8.6 继承与 super | 无，骨架你已经写过 |
> | 星期四 asyncio | 9.8 网络请求异常、13.9 time | async/await、gather |
>
> 特别是 8.10 那个 LLMClient 雏形，正是第 3 周星期三「用 OOP 设计 LLMClient」的迷你版。到时候把 `print` 模拟换成真实的 openai 调用，就是课程要的成品。
### 17.3 本指南刻意没深入的内容（交给阶段二）
为了让第 3 周保持新鲜感和挑战性，以下内容本指南只给了指针，**详细教程在阶段二第 3 周**：
| 主题 | 本指南只提到了 | 阶段二第 3 周会教你 |
|------|--------------|-------------------|
| 装饰器 | 7.11 闭包一句话 | @ 语法糖、三层嵌套、计时/日志/重试装饰器 |
| 生成器 | 6.8 推导式、10.2 逐行读文件 | yield 暂停恢复、大文件流式处理 |
| asyncio | 9.8 网络请求、13.9 time | async/await、asyncio.gather、Semaphore |
| 迭代器协议 | 6.5 for 底层 | `__iter__` / `__next__` |
> 这也是仓库的设计原则：**手机阅读输入，电脑编码输出，全程不依赖视频**。你现在通读的是纯文字、可搜索、可离线学习的指南，进入大模型课程后依然是这套打法。
### 17.4 学习纪律提醒

进入大模型学习前，再读一遍仓库的学习哲学：

1. **允许降级，不允许归零**：哪天太累，读半小时手机部分就算完成当天任务，但不要整天零学习
2. **先跑通再理解**：代码先运行起来看到输出，再回头琢磨原理；电脑时段结束后，磁盘上要有能运行的 .py 文件
3. **遇到报错先自己读**：异常信息（第九章）第一行就是答案的一半
4. **知识库化**：像 8.10 的 LLMClient 雏形那样，把关键代码存档进你的 Obsidian，随时回看
> 🎓 **最后一句话**：你已经完成了从零到能写命令行工具、能处理 JSON 数据、能设计类体系的跨越。大模型课程需要的 Python 基础，到此全部就位。接下来，去和真正的 AI 对话吧。
