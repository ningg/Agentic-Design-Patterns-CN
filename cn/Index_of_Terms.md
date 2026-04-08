# Glossary

## Fundamental Concepts

- **Prompt**: A prompt is the input, typically in the form of a question, instruction, or statement, that a user provides to an AI model to elicit a response. The quality and structure of the prompt heavily influence the model's output, making prompt engineering a key skill for effectively using AI.

> **提示（Prompt）：** 提示是用户提供给 AI 模型的输入，常见形式包括问题、指令或陈述等，用以引导模型作答。提示的质量与结构深刻影响输出，因此提示工程是高效运用 AI 的关键技能。

- **Context Window**: The context window is the maximum number of tokens an AI model can process at once, including both the input and its generated output. This fixed size is a critical limitation, as information outside the window is ignored, while larger windows enable more complex conversations and document analysis.

> **上下文窗口（Context Window）：** 指 AI 模型单次可处理的最大 token 总量（含输入与生成内容）。这一固定上限是关键约束：超出窗口的信息会被忽略；窗口越大，越能支撑复杂对话与长文档分析。

- **In-Context Learning**: In-context learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining. This powerful feature allows a single, general-purpose model to be adapted to countless specific tasks on the fly.

> **上下文学习（In-Context Learning）：** 指模型仅凭提示中的示例即可适应新任务，而无需重新训练。这使单一通用模型能即时适配众多具体任务。

- **Zero-Shot, One-Shot, & Few-Shot Prompting**: These are prompting techniques where a model is given zero, one, or a few examples of a task to guide its response. Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task.

> **零样本、单样本与少样本提示（Zero-Shot, One-Shot, & Few-Shot Prompting）：** 这类技术向模型提供零个、一个或少量任务示例以引导作答。一般而言，示例越多，模型越能把握用户意图，并在该任务上提升准确度。

- **Multimodality**: Multimodality is an AI's ability to understand and process information across multiple data types like text, images, and audio. This allows for more versatile and human-like interactions, such as describing an image or answering a spoken question.

> **多模态（Multimodality）：** 指 AI 理解并处理多种数据类型（如文本、图像、音频）的能力，从而支持更灵活、更接近人类的交互，例如描述图像或应答语音提问。

**Grounding**: Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG to make AI systems more trustworthy.

> **接地（Grounding）：** 将模型输出锚定到可验证的真实世界信息源，以提高事实准确性并抑制幻觉。常见做法包括 RAG 等技术，从而提升 AI 系统的可信度。

## Core AI Model Architectures

- **Transformers**: The Transformer is the foundational neural network architecture for most modern LLMs. Its key innovation is the self-attention mechanism, which efficiently processes long sequences of text and captures complex relationships between words.

> **Transformer：** 大多数现代 LLM 所依托的基础神经网络架构。其核心创新是自注意力机制，可高效处理长文本序列并捕捉词语间的复杂关联。

- **Recurrent Neural Network (RNN)**: The Recurrent Neural Network is a foundational architecture that preceded the Transformer. RNNs process information sequentially, using loops to maintain a "memory" of previous inputs, which made them suitable for tasks like text and speech processing.

> **循环神经网络（RNN）：** 早于 Transformer 的一类基础架构。RNN 顺序处理信息，借循环结构保留对先前输入的「记忆」，因而适用于文本与语音等任务。

- **Mixture of Experts (MoE)**: Mixture of Experts is an efficient model architecture where a "router" network dynamically selects a small subset of "expert" networks to handle any given input. This allows models to have a massive number of parameters while keeping computational costs manageable.

> **混合专家（MoE）：** 一种高效架构：由「路由」网络为每个输入动态挑选少数「专家」子网络。模型因此可拥有海量参数，同时把计算成本控制在可接受范围。

- **Diffusion Models**: Diffusion models are generative models that excel at creating high-quality images. They work by adding random noise to data and then training a model to meticulously reverse the process, allowing them to generate novel data from a random starting point.

> **扩散模型（Diffusion Models）：** 擅长生成高质量图像的生成式模型。思路是对数据注入随机噪声，再训练模型精细逆转该过程，从而由随机噪声生成新样本。

- **Mamba**: Mamba is a recent AI architecture using a Selective State Space Model (SSM) to process sequences with high efficiency, especially for very long contexts. Its selective mechanism allows it to focus on relevant information while filtering out noise, making it a potential alternative to the Transformer.

> **Mamba：** 较新的序列建模架构，基于选择性状态空间模型（SSM），在长上下文上尤为高效。选择性机制可聚焦相关信息、抑制噪声，有望成为 Transformer 的有力替代之一。

## The LLM Development Lifecycle

- The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values.

> 强大语言模型的开发分阶段推进：首先是**预训练（Pre-training）**，在海量通用互联网文本上训练基础模型，习得语言、推理与世界知识；继而是**微调（Fine-tuning）**，以规模较小、面向任务的数据继续训练，使能力贴合特定用途；最后是**对齐（Alignment）**，调校专用模型行为，使输出有益、无害并契合人类价值观。

- Pre-training Techniques: Pre-training is the initial phase where a model learns general knowledge from vast amounts of data. The top techniques for this involve different objectives for the model to learn from. The most common is Causal Language Modeling (CLM), where the model predicts the next word in a sentence. Another is Masked Language Modeling (MLM), where the model fills in intentionally hidden words in a text. Other important methods include Denoising Objectives, where the model learns to restore a corrupted input to its original state, Contrastive Learning, where it learns to distinguish between similar and dissimilar pieces of data, and Next Sentence Prediction (NSP), where it determines if two sentences logically follow each other.

> **预训练技术：** 预训练阶段中，模型从海量数据习得通用知识，常见训练目标包括：因果语言建模（CLM），预测下一词；掩码语言建模（MLM），恢复被故意遮盖的词；另有去噪目标（由损坏输入还原原文）、对比学习（区分相似与相异样本）、下一句预测（NSP，判断两句是否前后衔接）等。

- Fine-tuning Techniques: Fine-tuning is the process of adapting a general pre-trained model to a specific task using a smaller, specialized dataset. The most common approach is Supervised Fine-Tuning (SFT), where the model is trained on labeled examples of correct input-output pairs. A popular variant is Instruction Tuning, which focuses on training the model to better follow user commands. To make this process more efficient, Parameter-Efficient Fine-Tuning (PEFT) methods are used, with top techniques including LoRA (Low-Rank Adaptation), which only updates a small number of parameters, and its memory-optimized version, QLoRA. Another technique, Retrieval-Augmented Generation (RAG), enhances the model by connecting it to an external knowledge source during the fine-tuning or inference stage.

