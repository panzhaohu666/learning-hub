# API 完全指南 —— 从零基础到实战

> 适用对象：零基础入门 | 涵盖：API 基础概念、RESTful 设计、HTTP 协议、认证鉴权、API 文档、调用实战、设计最佳实践
> 配套仓库：[Public APIs](https://github.com/public-apis/public-apis) — 海量免费公开 API 合集

> **🔑 一句话理解：API = 远程函数 + JSON 返回值**
>
> API 就是把一个函数放到服务器上，你用 HTTP 请求去调用它，它把结果用 JSON 还给你。唯一区别：本地函数用 `( )` 传参，API 用 URL 或 JSON body 传参。

---

## 目录

1. [API 基础认知](#一api-基础认知)
   - [什么是 API](#11-什么是-api)
   - [API 的工作原理（餐厅类比）](#12-api-的工作原理餐厅类比)
   - [现实生活中 API 无处不在](#13-现实生活中-api-无处不在)
2. [HTTP 协议基础](#二http-协议基础)
   - [HTTP 请求结构](#21-http-请求结构)
   - [HTTP 响应结构](#22-http-响应结构)
   - [常用 HTTP 方法](#23-常用-http-方法)
   - [HTTP 状态码速查](#24-http-状态码速查)
3. [API 的四大类型](#三api-的四大类型)
   - [REST API](#31-rest-api)
   - [GraphQL](#32-graphql)
   - [SOAP](#33-soap)
   - [WebSocket / gRPC](#34-websocket--grpc)
4. [REST API 深入](#四rest-api-深入)
   - [核心设计原则](#41-核心设计原则)
   - [URL 设计规范](#42-url-设计规范)
   - [请求与响应格式](#43-请求与响应格式)
   - [分页、排序、过滤](#44-分页排序过滤)
   - [版本管理](#45-版本管理)
5. [API 认证与授权](#五api-认证与授权)
   - [API Key](#51-api-key)
   - [Basic Auth](#52-basic-auth)
   - [JWT（JSON Web Token）](#53-jwtjson-web-token)
   - [OAuth 2.0](#54-oauth-20)
   - [认证方式对比](#55-认证方式对比)
6. [API 文档](#六api-文档)
   - [Swagger / OpenAPI](#61-swagger--openapi)
   - [手写 API 文档](#62-手写-api-文档)
7. [调用 API 实战](#七调用-api-实战)
   - [curl 命令行](#71-curl-命令行)
   - [Python 调用](#72-python-调用)
   - [JavaScript 调用](#73-javascript-调用)
   - [Postman 工具](#74-postman-工具)
8. [API 设计最佳实践](#八api-设计最佳实践)
9. [推荐免费公开 API](#九推荐免费公开-api)
10. [常见问题 FAQ](#十常见问题-faq)
11. [GraphQL 入门](#十一graphql-入门)
    - [REST vs GraphQL 深入对比](#111-rest-vs-graphql-深入对比)
    - [Schema 定义与类型系统](#112-schema-定义与类型系统)
    - [Query、Mutation、Subscription](#113-query-mutation-subscription)
    - [Python Strawberry 实战](#114-python-strawberry-实战)
    - [N+1 问题与 DataLoader](#115-n1-问题与-dataloader)
12. [gRPC 与 Protobuf](#十二grpc-与-protobuf)
    - [gRPC 核心概念](#121-grpc-核心概念)
    - [Protobuf 编写](#122-protobuf-编写)
    - [Python gRPC 完整示例](#123-python-grpc-完整示例)
    - [gRPC vs REST 选型决策树](#124-grpc-vs-rest-选型决策树)
13. [WebSocket 实时通信](#十三websocket-实时通信)
    - [WebSocket 握手过程](#131-websocket-握手过程)
    - [FastAPI WebSocket 聊天室](#132-fastapi-websocket-聊天室)
    - [Socket.IO vs 原生 WebSocket](#133-socketio-vs-原生-websocket)
    - [心跳与重连策略](#134-心跳与重连策略)
14. [API 版本管理策略](#十四api-版本管理策略)
    - [三种版本方式详解](#141-三种版本方式详解)
    - [弃用策略与迁移指南](#142-弃用策略与迁移指南)
15. [API 限流与防护](#十五api-限流与防护)
    - [四种限流算法](#151-四种限流算法)
    - [Python 实现令牌桶](#152-python-实现令牌桶)
    - [FastAPI 限流中间件](#153-fastapi-限流中间件)
    - [认证方案选型](#154-认证方案选型)
16. [API 测试与监控](#十六api-测试与监控)
    - [pytest + httpx 自动化测试](#161-pytest--httpx-自动化测试)
    - [Postman Collection 管理](#162-postman-collection-管理)
    - [性能测试 k6/locust](#163-性能测试-k6locust)
    - [监控指标体系](#164-监控指标体系)
17. [API 设计最佳实践（进阶）](#十七api-设计最佳实践进阶)
    - [分页策略 cursor vs offset](#171-分页策略-cursor-vs-offset)
    - [HATEOAS 超媒体驱动](#172-hateoas-超媒体驱动)
    - [OpenAPI 3.0 规范详解](#173-openapi-30-规范详解)
    - [常见反模式与避坑指南](#174-常见反模式与避坑指南)

---

## 一、API 基础认知

### 1.1 什么是 API

**API = Application Programming Interface（应用程序编程接口）**

简单说：**API 就是两个程序之间通信的约定**——你按对方规定的格式发请求，对方按规定格式返回结果。

```
┌───────────┐      请求(Request)      ┌───────────┐
│           │ ──────────────────────→ │           │
│  客户端    │    "给我今天的天气"       │  服务端    │
│  (你的App) │ ←────────────────────── │  (API)    │
│           │      响应(Response)      │           │
└───────────┘   {"temp":25,"weather": └───────────┘
                 "晴","city":"北京"}
```

**API 不是什么神秘的东西**，你每天都在用：
- 打开天气 App → 内部调用了天气 API
- 微信扫码支付 → 调用了微信支付 API
- 用手机号登录 → 调用了短信验证码 API
- 在网页搜"附近的餐厅" → 调用了地图 API

**API 和本地函数的区别**：

| | 本地函数 | 远程 API |
|---|---------|---------|
| 写法 | `def add(a, b): return a + b` | `@app.get("/add")` |
| 调用方式 | `result = add(1, 2)` | `curl "http://api.com/add?a=1&b=2"` |
| 传参 | 括号传参 `add(1, 2)` | URL 参数 `?a=1&b=2` 或 JSON body |
| 返回值 | 直接 return `3` | 返回 JSON `{"result": 3}` |
| 通信方式 | 同一进程内 | 通过网络（HTTP） |
| 运行位置 | 你电脑上 | 远程服务器上 |

> **本质完全相同：都是调用一个函数，拿回一个结果。唯一的区别就是中间隔了一条网线。**

### 1.2 API 的工作原理（餐厅类比）

| 角色 | 对应 | 说明 |
|------|------|------|
| **你（顾客）** | 客户端 | 你的 App 或程序 |
| **菜单** | API 文档 | 告诉你能点什么、怎么点、参数是什么 |
| **服务员** | API 本身 | 接收你的请求，传给后厨，把结果带回来 |
| **后厨** | 服务器 | 真正处理数据的地方 |

```
你走进餐厅 → 看菜单 → 点"宫保鸡丁" → 服务员传话 → 后厨做菜 → 服务员端回来
你打开App  → 看文档 → 调 send_sms() → API 转发   → 服务器处理 → 返回结果
```

**核心好处**：你不需要知道后厨怎么炒菜（服务器内部逻辑），只要会看菜单（API 文档）就行。

### 1.3 现实生活中 API 无处不在

| 场景 | 背后的 API |
|------|-----------|
| 天气 App 显示"今天 25°C" | OpenWeatherMap API / 和风天气 API |
| 收到短信验证码 | 阿里云短信 API / Twilio API |
| 微信支付扫码付款 | 微信支付 API |
| 地图导航 | 高德地图 API / Google Maps API |
| 用 GitHub 登录某个网站 | GitHub OAuth API |
| ChatGPT 回答问题 | OpenAI API |
| 网站显示"今日热搜" | 微博 API / 百度 API |
| 翻译一段英文 | 百度翻译 API / DeepL API |

---

## 二、HTTP 协议基础

大多数 Web API 基于 HTTP 协议通信。理解 HTTP 是理解 API 的前提。

### 2.1 HTTP 请求结构

一个完整的 HTTP 请求包含四部分：

```
POST /api/users HTTP/1.1           ← 请求行（方法 + 路径 + 协议版本）
Host: api.example.com              ←
Content-Type: application/json     ← 请求头（Headers）
Authorization: Bearer xxxxxxxx     ←
                                   ← 空行（分隔符）
{                                  ←
  "name": "张三",                   ← 请求体（Body）
  "email": "zhangsan@example.com"  ←
}                                  ←
```

**请求行详解**：
```
GET    /api/posts?page=1&limit=10    HTTP/1.1
↑               ↑                        ↑
方法         路径 + 查询参数           协议版本
```

### 2.2 HTTP 响应结构

```
HTTP/1.1 200 OK                                  ← 状态行
Content-Type: application/json; charset=utf-8    ← 响应头
Content-Length: 156                              ←
                                                 ← 空行
{                                                ←
  "code": 200,                                   ←
  "message": "success",                          ← 响应体（Body）
  "data": {                                      ←
    "id": 1,                                     ←
    "name": "张三"                                ←
  }                                              ←
}                                                ←
```

### 2.3 常用 HTTP 方法

| 方法 | 含义 | 对应数据库操作 | 示例 |
|------|------|---------------|------|
| **GET** | 获取资源 | SELECT | `GET /api/posts` → 获取文章列表 |
| **POST** | 创建资源 | INSERT | `POST /api/posts` → 新建一篇文章 |
| **PUT** | 完整更新资源 | UPDATE | `PUT /api/posts/1` → 完全替换文章 |
| **PATCH** | 部分更新资源 | UPDATE | `PATCH /api/posts/1` → 只改标题 |
| **DELETE** | 删除资源 | DELETE | `DELETE /api/posts/1` → 删除文章 |
| **HEAD** | 同 GET 但不返回 Body | — | 检查资源是否存在 |
| **OPTIONS** | 查询支持的方法 | — | CORS 预检请求 |

> **PUT vs PATCH**：PUT 是"整个替换"（你不传的字段会被清空），PATCH 是"只改你传的"。

### 2.4 HTTP 状态码速查

```
1xx  信息    100 Continue            继续发送请求体
2xx  成功    200 OK                  请求成功
             201 Created             创建成功（POST 后返回）
             204 No Content          成功但无返回内容（DELETE 后）
3xx  重定向  301 永久重定向           URL 已永久变更
             302 临时重定向           URL 临时跳转
             304 Not Modified        内容未变（缓存用）
4xx  客户端  400 Bad Request         请求参数错误
             401 Unauthorized        未登录/未认证
             403 Forbidden           已登录但权限不足
             404 Not Found           资源不存在
             405 Method Not Allowed  方法不允许（如对只读接口发 POST）
             422 Unprocessable       参数格式正确但语义错误
             429 Too Many Requests   请求频率过高
5xx  服务端  500 Internal Server    服务器内部错误
             502 Bad Gateway         网关错误（上游服务挂了）
             503 Service Unavailable 服务暂时不可用（维护中）
             504 Gateway Timeout     网关超时
```

> **速记口诀**：2xx 成功，4xx 你的锅，5xx 我的锅。

---

## 三、API 的四大类型

### 3.1 REST API

**最主流、你 90% 会遇到的类型。**

REST = Representational State Transfer（表述性状态转移），核心思想：**把服务器上的一切都看作"资源"，用 URL 定位资源，用 HTTP 方法操作资源。**

```
GET    /api/posts          → 获取文章列表
GET    /api/posts/1        → 获取 ID 为 1 的文章
POST   /api/posts          → 新建文章
PUT    /api/posts/1        → 更新 ID 为 1 的文章
DELETE /api/posts/1        → 删除 ID 为 1 的文章
```

**特点**：
- ✅ 简单直观，URL 即资源
- ✅ 无状态（每次请求独立，不依赖"会话"）
- ✅ 使用标准 HTTP 方法和状态码
- ✅ 数据格式通常是 JSON

### 3.2 GraphQL

**Facebook 开源的查询语言**——解决 REST 的"过度获取"和"获取不足"问题。

```
# REST 的问题：要拿用户 + 用户文章，需要两次请求
GET /api/users/1          → 返回用户全部字段（可能你只要名字）
GET /api/users/1/posts    → 返回文章全部字段（可能你只要标题）

# GraphQL 一次搞定：
query {
  user(id: 1) {
    name           ← 只要名字
    posts {        ← 只要标题
      title
    }
  }
}
```

**特点**：
- ✅ 前端决定要什么数据，减少无效传输
- ✅ 一次请求获取多资源
- ❌ 学习曲线更陡
- ❌ 缓存比 REST 复杂

### 3.3 SOAP

**老牌企业级协议（XML 格式）**，银行、支付系统仍在用。

```xml
<!-- SOAP 请求 -->
<soap:Envelope>
  <soap:Body>
    <GetUser>
      <UserId>1</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>
```

**特点**：
- ✅ 严格规范，安全性强
- ❌ 冗长，XML 比 JSON 重得多
- ❌ 学习曲线陡峭

### 3.4 WebSocket / gRPC

| 类型 | 适用场景 | 特点 |
|------|---------|------|
| **WebSocket** | 聊天、实时通知、股票行情 | 全双工，服务端可主动推送 |
| **gRPC** | 微服务间高性能通信 | Google 出品，基于 Protocol Buffers，比 REST 快 5-10 倍 |

**四种类型对比**：

| | REST | GraphQL | SOAP | gRPC |
|------|------|------|------|------|
| 数据格式 | JSON | JSON | XML | Protobuf（二进制） |
| 学习难度 | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 性能 | 中 | 中 | 低 | 高 |
| 适用场景 | 通用 Web API | 复杂数据需求的 App | 银行/支付/企业 | 微服务内部通信 |
| 市场份额 | 🏆 主流 | 增长中 | 遗留系统 | 云原生 |

---

## 四、REST API 深入

### 4.1 核心设计原则

| 原则 | 说明 | 反例 |
|------|------|------|
| **资源导向** | URL 是名词（资源），不是动词（动作） | ❌ `GET /getPosts` ✅ `GET /posts` |
| **HTTP 方法表达动作** | 用 GET/POST/PUT/DELETE 操作资源 | ❌ `POST /deleteUser` ✅ `DELETE /users/1` |
| **无状态** | 每次请求包含所有需要的信息 | ❌ 依赖服务端 session |
| **统一接口** | 一致的 URL 模式和响应格式 | ❌ 有的返回 JSON，有的返回 XML |
| **层级结构** | 用 `/` 表示资源关系 | ✅ `/users/1/posts/5/comments` |

### 4.2 URL 设计规范

```
✅ 好的设计                          ❌ 差的设计
──────────────────────────────────────────────────
GET    /api/users                   GET    /api/getUsers
GET    /api/users/1                 GET    /api/users?id=1
POST   /api/users                   POST   /api/createUser
PUT    /api/users/1                 POST   /api/updateUser/1
DELETE /api/users/1                 GET    /api/deleteUser?id=1
GET    /api/users/1/posts           GET    /api/getPostsByUser?userId=1
```

**URL 命名规则**：
- 全小写，用 `-` 分隔（不用 `_` 或驼峰）
  - ✅ `/api/blog-posts` 
  - ❌ `/api/blogPosts` `/api/blog_posts`
- 资源用**复数**名词
  - ✅ `/api/users` 
  - ❌ `/api/user`
- 避免过深嵌套（最多 3 层）
  - ✅ `/api/users/1/posts` 
  - ❌ `/api/users/1/posts/5/comments/8/replies`

### 4.3 请求与响应格式

**标准请求格式（POST 示例）**：
```json
POST /api/posts
Content-Type: application/json

{
  "title": "我的第一篇文章",
  "content": "这是正文内容",
  "category_id": 1,
  "tags": ["Python", "API"],
  "published": true
}
```

**标准成功响应**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 42,
    "title": "我的第一篇文章",
    "slug": "my-first-post",
    "created_at": "2026-08-10T12:00:00Z"
  }
}
```

**标准列表响应**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [ ... ],
    "total": 150,
    "page": 1,
    "page_size": 10,
    "total_pages": 15
  }
}
```

**标准错误响应**：
```json
{
  "code": 422,
  "message": "参数验证失败",
  "errors": {
    "title": "标题不能为空",
    "email": "邮箱格式不正确"
  }
}
```

> **核心原则**：统一响应格式——不管成功失败，客户端都能用同一套代码解析。

### 4.4 分页、排序、过滤

```bash
# 分页（最常用）
GET /api/posts?page=1&limit=10          # 第1页，每页10条
GET /api/posts?offset=20&limit=10       # 跳过前20条，取10条

# 排序
GET /api/posts?sort=created_at          # 按创建时间排序
GET /api/posts?sort=-created_at         # 降序（加 - 号）

# 过滤
GET /api/posts?status=published         # 只看已发布的
GET /api/posts?category=python          # 只看 Python 分类
GET /api/posts?tag=api&tag=rest         # 同时包含 api 和 rest 标签

# 搜索
GET /api/posts?q=FastAPI                # 全文搜索
GET /api/posts?title__contains=Python   # 模糊匹配

# 字段筛选（只要部分字段）
GET /api/posts?fields=id,title,slug     # 只要 id, title, slug
```

### 4.5 版本管理

三种常见方式：

```bash
# 方式 1：URL 路径（最常用）
GET /api/v1/posts
GET /api/v2/posts

# 方式 2：请求头（GitHub 的做法）
GET /api/posts
Accept: application/vnd.github.v3+json

# 方式 3：查询参数
GET /api/posts?version=1
```

> **推荐用 URL 路径方式** `/api/v1/`，最直观、最容易被发现。

---

## 五、API 认证与授权

**认证（Authentication）** = 你是谁？（验证身份）
**授权（Authorization）** = 你能做什么？（检查权限）

### 5.1 API Key

最简单的方式——把密钥放在请求里。

```bash
# 方式 1：查询参数
GET /api/weather?key=abc123def456&city=beijing

# 方式 2：请求头（推荐，不会出现在 URL 日志里）
GET /api/weather?city=beijing
X-API-Key: abc123def456
```

**适用场景**：公开 API、服务间调用、简单的身份识别  
**缺点**：密钥泄露 = 别人可以冒充你

### 5.2 Basic Auth

HTTP 标准认证方式——把 `用户名:密码` 做 Base64 编码。

```bash
# curl 示例
curl -u admin:admin123 https://api.example.com/users

# 本质是加了 Header：
Authorization: Basic YWRtaW46YWRtaW4xMjM=
#              ↑ Base64("admin:admin123")
```

> ⚠️ **必须配合 HTTPS 使用**，否则密码明文暴露。

### 5.3 JWT（JSON Web Token）

**目前最主流的 API 认证方式**。

```
登录流程：
1. 用户 POST /api/auth/login  {username, password}
2. 服务器验证通过，返回 JWT Token
3. 客户端把 Token 存起来（localStorage / cookie）
4. 后续请求在 Header 里带上 Token
5. 服务器验证 Token 有效性后响应
```

**JWT 结构**（三段，用 `.` 分隔）：

```
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
│                      │                     │
├── Header（头部）      ├── Payload（载荷）    ├── Signature（签名）
│  算法 = HS256         │  user_id = 1         │  防篡改的签名
│  类型 = JWT           │  exp = 过期时间       │
```

**Python 示例**：
```python
import requests

# 1. 登录获取 Token
response = requests.post("https://api.example.com/auth/login", json={
    "username": "admin",
    "password": "admin123"
})
token = response.json()["access_token"]

# 2. 后续请求带上 Token
headers = {"Authorization": f"Bearer {token}"}
posts = requests.get("https://api.example.com/api/posts", headers=headers)
print(posts.json())
```

**Access Token + Refresh Token 双 Token 模式**（生产环境推荐）：

| Token | 有效期 | 作用 |
|-------|-------|------|
| Access Token | 短（15分钟 - 2小时） | 调用 API |
| Refresh Token | 长（7天 - 30天） | 获取新的 Access Token |

> 为什么？Access Token 过期快 → 即使泄露影响小。Refresh Token 换新时不需重输密码。

### 5.4 OAuth 2.0

**"用 GitHub 登录"、"用微信登录"** 就是 OAuth 2.0。

```
你的网站                       GitHub                     用户
  │                              │                         │
  │  1. 用户点"用GitHub登录"       │                         │
  │ ────────────────────────────→│                         │
  │                              │  2. 跳转 GitHub 授权页    │
  │                              │ ←──────────────────────→│
  │                              │  3. 用户点"同意授权"      │
  │  4. GitHub 回调你的网站       │                         │
  │ ←────────────────────────────│                         │
  │  带上授权码(code)             │                         │
  │                              │                         │
  │  5. 用 code 换 access_token   │                         │
  │ ────────────────────────────→│                         │
  │ ←────────────────────────────│                         │
  │  6. 用 token 拿用户信息        │                         │
  │ ────────────────────────────→│                         │
  │ ←── {name, email, avatar}────│                         │
```

**关键概念**：

| 概念 | 说明 | 类比 |
|------|------|------|
| Resource Owner | 用户本人 | 你 |
| Client | 要访问资源的应用 | 第三方网站 |
| Authorization Server | 授权服务器 | GitHub 的授权页 |
| Resource Server | 资源服务器 | GitHub API |
| Access Token | 访问令牌 | 临时通行证 |

### 5.5 认证方式对比

| 方式 | 安全性 | 复杂度 | 适用场景 |
|------|-------|-------|---------|
| API Key | ⭐⭐ | ⭐ | 公开 API、简单服务间调用 |
| Basic Auth | ⭐⭐ | ⭐ | 内部工具、开发调试（必须 HTTPS） |
| JWT | ⭐⭐⭐⭐ | ⭐⭐⭐ | Web App、移动 App、前后端分离 |
| OAuth 2.0 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 第三方登录、开放平台 |

---

## 六、API 文档

### 6.1 Swagger / OpenAPI

**OpenAPI** = API 描述规范（标准）
**Swagger** = 实现 OpenAPI 的生态工具

一个 API 文档长这样（OpenAPI 3.0 YAML 格式）：

```yaml
openapi: 3.0.0
info:
  title: 博客 API
  version: 1.0.0
paths:
  /api/posts:
    get:
      summary: 获取文章列表
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: 成功
    post:
      summary: 创建文章
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                content:
                  type: string
      responses:
        '201':
          description: 创建成功
```

**有了 OpenAPI 规范，自动生成**：
- 📄 **Swagger UI** — 交互式文档页面（`/api/docs`），可以直接在网页上测试 API
- 📘 **ReDoc** — 更美观的只读文档（`/api/redoc`）
- 🔧 **自动生成客户端代码**（Python / JS / Go / Java ...）

**Python FastAPI 示例**（自动生成 OpenAPI）：
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="博客 API", version="1.0.0")

class PostCreate(BaseModel):
    title: str
    content: str

@app.get("/api/posts", summary="获取文章列表")
async def get_posts(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}

@app.post("/api/posts", summary="创建文章", status_code=201)
async def create_post(post: PostCreate):
    return {"id": 1, "title": post.title}

# 启动后访问 http://localhost:8000/docs 即可看到 Swagger UI
# 访问 http://localhost:8000/redoc 即可看到 ReDoc
```

### 6.2 手写 API 文档

如果没有 Swagger，手写文档至少包含：

```markdown
## GET /api/users/{id}
获取指定用户信息。

### 请求参数
| 参数 | 位置 | 类型 | 必填 | 说明 |
|------|------|------|------|------|
| id | path | integer | 是 | 用户 ID |
| fields | query | string | 否 | 返回字段，逗号分隔 |

### 请求示例
curl -X GET "https://api.example.com/api/users/1?fields=name,email"

### 成功响应 (200)
{
  "code": 200,
  "data": {
    "id": 1,
    "name": "张三",
    "email": "zhangsan@example.com"
  }
}

### 错误响应 (404)
{
  "code": 404,
  "message": "用户不存在"
}
```

---

## 七、调用 API 实战

### 7.1 curl 命令行

**curl 是调试 API 的第一工具**，所有操作系统自带。

```bash
# === GET 请求 ===
curl https://api.github.com/users/panzhaohu666
curl "https://api.example.com/posts?page=1&limit=10"

# === POST 请求（JSON） ===
curl -X POST https://api.example.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"Hello","content":"World"}'

# === 带认证 ===
# Bearer Token
curl https://api.example.com/posts \
  -H "Authorization: Bearer eyJhbGciOi..."

# Basic Auth
curl -u admin:admin123 https://api.example.com/admin

# API Key
curl https://api.example.com/data \
  -H "X-API-Key: abc123def456"

# === 只看响应头 ===
curl -I https://api.example.com/posts

# === 显示请求详情（调试用） ===
curl -v https://api.example.com/posts

# === 下载文件 ===
curl -O https://api.example.com/files/report.pdf

# === 上传文件 ===
curl -X POST https://api.example.com/upload \
  -F "file=@/path/to/image.png"
```

### 7.2 Python 调用

```python
import requests

# ====== GET 请求 ======
response = requests.get("https://api.github.com/users/panzhaohu666")
if response.status_code == 200:
    data = response.json()
    print(f"用户名: {data['login']}")
    print(f"粉丝数: {data['followers']}")
else:
    print(f"请求失败: {response.status_code}")

# ====== POST 请求 ======
response = requests.post(
    "https://api.example.com/posts",
    json={
        "title": "我的第一篇文章",
        "content": "正文内容",
        "published": True
    },
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)
print(response.json())

# ====== 带查询参数 ======
response = requests.get(
    "https://api.example.com/posts",
    params={"page": 1, "limit": 10, "category": "python"}
)
# → 实际请求: GET /posts?page=1&limit=10&category=python

# ====== 上传文件 ======
with open("/path/to/image.png", "rb") as f:
    response = requests.post(
        "https://api.example.com/upload",
        files={"file": f},
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )

# ====== 处理超时 ======
try:
    response = requests.get("https://api.example.com/data", timeout=5)
except requests.Timeout:
    print("请求超时！")
except requests.ConnectionError:
    print("连接失败！")

# ====== 错误处理封装 ======
def api_call(url, method="GET", **kwargs):
    try:
        resp = requests.request(method, url, timeout=10, **kwargs)
        resp.raise_for_status()  # 非 2xx 抛异常
        return resp.json()
    except requests.HTTPError as e:
        print(f"HTTP 错误: {e.response.status_code} - {e.response.text}")
    except requests.RequestException as e:
        print(f"请求失败: {e}")
    return None
```

### 7.3 JavaScript 调用

```javascript
// ====== fetch API（浏览器原生） ======
async function getPosts() {
  try {
    const response = await fetch("https://api.example.com/posts?page=1", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_TOKEN"
      }
    });
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${await response.text()}`);
    }
    
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("请求失败:", error.message);
  }
}

// ====== POST 请求 ======
async function createPost(title, content) {
  const response = await fetch("https://api.example.com/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer YOUR_TOKEN"
    },
    body: JSON.stringify({ title, content })
  });
  return response.json();
}

// ====== axios（更推荐的库） ======
import axios from "axios";

const api = axios.create({
  baseURL: "https://api.example.com",
  timeout: 10000,
  headers: { "Content-Type": "application/json" }
});

// 请求拦截器：自动加 Token
api.interceptors.request.use(config => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// 响应拦截器：统一错误处理
api.interceptors.response.use(
  response => response.data,
  error => {
    if (error.response?.status === 401) {
      // Token 过期，跳转登录
      window.location.href = "/login";
    }
    return Promise.reject(error);
  }
);

// 使用
const posts = await api.get("/posts", { params: { page: 1 } });
const newPost = await api.post("/posts", { title: "Hello", content: "World" });
```

### 7.4 Postman 工具

**Postman** 是图形化 API 测试工具（官网 [postman.com](https://www.postman.com)）。

**核心功能**：
| 功能 | 说明 |
|------|------|
| 发送请求 | 支持所有 HTTP 方法，填 URL + 参数 + Headers + Body |
| 环境变量 | 定义 `{{base_url}}` 等变量，切换环境自动替换 |
| 集合 | 将相关 API 组织在一起，支持导出和团队共享 |
| 自动化测试 | 写脚本验证响应（如 `pm.expect(response.code).to.equal(200)`） |
| Mock Server | 后端没写好时，用模拟数据前端先开发 |

---

## 八、API 设计最佳实践

### 8.1 命名规范

```
✅ GET /api/users/1/posts        ❌ GET /api/getUserPosts?userId=1
✅ POST /api/posts               ❌ POST /api/createPost
✅ DELETE /api/posts/1           ❌ GET /api/posts/1/delete
```

### 8.2 错误处理

```json
// ✅ 好的错误响应：结构化、可解析
{
  "code": 422,
  "message": "参数验证失败",
  "errors": {
    "email": "邮箱格式不正确",
    "age": "年龄必须在 1-150 之间"
  }
}

// ❌ 差的错误响应：无法解析
"Something went wrong"
```

### 8.3 安全

| 原则 | 做法 |
|------|------|
| **HTTPS 强制** | 生产环境禁止 HTTP |
| **输入验证** | 永远不信任客户端数据，服务端必须验证 |
| **速率限制** | 限制每个 IP/用户每分钟请求次数，防滥用 |
| **CORS 控制** | 只允许可信域名跨域访问 |
| **敏感数据** | Token 不放 URL 参数里，用 Header |
| **最小权限** | 只返回用户需要的数据，不暴露内部字段（如密码哈希） |

### 8.4 性能

| 原则 | 做法 |
|------|------|
| **分页** | 列表接口必须分页，默认 `page_size=20` |
| **字段筛选** | 支持 `?fields=id,name`，减少不必要传输 |
| **压缩** | 启用 Gzip/Brotli，JSON 压缩率可达 80% |
| **缓存** | 用 ETag / Cache-Control 头控制缓存 |
| **批量操作** | 提供批量创建/删除，减少请求数 |

### 8.5 版本兼容

```
规则：新增字段 → 不能破坏老客户端
    删除/重命名字段 → 必须升级版本号
    修改字段类型 → 必须升级版本号
```

---

## 九、推荐免费公开 API

**API 黄页**：[github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)

### 入门推荐（免费 + 无需 Key）

| API | 说明 | 示例请求 |
|-----|------|---------|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com) | 假数据 REST API | `GET /posts/1` |
| [Dog API](https://dog.ceo/dog-api/) | 随机狗狗图片 | `GET /api/breeds/image/random` |
| [Cat Facts](https://catfact.ninja/) | 随机猫咪知识 | `GET /fact` |
| [PokéAPI](https://pokeapi.co/) | 宝可梦数据 | `GET /api/v2/pokemon/pikachu` |
| [httpbin](https://httpbin.org/) | HTTP 请求调试 | `GET /get?name=test` |
| [GitHub API](https://api.github.com) | GitHub 公开数据 | `GET /users/panzhaohu666` |

### 进阶（需要注册 API Key，有免费额度）

| API | 说明 | 免费额度 |
|-----|------|---------|
| [OpenWeatherMap](https://openweathermap.org/api) | 天气预报 | 1000 次/天 |
| [OpenAI](https://platform.openai.com/docs) | GPT 大模型 | 注册送 $5 |
| [DeepSeek](https://platform.deepseek.com/api-docs) | 国产大模型 | 注册送额度 |
| [NewsAPI](https://newsapi.org/) | 新闻聚合 | 100 次/天 |
| [ExchangeRate](https://www.exchangerate-api.com/) | 汇率查询 | 1500 次/月 |

### 实战：30 秒调通第一个 API

```bash
# 不需要注册、不需要 Key，直接在终端运行：
curl https://api.github.com/users/panzhaohu666

# 你会看到类似这样的 JSON：
{
  "login": "panzhaohu666",
  "id": ...,
  "name": "...",
  "public_repos": ...,
  "followers": ...
}
```

🎉 恭喜你完成了人生中第一个 API 调用！

---

## 十、常见问题 FAQ

**Q: API 和 SDK 有什么区别？**
A: API 是接口规范（告诉你 URL 和参数），SDK 是对 API 的封装（一行代码搞定）。比如 OpenAI SDK 内部就是调 OpenAI API。API 是菜单，SDK 是打包好的套餐。

**Q: API 一定要用 JSON 吗？**
A: 不是，但 JSON 是主流（90%+）。XML 在老系统常见，Protobuf 在 gRPC 中常见。

**Q: 怎么知道一个网站有没有 API？**
A: 
1. 搜 `网站名 + API` 或 `网站名 + developer`
2. 打开浏览器开发者工具（F12）→ Network 标签 → 刷新页面 → 看有没有返回 JSON 的请求
3. 在 [public-apis](https://github.com/public-apis/public-apis) 里搜

**Q: REST API 和 RESTful API 有区别吗？**
A: REST 是理论规范，RESTful 是符合 REST 规范的 API 实现。日常混用，没人在意。

**Q: POST 和 PUT 到底怎么区分？**
A: POST = 新建（发给集合），PUT = 替换（发给具体资源）。实用主义：大部分项目只用 GET 和 POST。

**Q: 为什么我的 API 请求被拒绝了（CORS 错误）？**
A: 浏览器的安全策略——API 服务器没允许你的域名跨域访问。解决：后端加 CORS 头，或用后端代理转发。

**Q: API 的免费额度用完了怎么办？**
A: 
1. 等明天/下月重置
2. 多注册几个账号（不推荐，违反 ToS）
3. 找替代 API（public-apis 里有海量选择）
4. 付费升级

---

## 十一、GraphQL 入门

> 前面第三章简要提过 GraphQL 的概念。这一章我们深入它——从对比 REST 的痛点开始，到写出一个可运行的 GraphQL 服务。

### 11.1 REST vs GraphQL 深入对比

REST 设计哲学是「一切皆资源，一个 URL 一个资源」。但真实业务中，资源之间是关联的——用户有关联的文章，文章有关联的评论。这带来了 REST 的两个核心痛点：

**痛点一：过度获取（Over-fetching）**

```
# 你只需要用户名和头像，但 REST 返回了全部字段
GET /api/users/1
→ {"id":1, "name":"张三", "email":"z@e.com", "phone":"138...",
   "address":"...", "bio":"...", "avatar":"...", "created_at":"...", ...}
```

**痛点二：获取不足（Under-fetching）**

```
# 你要用户信息 + 他的文章列表 → 需要两次请求
GET /api/users/1           → 拿到用户
GET /api/users/1/posts     → 拿到文章
# 如果要文章下的评论？第三次请求！
GET /api/posts/42/comments
```

**GraphQL 的解决思路：前端声明要什么，后端精确返回。**

```graphql
# 一次请求，精确拿到想要的数据
query {
  user(id: 1) {
    name
    avatar
    posts(limit: 3) {
      title
      comments { content }
    }
  }
}
```

📱 **阅读：架构对比**

| 维度 | REST | GraphQL |
|------|------|---------|
| 端点数量 | 多个（/users, /posts, /comments...） | 1 个（/graphql） |
| 数据控制 | **后端决定**返回哪些字段 | **前端决定**要哪些字段 |
| 版本管理 | 需要 v1/v2 URL | Schema 演进，无需版本号 |
| 缓存策略 | HTTP 缓存天然支持（ETag/Cache-Control） | 需要客户端库（Apollo/Relay） |
| 文件上传 | 原生支持 multipart | 需要额外规范（graphql-upload） |
| 学习曲线 | ⭐ | ⭐⭐⭐ |
| 适合场景 | 简单 CRUD、公开 API | 复杂关联查询、多端（Web+iOS+Android） |

> **一句话判断**：如果你的前端页面需要从 3+ 个 REST 端点聚合数据 → 值得考虑 GraphQL。

### 11.2 Schema 定义与类型系统

GraphQL 的核心是 **Schema**——它定义了「有哪些数据类型、能做什么查询、能做什么修改」。Schema 是服务端和客户端的**共同契约**。

**基础标量类型（Scalar Types）**：

```graphql
type User {
  id: ID!           # ID 类型，! 表示必填（非空）
  name: String!     # 字符串
  age: Int          # 整数（可选）
  score: Float      # 浮点数
  active: Boolean!  # 布尔值
}
```

**自定义类型 + 关联**：

```graphql
type Author {
  id: ID!
  name: String!
  books: [Book!]!   # [Book!]! = 返回必为数组，数组内元素必为 Book 类型
}

type Book {
  id: ID!
  title: String!
  author: Author!   # 关联回 Author
  tags: [String!]   # 字符串数组
}
```

> **类型系统是 GraphQL 最大的价值**——它不仅是文档，还是编译器可以检查的契约。前端写错字段名，IDE 马上标红。

⚠️ **常见误区**：
- `[Book]` vs `[Book!]` vs `[Book!]!` 完全不同
  - `[Book]`：数组和元素都可以为 null
  - `[Book!]`：数组可为 null，但元素不能为 null
  - `[Book!]!`：数组不能为 null，元素也不能为 null（最严格）

### 11.3 Query、Mutation、Subscription

GraphQL 有三种操作类型，分别对应「读」「写」「订阅」：

| 类型 | 对应 REST | 语义 | 特点 |
|------|----------|------|------|
| **Query** | GET | 只读查询 | 可以并行执行 |
| **Mutation** | POST/PUT/DELETE | 修改数据 | **串行执行**（保证顺序） |
| **Subscription** | WebSocket | 实时数据推送 | 长连接，服务端主动推送 |

```graphql
# Query —— 查询（只读）
query GetBookAndAuthor {
  book(id: 1) { title }
  author(id: 2) { name books { title } }
}

# Mutation —— 修改（写操作）
mutation CreateBook {
  createBook(title: "GraphQL 实战", authorId: 1) {
    id
    title
    createdAt
  }
}

# Subscription —— 订阅（实时推送）
subscription OnBookAdded {
  bookAdded {
    id
    title
  }
}
```

> **关键区别**：Query 的多个字段会并行请求（性能好），Mutation 的多个字段会**从上到下串行**执行（避免数据不一致）。

### 11.4 Python Strawberry 实战

> 💻 **动手：用 Strawberry 搭建一个 GraphQL 图书服务**

📱 **阅读**：Strawberry 是目前最推荐的 Python GraphQL 库，使用 Python 类型注解定义 Schema，与 FastAPI 无缝集成。

```bash
pip install 'strawberry-graphql[fastapi]' uvicorn
```

**完整服务端 `graphql_server.py`**：

```python
"""
GraphQL 图书管理服务 —— 使用 Strawberry + FastAPI
启动：python graphql_server.py
访问：http://localhost:8000/graphql （GraphiQL 交互式查询界面）
"""
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
from fastapi import FastAPI
from typing import Optional

# ========== 第一步：定义数据类型（Schema Types） ==========

@strawberry.type
class Author:
    id: int
    name: str

@strawberry.type
class Book:
    id: int
    title: str
    year: int
    author: Author  # 嵌套类型——GraphQL 的核心能力

# ========== 第二步：模拟数据 ==========

authors_db = {
    1: {"id": 1, "name": "Eric Matthes"},
    2: {"id": 2, "name": "Luciano Ramalho"},
}

books_db = {
    1: {"id": 1, "title": "Python 编程：从入门到实践", "year": 2023, "author_id": 1},
    2: {"id": 2, "title": "流畅的 Python", "year": 2022, "author_id": 2},
    3: {"id": 3, "title": "Python 速成", "year": 2025, "author_id": 1},
}

# ========== 第三步：定义查询（Query） ==========

@strawberry.type
class Query:
    @strawberry.field(description="获取所有图书")
    def books(self) -> list[Book]:
        return [
            Book(id=b["id"], title=b["title"], year=b["year"],
                 author=Author(**authors_db[b["author_id"]]))
            for b in books_db.values()
        ]

    @strawberry.field(description="根据 ID 获取图书")
    def book(self, id: int) -> Optional[Book]:
        b = books_db.get(id)
        if b is None:
            return None
        return Book(id=b["id"], title=b["title"], year=b["year"],
                    author=Author(**authors_db[b["author_id"]]))

    @strawberry.field(description="获取所有作者")
    def authors(self) -> list[Author]:
        return [Author(**a) for a in authors_db.values()]

# ========== 第四步：定义变更（Mutation） ==========

@strawberry.type
class Mutation:
    @strawberry.mutation(description="创建新图书")
    def create_book(self, title: str, author_id: int, year: int) -> Book:
        new_id = max(books_db.keys()) + 1
        books_db[new_id] = {"id": new_id, "title": title,
                            "year": year, "author_id": author_id}
        author = Author(**authors_db[author_id])
        return Book(id=new_id, title=title, year=year, author=author)

# ========== 第五步：组装 Schema 并挂载到 FastAPI ==========

schema = strawberry.Schema(query=Query, mutation=Mutation)
app = FastAPI(title="GraphQL 图书管理")
app.include_router(GraphQLRouter(schema, path="/graphql"), prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**前端查询示例（在 GraphiQL 界面中粘贴执行）**：

```graphql
# 查询：只拿书名和作者名
query {
  books {
    title
    year
    author { name }
  }
}

# 查询：按 ID 拿一本书
query {
  book(id: 1) { title author { name } }
}

# 变更：创建新书
mutation {
  createBook(title: "深入理解计算机系统", authorId: 2, year: 2016) {
    id
    title
  }
}
```

**Python 客户端调用**：

```python
# 用 requests 发 GraphQL 请求（所有请求都发到同一个 /graphql 端点）
import requests

url = "http://localhost:8000/graphql"

# 查询图书
query = """
query {
  books { id title year author { name } }
}
"""
resp = requests.post(url, json={"query": query})
print(resp.json())

# 创建图书
mutation = """
mutation {
  createBook(title: "算法导论", authorId: 1, year: 2022) { id title }
}
"""
resp = requests.post(url, json={"query": mutation})
print(resp.json())
```

> 🎉 现在你有了一个同时支持精确查询和修改的 GraphQL 服务！所有请求都发到 `/graphql` 这一个端点。

### 11.5 N+1 问题与 DataLoader

📱 **阅读：N+1 是 GraphQL 最常见的性能陷阱**

**问题场景**：查询 100 本图书，每本图书需要查一次作者。

```
查询: { books { title author { name } } }

执行过程（没有 DataLoader）：
1. SELECT * FROM books                      → 1 次查询，返回 100 本
2. SELECT * FROM authors WHERE id = 1       → 第 1 本书的作者
3. SELECT * FROM authors WHERE id = 2       → 第 2 本书的作者
   ...
101. SELECT * FROM authors WHERE id = ...    → 第 100 本书的作者

总计：1 + 100 = 101 次数据库查询！
```

这就是 N+1 问题：1 次主查询 + N 次关联查询。100 本书 → 101 次查询。

💻 **动手：用 DataLoader 将 N+1 变成 2 次查询**

DataLoader 的核心思想：**收集一批 ID，合并成一条 `WHERE id IN (...)` 查询**。

```python
"""
DataLoader 解决 N+1 问题
pip install strawberry-graphql[fastapi] uvicorn
"""
from strawberry.dataloader import DataLoader
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info
import strawberry
from fastapi import FastAPI
from typing import Optional

# ========== 模拟数据库查询函数 ==========

async def load_authors(keys: list[int]) -> list[Optional[dict]]:
    """批量加载作者——只查一次数据库"""
    print(f"  🔍 批量查询作者: IDs={keys}")  # 你会看到只打印一次！
    result = {k: authors_db.get(k) for k in keys}
    return [result.get(k) for k in keys]

async def load_books(keys: list[int]) -> list[Optional[dict]]:
    """批量加载图书"""
    print(f"  🔍 批量查询图书: IDs={keys}")
    result = {k: books_db.get(k) for k in keys}
    return [result.get(k) for k in keys]

# ========== 数据 ==========

authors_db = {
    1: {"id": 1, "name": "Eric Matthes"},
    2: {"id": 2, "name": "Luciano Ramalho"},
    3: {"id": 3, "name": "Robert C. Martin"},
}

books_db = {i: {"id": i, "title": f"图书 {i}", "year": 2020 + i,
                "author_id": (i % 3) + 1} for i in range(1, 51)}

# ========== Strawberry 类型（使用 DataLoader） ==========

@strawberry.type
class Author:
    id: int
    name: str

@strawberry.type
class Book:
    id: int
    title: str
    year: int

    @strawberry.field
    async def author(self, info: Info) -> Author:
        """通过 DataLoader 加载作者——自动批量合并"""
        author = await info.context["author_loader"].load(
            books_db[self.id]["author_id"]
        )
        return Author(id=author["id"], name=author["name"])

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(id=b["id"], title=b["title"], year=b["year"])
            for b in books_db.values()
        ]

# ========== 组装应用 ==========

schema = strawberry.Schema(query=Query)

async def get_context():
    return {
        "author_loader": DataLoader(load_fn=load_authors),
        "book_loader": DataLoader(load_fn=load_books),
    }

app = FastAPI()
app.include_router(
    GraphQLRouter(schema, path="/graphql", context_getter=get_context),
    prefix="/graphql",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**验证效果**：在 GraphiQL 中执行：
```graphql
query {
  books { title author { name } }
}
```
查看终端输出——只会看到 **1 次** `批量查询作者`，而不是 50 次！

```
  🔍 批量查询作者: IDs=[1, 2, 3, 1, 2, 3, ...]  ← 只打印一次！
```

> **DataLoader 做了什么**：它把一帧事件循环内所有 `.load()` 调用收集起来，去重后一次性查询，结果再分发回去。50 本书 → 2 次查询（1 次 books + 1 次 batched authors）。

### 总结

| 概念 | 一句话 |
|------|--------|
| GraphQL 本质 | 前端声明要什么，后端精确返回——一个端点搞定所有 |
| Schema | 类型契约，编译时可检查，IDE 友好 |
| Query/Mutation/Subscription | 读 / 写 / 实时推送 |
| N+1 问题 | GraphQL 最常见的性能陷阱——1 次主查询 + N 次关联查询 |
| DataLoader | 批量合并查询，把 N+1 变成 2 |

> **选型建议**：简单 CRUD → REST 足够。复杂关联查询 + 多端（Web/App） → 考虑 GraphQL。如果团队只有 2 个人 → 先用 REST，别增加复杂度。

---

## 十二、gRPC 与 Protobuf

### 12.1 gRPC 核心概念

📱 **阅读**

gRPC（Google Remote Procedure Call）是 Google 开源的高性能 RPC 框架。它的核心思想是：**调用远程服务像调用本地函数一样**。

```
┌──────────┐         ┌──────────────────┐         ┌──────────┐
│ 客户端    │ ────→  │  gRPC Stub       │ ────→  │ 服务端    │
│ stub =    │         │  (自动生成代码)    │         │ 函数实现  │
│ Greeter() │ ←────  │                  │ ←────  │          │
└──────────┘         └──────────────────┘         └──────────┘
        stub.SayHello("world")        →         def SayHello(name):
          就像调用本地函数                          return f"Hello {name}"
```

**gRPC 四大核心优势**：

| 特性 | 说明 | 对比 REST |
|------|------|----------|
| **Protobuf 序列化** | 二进制格式，体积比 JSON 小 3-10 倍 | JSON 是文本，冗余大 |
| **HTTP/2 多路复用** | 一个 TCP 连接承载多个请求/响应 | HTTP/1.1 每个请求一个连接 |
| **强类型契约** | `.proto` 文件定义接口，自动生成客户端/服务端代码 | REST 靠文档约定 |
| **四种通信模式** | 一元、服务端流、客户端流、双向流 | REST 只有请求-响应 |

**四种通信模式**：

```
一元 RPC：客户端发一个请求，服务端回一个响应
   Client ──req──→ Server
   Client ←─resp── Server

服务端流式：客户端发一个请求，服务端持续推送多条响应
   Client ──req──→ Server
   Client ←─r1──  Server
   Client ←─r2──  Server
   Client ←─r3──  Server

客户端流式：客户端持续发送多条请求，服务端最后回一个响应
   Client ──r1──→ Server
   Client ──r2──→ Server
   Client ──r3──→ Server
   Client ←─resp── Server

双向流式：双方同时发送和接收（聊天、实时协作）
   Client ⇄⇄⇄⇄⇄⇄⇄ Server
```

### 12.2 Protobuf 编写

> 📱 阅读：`.proto` 文件是 gRPC 的「接口定义语言（IDL）」，写好一份 `.proto`，gRPC 工具链自动生成各语言的客户端和服务端代码。

**Protobuf 基础语法**：

```protobuf
syntax = "proto3";  // 使用 proto3 版本（推荐）

// 定义消息（Message）——相当于 struct / 数据类
message Book {
  int32 id = 1;         // = 后面的数字是「字段编号」，不是默认值！
  string title = 2;     // 编号一旦分配就不能改变（用于二进制编码）
  string author = 3;
  int32 year = 4;
  optional int32 pages = 5;  // proto3 中可选字段
}

message GetBookRequest {
  int32 book_id = 1;
}

message ListBooksResponse {
  repeated Book books = 1;   // repeated = 数组
  int32 total = 2;
}
```

**⚠️ 常见误区：字段编号不是默认值！**

```protobuf
int32 id = 1;   // ← 这个 1 不是 id 的默认值，是「字段在二进制中的编号」
string name = 2; // ← 编号 2
// 编号 1-15 占用 1 字节，16-2047 占用 2 字节。高频字段用 1-15。
```

**Protobuf 类型映射表**：

| Protobuf | Python | 说明 |
|----------|--------|------|
| `int32` | `int` | 32 位整数 |
| `int64` | `int` | 64 位整数 |
| `float` / `double` | `float` | 浮点数 |
| `string` | `str` | UTF-8 字符串 |
| `bool` | `bool` | 布尔值 |
| `bytes` | `bytes` | 二进制数据 |
| `repeated T` | `list[T]` | 数组 |
| `map<K,V>` | `dict` | 字典 |

### 12.3 Python gRPC 完整示例

💻 **动手：构建一个完整的 gRPC 图书服务**

```bash
pip install grpcio grpcio-tools
```

**第 1 步：创建 `bookstore.proto`**

```protobuf
syntax = "proto3";

package bookstore;

// 图书消息
message Book {
  int32 id = 1;
  string title = 2;
  string author = 3;
  int32 year = 4;
}

// 请求：按 ID 查询
message GetBookRequest {
  int32 book_id = 1;
}

// 请求：创建图书
message CreateBookRequest {
  string title = 1;
  string author = 2;
  int32 year = 3;
}

// 响应：图书列表
message ListBooksResponse {
  repeated Book books = 1;
  int32 total = 2;
}

// 空请求/响应
message Empty {}

// 服务定义——这就是 API 契约
service BookService {
  rpc GetBook(GetBookRequest) returns (Book);
  rpc ListBooks(Empty) returns (ListBooksResponse);
  rpc CreateBook(CreateBookRequest) returns (Book);
  rpc DeleteBook(GetBookRequest) returns (Empty);
}
```

**第 2 步：生成 Python 代码**

```bash
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  bookstore.proto
# 生成 bookstore_pb2.py（消息类）和 bookstore_pb2_grpc.py（服务类）
```

**第 3 步：服务端 `grpc_server.py`**

```python
"""gRPC 图书管理服务端"""
from concurrent import futures
import grpc
import bookstore_pb2
import bookstore_pb2_grpc

class BookService(bookstore_pb2_grpc.BookServiceServicer):
    """实现 .proto 中定义的 BookService"""

    def __init__(self):
        self.books = {
            1: bookstore_pb2.Book(id=1, title="Python编程", author="Eric", year=2023),
            2: bookstore_pb2.Book(id=2, title="流畅的Python", author="Luciano", year=2022),
        }
        self.next_id = 3

    def GetBook(self, request, context):
        """一元 RPC：获取单本图书"""
        book = self.books.get(request.book_id)
        if book is None:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"图书 #{request.book_id} 不存在")
            return bookstore_pb2.Book()
        return book

    def ListBooks(self, request, context):
        """一元 RPC：获取所有图书"""
        return bookstore_pb2.ListBooksResponse(
            books=list(self.books.values()),
            total=len(self.books),
        )

    def CreateBook(self, request, context):
        """一元 RPC：创建图书"""
        book = bookstore_pb2.Book(
            id=self.next_id, title=request.title,
            author=request.author, year=request.year,
        )
        self.books[self.next_id] = book
        self.next_id += 1
        return book

    def DeleteBook(self, request, context):
        """一元 RPC：删除图书"""
        if request.book_id in self.books:
            del self.books[request.book_id]
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
        return bookstore_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bookstore_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("🚀 gRPC 服务启动在 localhost:50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
```

**第 4 步：客户端 `grpc_client.py`**

```python
"""gRPC 图书管理客户端"""
import grpc
import bookstore_pb2
import bookstore_pb2_grpc

def main():
    # 建立连接（不加密，仅演示用）
    channel = grpc.insecure_channel("localhost:50051")
    stub = bookstore_pb2_grpc.BookServiceStub(channel)

    # 1. 列出所有图书
    print("📚 所有图书：")
    response = stub.ListBooks(bookstore_pb2.Empty())
    for book in response.books:
        print(f"  [{book.id}] {book.title} — {book.author} ({book.year})")

    # 2. 获取单本图书
    print("\n🔍 获取图书 #1：")
    book = stub.GetBook(bookstore_pb2.GetBookRequest(book_id=1))
    print(f"  {book.title} — {book.author}")

    # 3. 创建图书
    print("\n✏️ 创建新书：")
    new_book = stub.CreateBook(bookstore_pb2.CreateBookRequest(
        title="算法导论", author="Cormen", year=2022
    ))
    print(f"  创建成功: [{new_book.id}] {new_book.title}")

    # 4. 错误处理：查询不存在的书
    print("\n❌ 查询不存在的书：")
    try:
        stub.GetBook(bookstore_pb2.GetBookRequest(book_id=999))
    except grpc.RpcError as e:
        print(f"  错误码: {e.code()}, 详情: {e.details()}")

if __name__ == "__main__":
    main()
```

**第 5 步：运行**

```bash
# 终端 1：启动服务端
python grpc_server.py

# 终端 2：运行客户端
python grpc_client.py
```

### 12.4 gRPC vs REST 选型决策树

📱 **阅读：一句话决策**

```
你要做什么？
│
├─ 对外公开 API（第三方调用）         → REST（生态成熟，curl 可调试）
├─ 微服务内部通信（你的服务调你的服务） → gRPC（性能高，强类型）
├─ 浏览器直接调用                     → REST 或 gRPC-Web
├─ 移动 App 调用                      → 都可以，GraphQL 也可能是好选择
├─ 需要实时流式数据                    → gRPC（原生支持 streaming）
└─ 团队只有后端，前端外包             → REST（前端更熟悉）
```

| 场景 | 推荐 | 原因 |
|------|------|------|
| 公开 API（类似 GitHub API） | REST | 生态成熟，curl 能调试，文档好写 |
| 微服务间高频调用 | gRPC | 二进制序列化快，HTTP/2 多路复用 |
| 移动 App 后端 | GraphQL 或 REST | 看数据复杂度 |
| IoT / 嵌入式设备 | gRPC | Protobuf 体积极小，省带宽 |
| 实时推送（股票行情） | gRPC streaming 或 WebSocket | |
| 团队刚接触微服务 | REST | 降低学习成本 |

### 总结

| 概念 | 一句话 |
|------|--------|
| gRPC 本质 | 用 Protobuf 定义接口，自动生成代码，像调本地函数一样调远程服务 |
| Protobuf | 二进制序列化格式，体积比 JSON 小 3-10 倍 |
| .proto 文件 | 接口契约——写好一份，自动生成所有语言的客户端/服务端 |
| HTTP/2 | gRPC 的传输层——多路复用、头部压缩、服务端推送 |
| 4 种通信模式 | 一元 / 服务端流 / 客户端流 / 双向流 |

---

## 十三、WebSocket 实时通信

### 13.1 WebSocket 握手过程

📱 **阅读：从 HTTP 升级到 WebSocket**

WebSocket 和普通 HTTP 的关键区别：HTTP 是「请求-响应」模式（客户端问，服务端答）；WebSocket 是「全双工」模式（双方随时可以发消息）。

**握手过程（WebSocket 协议升级）**：

```
客户端                                    服务端
  │                                          │
  │  ① 客户端发起 HTTP 请求（要求升级）        │
  │ ──────────────────────────────────────→  │
  │  GET /chat HTTP/1.1                      │
  │  Host: example.com                       │
  │  Upgrade: websocket          ← 关键！     │
  │  Connection: Upgrade          ← 关键！     │
  │  Sec-WebSocket-Key: dGhlIHNhbXBsZQ==     │  随机密钥
  │  Sec-WebSocket-Version: 13               │
  │                                          │
  │  ② 服务端同意升级                          │
  │ ←──────────────────────────────────────  │
  │  HTTP/1.1 101 Switching Protocols        │  101 = 协议切换
  │  Upgrade: websocket                      │
  │  Connection: Upgrade                     │
  │  Sec-WebSocket-Accept: s3pPLMBi...       │  对 Key 的签名
  │                                          │
  │  ③ TCP 连接保持，双方开始双向通信！        │
  │ ⇄══════════════════════════════════════⇄ │
  │     帧（Frame）通信，不再走 HTTP 格式        │
```

> **核心理解**：WebSocket 借 HTTP 完成「握手」，之后降级为 TCP 长连接，用自己的一套帧格式通信。这就是为什么它比 HTTP 轮询高效——不用每次重建连接、不用每次带 HTTP 头。

**WebSocket vs HTTP 轮询 vs SSE**：

| | HTTP 短轮询 | HTTP 长轮询 | SSE | WebSocket |
|---|-----------|-----------|-----|-----------|
| 方向 | 客户端→服务端 | 客户端→服务端 | 服务端→客户端 | 双向 |
| 连接 | 每次新建 | 每次新建 | 一条长连接 | 一条长连接 |
| 效率 | 最低 | 低 | 中 | 最高 |
| 浏览器支持 | 所有 | 所有 | 大多数 | 所有现代 |
| 适用场景 | 低频查询 | 准实时通知 | 单向推送（新闻） | 聊天/协作/游戏 |

### 13.2 FastAPI WebSocket 聊天室

💻 **动手：用 FastAPI 构建一个多人在线聊天室**

```bash
pip install fastapi uvicorn websockets
```

**完整服务端 `chat_server.py`**：

```python
"""
WebSocket 聊天室服务端
启动：python chat_server.py
前端：打开浏览器访问 http://localhost:8000
"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import list

app = FastAPI(title="WebSocket 聊天室")

# 维护所有在线连接
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str, sender: WebSocket):
        """向所有其他人广播消息"""
        for connection in self.active_connections:
            if connection != sender:
                await connection.send_text(message)

manager = ConnectionManager()

# ========== HTML 聊天界面 ==========

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>WebSocket 聊天室</title>
    <style>
        body { max-width:600px; margin:50px auto; font-family:sans-serif; }
        #messages { border:1px solid #ccc; height:400px; overflow-y:auto;
                    padding:10px; margin-bottom:10px; background:#f9f9f9; }
        #messages p { margin:5px 0; padding:5px; border-radius:4px; }
        .system { color:#888; font-size:0.85em; text-align:center; }
        .message { background:#e3f2fd; }
        input { width:78%; padding:10px; font-size:14px; }
        button { width:18%; padding:10px; font-size:14px; cursor:pointer; }
    </style>
</head>
<body>
    <h2>💬 WebSocket 聊天室</h2>
    <div id="messages"></div>
    <input id="msgInput" placeholder="输入消息..." autofocus>
    <button onclick="send()">发送</button>

    <script>
        const ws = new WebSocket(`ws://${location.host}/ws`);
        const messages = document.getElementById("messages");
        const input = document.getElementById("msgInput");

        ws.onopen = () => addMsg("✅ 已连接到聊天室", "system");
        ws.onclose = () => addMsg("❌ 连接已断开", "system");
        ws.onmessage = (e) => addMsg(e.data, "message");

        function addMsg(text, cls) {
            const p = document.createElement("p");
            p.className = cls;
            p.textContent = text;
            messages.appendChild(p);
            messages.scrollTop = messages.scrollHeight;
        }

        function send() {
            const text = input.value.trim();
            if (text) { ws.send(text); addMsg("我: " + text, "message"); input.value = ""; }
        }
        input.addEventListener("keypress", (e) => { if (e.key === "Enter") send(); });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get():
    return HTML

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    await manager.broadcast("👋 有人加入了聊天室", websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("👋 有人离开了聊天室", websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

> 🎉 启动后在**两个浏览器标签页**中打开 `http://localhost:8000`，体验实时多人聊天！

### 13.3 Socket.IO vs 原生 WebSocket

📱 **阅读：什么时候用 Socket.IO？**

| | 原生 WebSocket | Socket.IO |
|---|--------------|-----------|
| 底层协议 | WebSocket (RFC 6455) | 先尝试 WebSocket，不行降级到 HTTP 长轮询 |
| 自动重连 | ❌ 需自己实现 | ✅ 内置 |
| 房间/广播 | ❌ 需自己实现 | ✅ 内置 `io.to("room").emit()` |
| 心跳检测 | ❌ 需自己实现 ping/pong | ✅ 自动 |
| 消息确认 | ❌ 无 | ✅ ACK 回调 |
| 负载 | 轻量 | 较重（额外协议层） |
| 浏览器兼容 | 现代浏览器 | IE9+（降级到轮询） |

> **一句话建议**：如果是内部系统或现代浏览器 → 原生 WebSocket 够了。如果是对外的 SaaS 产品、需要兼容老浏览器、需要自动重连 → 用 Socket.IO。

### 13.4 心跳与重连策略

💻 **动手：生产级 WebSocket 必须处理的三个问题**

⚠️ **常见误区**：很多 WebSocket 连接莫名其妙断开（Nginx 超时、网络切换、防火墙），但代码里根本没处理。

**心跳机制（Ping/Pong）**：

```python
# 服务端：定期 ping，检测死连接
import asyncio

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # 启动心跳任务
    async def heartbeat():
        while True:
            try:
                await asyncio.sleep(30)  # 每 30 秒
                await websocket.send_json({"type": "ping"})
            except Exception:
                break
    asyncio.create_task(heartbeat())
    try:
        while True:
            data = await websocket.receive_text()
            # 处理消息...
    except WebSocketDisconnect:
        print("客户端断开")
```

**前端重连策略（指数退避）**：

```javascript
// 前端自动重连，等待时间逐渐增加
function createWebSocket(url) {
    let retries = 0;
    const maxRetries = 10;

    function connect() {
        const ws = new WebSocket(url);

        ws.onopen = () => {
            console.log("✅ 已连接");
            retries = 0;  // 重置
        };

        ws.onclose = () => {
            if (retries < maxRetries) {
                const delay = Math.min(1000 * Math.pow(2, retries), 30000);
                // 1s → 2s → 4s → 8s → 16s → 30s → 30s ...
                console.log(`❌ 断开，${delay/1000}s 后重连...`);
                setTimeout(connect, delay);
                retries++;
            } else {
                console.log("达到最大重试次数，停止重连");
            }
        };

        ws.onmessage = (e) => {
            const msg = JSON.parse(e.data);
            if (msg.type === "ping") {
                ws.send(JSON.stringify({ type: "pong" }));
                return;
            }
            // 处理业务消息...
        };

        return ws;
    }

    return connect();
}

const ws = createWebSocket("ws://localhost:8000/ws");
```

> **生产环境 Checklist**：
> - [x] 心跳检测（30 秒 ping/pong）
> - [x] 自动重连（指数退避，最大 30 秒）
> - [x] 消息序号/去重（防止重连后收到重复消息）
> - [x] 连接状态管理（connecting / connected / disconnected）

### 总结

| 概念 | 一句话 |
|------|--------|
| WebSocket 握手机制 | 借 HTTP Upgrade 完成握手，降级为 TCP 长连接双向通信 |
| 全双工 vs 半双工 | WebSocket 双方同时发消息；HTTP 只能客户端先问 |
| FastAPI WebSocket | `@app.websocket("/ws")` + `await ws.receive_text()` |
| 心跳 | 定期 ping/pong，检测死连接，防止被代理超时断开 |
| 重连 | 指数退避重连，避免服务端被打垮 |

---

## 十四、API 版本管理策略

### 14.1 三种版本方式详解

📱 **阅读：API 版本管理是「兼容的艺术」**

API 一定会变——加字段、改格式、删旧接口。版本管理的目标是：**老客户端不升级也能继续用，新客户端享受新功能**。

**方式一：URL 路径版本（最推荐）**

```bash
GET /api/v1/books       # 版本 1
GET /api/v2/books       # 版本 2
POST /api/v2/books      # 版本 2 的创建接口
```

✅ 直观，URL 一眼看出版本 | ✅ 方便 Nginx/CDN 按版本路由 | ✅ 最常用（Stripe、GitHub、Twilio）

**方式二：请求头版本**

```bash
GET /api/books
Accept-Version: v2
# 或
Accept: application/vnd.myapp.v2+json
```

✅ URL 干净 | ❌ 调试不便（curl 得加 -H） | ❌ 浏览器直接访问看不出版本

**方式三：查询参数版本**

```bash
GET /api/books?version=2
```

✅ 实现简单 | ❌ 容易被忽略 | ❌ URL 变脏 | ❌ 缓存键变复杂

**三选一建议**：

```
你是公开 API（类似 GitHub API）？ → URL 路径（/v1/）
你是内部微服务？                   → 请求头（不暴露版本细节）
你是快速原型/临时方案？             → 查询参数（千万别用于生产）
```

### 14.2 弃用策略与迁移指南

📱 **阅读：如何让用户心甘情愿地升级**

**弃用（Deprecation）五步法**：

```
第 1 步：发布新版本（v2），旧版本（v1）保持不变
第 2 步：在 v1 响应头中加入弃用通知
         Sunset: Sat, 31 Dec 2026 23:59:59 GMT
         Deprecation: true
         Link: </api/v2/books>; rel="successor-version"
第 3 步：文档标注 v1 弃用，提供迁移指南
第 4 步：监控 v1 调用量，主动通知还在用 v1 的用户
第 5 步：到了截止日期，关闭 v1（或返回 410 Gone）
```

**FastAPI 实现版本路由**：

```python
from fastapi import FastAPI, APIRouter

app = FastAPI()

# ===== v1 路由 =====
v1 = APIRouter(prefix="/api/v1")

@v1.get("/books")
async def list_books_v1():
    return {"version": "v1", "books": [...], "deprecated": True}

# ===== v2 路由 =====
v2 = APIRouter(prefix="/api/v2")

@v2.get("/books")
async def list_books_v2():
    return {"version": "v2", "books": [...], "pagination": {"cursor": "abc"}}

app.include_router(v1)
app.include_router(v2)
```

**迁移指南模板**（写在文档里）：

```markdown
## 从 v1 迁移到 v2

### 破坏性变更
- `GET /api/v1/users` → `GET /api/v2/users` 响应中 `full_name` 拆分为 `first_name` + `last_name`
- 分页从 `?page=1&limit=10` 改为 `?cursor=xxx&limit=10`

### 迁移步骤
1. v2 已上线，v1 保持可用（截止 2026-12-31）
2. 在请求头中加 `Accept-Version: v2` 测试
3. 确认无误后，切换到 `/api/v2/` 端点
4. 如有问题，临时切回 `/api/v1/`

### 常见问题
Q: 老数据在 v2 中怎么表示？
A: v2 兼容所有 v1 数据格式，`first_name` 会从旧 `full_name` 中提取。
```

⚠️ **常见误区**：

| 误区 | 正确做法 |
|------|---------|
| 「加个字段而已，不需要新版本」 | 新增可选字段不需要新版本；**修改/删除已有字段需要** |
| 「v1 没人用了，直接删掉」 | 永远先通告再删除，至少给 3-6 个月过渡期 |
| 「多版本就是多套代码」 | 可以共享核心逻辑，只在不同路由层做转换 |

### 总结

| 策略 | 推荐度 | 适用 |
|------|-------|------|
| URL 路径 `/v1/` | ⭐⭐⭐⭐⭐ | 公开 API |
| 请求头 `Accept-Version` | ⭐⭐⭐⭐ | 内部微服务 |
| 查询参数 `?version=1` | ⭐⭐ | 仅原型阶段 |
| 版本兼容进化 | 目标 | 不破坏老客户端的前提下渐进改进 |

---

## 十五、API 限流与防护

### 15.1 四种限流算法

📱 **阅读：限流就是「控制每分钟最多几个请求」——但如何精确控制？**

**算法一：固定窗口计数器**

```
窗口：[0秒 ——— 60秒] [60秒 ——— 120秒]
       允许 100 次     允许 100 次

问题：在窗口交界处，可能瞬间涌入 200 次请求！
      第 59 秒 100 次 + 第 60 秒 100 次 = 实际上 1 秒 200 次
```

**算法二：滑动窗口日志**

```
「过去 60 秒内，最多 100 次」
每来一个请求，检查过去 60 秒的请求记录。

优点：精确，无边界问题
缺点：存储开销大（需要记录每个请求的时间戳）
```

**算法三：令牌桶（最常用，推荐）**

```
┌─────────────┐
│ 令牌生成器    │ → 每秒往桶里放 N 个令牌（桶容量上限 M）
└──────┬──────┘
       ↓
┌─────────────┐
│  🎫🎫🎫 桶   │ ← 请求来了拿走一个令牌
│   容量 M     │   没令牌 = 限流！
└─────────────┘

特点：允许突发流量（桶里攒的令牌可以一次性用完）
```

**算法四：漏桶**

```
请求 → [进水口] → ═══════ 桶 ═══════ → [出水口] → 以固定速率处理
                 ↑           恒定速率输出

特点：强制平滑，不允许突发
```

**四种算法对比**：

| 算法 | 精确度 | 实现难度 | 允许突发 | 适用场景 |
|------|-------|---------|---------|---------|
| 固定窗口 | ⭐⭐ | ⭐ | ❌ | 简单场景（不推荐生产） |
| 滑动窗口 | ⭐⭐⭐⭐ | ⭐⭐⭐ | ❌ | 需要精确控制的场景 |
| **令牌桶** | ⭐⭐⭐⭐ | ⭐⭐ | ✅ | **通用推荐** |
| 漏桶 | ⭐⭐⭐ | ⭐⭐ | ❌ | 需要平滑输出的场景 |

### 15.2 Python 实现令牌桶

💻 **动手：从零实现一个令牌桶**

```python
import time
import threading

class TokenBucket:
    """令牌桶限流器"""

    def __init__(self, rate: float, capacity: int):
        """
        rate: 每秒生成令牌数（如 10 = 每秒最多处理 10 个请求）
        capacity: 桶的最大容量（如 20 = 允许最多 20 个突发请求）
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity          # 当前令牌数（初始满桶）
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def _refill(self):
        """补充令牌（按经过的时间计算）"""
        now = time.monotonic()
        elapsed = now - self.last_refill
        new_tokens = elapsed * self.rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill = now

    def consume(self, tokens: int = 1) -> bool:
        """尝试消费 tokens 个令牌，成功返回 True"""
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

# ========== 使用示例 ==========

limiter = TokenBucket(rate=5, capacity=10)  # 每秒 5 个，最多 10 个突发

# 模拟 20 个并发请求
import concurrent.futures

def make_request(i: int):
    if limiter.consume():
        return f"请求 #{i}: ✅ 通过"
    else:
        return f"请求 #{i}: ❌ 被限流"

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(make_request, range(20))
    for r in results:
        print(r)
```

### 15.3 FastAPI 限流中间件

💻 **动手：把令牌桶集成到 FastAPI 中间件**

```python
"""
FastAPI 全局限流中间件
基于 IP 的令牌桶限流，每个 IP 独立计数
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time
from collections import defaultdict

app = FastAPI()

# 每个 IP 一个令牌桶：每秒 10 个请求，最大突发 20 个
RATE = 10
CAPACITY = 20

class IPTokenBucket:
    def __init__(self):
        self.buckets: dict[str, dict] = defaultdict(
            lambda: {"tokens": CAPACITY, "last_refill": time.monotonic()}
        )

    def is_allowed(self, ip: str) -> bool:
        bucket = self.buckets[ip]
        now = time.monotonic()
        elapsed = now - bucket["last_refill"]
        bucket["tokens"] = min(CAPACITY, bucket["tokens"] + elapsed * RATE)
        bucket["last_refill"] = now

        if bucket["tokens"] >= 1:
            bucket["tokens"] -= 1
            return True
        return False

rate_limiter = IPTokenBucket()

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    """全局限流中间件——在每个请求处理前检查"""
    client_ip = request.client.host if request.client else "unknown"

    if not rate_limiter.is_allowed(client_ip):
        return JSONResponse(
            status_code=429,
            content={
                "code": 429,
                "message": "请求过于频繁，请稍后再试",
                "retry_after": 1,
            },
            headers={"Retry-After": "1"},
        )

    response = await call_next(request)

    # 在响应头中告诉客户端剩余额度（可选，方便客户端自我调节）
    bucket = rate_limiter.buckets[client_ip]
    response.headers["X-RateLimit-Remaining"] = str(int(bucket["tokens"]))
    response.headers["X-RateLimit-Limit"] = str(RATE)

    return response

# ===== 测试端点 =====

@app.get("/api/test")
async def test():
    return {"message": "请求成功"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**测试限流效果**：

```bash
# 快速连续发送 15 个请求——前 10 个通过，后 5 个被限流
for i in $(seq 1 15); do
  curl -s -o /dev/null -w "请求 $i: HTTP %{http_code}\n" http://localhost:8000/api/test
done
```

### 15.4 认证方案选型

📱 **阅读：限流 + 认证 = API 安全的基础**

**API Key vs OAuth2 选型决策**：

```
你的场景是什么？
│
├─ 服务间调用（后端调后端）
│  └─ API Key（够用，简单）
│
├─ 第三方开发者调用你的 API
│  └─ API Key（GitHub/OpenAI 的做法）
│
├─ 用户登录你的 App，App 调你的 API
│  └─ JWT / OAuth2 Password Grant
│
├─ 「用微信登录」第三方网站
│  └─ OAuth2 Authorization Code Grant
│
└─ 移动 App + Web + 第三方 都要支持
   └─ OAuth2（一种方案覆盖所有场景）
```

**认证实现速查表**：

| 方案 | 实现难度 | 安全等级 | Token 管理 | 典型场景 |
|------|---------|---------|-----------|---------|
| API Key (Header) | ⭐ | ⭐⭐ | 手动生成/撤销 | 公开 API |
| JWT | ⭐⭐ | ⭐⭐⭐⭐ | 自动过期 | Web App |
| OAuth2 + JWT | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Refresh Token 轮换 | 多端产品 |

⚠️ **常见误区**：

| 误区 | 正确做法 |
|------|---------|
| Token 放 URL 里 `?token=xxx` | Token 放 Header `Authorization: Bearer xxx`——URL 会记录在日志里 |
| 永久有效的 Token | 加过期时间，配合 Refresh Token |
| 只用限流不用认证 | 公开接口也要限流；敏感接口限流+认证都要 |
| 所有用户共用同一个限流阈值 | VIP 用户给更高配额（差异化限流） |

### 总结

| 层级 | 措施 |
|------|------|
| 传输层 | HTTPS 强制 |
| 认证层 | API Key / JWT / OAuth2（按场景选） |
| 限流层 | 令牌桶（推荐），按 IP/用户/API Key 限流 |
| 监控层 | 记录被限流的请求，异常飙升时告警 |

---

## 十六、API 测试与监控

### 16.1 pytest + httpx 自动化测试

💻 **动手：为图书管理 API 写自动化测试**

📱 **阅读**：API 测试的核心——不用浏览器，用代码模拟 HTTP 请求，验证响应。

```bash
pip install pytest httpx
```

**测试文件 `test_api.py`**：

```python
"""图书管理 API 自动化测试（基于第三章的 demo/server.py）"""
import pytest
from httpx import AsyncClient, ASGITransport
import sys
sys.path.insert(0, "demo")
from server import app

@pytest.fixture
async def client():
    """创建测试客户端"""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

@pytest.mark.anyio
async def test_root(client):
    """测试：API 首页"""
    resp = await client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "图书管理 API"
    assert "docs" in data

@pytest.mark.anyio
async def test_list_books(client):
    """测试：获取图书列表"""
    resp = await client.get("/api/books")
    assert resp.status_code == 200
    data = resp.json()
    assert data["code"] == 200
    assert data["data"]["total"] >= 4  # 预置了 4 本

@pytest.mark.anyio
async def test_get_book_found(client):
    """测试：获取存在的图书"""
    resp = await client.get("/api/books/1")
    assert resp.status_code == 200
    assert resp.json()["data"]["id"] == 1

@pytest.mark.anyio
async def test_get_book_not_found(client):
    """测试：获取不存在的图书"""
    resp = await client.get("/api/books/99999")
    assert resp.status_code == 404

@pytest.mark.anyio
async def test_create_book(client):
    """测试：创建图书"""
    resp = await client.post("/api/books", json={
        "title": "测试书籍", "author": "测试作者", "year": 2025
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["data"]["title"] == "测试书籍"
    assert data["data"]["id"] is not None

@pytest.mark.anyio
async def test_create_book_invalid(client):
    """测试：创建图书——参数验证"""
    resp = await client.post("/api/books", json={
        "title": "",  # 空标题 ❌
        "author": "作者",
        "year": 1899  # 年份超出范围 ❌
    })
    assert resp.status_code == 422  # 参数验证失败

@pytest.mark.anyio
async def test_search_books(client):
    """测试：搜索图书"""
    resp = await client.get("/api/books", params={"q": "Python"})
    assert resp.status_code == 200
    data = resp.json()
    for book in data["data"]["items"]:
        assert "Python" in book["title"] or "Python" in book["author"]

@pytest.mark.anyio
async def test_delete_book(client):
    """测试：删除图书"""
    # 先创建
    resp = await client.post("/api/books", json={
        "title": "待删除", "author": "作者", "year": 2025
    })
    new_id = resp.json()["data"]["id"]
    # 再删除
    resp = await client.delete(f"/api/books/{new_id}")
    assert resp.status_code == 204
    # 再查应该 404
    resp = await client.get(f"/api/books/{new_id}")
    assert resp.status_code == 404
```

**运行测试**：

```bash
# 运行所有测试
pytest test_api.py -v

# 输出示例：
# test_api.py::test_root PASSED
# test_api.py::test_list_books PASSED
# test_api.py::test_get_book_found PASSED
# test_api.py::test_get_book_not_found PASSED
# test_api.py::test_create_book PASSED
# test_api.py::test_create_book_invalid PASSED
# test_api.py::test_search_books PASSED
# test_api.py::test_delete_book PASSED
# ======== 8 passed ========
```

> **核心思想**：API 测试 = 模拟请求 → 验证状态码 → 验证响应体 → 验证边界情况

### 16.2 Postman Collection 管理

📱 **阅读：Postman Collection 是 API 测试的「基础设施即代码」**

**Collection 结构化建议**：

```
📁 图书管理 API
├── 📁 系统
│   ├── GET  API 首页
│   └── GET  统计信息
├── 📁 图书
│   ├── GET  图书列表
│   ├── GET  图书详情
│   ├── POST 创建图书
│   ├── PUT  更新图书
│   └── DELETE 删除图书
└── 📁 测试流程
    └── 🏃 创建→查询→更新→删除 (E2E)
```

**导出为 JSON（用于 CI/CD）**：

Postman → Collection → Export → Collection v2.1 → 生成 `.json` 文件。然后用 Newman 在命令行运行：

```bash
npm install -g newman
newman run 图书管理API.postman_collection.json \
  --env-var base_url=http://localhost:8000 \
  --reporters cli,json
```

💻 **动手：Postman 环境变量与 Pre-request Script**

```javascript
// Pre-request Script：自动生成测试数据
const randomSuffix = Math.random().toString(36).substring(2, 8);
pm.variables.set("book_title", `测试书籍_${randomSuffix}`);

// Tests 脚本：自动验证响应
pm.test("状态码为 200", () => pm.response.to.have.status(200));
pm.test("响应包含 data", () => {
    pm.expect(pm.response.json()).to.have.property("data");
});
pm.test("响应时间小于 500ms", () => {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

### 16.3 性能测试 k6/locust

📱 **阅读：功能正确 ≠ 性能可用**

**k6 示例 —— 轻量、脚本化、适合 CI**：

```javascript
// k6 压测脚本：test_performance.js
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
    stages: [
        { duration: "30s", target: 10 },   // 30 秒内逐步升至 10 并发
        { duration: "1m",  target: 50 },   // 1 分钟内升至 50 并发
        { duration: "30s", target: 0 },    // 30 秒内降至 0
    ],
    thresholds: {
        http_req_duration: ["p(95)<500"],  // 95% 请求 < 500ms
        http_req_failed: ["rate<0.01"],     // 错误率 < 1%
    },
};

export default function () {
    const resp = http.get("http://localhost:8000/api/books?page=1");
    check(resp, {
        "status is 200": (r) => r.status === 200,
        "response has data": (r) => r.json().hasOwnProperty("data"),
    });
    sleep(1);
}
```

```bash
# 安装 k6：brew install k6 或从 k6.io 下载
k6 run test_performance.js
```

**Locust 示例 —— Python 原生、Web UI 可视化**：

```python
# locustfile.py
from locust import HttpUser, task, between

class BookAPIUser(HttpUser):
    wait_time = between(1, 3)  # 用户等待 1-3 秒再发下一个请求

    @task(3)  # 权重 3——更频繁执行
    def list_books(self):
        self.client.get("/api/books?page=1")

    @task(2)
    def get_book(self):
        self.client.get("/api/books/1")

    @task(1)
    def create_book(self):
        self.client.post("/api/books", json={
            "title": "压测书籍", "author": "Test", "year": 2025
        })
```

```bash
pip install locust
locust -f locustfile.py --host=http://localhost:8000
# 浏览器打开 http://localhost:8089，设置并发数，开始压测！
```

> **k6 vs Locust**：k6 更轻量，适合 CI 集成；Locust 有 Web UI，适合开发时调试。

### 16.4 监控指标体系

📱 **阅读：API 上线后，你需要盯哪些指标？**

**四大黄金指标（RED 方法）**：

| 指标 | 英文 | 计算方式 | 告警阈值示例 |
|------|------|---------|------------|
| **请求速率** | Rate (QPS) | 请求数 / 秒 | > 平时的 3 倍（突发流量） |
| **错误率** | Errors | 错误请求数 / 总请求数 | > 1%（服务异常） |
| **延迟** | Duration | P50 / P95 / P99 响应时间 | P95 > 500ms（性能劣化） |
| **饱和度** | Saturation | CPU / 内存 / 连接数 | CPU > 80% |

**FastAPI + Prometheus 接入示例**：

```python
# pip install prometheus-fastapi-instrumentator
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)
# 访问 /metrics 即可看到 Prometheus 格式的指标
```

**简单自建监控（无需 Prometheus）**：

```python
import time
from collections import defaultdict

class SimpleAPIMonitor:
    """简单 API 监控——统计每个端点的调用次数和耗时"""
    def __init__(self):
        self.stats: dict[str, dict] = defaultdict(
            lambda: {"count": 0, "errors": 0, "total_time": 0.0}
        )

    def record(self, path: str, duration: float, status: int):
        s = self.stats[path]
        s["count"] += 1
        s["total_time"] += duration
        if status >= 400:
            s["errors"] += 1

    def report(self) -> dict:
        return {
            path: {
                "qps": s["count"],
                "avg_ms": round(s["total_time"] / s["count"] * 1000, 1) if s["count"] else 0,
                "error_rate": round(s["errors"] / s["count"] * 100, 1) if s["count"] else 0,
            }
            for path, s in self.stats.items()
        }

monitor = SimpleAPIMonitor()

@app.middleware("http")
async def monitor_middleware(request: Request, call_next):
    start = time.monotonic()
    response = await call_next(request)
    duration = time.monotonic() - start
    monitor.record(request.url.path, duration, response.status_code)
    return response

@app.get("/api/monitor")
async def get_monitor():
    """查看当前监控数据"""
    return {"monitor": monitor.report()}
```

### 总结

| 测试层级 | 工具 | 目的 |
|---------|------|------|
| 单元/集成测试 | pytest + httpx | 保证功能正确 |
| 手动/探索测试 | Postman / curl | 开发调试、手动验证 |
| 性能测试 | k6 / Locust | 知道系统能扛多少并发 |
| 生产监控 | Prometheus + Grafana | 持续观察，及时告警 |

---

## 十七、API 设计最佳实践（进阶）

> 前面第八章讲了基础实践——命名、错误处理、安全、性能。这一章讲进阶话题。

### 17.1 分页策略 cursor vs offset

📱 **阅读：分页的两种哲学**

**Offset 分页（传统方式）**：

```bash
GET /api/books?offset=0&limit=10   # 第 1 页
GET /api/books?offset=10&limit=10  # 第 2 页
GET /api/books?offset=20&limit=10  # 第 3 页
```

✅ 简单，用户能直接跳到第 N 页 | ❌ 翻页时如果数据被插入/删除 → 重复或遗漏

**Cursor 分页（推荐方式）**：

```bash
GET /api/books?cursor=xxx&limit=10
# 响应中返回 next_cursor
{
  "data": {
    "items": [...],
    "next_cursor": "eyJpZCI6MTB9",  // base64 编码的游标
    "has_more": true
  }
}
```

✅ 不受数据插入/删除影响 | ✅ 在大数据集上性能更好 | ❌ 无法跳页

**对比总结**：

| | Offset | Cursor |
|---|--------|--------|
| 实现难度 | ⭐ | ⭐⭐ |
| 跳页 | ✅ 可以 | ❌ 不行 |
| 数据一致性 | ❌ 可能重复/遗漏 | ✅ 稳定 |
| 大数据量性能 | ❌ `OFFSET 100000` 很慢 | ✅ 利用索引 |
| 适合场景 | 数据量小、后台管理 | API 列表、Feed 流、App |

```python
# Cursor 分页的 FastAPI 实现
from base64 import b64encode, b64decode

@app.get("/api/posts")
async def list_posts(cursor: str = None, limit: int = 10):
    # 解码游标
    after_id = int(b64decode(cursor).decode()) if cursor else 0

    posts = db.query.filter(Post.id > after_id).order_by(
        Post.id
    ).limit(limit + 1).all()

    has_more = len(posts) > limit
    items = posts[:limit]

    # 生成下一页游标
    next_cursor = b64encode(str(items[-1].id).encode()).decode() if has_more else None

    return {"items": items, "next_cursor": next_cursor, "has_more": has_more}
```

### 17.2 HATEOAS 超媒体驱动

📱 **阅读：让 API 自己告诉客户端「接下来能做什么」**

HATEOAS（Hypermedia As The Engine Of Application State）是 REST 最容易被忽略的一条原则。核心思想：**API 响应里包含可用的操作链接**。

**普通 API 响应 vs HATEOAS 响应**：

```json
// ❌ 普通响应：客户端需要硬编码 URL
{
  "id": 1,
  "title": "Python 编程",
  "status": "draft"
}
// 客户端：我没法知道这个资源能做什么操作

// ✅ HATEOAS 响应：自带操作链接
{
  "id": 1,
  "title": "Python 编程",
  "status": "draft",
  "_links": {
    "self": { "href": "/api/books/1" },
    "publish": { "href": "/api/books/1/publish", "method": "POST" },
    "delete": { "href": "/api/books/1", "method": "DELETE" },
    "author": { "href": "/api/authors/42" }
  }
}
// 客户端：我知道这本书能发布、能删除、还能看作者
```

💻 **动手：FastAPI 添加 HATEOAS 链接**：

```python
def add_links(book_id: int, status: str) -> dict:
    """为图书资源生成 HATEOAS 链接"""
    links = {"self": {"href": f"/api/books/{book_id}"}}

    if status == "draft":
        links["publish"] = {"href": f"/api/books/{book_id}/publish", "method": "POST"}
        links["delete"] = {"href": f"/api/books/{book_id}", "method": "DELETE"}
    elif status == "published":
        links["archive"] = {"href": f"/api/books/{book_id}/archive", "method": "POST"}

    return links

@app.get("/api/books/{book_id}")
async def get_book(book_id: int):
    book = load_book(book_id)
    return {
        "code": 200,
        "data": {
            **book,
            "_links": add_links(book_id, book["status"]),
        },
    }
```

> **现实检查**：HATEOAS 在理论上很优雅，但业界实际落地率很低——大部分 API 不实现它。知道这个概念，面试可能考，实际项目看情况。

### 17.3 OpenAPI 3.0 规范详解

📱 **阅读：OpenAPI 3.0 是 API 世界的「统一度量衡」**

OpenAPI 3.0 相比 2.0（Swagger）的重大改进：

| 特性 | OpenAPI 2.0 | OpenAPI 3.0 |
|------|-----------|-----------|
| 请求体描述 | `body` 参数 | `requestBody` 独立字段 |
| 多服务器 | ❌ | ✅ `servers` 数组 |
| Cookie 参数 | ❌ | ✅ `in: cookie` |
| 示例 | 单个 `example` | `examples` 复数 + `example` |
| 链接（HATEOAS） | ❌ | ✅ `links` 字段 |
| 回调（Webhook） | ❌ | ✅ `callbacks` 字段 |

**OpenAPI 3.0 核心结构**：

```yaml
openapi: 3.0.3
info:
  title: 图书管理 API
  version: 2.0.0
  description: 这是一个完整的 OpenAPI 3.0 规范示例

servers:                          # 🆕 3.0 新增
  - url: https://api.example.com/v2
    description: 生产环境
  - url: http://localhost:8000
    description: 本地开发

paths:
  /api/books:
    get:
      summary: 获取图书列表
      operationId: listBooks       # 🆕 推荐：唯一标识，方便代码生成
      tags: [图书]
      parameters:
        - name: page
          in: query
          schema: { type: integer, default: 1 }
        - name: q
          in: query
          description: 搜索关键词
          schema: { type: string }
      responses:
        "200":
          description: 成功
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/BookList"  # 引用复用
        "429":
          $ref: "#/components/responses/RateLimited"    # 🆕 引用复用

components:                       # 🆕 统一管理可复用组件
  schemas:
    Book:
      type: object
      required: [id, title]
      properties:
        id: { type: integer }
        title: { type: string, example: "Python 编程" }
        author: { $ref: "#/components/schemas/Author" }
    Author:
      type: object
      properties:
        id: { type: integer }
        name: { type: string }
    BookList:
      type: object
      properties:
        items:
          type: array
          items: { $ref: "#/components/schemas/Book" }
        total: { type: integer }

  responses:                       # 🆕 3.0 支持复用响应
    RateLimited:
      description: 请求频率过高
      content:
        application/json:
          schema:
            type: object
            properties:
              code: { type: integer, example: 429 }
              message: { type: string, example: "请求过于频繁" }

  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:                          # 🆕 全局安全配置
  - BearerAuth: []
```

> **为什么写 OpenAPI 规范？** 一份完整的 openapi.yaml = 文档（Swagger UI） + 客户端代码（自动生成） + Mock Server + 测试基础。一份投入，四份产出。

### 17.4 常见反模式与避坑指南

📱 **阅读：别人踩过的坑，你别再踩**

⚠️ **反模式 1：把 API 当成数据库直接暴露**

```bash
# ❌ 允许客户端写任意 SQL
GET /api/query?sql=SELECT * FROM users WHERE ...

# ❌ 暴露内部 ID 自增规律
GET /api/users/1   # 返回内部自增 ID
# → 攻击者：那我试试 /api/users/2, /api/users/3...

# ✅ 对外用 UUID 或 Hash ID
GET /api/users/a3f2b8c1-...
```

⚠️ **反模式 2：响应格式不统一**

```json
// ❌ 成功时返回不同的结构
GET /api/books  → { "books": [...] }
POST /api/books → { "id": 1, "title": "..." }
// 客户端需要写两套解析代码

// ✅ 统一响应格式（第四章已经强调过）
{ "code": 200, "message": "success", "data": { ... } }
```

⚠️ **反模式 3：同步处理耗时操作**

```python
# ❌ 创建订单时同步发送邮件——用户等 5 秒才收到响应
@app.post("/api/orders")
async def create_order(order: OrderCreate):
    order_id = save_order(order)        # 50ms
    send_email(order.email)             # 5000ms ← 用户卡在这里！
    return {"order_id": order_id}

# ✅ 异步处理：立即返回，后台发邮件
@app.post("/api/orders")
async def create_order(order: OrderCreate, background_tasks: BackgroundTasks):
    order_id = save_order(order)        # 50ms
    background_tasks.add_task(send_email, order.email)
    return {"order_id": order_id}       # 立即返回！
```

⚠️ **反模式 4：响应体过大无分页**

```python
# ❌ 一次返回全部 10 万条数据
GET /api/users

# ✅ 必须分页
GET /api/users?page=1&limit=50  → 最多返回 50 条
```

| 反模式 | 后果 | 快速修复 |
|--------|------|---------|
| 暴露自增 ID | 数据可遍历 | 对外用 UUID |
| 同步耗时操作 | 接口超时 | 异步队列 / BackgroundTasks |
| 无分页返回全量 | OOM 打垮服务 | 强制分页 + 最大 limit |
| 无输入长度限制 | 被灌入巨大请求体 | Pydantic `max_length` |
| 无超时设置 | 连接池耗尽 | `timeout=30` 对一切 HTTP 调用 |
| 硬编码 URL | 换域名全挂 | 用配置文件/环境变量 |

### 总结

> API 设计不是一次性工作——它是随着业务持续演进的。好的设计让演进变得容易，差的设计让每次改动都是灾难。

| 实践 | 一句话 |
|------|--------|
| Cursor 分页 | 大数据量 + 实时数据场景的首选 |
| HATEOAS | REST 的终极形态，知道概念即可，落地看场景 |
| OpenAPI 3.0 | 一份规范 → 文档 + 客户端 + Mock + 测试 |
| 避免反模式 | 大多数 API 事故来自这些看似合理的设计 |

---

> **一份 API 文档就是一份菜单——看懂了就能点菜，不需要进厨房。**

> 下一步推荐：打开 [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts/1)，用 curl 或浏览器直接访问，看返回的 JSON 长什么样。然后自己写一个 Python 脚本试试。
