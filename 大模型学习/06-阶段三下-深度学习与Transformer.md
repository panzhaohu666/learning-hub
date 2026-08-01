# 阶段三 · 下 · 每日学习指南

阶段三·下 · 每日学习指南
### 深度学习 + NLP + 手写 Transformer（第 12-16 周）★核心中的核心★


说明：这 5 周是整份计划中最重要的部分。
第 15 周（手写 Transformer）是所有知识的中点，
之前一切都在为它打基础，之后一切都在它上面构建。

### 第12周 · 主题：深度学习基础与训练技巧


### 第12周 · 星期一：手写反向传播（纸笔推导 + 代码验证）
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：反向传播 —— 深度学习的核心算法

核心知识点

1. 反向传播的本质

正向：输入 → 计算 → 输出 → 损失
反向：损失 → 逐层计算梯度 → 更新参数

数学工具：链式法则（Chain Rule）

dz/dx = dz/dy × dy/dx

对于多层网络：
Loss → ∂L/∂w₃ → ∂L/∂w₂ → ∂L/∂w₁
从最后一层"反向"传播到第一层。

2. 一个具体例子（2 层 MLP）

x → [Linear + ReLU] → h → [Linear] → ŷ
损失: L = (ŷ - y)²

推导 ∂L/∂w₂（第 2 层的权重梯度）：
① ∂L/∂ŷ = 2(ŷ - y)
② ∂ŷ/∂w₂ = h（因为 ŷ = w₂·h + b₂）
③ ∂L/∂w₂ = ∂L/∂ŷ × ∂ŷ/∂w₂ = 2(ŷ - y) × h

推导 ∂L/∂w₁（第 1 层的权重梯度）：
④ ∂ŷ/∂h = w₂
⑤ ∂h/∂w₁ = x × ReLU'(w₁·x)  （ReLU' = 输入>0时为1，否则为0）
⑥ ∂L/∂w₁ = ∂L/∂ŷ × ∂ŷ/∂h × ∂h/∂w₁
= 2(ŷ - y) × w₂ × x × ReLU'(w₁·x)

3. 关键洞察

链式法则意味着：离输出越远的层，梯度可能越小（梯度消失）
或越大（梯度爆炸）。这是深层网络难训练的根本原因。

- 梯度消失 → 用 ReLU 替代 sigmoid、BatchNorm、残差连接
- 梯度爆炸 → 梯度裁剪（Gradient Clipping）

今日思考题
- 如果网络有 100 层，每层梯度都乘 0.8，第一层的梯度和最后一层的梯度
差多少？0.8^99 ≈ 2.5×10^-10 —— 这就是梯度消失的数学本质。

### 晚上电脑 · 2 小时
任务：用纸笔 + 代码验证一个 2 层 MLP 的反向传播

建文件 backprop_from_scratch.py：

```python
  import torch
  import torch.nn.functional as F
```

# 固定随机种子
torch.manual_seed(42)

# 小规模数据：2层 MLP，从零实现反向传播
n, d_in, d_hidden, d_out = 4, 3, 5, 2
X = torch.randn(n, d_in)
y = torch.randn(n, d_out)

# ----- 参数 -----
w1 = torch.randn(d_in, d_hidden, requires_grad=False) * 0.1
b1 = torch.zeros(d_hidden, requires_grad=False)
w2 = torch.randn(d_hidden, d_out, requires_grad=False) * 0.1
b2 = torch.zeros(d_out, requires_grad=False)

# ====== 前向传播（手动）======
z1 = X @ w1 + b1          # (4, 3) @ (3, 5) = (4, 5)
a1 = F.relu(z1)           # (4, 5)
z2 = a1 @ w2 + b2         # (4, 5) @ (5, 2) = (4, 2)
loss = F.mse_loss(z2, y)

# ====== 反向传播（手动推导 + 代码实现）======

# ① ∂L/∂z2
d_z2 = 2 * (z2 - y) / (n * d_out)  # MSE 对 z2 的梯度
#     = (2/n*d_out) * (z2 - y)

# ② ∂L/∂w2 = a1^T @ d_z2
d_w2 = a1.T @ d_z2  # (5, 4) @ (4, 2) = (5, 2)
d_b2 = d_z2.sum(dim=0)  # (2,)

# ③ ∂L/∂a1 = d_z2 @ w2^T
d_a1 = d_z2 @ w2.T  # (4, 2) @ (2, 5) = (4, 5)

# ④ ∂L/∂z1 = d_a1 * ReLU'(z1)
d_z1 = d_a1 * (z1 > 0).float()  # ReLU 导数：>0 时为 1，否则为 0

# ⑤ ∂L/∂w1 = X^T @ d_z1
d_w1 = X.T @ d_z1  # (3, 4) @ (4, 5) = (3, 5)
d_b1 = d_z1.sum(dim=0)  # (5,)

print("手动计算的梯度:")
print(f"  d_w1 shape: {d_w1.shape}")
print(f"  d_w2 shape: {d_w2.shape}")

# ====== 用 PyTorch Autograd 验证 ======
w1_a = w1.clone().requires_grad_(True)
b1_a = b1.clone().requires_grad_(True)
w2_a = w2.clone().requires_grad_(True)
b2_a = b2.clone().requires_grad_(True)

z1_a = X @ w1_a + b1_a
a1_a = F.relu(z1_a)
z2_a = a1_a @ w2_a + b2_a
loss_a = F.mse_loss(z2_a, y)
loss_a.backward()

