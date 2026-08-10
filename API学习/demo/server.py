"""
一个完整的 API 演示项目 —— 图书管理系统
===========================================
跑起来就能看到 API 的真面目。

启动方式：
  pip install fastapi uvicorn
  python server.py

然后打开浏览器访问：
  http://localhost:8000/docs    ← 交互式 API 文档（可以直接在网页上测试！）
  http://localhost:8000/redoc    ← ReDoc 只读文档
"""

from datetime import datetime
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

# ============================================================================
# 第一步：创建 App（这就是你的 API 服务器）
# ============================================================================
app = FastAPI(
    title="图书管理 API",
    description="一个完整演示：增删改查 + 认证 + 分页 + 错误处理 + Swagger 文档",
    version="1.0.0",
)

# ============================================================================
# 第二步：定义数据结构（Schema / Model）
#    这就是 API 的"菜单"——明确告诉调用方：你给我什么，我给你什么
# ============================================================================

# 请求体：创建/更新图书时客户端发来的数据
class BookCreate(BaseModel):
    """创建图书的请求体"""
    title: str = Field(..., min_length=1, max_length=200, description="书名", examples=["Python 编程：从入门到实践"])
    author: str = Field(..., min_length=1, max_length=100, description="作者", examples=["Eric Matthes"])
    year: int = Field(..., ge=1900, le=2026, description="出版年份", examples=[2023])
    pages: Optional[int] = Field(default=None, ge=1, description="页数（可选）", examples=[456])

class BookUpdate(BaseModel):
    """更新图书的请求体——所有字段可选，只更新你传的"""
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    author: Optional[str] = Field(default=None, min_length=1, max_length=100)
    year: Optional[int] = Field(default=None, ge=1900, le=2026)
    pages: Optional[int] = Field(default=None, ge=1)

# 响应体：API 返回给客户端的数据
class Book(BaseModel):
    """图书的响应体"""
    id: int = Field(..., description="图书 ID（自动生成）")
    title: str
    author: str
    year: int
    pages: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")

# 统一响应格式 —— 所有接口用同一套结构
class ApiResponse(BaseModel):
    """统一响应格式"""
    code: int = 200
    message: str = "success"
    data: Optional[object] = None

class PaginatedResponse(BaseModel):
    """分页列表响应格式"""
    code: int = 200
    message: str = "success"
    data: dict = {}

# ============================================================================
# 第三步：模拟数据库（真实项目中这里是 PostgreSQL/MySQL）
# ============================================================================
books_db: dict[int, dict] = {}   # {1: {...}, 2: {...}}
next_id: int = 1

# 预设几条示例数据
sample_books = [
    {"title": "Python 编程：从入门到实践", "author": "Eric Matthes", "year": 2023, "pages": 456},
    {"title": "深入理解计算机系统", "author": "Randal E. Bryant", "year": 2016, "pages": 1120},
    {"title": "算法导论", "author": "Thomas H. Cormen", "year": 2022, "pages": 1312},
    {"title": "设计模式", "author": "Erich Gamma", "year": 1994, "pages": 395},
]

for book in sample_books:
    books_db[next_id] = {**book, "id": next_id, "created_at": datetime.now()}
    next_id += 1


# ============================================================================
# 第四步：编写 API 端点（Routes）
#    每一个 @app.get / @app.post 等就是一个 API 端点
# ============================================================================

# --------------------------------------------------------------------------
# 4.1 根路径 —— API 的"首页"
# --------------------------------------------------------------------------
@app.get("/", summary="API 首页", tags=["系统"])
async def root():
    """最简单的 API：返回欢迎信息"""
    return {
        "name": "图书管理 API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "图书列表": "GET /api/books",
            "图书详情": "GET /api/books/{id}",
            "创建图书": "POST /api/books",
            "更新图书": "PUT /api/books/{id}",
            "删除图书": "DELETE /api/books/{id}",
            "搜索图书": "GET /api/books/search?q=关键词",
            "统计信息": "GET /api/stats",
        },
    }


