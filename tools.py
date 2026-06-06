"""
Cache Tools - AI缓存工具
支持缓存策略生成、优化、监控
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class CacheTools:
    """
    AI缓存工具
    支持：策略生成、优化、监控
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_strategy(self, app_type: str, traffic: str = "medium") -> Dict:
        """生成缓存策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{app_type}应用生成缓存策略：

流量级别：{traffic}

请返回JSON格式：
{{
    "layers": [
        {{"name": "缓存层", "type": "类型", "ttl": "过期时间", "size": "大小"}}
    ],
    "invalidation": "失效策略",
    "tools": ["推荐工具"],
    "best_practices": ["最佳实践"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"strategy": content}

    def generate_redis_config(self, use_case: str) -> str:
        """生成Redis配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下场景生成Redis配置：

场景：{use_case}

要求：
1. 性能优化
2. 内存优化
3. 持久化配置
4. 安全配置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def optimize_cache(self, current_config: str, hit_rate: float) -> Dict:
        """优化缓存"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请优化以下缓存配置：

当前配置：{current_config}
命中率：{hit_rate}%

请返回JSON格式：
{{
    "issues": ["问题1", "问题2"],
    "optimizations": [
        {{"setting": "配置项", "current": "当前值", "recommended": "推荐值", "reason": "原因"}}
    ],
    "expected_improvement": "预期提升"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_cdn_config(self, domain: str, content_type: str = "static") -> str:
        """生成CDN配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{domain}生成CDN配置：

内容类型：{content_type}

请生成Nginx/CloudFlare配置："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def analyze_cache_pattern(self, access_logs: List[str]) -> Dict:
        """分析缓存模式"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        logs_text = "\n".join(access_logs[:20])

        prompt = f"""请分析以下访问日志的缓存模式：

{logs_text}

请返回JSON格式：
{{
    "hot_keys": ["热点key"],
    "access_pattern": "访问模式",
    "ttl_suggestions": {{"key_pattern": "建议TTL"}},
    "optimizations": ["优化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}


def create_tools(**kwargs) -> CacheTools:
    """创建缓存工具"""
    return CacheTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Cache Tools")
    print()

    # 测试
    strategy = tools.generate_strategy("电商网站", "high")
    print(json.dumps(strategy, ensure_ascii=False, indent=2))