# 验证：手动计算 vs Autograd
print(f"\nw1 梯度差异: {(d_w1 - w1_a.grad).abs().max():.10f}")
print(f"w2 梯度差异: {(d_w2 - w2_a.grad).abs().max():.10f}")
print(f"b1 梯度差异: {(d_b1 - b1_a.grad).abs().max():.10f}")
print(f"b2 梯度差异: {(d_b2 - b2_a.grad).abs().max():.10f}")
# 所有差异应接近 0

- [ ] 今日完成检查
- [ ] 2 层 MLP 反向传播手动推导 + 代码实现
- [ ] 手动梯度和 Autograd 一致（差异 ≈ 0）
### 第12周 · 星期二：Dropout + BatchNorm + LayerNorm
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：正则化与归一化

核心知识点

1. Dropout（随机失活）

训练时，每个神经元以概率 p 被"关闭"（输出置为 0）。
每个 batch 关掉的神经元不同 → 相当于每次训练不同的子网络。

为什么有效？
- 防止神经元之间"共谋"（co-adaptation）
- 等同于训练多个子网络并取平均（集成学习的效果）

测试时：不关闭任何神经元，但权重乘以 (1-p) 来补偿。

重要：Dropout 只在训练时生效！model.train() / model.eval()
影响 Dropout 的行为。

2. BatchNorm vs LayerNorm（面试高频考点！）

BatchNorm：在 batch 维度做归一化
LayerNorm：在 feature 维度做归一化

假设输入是 (batch=32, features=128)：

BatchNorm：对每个 features，用 32 个样本的均值和方差归一化
LayerNorm：对每个样本，用 128 个 features 的均值和方差归一化

为什么 Transformer 用 LayerNorm 不用 BatchNorm？
① NLP 的 batch 大小通常较小（受显存限制），小 batch 下 BN 不稳定
② 文本长度不固定，BN 需要 padding mask 处理，LN 天然支持
③ LN 对 batch size 不敏感，训练和推理行为一致

3. LayerNorm 的训练/推理区别

训练时：用当前 batch 的均值/方差
推理时：用训练时累积的 running mean/var（和 BatchNorm 一样）

### 晚上电脑 · 2 小时
任务 1：实现 Dropout 并验证效果

```python
  class MyDropout(nn.Module):
      def __init__(self, p=0.5):
          super().__init__()
          self.p = p
```

def forward(self, x):
          if self.training:
              mask = (torch.rand_like(x) > self.p).float()
              return x * mask / (1 - self.p)  # 除以 (1-p) 补偿
          return x
```

# 验证 train/eval 模式的区别
drop = MyDropout(p=0.5)
x = torch.ones(1000)

drop.train()
train_out = drop(x)
print(f"训练模式，非零比例: {(train_out > 0).float().mean():.3f}")  # ≈ 0.5

drop.eval()
eval_out = drop(x)
print(f"评估模式，均值: {eval_out.mean():.3f}")  # ≈ 1.0

任务 2：对比 BN vs LN 的实验

训练 3 个相同的 MLP：
- 无归一化
- 带 BatchNorm
- 带 LayerNorm
对比收敛速度和最终准确率。

- [ ] 今日完成检查
- [ ] Dropout 手写实现，train/eval 模式切换正确
- [ ] BatchNorm vs LayerNorm 的区别能说清楚
### 第12周 · 星期三-六：权重初始化 + 梯度裁剪 + 混合精度
---
### 星期三
权重初始化实验
Xavier 初始化 vs Kaiming 初始化 vs 随机小值
验证不同初始化对训练速度的影响

### 星期四
梯度裁剪 + Warmup
```python
    # Warmup：前 N 步学习率从 0 线性增长到目标值
    def warmup_lr(step, warmup_steps, target_lr):
        if step < warmup_steps:
            return target_lr * step / warmup_steps
        return target_lr
```

# 梯度裁剪：防止梯度爆炸
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    ```


### 星期五
混合精度训练（AMP）
```

    from torch.cuda.amp import autocast, GradScaler
```

scaler = GradScaler()
```python
with autocast():  # 自动用 fp16 计算（更快）
        output = model(x)
        loss = criterion(output, y)
```

scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()

### 星期六
深度学习调参完整实验
固定模型，系统调 4 个超参数：
lr × batch_size × dropout × weight_decay
输出调参报告 + Wandb 对比图

- [ ] 第12周完成检查
- [ ] 反向传播能手动推导 2 层 MLP
- [ ] Dropout/BN/LN 手写实现
- [ ] 梯度裁剪 + AMP 会用
### 第13周 · 主题：深度学习进阶


-  本周目标：用 CNN/LSTM 做真实任务 ──
第13周 · 星期一：CNN 做 CIFAR-10（自定义数据集）

手机摸鱼：
CNN 核心组件：Conv2d（卷积提取特征）→ ReLU（非线性）→ MaxPool2d（降采样）
多层堆叠：浅层学边缘/纹理，深层学形状/语义
关键参数：kernel_size（卷积核大小）、stride（步长）、padding（填充）

带数据增强的 CNN：
```python
  from torchvision import transforms
```