> **微调技术：** 以较小、专用的数据集将通用预训练模型适配到具体任务。最常见的是监督微调（SFT），使用标注的输入—输出对；常见变体是指令微调，侧重更好遵循用户指令。为提升效率可采用参数高效微调（PEFT），例如 LoRA（低秩适配）仅更新少量参数，及其内存优化版 QLoRA。检索增强生成（RAG）可在微调或推理阶段接入外部知识源以增强模型。

- Alignment & Safety Techniques: Alignment is the process of ensuring an AI model's behavior aligns with human values and expectations, making it helpful and harmless. The most prominent technique is Reinforcement Learning from Human Feedback (RLHF), where a "reward model" trained on human preferences guides the AI's learning process, often using an algorithm like Proximal Policy Optimization (PPO) for stability. Simpler alternatives have emerged, such as Direct Preference Optimization (DPO), which bypasses the need for a separate reward model, and Kahneman-Tversky Optimization (KTO), which simplifies data collection further. To ensure safe deployment, Guardrails are implemented as a final safety layer to filter outputs and block harmful actions in real-time.

> **对齐与安全：** 对齐旨在使模型行为符合人类价值观与期望，做到有益且无害。主流路径包括基于人类反馈的强化学习（RLHF），以在人类偏好上训练的「奖励模型」引导学习，常配合近端策略优化（PPO）等算法以稳定训练。更轻量的替代包括直接偏好优化（DPO，无需单独奖励模型）与 Kahneman–Tversky 优化（KTO，进一步简化偏好数据收集）。部署阶段还可借助护栏（Guardrails）作为最后防线，过滤输出并实时拦截有害行为。

## Enhancing AI Agent Capabilities

- AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.

> 智能体能够感知环境并自主行动以达成目标；其实际效果往往离不开稳健的推理框架。

- **Chain of Thought (CoT)**: This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer. This process of "thinking out loud" often leads to more accurate results on complex reasoning tasks.

> **思维链（CoT）：** 该提示技术鼓励模型在给出最终答案前逐步展开推理。这种「边想边说」的方式往往能在复杂推理任务上带来更高准确度。

- **Tree of Thoughts (ToT)**: Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously, like branches on a tree. It allows the agent to self-evaluate different lines of thought and choose the most promising one to pursue, making it more effective at complex problem-solving.

> **思维树（ToT）：** 进阶推理框架：智能体并行探索多条推理路径（如树之分叉），自我评估各条思路并择优深入，从而在复杂问题上更有效。

**ReAct (Reason and Act)**: ReAct is an agent framework that combines reasoning and acting in a loop. The agent first "thinks" about what to do, then takes an "action" using a tool, and uses the resulting observation to inform its next thought, making it highly effective at solving complex tasks.

> **ReAct（推理与行动）：** 将推理与行动纳入同一循环：智能体先「思考」下一步，再调用工具「行动」，并以观察结果驱动下一轮思考，因而在复杂任务上表现突出。

- **Planning**: This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks. The agent then creates a plan to execute these steps in order, allowing it to handle complex, multi-step assignments.

> **规划：** 智能体把高层目标拆解为一系列较小、可控的子任务，并编排执行顺序，以应对复杂、多步骤任务。

- **Deep Research**: Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions. This allows the agent to build a comprehensive understanding of a subject far beyond a single search query.

> **深度研究：** 智能体通过迭代检索、综合发现并追问新线索，自主深入某一主题，从而形成远超单次检索查询的全面理解。

- **Critique Model**: A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model. It acts as an automated critic, helping to identify errors, improve reasoning, and ensure the final output meets a desired quality standard.

> **评判模型：** 专门用于审阅、打分并对另一模型输出给出反馈的 AI 模型，扮演自动化评审角色，有助于发现错误、改进推理并使终稿满足质量要求。

## Index of Terms

This index of terms was generated using Gemini Pro 2.5. The prompt and reasoning steps are included at the end to demonstrate the time-saving benefits and for educational purposes.

> 本术语索引由 Gemini Pro 2.5 生成。文末附有原始提示与推理步骤，既便于体会其节省时间的效果，也可作为学习参考。

### A

- A/B Testing - Chapter 3: Parallelization  
  > A/B 测试 — Chapter 3: Parallelization
- Action Selection - Chapter 20: Prioritization  
  > 动作选择 — Chapter 20: Prioritization
- Adaptation - Chapter 9: Learning and Adaptation  
  > 适应 — Chapter 9: Learning and Adaptation
- Adaptive Task Allocation - Chapter 16: Resource-Aware Optimization  
  > 自适应任务分配 — Chapter 16: Resource-Aware Optimization
- Adaptive Tool Use & Selection - Chapter 16: Resource-Aware Optimization  
  > 自适应工具使用与选择 — Chapter 16: Resource-Aware Optimization
- Agent - What makes an AI system an Agent?  
  > 智能体（Agent） — What makes an AI system an Agent?
- Agent-Computer Interfaces (ACIs) - Appendix B  
  > 智能体与计算机接口（ACIs） — Appendix B
- Agent-Driven Economy - What makes an AI system an Agent?  
  > 智能体驱动的经济 — What makes an AI system an Agent?
- Agent as a Tool - Chapter 7: Multi-Agent Collaboration  
  > 作为工具的智能体 — Chapter 7: Multi-Agent Collaboration
- Agent Cards - Chapter 15: Inter-Agent Communication (A2A)  
  > 智能体卡片（Agent Cards） — Chapter 15: Inter-Agent Communication (A2A)
- Agent Development Kit (ADK) - Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C  
  > 智能体开发套件（ADK） — Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C
- Agent Discovery - Chapter 15: Inter-Agent Communication (A2A)  
  > 智能体发现 — Chapter 15: Inter-Agent Communication (A2A)
- Agent Trajectories - Chapter 19: Evaluation and Monitoring  
  > 智能体轨迹 — Chapter 19: Evaluation and Monitoring
- Agentic Design Patterns - Introduction  
  > 智能体设计模式 — Introduction
- Agentic RAG - Chapter 14: Knowledge Retrieval (RAG)  
  > 智能体化 RAG — Chapter 14: Knowledge Retrieval (RAG)
- Agentic Systems - Introduction  
  > 智能体化系统 — Introduction
- AI Co-scientist - Chapter 21: Exploration and Discovery  
  > AI 联合科学家（AI Co-scientist） — Chapter 21: Exploration and Discovery
- Alignment - Glossary  
  > 对齐（Alignment） — Glossary
- AlphaEvolve - Chapter 9: Learning and Adaptation  
  > AlphaEvolve — Chapter 9: Learning and Adaptation
- Analogies - Appendix A  
  > 类比 — Appendix A
