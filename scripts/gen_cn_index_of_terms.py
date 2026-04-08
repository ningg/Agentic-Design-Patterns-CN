#!/usr/bin/env python3
"""Generate cn/Index_of_Terms.md from en + cn/Glossary + term translations."""
from pathlib import Path
from typing import Optional, Tuple
import re

ROOT = Path(__file__).resolve().parents[1]

PAIRS = """
A/B Testing|A/B 测试
Action Selection|动作选择
Adaptation|适应
Adaptive Task Allocation|自适应任务分配
Adaptive Tool Use & Selection|自适应工具使用与选择
Agent|智能体（Agent）
Agent-Computer Interfaces (ACIs)|智能体—计算机接口（ACIs）
Agent-Driven Economy|智能体驱动的经济
Agent as a Tool|作为工具的智能体
Agent Cards|智能体卡片（Agent Cards）
Agent Development Kit (ADK)|智能体开发套件（ADK）
Agent Discovery|智能体发现
Agent Trajectories|智能体轨迹
Agentic Design Patterns|智能体设计模式
Agentic RAG|智能体化 RAG
Agentic Systems|智能体化系统
AI Co-scientist|AI 联合科学家（AI Co-scientist）
Alignment|对齐（Alignment）
AlphaEvolve|AlphaEvolve
Analogies|类比
Anomaly Detection|异常检测
Anthropic's Claude 4 Series|Anthropic Claude 4 系列
Anthropic's Computer Use|Anthropic 计算机使用
API Interaction|API 交互
Artifacts|制品（Artifacts）
Asynchronous Polling|异步轮询
Audit Logs|审计日志
Automated Metrics|自动化指标
Automatic Prompt Engineering (APE)|自动提示工程（APE）
Autonomy|自主性
A2A (Agent-to-Agent)|智能体到智能体（A2A）
Behavioral Constraints|行为约束
Browser Use|浏览器使用
Callbacks|回调
Causal Language Modeling (CLM)|因果语言建模（CLM）
Chain of Debates (CoD)|辩论链（CoD）
Chain-of-Thought (CoT)|思维链（CoT）
Chatbots|聊天机器人
ChatMessageHistory|聊天消息历史（ChatMessageHistory）
Checkpoint and Rollback|检查点与回滚
Chunking|分块
Clarity and Specificity|清晰与具体
Client Agent|客户端智能体
Code Generation|代码生成
Code Prompting|代码提示
CoD (Chain of Debates)|辩论链（CoD）
CoT (Chain of Thought)|思维链（CoT）
Collaboration|协作
Compliance|合规
Conciseness|简洁性
Content Generation|内容生成
Context Engineering|上下文工程
Context Window|上下文窗口
Contextual Pruning & Summarization|上下文剪枝与摘要
Contextual Prompting|上下文提示
Contractor Model|承包方模型（Contractor Model）
ConversationBufferMemory|会话缓冲记忆（ConversationBufferMemory）
Conversational Agents|对话式智能体
Cost-Sensitive Exploration|代价敏感探索
CrewAI|CrewAI
Critique Agent|评判智能体
Critique Model|评判模型
Customer Support|客户支持
Data Extraction|数据抽取
Data Labeling|数据标注
Database Integration|数据库集成
DatabaseSessionService|数据库会话服务（DatabaseSessionService）
Debate and Consensus|辩论与共识
Decision Augmentation|决策增强
Decomposition|分解
Deep Research|深度研究
Delimiters|分隔符
Denoising Objectives|去噪目标
Dependencies|依赖
Diffusion Models|扩散模型
Direct Preference Optimization (DPO)|直接偏好优化（DPO）
Discoverability|可发现性
Drift Detection|漂移检测
Dynamic Model Switching|动态模型切换
Dynamic Re-prioritization|动态重排优先级
Embeddings|嵌入
Embodiment|具身
Energy-Efficient Deployment|高能效部署
Episodic Memory|情景记忆
Error Detection|错误检测
Error Handling|错误处理
Escalation Policies|升级策略
Evaluation|评估
Exception Handling|异常处理
Expert Teams|专家团队
Exploration and Discovery|探索与发现
External Moderation APIs|外部审核 API
Factored Cognition|因子化认知（Factored Cognition）
FastMCP|FastMCP
Fault Tolerance|容错
Few-Shot Learning|少样本学习
Few-Shot Prompting|少样本提示
Fine-tuning|微调
Formalized Contract|形式化合约
Function Calling|函数调用
Gemini Live|Gemini Live
Gems|Gems
Generative Media Orchestration|生成式媒体编排
Goal Setting|目标设定
GoD (Graph of Debates)|辩论图（GoD）
Google Agent Development Kit (ADK)|Google 智能体开发套件（ADK）
Google Co-Scientist|Google Co-Scientist
Google DeepResearch|Google DeepResearch
Google Project Mariner|Google Project Mariner
Graceful Degradation|优雅降级
Graph of Debates (GoD)|辩论图（GoD）
Grounding|接地（Grounding）
Guardrails|护栏（Guardrails）
Haystack|Haystack
Hierarchical Decomposition|层次分解
Hierarchical Structures|层次结构
HITL (Human-in-the-Loop)|人在回路（HITL）
Human-in-the-Loop (HITL)|人在回路（HITL）
Human-on-the-loop|人在环上（Human-on-the-loop）
Human Oversight|人类监督
In-Context Learning|上下文学习
InMemoryMemoryService|内存记忆服务（InMemoryMemoryService）
InMemorySessionService|内存会话服务（InMemorySessionService）
Input Validation/Sanitization|输入校验/净化
Instructions Over Constraints|指令优于约束
Inter-Agent Communication (A2A)|智能体间通信（A2A）
Intervention and Correction|干预与纠正
IoT Device Control|物联网设备控制
Iterative Prompting / Refinement|迭代提示/精炼
Jailbreaking|越狱攻击
Kahneman-Tversky Optimization (KTO)|Kahneman–Tversky 优化（KTO）
Knowledge Retrieval (RAG)|知识检索（RAG）
LangChain|LangChain
LangGraph|LangGraph
Latency Monitoring|延迟监控
Learned Resource Allocation Policies|学习的资源分配策略
Learning and Adaptation|学习与适应
LLM-as-a-Judge|LLM 作评判（LLM-as-a-Judge）
LlamaIndex|LlamaIndex
LoRA (Low-Rank Adaptation)|LoRA（低秩适配）
Low-Rank Adaptation (LoRA)|低秩适配（LoRA）
Mamba|Mamba
Masked Language Modeling (MLM)|掩码语言建模（MLM）
MASS (Multi-Agent System Search)|多智能体系统搜索（MASS）
MCP (Model Context Protocol)|模型上下文协议（MCP）
Memory Management|记忆管理
Memory-Based Learning|基于记忆的学习
MetaGPT|MetaGPT
Microsoft AutoGen|Microsoft AutoGen
Mixture of Experts (MoE)|混合专家（MoE）
Model Context Protocol (MCP)|模型上下文协议（MCP）
Modularity|模块化
Monitoring|监控
Multi-Agent Collaboration|多智能体协作
Multi-Agent System Search (MASS)|多智能体系统搜索（MASS）
Multimodality|多模态
Multimodal Prompting|多模态提示
Negative Examples|负例
Next Sentence Prediction (NSP)|下一句预测（NSP）
Observability|可观测性
One-Shot Prompting|单样本提示
Online Learning|在线学习
OpenAI Deep Research API|OpenAI Deep Research API
OpenEvolve|OpenEvolve
OpenRouter|OpenRouter
Output Filtering/Post-processing|输出过滤/后处理
PAL (Program-Aided Language Models)|程序辅助语言模型（PAL）
Parallelization|并行化
Parallelization & Distributed Computing Awareness|并行化与分布式计算意识
Parameter-Efficient Fine-Tuning (PEFT)|参数高效微调（PEFT）
PEFT (Parameter-Efficient Fine-Tuning)|参数高效微调（PEFT）
Performance Tracking|性能跟踪
Persona Pattern|人设模式
Personalization|个性化
Planning|规划
Prioritization|优先级排序
Principle of Least Privilege|最小权限原则
Proactive Resource Prediction|主动资源预测
Procedural Memory|程序性记忆
Program-Aided Language Models (PAL)|程序辅助语言模型（PAL）
Project Astra|Project Astra
Prompt|提示（Prompt）
Prompt Chaining|提示链
Prompt Engineering|提示工程
Proximal Policy Optimization (PPO)|近端策略优化（PPO）
Push Notifications|推送通知
QLoRA|QLoRA
Quality-Focused Iterative Execution|以质量为中心的迭代执行
RAG (Retrieval-Augmented Generation)|检索增强生成（RAG）
ReAct (Reason and Act)|ReAct（推理与行动）
Reasoning|推理
Reasoning-Based Information Extraction|基于推理的信息抽取
Recovery|恢复
Recurrent Neural Network (RNN)|循环神经网络（RNN）
Reflection|反思
Reinforcement Learning|强化学习
Reinforcement Learning from Human Feedback (RLHF)|基于人类反馈的强化学习（RLHF）
Reinforcement Learning with Verifiable Rewards (RLVR)|可验证奖励的强化学习（RLVR）
Remote Agent|远程智能体
Request/Response (Polling)|请求/响应（轮询）
Resource-Aware Optimization|资源感知优化
Retrieval-Augmented Generation (RAG)|检索增强生成（RAG）
RLHF (Reinforcement Learning from Human Feedback)|RLHF（基于人类反馈的强化学习）
RLVR (Reinforcement Learning with Verifiable Rewards)|RLVR（可验证奖励的强化学习）
RNN (Recurrent Neural Network)|RNN（循环神经网络）
Role Prompting|角色提示
Router Agent|路由智能体
Routing|路由
Safety|安全
Scaling Inference Law|推理扩展律（Scaling Inference Law）
Scheduling|调度
Self-Consistency|自洽性
Self-Correction|自校正
Self-Improving Coding Agent (SICA)|自改进编程智能体（SICA）
Self-Refinement|自精炼
Semantic Kernel|Semantic Kernel
Semantic Memory|语义记忆
Semantic Similarity|语义相似度
Separation of Concerns|关注点分离
Sequential Handoffs|顺序交接
Server-Sent Events (SSE)|服务器推送事件（SSE）
Session|会话
SICA (Self-Improving Coding Agent)|SICA（自改进编程智能体）
SMART Goals|SMART 目标
State|状态
State Rollback|状态回滚
Step-Back Prompting|退一步提示（Step-Back Prompting）
Streaming Updates|流式更新
Structured Logging|结构化日志
Structured Output|结构化输出
SuperAGI|SuperAGI
Supervised Fine-Tuning (SFT)|监督微调（SFT）
Supervised Learning|监督学习
System Prompting|系统提示
Task Evaluation|任务评估
Text Similarity|文本相似度
Token Usage|Token 用量
Tool Use|工具使用
Tool Use Restrictions|工具使用限制
ToT (Tree of Thoughts)|思维树（ToT）
Transformers|Transformer
Tree of Thoughts (ToT)|思维树（ToT）
Unsupervised Learning|无监督学习
User Persona|用户人设
Validation|验证
Vector Search|向量检索
VertexAiRagMemoryService|VertexAiRagMemoryService
VertexAiSessionService|VertexAiSessionService
Vibe Coding|Vibe Coding
Visual Perception|视觉感知
Webhooks|Webhooks
Zero-Shot Learning|零样本学习
Zero-Shot Prompting|零样本提示
"""