train_transform = transforms.Compose([
```python
transforms.RandomHorizontalFlip(p=0.5),   # 随机翻转（数据增强！）
      transforms.RandomCrop(32, padding=4),     # 随机裁剪
      transforms.ToTensor(),
      transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))
  ])
  # 数据增强是防止过拟合最有效的手段之一，比调参更有效
  ```


第13周 · 星期二：RNN / LSTM 做文本情感分类

手机摸鱼：
RNN 循环：h_t = tanh(W_h·h_{t-1} + W_x·x_t)
问题：长序列梯度消失 → 记不住远距离依赖
LSTM 改进：引入"门控"机制（遗忘门/输入门/输出门），选择性记忆

晚上代码：用真实中文数据集（如 ChnSentiCorp）训练 LSTM 分类器
```

  class LSTMClassifier(nn.Module):
      def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
          self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True,
                              bidirectional=True, dropout=0.3, num_layers=2)
          self.fc = nn.Sequential(
              nn.Linear(hidden_dim * 2, hidden_dim),
              nn.ReLU(), nn.Dropout(0.3),
              nn.Linear(hidden_dim, num_classes)
          )
```

def forward(self, x, lengths):
          # x: (batch, seq_len)
          embedded = self.embedding(x)
          # pack_padded_sequence 跳过 padding，加速计算
          packed = nn.utils.rnn.pack_padded_sequence(
              embedded, lengths.cpu(), batch_first=True, enforce_sorted=False)
          lstm_out, (h_n, c_n) = self.lstm(packed)
          # 取两个方向最后一层的 hidden state
          last_hidden = torch.cat([h_n[-2], h_n[-1]], dim=-1)  # (batch, hidden*2)
          return self.fc(last_hidden)
  ```


第13周 · 星期三：GRU 对比 LSTM

手机摸鱼：
GRU = LSTM 的简化版：合并遗忘门和输入门为"更新门"
参数量少 25%，训练更快，效果相当（小数据集上甚至更好）

晚上：用相同数据、相同超参对比 LSTM vs GRU 的速度和准确率

第13周 · 星期四：AMP 混合精度原理 + PyTorch Lightning

手机摸鱼：
为什么 fp16 更快？现代 GPU（如 3090/A100）的 fp16 算力是 fp32 的 8-16 倍。
为什么不能全用 fp16？梯度下溢：小梯度在 fp16 中变成 0 → 参数不更新。
GradScaler：在 backward 前把 loss 放大（scale），backward 后再缩小（unscale），
这样小梯度就不会在 fp16 中下溢。

PyTorch Lightning：把训练循环抽象掉，只保留模型的 forward + configure_optimizers。
Trainer 自动处理 device/checkpoint/logging/multi-GPU。

```

  # AMP 原理验证：观察 fp16 和 fp32 的数值差异
  x_fp32 = torch.tensor(1e-8, dtype=torch.float32)
  x_fp16 = torch.tensor(1e-8, dtype=torch.float16)
  print(f"fp32: {x_fp32.item():.15f}")  # 1e-8（保留）
  print(f"fp16: {x_fp16.item():.15f}")  # 0.0（下溢！）
  # 这就是为什么需要 GradScaler——防止小梯度在 fp16 中变成 0
  ```


第13周 · 星期五-六：GPU 显存管理 + 综合项目

星期五手机：了解 OOM 原因和处理
显存占用 = 模型参数 + 梯度 + 优化器状态 + 中间激活（activations）
Adam 优化器占用 = 模型参数的 2 倍（m 和 v 两个状态）
训练时总显存 ≈ 模型参数 × 4（前向+反向+优化器×2）+ batch 相关

星期五晚上 + 星期六：
综合 DL 项目：图像分类或文本分类，包含以下完整流程
① 数据加载（自定义 Dataset）→ ② 数据增强 → ③ 模型定义
→ ④ 训练循环（AMP + gradient clipping）→ ⑤ Wandb 监控
→ ⑥ Checkpoint 保存/加载 → ⑦ 测试集评估 → ⑧ 混淆矩阵可视化

```

  # 显存诊断工具
  print(torch.cuda.memory_summary())  # 详细显存报告
  print(f"已分配: {torch.cuda.memory_allocated()/1e9:.2f} GB")
  print(f"已缓存: {torch.cuda.memory_reserved()/1e9:.2f} GB")
```

# OOM 处理策略（优先级从高到低）
# 1. 减小 batch_size（最直接）
# 2. 启用 gradient_accumulation（小 batch 多步累积再更新）
# 3. 减小模型（hidden_dim 或 n_layers）
# 4. 用 fp16/bf16（省一半显存）
# 5. 用 gradient checkpointing（牺牲 20% 速度节省激活显存）

- [ ] 第13周完成检查
- [ ] CNN 能处理带数据增强的自定义数据集
- [ ] LSTM/GRU 情感分类跑通，能对比效果
- [ ] 理解 AMP 原理 + 能处理 OOM
- [ ] 综合 DL 项目完成并 push
### 第14周 · 主题：NLP 基础 + BERT Fine-tune


-  本周目标：掌握 NLP 标准工具链 ──
### 星期一
文本预处理完整 pipeline
手机摸鱼：
中文分词难点：不像英文有空格分隔。jieba 是最常用中文分词库。
去停用词：的/了/是/在... 这些高频但对语义贡献小的词。
TF-IDF = 词频 × log(总文档数/包含该词的文档数)，用于找"重要但不常见"的词。

```python
  import jieba, re
  from collections import Counter
```

def preprocess_chinese(text):
```python
# 1. 去除非中文字符
      text = re.sub(r'[^\u4e00-\u9fff]', ' ', text)
      # 2. 分词
      words = jieba.lcut(text)
      # 3. 去停用词
      stopwords = set(['的', '了', '在', '是', '我', '有', '和', '就',
                       '不', '人', '都', '一', '一个', '上', '也', '很', '到'])
      words = [w for w in words if w not in stopwords and len(w) > 1]
      return words
```

# 测试
text = "自然语言处理是人工智能的一个重要方向，近年来发展迅速"
print(preprocess_chinese(text))
# ['自然语言', '处理', '人工智能', '一个', '重要', '方向', '近年', '发展', '迅速']

### 星期二
Word2Vec / GloVe 词向量
手机摸鱼：
独热编码：词表 5 万 → 每个词是 5 万维向量（极度稀疏，无法表达语义）
词向量：把每个词映射到低维稠密空间（如 300 维），语义相近的词向量也相近
king - man + woman ≈ queen（向量运算表达了语义关系！）

```python
  import gensim.downloader as api
```

# 加载预训练词向量
wv = api.load('glove-wiki-gigaword-100')  # 100 维，约 400MB
# 或中文：wv = api.load('glove-wiki-gigaword-100')  # 无官方中文版，可用 Tencent AI Lab 的

# 语义相似度
print(wv.similarity('king', 'queen'))      # ~0.75
print(wv.similarity('king', 'computer'))   # ~0.1

# 类比推理
print(wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=3))
# [('queen', ...), ('princess', ...), ...]

# 不匹配词
print(wv.doesnt_match(['apple', 'banana', 'car', 'orange']))  # car

### 星期三
Tokenizer 原理（BPE 深度）
手机摸鱼：
BPE 步骤：
① 把所有词拆成字符：hello → h e l l o
② 统计所有相邻字符对的出现频率
③ 选择最高频的一对合并为一个新 token
④ 重复 N 次（N 是词表大小）

为什么好？未登录词（训练时没见过的词）可以被拆成已知的子词。
"unhappiness" → "un" + "happiness" → 模型能猜出意思。

```python
  # 用 HuggingFace tokenizer 实验
  from transformers import AutoTokenizer
```

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
text = "我喜欢学习人工智能"
tokens = tokenizer.tokenize(text)
print(tokens)  # ['我', '喜', '欢', '学', '习', '人', '工', '智', '能']
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
restored = tokenizer.decode(ids)
print(restored)  # 我 喜 欢 学 习 人 工 智 能（空格分隔）

### 星期四
BERT Fine-tune 文本分类（完整版）
```python
  from transformers import AutoTokenizer, AutoModelForSequenceClassification
  from transformers import Trainer, TrainingArguments, EarlyStoppingCallback
  from datasets import Dataset
  import numpy as np
  from sklearn.metrics import accuracy_score, f1_score
```

def compute_metrics(eval_pred):
logits, labels = eval_pred
preds = np.argmax(logits, axis=1)
return {"accuracy": accuracy_score(labels, preds),
"f1": f1_score(labels, preds, average='macro')}

model_name = "bert-base-chinese"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

def tokenize_fn(examples):
return tokenizer(examples["text"], padding=True, truncation=True, max_length=256)

# 假设已有 train_texts, train_labels, test_texts, test_labels
train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels})
test_dataset = Dataset.from_dict({"text": test_texts, "label": test_labels})
train_dataset = train_dataset.map(tokenize_fn, batched=True)
test_dataset = test_dataset.map(tokenize_fn, batched=True)

training_args = TrainingArguments(
output_dir="./bert-finetuned",
num_train_epochs=5,
per_device_train_batch_size=16,
per_device_eval_batch_size=64,
```python
evaluation_strategy="epoch",    # 每个 epoch 评估一次
      save_strategy="epoch",          # 每个 epoch 保存
      load_best_model_at_end=True,    # 训练完加载最佳模型
      metric_for_best_model="f1",
      logging_dir="./logs",
      logging_steps=50,
      fp16=torch.cuda.is_available(), # 有 GPU 就用混合精度
  )
```

trainer = Trainer(
model=model,
args=training_args,
train_dataset=train_dataset,
eval_dataset=test_dataset,
compute_metrics=compute_metrics,
callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
)

trainer.train()
print(trainer.evaluate())
trainer.save_model("./bert-finetuned-best")

### 星期五
GPT-2 文本生成
```python
  from transformers import GPT2LMHeadModel, GPT2Tokenizer
```

model = GPT2LMHeadModel.from_pretrained("uer/gpt2-chinese-cluecorpussmall")
tokenizer = GPT2Tokenizer.from_pretrained("uer/gpt2-chinese-cluecorpussmall")

def generate(prompt, max_length=100, temperature=0.8, top_p=0.9):
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
**inputs,
max_length=max_length,
```python
temperature=temperature,   # 控制随机性
          top_p=top_p,               # nucleus sampling
          do_sample=True,
          pad_token_id=tokenizer.eos_token_id,
          no_repeat_ngram_size=2,    # 避免重复
      )
      return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