- Anomaly Detection - Chapter 19: Evaluation and Monitoring  
  > 异常检测 — Chapter 19: Evaluation and Monitoring
- Anthropic's Claude 4 Series - Appendix B  
  > Anthropic Claude 4 系列 — Appendix B
- Anthropic's Computer Use - Appendix B  
  > Anthropic 计算机使用 — Appendix B
- API Interaction - Chapter 10: Model Context Protocol (MCP)  
  > API 交互 — Chapter 10: Model Context Protocol (MCP)
- Artifacts - Chapter 15: Inter-Agent Communication (A2A)  
  > 制品（Artifacts） — Chapter 15: Inter-Agent Communication (A2A)
- Asynchronous Polling - Chapter 15: Inter-Agent Communication (A2A)  
  > 异步轮询 — Chapter 15: Inter-Agent Communication (A2A)
- Audit Logs - Chapter 15: Inter-Agent Communication (A2A)  
  > 审计日志 — Chapter 15: Inter-Agent Communication (A2A)
- Automated Metrics - Chapter 19: Evaluation and Monitoring  
  > 自动化指标 — Chapter 19: Evaluation and Monitoring
- Automatic Prompt Engineering (APE) - Appendix A  
  > 自动提示工程（APE） — Appendix A
- Autonomy - Introduction  
  > 自主性 — Introduction
- A2A (Agent-to-Agent) - Chapter 15: Inter-Agent Communication (A2A)
  > 智能体到智能体（A2A） — Chapter 15: Inter-Agent Communication (A2A)

### B

- Behavioral Constraints - Chapter 18: Guardrails/Safety Patterns  
  > 行为约束 — Chapter 18: Guardrails/Safety Patterns
- Browser Use - Appendix B
  > 浏览器使用 — Appendix B

### C

- Callbacks - Chapter 18: Guardrails/Safety Patterns  
  > 回调 — Chapter 18: Guardrails/Safety Patterns
- Causal Language Modeling (CLM) - Glossary  
  > 因果语言建模（CLM） — Glossary
- Chain of Debates (CoD) - Chapter 17: Reasoning Techniques  
  > 辩论链（CoD） — Chapter 17: Reasoning Techniques
- Chain-of-Thought (CoT) - Chapter 17: Reasoning Techniques, Appendix A  
  > 思维链（CoT） — Chapter 17: Reasoning Techniques, Appendix A
- Chatbots - Chapter 8: Memory Management  
  > 聊天机器人 — Chapter 8: Memory Management
- ChatMessageHistory - Chapter 8: Memory Management  
  > 聊天消息历史（ChatMessageHistory） — Chapter 8: Memory Management
- Checkpoint and Rollback - Chapter 18: Guardrails/Safety Patterns  
  > 检查点与回滚 — Chapter 18: Guardrails/Safety Patterns
- Chunking - Chapter 14: Knowledge Retrieval (RAG)  
  > 分块 — Chapter 14: Knowledge Retrieval (RAG)
- Clarity and Specificity - Appendix A  
  > 清晰与具体 — Appendix A
- Client Agent - Chapter 15: Inter-Agent Communication (A2A)  
  > 客户端智能体 — Chapter 15: Inter-Agent Communication (A2A)
- Code Generation - Chapter 1: Prompt Chaining, Chapter 4: Reflection  
  > 代码生成 — Chapter 1: Prompt Chaining, Chapter 4: Reflection
- Code Prompting - Appendix A  
  > 代码提示 — Appendix A
- CoD (Chain of Debates) - Chapter 17: Reasoning Techniques  
  > 辩论链（CoD） — Chapter 17: Reasoning Techniques
- CoT (Chain of Thought) - Chapter 17: Reasoning Techniques, Appendix A  
  > 思维链（CoT） — Chapter 17: Reasoning Techniques, Appendix A
- Collaboration - Chapter 7: Multi-Agent Collaboration  
  > 协作 — Chapter 7: Multi-Agent Collaboration
- Compliance - Chapter 19: Evaluation and Monitoring  
  > 合规 — Chapter 19: Evaluation and Monitoring
- Conciseness - Appendix A  
  > 简洁性 — Appendix A
- Content Generation - Chapter 1: Prompt Chaining, Chapter 4: Reflection  
  > 内容生成 — Chapter 1: Prompt Chaining, Chapter 4: Reflection
- Context Engineering - Chapter 1: Prompt Chaining  
  > 上下文工程 — Chapter 1: Prompt Chaining
- Context Window - Glossary  
  > 上下文窗口 — Glossary
- Contextual Pruning & Summarization - Chapter 16: Resource-Aware Optimization  
  > 上下文剪枝与摘要 — Chapter 16: Resource-Aware Optimization
- Contextual Prompting - Appendix A  
  > 上下文提示 — Appendix A
- Contractor Model - Chapter 19: Evaluation and Monitoring  
  > 承包方模型（Contractor Model） — Chapter 19: Evaluation and Monitoring
- ConversationBufferMemory - Chapter 8: Memory Management  
  > 会话缓冲记忆（ConversationBufferMemory） — Chapter 8: Memory Management
- Conversational Agents - Chapter 1: Prompt Chaining, Chapter 4: Reflection  
  > 对话式智能体 — Chapter 1: Prompt Chaining, Chapter 4: Reflection
- Cost-Sensitive Exploration - Chapter 16: Resource-Aware Optimization  
  > 代价敏感探索 — Chapter 16: Resource-Aware Optimization
- CrewAI - Chapter 3: Parallelization, Chapter 5: Tool Use, Chapter 6: Planning, Chapter 7: Multi-Agent Collaboration, Chapter 18: Guardrails/Safety Patterns, Appendix C  
  > CrewAI — Chapter 3: Parallelization, Chapter 5: Tool Use, Chapter 6: Planning, Chapter 7: Multi-Agent Collaboration, Chapter 18: Guardrails/Safety Patterns, Appendix C
- Critique Agent - Chapter 16: Resource-Aware Optimization  
  > 评判智能体 — Chapter 16: Resource-Aware Optimization
- Critique Model - Glossary  
  > 评判模型 — Glossary
- Customer Support - Chapter 13: Human-in-the-Loop
  > 客户支持 — Chapter 13: Human-in-the-Loop

### D

- Data Extraction - Chapter 1: Prompt Chaining  
  > 数据抽取 — Chapter 1: Prompt Chaining
- Data Labeling - Chapter 13: Human-in-the-Loop  
  > 数据标注 — Chapter 13: Human-in-the-Loop
- Database Integration - Chapter 10: Model Context Protocol (MCP)  
  > 数据库集成 — Chapter 10: Model Context Protocol (MCP)