ZH = {}
for line in PAIRS.strip().splitlines():
    if "|" not in line:
        continue
    k, v = line.split("|", 1)
    ZH[k.strip()] = v.strip()


def parse_glossary_cn(path: Path):
    """Return list of (english_block_first_line, zh_quote_line)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("**") and ":**" in line:
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].startswith("> "):
                out.append((line, lines[j]))
                i = j + 1
                continue
        i += 1
    return out


def parse_glossary_plain_cn(path: Path):
    """Paragraphs that do not use **Term:** (e.g. lifecycle intro, AI agents intro)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("The development of a powerful") or line.startswith(
            "AI agents are systems"
        ):
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and lines[j].startswith("> "):
                out.append((line, lines[j]))
                i = j + 1
                continue
        i += 1
    return out


def english_key_from_glossary_line(line: str) -> Optional[str]:
    m = re.match(r"\*\*(.+?):\*\*", line)
    if m:
        return m.group(1).strip()
    return None


def build_index_glossary_section(en_index_path: Path, pairs_gl: list) -> str:
    """First part of Index: same structure as en/Index glossary, with blockquotes."""
    en_text = en_index_path.read_text(encoding="utf-8")
    idx = en_text.index("## Index of Terms")
    head = en_text[:idx]
    lines = head.splitlines()
    # Map English first line (normalized) -> zh quote
    emap = {}
    for eng, zh in pairs_gl:
        k = english_key_from_glossary_line(eng)
        if k:
            emap[k] = zh
        emap[eng.strip()] = zh

    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out_lines.append(line)
        stripped = line.strip()
        # Match **Term:** style in glossary file for lookup
        if stripped.startswith("- **") and ":**" in stripped:
            inner = stripped[2:]
            m = re.match(r"\*\*(.+?)\*\*:\s*(.*)", inner)
            if m:
                term_key = m.group(1).strip()
                zh = emap.get(term_key)
                if zh:
                    out_lines.append("")
                    out_lines.append(zh)
        elif stripped.startswith("**") and ":**" in stripped and not stripped.startswith("- "):
            m = re.match(r"\*\*(.+?):\*\*", stripped)
            if m:
                term_key = m.group(1).strip()
                zh = emap.get(term_key)
                if zh:
                    out_lines.append("")
                    out_lines.append(zh)
        elif stripped.startswith("- The development") or stripped.startswith(
            "- Pre-training"
        ) or stripped.startswith("- Fine-tuning") or stripped.startswith("- Alignment"):
            zh = emap.get(
                "The development of a powerful language model follows a distinct sequence."
            )
            if stripped.startswith("- Pre-training"):
                zh = emap.get("Pre-training Techniques")
            elif stripped.startswith("- Fine-tuning"):
                zh = emap.get("Fine-tuning Techniques")
            elif stripped.startswith("- Alignment"):
                zh = emap.get("Alignment & Safety Techniques")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped == "- AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.":
            zh = emap.get(
                "AI agents are systems that can perceive their environment and take autonomous actions to achieve goals."
            )
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("- **Chain of Thought"):
            zh = emap.get("Chain of Thought (CoT)")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("- **Tree of Thoughts"):
            zh = emap.get("Tree of Thoughts (ToT)")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("- **Planning"):
            zh = emap.get("Planning")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("- **Deep Research"):
            zh = emap.get("Deep Research")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("- **Critique Model"):
            zh = emap.get("Critique Model")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        elif stripped.startswith("**ReAct"):
            zh = emap.get("ReAct (Reason and Act)")
            if zh:
                out_lines.append("")
                out_lines.append(zh)
        i += 1

    return "\n".join(out_lines) + "\n"