print(generate("人工智能的未来是"))

### 星期六 · 3.5h
NLP 综合实战
选一个任务：新闻分类/情感分析/意图识别
完整流程：数据加载→预处理→Tokenizer→Trainer训练→评估→推理→部署
push 到 GitHub + README

- [ ] 第14周完成检查
- [ ] 文本预处理 pipeline 能独立编写
- [ ] 词向量语义运算理解
- [ ] BERT fine-tune 完整流程跑通（含 early stopping + 最佳模型保存）
- [ ] GPT-2 生成能调 temperature/top_p 控制输出
### 第15周 · 主题：****★★**★** 手写 Transformer ****★★**★**


这是整个 6 个月计划中最重要的 1 周。
目标：用纯 PyTorch 从零手写一个 Transformer，
不使用任何第三方库的 Transformer 实现。

> ⚠️ ️ 调试铁律（保存下来！）：
每写完一个模块，立即 print(x.shape) 确认维度。
Transformer 99% 的 bug 都是维度不匹配。
报错 "mat1 and mat2 shapes cannot be multiplied" 时，
检查 view/transpose/permute 的维度变换是否正确。
常用排查命令：
```python
print(f"期望: (batch, seq, d_model), 实际: {x.shape}")
```

### 第15周 · 星期一：Scaled Dot-Product Attention
---
### 手机摸鱼 · 上午 30 分钟
阅读主题：Attention 机制 —— Transformer 的灵魂