- DatabaseSessionService - Chapter 8: Memory Management  
  > 数据库会话服务（DatabaseSessionService） — Chapter 8: Memory Management
- Debate and Consensus - Chapter 7: Multi-Agent Collaboration  
  > 辩论与共识 — Chapter 7: Multi-Agent Collaboration
- Decision Augmentation - Chapter 13: Human-in-the-Loop  
  > 决策增强 — Chapter 13: Human-in-the-Loop
- Decomposition - Appendix A  
  > 分解 — Appendix A
- Deep Research - Chapter 6: Planning, Chapter 17: Reasoning Techniques, Glossary  
  > 深度研究 — Chapter 6: Planning, Chapter 17: Reasoning Techniques, Glossary
- Delimiters - Appendix A  
  > 分隔符 — Appendix A
- Denoising Objectives - Glossary  
  > 去噪目标 — Glossary
- Dependencies - Chapter 20: Prioritization  
  > 依赖 — Chapter 20: Prioritization
- Diffusion Models - Glossary  
  > 扩散模型 — Glossary
- Direct Preference Optimization (DPO) - Chapter 9: Learning and Adaptation  
  > 直接偏好优化（DPO） — Chapter 9: Learning and Adaptation
- Discoverability - Chapter 10: Model Context Protocol (MCP)  
  > 可发现性 — Chapter 10: Model Context Protocol (MCP)
- Drift Detection - Chapter 19: Evaluation and Monitoring  
  > 漂移检测 — Chapter 19: Evaluation and Monitoring
- Dynamic Model Switching - Chapter 16: Resource-Aware Optimization  
  > 动态模型切换 — Chapter 16: Resource-Aware Optimization
- Dynamic Re-prioritization - Chapter 20: Prioritization
  > 动态重排优先级 — Chapter 20: Prioritization

### E

- Embeddings - Chapter 14: Knowledge Retrieval (RAG)  
  > 嵌入 — Chapter 14: Knowledge Retrieval (RAG)
- Embodiment - What makes an AI system an Agent?  
  > 具身 — What makes an AI system an Agent?
- Energy-Efficient Deployment - Chapter 16: Resource-Aware Optimization  
  > 高能效部署 — Chapter 16: Resource-Aware Optimization
- Episodic Memory - Chapter 8: Memory Management  
  > 情景记忆 — Chapter 8: Memory Management
- Error Detection - Chapter 12: Exception Handling and Recovery  
  > 错误检测 — Chapter 12: Exception Handling and Recovery
- Error Handling - Chapter 12: Exception Handling and Recovery  
  > 错误处理 — Chapter 12: Exception Handling and Recovery
- Escalation Policies - Chapter 13: Human-in-the-Loop  
  > 升级策略 — Chapter 13: Human-in-the-Loop
- Evaluation - Chapter 19: Evaluation and Monitoring  
  > 评估 — Chapter 19: Evaluation and Monitoring
- Exception Handling - Chapter 12: Exception Handling and Recovery  
  > 异常处理 — Chapter 12: Exception Handling and Recovery
- Expert Teams - Chapter 7: Multi-Agent Collaboration  
  > 专家团队 — Chapter 7: Multi-Agent Collaboration
- Exploration and Discovery - Chapter 21: Exploration and Discovery  
  > 探索与发现 — Chapter 21: Exploration and Discovery
- External Moderation APIs - Chapter 18: Guardrails/Safety Patterns
  > 外部审核 API — Chapter 18: Guardrails/Safety Patterns

### F

- Factored Cognition - Appendix A  
  > 因子化认知（Factored Cognition） — Appendix A
- FastMCP - Chapter 10: Model Context Protocol (MCP)  
  > FastMCP — Chapter 10: Model Context Protocol (MCP)
- Fault Tolerance - Chapter 18: Guardrails/Safety Patterns  
  > 容错 — Chapter 18: Guardrails/Safety Patterns
- Few-Shot Learning - Chapter 9: Learning and Adaptation  
  > 少样本学习 — Chapter 9: Learning and Adaptation
- Few-Shot Prompting - Appendix A  
  > 少样本提示 — Appendix A
- Fine-tuning - Glossary  
  > 微调 — Glossary
- Formalized Contract - Chapter 19: Evaluation and Monitoring  
  > 形式化合约 — Chapter 19: Evaluation and Monitoring
- Function Calling - Chapter 5: Tool Use, Appendix A
  > 函数调用 — Chapter 5: Tool Use, Appendix A

### G

- Gemini Live - Appendix B  
  > Gemini Live — Appendix B
- Gems - Appendix A  
  > Gems — Appendix A
- Generative Media Orchestration - Chapter 10: Model Context Protocol (MCP)  
  > 生成式媒体编排 — Chapter 10: Model Context Protocol (MCP)
- Goal Setting - Chapter 11: Goal Setting and Monitoring  
  > 目标设定 — Chapter 11: Goal Setting and Monitoring
- GoD (Graph of Debates) - Chapter 17: Reasoning Techniques  
  > 辩论图（GoD） — Chapter 17: Reasoning Techniques
- Google Agent Development Kit (ADK) - Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C  
  > Google 智能体开发套件（ADK） — Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 7: Multi-Agent Collaboration, Chapter 8: Memory Management, Chapter 12: Exception Handling and Recovery, Chapter 13: Human-in-the-Loop, Chapter 15: Inter-Agent Communication (A2A), Chapter 16: Resource-Aware Optimization, Chapter 19: Evaluation and Monitoring, Appendix C
- Google Co-Scientist - Chapter 21: Exploration and Discovery  
  > Google Co-Scientist — Chapter 21: Exploration and Discovery
- Google DeepResearch - Chapter 6: Planning  
  > Google DeepResearch — Chapter 6: Planning
- Google Project Mariner - Appendix B  
  > Google Project Mariner — Appendix B
- Graceful Degradation - Chapter 12: Exception Handling and Recovery, Chapter 16: Resource-Aware Optimization  
  > 优雅降级 — Chapter 12: Exception Handling and Recovery, Chapter 16: Resource-Aware Optimization
- Graph of Debates (GoD) - Chapter 17: Reasoning Techniques  
  > 辩论图（GoD） — Chapter 17: Reasoning Techniques
- Grounding - Glossary  
  > 接地（Grounding） — Glossary
- Guardrails - Chapter 18: Guardrails/Safety Patterns
  > 护栏（Guardrails） — Chapter 18: Guardrails/Safety Patterns

### H

- Haystack - Appendix C  
  > Haystack — Appendix C
- Hierarchical Decomposition - Chapter 19: Evaluation and Monitoring  
  > 层次分解 — Chapter 19: Evaluation and Monitoring
