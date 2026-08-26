# 前端基础完全指南（HTML + CSS + JavaScript）

> 适用对象：Python / Django 后端学习者，零前端基础，需要为 Django 模板和全栈计划阶段 5 补齐前端地基
> 涵盖：HTML、CSS、原生 JavaScript、浏览器调试、3 个可运行实战、与 Django 模板的结合
> 学习方式：📱 手机读概念，💻 电脑抄代码，全程不依赖视频
> 前置要求：会 Python 基础语法。本指南大量用 Python 类比讲解 JS，学起来会很快
> 关联文档：《Django 完全指南》第 6 章（模板层）、第 11 章（静态文件）、《Python 全栈工程师完整学习计划》阶段 5、`API学习/demo/server.py`

---

## 目录

1. [前端技术栈全景](#一前端技术栈全景)
2. [HTML：网页的结构](#二html网页的结构)
3. [CSS：网页的样式](#三css网页的样式)
4. [JavaScript：网页的行为](#四javascript网页的行为)
5. [浏览器开发者工具](#五浏览器开发者工具)
6. [实战 1：纯静态个人主页](#六实战-1纯静态个人主页)
7. [实战 2：待办事项应用](#七实战-2待办事项应用)
8. [实战 3：用 fetch 对接后端 API](#八实战-3用-fetch-对接后端-api)
9. [与 Django 模板的结合](#九与-django-模板的结合)
10. [前端学习下一步路线](#十前端学习下一步路线)
11. [章节练习汇总](#十一章节练习汇总)

---

## 一、前端技术栈全景

### 1.1 三个角色的分工 📱

浏览器里显示的任何网页，背后都是三种语言在协作：

```
┌───────────────────────────────────────────────────┐
│                    浏览器                          │
│                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────┐  │
│  │    HTML      │  │     CSS      │  │   JS    │  │
│  │  结构（骨架） │  │  样式（外观）  │  │ 行为（动作）│  │
│  │ <p>一段文字</p>│  │ color: red   │  │ 点击后变色 │  │
│  └──────────────┘  └──────────────┘  └─────────┘  │
│                   ↑  ↑  ↑                        │
│         三者共同决定浏览器如何绘制页面               │
│                                                   │
│       HTTP 请求 / 响应（阶段 2 已学过）              │
└───────────────────────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │        后端（Django / API）       │
        │ 处理请求、读写数据库、返回数据     │
        └─────────────────────────────────┘
```

| 语言 | 角色 | 通俗类比 | 你的 Python 类比 |
|------|------|----------|------------------|
| **HTML** | 结构：定义页面上有什么内容 | 一栋房子的钢筋骨架 | 数据结构和模板 |
| **CSS** | 样式：定义这些内容长什么样 | 房子的装修、配色、家具摆放 | 无直接类比，是纯声明式配置 |
| **JavaScript** | 行为：定义页面如何响应操作 | 房子里的水电和智能开关 | 你写的 Python 业务逻辑 |

三句话记住：

- HTML 决定「页面上有什么」。一个标题、一个按钮、一张图片，都是 HTML。
- CSS 决定「它们长什么样」。红色还是蓝色、宽还是窄、在左边还是右边。
- JavaScript 决定「它们干什么」。点击按钮弹出提示、输入框实时搜索、从后端拉数据。

> 📱 后端代码跑在 Python 解释器里，前端代码跑在浏览器里。你写的 HTML/CSS/JS 不需要安装任何东西，浏览器（Chrome、Edge、Firefox）开箱即用：写后端要 `pip install`、起服务、curl 测试；写前端只需要一个文本编辑器加一个浏览器，双击 HTML 文件就能看到效果。这也是本指南所有实战都「能在普通浏览器里直接看」的原因。

### 1.2 两种 Web 开发模式 📱

你学 Django 时接触的是**前后端不分离**模式，全栈计划阶段 5 的 React 走的是**前后端分离**模式。两种模式都要先懂 HTML/CSS/JS，区别只在数据怎么来：

```
模式 A：前后端不分离（Django 模板）
请求 /books → 视图查数据库 → 模板把数据填进 HTML
→ 返回「已带数据」的完整页面 → 浏览器直接显示
JS 只负责次要交互，不负责拿数据

模式 B：前后端分离（fetch + API）
打开静态页面 → JS 用 fetch 请求后端 → 后端返回 JSON
→ JS 自己把数据渲染成 HTML → 页面动态更新
```

Django 学的是模式 A，本指南实战 3 会用 fetch 演示模式 B，正好把 `API学习/demo/server.py` 那个 API 用起来。模式 A 和 B 你都得会，因为阶段 5 的 React 项目是模式 B。

### 1.3 浏览器如何把代码变成画面 📱

```
HTML ──解析──→ DOM 树（文档对象模型：页面内容的内存结构）
CSS  ──解析──→ CSSOM（样式规则）
                    ↓
        DOM + CSSOM 合并成渲染树
                    ↓
            布局（算每个元素的位置和大小）
                    ↓
            绘制（把像素画到屏幕上）
```

这个流程不用背，但「**DOM 树**」这个概念必须记住：JavaScript 改页面，本质就是改这棵树。第 4 章会细讲。

---

## 二、HTML：网页的结构

### 2.1 文档基本结构 💻

HTML 不是编程语言，而是一种**标记语言**：用标签（tag）把内容「标记」出来。新建一个 `index.html`，把下面代码原样复制进去，双击用浏览器打开：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>我的第一个网页</title>
</head>
<body>
  <h1>你好，世界</h1>
  <p>这是我的第一个网页。</p>
</body>
</html>
```

逐行解释：

| 代码 | 作用 |
|------|------|
| `<!DOCTYPE html>` | 声明这是 HTML5 文档。必须写在第一行，让浏览器用标准模式解析 |
| `<html lang="zh-CN">` | 整个页面的根元素。`lang` 告诉浏览器页面是中文，影响朗读和拼写检查 |
| `<head>` | 页面的「配置区」，里面的内容不会显示在页面上 |
| `<meta charset="UTF-8">` | 声明字符编码为 UTF-8。**不写这句中文必乱码** |
| `<meta name="viewport" ...>` | 让页面在手机上按屏幕宽度显示。响应式布局必备 |
| `<title>` | 浏览器标签页上显示的文字 |
| `<body>` | 页面「内容区」，所有能看见的东西都写在这里 |

> 📱 记忆法：`<head>` 是脑，`<body>` 是身。脑里是配置，身里是内容。

每个 HTML 文件都要有上面这个骨架。后面的实战项目都会从这段骨架开始。

### 2.2 标签、元素与属性 💻

**标签**是尖括号包裹的关键字，分两种：

```html
<!-- 成对标签：有开始有结束 -->
<p>这是一段文字</p>
<h1>标题</h1>

<!-- 自闭合标签：没有内容，自己结束（单标签） -->
<br>      <!-- 换行 -->
<img src="logo.png" alt="logo">
```

**元素** = 开始标签 + 内容 + 结束标签。`<p>你好</p>` 整体是一个 `<p>` 元素。

**属性**写在开始标签里，用来给元素附加信息，格式是 `属性名="值"`：

```html
<a href="https://www.example.com" target="_blank" title="点击跳转">示例链接</a>
<img src="photo.jpg" alt="一张照片" width="300">
```

| 常用属性 | 用在谁身上 | 作用 |
|----------|-----------|------|
| `id="xxx"` | 任何元素 | 唯一标识，一个页面里只能出现一次。CSS 和 JS 都靠它定位元素 |
| `class="xxx"` | 任何元素 | 样式类名，可以重复。CSS 主力选择器 |
| `src="..."` | img / script / video | 资源地址 |
| `href="..."` | a | 链接目标 |
| `alt="..."` | img | 图片加载失败时显示的文字，也供读屏软件朗读。**每张图片都要写** |
| `title="..."` | 任何元素 | 鼠标悬停时显示的小提示 |
| `lang="..."` | html | 页面语言 |
| `style="..."` | 任何元素 | 内联样式（第 3 章讲，日常少用） |

### 2.3 文本与标题 💻

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<!-- h1 到 h6，总共六级，h1 只能有一个，是页面最重要的标题 -->

<p>这是一个段落。段落之间会自动换行并留出间距。</p>

<strong>加粗文字</strong>          <!-- 语义：重要 -->
<em>斜体文字</em>                  <!-- 语义：强调 -->
<br>                              <!-- 强制换行 -->
<hr>                              <!-- 水平分割线 -->

<blockquote>这是一段引用，浏览器默认缩进显示。</blockquote>

<pre>
function hello() {
  console.log('保留空格和换行的代码块');
}
</pre>
```

> 📱 用 `<strong>` 不用 `<b>`，用 `<em>` 不用 `<i>`。`<b>` 和 `<i>` 只是视觉加粗/斜体，而 `<strong>` 和 `<em>` 还带着「重要/强调」的语义，对无障碍和 SEO 更友好。旧标签表格见 2.10。

### 2.4 链接与图片 💻

```html
<!-- 基本链接 -->
<a href="https://www.python.org">Python 官网</a>

<!-- 新标签页打开。写 target="_blank" 时必须带上 rel="noopener"，
     防止新页面通过 window.opener 反向控制你的页面（安全漏洞） -->
<a href="https://www.python.org" target="_blank" rel="noopener">新标签页打开</a>

<!-- 页内锚点：跳转到本页 id 为 intro 的元素 -->
<a href="#intro">跳到简介</a>
<h2 id="intro">简介</h2>

<!-- 图片 -->
<img src="cat.jpg" alt="一只猫" width="300">
```

### 2.5 列表 💻

```html
<!-- 无序列表：项目符号 -->
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>JavaScript</li>
</ul>

<!-- 有序列表：自动编号 -->
<ol>
  <li>第一步：写 HTML</li>
  <li>第二步：写 CSS</li>
  <li>第三步：写 JS</li>
</ol>

<!-- 嵌套列表 -->
<ul>
  <li>后端
    <ul>
      <li>FastAPI</li>
      <li>Django</li>
    </ul>
  </li>
  <li>前端</li>
</ul>
```

> 📱 列表是网页最常见的结构。导航菜单、文章列表、选项组，全是 `<ul><li>`。

### 2.6 表格 💻

```html
<table>
  <caption>2026 年学习计划</caption>
  <thead>
    <tr>
      <th>阶段</th>
      <th>内容</th>
      <th>时长</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>阶段 4</td>
      <td>后端框架</td>
      <td>4 周</td>
    </tr>
    <tr>
      <td>阶段 5</td>
      <td>前端框架</td>
      <td>5 周</td>
    </tr>
  </tbody>
</table>
```

| 标签 | 含义 |
|------|------|
| `<table>` | 表格 |
| `<caption>` | 表格标题（可选） |
| `<thead>` / `<tbody>` | 表头 / 表体（把表头和内容分开，方便加样式） |
| `<tr>` | 一行（table row） |
| `<th>` | 表头单元格，默认加粗居中 |
| `<td>` | 普通单元格（table data） |

> 📱 表格只用来展示「真正的表格数据」（报表、对比、日历）。做页面布局请用 Flex 和 Grid（第 3 章），那是现代做法。用 `<table>` 拼页面布局是 2005 年的老古董做法。

### 2.7 语义化标签 📱

HTML5 提供了一批「自带含义」的标签，替代到处乱飞的 `<div>`：

```
┌─────────────────────────────────────────┐
│ <header>      页头：logo + 导航            │
│   <nav> 首页 文章 关于我 </nav>            │
├─────────────────────────────────────────┤
│ <main>                                  │
│   <article>                            │
│     <h2>文章标题</h2>                    │
│     <p>文章正文…</p>                     │
│   </article>                           │
│   <aside>侧边栏：相关推荐</aside>          │
├─────────────────────────────────────────┤
│ <footer>      页脚：版权信息               │
└─────────────────────────────────────────┘
```

```html
<header>    <!-- 页头 -->
  <nav>     <!-- 导航 -->
    <a href="/">首页</a>
    <a href="/about">关于</a>
  </nav>
</header>

<main>      <!-- 页面主体，一个页面只能有一个 -->
  <section> <!-- 内容分区 -->
    <h2>技能</h2>
    <ul>
      <li>Python</li>
      <li>Django</li>
    </ul>
  </section>

  <article> <!-- 独立内容块：一篇文章、一条新闻 -->
    <h2>文章标题</h2>
    <p>正文内容</p>
    <figure>
      <img src="diagram.png" alt="架构图">
      <figcaption>图 1：系统架构图</figcaption>
    </figure>
    <time datetime="2026-08-03">2026 年 8 月 3 日</time>
  </article>
</main>

<aside>     <!-- 侧边栏：与主内容相关的补充 -->
  <p>相关阅读</p>
</aside>

<footer>    <!-- 页脚 -->
  <p>© 2026</p>
</footer>
```

**为什么要语义化？**

- 搜索引擎更懂你的页面，SEO 更好。
- 读屏软件能正确朗读结构，盲人也能用你的页面。
- 代码可读性强，团队协作时一眼看懂每个区块是干嘛的。Django 模板里同样适用，`{% block %}` 之间的内容也用这些标签。

> 📱 选标签的思考顺序：`<header>/<nav>/<main>/<section>/<article>/<aside>/<footer>` 都不合适时，才轮到 `<div>`（无含义的通用容器）。

### 2.8 块级元素与行内元素 📱

这是 CSS 的入门概念，HTML 先认识一下：

| 类型 | 行为 | 常见代表 |
|------|------|----------|
| **块级元素** | 独占一行，从上到下排列，默认宽度撑满父容器 | `div p h1~h6 ul ol li table section header footer` |
| **行内元素** | 一行内从左到右排列，放不下才换行，宽度由内容决定 | `a span strong em img input label code` |

```html
<!-- 块级：每个占一行 -->
<p>第一段</p>
<p>第二段</p>

<!-- 行内：并排在一行里 -->
<p>这段文字里有 <a href="#">链接</a> 和 <strong>加粗</strong>，它们都排在行内。</p>
```

| 用途 | 用什么 |
|------|--------|
| 布局分区、装大块内容 | `<div>`（块级） |
| 行内文字上挂样式或钩子 | `<span>`（行内） |

> 📱 一个常见错误：在 `<span>`（行内）上设置 `width`、`margin-top` 无效。想让它生效，先通过 CSS 把它变成块级或行内块（第 3 章 3.7 节）。

### 2.9 表单与提交 💻

表单是「用户输入数据，发给后端」的通道。你写 Django 时天天和它打交道，这里是它的 HTML 真身。

```html
<form action="/search" method="get">
  <label for="q">搜索：</label>
  <input type="search" id="q" name="q" placeholder="输入关键词">
  <button type="submit">搜索</button>
</form>
```

**form 的两个关键属性：**

| 属性 | 作用 |
|------|------|
| `action` | 提交到哪个地址（后端 URL）。不写则提交到当前页 |
| `method` | `get` 或 `post`，对应 HTTP 方法 |

**input 的 name 属性最重要：** 没有 `name` 的输入框，数据不会被发送。`name` 是数据在请求里的「键」。

- `method="get"` 提交后，浏览器地址变成 `/search?q=关键词`，数据拼在 URL 里。适合搜索、筛选这类不敏感的数据。
- `method="post"` 提交后，数据放在请求体里，URL 不变。适合提交表单、修改数据。Django 的 POST 表单必须加 `{% csrf_token %}`（第 9 章详述）。

Django 端对应的取数代码：

```python
# views.py
def search(request):
    keyword = request.GET.get("q")     # 对应 method="get" 的 name="q"
    return render(request, "index.html", {"keyword": keyword})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")   # 对应 name="username"
```

**常用输入控件一览：**

```html
<form action="/register" method="post">
  <label for="username">用户名</label>
  <input type="text" id="username" name="username" placeholder="请输入用户名" required>

  <label for="pwd">密码</label>
  <input type="password" id="pwd" name="pwd" required>

  <label for="email">邮箱</label>
  <input type="email" id="email" name="email" required>

  <label for="age">年龄</label>
  <input type="number" id="age" name="age" min="0" max="150">

  <label for="birth">生日</label>
  <input type="date" id="birth" name="birth">

  <p>学习方向：</p>
  <input type="checkbox" id="fe" name="direction" value="前端">
  <label for="fe">前端</label>
  <input type="checkbox" id="be" name="direction" value="后端">
  <label for="be">后端</label>

  <p>经验：</p>
  <input type="radio" id="exp1" name="level" value="新手">
  <label for="exp1">新手</label>
  <input type="radio" id="exp2" name="level" value="熟练">
  <label for="exp2">熟练</label>

  <label for="intro">自我介绍</label>
  <textarea id="intro" name="intro" rows="4" placeholder="写点什么…"></textarea>

  <label for="city">城市</label>
  <select id="city" name="city">
    <option value="beijing">北京</option>
    <option value="shanghai" selected>上海</option>
    <option value="shenzhen">深圳</option>
  </select>

  <button type="submit">注册</button>
</form>
```

| 控件 | 标签 | 说明 |
|------|------|------|
| 单行文本 | `<input type="text">` | 最常用 |
| 密码 | `<input type="password">` | 输入显示为圆点 |
| 邮箱 | `<input type="email">` | 浏览器自动校验格式 |
| 数字 | `<input type="number">` | 带增减按钮，`min`/`max` 限范围 |
| 日期 | `<input type="date">` | 弹日期选择器 |
| 复选框 | `<input type="checkbox">` | 可多选，`name` 相同 |
| 单选 | `<input type="radio">` | 只能选一个，**`name` 必须相同才互斥** |
| 多行文本 | `<textarea>` | 用 `rows` 控制高度 |
| 下拉框 | `<select>` + `<option>` | `selected` 指定默认项 |
| 搜索框 | `<input type="search">` | 带清除按钮 |
| 滑块 | `<input type="range">` | 调节音量等 |
| 文件 | `<input type="file">` | 上传用，表单要加 `enctype="multipart/form-data"` |
| 提交按钮 | `<button type="submit">` | 点击触发提交 |

**三个必须遵守的规范：**

1. 每个输入控件配一个 `<label>`，用 `for="控件id"` 关联。点 label 文字就能聚焦输入框，读屏软件也能读出含义。
2. `type="button"` 的按钮不会提交表单；`type="submit"` 才会。忘记写 `type` 时，`<button>` 默认是 submit。
3. 必填项加 `required`，浏览器会自动拦截空提交，不用写 JS。

### 2.10 已废弃的旧标签 📱

网上老教程里常见这些标签，**它们已经废弃或过时，不要在新代码里用**：

| 旧标签 | 问题 | 现代替代 |
|--------|------|----------|
| `<center>` | 废弃，居中请用 CSS | `text-align: center` 或 Flex |
| `<font color="red">` | 废弃，样式必须交给 CSS | `color: red` |
| `<b>` / `<i>` | 只有视觉效果，无语义 | `<strong>` / `<em>` |
| `<marquee>` | 跑马灯滚动，纯属恶搞 | CSS 动画或干脆不用 |
| `<big>` | 废弃 | CSS `font-size` |
| `<strike>` / `<u>` | 废弃 / 有歧义 | CSS `text-decoration` |
| `<frame>` / `<frameset>` | 已移除，破坏 SEO 和导航 | 普通页面 + `<iframe>`（少用） |
| `<table>` 做页面布局 | 过时做法 | Flex / Grid |

> 📱 判断一个标签能不能用：去 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTML) 查。文档里标注「Deprecated / Obsolete」的都不要用。

### 2.11 HTML 实体与注释 💻

**实体（entity）**：有些字符在 HTML 里有特殊含义，直接写会被浏览器误解，要用转义写法：

| 实体 | 显示 | 含义 | 用法示例 |
|------|------|------|----------|
| `&lt;` | `<` | 小于号 | `&lt;p&gt;` 显示为 `<p>` |
| `&gt;` | `>` | 大于号 | `2 &gt; 1` 显示为 `2 > 1` |
| `&amp;` | `&` | 和号 | `AT&amp;T` 显示为 `AT&T` |
| `&copy;` | © | 版权符号 | `&copy; 2026` 显示为 `© 2026` |
| `&nbsp;` | 空格 | 不换行空格 | 连续多个空格在 HTML 中默认只显示一个，用实体强制 |

**注释：**

```html
<!-- 这是 HTML 注释，浏览器不显示，但会出现在源码里 -->
<!-- 别在注释里写密码、密钥等敏感信息 -->
```

> 📱 回忆一下 Django 模板的注释是 `{# 注释 #}`，会直接被服务器吃掉，不会出现在源码里。HTML 注释则会被原样发给浏览器。

---

## 三、CSS：网页的样式

### 3.1 CSS 的三种写法 💻

CSS（Cascading Style Sheets，层叠样式表）负责「长什么样」。基本语法：

```css
选择器 {
  属性: 值;
  属性: 值;
}

p {
  color: red;        /* 文字红色 */
  font-size: 18px;   /* 字号 18 像素 */
}
```

三种写进页面的方式：

```html
<!-- 方式一：内联样式（写在标签的 style 属性里）。能用但别常用，无法复用 -->
<p style="color: red;">红色文字</p>

<!-- 方式二：页面内 <style>（写在 head 里）。单文件演示项目可以这么干 -->
<style>
  p { color: red; }
</style>

<!-- 方式三：外部样式表（推荐）。用 link 引入 .css 文件，多页面共享 -->
<link rel="stylesheet" href="style.css">
```

| 方式 | 复用性 | 适用场景 |
|------|--------|----------|
| 内联 `style="..."` | 无 | 极少数一次性微调 |
| `<style>` | 单页内 | 演示、小工具页 |
| 外部 `.css` 文件 | 全站 | **项目首选** |

> 📱 Django 里第三种方式对应 `{% static %}` 引入静态文件，见第 9 章。

### 3.2 选择器 💻

选择器决定「CSS 规则作用在哪些元素上」。这是 CSS 的核心语法。

```css
/* 标签选择器：命中所有 <p> */
p { font-size: 16px; }

/* 类选择器：命中所有 class="warning" 的元素。点号开头 */
.warning { color: #e74c3c; }

/* ID 选择器：命中 id="nav" 的唯一个元素。# 开头 */
#nav { background: #2c3e50; }

/* 通配符：命中所有元素。慎用，性能差 */
* { box-sizing: border-box; }

/* 后代选择器：命中 <nav> 里的所有 <a>（含孙子层级） */
nav a { color: white; }

/* 子代选择器：只命中直接子元素，不包含孙子 */
nav > a { color: white; }

/* 相邻兄弟：命中紧跟在 <h2> 后面的第一个 <p> */
h2 + p { font-style: italic; }

/* 属性选择器：命中 type 为 text 的 input */
input[type="text"] { border: 1px solid #ccc; }
a[href^="https"] { color: green; }   /* href 以 https 开头 */
a[href$=".pdf"] { color: red; }      /* href 以 .pdf 结尾 */

/* 伪类：元素处于某种状态时生效。冒号一个 */
a:hover { color: orange; }            /* 鼠标悬停 */
li:first-child { font-weight: bold; } /* 第一个子元素 */
li:nth-child(even) { background: #f5f5f5; } /* 第偶数个 */
input:focus { outline: 2px solid #3498db; } /* 聚焦时 */

/* 伪元素：元素的某个部分。两个冒号 */
p::first-line { font-weight: bold; }
.note::before { content: "📌 "; }     /* 在元素内容前面插入 */
.note::after  { content: ""; }

/* 分组：同时选中多个 */
h1, h2, h3 { color: #2c3e50; }
```

| 选择器 | 符号 | 权重感觉 | 优先级计数（下一节细讲） |
|--------|------|----------|--------------------------|
| ID | `#nav` | 最强 | 1-0-0 |
| 类 / 属性 / 伪类 | `.box` `[type]` `:hover` | 中 | 0-1-0 |
| 标签 / 伪元素 | `p` `::before` | 弱 | 0-0-1 |
| 通配符 | `*` | 最弱 | 0-0-0 |

> 💻 **练习建议**：每学一种选择器，在浏览器开发者工具里 F12 用 Console 敲 `document.querySelectorAll('nav a')` 看命中结果，或者直接在 Elements 面板给元素临时加类名。看到命中的是哪些元素，比背规则有效十倍。

### 3.3 优先级（层叠规则）📱

同一元素可能被多条规则同时命中，到底听谁的？按这个顺序：

```
内联样式 style="..."      >    id 选择器    >    类/属性/伪类    >    标签/伪元素    >    通配符/继承
（最高优先级）                （1-0-0）        （0-1-0）          （0-0-1）           （最低）
```

优先级用「三位计数」比较，左边数字大的赢：

| 规则 | ID 数 | 类数 | 标签数 | 谁赢 |
|------|:-----:|:----:|:------:|------|
| `p` | 0 | 0 | 1 | |
| `.warning` | 0 | 1 | 0 | 赢 |
| `#nav .item p` | 1 | 1 | 1 | 赢 |
| `ul li a` | 0 | 0 | 3 | 比 `p` 强 |
| `.a .b .c .d` | 0 | 4 | 0 | 赢 |

三条实操结论，比死记规则有用：

1. **同优先级时，写在后面的规则赢**。所以通用样式放前面，覆盖样式放后面。
2. **能用 class 就别用 id 做样式**。id 优先级太高，后面想覆盖只能靠更长的选择器，代码越写越脏。id 留给 JS 和锚点。
3. **`!important` 是核武器**，滥用会让项目无法维护：

```css
/* 能用优先级解决，就不要用 !important */
.error { color: red !important; }   /* 会覆盖任何选择器的 color，除非另一个 !important 更晚 */
```

> 📱 在开发者工具 Elements 面板的 Styles 里，被覆盖的规则会显示为「灰色加删除线」，鼠标放上去能看到是哪条规则赢了。这是排查样式问题的第一利器。

### 3.4 颜色、字体与文本 💻

```css
body {
  /* 颜色：四种写法 */
  color: red;                     /* 颜色名 */
  color: #e74c3c;                 /* 十六进制（最常用），#rrggbb */
  color: rgb(231, 76, 60);        /* rgb 函数 */
  color: rgba(231, 76, 60, 0.5);  /* 带透明度，0 完全透明，1 不透明 */

  /* 中文字体族：依次回退，第一个没有就用下一个 */
  font-family: -apple-system, "PingFang SC", "Microsoft YaHei",
               "Noto Sans CJK SC", sans-serif;

  font-size: 16px;        /* 字号 */
  font-weight: bold;      /* 粗细：normal / bold / 100~900 */
  line-height: 1.6;       /* 行高：无单位 = 字号的 1.6 倍，中文正文推荐 1.6~1.8 */

  text-align: center;     /* 对齐：left / center / right / justify */
  text-decoration: none;  /* 常用值：underline 下划线 / line-through 删除线 / none 去掉 */
  letter-spacing: 1px;    /* 字间距 */
}
```

取色工具：浏览器开发者工具自带的取色器、`colorpick eyedropper` 插件、或者搜索引擎搜「颜色选择器」。写网站配色从现成的调色板开始最省力，比如 [Coolors](https://coolors.co/) 或 [Open Color](https://yeun.github.io/open-color/)。

### 3.5 盒模型 📱

**每个元素都是一个盒子。** 布局之前必须把这张图画进脑子里：

```
┌────────────────────────────────┐
│          margin（外边距）         │  ← 盒子和外面元素的距离
│  ┌──────────────────────────┐  │
│  │      border（边框）        │  │  ← 边框
│  │  ┌────────────────────┐  │  │
│  │  │   padding（内边距）   │  │  │  ← 内容与边框的距离
│  │  │  ┌──────────────┐  │  │  │
│  │  │  │  content     │  │  │  │  ← 内容（文字、图片）
│  │  │  │  （内容区）    │  │  │  │
│  │  │  └──────────────┘  │  │  │
│  │  └────────────────────┘  │  │
│  └──────────────────────────┘  │
└────────────────────────────────┘
```

```css
.box {
  width: 200px;
  height: 100px;
  padding: 20px;         /* 内边距：内容区四周 20px */
  border: 2px solid #333;/* 边框：2px 宽、实线、深灰色 */
  margin: 10px;          /* 外边距：盒子四周 10px */
}

/* 简写规则（上 右 下 左，顺时针） */
padding: 10px 20px 10px 20px;   /* 上 右 下 左 */
padding: 10px 20px;             /* 上下 10px，左右 20px */
padding: 10px;                  /* 四周都是 10px */
/* margin、border 同理 */
```

**最关键的坑：`box-sizing`。**

- 默认值 `content-box`：`width: 200px` 指**内容区**宽度。加上 padding 和 border，盒子实际占 200 + 20*2 + 2*2 = 244px。算布局时经常对不上。
- `border-box`：`width: 200px` 指**包含 padding 和 border 的总宽度**，内容区自动压缩。符合直觉，业界标配。

所以第一行 CSS 请固定写这段「reset」：

```css
*, *::before, *::after {
  box-sizing: border-box;
}
body {
  margin: 0;              /* 浏览器默认给 body 8px 外边距，先清掉 */
}
```

> 📱 再记两个盒子相关的概念：
> - **外边距合并**：上下两个块元素的 margin 会取较大值，而不是相加。经典例子：两个 `margin: 20px` 的元素之间只有 20px 而不是 40px。
> - `outline` 不占布局空间，适合做「聚焦高亮」而不挤动布局。`border` 占空间，加在 hover 上会把盒子挤大，这时用 `outline` 或者提前预留透明 border。

### 3.6 定位 💻

`position` 决定元素在页面里的「坐标方式」：

```css
.static  { position: static; }    /* 默认值：文档流正常排列，top/left 无效 */
.relative { position: relative; } /* 相对自己原来的位置偏移，不脱离文档流 */
.absolute { position: absolute; } /* 脱离文档流，相对最近的「定位祖先」定位 */
.fixed    { position: fixed; }    /* 脱离文档流，相对浏览器视口固定，滚动不动 */
.sticky   { position: sticky; }   /* 滚动到某个位置后「粘」住，常用于导航栏 */
```

```css
/* 相对定位：自己从原位置向右下挪，原来的坑还占着 */
.relative {
  position: relative;
  top: 10px;      /* 向下移 10px */
  left: 20px;     /* 向右移 20px */
}

/* 绝对定位：相对于最近的定位祖先（relative/absolute/fixed）*/
/* 如果祖先都没有定位，就相对于视口 */
.parent { position: relative; }
.child {
  position: absolute;
  top: 0;
  right: 0;       /* 贴在父盒子右上角 */
}

/* 固定定位：贴屏幕。弹窗遮罩、回到顶部按钮 */
.back-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
}

/* 粘性定位：滚动导航栏，< 视口顶部时就吸住 */
.nav {
  position: sticky;
  top: 0;
}
```

偏移属性：`top` `right` `bottom` `left`，也可以用 `inset: 0` 表示四个方向都是 0。多元素重叠时用 `z-index` 控制谁在上层，数字大的在上：

```css
.modal { position: fixed; inset: 0; z-index: 100; }
```

> 📱 记忆口诀：`absolute` 是「找最近的定位祖先当参照系」；没有就退化为相对视口。这是新手最容易犯的错，加了 absolute 但父元素没写 `position: relative`，元素就飘到页面角落去了。

### 3.7 居中方案大全 💻

「怎么居中」是前端最高频的问题。别再瞎试了，按这张表查：

| 想居中的东西 | 方案 |
|--------------|------|
| 文字水平居中（块内） | 父元素 `text-align: center` |
| 文字垂直居中（单行） | `line-height` 等于盒子高度 |
| 块级元素水平居中（有宽度的） | `margin: 0 auto` + 设定 `width`，或 Flex |
| 图片 / 行内元素水平居中 | 父元素 `text-align: center` |
| 图片垂直居中 | Flex（见下） |
| 任意元素水平垂直居中 | Flex 或 Grid（**首选**） |
| 绝对定位元素居中 | `inset: 0; margin: auto;` + 设定宽高，或 `transform` |

```css
/* 方案一：Flex（现代首选，最推荐） */
.parent {
  display: flex;
  justify-content: center;   /* 主轴居中 */
  align-items: center;       /* 交叉轴居中 */
}

/* 方案二：Grid（更短） */
.parent {
  display: grid;
  place-items: center;
}

/* 方案三：绝对定位 + transform（元素不知道宽高也能居中） */
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

/* 文字垂直居中：line-height 技巧（只适合单行） */
.btn {
  height: 40px;
  line-height: 40px;   /* 行高等于高度，文字自动垂直居中 */
}
```

> 📱 补充：老代码里还有「绝对定位 + `inset: 0; margin: auto` + 固定宽高」的居中法，属于遗留写法，能看懂就行，新代码不用它。

### 3.8 Flex 布局详解 📱

Flex（弹性盒）是**一维布局**，要么横排要么竖排。它是现代网页布局的绝对主力，必须吃透。

**容器（父元素）的属性：**

```css
.container {
  display: flex;          /* 开启 Flex，子元素默认横排 */

  flex-direction: row;         /* 横排（默认） */
  flex-direction: column;      /* 竖排 */
  /* row-reverse / column-reverse 反向 */

  flex-wrap: wrap;        /* 放不下时换行（默认 nowrap 不换行） */
  /* 常用组合简写：flex-flow: row wrap; */

  justify-content: flex-start;   /* 主轴对齐方式（默认） */
  justify-content: center;       /* 居中 */
  justify-content: space-between;/* 两端对齐，中间均分 */
  justify-content: space-around; /* 每个元素两侧间距均等 */
  justify-content: space-evenly; /* 元素间间距完全相等 */

  align-items: stretch;    /* 交叉轴：拉伸填满（默认） */
  align-items: center;     /* 交叉轴：居中（垂直居中神器） */
  align-items: flex-start; /* 顶部对齐 */
  align-items: flex-end;   /* 底部对齐 */

  gap: 16px;               /* 子元素间距，比 margin 好使一万倍 */
}
```

`justify-content` 三种值的示意图：

```
justify-content: center
  [  A  ][  B  ][  C  ]    ← 整组居中，组内无间距

justify-content: space-between
  [A]        [B]        [C]   ← 两端贴边，中间均分

justify-content: space-evenly
    [A]   [B]   [C]      ← 每个缝隙间距相等
```

**子元素的属性：**

```css
.item {
  flex-grow: 1;       /* 剩余空间按 grow 比例分配，实现「弹性伸缩」 */
  flex-shrink: 1;     /* 空间不够时怎么缩（默认 1） */
  flex-basis: 200px;  /* 初始宽度 */
  /* 常用简写：flex: 1;  ===  flex: 1 1 0%; */
  /* flex: 0 0 200px; 固定 200px 不伸缩 */

  align-self: center; /* 单独覆盖自己的交叉轴对齐 */

  order: 1;           /* 排列顺序，越小越靠前（默认 0） */
}
```

**三个实战组合，抄走就用：**

```css
/* 1. 导航栏：logo 靠左，菜单靠右 */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* 2. 卡片列表：自动换行，三列效果（配合 gap） */
.card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card-list .card {
  flex: 1 1 200px;   /* 每张卡至少 200px，多了自动加宽 */
}

/* 3. 经典三栏：左右固定，中间自适应 */
.layout {
  display: flex;
}
.sidebar { flex: 0 0 200px; }
.main    { flex: 1; }
```

> 📱 Flex 的两条主轴搞清楚了，其余全是细节：`justify-content` 管「主轴方向怎么排」，`align-items` 管「交叉轴怎么对齐」。`flex-direction: column` 时主轴变成垂直，两条轴的理解跟着转 90 度。

### 3.9 Grid 布局入门 💻

Grid 是**二维布局**（同时控制行和列），适合页面整体框架和规则网格。

```css
.grid {
  display: grid;
  grid-template-columns: 200px 1fr 1fr;   /* 三列：固定 200px，其余两列均分剩余 */
  grid-template-columns: repeat(3, 1fr);  /* 等价写法：三列均分 */
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); /* 响应式神器：自动填充 */
  gap: 16px;                              /* 行列间距 */
  grid-template-rows: 100px 1fr;          /* 两行：固定 100px + 剩余 */
}

/* 子元素跨行跨列 */
.item-1 { grid-column: 1 / 3; }   /* 占第 1 列到第 3 列（即两列） */
.item-2 { grid-row: 1 / 3; }      /* 占两行 */
.item-3 { grid-column: span 2; }  /* 跨两列，更直观的写法 */

/* 元素定位到指定格子 */
.item { grid-column: 2; grid-row: 1; }
```

**Flex 还是 Grid？一张表选清楚：**

| 场景 | 选谁 |
|------|------|
| 导航栏、按钮组、卡片一行内排列 | Flex |
| 垂直居中、水平居中 | Flex 或 Grid |
| 整体页面框架（页头 + 侧栏 + 主区 + 页脚） | Grid |
| 规则的行列网格（相册、商品列表、数据面板） | Grid |
| 混合：整体 Grid、局部内部 Flex | 两者结合，各干各的 |

> 📱 通用原则：**一维用 Flex，二维用 Grid。** 新手先把 Flex 练到不用查文档，Grid 会 `repeat`、`minmax`、`auto-fill` 三个函数和 `grid-column` 跨度就够了。

### 3.10 单位 📱

| 单位 | 含义 | 典型用途 |
|------|------|----------|
| `px` | 像素，绝对单位 | 边框、小间距、固定宽度 |
| `%` | 相对父元素 | 宽度、高度 |
| `em` | 相对**父元素**字号 | 少用，嵌套会叠乘，容易失控 |
| `rem` | 相对**根元素**字号（默认 16px） | **字号首选**。改一个根字号，全局等比缩放 |
| `vw` / `vh` | 视口宽/高的 1% | 全屏区块、Hero 区 |
| `fr` | Grid 剩余空间份数 | 仅 Grid 内使用 |

```css
html { font-size: 16px; }        /* 根字号默认就是 16px */

.title { font-size: 2rem; }      /* = 32px，跟随根字号缩放 */
.note  { font-size: 0.875rem; }  /* = 14px */

.hero {
  width: 100vw;                  /* 撑满整个视口宽度 */
  height: 60vh;                  /* 占视口高度的 60% */
}

.box { width: calc(100% - 40px); }   /* calc 计算，注意运算符两侧要有空格 */
```

> 📱 移动端最佳实践：字号用 `rem`，间距用 `px` 或 `rem` 都行，弹性容器内部用 `%`、`flex`、`fr` 自适应。`em` 只在个别场景用（比如按钮的 padding 想跟随按钮字号走）。

### 3.11 响应式与媒体查询 💻

一个页面在手机、平板、电脑上都要好看，叫响应式。前提是 HTML 头部必须有 viewport 声明（2.1 节讲过）：

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**媒体查询 `@media`** 按屏幕宽度切换样式：

```css
/* 基础样式先按手机写（移动优先），再一步步放大适配 */
.card-list {
  display: grid;
  grid-template-columns: 1fr;      /* 手机：单列 */
  gap: 16px;
}

/* 平板及以上：两列 */
@media (min-width: 768px) {
  .card-list { grid-template-columns: repeat(2, 1fr); }
}

/* 桌面：四列 */
@media (min-width: 1200px) {
  .card-list { grid-template-columns: repeat(4, 1fr); }
}
```

**常用断点（breakpoint）：**

| 设备 | 宽度 |
|------|------|
| 手机 | < 768px |
| 平板 | 768px ~ 1024px |
| 桌面 | > 1024px |

**其他响应式技巧：**

```css
img {
  max-width: 100%;       /* 图片永不超出容器，自动缩放 */
  height: auto;          /* 保持宽高比 */
}

.container {
  max-width: 960px;      /* 内容最多 960px，窄屏自动缩 */
  margin: 0 auto;
}

@media (max-width: 768px) {
  .nav { flex-direction: column; }   /* 窄屏时导航竖排 */
  .hide-on-mobile { display: none; } /* 某些元素手机端隐藏 */
}
```

> 📱 响应式不是「移动端单独做一套」，而是「用一套 HTML，通过媒体查询在不同宽度下换样式」。开发时用浏览器开发者工具的「设备模拟」按钮（第 5 章）直接看手机效果。

### 3.12 CSS 变量 📱

CSS 变量（自定义属性）让配色和间距可复用、可集中管理：

```css
:root {
  --primary: #3498db;      /* 主题色 */
  --danger: #e74c3c;       /* 危险色 */
  --gap: 16px;
  --radius: 8px;
}

.btn {
  background: var(--primary);
  border-radius: var(--radius);
}

.btn-danger { background: var(--danger); }
.card { gap: var(--gap); }
```

改一处 `--primary`，全站按钮和链接同步变色。这在做「换肤」和主题化时是基础能力，后面的实战 1 会用到。

---

## 四、JavaScript：网页的行为

你已经会 Python，JavaScript 学起来会非常快。**不要把它当新语言从头学，而是当「披着 C 语法外衣、和 Python 同族」的语言对照着学**。下面每一节都带 Python 对照表。

### 4.1 JS 放在哪里 💻

```html
<!-- 方式一：页面内 script，放 body 底部保证 HTML 先渲染完 -->
<script>console.log('这是页面内 JS');</script>

<!-- 方式二：外部 JS 文件（推荐）。defer 表示等 HTML 解析完再执行 -->
<script src="app.js" defer></script>
```

`console.log` 就是 JS 的 `print`，结果输出到浏览器开发者工具的 Console 面板（第 5 章），不是页面上。

> 📱 为什么 script 要放底部或加 `defer`？因为 JS 执行时，如果它要操作的 DOM 还没解析出来，就会报「找不到元素」。`defer` 让脚本等页面解析完再跑，是现在的标准姿势。

### 4.2 变量与数据类型 💻

```js
let count = 1;            // let：可重新赋值，首选
const PI = 3.14159;       // const：常量，声明后不能重新赋值，首选
var old = 1;              // var：旧语法，有各种坑，别用
```

| 关键字 | 可改值 | 作用域 | 结论 |
|--------|--------|--------|------|
| `const` | 否 | 块级 | **能 const 就 const** |
| `let` | 是 | 块级 | 需要改值时用 |
| `var` | 是 | 函数级 | 过时，不要写 |

**数据类型：**

```js
const num = 42;              // number：整数和小数都是它
const str = '你好';          // string：单引号双引号都行
const flag = true;           // boolean：true / false
const nothing = null;        // null：显式的「空」
let x;                       // undefined：声明了但没赋值

console.log(typeof num);     // 'number'，typeof 是判断类型的运算符
```

**Python 对照表：**

| Python | JavaScript | 差异提醒 |
|--------|-----------|----------|
| `None` | `null` 和 `undefined` | JS 有两个空值：`null`（手动设置的空）和 `undefined`（没赋值） |
| `list` | `Array` | 方法名不同，见 4.5 |
| `dict` | `Object` | 键名写法不同，见 4.6 |
| `def f():` | `function` / 箭头函数 | 见 4.7 |
| `print(...)` | `console.log(...)` | 输出在浏览器 Console |
| `f"hi {name}"` | `` `hi ${name}` `` | 模板字符串用反引号 |
| `len(x)` | `x.length` | 属性不是函数 |
| `x == None` | `x === null` | 判断用三等号，见 4.3 |
| `if x:` | `if (x) { }` | 语法括号加花括号 |

### 4.3 运算符 💻

```js
// 算术：+ - * / % 和 Python 一样，但除法永远是浮点数
console.log(5 / 2);    // 2.5，JS 没有 // 整除
console.log(5 % 2);    // 1
console.log(2 ** 10);  // 1024，幂运算（Python 是 2 ** 10）

// 比较：永远用三个等号！
console.log(1 === 1);    // true，严格相等（值和类型都相同）
console.log(1 == '1');   // true，宽松相等（会偷偷转类型，有坑，别用）
console.log(1 === '1');  // false，严格比较
console.log(1 !== '1');  // true，不相等
console.log(10 > 5);     // true
console.log('a' < 'b');  // true，字符串按字典序比

// 逻辑：&&（and）||（or）!（not）
const a = true && false;   // false
const b = true || false;   // true
const c = !true;           // false

// 三元表达式：if/else 的简写
const age = 18;
const type = age >= 18 ? '成年人' : '未成年人';

// 空值合并 ??：左边是 null/undefined 时用右边
const username = null;      // 先给个变量，方便下面演示
const name = username ?? '匿名';

// 注意：+ 号遇字符串就拼接
console.log('1' + 2);    // '12'，不是 3！数字先被转成了字符串
```

> 📱 **一句话记住 JS 的坑**：永远用 `===` 和 `!==`，别用 `==` 和 `!=`。`+` 号有一边是字符串就整体变字符串拼接。

**真值（truthy）与假值（falsy）：**

```js
// 在 if 判断里为「假」的值只有这几个：
// false、0、''（空字符串）、null、undefined、NaN
// 其余一切（包括空数组 [] 和空对象 {}）都是「真」

if (0) { console.log('不会执行'); }
if ([]) { console.log('会执行，空数组也是真'); }
const name2 = '小明';
if (name2) { console.log('name2 有值才执行'); }   // 常用写法
```

### 4.4 字符串与模板字符串 💻

```js
const name = '小明';
const greet = '你好，' + name;            // 拼接（老方法）
const greet2 = `你好，${name}！`;          // 模板字符串（推荐），用反引号

const price = 9.9;
console.log(`价格：¥${price.toFixed(2)}`); // 支持任意表达式

// 常用方法（和 Python 对应）
const s = 'hello world';
s.length;               // 11（len(s)）
s.toUpperCase();        // 'HELLO WORLD'（s.upper()）
s.includes('world');    // true（'world' in s）
s.startsWith('he');     // true（s.startswith('he')）
s.indexOf('world');     // 6（s.index('world')，找不到返回 -1）
s.slice(0, 5);          // 'hello'（s[:5]）
s.split(' ');           // ['hello', 'world']（s.split(' ')）
s.replace('hello', 'hi'); // 'hi world'（s.replace('hello', 'hi')，只换第一个）
s.trim();               // 去掉首尾空白（s.strip()）
```

### 4.5 数组 💻

```js
// 创建
const fruits = ['苹果', '香蕉', '橙子'];
const nums = [1, 2, 3, 4, 5];

// 读写
fruits[0];             // '苹果'
fruits[0] = '梨';
fruits.length;         // 3（len(fruits)）

// 增删
fruits.push('西瓜');      // 末尾加（list.append）
fruits.pop();             // 末尾取走（list.pop()）
fruits.shift();           // 头部取走（list.pop(0)）
fruits.unshift('草莓');    // 头部加
fruits.indexOf('香蕉');   // 找下标（list.index），找不到返回 -1
fruits.includes('苹果');  // true（'苹果' in list）

// 循环
for (const fruit of fruits) {   // for...of 等价于 Python 的 for x in list
  console.log(fruit);
}
fruits.forEach((fruit, i) => {  // forEach 带下标
  console.log(i, fruit);
});

// 复制（重要：直接赋值是引用，不是复制！）
const copy = [...fruits];        // 展开运算符，生成新数组
const copy2 = fruits.slice();    // 或 slice()

// 转字符串
fruits.join('、');               // '苹果、香蕉、橙子'（'、'.join(fruits)）
```

**数组三剑客：map / filter / reduce**，阶段 5 学 React 时天天用，现在必须会：

```js
const nums = [1, 2, 3, 4, 5];

// map：每个元素变换，返回等长新数组（Python: [x*2 for x in nums]）
const doubled = nums.map(x => x * 2);
// [2, 4, 6, 8, 10]

// filter：筛选，返回满足条件的新数组（Python: [x for x in nums if ...]）
const evens = nums.filter(x => x % 2 === 0);
// [2, 4]

// reduce：把整个数组归约为一个值（Python: functools.reduce）
const total = nums.reduce((acc, x) => acc + x, 0);
// 15，acc 是累加器，初始为 0

// 实战组合拳：从图书数组里筛出年份 >= 2020 的书名
const books = [
  { title: 'Python 编程', year: 2023 },
  { title: '算法导论', year: 2009 },
];
const titles = books.filter(b => b.year >= 2020).map(b => b.title);
// ['Python 编程']
```

> 📱 `map` 和 `filter` 不改变原数组，返回新数组。这是函数式风格的基础，比 `for` 循环手动改数组更不容易出错。

### 4.6 对象 💻

```js
// 对象字面量：等价于 Python 的 dict
const book = {
  title: '流畅的 Python',
  author: 'Luciano Ramalho',
  year: 2022,
};

// 读取：点语法 / 方括号语法
book.title;            // '流畅的 Python'
book['title'];         // 同上，变量键名时用方括号
const key = 'author';
book[key];             // 'Luciano Ramalho'

// 修改与新增
book.year = 2023;
book.pages = 880;      // 键不存在就自动加上

// 删除
delete book.pages;

// 遍历键
for (const k of Object.keys(book)) {
  console.log(k, book[k]);
}
Object.keys(book);     // ['title', 'author', 'year']
Object.values(book);   // ['流畅的 Python', ...]

// 复制：展开运算符（浅拷贝）
const copy = { ...book, year: 2025 };   // 复制并顺手改一个字段

// 解构：从对象里取出字段（前端超高频写法）
const { title, author } = book;
console.log(title);    // 直接用，不用 book.title

// 从数组解构
const [first, second] = [1, 2, 3];
// first = 1, second = 2
```

**对象数组**是前后端数据交换的标准形状，后端返回的 JSON 列表解析后就是这个结构。实战 3 里你渲染的图书列表就是 `[{id, title, author, year}, ...]`。

```js
// 对象数组的操作套路
const books = [
  { id: 1, title: 'A', author: '张三' },
  { id: 2, title: 'B', author: '李四' },
];

// 按条件找一个（等价于 first-or-none）
const found = books.find(b => b.id === 2);      // 找不到返回 undefined

// 按条件找全部
const list = books.filter(b => b.author === '张三');

// 取所有 id
const ids = books.map(b => b.id);               // [1, 2]

// 找下标
const idx = books.findIndex(b => b.title === 'A'); // 0

// 排序（返回新数组）
const sorted = [...books].sort((a, b) => a.id - b.id);
```

> 📱 `const` 只能保证「这个变量指向这个对象」，不能阻止「这个对象里的字段被修改」。所以 `const book` 后依然可以 `book.year = 2025`。Python 里 `tuple` 和 `list` 的关系可以帮你理解：const 是引用固定，不是内容冻结。

### 4.7 函数 💻

```js
// 声明式（function 关键字）
function add(a, b) {
  return a + b;
}
add(1, 2);           // 3

// 函数表达式：函数也是一个值，能赋值给变量
const add2 = function (a, b) {
  return a + b;
};

// 箭头函数（现代首选，更短）
const add3 = (a, b) => a + b;         // 单行直接返回
const greet = (name) => {
  console.log(`你好，${name}`);
  return `你好，${name}`;
};
const square = x => x * x;            // 一个参数时可以省略括号

// 默认参数
function hello(name = '陌生人') {
  return `你好，${name}`;
}
```

**Python 对照：**

| Python | JavaScript |
|--------|-----------|
| `def add(a, b): return a + b` | `const add = (a, b) => a + b;` |
| 函数是对象，能传参 | 一样！函数是一等公民 |
| `lambda x: x*2` | `x => x * 2` |
| 闭包 | 闭包，一样的存在 |
| 装饰器 | 没有直接等价物（用高阶函数模拟） |

**函数作为值传递**是 JS 最核心的思维，事件处理、数组方法全靠它：

```js
// 把函数当作参数传给另一个函数
function process(value, transform) {
  return transform(value);
}
process(5, x => x * 10);   // 50

// 回调函数：稍后被调用的函数
function loadData(onSuccess, onError) {
  // ... 模拟异步请求
  const ok = true;
  if (ok) onSuccess('数据');
  else onError('出错了');
}
loadData(
  (data) => console.log('成功', data),
  (err) => console.log('失败', err),
);
```

### 4.8 条件与循环 💻

```js
// if / else if / else
const score = 85;
let grade;
if (score >= 90) {
  grade = 'A';
} else if (score >= 80) {
  grade = 'B';
} else {
  grade = 'C';
}

// switch：多个固定值判断用（记住每个 case 末尾要 break，否则会穿透）
const action = 'add';
switch (action) {
  case 'add': console.log('执行新增'); break;
  case 'delete': console.log('执行删除'); break;
  default: console.log('未知操作');
}

// 循环
for (let i = 0; i < 5; i++) {       // 计数循环
  console.log(i);                    // 0 1 2 3 4
}
for (const item of items) { /* 遍历数组（首选） */ }
for (const key in obj) { /* 遍历对象键（少用） */ }
while (condition) { /* 条件循环 */ }
```

> 📱 `for...of` 就是 Python 的 `for x in list`，碰到数组就用它。`for` 计数循环留给「需要下标做算术」的场景。

### 4.9 操作 DOM 💻

DOM（文档对象模型）是浏览器把 HTML 变成的内存树。JS 改页面 = 查树 + 改树。

```js
// ===== 查询元素 =====
document.querySelector('.box');         // 命中第一个，返回元素或 null
document.querySelector('#nav a');       // 支持完整 CSS 选择器
document.querySelectorAll('.item');     // 命中全部，返回类数组（可以 for...of）
document.getElementById('nav');         // 旧 API，等价 querySelector('#nav')
document.querySelector('input[name="q"]'); // 按属性查

// ===== 改内容 =====
const h1 = document.querySelector('h1');
h1.textContent = '新标题';              // 改文字（安全，推荐）
h1.innerHTML = '<span>新标题</span>';   // 可以塞 HTML，但有 XSS 风险（见下）

// ===== 改样式 =====
h1.style.color = 'red';
h1.style.fontSize = '24px';            // CSS 的 font-size 写成 camelCase
h1.style.display = 'none';

// ===== 改类名（推荐，配合 CSS）=====
h1.classList.add('highlight');
h1.classList.remove('highlight');
h1.classList.toggle('highlight');      // 有则删，无则加

// ===== 创建和插入元素 =====
const li = document.createElement('li');   // 建元素
li.textContent = '新列表项';
li.className = 'todo-item';
list.append(li);                          // 插到末尾（appendChild 的老写法也能用）

const btn = document.createElement('button');
btn.textContent = '删除';
li.append(btn);

// ===== 删除元素 =====
li.remove();                              // 自己删自己，最省事

// ===== 属性操作 =====
const img = document.querySelector('img');
img.src = 'new.png';
img.setAttribute('alt', '新图片说明');
img.dataset.id = '42';                    // 自定义 data-* 属性：HTML 里写 data-id="42"
```

> 🚨 **XSS 警告（必须看）**：
> ```js
> // 危险写法：如果 text 来自用户输入，用户输入 "<img src=x onerror=alert(1)>"
> // 会被浏览器当成 HTML 解析执行，这就是 XSS 注入
> el.innerHTML = `<p>${userInput}</p>`;
>
> // 安全写法：textContent 把内容当纯文本，任何字符都只会被显示
> el.textContent = userInput;
> ```
> 回忆 Django 的 `{{ 变量 }}` 默认自动转义，就是帮你防这个。JS 没有自动转义，**动态插入用户数据一律用 `textContent` 或 `createElement`，别用 `innerHTML` 拼数据**。实战 2、实战 3 全程遵守这个原则。

### 4.10 事件 💻

事件是「用户动了页面 → 你写的代码被触发」的机制。

```js
// 绑定事件：addEventListener（推荐）
const btn = document.querySelector('#submit-btn');
btn.addEventListener('click', () => {
  console.log('按钮被点击了');
});

// 事件对象：点击时浏览器会传入一个 event 参数
btn.addEventListener('click', (event) => {
  console.log(event.target);      // 实际被点击的元素
  console.log(event.type);        // 'click'
});

// 常用事件
input.addEventListener('input', () => { /* 输入框每敲一个字触发 */ });
input.addEventListener('change', () => { /* 输入框失去焦点且值变了触发 */ });
checkbox.addEventListener('change', () => { /* 勾选状态变化 */ });
form.addEventListener('submit', (e) => {
  e.preventDefault();             // 阻止表单默认提交（阻止页面刷新）
  console.log('提交了，但我们拦下来自己处理');
});

// 解绑事件
btn.removeEventListener('click', handler);
```

**表单处理的标准姿势**（实战 2 会用）：

```html
<form id="todo-form">
  <input id="todo-input" type="text" placeholder="要做什么？">
  <button type="submit">添加</button>
</form>
```

```js
const form = document.querySelector('#todo-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();                     // 1. 阻止页面刷新
  const input = document.querySelector('#todo-input');
  const text = input.value.trim();        // 2. 取输入值，trim 去空格
  if (!text) return;                      // 3. 空输入直接返回
  console.log('要添加的任务：', text);
  input.value = '';                       // 4. 清空输入框
});
```

> 📱 记住：原生表单 `submit` 会刷新页面。想用 JS 接管提交，第一行永远是 `e.preventDefault()`。Django 的 `{% csrf_token %}` 表单如果要被 JS 接管，别忘了把 token 带上（第 9 章）。

### 4.11 定时器 💻

```js
// setTimeout：延迟执行一次，返回定时器 id
const timer = setTimeout(() => {
  console.log('2 秒后执行');
}, 2000);
clearTimeout(timer);            // 取消（在还没到 2 秒前调用就取消）

// setInterval：每隔一段时间执行一次
let count = 0;
const interval = setInterval(() => {
  count++;
  console.log(`第 ${count} 秒`);
  if (count >= 5) {
    clearInterval(interval);    // 到 5 次就停
  }
}, 1000);
```

> 📱 定时器回调里的代码是「延迟执行的」，不是「同步等」的。这是理解 4.12 异步的基础。倒计时、轮询刷新列表（比如 5 秒调一次 fetch）、防抖搜索，都是它的常见用法。

### 4.12 Promise 与 async/await 📱

**先想清楚：JS 是单线程的，但网络请求、定时器这类操作不能干等。**

场景：请求后端接口要 200ms，如果 JS 干等着，页面就卡死 200ms 什么都点不了。所以 JS 用「**先答应你，回头再兑现**」的方式处理：

```js
// Promise 的三种状态：pending（进行中）→ fulfilled（成功）或 rejected（失败）
// 点外卖类比：下单 = pending，送到 = fulfilled，商家关门 = rejected
```

**传统写法 `.then()` 只需认得**：`fetch(...).then(r => r.json()).then(data => ...).catch(err => ...)`，链上每个 `.then` 拿到上一个的结果。写业务代码时 99% 用下面的 `async/await` 写法：

**现代写法：`async / await`（推荐，看着像同步代码）**

```js
async function getBook(id) {
  try {
    const resp = await fetch(`/api/books/${id}`);   // await 等 Promise 完成
    const data = await resp.json();
    console.log('拿到了', data);
  } catch (err) {
    console.error('出错了', err);
  }
}

// 并发请求多个接口：Promise.all 等全部完成
async function loadDashboard() {
  const [booksResp, statsResp] = await Promise.all([
    fetch('/api/books'),
    fetch('/api/stats'),
  ]);
  const booksData = await booksResp.json();
  const statsData = await statsResp.json();
  return { booksData, statsData };
}
```

**`async` 和 `await` 两个规则：**

1. `async function` 内部才能用 `await`。`async` 函数永远返回一个 Promise。
2. `await` 会暂停当前函数，等 Promise 有结果再继续，但**不会阻塞页面**（浏览器内部是异步调度）。

**和 Python 的 asyncio 对照（阶段 4 学过）：**

| Python | JavaScript |
|--------|-----------|
| `async def` | `async function` |
| `await` | `await` |
| `asyncio.gather(...)` | `Promise.all([...])` |
| `asyncio.create_task(...)` | 立即调用的 async 函数 / `Promise.all` |
| 事件循环 | 浏览器事件循环 |

> 📱 写业务代码时 99% 用 `async/await`。`.then()` 只要看得懂、知道它是底层机制就行。

### 4.13 fetch 发起 HTTP 请求 💻

`fetch` 是浏览器内置的发 HTTP 请求的 API，等价于 Python 的 `requests`。**这一节是实战 3 的地基。**

**GET 请求：**

```js
// 完整版（带错误检查，强烈推荐照着写）
async function loadBooks() {
  try {
    const resp = await fetch('http://localhost:8000/api/books');
    if (!resp.ok) {                   // resp.ok 为 false 表示 HTTP 状态码 >= 400
      throw new Error(`接口返回 ${resp.status}`);
    }
    const data = await resp.json();   // 解析 JSON 响应体
    return data;
  } catch (err) {
    console.error('请求失败：', err.message);
    return null;
  }
}
```

**POST 请求（提交 JSON 数据）：**

```js
const resp = await fetch('http://localhost:8000/api/books', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',   // 告诉后端 body 是 JSON
  },
  body: JSON.stringify({
    title: '流畅的 Python',
    author: 'Luciano Ramalho',
    year: 2022,
    pages: 880,
  }),
});
const data = await resp.json();
```

**带查询参数的 GET：**

```js
// 手动拼：注意中文要 encodeURIComponent 转码
const keyword = 'Python';
const resp = await fetch(
  `http://localhost:8000/api/books?q=${encodeURIComponent(keyword)}&page=1`
);

// 标准做法：用 URL 对象拼
const url = new URL('http://localhost:8000/api/books');
url.searchParams.set('q', keyword);
url.searchParams.set('page', '1');
const resp2 = await fetch(url);
```

| Python requests | JS fetch |
|-----------------|----------|
| `requests.get(url)` | `fetch(url)` |
| `resp.status_code` | `resp.status`（`resp.ok` 判断 200~299） |
| `resp.json()` | `await resp.json()` |
| `requests.post(url, json=...)` | `fetch(url, {method:'POST', body: JSON.stringify(...)})` |
| 请求失败抛异常 | 网络错误才 reject，**HTTP 4xx/5xx 不会抛异常**，要自己查 `resp.ok` |

> 🚨 **最常踩的坑**：`fetch` 遇到 404、500 不会报错，`resp.ok` 是 false 而已。不检查 `resp.ok`，拿到错误响应还继续 `resp.json()`，就会出现各种诡异问题。检查 `resp.ok` 是必写步骤。

### 4.14 JSON 与数据传递 💻

后端返回的数据在网络上传输时是 JSON **字符串**，JS 拿到后要解析成对象：

```js
// JSON 字符串 → JS 对象
const jsonText = '{"title":"流畅的 Python","year":2022}';
const obj = JSON.parse(jsonText);
console.log(obj.title);          // '流畅的 Python'

// JS 对象 → JSON 字符串（发送请求体、保存到 localStorage 时用）
const book = { title: '流畅的 Python', year: 2022 };
const json = JSON.stringify(book);
// '{"title":"流畅的 Python","year":2022}'

// 数组也可以
JSON.stringify([{ id: 1 }, { id: 2 }]);
JSON.parse('[1, 2, 3]');
```

**注意：JSON 和 JS 对象不完全一样**

- JSON 的键必须用双引号，JS 对象字面量可以不用引号。
- JSON 里没有 `undefined`，只有 `null`。
- JSON 是纯数据，不能存函数、`Date` 对象、`undefined`。

> 📱 调试必学：浏览器 Console 里 `JSON.parse` 解析后的对象可以展开看，也可以用 `console.table(数组)` 把对象数组渲染成表格，一眼看清全部数据。

### 4.15 错误处理与调试 💻

```js
// try / catch / finally：等价于 Python 的 try / except / finally
try {
  const resp = await fetch('/api/books');
  if (!resp.ok) {
    throw new Error(`请求失败：${resp.status}`);   // 主动抛错
  }
  const data = await resp.json();
  console.log(data);
} catch (err) {
  console.error('这里处理错误：', err.message);
} finally {
  console.log('不管成败都会执行（比如关掉 loading 动画）');
}
```

**调试三板斧：**

```js
console.log('普通日志');
console.warn('警告');
console.error('错误（红色）');
console.table(arrayOfObjects);       // 数组渲染成表格
console.log({ a, b, c });            // 传对象字面量，打印出变量名和值

// debugger 语句：执行到这里会暂停，配合 Sources 面板单步调试
debugger;
```

| Python | JavaScript |
|--------|-----------|
| `raise ValueError('...')` | `throw new Error('...')` |
| `try / except Exception as e` | `try { } catch (e) { }` |
| `print(x)` | `console.log(x)` |
| `pdb.set_trace()` | `debugger;` |
| 崩溃信息在终端 | 报错在浏览器 Console |

> 📱 排错顺序：先看 Console 有没有红字 → 报错定位到文件和行号 → 点击跳过去 → 在报错前一行的 `console.log` 打印关键变量。90% 的 bug 是这个流程查出来的。

---

## 五、浏览器开发者工具

前端调试全靠浏览器自带的开发者工具（DevTools）。它相当于后端的「日志 + 调试器 + curl」三合一。下面的操作以 Chrome / Edge 为例，火狐大同小异。

### 5.1 打开开发者工具 💻

| 方式 | 操作 |
|------|------|
| 快捷键 | `F12` 或 `Ctrl + Shift + I` |
| 右键菜单 | 页面任意位置右键 →「检查」 |
| 手机模拟 | `Ctrl + Shift + M`（Device Toolbar） |

界面顶部是面板切换栏：**Elements、Console、Network、Sources、Application** 等。日常开发只用前四个。

### 5.2 Elements：检查结构与样式 💻

**用途**：看页面结构、改样式、快速试效果。

- 左侧是 DOM 树，点任意元素。
- 右侧 Styles 面板列出命中该元素的全部 CSS 规则，**被覆盖的规则显示灰色加删除线**。
- 直接点灰掉的属性改成新值，页面实时变化，**改完复制回自己的 CSS 文件**。
- Computed 面板显示最终生效的样式和**盒模型图**（content/padding/border/margin 四层），排查「元素为什么这么宽」直接用。
- 右侧可以临时增删类名：选中元素 → Styles 面板最上面点 `.cls` → 输入类名回车。
- 想截图某个元素：选中元素 → 右键 →「Capture node screenshot」。

**典型排查**：「文字没居中？」选中父元素看它有没有 `text-align`、Flex 属性；「盒子太宽？」看 Computed 里的盒模型图，padding 和 border 是不是吃掉了宽度（检查有没有 `box-sizing: border-box`）。

### 5.3 Console：看日志和报错 💻

**用途**：看 `console.log` 输出、JS 报错、直接执行代码。

- 页面 JS 一报错，Console 立刻出现红色错误，带**文件名和行号**，点击直接跳到 Sources。
- 可以在 Console 里直接敲 JS 代码回车执行（临时试验 `document.querySelector` 等）。
- 网络错误（比如 fetch 被 CORS 拦截）也会出现在这里，红字会写明原因。

```
示例报错：
Access to fetch at 'http://localhost:8000/api/books' from origin
'http://localhost:5500' has been blocked by CORS policy:
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```
看到这行，说明是跨域问题，不是代码逻辑问题。实战 3 的 8.7 节专门解决它。

### 5.4 Network：观察所有网络请求 💻

**用途**：看页面发了哪些请求、请求结果、响应内容。

- 刷新页面，Network 面板记录所有请求，每个一行，显示方法、状态码、资源类型、耗时。
- 点击任意请求看详情：
  - **Headers**：请求和响应头（看 URL、方法、`Content-Type`）。
  - **Preview / Response**：响应内容，JSON 直接格式化展示（查看接口返回数据的首选位置）。
- 红色行 = 请求失败（4xx/5xx 或网络错误），一眼定位接口问题。
- 左上角有类型筛选（Fetch/XHR 专门看 AJAX 请求）。
- 想复现接口调用：右键请求 →「Copy as cURL」，把命令粘到终端跑，效果和在浏览器里一致。
- 慢速网络模拟：Network 面板顶部的「No throttling」下拉选 `Slow 3G`，测试加载体验。

**典型排查**：「页面没数据」→ 刷新，看 Fetch/XHR 有没有请求 → 看状态码 → 看 Response 是不是预期 JSON → 如果报 CORS，回 5.3 的报错信息处理。

### 5.5 Sources：断点调试 💻

**用途**：让代码执行到某一行停下来，一步步看变量值。左侧文件树找到 `app.js`，点行号打**断点**（红点）→ 刷新页面或触发操作，执行到断点自动暂停 → 右侧 Scope 面板看变量值，上方按钮**单步执行**。`debugger;` 语句等效于打一个断点。

**典型排查**：「计算出的值不对」→ 在计算代码前打断点 → 单步走 → 看变量到底是多少。

### 5.6 排查问题流程 📱

| 症状 | 去哪查 | 查什么 |
|------|--------|--------|
| 页面白屏 | Console | 有没有 JS 报错，点行号跳转 |
| 样式不对（没居中/没变色/宽了） | Elements | Styles 里规则有没有生效，Computed 看最终值 |
| 数据不显示 | Console + Network | Console 看 JS 报错；Network 看接口是否 200、Response 数据 |
| 接口返回 404/500 | Network | 看请求的 URL 和方法对不对，Response 里的错误信息 |
| fetch 报 CORS / blocked | Console | 确认是不是跨域，按 8.7 节处理 |
| 交互没反应（点按钮没动静） | Sources | 断点看事件回调有没有执行、变量值 |

> 📱 记忆口诀：**样式问题查 Elements，逻辑问题查 Console，数据问题查 Network，复杂逻辑打断点**。先缩小范围再动手改，不要瞎猜。

---

## 六、实战 1：纯静态个人主页

目标：只靠 HTML + CSS 做一个能放进简历的个人主页。做完你会亲手用上第 2、3 章几乎所有核心知识点。

### 6.1 需求与目录结构 📱

```
前端学习/
  实战1-个人主页/
    index.html      ← 页面结构
    style.css       ← 页面样式
```

功能点：

- 顶部固定导航栏（滚动时吸住，`position: sticky`）。
- Hero 欢迎区（居中排版）。
- 关于我、技能、联系方式三个区块。
- 技能用 Flex 自动换行排成标签。
- 手机上依然好看（响应式）。

### 6.2 完整代码 index.html 💻

新建 `index.html`，粘贴以下内容：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>张小明 · 个人主页</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- 页头导航：sticky 让它滚动时吸在顶部 -->
  <header class="site-header">
    <div class="container nav">
      <span class="logo">🐍 张小明</span>
      <nav>
        <a href="#about">关于我</a>
        <a href="#skills">技能</a>
        <a href="#contact">联系</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <!-- Hero 区 -->
    <section class="hero">
      <h1>你好，我是张小明</h1>
      <p>一名正在学习 Python 全栈的后端工程师，立志做出好用又好看的网站。</p>
      <a class="btn" href="#contact">联系我</a>
    </section>

    <!-- 关于我 -->
    <section id="about">
      <h2>关于我</h2>
      <p>我喜欢用代码解决问题，也喜欢把复杂的事情讲清楚。目前主攻 Python 后端，
         同时在学习前端基础，目标是成为能独立交付完整功能的全栈工程师。</p>
    </section>

    <!-- 技能 -->
    <section id="skills">
      <h2>技能</h2>
      <ul class="skill-list">
        <li>Python / Django</li>
        <li>SQL 数据库</li>
        <li>HTML / CSS / JavaScript</li>
        <li>Linux 基础</li>
        <li>Git 版本控制</li>
      </ul>
    </section>

    <!-- 联系 -->
    <section id="contact">
      <h2>联系我</h2>
      <p>邮箱：zhangxiaoming@example.com</p>
    </section>
  </main>

  <footer class="site-footer">
    <p>© 2026 张小明</p>
  </footer>
</body>
</html>
```

### 6.3 完整代码 style.css 💻

新建 `style.css`，粘贴以下内容：

```css
/* ===== 全局重置：每个项目固定开头 ===== */
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: -apple-system, "PingFang SC", "Microsoft YaHei",
               "Noto Sans CJK SC", sans-serif;
  line-height: 1.6;
  color: #2c3e50;
  background: #f8f9fa;
}

.container { max-width: 900px; margin: 0 auto; padding: 0 20px; }

/* ===== 导航栏 ===== */
.site-header {
  background: #2c3e50;
  color: #fff;
  position: sticky;        /* 滚动到顶部时吸住 */
  top: 0;
  z-index: 10;
}

.nav {
  display: flex;
  justify-content: space-between;   /* logo 靠左，菜单靠右 */
  align-items: center;
  height: 60px;
}

.nav a {
  color: #fff;
  text-decoration: none;
  margin-left: 20px;
}

.nav a:hover { color: #3498db; }

/* ===== Hero 区 ===== */
.hero { text-align: center; padding: 80px 0; }

.hero h1 { font-size: 2.4rem; margin: 0 0 10px; }

.hero p { color: #555; }

.btn {
  display: inline-block;
  background: var(--primary, #3498db);
  color: #fff;
  padding: 10px 28px;
  border-radius: 6px;
  text-decoration: none;
  margin-top: 20px;
}

.btn:hover { background: #2980b9; }

/* ===== 各区块 ===== */
section { margin: 48px 0; }

h2 { border-bottom: 2px solid #3498db; padding-bottom: 8px; }

/* 技能标签：Flex 自动换行 */
.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  list-style: none;
  padding: 0;
}

.skill-list li {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 20px;
  padding: 6px 18px;
}

/* ===== 页脚 ===== */
.site-footer {
  text-align: center;
  padding: 20px;
  background: #2c3e50;
  color: #fff;
  margin-top: 60px;
}

/* ===== 响应式：窄屏（手机）时调整 ===== */
@media (max-width: 600px) {
  .nav {
    flex-direction: column;   /* 导航改竖排 */
    height: auto;
    padding: 10px 0;
    gap: 8px;
  }
  .hero h1 { font-size: 1.8rem; }
}
```

### 6.4 运行与验证 💻

1. 双击 `index.html`，浏览器直接打开（CSS 是相对路径引用，`file://` 下也能正常加载）。
2. 或起一个本地静态服务器（模拟真实网站环境，推荐）：

```bash
cd /home/pzh/数据文件夹/杂/learning-hub/前端学习/实战1-个人主页
python -m http.server 5500
```

浏览器访问 `http://localhost:5500/`。

**验证清单：**

- [ ] 页面有标题、导航、三个区块、页脚。
- [ ] 导航栏四个链接能跳转（页内锚点）。
- [ ] 往下滚动，导航栏吸在顶部不动。
- [ ] 把浏览器窗口拉窄到手机宽度（或按 `Ctrl+Shift+M`），导航变竖排、整体不变形。
- [ ] 鼠标悬停导航链接变色。

### 6.5 挑战题 💻

1. 把配色改成你自己的主题色（用 CSS 变量 `:root { --primary: ...; }` 统一管理，把 `.btn` 里的 `var(--primary, #3498db)` 真正用起来）。
2. 加一个「技能」进度条区块（每个技能一个长条，用 CSS 宽度百分比表示熟练度）。
3. 把页脚做成三栏小布局：联系方式、常用链接、备案信息（用 Grid 或 Flex）。
4. 给自己加一张头像，注意 `max-width: 100%` 保证手机不溢出。

---

## 七、实战 2：待办事项应用

目标：写出第一个「有交互」的应用。数据在 JS 内存里，用户增删改，页面实时更新。这是前端最经典的入门项目，做完你会彻底掌握「数据 → 渲染 → 事件 → 再渲染」的闭环。

### 7.1 需求与目录结构 📱

```
前端学习/
  实战2-待办事项/
    index.html
    style.css
    app.js
```

功能点：

- 输入框输入任务，点「添加」加入列表。
- 每条任务前面有勾选框，勾选标记完成（样式变化）。
- 每条任务有「删除」按钮。
- 显示「共 X 项，未完成 Y 项」统计。
- 数据存在 JS 的一个数组里，页面渲染由 `render()` 函数全量重绘。

**核心思想先看明白：** 数据（`todos` 数组）是唯一的真相，HTML 只是它的「投影」。每次数据变化就重新 `render()` 一遍，页面永远是数据的镜像。这个「数据驱动视图」的思路，正是 React 的前身，阶段 5 会以更高级的形式见到它。

### 7.2 完整代码 index.html 💻

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>我的待办事项</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="app">
    <h1>📝 待办事项</h1>

    <form id="todo-form">
      <input id="todo-input" type="text" placeholder="要做什么？" required>
      <button type="submit">添加</button>
    </form>

    <p id="counter" class="counter"></p>
    <ul id="todo-list" class="todo-list"></ul>
  </main>

  <script src="app.js" defer></script>
</body>
</html>
```

### 7.3 完整代码 style.css 💻

```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: -apple-system, "PingFang SC", "Microsoft YaHei",
               "Noto Sans CJK SC", sans-serif;
  background: #f0f2f5;
}

.app {
  max-width: 520px;
  margin: 40px auto;
  background: #fff;
  border-radius: 10px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

h1 { margin: 0 0 16px; font-size: 1.5rem; text-align: center; }

#todo-form { display: flex; gap: 8px; margin-bottom: 12px; }

#todo-input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

#todo-form button {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  background: #3498db;
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
}

.counter { color: #888; font-size: 0.9rem; margin: 8px 0; }

.todo-list { list-style: none; padding: 0; margin: 0; }

.todo-list li {
  display: flex;            /* 勾选框 + 文字 + 删除按钮一行排开 */
  align-items: center;
  gap: 10px;
  padding: 10px 8px;
  border-bottom: 1px solid #f0f0f0;
}

.todo-list li span { flex: 1; }   /* 文字占满剩余空间 */

/* 完成态：文字变灰加删除线 */
.todo-list li.done span {
  color: #aaa;
  text-decoration: line-through;
}

.delete-btn {
  border: none;
  background: none;
  color: #e74c3c;
  cursor: pointer;
  font-size: 0.9rem;
  padding: 4px 8px;
  border-radius: 4px;
}

.delete-btn:hover { background: #fdecea; }
```

### 7.4 完整代码 app.js 💻

```js
// ===== 数据：唯一的真相来源 =====
// 每个任务 = { id, text, done }
let todos = [];

// ===== 渲染：把 todos 数组画成页面 =====
function render() {
  const list = document.querySelector('#todo-list');
  list.textContent = '';        // 清空旧列表（textContent='' 安全且高效）

  for (const todo of todos) {
    // 用 createElement 拼元素，不用 innerHTML 拼数据（防 XSS，见 4.9）
    const li = document.createElement('li');
    li.className = todo.done ? 'done' : '';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = todo.done;
    checkbox.addEventListener('change', () => toggleTodo(todo.id));

    const span = document.createElement('span');
    span.textContent = todo.text;

    const delBtn = document.createElement('button');
    delBtn.textContent = '删除';
    delBtn.className = 'delete-btn';
    delBtn.addEventListener('click', () => removeTodo(todo.id));

    li.append(checkbox, span, delBtn);
    list.append(li);
  }

  updateCounter();
}

// ===== 统计 =====
function updateCounter() {
  const doneCount = todos.filter(t => t.done).length;
  document.querySelector('#counter').textContent =
    `共 ${todos.length} 项，未完成 ${todos.length - doneCount} 项`;
}

// ===== 增 =====
function addTodo(text) {
  todos.push({ id: Date.now(), text, done: false });   // Date.now() 当唯一 id
  render();
}

// ===== 改 =====
function toggleTodo(id) {
  const todo = todos.find(t => t.id === id);
  if (todo) {
    todo.done = !todo.done;
  }
  render();
}

// ===== 删 =====
function removeTodo(id) {
  todos = todos.filter(t => t.id !== id);
  render();
}

// ===== 事件绑定 =====
const form = document.querySelector('#todo-form');
form.addEventListener('submit', (e) => {
  e.preventDefault();                       // 阻止页面刷新
  const input = document.querySelector('#todo-input');
  const text = input.value.trim();
  if (!text) return;                        // 空输入忽略
  addTodo(text);
  input.value = '';                         // 清空输入框
});

// 首次渲染
render();
```

**这段代码里值得反复看的三个点：**

1. `todos` 数组是唯一数据源，增删改都只动数组，然后调 `render()`。
2. 每一条任务用 `createElement` 创建，勾选框、文字、删除按钮都是独立事件绑定。
3. `todo.done` 改变后重新 `render()`，页面通过 CSS 类 `.done` 呈现完成态。

### 7.5 运行与验证 💻

```bash
cd /home/pzh/数据文件夹/杂/learning-hub/前端学习/实战2-待办事项
python -m http.server 5500
```

浏览器访问 `http://localhost:5500/`。

**验证清单：**

- [ ] 输入「学 HTML」，点添加，列表出现该任务，统计变「共 1 项，未完成 1 项」。
- [ ] 勾选任务，文字变灰加删除线，统计变「未完成 0 项」。
- [ ] 再勾选一次，恢复原样。
- [ ] 点删除，任务消失。
- [ ] 输入框为空时点添加，不产生空任务。
- [ ] 连续添加多条，列表顺序正确。
- [ ] 刷新页面数据丢失（正常！数据在内存里，7.6 节解决）。

### 7.6 进阶：用 localStorage 保存数据 💻

内存数据刷新就没了。浏览器提供 `localStorage` 可以在本地持久化（容量约 5MB，只存字符串）。改动很小：

```js
// 在 addTodo / toggleTodo / removeTodo 里每次改动后调用 save()
function save() {
  localStorage.setItem('todos', JSON.stringify(todos));
}

// 页面加载时读取
function load() {
  const raw = localStorage.getItem('todos');
  todos = raw ? JSON.parse(raw) : [];
}

// 改法示例：addTodo 末尾加一行
function addTodo(text) {
  todos.push({ id: Date.now(), text, done: false });
  save();        // ← 新增
  render();
}
// toggleTodo、removeTodo 同样在 render() 前加 save()

// 页面最底部：把 render() 换成先加载再渲染
load();
render();
```

刷新页面，数据还在。`JSON.stringify` / `JSON.parse` 就是 4.14 节学过的序列化与反序列化，这里派上用场了。

> 📱 `localStorage` 按「域名」隔离存储，只能存字符串。所以对象、数组必须先 `JSON.stringify` 再存，取出来再 `JSON.parse`。`sessionStorage` 用法相同，区别是关掉标签页就清空。

### 7.7 挑战题 💻

1. 加一个「清空已完成」按钮（用 `todos.filter(t => !t.done)` 重新赋值）。
2. 加三个筛选按钮：全部 / 未完成 / 已完成（用一个 `filter` 状态变量控制显示）。
3. 双击任务文字可以直接编辑（把 `span` 换成输入框，失焦时保存）。
4. 给删除按钮加确认（`confirm('确定删除？')`）。
5. 统计区域加一个小进度条：已完成数占总数的百分比，用 CSS 宽度表示。

---

## 八、实战 3：用 fetch 对接后端 API

目标：把前面学的 JS 和 `API学习/demo/server.py` 这个真实后端连起来，做一个「图书书架」页面。这是你第一次**前后端分离**，也是阶段 5 React 项目的缩小版。

### 8.1 先认识后端接口 📱

`API学习/demo/server.py` 提供这些接口（完整说明见 `API学习/demo/README.md`）：

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/api/books` | 图书列表（支持 `?page=1&page_size=10&q=关键词`） |
| `GET` | `/api/books/{id}` | 单本图书详情 |
| `POST` | `/api/books` | 创建新书（JSON body） |
| `PUT` | `/api/books/{id}` | 更新图书 |
| `DELETE` | `/api/books/{id}` | 删除图书 |
| `GET` | `/api/stats` | 统计信息 |

`GET /api/books` 返回的数据结构（这是前端要消费的「合同」）：

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [
      {
        "id": 4,
        "title": "设计模式",
        "author": "Erich Gamma",
        "year": 1994,
        "pages": 395,
        "created_at": "2026-08-12T09:23:45.123456"
      }
    ],
    "total": 4,
    "page": 1,
    "page_size": 10,
    "total_pages": 1
  }
}
```

前端要做的事就一件：`fetch` 拿这个 JSON，把 `data.items` 渲染成卡片列表。

### 8.2 目录结构 📱

```
前端学习/
  实战3-图书书架/
    index.html
    style.css
    app.js
```

### 8.3 完整代码 index.html 💻

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>图书书架 · fetch 对接后端</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="shelf">
    <h1>📚 图书书架</h1>
    <p class="subtitle">
      数据来自 <code>API学习/demo/server.py</code> 的 <code>GET /api/books</code>
    </p>

    <!-- 搜索框 -->
    <div class="toolbar">
      <input id="search-input" type="search" placeholder="搜索书名或作者…">
      <span id="total" class="total"></span>
    </div>

    <!-- 状态区：加载中 / 空 / 错误，只显示一种 -->
    <div id="status" class="status hidden"></div>

    <!-- 图书列表 -->
    <ul id="book-list" class="book-list"></ul>
  </main>

  <script src="app.js" defer></script>
</body>
</html>
```

### 8.4 完整代码 style.css 💻

```css
*, *::before, *::after { box-sizing: border-box; }

body {
  margin: 0;
  font-family: -apple-system, "PingFang SC", "Microsoft YaHei",
               "Noto Sans CJK SC", sans-serif;
  background: #f0f2f5;
  color: #2c3e50;
}

.shelf { max-width: 860px; margin: 40px auto; padding: 0 20px; }

h1 { text-align: center; font-size: 1.8rem; }

.subtitle { text-align: center; color: #888; font-size: 0.9rem; }

.subtitle code { background: #eee; padding: 2px 6px; border-radius: 4px; }

.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin: 20px 0;
}

#search-input {
  flex: 1;
  max-width: 400px;
  padding: 8px 14px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.total { color: #888; font-size: 0.9rem; }

/* 状态提示 */
.status {
  padding: 12px 16px;
  border-radius: 6px;
  margin: 12px 0;
  text-align: center;
}

.status.loading { background: #eaf3fb; color: #2c6fbb; }
.status.empty   { background: #f7f7f7; color: #888; }
.status.error   { background: #fdecea; color: #c0392b; }
.hidden { display: none; }

/* 图书卡片：响应式网格 */
.book-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
}

.book-card {
  background: #fff;
  border-radius: 10px;
  padding: 18px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: relative;          /* 让右下角 id 徽章可以绝对定位 */
  transition: transform 0.15s;
}

.book-card:hover { transform: translateY(-3px); }

.book-card h2 {
  font-size: 1.1rem;
  margin: 0 0 8px;
  padding-right: 36px;         /* 给 id 徽章留位置 */
}

.book-card p { margin: 0; color: #666; font-size: 0.9rem; }

.book-id {
  position: absolute;
  right: 14px;
  top: 14px;
  background: #3498db;
  color: #fff;
  border-radius: 10px;
  font-size: 0.75rem;
  padding: 2px 8px;
}

@media (max-width: 600px) {
  .toolbar { flex-direction: column; align-items: stretch; }
  #search-input { max-width: none; }
}
```

### 8.5 完整代码 app.js 💻

```js
// ===== 后端地址 =====
// 演示 API 用 python server.py 启动后监听在 8000 端口
const API_BASE = 'http://localhost:8000';

// 缓存 DOM 元素，避免每次查询
const listEl = document.querySelector('#book-list');
const statusEl = document.querySelector('#status');
const totalEl = document.querySelector('#total');

// ===== 拉取并渲染图书列表 =====
async function loadBooks(keyword = '') {
  showStatus('loading', '加载中…');
  listEl.textContent = '';

  try {
    // 有关键词就带查询参数（encodeURIComponent 处理中文）
    const url = keyword
      ? `${API_BASE}/api/books?q=${encodeURIComponent(keyword)}`
      : `${API_BASE}/api/books`;

    const resp = await fetch(url);

    // fetch 对 4xx/5xx 不报错，必须自己检查 resp.ok
    if (!resp.ok) {
      throw new Error(`接口返回 ${resp.status}`);
    }

    const data = await resp.json();
    const items = data.data.items;      // 走到数据：data → data.data.items
    totalEl.textContent = `共 ${data.data.total} 本`;

    if (items.length === 0) {
      showStatus('empty', '没有找到图书，换个关键词试试。');
      return;
    }

    for (const book of items) {
      listEl.append(renderBook(book));
    }
    hideStatus();
  } catch (err) {
    // 常见的两种情况：后端没启动（连接被拒），或跨域被浏览器拦截
    showStatus('error',
      `加载失败：${err.message}。请确认后端已启动、页面通过 http 访问、且 CORS 已按 8.7 节处理。`);
  }
}

// ===== 把一本图书渲染成一个卡片元素 =====
function renderBook(book) {
  const li = document.createElement('li');
  li.className = 'book-card';

  const id = document.createElement('span');
  id.className = 'book-id';
  id.textContent = `#${book.id}`;

  const title = document.createElement('h2');
  title.textContent = book.title;           // textContent，不用 innerHTML，防 XSS

  const meta = document.createElement('p');
  const pages = book.pages ? ` · ${book.pages} 页` : '';
  meta.textContent = `作者：${book.author} · 出版年份：${book.year}${pages}`;

  li.append(id, title, meta);
  return li;
}

// ===== 状态提示控制 =====
function showStatus(type, message) {
  statusEl.className = `status ${type}`;
  statusEl.textContent = message;
}

function hideStatus() {
  statusEl.className = 'status hidden';
}

// ===== 搜索：输入即搜（加 300ms 防抖，避免每敲一个字母都请求）=====
let searchTimer = null;
document.querySelector('#search-input').addEventListener('input', (e) => {
  clearTimeout(searchTimer);
  const keyword = e.target.value.trim();
  searchTimer = setTimeout(() => loadBooks(keyword), 300);
});

// ===== 页面加载后首次拉取 =====
loadBooks();
```

### 8.6 启动后端与前端 💻

**第一步：启动后端 API**（单独开一个终端）：

```bash
cd /home/pzh/数据文件夹/杂/learning-hub/API学习/demo
pip install fastapi uvicorn        # 第一次才需要
python server.py
```

看到 `Uvicorn running on http://0.0.0.0:8000` 就成功了。可以先去 `http://localhost:8000/docs` 看看 Swagger 文档，或者用 curl 验证：

```bash
curl http://localhost:8000/api/books
```

**第二步：启动前端静态服务器**（另开一个终端）：

```bash
cd /home/pzh/数据文件夹/杂/learning-hub/前端学习/实战3-图书书架
python -m http.server 5500
```

浏览器访问 `http://localhost:5500/`。

**结果**：页面显示「加载中…」后，出现 4 本图书卡片。如果直接报错误状态，看 8.7 节。

### 8.7 跨域 CORS 与两种解决路径 📱

**问题**：你的页面在 `http://localhost:5500`，API 在 `http://localhost:8000`。端口不同 = 不同源。浏览器出于安全考虑（同源策略），**默认禁止页面读取其他源的响应**。后端响应头里没有 `Access-Control-Allow-Origin`，浏览器就把响应拦下，报出 5.3 节看到的那条 CORS 错误。

**这不是 bug，是浏览器的安全机制**，所有前后端分离项目都要面对它。`API学习/demo/server.py` 没有配置 CORS（README 说了它是个骨架 demo），前端要跑起来，二选一：

**路径 A：临时测试用（不动后端代码）**

用关闭同源策略的浏览器窗口测试（Chromium 系 Chrome/Edge 通用，文件名按你系统实际来）：

```bash
chromium --disable-web-security --user-data-dir=/tmp/chrome-test
# Windows：
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir=C:\tmp\chrome-test
```

在这个新开的窗口里访问 `http://localhost:5500/`，fetch 就能读到数据。

> ⚠️ `--disable-web-security` 会关闭所有网站的同源保护，**只能用来测本地页面，用完立刻关掉这个窗口**。日常浏览请用正常窗口。`.user-data-dir` 必须带，否则会拒绝启动。

**路径 B：正规方案（给你自己以后的后端项目用）**

真实项目的前后端分离，做法是在**自己的**后端加上 CORS 中间件，白名单放行前端地址。这是标准姿势，等你自己写 FastAPI 项目时照抄（**不要改 demo/server.py**）：

```python
# 你自己的 FastAPI 项目 main.py 里：
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],   # 只放行你自己的前端地址
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Django 项目则用 `django-cors-headers`，配置 `CORS_ALLOWED_ORIGINS`。

> 📱 **一个关键认知**：你在实战 3 用的模式 B（静态页 + fetch）才有 CORS 问题。回到第 9 章的 Django 模板模式（模式 A），页面和后端同源，根本不需要 CORS。所以 Django 新手一开始碰不到 CORS，到了 React 阶段 5 才必须懂，现在提前踩了这个坑是赚到。

### 8.8 进阶：用 POST 创建图书 💻

在 `index.html` 的 `.toolbar` 前面加一个创建表单：

```html
<form id="add-form" class="add-form">
  <input name="title" placeholder="书名" required>
  <input name="author" placeholder="作者" required>
  <input name="year" type="number" placeholder="出版年份" required>
  <button type="submit">添加图书</button>
</form>
```

`style.css` 加一行：

```css
.add-form { display: flex; gap: 8px; margin-bottom: 12px; }
.add-form input { flex: 1; padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px; }
.add-form button { padding: 8px 16px; border: none; border-radius: 6px; background: #27ae60; color: #fff; cursor: pointer; }
```

`app.js` 末尾加：

```js
// ===== 创建图书（POST）=====
document.querySelector('#add-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;

  const body = {
    title: form.title.value.trim(),
    author: form.author.value.trim(),
    year: Number(form.year.value),     // 数字，别传字符串
  };

  try {
    const resp = await fetch(`${API_BASE}/api/books`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    if (!resp.ok) {
      throw new Error(`接口返回 ${resp.status}`);
    }
    form.reset();
    loadBooks();                        // 创建成功，刷新列表
  } catch (err) {
    alert(`添加失败：${err.message}（检查年份是否在 1900~2026 之间）`);
  }
});
```

成功后列表刷新，新书出现在最前面（因为 demo 按 id 倒序排列）。到 `http://localhost:8000/docs` 或 curl 确认数据真的进了后端内存。

### 8.9 验证清单 💻

- [ ] 后端终端显示 `python server.py` 启动成功。
- [ ] `curl http://localhost:8000/api/books` 返回 JSON，含 4 本预设图书。
- [ ] 前端页面 `http://localhost:5500/` 显示 4 张图书卡片。
- [ ] 搜索框输入「Python」，列表只剩书名或作者含 Python 的书。
- [ ] 搜索一个不存在的词，显示空状态提示。
- [ ] 停掉后端（Ctrl+C），刷新页面，显示红色错误提示而不是白屏。
- [ ] 用 POST 表单添加一本书，列表立刻刷新并出现在最前。
- [ ] 浏览器 Console 无红色报错。

> 💪 **全栈里程碑**：到这里，你完成了一次真正的「前端 → HTTP → 后端 → 前端」完整数据链路。这个图书书架就是你未来 React 管理后台的最小雏形。

---

## 九、与 Django 模板的结合

这一章把前面学的 HTML/CSS/JS 翻译成 Django 的用法。学完你可以放心回去读《Django 完全指南》第 6 章（模板层）和第 11 章（静态文件），会发现那些代码你已经全看得懂，只是换了一层语法。

### 9.1 前端知识在 Django 里的位置 📱

Django 模板 = HTML + 模板语法。三样前端基础分别对应：

| 前端基础 | 在 Django 里的位置 |
|----------|--------------------|
| HTML 结构 | 模板文件 `templates/*.html`，用 `{% %}` 和 `{{ }}` 嵌入数据 |
| CSS 样式 | 静态文件 `static/*.css`，用 `{% static %}` 引入 |
| JavaScript | 静态文件 `static/*.js`，用 `<script src="{% static %}" defer>` 引入 |

请求流程（对照 1.2 节的模式 A）：

```
浏览器请求 /books
  → Django 视图查数据库得到 books 列表
  → 用模板把 books 填充进 HTML（此时页面上已经有数据）
  → 返回完整的 HTML 页面
  → 浏览器拿到后，再加载 CSS 和 JS 文件并执行
```

所以模板里能看到的 `{{ book.title }}`，到了浏览器就成了 `流畅的 Python`。**模板语法是「服务端先渲染，再发给浏览器」，和 JS 的「浏览器里动态渲染」是两个阶段**，这是理解 Django 模板最关键的一点。

### 9.2 模板语法对照表 📱

| 场景 | Django 模板 | JavaScript |
|------|-------------|-----------|
| 输出一个变量 | `{{ name }}` | `` `\${name}` `` |
| 条件判断 | `{% if x %}...{% endif %}` | `if (x) { }` |
| 循环 | `{% for b in books %}...{% endfor %}` | `for (const b of books) { }` |
| 空数据兜底 | `{% for ... %}{% empty %}暂无{% endfor %}` | `if (items.length === 0)` |
| 处理字符串 | `{{ name\|upper }}` 过滤器 | `name.toUpperCase()` |
| 默认值 | `{{ x\|default:"暂无" }}` | `x ?? '暂无'` |
| 注释 | `{# 不会发给浏览器 #}` | `// 会发给浏览器` |
| 拼接链接 | `{% url 'post_detail' slug %}` | `` `/api/${id}` `` |
| 引用静态文件 | `{% static 'app/style.css' %}` | 相对路径 `style.css` |
| 防 XSS | `{{ 变量 }}` **自动转义** | 用 `textContent`，**无自动转义** |

**两条最该记的对应关系：**

1. Django 的 `{{ }}` 是「服务端填入数据」，JS 的模板字符串是「浏览器填入数据」。前者页面刷新一次就定型，后者可以随时变。
2. Django 的 `{% for %}` 和 JS 的 `for...of` 都是遍历，区别是 Django 在服务端把 HTML 拼完，JS 在浏览器动态创建。实战 2 用 JS 拼列表，Django 里就是：

```html+django
<ul>
  {% for book in books %}
    <li>{{ book.title }} · {{ book.author }}（{{ book.year }}）</li>
  {% empty %}
    <li>暂无图书</li>
  {% endfor %}
</ul>
```

> 📱 阶段 5 学 React 时你还会看到第三种写法：JSX 里用 `{books.map(b => <li>{b.title}</li>)}`。三种都是「循环渲染列表」，底层思想一致。

### 9.3 静态文件管理 📱

Django 默认把 CSS/JS/图片叫**静态文件**（static），配置见《Django 完全指南》第 11 章。目录结构规范：

```
myproject/
  myapp/
    static/
      myapp/                  # 惯例：static 下再套一层 app 名，防重名
        css/
          style.css
        js/
          app.js
  templates/
    base.html
```

模板里引用：

```html+django
{% load static %}          <!-- 第一行先加载 static 标签库 -->

<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
<script src="{% static 'myapp/js/app.js' %}" defer></script>
<img src="{% static 'myapp/img/logo.png' %}" alt="logo">
```

`{% static %}` 会根据 `settings.py` 里的 `STATIC_URL` 自动生成 URL（开发默认 `/static/...`），部署到 CDN 时也只要改一处配置。这就是「外部 CSS/JS 文件」的 Django 正式版，对应 3.1 节的推荐写法。

### 9.4 完整例子：base.html 与列表页 💻

把实战 1 的页面拆成 Django 的「基础模板 + 子模板」，这是《Django 完全指南》6.3 节的内容，这里给出能直接跑的骨架：

**`templates/base.html`（页面骨架，子页面共用）：**

```html+django
{% load static %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}我的网站{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
</head>
<body>
  <header class="site-header">
    <nav>
      <a href="{% url 'post_list' %}">首页</a>
      <a href="{% url 'about' %}">关于</a>
    </nav>
  </header>

  <main class="container">
    {% block content %}{% endblock %}   <!-- 子页面内容填这里 -->
  </main>

  <footer>
    <p>© 2026 我的网站</p>
  </footer>

  <script src="{% static 'myapp/js/app.js' %}" defer></script>
</body>
</html>
```

**`templates/blog/index.html`（子模板：图书列表页）：**

```html+django
{% extends 'base.html' %}

{% block title %}图书列表{% endblock %}

{% block content %}
  <h1>图书列表</h1>

  <ul class="book-list">
    {% for book in books %}
      <li class="book-card">
        <h2>{{ book.title }}</h2>
        <p>作者：{{ book.author }} · {{ book.year }}</p>
      </li>
    {% empty %}
      <li>暂无图书</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**视图**（`views.py`，模板里的 `books` 来自这里）：

```python
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "blog/index.html", {"books": books})
```

**CSS 用谁？** 第 3 章学的所有选择器、Flex、Grid、媒体查询，在这里照用不误，只是 `class` 名换成你在模板里写的那些。

### 9.5 把后端数据安全地交给 JS 📱

有时页面初值由 Django 渲染，但后续交互需要 JS 拿到同一份数据。用 Django 内置的 `json_script` 过滤器，把 Python 数据安全地序列化进页面，JS 再读出来：

```html+django
{% load static %}

<!-- 把 books 序列化成 JSON，藏进 id 为 books-data 的 <script type="application/json"> 里 -->
{{ books|json_script:"books-data" }}

<script src="{% static 'myapp/js/books.js' %}" defer></script>
```

```js
// books.js：从页面读数据，注意要等 DOM 就绪（defer 已保证）
const books = JSON.parse(document.getElementById('books-data').textContent);
console.log(books);
```

这样既享受了 Django 渲染服务端数据的便利，又让 JS 拿得到初始数据，还能避免把 Python 对象直接塞进 JS 引号里的转义灾难。`json_script` 自带 HTML 转义，比手动拼 `<script>var data = {{ data }};</script>` 安全得多。

### 9.6 什么时候用 Django 渲染，什么时候用 JS 📱

| 场景 | 推荐做法 |
|------|----------|
| 列表初始内容、表单初始值、页面骨架 | Django 模板渲染（服务端拼好，首屏快，天然防 XSS） |
| 用户点击后的局部变化（勾选、删除、展开） | JS 操作 DOM（如实战 2 的方式） |
| 提交表单 | 简单表单用 Django 表单 + `{% csrf_token %}`；需要局部刷新时用 fetch 带 CSRF token |
| 实时数据（搜索联想、聊天、通知） | JS fetch 轮询或 WebSocket |
| 页面路由、复杂交互、状态管理 | 阶段 5 的 React / Vue（前后端分离） |

> 📱 **具体建议**：在 Django 项目里，初始数据列表用模板 `{% for %}` 渲染，**增删改后的局部更新**用 JS。比如点「删除」后 JS 直接移除 DOM 里的那个 `<li>`，同时发请求给后端，比整页刷新体验好很多。这就是「服务端渲染 + 前端增强」的经典组合，也是 Django 新手最容易上手的全栈姿势。

---

## 十、前端学习下一步路线

恭喜，到这里你已经有能力看懂并修改任何一个 Django 项目的模板了。接下来要不要学框架，看两条路：

| 路线 | 适合 | 学习起点 |
|------|------|----------|
| **React + TypeScript + Next.js** | 全栈计划主线的选择，岗位最多、生态最大，面试高频 | 《Python 全栈工程师完整学习计划》阶段 5，从 React 官方文档 Quick Start 开始 |
| **Vue 3 + Nuxt** | 国内中小公司流行，学习曲线更平缓，中文资料多 | Vue 官方教程，或 Python-100-Days 自带 Vue 入门 |

**一句话选型**：想按仓库的全栈计划走就选 React，想更快上手国内岗位就选 Vue，两者核心的组件化 + 数据驱动思想一样，本指南第 7 章的「数据驱动视图」就是它们的共同祖先。无论选哪个，先把这里 JS 数组方法、fetch、Promise 练熟，学框架会顺畅得多。

---

## 十一、章节练习汇总

### HTML

1. 写一个完整的 HTML 文档骨架（含 UTF-8 和 viewport 声明），解释每行的作用。
2. 做一个「学习进度」表格：阶段、内容、完成状态，用 `thead/tbody` 结构。
3. 用语义化标签重构这段「div 汤」（`<div class="top"><div class="menu"><a href="#">首页</a></div></div>` + 正文 + 页脚），并说明每个语义标签为什么合适。
4. 写一个注册表单：用户名、密码、邮箱、性别单选、爱好多选、城市下拉、个人介绍，全部带 label，必填项加 `required`。
5. 回答：`method="get"` 和 `method="post"` 提交后，数据分别去哪里？Django 端用什么取？
6. 列出 4 个已废弃的 HTML 标签，并写出各自的现代替代方案。

### CSS

1. 写出 4 种选择器，并说出它们的优先级排序（ID / 类 / 标签 / 通配符）。
2. 给一个 200px 宽、20px padding、2px border 的盒子算实际总宽度：`content-box` 和 `border-box` 各是多少？为什么项目里统一用 `border-box`？
3. 用三种不同的 CSS 写法实现一个元素水平垂直居中，并说明各自适用场景。
4. 写一个三栏布局：左右各 200px 固定，中间自适应（Flex 方案），再写一个 Grid 方案。
5. 写一段媒体查询：手机（<768px）单列，桌面（≥1024px）三列，说明「移动优先」的写法。
6. 用自己的配色定义 4 个 CSS 变量（主色、成功色、危险色、间距），并用在按钮和卡片上。
7. 解释 `px`、`rem`、`vw`、`fr` 的区别，各举一个适用场景。

### JavaScript

1. 说出 `let`、`const`、`var` 的区别，以及 `===` 和 `==` 的区别。
2. 用 `map`、`filter`、`reduce` 分别处理数组 `[1, 2, 3, 4, 5]`：全部乘 2、取偶数、求和。
3. 定义一个图书对象数组，用 `find` 按 id 查一本，用 `filter` 筛某作者，用 `map` 取全部书名。
4. 解释 `textContent` 和 `innerHTML` 的区别，为什么动态插入用户数据必须用 `textContent`？
5. 给一个表单写 submit 事件：阻止默认提交、取输入值、清空输入框（实战 2 的代码改造成自己的需求）。
6. 用 `async/await` 写一个函数：fetch 一个接口，检查 `resp.ok`，解析 JSON，catch 里打印错误，并在 finally 里提示加载完成。
7. 说出 `fetch` 在什么情况下会抛出异常、什么情况下不会，为什么必须检查 `resp.ok`？

### 浏览器开发者工具

1. 打开你的实战 2 页面，用 Elements 面板临时把一个任务的文字改色，再把改动同步回 CSS 文件。
2. 用 Network 面板复现实战 3 的图书请求：找到那条 `GET /api/books`，查看它的响应 JSON 和状态码。
3. 故意停掉后端，刷新实战 3 页面，在 Console 里找到报错，说明报错内容和排查步骤。
4. 用 Console 执行 `document.querySelectorAll`，统计你主页上有几个 `<section>`。

### 实战拓展

1. 给实战 1 加一个深色/浅色主题切换按钮（用 CSS 变量 + `classList.toggle`，JS 只需要几行）。
2. 给实战 2 加「筛选：全部 / 未完成 / 已完成」三个按钮。
3. 给实战 3 加一个「统计」区域，用 `GET /api/stats` 显示总书数和作者数。
4. 把实战 3 的图书列表改成表格视图（`<table>`），并加一个按年份降序排序按钮（先 `[...items].sort()` 再重新渲染）。
5. 在 Django 里把实战 1 的个人主页改成 base.html + 子模板结构，CSS 走 `{% static %}`，跑通 `runserver` 后用浏览器确认样式和实战 1 一致。

---

> **最后的建议**：
> 1. 前端是「练」出来的不是「看」出来的。每个实战至少亲手敲一遍，改错、调试、修复，才算学会。
> 2. 排查问题永远先看浏览器开发者工具，再猜代码。工具会告诉你答案。
> 3. 遇到不懂的标签或属性，去 [MDN](https://developer.mozilla.org/zh-CN/docs/Web) 查，它是最权威的参考手册。
> 4. 想深入 JS 原理，中文最好的教程是[现代 JavaScript 教程](https://zh.javascript.info/)，全栈计划阶段 5 也推荐它。
> 5. 学完本指南，下一步就是《Python 全栈工程师完整学习计划》阶段 5 的 React/TypeScript，你已经有地基了。

---

*文档版本：v1.0 | 生成日期：2026-08-26 | 11 章 | 2000+ 行 | 含 3 个实战项目与练习题 | 关联：Django完全指南 §6/§11、API学习 demo、Python全栈计划 阶段5*