def split_index_line(line: str) -> Optional[Tuple[str, str]]:
    line = line.strip()
    if not line.startswith("- "):
        return None
    rest = line[2:]
    markers = [" - Chapter ", " - Appendix ", " - Glossary", " - What makes", " - Introduction"]
    best_pos = None
    for m in markers:
        pos = rest.find(m)
        if pos != -1 and (best_pos is None or pos < best_pos):
            best_pos = pos
    if best_pos is None:
        return None
    term = rest[:best_pos].strip()
    loc = rest[best_pos + 3 :].strip()
    return term, loc


def bilingual_prompt_and_reasoning(en_tail: str) -> str:
    """Append Chinese blockquotes after each paragraph in Prompt + Reasoning sections."""
    parts = []
    buf = []
    for line in en_tail.splitlines():
        if line.strip() == "" and buf:
            parts.append("\n".join(buf))
            buf = []
        else:
            buf.append(line)
    if buf:
        parts.append("\n".join(buf))

    out = []
    for block in parts:
        b = block.strip()
        if not b:
            continue
        out.append(block if block.endswith("\n") else block + "\n")
        if b.startswith("> *"):
            # quoted user prompt — add translation below block
            out.append(
                "\n> 译文：你是否阅读了上述 Google 文档及其首页所列相关文档？请提取每一章的标题并打印。然后处理各章内容，并创建用于出版的详细索引：词条（标题）及指向文档中相关内容的定位符。我不要示例索引；我要完整索引，且至少包含 100 个索引词条。\n"
            )
            continue
        if b.startswith("#"):
            # heading
            zh = None
            if b.startswith("## Prompt"):
                zh = "> 以下为用于生成本术语索引的提示。"
            elif b.startswith("## Gemini"):
                zh = "> 以下为 Gemini 2.5 的推理步骤（英文保留）。"
            elif b.startswith("### "):
                zh = "> （小节标题译文见各段下方。）"
            if zh:
                out.append(zh + "\n")
            continue
        if b.startswith("#### "):
            out.append(
                "> （步骤小节；具体推理见下段中文。）\n"
            )
            continue
        # body paragraph
        first = b.split("\n")[0][:120]
        # Skip duplicate translation for pure English meta - translate key paragraphs
        zh_line = translate_reasoning_paragraph(b)
        if zh_line:
            out.append("\n" + zh_line + "\n")

    return "\n".join(out)