- Hierarchical Structures - Chapter 7: Multi-Agent Collaboration  
  > 层次结构 — Chapter 7: Multi-Agent Collaboration
- HITL (Human-in-the-Loop) - Chapter 13: Human-in-the-Loop  
  > 人在回路中（HITL） — Chapter 13: Human-in-the-Loop
- Human-in-the-Loop (HITL) - Chapter 13: Human-in-the-Loop  
  > 人在回路中（HITL） — Chapter 13: Human-in-the-Loop
- Human-on-the-loop - Chapter 13: Human-in-the-Loop  
  > 人在环上（Human-on-the-loop） — Chapter 13: Human-in-the-Loop
- Human Oversight - Chapter 13: Human-in-the-Loop, Chapter 18: Guardrails/Safety Patterns
  > 人类监督 — Chapter 13: Human-in-the-Loop, Chapter 18: Guardrails/Safety Patterns

### I

- In-Context Learning - Glossary  
  > 上下文学习 — Glossary
- InMemoryMemoryService - Chapter 8: Memory Management  
  > 内存记忆服务（InMemoryMemoryService） — Chapter 8: Memory Management
- InMemorySessionService - Chapter 8: Memory Management  
  > 内存会话服务（InMemorySessionService） — Chapter 8: Memory Management
- Input Validation/Sanitization - Chapter 18: Guardrails/Safety Patterns  
  > 输入校验/净化 — Chapter 18: Guardrails/Safety Patterns
- Instructions Over Constraints - Appendix A  
  > 指令优于约束 — Appendix A
- Inter-Agent Communication (A2A) - Chapter 15: Inter-Agent Communication (A2A)  
  > 智能体间通信（A2A） — Chapter 15: Inter-Agent Communication (A2A)
- Intervention and Correction - Chapter 13: Human-in-the-Loop  
  > 干预与纠正 — Chapter 13: Human-in-the-Loop
- IoT Device Control - Chapter 10: Model Context Protocol (MCP)  
  > 物联网设备控制 — Chapter 10: Model Context Protocol (MCP)
- Iterative Prompting / Refinement - Appendix A
  > 迭代式提示与精炼 — Appendix A

### J

- Jailbreaking - Chapter 18: Guardrails/Safety Patterns
  > 越狱攻击 — Chapter 18: Guardrails/Safety Patterns

### K

- Kahneman-Tversky Optimization (KTO) - Glossary  
  > Kahneman–Tversky 优化（KTO） — Glossary
- Knowledge Retrieval (RAG) - Chapter 14: Knowledge Retrieval (RAG)
  > 知识检索（RAG） — Chapter 14: Knowledge Retrieval (RAG)

### L

- LangChain - Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Chapter 20: Prioritization, Appendix C  
  > LangChain — Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Chapter 20: Prioritization, Appendix C
- LangGraph - Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Appendix C  
  > LangGraph — Chapter 1: Prompt Chaining, Chapter 2: Routing, Chapter 3: Parallelization, Chapter 4: Reflection, Chapter 5: Tool Use, Chapter 8: Memory Management, Appendix C
- Latency Monitoring - Chapter 19: Evaluation and Monitoring  
  > 延迟监控 — Chapter 19: Evaluation and Monitoring
- Learned Resource Allocation Policies - Chapter 16: Resource-Aware Optimization  
  > 基于学习的资源分配策略 — Chapter 16: Resource-Aware Optimization
- Learning and Adaptation - Chapter 9: Learning and Adaptation  
  > 学习与适应 — Chapter 9: Learning and Adaptation
- LLM-as-a-Judge - Chapter 19: Evaluation and Monitoring  
  > 以 LLM 为评判者（LLM-as-a-Judge） — Chapter 19: Evaluation and Monitoring
- LlamaIndex - Appendix C  
  > LlamaIndex — Appendix C
- LoRA (Low-Rank Adaptation) - Glossary  
  > LoRA（低秩适配） — Glossary
- Low-Rank Adaptation (LoRA) - Glossary
  > 低秩适配（LoRA） — Glossary

### M

- Mamba - Glossary  
  > Mamba — Glossary
- Masked Language Modeling (MLM) - Glossary  
  > 掩码语言建模（MLM） — Glossary
- MASS (Multi-Agent System Search) - Chapter 17: Reasoning Techniques  
  > 多智能体系统搜索（MASS） — Chapter 17: Reasoning Techniques
- MCP (Model Context Protocol) - Chapter 10: Model Context Protocol (MCP)  
  > 模型上下文协议（MCP） — Chapter 10: Model Context Protocol (MCP)
- Memory Management - Chapter 8: Memory Management  
  > 记忆管理 — Chapter 8: Memory Management
- Memory-Based Learning - Chapter 9: Learning and Adaptation  
  > 基于记忆的学习 — Chapter 9: Learning and Adaptation
- MetaGPT - Appendix C  
  > MetaGPT — Appendix C
- Microsoft AutoGen - Appendix C  
  > Microsoft AutoGen — Appendix C
- Mixture of Experts (MoE) - Glossary  
  > 混合专家（MoE） — Glossary
- Model Context Protocol (MCP) - Chapter 10: Model Context Protocol (MCP)  
  > 模型上下文协议（MCP） — Chapter 10: Model Context Protocol (MCP)
- Modularity - Chapter 18: Guardrails/Safety Patterns  
  > 模块化 — Chapter 18: Guardrails/Safety Patterns
- Monitoring - Chapter 11: Goal Setting and Monitoring, Chapter 19: Evaluation and Monitoring  
  > 监控 — Chapter 11: Goal Setting and Monitoring, Chapter 19: Evaluation and Monitoring
- Multi-Agent Collaboration - Chapter 7: Multi-Agent Collaboration  
  > 多智能体协作 — Chapter 7: Multi-Agent Collaboration
- Multi-Agent System Search (MASS) - Chapter 17: Reasoning Techniques  
  > 多智能体系统搜索（MASS） — Chapter 17: Reasoning Techniques
- Multimodality - Glossary  
  > 多模态 — Glossary
- Multimodal Prompting - Appendix A
  > 多模态提示 — Appendix A

### N

- Negative Examples - Appendix A  
  > 负例 — Appendix A
- Next Sentence Prediction (NSP) - Glossary
  > 下一句预测（NSP） — Glossary

### O

- Observability - Chapter 18: Guardrails/Safety Patterns  
  > 可观测性 — Chapter 18: Guardrails/Safety Patterns
- One-Shot Prompting - Appendix A  
  > 单样本提示 — Appendix A
- Online Learning - Chapter 9: Learning and Adaptation  
  > 在线学习 — Chapter 9: Learning and Adaptation
