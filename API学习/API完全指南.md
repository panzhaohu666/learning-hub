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

> **一份 API 文档就是一份菜单——看懂了就能点菜，不需要进厨房。**

> 下一步推荐：打开 [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts/1)，用 curl 或浏览器直接访问，看返回的 JSON 长什么样。然后自己写一个 Python 脚本试试。
