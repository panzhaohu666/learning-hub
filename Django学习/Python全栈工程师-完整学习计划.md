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