核心知识点（反复读直到能背）

1. Attention 的直觉

你在读一句话："我昨天去了那家餐厅，食物很好吃。"

当你要理解"食物"这个词时，你自然会关注"餐厅"和"好吃"。
你不会关注"昨天"这种无关的词。

Attention 就是让模型学会"关注什么"。

2. Query、Key、Value —— 三要素

Query (Q)：我要查什么？（当前词在问：谁和我有关？）
Key   (K)：我是什么？（每个词在喊：我在这里！我长这样！）
Value (V)：我有什么信息？（每个词的内容）

注意力计算：用 Q 去"查询"每个 K，得到的"匹配分数"
作为权重，对 V 加权求和。

3. Scaled Dot-Product Attention 公式（背下来！）

Attention(Q, K, V) = softmax(QK^T / √d_k) × V

分解理解：
① Q @ K^T ：计算每对词之间的"相关程度"矩阵
(batch, seq_len, d_k) @ (batch, d_k, seq_len) → (batch, seq_len, seq_len)
结果矩阵的 [i][j] 位置 = 词 i 对词 j 的 attention 分数

② / √d_k ：缩放。为什么？
d_k 很大时，QK^T 的值很大 → softmax 后梯度接近 0 → 学不动
除以 √d_k 把方差拉回 1。

③ softmax ：把分数变成"概率"（每行和为 1）
第 i 行的第 j 列 = 词 i 应该给词 j 多少"注意力"

④ @ V ：按注意力权重从 V 中提取信息
(batch, seq, seq) @ (batch, seq, d_v) → (batch, seq, d_v)

维度对照表（一定要记住！）

假设：batch=2, seq_len=4, d_model=8, num_heads=2
那么 d_k = d_model / num_heads = 4

Q: (2, 4, 4)    ← (batch, seq_len, d_k)
K: (2, 4, 4)
V: (2, 4, 4)

QK^T: (2, 4, 4) @ (2, 4, 4)^T = (2, 4, 4)
softmax(QK^T/√4): (2, 4, 4)   ← 每行和为 1
output: (2, 4, 4) @ (2, 4, 4) = (2, 4, 4)  ← 和 Q 形状一样！

### 晚上电脑 · 2 小时
任务：手写 Scaled Dot-Product Attention！

```python
  import torch
  import torch.nn as nn
  import torch.nn.functional as F
  import math
```

class ScaledDotProductAttention(nn.Module):
"""手写注意力：Attention(Q,K,V) = softmax(QK^T/√d_k)V"""

```python
def __init__(self, dropout=0.1):
          super().__init__()
          self.dropout = nn.Dropout(dropout)
```

def forward(self, Q, K, V, mask=None):
          """
          Q, K, V: (batch, n_heads, seq_len, d_k)
          mask: (batch, 1, seq_len, seq_len) or None
          """
          d_k = Q.size(-1)
```

# ① Q @ K^T / √d_k
          scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
          # scores: (batch, n_heads, seq_len, seq_len)
```

# ② mask（可选：Decoder 需要遮住未来位置）
          if mask is not None:
              scores = scores.masked_fill(mask == 0, float('-inf'))
```

# ③ softmax
          attention_weights = F.softmax(scores, dim=-1)
          attention_weights = self.dropout(attention_weights)
```

# ④ 加权求和
          output = torch.matmul(attention_weights, V)
          return output, attention_weights
```

# ========== 验证 ==========
batch, seq_len, d_model, n_heads = 2, 4, 8, 2
d_k = d_model // n_heads  # 4

Q = torch.randn(batch, n_heads, seq_len, d_k)
K = torch.randn(batch, n_heads, seq_len, d_k)
V = torch.randn(batch, n_heads, seq_len, d_k)

attn = ScaledDotProductAttention()
output, weights = attn(Q, K, V)

print(f"输出形状: {output.shape}")     # (2, 2, 4, 4)
print(f"注意力权重形状: {weights.shape}")  # (2, 2, 4, 4)
print(f"每行权重和（应接近1）:\n{weights[0,0].sum(dim=-1)}")

- [ ] 今日完成检查
- [ ] Attention 公式能默写：softmax(QK^T/√d_k)V
- [ ] 代码跑通，输出形状正确
- [ ] 理解 d_k 为什么是 d_model/num_heads
### 第15周 · 星期二：Multi-Head Attention
---
### 手机摸鱼
核心知识点

1. 为什么需要多头？

单头注意力：每个词只能以一种方式"关注"其他词。
多头注意力：并行计算多个"注意力视角"。

比如：
头 1：关注语法关系（主语-谓语）
头 2：关注语义关系（同义词）
头 3：关注位置关系（前后文）
头 4：关注...

2. Multi-Head Attention 的计算步骤

① 将 Q, K, V 分别投影 h 次（h = num_heads）
Q → [Q₁, Q₂, ..., Qₕ]  （每个是 d_k = d_model/h 维）
K → [K₁, K₂, ..., Kₕ]
V → [V₁, V₂, ..., Vₕ]

② 每个头独立执行 Attention(Qᵢ, Kᵢ, Vᵢ)

③ 将所有头的输出拼接 → 再经一次线性投影

MultiHead(Q,K,V) = Concat(head₁, ..., headₕ) W_O

其中 headᵢ = Attention(QWᵢ^Q, KWᵢ^K, VWᵢ^V)

### 晚上电脑
```python
  class MultiHeadAttention(nn.Module):
      def __init__(self, d_model, n_heads, dropout=0.1):
          super().__init__()
          assert d_model % n_heads == 0, "d_model 必须能被 n_heads 整除"