# --------------------------------------------------------------------------
# 4.2 GET /api/books —— 获取图书列表（带分页和搜索）
# --------------------------------------------------------------------------
@app.get("/api/books", response_model=PaginatedResponse, summary="获取图书列表", tags=["图书"])
async def list_books(
    page: int = Query(default=1, ge=1, description="页码"),
    page_size: int = Query(default=10, ge=1, le=100, description="每页数量"),
    q: Optional[str] = Query(default=None, description="搜索关键词（匹配书名和作者）"),
    year: Optional[int] = Query(default=None, description="按年份筛选"),
):
    """
    获取图书列表，支持：
    - 分页：?page=1&page_size=10
    - 搜索：?q=Python
    - 筛选：?year=2023
    - 组合：?page=1&page_size=5&q=Python&year=2023
    """
    # 1. 过滤
    results = list(books_db.values())
    if q:
        q_lower = q.lower()
        results = [
            b for b in results
            if q_lower in b["title"].lower() or q_lower in b["author"].lower()
        ]
    if year:
        results = [b for b in results if b["year"] == year]

    # 2. 排序（按 ID 倒序）
    results = sorted(results, key=lambda b: b["id"], reverse=True)

    # 3. 分页
    total = len(results)
    start = (page - 1) * page_size
    end = start + page_size
    page_items = results[start:end]

    return {
        "code": 200,
        "message": "success",
        "data": {
            "items": page_items,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
        },
    }


# --------------------------------------------------------------------------
# 4.3 GET /api/books/{id} —— 获取单本图书详情
# --------------------------------------------------------------------------
@app.get("/api/books/{book_id}", response_model=ApiResponse, summary="获取图书详情", tags=["图书"])
async def get_book(book_id: int):
    """
    根据 ID 获取一本图书的详细信息。
    如果图书不存在，返回 404 错误。
    """
    book = books_db.get(book_id)
    if book is None:
        # 这就是 API 的错误处理方式——返回标准 HTTP 状态码 + 结构化错误信息
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": 404, "message": f"图书 #{book_id} 不存在"},
        )
    return {"code": 200, "message": "success", "data": book}


# --------------------------------------------------------------------------
# 4.4 POST /api/books —— 创建一本新书
# --------------------------------------------------------------------------
@app.post(
    "/api/books",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,  # 201 = 创建成功
    summary="创建图书",
    tags=["图书"],
)
async def create_book(book: BookCreate):
    """
    创建一本新书。请求体示例：
    {
        "title": "流畅的 Python",
        "author": "Luciano Ramalho",
        "year": 2022,
        "pages": 880
    }
    """
    global next_id
    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "pages": book.pages,
        "created_at": datetime.now(),
    }
    books_db[next_id] = new_book
    next_id += 1
    return {"code": 201, "message": "创建成功", "data": new_book}


# --------------------------------------------------------------------------
# 4.5 PUT /api/books/{id} —— 完整更新一本书
# --------------------------------------------------------------------------
@app.put("/api/books/{book_id}", response_model=ApiResponse, summary="更新图书（全量替换）", tags=["图书"])
async def update_book(book_id: int, book: BookCreate):
    """
    PUT 是全量替换——你必须传所有必填字段。
    如果只想改部分字段，用 PATCH（本 demo 未实现）。
    """
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": 404, "message": f"图书 #{book_id} 不存在"},
        )
    updated = {
        "id": book_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "pages": book.pages,
        "created_at": books_db[book_id]["created_at"],  # 保留原创建时间
    }
    books_db[book_id] = updated
    return {"code": 200, "message": "更新成功", "data": updated}


# --------------------------------------------------------------------------
# 4.6 DELETE /api/books/{id} —— 删除一本书
# --------------------------------------------------------------------------
@app.delete(
    "/api/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,  # 204 = 成功但无返回内容
    summary="删除图书",
    tags=["图书"],
)
async def delete_book(book_id: int):
    """删除一本书。成功返回 204 No Content。"""
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": 404, "message": f"图书 #{book_id} 不存在"},
        )
    del books_db[book_id]
    # 204 不返回 body，FastAPI 自动处理


# --------------------------------------------------------------------------
# 4.7 GET /api/stats —— 统计信息
# --------------------------------------------------------------------------
@app.get("/api/stats", response_model=ApiResponse, summary="获取统计信息", tags=["系统"])
async def get_stats():
    """获取图书库的整体统计"""
    books = list(books_db.values())
    authors = set(b["author"] for b in books)
    years = [b["year"] for b in books if b["year"]]

    return {
        "code": 200,
        "message": "success",
        "data": {
            "total_books": len(books),
            "total_authors": len(authors),
            "avg_pages": round(sum(b.get("pages", 0) or 0 for b in books) / len(books), 1) if books else 0,
            "oldest_year": min(years) if years else None,
            "newest_year": max(years) if years else None,
        },
    }


# ============================================================================
# 第五步：启动服务器
# ============================================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