- OpenAI Deep Research API - Chapter 6: Planning  
  > OpenAI Deep Research API — Chapter 6: Planning
- OpenEvolve - Chapter 9: Learning and Adaptation  
  > OpenEvolve — Chapter 9: Learning and Adaptation
- OpenRouter - Chapter 16: Resource-Aware Optimization  
  > OpenRouter — Chapter 16: Resource-Aware Optimization
- Output Filtering/Post-processing - Chapter 18: Guardrails/Safety Patterns
  > 输出过滤/后处理 — Chapter 18: Guardrails/Safety Patterns

### P

- PAL (Program-Aided Language Models) - Chapter 17: Reasoning Techniques  
  > 程序辅助语言模型（PAL） — Chapter 17: Reasoning Techniques
- Parallelization - Chapter 3: Parallelization  
  > 并行化 — Chapter 3: Parallelization
- Parallelization & Distributed Computing Awareness - Chapter 16: Resource-Aware Optimization  
  > 并行化与分布式计算认知 — Chapter 16: Resource-Aware Optimization
- Parameter-Efficient Fine-Tuning (PEFT) - Glossary  
  > 参数高效微调（PEFT） — Glossary
- PEFT (Parameter-Efficient Fine-Tuning) - Glossary  
  > 参数高效微调（PEFT） — Glossary
- Performance Tracking - Chapter 19: Evaluation and Monitoring  
  > 性能跟踪 — Chapter 19: Evaluation and Monitoring
- Persona Pattern - Appendix A  
  > 人设模式 — Appendix A
- Personalization - What makes an AI system an Agent?  
  > 个性化 — What makes an AI system an Agent?
- Planning - Chapter 6: Planning, Glossary  
  > 规划 — Chapter 6: Planning, Glossary
- Prioritization - Chapter 20: Prioritization  
  > 优先级排序 — Chapter 20: Prioritization
- Principle of Least Privilege - Chapter 18: Guardrails/Safety Patterns  
  > 最小权限原则 — Chapter 18: Guardrails/Safety Patterns
- Proactive Resource Prediction - Chapter 16: Resource-Aware Optimization  
  > 主动资源预测 — Chapter 16: Resource-Aware Optimization
- Procedural Memory - Chapter 8: Memory Management  
  > 程序性记忆 — Chapter 8: Memory Management
- Program-Aided Language Models (PAL) - Chapter 17: Reasoning Techniques  
  > 程序辅助语言模型（PAL） — Chapter 17: Reasoning Techniques
- Project Astra - Appendix B  
  > Project Astra — Appendix B
- Prompt - Glossary  
  > 提示（Prompt） — Glossary
- Prompt Chaining - Chapter 1: Prompt Chaining  
  > 提示链 — Chapter 1: Prompt Chaining
- Prompt Engineering - Appendix A  
  > 提示工程 — Appendix A
- Proximal Policy Optimization (PPO) - Chapter 9: Learning and Adaptation  
  > 近端策略优化（PPO） — Chapter 9: Learning and Adaptation
- Push Notifications - Chapter 15: Inter-Agent Communication (A2A)
  > 推送通知 — Chapter 15: Inter-Agent Communication (A2A)

### Q

- QLoRA - Glossary  
  > QLoRA — Glossary
- Quality-Focused Iterative Execution - Chapter 19: Evaluation and Monitoring
  > 质量导向的迭代执行 — Chapter 19: Evaluation and Monitoring

### R

- RAG (Retrieval-Augmented Generation) - Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A  
  > 检索增强生成（RAG） — Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A
- ReAct (Reason and Act) - Chapter 17: Reasoning Techniques, Appendix A, Glossary  
  > ReAct（推理与行动） — Chapter 17: Reasoning Techniques, Appendix A, Glossary
- Reasoning - Chapter 17: Reasoning Techniques  
  > 推理 — Chapter 17: Reasoning Techniques
- Reasoning-Based Information Extraction - Chapter 10: Model Context Protocol (MCP)  
  > 基于推理的信息抽取 — Chapter 10: Model Context Protocol (MCP)
- Recovery - Chapter 12: Exception Handling and Recovery  
  > 恢复 — Chapter 12: Exception Handling and Recovery
- Recurrent Neural Network (RNN) - Glossary  
  > 循环神经网络（RNN） — Glossary
- Reflection - Chapter 4: Reflection  
  > 反思 — Chapter 4: Reflection
- Reinforcement Learning - Chapter 9: Learning and Adaptation  
  > 强化学习 — Chapter 9: Learning and Adaptation
- Reinforcement Learning from Human Feedback (RLHF) - Glossary  
  > 基于人类反馈的强化学习（RLHF） — Glossary
- Reinforcement Learning with Verifiable Rewards (RLVR) - Chapter 17: Reasoning Techniques  
  > 可验证奖励的强化学习（RLVR） — Chapter 17: Reasoning Techniques
- Remote Agent - Chapter 15: Inter-Agent Communication (A2A)  
  > 远程智能体 — Chapter 15: Inter-Agent Communication (A2A)
- Request/Response (Polling) - Chapter 15: Inter-Agent Communication (A2A)  
  > 请求/响应（轮询） — Chapter 15: Inter-Agent Communication (A2A)
- Resource-Aware Optimization - Chapter 16: Resource-Aware Optimization  
  > 资源感知优化 — Chapter 16: Resource-Aware Optimization
- Retrieval-Augmented Generation (RAG) - Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A  
  > 检索增强生成（RAG） — Chapter 8: Memory Management, Chapter 14: Knowledge Retrieval (RAG), Appendix A
- RLHF (Reinforcement Learning from Human Feedback) - Glossary  
  > RLHF（基于人类反馈的强化学习） — Glossary
- RLVR (Reinforcement Learning with Verifiable Rewards) - Chapter 17: Reasoning Techniques  
  > RLVR（可验证奖励的强化学习） — Chapter 17: Reasoning Techniques
- RNN (Recurrent Neural Network) - Glossary  
  > RNN（循环神经网络） — Glossary
- Role Prompting - Appendix A  
  > 角色提示 — Appendix A
- Router Agent - Chapter 16: Resource-Aware Optimization  
  > 路由智能体 — Chapter 16: Resource-Aware Optimization
- Routing - Chapter 2: Routing
  > 路由 — Chapter 2: Routing

### S

- Safety - Chapter 18: Guardrails/Safety Patterns  
  > 安全 — Chapter 18: Guardrails/Safety Patterns
- Scaling Inference Law - Chapter 17: Reasoning Techniques  
  > 推理扩展律（Scaling Inference Law） — Chapter 17: Reasoning Techniques
- Scheduling - Chapter 20: Prioritization  
  > 调度 — Chapter 20: Prioritization