```

self.d_model = d_model
          self.n_heads = n_heads
          self.d_k = d_model // n_heads
```

# 投影矩阵（注意：合并了所有头的投影，效率更高）
          self.W_Q = nn.Linear(d_model, d_model)
          self.W_K = nn.Linear(d_model, d_model)
          self.W_V = nn.Linear(d_model, d_model)
          self.W_O = nn.Linear(d_model, d_model)  # 输出投影
```

self.attention = ScaledDotProductAttention(dropout)

```python
def split_heads(self, x):
          """x: (batch, seq_len, d_model)
             → (batch, n_heads, seq_len, d_k)"""
          batch, seq_len, _ = x.shape
          x = x.view(batch, seq_len, self.n_heads, self.d_k)
          return x.transpose(1, 2)  # (batch, n_heads, seq_len, d_k)
```

def combine_heads(self, x):
          """x: (batch, n_heads, seq_len, d_k)
             → (batch, seq_len, d_model)"""
          batch, _, seq_len, _ = x.shape
          x = x.transpose(1, 2)  # (batch, seq_len, n_heads, d_k)
          return x.reshape(batch, seq_len, self.d_model)
```

def forward(self, Q, K, V, mask=None):
          # 1. 线性投影
          Q = self.W_Q(Q)  # (batch, seq, d_model)
          K = self.W_K(K)
          V = self.W_V(V)
```

# 2. 拆分为多头
          Q = self.split_heads(Q)  # (batch, n_heads, seq, d_k)
          K = self.split_heads(K)
          V = self.split_heads(V)
```

# 3. 每个头独立做 Attention
          attn_out, attn_weights = self.attention(Q, K, V, mask)
```

# 4. 合并多头
          attn_out = self.combine_heads(attn_out)  # (batch, seq, d_model)
```

# 5. 输出投影
          return self.W_O(attn_out)
```

# ========== 验证 ==========
batch, seq_len, d_model, n_heads = 2, 4, 8, 2
x = torch.randn(batch, seq_len, d_model)

mha = MultiHeadAttention(d_model, n_heads)
output = mha(x, x, x)  # Self-Attention: Q=K=V=x
print(f"Multi-Head Attention 输出: {output.shape}")  # (2, 4, 8) ← 和输入形状一样！

- [ ] 今日完成检查
- [ ] 理解 split_heads / combine_heads 的维度变换
- [ ] Multi-Head Attention 输出和输入形状一致
- [ ] 能画出"输入 → 投影 → 拆头 → Attention → 拼头 → 输出"的数据流
### 第15周 · 星期三：Positional Encoding + Feed-Forward
---
### 手机摸鱼
核心知识点

1. 为什么需要位置编码？

Attention 本身是"无序"的——它对输入位置的排列不敏感。
但语言是有顺序的："狗咬人" vs "人咬狗"完全不同。

所以需要注入位置信息。

2. 正弦位置编码（Sinusoidal PE）

PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

其中 pos 是位置，i 是维度索引。

直觉：不同频率的正弦/余弦波编码了不同的位置模式。
位置相近的向量也相近（因为连续函数）。

优点：不需要学习参数，能外推到训练时没见过的长度。

3. Feed-Forward Network (FFN)

FFN(x) = ReLU(x @ W₁ + b₁) @ W₂ + b₂

或更现代的版本（LLaMA 用）：
FFN(x) = (SiLU(x @ W_gate) ⊙ (x @ W_up)) @ W_down

本质上是一个"两层的 MLP"，每个位置独立计算。
作用：增加模型的非线性和表达能力。

### 晚上电脑
任务 1：手写 Positional Encoding

```python
  class SinusoidalPositionalEncoding(nn.Module):
      def __init__(self, d_model, max_len=5000):
          super().__init__()
          pe = torch.zeros(max_len, d_model)
          position = torch.arange(0, max_len).unsqueeze(1).float()
          div_term = torch.exp(
              torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model)
          )
          pe[:, 0::2] = torch.sin(position * div_term)  # 偶数维度用 sin
          pe[:, 1::2] = torch.cos(position * div_term)  # 奇数维度用 cos
          self.register_buffer('pe', pe.unsqueeze(0))   # (1, max_len, d_model)
```

def forward(self, x):
          # x: (batch, seq_len, d_model)
          return x + self.pe[:, :x.size(1), :]
  ```


任务 2：手写 Feed-Forward Network

```

  class FeedForward(nn.Module):
      def __init__(self, d_model, d_ff, dropout=0.1):
          super().__init__()
          self.fc1 = nn.Linear(d_model, d_ff)    # 扩展：512 → 2048
          self.fc2 = nn.Linear(d_ff, d_model)    # 压缩：2048 → 512
          self.dropout = nn.Dropout(dropout)
          self.activation = nn.GELU()  # 或 ReLU()
```

