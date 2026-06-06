# ⚡ Cache Tools

AI缓存工具，支持缓存策略生成、优化、监控。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📋 缓存策略生成
- ⚙️ Redis配置生成
- ⚡ 缓存优化
- 🌐 CDN配置生成
- 📊 缓存模式分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from cache_tools import create_tools

tools = create_tools()

# 生成策略
strategy = tools.generate_strategy("电商网站", "high")

# Redis配置
redis_config = tools.generate_redis_config("会话缓存")

# 优化缓存
optimization = tools.optimize_cache(current_config, 0.65)

# CDN配置
cdn = tools.generate_cdn_config("example.com", "static")

# 分析模式
pattern = tools.analyze_cache_pattern(access_logs)
```

## 📁 项目结构

```
cache-tools/
├── tools.py       # 缓存工具核心
└── README.md
```

## 📄 许可证

MIT License