- Self-Consistency - Appendix A  
  > 自洽性 — Appendix A
- Self-Correction - Chapter 4: Reflection, Chapter 17: Reasoning Techniques  
  > 自校正 — Chapter 4: Reflection, Chapter 17: Reasoning Techniques
- Self-Improving Coding Agent (SICA) - Chapter 9: Learning and Adaptation  
  > 自改进编程智能体（SICA） — Chapter 9: Learning and Adaptation
- Self-Refinement - Chapter 17: Reasoning Techniques  
  > 自精炼 — Chapter 17: Reasoning Techniques
- Semantic Kernel - Appendix C  
  > Semantic Kernel — Appendix C
- Semantic Memory - Chapter 8: Memory Management  
  > 语义记忆 — Chapter 8: Memory Management
- Semantic Similarity - Chapter 14: Knowledge Retrieval (RAG)  
  > 语义相似度 — Chapter 14: Knowledge Retrieval (RAG)
- Separation of Concerns - Chapter 18: Guardrails/Safety Patterns  
  > 关注点分离 — Chapter 18: Guardrails/Safety Patterns
- Sequential Handoffs - Chapter 7: Multi-Agent Collaboration  
  > 顺序交接 — Chapter 7: Multi-Agent Collaboration
- Server-Sent Events (SSE) - Chapter 15: Inter-Agent Communication (A2A)  
  > 服务器推送事件（SSE） — Chapter 15: Inter-Agent Communication (A2A)
- Session - Chapter 8: Memory Management  
  > 会话 — Chapter 8: Memory Management
- SICA (Self-Improving Coding Agent) - Chapter 9: Learning and Adaptation  
  > SICA（自改进编程智能体） — Chapter 9: Learning and Adaptation
- SMART Goals - Chapter 11: Goal Setting and Monitoring  
  > SMART 目标 — Chapter 11: Goal Setting and Monitoring
- State - Chapter 8: Memory Management  
  > 状态 — Chapter 8: Memory Management
- State Rollback - Chapter 12: Exception Handling and Recovery  
  > 状态回滚 — Chapter 12: Exception Handling and Recovery
- Step-Back Prompting - Appendix A  
  > 退一步提示（Step-Back Prompting） — Appendix A
- Streaming Updates - Chapter 15: Inter-Agent Communication (A2A)  
  > 流式更新 — Chapter 15: Inter-Agent Communication (A2A)
- Structured Logging - Chapter 18: Guardrails/Safety Patterns  
  > 结构化日志 — Chapter 18: Guardrails/Safety Patterns
- Structured Output - Chapter 1: Prompt Chaining, Appendix A  
  > 结构化输出 — Chapter 1: Prompt Chaining, Appendix A
- SuperAGI - Appendix C  
  > SuperAGI — Appendix C
- Supervised Fine-Tuning (SFT) - Glossary  
  > 监督微调（SFT） — Glossary
- Supervised Learning - Chapter 9: Learning and Adaptation  
  > 监督学习 — Chapter 9: Learning and Adaptation
- System Prompting - Appendix A
  > 系统提示 — Appendix A

### T

- Task Evaluation - Chapter 20: Prioritization  
  > 任务评估 — Chapter 20: Prioritization
- Text Similarity - Chapter 14: Knowledge Retrieval (RAG)  
  > 文本相似度 — Chapter 14: Knowledge Retrieval (RAG)
- Token Usage - Chapter 19: Evaluation and Monitoring  
  > Token 用量 — Chapter 19: Evaluation and Monitoring
- Tool Use - Chapter 5: Tool Use, Appendix A  
  > 工具使用 — Chapter 5: Tool Use, Appendix A
- Tool Use Restrictions - Chapter 18: Guardrails/Safety Patterns  
  > 工具使用限制 — Chapter 18: Guardrails/Safety Patterns
- ToT (Tree of Thoughts) - Chapter 17: Reasoning Techniques, Appendix A, Glossary  
  > 思维树（ToT） — Chapter 17: Reasoning Techniques, Appendix A, Glossary
- Transformers - Glossary  
  > Transformer — Glossary
- Tree of Thoughts (ToT) - Chapter 17: Reasoning Techniques, Appendix A, Glossary
  > 思维树（ToT） — Chapter 17: Reasoning Techniques, Appendix A, Glossary

### U

- Unsupervised Learning - Chapter 9: Learning and Adaptation  
  > 无监督学习 — Chapter 9: Learning and Adaptation
- User Persona - Appendix A
  > 用户人设 — Appendix A

### V

- Validation - Chapter 3: Parallelization  
  > 验证 — Chapter 3: Parallelization
- Vector Search - Chapter 14: Knowledge Retrieval (RAG)  
  > 向量检索 — Chapter 14: Knowledge Retrieval (RAG)
- VertexAiRagMemoryService - Chapter 8: Memory Management  
  > VertexAiRagMemoryService — Chapter 8: Memory Management
- VertexAiSessionService - Chapter 8: Memory Management  
  > VertexAiSessionService — Chapter 8: Memory Management
- Vibe Coding - Appendix B  
  > Vibe Coding — Appendix B
- Visual Perception - Appendix B
  > 视觉感知 — Appendix B

### W

- Webhooks - Chapter 15: Inter-Agent Communication (A2A)
  > Webhooks — Chapter 15: Inter-Agent Communication (A2A)

### Z

- Zero-Shot Learning - Chapter 9: Learning and Adaptation  
  > 零样本学习 — Chapter 9: Learning and Adaptation
- Zero-Shot Prompting - Appendix A
  > 零样本提示 — Appendix A

## Prompt

Below is the prompt that was utilized to create this index of terms.

> 以下为生成本术语索引时所使用的原始提示。

> *Do you read [https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0) and all the related documents in the first page Please extract all the titles for each chapter. and print them. Then process the content of all the individual chapters, and create a detailed index used for publishing, a list of words or phrases ('headings') and associated pointers ('locators') to where useful material relating to that heading can be found in a document or collection of documents. I don't want a sample index. I want the full index, with 100 index terms*

> **译文：** 请阅读上述 Google 文档（链接见上）及首页所列全部关联文档；提取各章标题并列出。随后通读各章正文，编制可供出版的详细索引：每个词条（heading）配以定位符（locator），指向相关内容所在位置。不要示例索引；需要完整索引，且至少包含 100 个索引词条。

## Gemini 2.5: Reasoning Steps

> 以下为 Gemini 2.5 生成该索引时的推理步骤（保留英文原文，并在段后附中文提要）。

### Beginning Index Creation