def forward(self, x):
          return self.fc2(self.dropout(self.activation(self.fc1(x))))
  ```


- [ ] 今日完成检查
- [ ] PE 公式能默写
- [ ] FFN 的两层结构理解
### 第15周 · 星期四：Encoder Layer + Encoder 完整组装
---
### 手机摸鱼
核心知识点

1. Transformer Encoder Layer（一层）

输入 x
↓
Multi-Head Self-Attention
↓
Add & Norm (残差连接 + LayerNorm)
↓
Feed-Forward Network
↓
Add & Norm
↓
输出

伪代码：
```

def encoder_layer(x):
         x = LayerNorm(x + MultiHeadAttention(x, x, x))
         x = LayerNorm(x + FeedForward(x))
         return x
```

2. 残差连接（Residual Connection）的作用

把输入"跳过"一层直接加到输出上：
output = LayerNorm(x + sublayer(x))

为什么需要？
- 梯度可以直接流过残差路径（短路），缓解梯度消失
- 让深层网络至少不会比浅层更差（最坏情况 sublayer 输出 0，
残差连接保证至少输出原输入）

3. 完整的 Transformer Encoder

N 个 Encoder Layer 堆叠：
x → EncoderLayer₁ → EncoderLayer₂ → ... → EncoderLayerₙ → output

### 晚上电脑
```python
  class EncoderLayer(nn.Module):
      def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
          super().__init__()
          self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.feed_forward = FeedForward(d_model, d_ff, dropout)
          self.norm1 = nn.LayerNorm(d_model)
          self.norm2 = nn.LayerNorm(d_model)
          self.dropout = nn.Dropout(dropout)
```

def forward(self, x, mask=None):
          # 1. Self-Attention + 残差 + Norm
          attn_out = self.self_attn(x, x, x, mask)
          x = self.norm1(x + self.dropout(attn_out))
```

# 2. FFN + 残差 + Norm
          ff_out = self.feed_forward(x)
          x = self.norm2(x + self.dropout(ff_out))
```

return x

class TransformerEncoder(nn.Module):
```python
def __init__(self, vocab_size, d_model, n_heads, d_ff, n_layers, dropout=0.1):
          super().__init__()
          self.embedding = nn.Embedding(vocab_size, d_model)
          self.pos_encoding = SinusoidalPositionalEncoding(d_model)
          self.layers = nn.ModuleList([
              EncoderLayer(d_model, n_heads, d_ff, dropout)
              for _ in range(n_layers)
          ])
          self.dropout = nn.Dropout(dropout)
```

def forward(self, x, mask=None):
          # Token Embedding + Positional Encoding
          x = self.embedding(x) * math.sqrt(self.embedding.embedding_dim)
          x = self.pos_encoding(x)
          x = self.dropout(x)
```

# 逐层通过 Encoder
          for layer in self.layers:
              x = layer(x, mask)
```

return x

# ⚠️ 架构注释：这是 Post-LN（原论文风格）
#    写法：y = LayerNorm(x + Sublayer(x))
#    现代 LLM 用 Pre-LN：y = x + Sublayer(LayerNorm(x))
#    Pre-LN 训练更稳定，不需要 warmup。
#    面试常问两者的区别——在这里建立第一印象。

# ========== 验证：用随机输入测试 forward ==========
vocab_size, d_model, n_heads, d_ff, n_layers = 1000, 512, 8, 2048, 6
batch, seq_len = 2, 10

encoder = TransformerEncoder(vocab_size, d_model, n_heads, d_ff, n_layers)
dummy_input = torch.randint(0, vocab_size, (batch, seq_len))  # 随机 token IDs

output = encoder(dummy_input)
print(f"Encoder 输出形状: {output.shape}")  # (2, 10, 512)
print(f"参数量: {sum(p.numel() for p in encoder.parameters()):,}")

- [ ] 今日完成检查
- [ ] Encoder Layer 结构能画出来
- [ ] 完整 Encoder 能 forward 跑通
- [ ] 理解残差连接的梯度短路作用
### 第15周 · 星期五：Decoder + 完整 Transformer
---
### 手机摸鱼
核心知识点

1. Decoder 和 Encoder 的区别

Encoder：双向看（每个词能看到所有其他词）
Decoder：单向看（生成第 t 个词时，只能看到前 t-1 个词）

Decoder 比 Encoder 多一层 Cross-Attention：
- Self-Attention（Masked）：只看当前和之前的位置
- Cross-Attention：用 Decoder 的 Q 去查 Encoder 输出的 K, V

2. Masked Self-Attention

用一个上三角矩阵 mask：
[1, 0, 0, 0]  ← 第 1 个词只能看自己
[1, 1, 0, 0]  ← 第 2 个词能看 1-2
[1, 1, 1, 0]
[1, 1, 1, 1]

在 softmax 前，把 mask=0 的位置设为 -inf：
scores.masked_fill(mask == 0, float('-inf'))

softmax(-inf) = 0 → 这些位置的注意力权重为 0。

今日思考题
- 为什么 Decoder 在训练时也只需要一次 forward？
（因为 Masked Self-Attention + Teacher Forcing，
训练时输入是真实的前 t-1 个 token，不需要自回归生成）

### 晚上电脑
```python
  class DecoderLayer(nn.Module):
      def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
          super().__init__()
          self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)
          self.feed_forward = FeedForward(d_model, d_ff, dropout)
          self.norm1 = nn.LayerNorm(d_model)
          self.norm2 = nn.LayerNorm(d_model)
          self.norm3 = nn.LayerNorm(d_model)
          self.dropout = nn.Dropout(dropout)
```

def forward(self, x, enc_output, src_mask=None, tgt_mask=None):
          # 1. Masked Self-Attention（只能看当前及之前位置）
          attn_out = self.self_attn(x, x, x, tgt_mask)
          x = self.norm1(x + self.dropout(attn_out))
```