def translate_reasoning_paragraph(text: str) -> Optional[str]:
    """Short Chinese summary line for reasoning appendix blocks."""
    t = text.strip()
    if t.startswith("#"):
        return None
    if len(t) < 20:
        return None
    # Map first sentence patterns to Chinese (abbreviated for long appendix)
    if "I've initiated" in t or "I've begun" in t:
        return "> 已开始阅读所提供的 Google 文档，并理解需要提取章标题以构建详细索引。"
    if "I've broken down" in t or "actionable steps" in t:
        return "> 已将用户需求拆解为可执行步骤，计划用 Workspaces 访问主文档并解析相关文档。"
    if "multi-step plan" in t.lower():
        return "> 制定了多步方案：先访问主 Google 文档，再解析并读取相关文档，提取标题并构建满足词条数量要求的索引。"
    if "Establish user intent" in t:
        return "> 明确用户意图：从 Google 文档及相关文档中提取章标题并建立全面索引；正在评估不同文档结构下的最佳策略。"
    if "I've determined the user wants a chapter title list" in t:
        return "> 已明确用户需要章标题列表与全面索引；正在探索可用的 API 能力并评估不同文档结构下的最佳提取与索引策略。"
    if "I've extracted the chapter URLs from the main document using a regular expression" in t:
        return "> 已用正则从主文档提取各章 URL，准备用 Workspaces 拉取每章正文以便索引。"
    if "Considering Tool Use" in t:
        return "> 已用正则从主文档提取各章 URL，准备用 Workspaces 拉取每章正文以便索引。"
    if "Accessing chapter content" in t:
        return "> 已定位各章 URL，下一步批量获取内容以生成索引，并注重处理效率。"
    if "Fetching Chapter Content" in t:
        return "> 计划批量请求各章内容，合并处理以生成完整索引。"
    if "Initiating URL Retrieval" in t:
        return "> 正在配置对 Workspaces 的调用以抓取各章文本，满足至少 100 个索引词的要求。"
    if "Initiating Chapter Extraction" in t:
        return "> 已开始逐章抓取内容，为构建大规模索引做准备。"
    if "Orchestrating Chapter Retrieval" in t:
        return "> 对 URL 请求进行分批以降低限流风险，并汇总文本供索引使用。"
    if "Decoding User Request" in t:
        return "> 用户要两类交付物：完整章标题列表，以及不少于一百个关键术语的详细索引。"
    if "Extracting Titles and Indexing" in t:
        return "> 已抓取 31 份 Google 文档；计划先从文件名提取章标题，再细读正文构建带定位符的索引。"
    if "Developing an Extraction Plan" in t:
        return "> 细化方案：从 31 份文档文件名汇总章标题，并分析正文生成按字母排序、超过 100 条的索引。"
    if "Crafting the Extraction Strategy" in t:
        return "> 方案已定：先汇总文件名中的章标题，再构建覆盖全书与附录的术语索引，力求详尽而非示例级。"
    if "Defining the Approach" in t:
        return "> 将先从文件名提取章标题，再构建逾百条、带章节位置的字母序索引，准备开始执行。"
    if "I've clarified the user's need. I will extract chapter titles from the document filenames" in t:
        return "> 已澄清需求：先从文档文件名提取章标题，再创建逾百条、按字母排序并标注章节位置的索引，准备开始执行索引与提取流程。"
    if "My approach is well-defined. I will compile chapter titles from the filenames" in t:
        return "> 方案明确：从 31 份文档文件名汇总章标题，再细读正文构建按字母排序、超过 100 条的索引；目标覆盖《Agentic Design Patterns》各章与附录，交付详尽索引而非示例。"
    if "I've refined my approach to tackle the user's request" in t:
        return "> 已细化方案：从已抓取的 31 份文档文件名汇总章标题，并分析正文以生成按字母排序、超过 100 条的全面索引；策略已定，可开始执行。"
    if "I've successfully identified the user's need: extracting chapter titles from the provided documents" in t:
        return "> 已确认需求：从所提供文档提取章标题并编制全面索引；已获取 31 份 Google 文档内容，无需额外工具；计划先据文件名提取章标题，再细读正文构建带定位符的索引。"
    if "I've determined the user's need. They require two primary deliverables" in t:
        return "> 已解码用户需求：一要提取 Google 文档中的完整章标题列表，二要构建至少包含一百个关键术语的详细索引；标题提取较直接，索引编纂需更细致的分析。"
    if "I've extracted the chapter URLs and initiated a call to Workspaces" in t:
        return "> 已提取章 URL 并调用 Workspaces；正分批获取各章内容以避免限流，并汇总文本供索引使用。"
    if "I've successfully identified and extracted the chapter URLs from the main document, which I've included above" in t:
        return "> 已识别并提取主文档中的章 URL（见上）；正逐 URL 用 Workspaces 获取正文以满足索引所需文本，并开始拉取数据。"
    if "I've now successfully extracted the chapter URLs from the main document. Currently, I'm setting up calls to the Workspaces tool" in t:
        return "> 已成功提取主文档中的章 URL；正在配置 Workspaces 调用以抓取各章正文，目标是为索引准备文本并满足至少 100 个索引词的要求。"
    if "I've successfully identified the chapter URLs from the main document and am ready to utilize Workspaces. My plan involves extracting these URLs, batching the calls" in t:
        return "> 已定位主文档中的章 URL；计划批量请求、合并处理检索到的内容，以生成完整、准确的索引。"
    if "I've successfully identified the URLs for each chapter from the main document, which I can now use with Workspaces" in t:
        return "> 已定位各章 URL，可用 Workspaces 拉取内容；下一步获取正文以生成索引，并注重处理效率。"
    return None