I've initiated the process by reading the Google Doc provided. Currently, I'm focusing on understanding the user's request: extracting chapter titles to build a detailed index. I'm carefully reviewing the document, looking for clear structural elements that would indicate chapter breaks. I'm hoping to identify consistent formatting or keywords that will guide the indexing process.

> 已打开主 Google 文档，并把握「提取章标题、构建详细索引」这一核心需求。

### Defining Index Extraction Process

I'm now fully immersed in the task. I've broken down the user's request into actionable steps. My initial focus is using Workspaces to access the main Google Doc. Following this, I'll parse the document to locate and retrieve related documents, which will also be accessed using the same tool. Finally, I will extract all chapter titles from all the documents, and create a comprehensive index. I've planned the detailed process.

> 已将用户需求拆解为可执行步骤，计划通过 Workspaces 访问主文档，并进一步解析相关联的文档。

### Refining the Extraction Strategy

The user's instructions are clear: read a Google Doc, its related documents, and build a detailed index of chapter titles. I've devised a multi-step plan. First, Workspaces will access the main Google Doc. Then, I'll parse it to find and read related documents, also using Workspaces. I'm now focusing on extracting titles and forming the detailed index with the required terms. I'm prioritizing accuracy to meet the user's specific demands for a comprehensive index.

> 已形成多步流程：访问主 Google 文档 → 解析并读取关联文档 → 提取标题并编制满足词条数量要求的索引。

#### 1 . Establish user intent:

I've determined the user wants a chapter title list and comprehensive index from the Google Doc and related documents. Now I need to figure out the most effective method for this extraction and indexing process. I'm exploring potential API functionalities to streamline this task, and will need to assess the best strategy for handling different document structures.

> 交付物已明确为章标题列表与全面索引；正在评估可用 API 能力及不同文档结构下的提取与索引策略。

#### 2. Considering Tool Use

I've extracted the chapter URLs from the main document using a regular expression. Now, I'm ready to utilize Workspaces to retrieve the actual content of each chapter. Once I have the text for each chapter, I'll proceed with indexing.

> 已用正则从主文档提取各章 URL，准备通过 Workspaces 拉取正文以支撑索引编制。

### Accessing chapter content:

I've successfully identified the URLs for each chapter from the main document, which I can now use with Workspaces. My next step is to retrieve the content from these URLs, which will then allow me to generate the index. I'm focusing on efficiency, aiming to process this information quickly.

> 各章 URL 已就绪；下一步经 Workspaces 抓取正文以生成索引，并兼顾处理效率。

### Fetching Chapter Content

I've successfully identified the chapter URLs from the main document and am ready to utilize Workspaces. My plan involves extracting these URLs, batching the calls for efficiency, and then processing the retrieved content to create the desired index. This ensures all relevant information is captured, paving the way for a comprehensive and accurate result.

> 主文档中的章级 URL 已锁定；拟批量请求并整合正文，以生成完整、准确的索引。

### Initiating URL Retrieval

I've now successfully extracted the chapter URLs from the main document. Currently, I'm setting up calls to the Workspaces tool, preparing to fetch the content of each chapter. The goal is to obtain the necessary text for indexing. This information will then facilitate the creation of the index with at least 100 terms as requested.

> 主文档中的章 URL 已全部提取；正在配置 Workspaces 抓取各章全文，为编制至少含 100 个词条的索引准备语料。

### Initiating Chapter Extraction

I've successfully identified and extracted the chapter URLs from the main document, which I've included above. I am now proceeding to use Workspaces for each URL to obtain the chapter content. The goal is to obtain the necessary text for indexing. This information will then facilitate the creation of the index with at least 100 terms as requested. I've begun to retrieve this information.

> 已按 URL 逐章调用 Workspaces 获取正文，并开始汇总文本以满足索引规模要求。

### Orchestrating Chapter Retrieval

I've extracted the chapter URLs and initiated a call to Workspaces. I'm currently retrieving the content for each chapter. To ensure a smooth process, I'm batching the calls to prevent any rate-limiting issues. This should enable me to efficiently compile the text needed for the index.

> 已发起 Workspaces 调用；正分批拉取各章内容以规避限流，并汇总文本供编制索引。

### Decoding User Request

I've determined the user's need. They require two primary deliverables: first, a comprehensive list of chapter titles extracted from Google Docs, and second, a detailed index containing a minimum of one hundred key terms. The process of extracting titles seems straightforward, while curating the index will involve more nuanced analysis.

> 需求已拆解：一要罗列 Google 文档中的完整章标题，二要编制至少含一百个关键术语的详细索引；前者较直接，后者需更细的内容取舍与归类。

### Extracting Titles and Indexing

I've successfully identified the user's need: extracting chapter titles from the provided documents and compiling a comprehensive index. I've fetched the content of 31 Google Docs, including the main document and its chapters. I've confirmed that no additional tools are needed. My plan involves two steps: first, extracting chapter titles from the document filenames, and second, meticulously processing the text to build the index with key terms and chapter locators.

> 需求已确认：基于所供文档提取章标题并编制全面索引；已拉取 31 份 Google 文档正文且无需额外工具；拟先据文件名提取章题，再精读正文并配以章节定位符。

### Developing an Extraction Plan

I've refined my approach to tackle the user's request. I've now formulated a precise plan. Firstly, I will compile the chapter titles from the filenames of the 31 fetched documents. Secondly, and more complexly, I will meticulously analyze the content to create a comprehensive, alphabetically ordered index exceeding 100 entries. I have finalized my extraction and indexing strategy and can now commence execution.

> 方案已细化：先依据已抓取的 31 份文档文件名汇总章节标题，再分析正文生成按字母排序、超过 100 条的完整索引；策略已明确，可进入执行阶段。

### Crafting the Extraction Strategy

My approach is well-defined. I will compile chapter titles from the filenames of the 31 fetched documents. Subsequently, I'll analyze the content meticulously to construct an alphabetically organized index exceeding 100 entries. I've finalized the extraction and indexing strategy and can now commence implementation. The user's goal of a detailed index, covering content from diverse chapters and appendices within the Agentic Design Patterns series, is now within reach. I'll focus on delivering a thorough response, going beyond a mere sample index.

> 路径明确：据 31 份文件名汇总章题，再精读正文，构建按字母排序、逾百条的索引；覆盖《Agentic Design Patterns》全书及各附录，交付完整索引而非示例稿。

### Defining the Approach

I've clarified the user's need. I will extract chapter titles from the document filenames. Following that, I will carefully create an index exceeding 100 entries, arranging them alphabetically and noting their chapter locations. I am prepared to begin the indexing and extraction process.

> 需求已厘清：先从文件名提取章标题，再编制逾百条、按字母排序且标注章节位置的索引；准备开始提取与编制。