# 2. Cross-Attention（用 Decoder 的 Q 查 Encoder 的 K,V）
          attn_out = self.cross_attn(x, enc_output, enc_output, src_mask)
          x = self.norm2(x + self.dropout(attn_out))
```

# 3. FFN
          ff_out = self.feed_forward(x)
          x = self.norm3(x + self.dropout(ff_out))
```

return x

- [ ] 今日完成检查
- [ ] Decoder Layer 三层结构理解（Self-Attn → Cross-Attn → FFN）
- [ ] 理解 Masked Self-Attention 的作用
### 第15周 · 星期六：★★★ 终极组装 ★★★
### 14:00-17:00 完整 Transformer（Encoder + Decoder）+ 测试
```python
  class Transformer(nn.Module):
      def __init__(self, src_vocab_size, tgt_vocab_size,
                   d_model, n_heads, d_ff, n_layers, dropout=0.1):
          super().__init__()
          self.encoder = TransformerEncoder(
              src_vocab_size, d_model, n_heads, d_ff, n_layers, dropout)
          self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
          self.decoder_pos = SinusoidalPositionalEncoding(d_model)
          self.decoder_layers = nn.ModuleList([
              DecoderLayer(d_model, n_heads, d_ff, dropout)
              for _ in range(n_layers)
          ])
          self.fc_out = nn.Linear(d_model, tgt_vocab_size)
          self.dropout = nn.Dropout(dropout)
```

def forward(self, src, tgt, src_mask=None, tgt_mask=None):
          # Encoder
          enc_output = self.encoder(src, src_mask)
```

# Decoder
          x = self.decoder_embedding(tgt) * math.sqrt(d_model)
          x = self.decoder_pos(x)
          x = self.dropout(x)
```

for layer in self.decoder_layers:
x = layer(x, enc_output, src_mask, tgt_mask)

```python
return self.fc_out(x)  # (batch, tgt_len, tgt_vocab_size)
```

def generate(self, src, max_len, start_token, end_token):
          """推理模式：自回归生成"""
          self.eval()
          # Encode 源序列（只做一次）
          with torch.no_grad():
              enc_output = self.encoder(src)
```

# 逐 token 生成
          generated = [start_token]
          for _ in range(max_len):
              tgt = torch.tensor([generated]).to(src.device)
              # 构建因果 mask
              tgt_mask = self._generate_square_subsequent_mask(len(generated))
              # Decoder forward
              output = self.forward(src, tgt, tgt_mask=tgt_mask)
              # 取最后一个位置的预测
              next_token = output[0, -1].argmax().item()
              generated.append(next_token)
              if next_token == end_token:
                  break
```

return generated

验证清单（逐一确认）：
- [ ] Encoder 输入 (2, 10)，输出 (2, 10, 512) ✓
- [ ] Decoder 输入 (2, 8) + Encoder 输出，输出 (2, 8, tgt_vocab_size) ✓
- [ ] 所有层参数正确计数
- [ ] generate() 能自回归生成 token 序列

- ⭐ 把这个 Transformer 类和本周所有模块的代码 push 到 GitHub！
17:00-17:30 复盘
本周你面前（不是背，是亲手写！）了：
- [ ] Scaled Dot-Product Attention
- [ ] Multi-Head Attention
- [ ] Positional Encoding
- [ ] Feed-Forward Network
- [ ] Encoder Layer → Encoder
- [ ] Decoder Layer
- [ ] 完整 Transformer（Encoder + Decoder）
- [ ] generate() 自回归推理

- [ ] 第15周完成检查
- [ ] 完整 Transformer 能 forward 跑通
- [ ] 维度全部核对正确
- [ ] 代码 push 到 GitHub
### 第16周 · 主题：NLP 进阶 + 微调概念入门


### 星期一
Decoder 回顾 + GPT-2 Fine-tuning（HF Trainer）
### 星期二
P-Tuning v2 概念 + 简单实验
### 星期三
LoRA 概念理解（低秩分解的直觉）+ PEFT 库入门
LoRA 核心思想：不在原权重矩阵上训练，而是在旁边加两个小矩阵 A 和 B，
只训练 A 和 B（参数量是原来的 1/1000）。
W_new = W_original + B × A（其中 A 和 B 的秩远小于 W）
### 星期四
完整训练一个 GPT-2 Small 文本生成
### 星期五
复习 + 整理所有 NLP 代码
### 星期六
阶段三综合复盘
1. 手写一遍 Transformer forward（白板默写！不查代码！）
2. 标注每个 tensor 的维度
3. 整理本周所有代码到 GitHub
4. 更新 Obsidian

- [ ] 第16周完成检查
- [ ] GPT-2 fine-tune 成功
- [ ] 理解 LoRA 的低秩分解原理
- [ ] Transformer 能闭眼默写
### 阶段三结束 · 终极验收


你已完成整个计划中最核心的 162 小时！

- [ ] 能手写完整的 Transformer forward
Attention(Q,K,V) = softmax(QK^T/√d_k)V
MultiHead → Add&Norm → FFN → Add&Norm
- [ ] 能独立写完训练循环（DataLoader → forward → loss → backward → step）
- [ ] 能用 HuggingFace fine-tune BERT/GPT-2
- [ ] 理解 LoRA 的核心思想
- [ ] sklearn ML Pipeline + PyTorch DL Pipeline 都做过实战

下一步：阶段四 · Agent 开发（LangChain + LangGraph + RAG）

### END OF 阶段三·下

