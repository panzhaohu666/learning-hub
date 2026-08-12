# API 演示项目 —— 图书管理系统

一个 **可运行的、麻雀虽小五脏俱全的 API 示例**，帮你直观理解"API 的代码长什么样"。

## 🚀 30 秒跑起来

```bash
# 1. 安装依赖
pip install fastapi uvicorn

# 2. 启动
python server.py

# 3. 打开浏览器
# → http://localhost:8000/docs   交互式 API 文档（可以直接测试！）
# → http://localhost:8000/redoc  只读 API 文档
```

## 🔍 代码结构速览

`server.py` 只有 **295 行**，按 5 步组织：

| 步骤 | 代码 | 对应现实 |
|------|------|---------|
| **第一步** | `app = FastAPI(...)` | 开一家餐厅 |
| **第二步** | `class BookCreate(BaseModel)` | 制定菜单（定义数据格式） |
| **第三步** | `books_db = {}` | 准备后厨（数据存储） |
| **第四步** | `@app.get(...)` `@app.post(...)` | 安排服务员（API 端点） |
| **第五步** | `uvicorn.run(app)` | 开门营业 |

## 📡 API 端点一览

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/` | API 首页，列出所有端点 |
| `GET` | `/api/books` | 图书列表（支持 `?page=1&q=Python`） |
| `GET` | `/api/books/1` | 图书详情 |
| `POST` | `/api/books` | 创建新书（JSON body） |
| `PUT` | `/api/books/1` | 更新图书（全量替换） |
| `DELETE` | `/api/books/1` | 删除图书 |
| `GET` | `/api/stats` | 统计信息 |

## 🧪 用 curl 测试

```bash
# 查看欢迎页
curl http://localhost:8000/

# 获取图书列表（默认 10 条/页）
curl http://localhost:8000/api/books

# 搜索 + 分页
curl "http://localhost:8000/api/books?q=Python&page=1&page_size=3"

# 获取单本图书
curl http://localhost:8000/api/books/1

# 创建新书
curl -X POST http://localhost:8000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title":"流畅的 Python","author":"Luciano Ramalho","year":2022,"pages":880}'

# 更新图书
curl -X PUT http://localhost:8000/api/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Python 编程（第3版）","author":"Eric Matthes","year":2025}'

# 删除图书
curl -X DELETE http://localhost:8000/api/books/4

# 获取统计
curl http://localhost:8000/api/stats
```

## 🐍 用 Python 调用

```python
import requests

BASE = "http://localhost:8000"

# 获取列表
resp = requests.get(f"{BASE}/api/books", params={"q": "Python", "page": 1})
print(f"找到 {resp.json()['data']['total']} 本相关图书")

# 创建新书
resp = requests.post(f"{BASE}/api/books", json={
    "title": "流畅的 Python",
    "author": "Luciano Ramalho",
    "year": 2022,
    "pages": 880
})
print(f"创建成功: ID={resp.json()['data']['id']}")

# 获取详情
resp = requests.get(f"{BASE}/api/books/1")
print(resp.json()["data"]["title"])

# 统计
stats = requests.get(f"{BASE}/api/stats").json()
print(f"共 {stats['data']['total_books']} 本书, {stats['data']['total_authors']} 位作者")
```

## 📖 读代码时的对照表

帮你理解代码中的关键概念：

| 代码里的名词 | 通俗含义 |
|-------------|---------|
| `@app.get("/api/books")` | "有人访问这个 URL 时，执行我下面这个函数" |
| `book_id: int` | URL 路径参数（`/api/books/1` 中的 `1`） |
| `Query(default=1)` | URL 查询参数（`?page=1` 中的 `page`） |
| `BookCreate` (BaseModel) | "你必须给我这些字段，我会帮你校验格式" |
| `response_model=ApiResponse` | "我返回的数据一定长这样" |
| `HTTPException(status_code=404)` | "出错了！给调用方返回 404" |
| `status_code=201` | "创建成功，标准规定返回 201" |
| `204 No Content` | "删除成功，没什么可返回的" |

## 🎯 这个 demo 演示了哪些关键概念？

- [x] RESTful URL 设计（名词 + 复数）
- [x] GET / POST / PUT / DELETE 全部 HTTP 方法
- [x] 请求体验证（Pydantic 自动校验类型和范围）
- [x] 查询参数（分页 `?page=1&page_size=10`）
- [x] 搜索和筛选（`?q=关键词`）
- [x] 统一响应格式（`{code, message, data}`）
- [x] 错误处理（404 + 结构化错误信息）
- [x] 自动生成 Swagger 文档（`/docs`）
- [x] 无状态（数据在内存中，重启丢失——真实项目用数据库）

## 🏗️ 真实项目 vs 这个 demo

| | 这个 demo | 真实项目（如 personal_blog） |
|---|---|---|
| 数据存储 | Python 字典（重启丢失） | PostgreSQL / MySQL |
| 认证 | 无 | JWT（登录 → Token → 调用） |
| 代码组织 | 单个 server.py | 分 routers/ models/ services/ schemas/ |
| 数据库操作 | 手动 dict 操作 | SQLAlchemy ORM |
| 测试 | 无 | pytest + 集成测试 |
| 部署 | `python server.py` | Docker + Nginx + Gunicorn |

> 这个 demo 帮你理解 API 的**骨架**，真实项目只是在这骨架上加**肌肉**（认证、数据库、测试、部署）。