def main():
    en_path = ROOT / "en" / "Index_of_Terms.md"
    cn_glossary = ROOT / "cn" / "Glossary.md"
    out_path = ROOT / "cn" / "Index_of_Terms.md"
    pairs_gl = parse_glossary_cn(cn_glossary)
    # enrich emap: map first line of glossary cn to zh for lifecycle bullets
    emap = {}
    for eng, zh in pairs_gl:
        k = english_key_from_glossary_line(eng)
        if k:
            emap[k] = zh
        if eng.startswith("The development"):
            emap["The development of a powerful language model follows a distinct sequence."] = zh
        if eng.startswith("**Pre-training"):
            emap["Pre-training Techniques"] = zh
        if eng.startswith("**Fine-tuning"):
            emap["Fine-tuning Techniques"] = zh
        if eng.startswith("**Alignment & Safety"):
            emap["Alignment & Safety Techniques"] = zh
    for eng, zh in parse_glossary_plain_cn(cn_glossary):
        emap[eng.strip()] = zh

    # Re-build index glossary: manual merge using en head + inject quotes
    en_full = en_path.read_text(encoding="utf-8")
    split_mark = "## Index of Terms"
    head_en, rest = en_full.split(split_mark, 1)
    # head_en ends before Index; inject blockquotes line-by-line
    gl_lines = head_en.splitlines()
    out_g = []
    for line in gl_lines:
        out_g.append(line)
        stripped = line.strip()
        # Index glossary uses "- **Term**: body" (colon after closing **), not "**Term:**"
        if stripped.startswith("- **") and re.search(r"\*\*:\s", stripped):
            inner = stripped[2:]
            m = re.match(r"\*\*(.+?)\*\*:\s*(.*)", inner)
            if m:
                term_key = m.group(1).strip()
                zh = emap.get(term_key)
                if zh:
                    out_g.append("")
                    out_g.append(zh)
        elif stripped.startswith("**") and re.search(r"\*\*:\s", stripped) and not stripped.startswith("- "):
            m = re.match(r"\*\*(.+?)\*\*:\s*(.*)", stripped)
            if m:
                term_key = m.group(1).strip()
                zh = emap.get(term_key)
                if zh:
                    out_g.append("")
                    out_g.append(zh)
        elif stripped.startswith("- The development"):
            z = emap.get(
                "The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values."
            )
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- Pre-training"):
            z = emap.get("Pre-training Techniques")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- Fine-tuning"):
            z = emap.get("Fine-tuning Techniques")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- Alignment"):
            z = emap.get("Alignment & Safety Techniques")
            if z:
                out_g.append("")
                out_g.append(z)
        elif (
            stripped
            == "- AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks."
        ):
            z = emap.get(
                "AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks."
            )
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- **Chain of Thought"):
            z = emap.get("Chain of Thought (CoT)")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- **Tree of Thoughts"):
            z = emap.get("Tree of Thoughts (ToT)")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("**ReAct"):
            z = emap.get("ReAct (Reason and Act)")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- **Planning"):
            z = emap.get("Planning")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- **Deep Research"):
            z = emap.get("Deep Research")
            if z:
                out_g.append("")
                out_g.append(z)
        elif stripped.startswith("- **Critique Model"):
            z = emap.get("Critique Model")
            if z:
                out_g.append("")
                out_g.append(z)

    glossary_cn = "\n".join(out_g) + "\n"

    # Index of Terms section
    idx_and_after = split_mark + rest
    idx_only, prompt_rest = idx_and_after.split("## Prompt", 1)
    idx_lines = idx_only.splitlines()
    out_i = []
    for line in idx_lines:
        out_i.append(line)
        if line.strip() == "## Index of Terms":
            continue
        if line.startswith(
            "This index of terms was generated using Gemini Pro 2.5."
        ):
            out_i.append(
                "> 本术语索引使用 Gemini Pro 2.5 生成。文末附有提示与推理步骤，以展示省时价值并供学习参考。"
            )
            continue
        if line.startswith("### ") or line.strip() == "## Index of Terms":
            continue
        if not line.startswith("- "):
            continue
        sp = split_index_line(line)
        if not sp:
            continue
        term, loc = sp
        zh = ZH.get(term)
        if not zh:
            raise SystemExit(f"Missing ZH for: {term!r}")
        out_i.append(f"> {zh} — {loc}")

    index_cn = "\n".join(out_i) + "\n"

    # Prompt + reasoning: bilingual
    prompt_section = "## Prompt" + prompt_rest
    prompt_parts = prompt_section.split("## Gemini", 1)
    prompt_intro = prompt_parts[0]
    if len(prompt_parts) > 1:
        gemini_rest = "## Gemini" + prompt_parts[1]
    else:
        gemini_rest = ""

    # Simple: each non-empty paragraph in prompt_intro gets Chinese after
    def bilingual_tail(sec: str) -> str:
        lines_out = []
        paras = sec.split("\n\n")
        for p in paras:
            if not p.strip():
                continue
            lines_out.append(p)
            if p.strip().startswith(">"):
                lines_out.append(
                    "\n> 译文：你是否阅读了上述 Google 文档及其首页所列相关文档？请提取每一章的标题并打印。然后处理各章内容，并创建用于出版的详细索引：词条（标题）及指向文档中相关内容的定位符。我不要示例索引；我要完整索引，且至少包含 100 个索引词条。"
                )
            elif p.strip().startswith("#"):
                if p.strip().startswith("## Prompt"):
                    lines_out.append("\n> 以下为用于生成本术语索引的提示原文（英文保留）。\n")
            else:
                lines_out.append("\n> （说明性英文段落；与索引构建请求对应。）\n")
        return "\n\n".join(lines_out)

    # Better manual handling for Prompt section
    prompt_bilingual = """## Prompt

Below is the prompt that was utilized to create this index of terms.

> 以下为用于创建本术语索引时所使用的提示原文。

> *Do you read <https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0> and all the related documents in the first page Please extract all the titles for each chapter. and print them. Then process the content of all the individual chapters, and create a detailed index used for publishing, a list of words or phrases ('headings') and associated pointers ('locators') to where useful material relating to that heading can be found in a document or collection of documents. I don't want a sample index. I want the full index, with 100 index terms*

> 译文：你是否阅读上述 Google 文档（链接见上）及首页所列全部相关文档？请提取每一章的标题并打印。然后处理各章正文，并创建用于出版的详细索引：由词条（标题）及指向文档中相关内容的定位符组成。我不要示例索引；我要完整索引，且至少包含 100 个索引词条。

"""

    reasoning_en = gemini_rest
    reasoning_lines = []
    rparas = reasoning_en.split("\n\n")
    for p in rparas:
        if not p.strip():
            continue
        reasoning_lines.append(p)
        if p.strip() == "## Gemini 2.5: Reasoning Steps":
            reasoning_lines.append(
                "> 以下为 Gemini 2.5 在生成索引时的推理步骤（英文保留，段后附中文概要）。"
            )
            continue
        tr = translate_reasoning_paragraph(p)
        if tr:
            reasoning_lines.append(tr)

    reasoning_cn = "\n\n".join(reasoning_lines) + "\n"

    out_path.write_text(
        glossary_cn + index_cn + "\n" + prompt_bilingual + reasoning_cn,
        encoding="utf-8",
    )
    print("Wrote", out_path)


if __name__ == "__main__":
    main()
