# Glossary

## Fundamental Concepts

**Prompt:** A prompt is the input, typically in the form of a question, instruction, or statement, that a user provides to an AI model to elicit a response. The quality and structure of the prompt heavily influence the model's output, making prompt engineering a key skill for effectively using AI.

> **提示（Prompt）：** 提示指用户提供给 AI 模型的输入，通常以问题、指令或陈述的形式出现，用以引导模型生成回应。提示的质量与结构对输出影响显著，因此提示工程是有效运用 AI 的关键技能。

**Context Window:** The context window is the maximum number of tokens an AI model can process at once, including both the input and its generated output. This fixed size is a critical limitation, as information outside the window is ignored, while larger windows enable more complex conversations and document analysis.

> **上下文窗口（Context Window）：** 上下文窗口指单次处理中模型能够容纳的最大 token 数量，包括用户输入与模型已生成的内容。这一上限是硬性约束：超出窗口的信息不会被纳入考量；窗口越大，越能支撑长篇对话与文档级分析。

**In-Context Learning:** In-context learning is an AI's ability to learn a new task from examples provided directly in the prompt, without requiring any retraining. This powerful feature allows a single, general-purpose model to be adapted to countless specific tasks on the fly.

> **上下文学习（In-Context Learning）：** 指模型仅凭提示中直接给出的示例即可理解并完成新任务，而无需更新参数或重新训练。借助这一能力，单一通用模型能在运行时快速适配大量不同场景。

**Zero-Shot, One-Shot, & Few-Shot Prompting:** These are prompting techniques where a model is given zero, one, or a few examples of a task to guide its response. Providing more examples generally helps the model better understand the user's intent and improves its accuracy for the specific task.

> **零样本、单样本与少样本提示（Zero-Shot, One-Shot, & Few-Shot Prompting）：** 指在提示中分别提供零个、一个或少量任务示例，以引导模型行为。一般而言，示例越充分，模型越能把握用户意图，在该任务上的表现也越稳定。

**Multimodality:** Multimodality is an AI's ability to understand and process information across multiple data types like text, images, and audio. This allows for more versatile and human-like interactions, such as describing an image or answering a spoken question.

> **多模态（Multimodality）：** 指模型同时理解并处理多种信息形态（如文本、图像、音频）的能力，从而支持更自然、场景更丰富的交互，例如根据图像作答或响应语音提问。

**Grounding:** Grounding is the process of connecting a model's outputs to verifiable, real-world information sources to ensure factual accuracy and reduce hallucinations. This is often achieved with techniques like RAG to make AI systems more trustworthy.

> **接地（Grounding）：** 指将模型输出锚定到可核查的现实信息源，以提升事实准确性并降低幻觉。常见做法包括检索增强生成（RAG）等，从而增强系统的可验证性与可信度。

## Core AI Model Architectures

**Transformers:** The Transformer is the foundational neural network architecture for most modern LLMs. Its key innovation is the self-attention mechanism, which efficiently processes long sequences of text and captures complex relationships between words.

> **Transformer：** Transformer 是当代大多数 LLM 所依托的基础神经网络架构。其核心创新是自注意力机制，能高效处理长文本序列，并捕获词语之间的长距离依赖与复杂关系。

**Recurrent Neural Network (RNN):** The Recurrent Neural Network is a foundational architecture that preceded the Transformer. RNNs process information sequentially, using loops to maintain a "memory" of previous inputs, which made them suitable for tasks like text and speech processing.

> **循环神经网络（RNN）：** RNN 是 Transformer 兴起前广泛使用的基础架构。它按时间步依次处理输入，借助循环结构保留对历史上下文的表征，因而常用于文本与语音等序列建模任务。

**Mixture of Experts (MoE):** Mixture of Experts is an efficient model architecture where a "router" network dynamically selects a small subset of "expert" networks to handle any given input. This allows models to have a massive number of parameters while keeping computational costs manageable.

> **混合专家（MoE）：** MoE 是一种兼顾规模与效率的架构：由路由网络为每个输入动态激活少量专家子网络。这样可在总参数量很大的同时，将单次前向计算的实际开销控制在可接受范围。

**Diffusion Models:** Diffusion models are generative models that excel at creating high-quality images. They work by adding random noise to data and then training a model to meticulously reverse the process, allowing them to generate novel data from a random starting point.

> **扩散模型（Diffusion Models）：** 扩散模型是一类擅长生成高保真图像的生成式模型。典型做法是向数据逐步加入随机噪声，再训练网络学习精细的逆过程，从而从随机噪声起点采样出新的逼真样本。

**Mamba:** Mamba is a recent AI architecture using a Selective State Space Model (SSM) to process sequences with high efficiency, especially for very long contexts. Its selective mechanism allows it to focus on relevant information while filtering out noise, making it a potential alternative to the Transformer.

> **Mamba：** Mamba 是近年提出的序列建模架构，基于选择性状态空间模型（SSM），在长上下文场景下具有较高的计算效率。其选择性机制有助于聚焦相关信息并抑制干扰，被视为 Transformer 在部分应用中的替代方向之一。

## The LLM Development Lifecycle

The development of a powerful language model follows a distinct sequence. It begins with Pre-training, where a massive base model is built by training it on a vast dataset of general internet text to learn language, reasoning, and world knowledge. Next is Fine-tuning, a specialization phase where the general model is further trained on smaller, task-specific datasets to adapt its capabilities for a particular purpose. The final stage is Alignment, where the specialized model's behavior is adjusted to ensure its outputs are helpful, harmless, and aligned with human values.

> 强大语言模型的开发通常分为三个阶段：首先是**预训练（Pre-training）**，在海量通用互联网文本上学习语言规律、推理能力与世界知识，形成基础模型；其次是**微调（Fine-tuning）**，使用规模较小、与任务相关的数据继续训练，使能力贴合具体用途；最后是**对齐（Alignment）**，调整模型行为，使输出更有帮助、更安全，并更符合人类价值观。

**Pre-training Techniques:** Pre-training is the initial phase where a model learns general knowledge from vast amounts of data. The top techniques for this involve different objectives for the model to learn from. The most common is Causal Language Modeling (CLM), where the model predicts the next word in a sentence. Another is Masked Language Modeling (MLM), where the model fills in intentionally hidden words in a text. Other important methods include Denoising Objectives, where the model learns to restore a corrupted input to its original state, Contrastive Learning, where it learns to distinguish between similar and dissimilar pieces of data, and Next Sentence Prediction (NSP), where it determines if two sentences logically follow each other.

> **预训练技术：** 预训练阶段通过自监督等学习目标，让模型从海量数据中获得通用表示。常见目标包括：因果语言建模（CLM），根据前文预测下一个词；掩码语言建模（MLM），恢复文本中被故意遮盖的词；此外还有去噪目标（从损坏输入重建原文）、对比学习（区分相似与相异样本），以及下一句预测（NSP，判断两句是否语义上前后衔接）等。

**Fine-tuning Techniques:** Fine-tuning is the process of adapting a general pre-trained model to a specific task using a smaller, specialized dataset. The most common approach is Supervised Fine-Tuning (SFT), where the model is trained on labeled examples of correct input-output pairs. A popular variant is Instruction Tuning, which focuses on training the model to better follow user commands. To make this process more efficient, Parameter-Efficient Fine-Tuning (PEFT) methods are used, with top techniques including LoRA (Low-Rank Adaptation), which only updates a small number of parameters, and its memory-optimized version, QLoRA. Another technique, Retrieval-Augmented Generation (RAG), enhances the model by connecting it to an external knowledge source during the fine-tuning or inference stage.

> **微调技术：** 微调指用任务专用的小规模数据集，将通用预训练模型适配到具体场景。主流做法是监督微调（SFT），即用标注好的输入—输出对训练模型；常见扩展是指令微调，以增强遵循自然语言指令的能力。为降低算力与显存成本，可采用参数高效微调（PEFT），例如低秩适配（LoRA）仅更新少量附加参数，或其内存友好变体 QLoRA。检索增强生成（RAG）则通过在微调或推理阶段接入外部知识源，为模型补充可检索的事实依据。

**Alignment & Safety Techniques:** Alignment is the process of ensuring an AI model's behavior aligns with human values and expectations, making it helpful and harmless. The most prominent technique is Reinforcement Learning from Human Feedback (RLHF), where a "reward model" trained on human preferences guides the AI's learning process, often using an algorithm like Proximal Policy Optimization (PPO) for stability. Simpler alternatives have emerged, such as Direct Preference Optimization (DPO), which bypasses the need for a separate reward model, and Kahneman-Tversky Optimization (KTO), which simplifies data collection further. To ensure safe deployment, Guardrails are implemented as a final safety layer to filter outputs and block harmful actions in real-time.

> **对齐与安全：** 对齐旨在使模型行为与人类价值观及使用预期一致，做到有益且无害。代表性路线是基于人类反馈的强化学习（RLHF）：先训练反映人类偏好的奖励模型，再以近端策略优化（PPO）等算法稳定优化策略。近年来也出现了更轻量的替代方案，如直接偏好优化（DPO，无需单独训练奖励模型）与 Kahneman–Tversky 优化（KTO，进一步简化偏好数据收集）。部署阶段还可叠加护栏（Guardrails），在推理时过滤不当输出并实时阻断有害行为。

## Enhancing AI Agent Capabilities

AI agents are systems that can perceive their environment and take autonomous actions to achieve goals. Their effectiveness is enhanced by robust reasoning frameworks.

> 智能体是能够感知环境、自主决策并执行动作以达成目标的系统；要充分发挥其能力，通常需要依托稳健的推理框架。

**Chain of Thought (CoT):** This prompting technique encourages a model to explain its reasoning step-by-step before giving a final answer. This process of "thinking out loud" often leads to more accurate results on complex reasoning tasks.

> **思维链（CoT）：** 该提示技术鼓励模型在给出最终答案前先逐步展开推理过程。这种显式分步推理的做法，常能提升模型在算术、逻辑与常识等复杂任务上的表现。

**Tree of Thoughts (ToT):** Tree of Thoughts is an advanced reasoning framework where an agent explores multiple reasoning paths simultaneously, like branches on a tree. It allows the agent to self-evaluate different lines of thought and choose the most promising one to pursue, making it more effective at complex problem-solving.

> **思维树（ToT）：** ToT 是一种高阶推理框架：智能体并行探索多条推理路径（类似树的分支），对各路径进行自我评估，再沿最有希望的方向深入，从而在复杂问题求解上更为有效。

**ReAct (Reason and Act):** ReAct is an agent framework that combines reasoning and acting in a loop. The agent first "thinks" about what to do, then takes an "action" using a tool, and uses the resulting observation to inform its next thought, making it highly effective at solving complex tasks.

> **ReAct（推理与行动）：** ReAct 将推理与行动纳入同一循环：智能体先「思考」下一步策略，再调用工具执行「行动」，并将观察结果反馈到下一轮思考，因而特别适合需要与外部环境交互的复杂任务。

**Planning:** This is an agent's ability to break down a high-level goal into a sequence of smaller, manageable sub-tasks. The agent then creates a plan to execute these steps in order, allowing it to handle complex, multi-step assignments.

> **规划：** 指智能体将高层目标拆解为一系列较小、可管理的子任务，并制定按序执行的计划，从而系统性地完成复杂、多步骤的任务。

**Deep Research:** Deep research refers to an agent's capability to autonomously explore a topic in-depth by iteratively searching for information, synthesizing findings, and identifying new questions. This allows the agent to build a comprehensive understanding of a subject far beyond a single search query.

> **深度研究：** 指智能体围绕某一主题自主开展多轮检索、归纳与追问，在迭代中扩展覆盖面并形成结构化理解，从而获得单次搜索或单轮问答难以达到的广度与深度。

**Critique Model:** A critique model is a specialized AI model trained to review, evaluate, and provide feedback on the output of another AI model. It acts as an automated critic, helping to identify errors, improve reasoning, and ensure the final output meets a desired quality standard.

> **评判模型：** 评判模型是专门用于审查、评估另一模型输出并给出反馈的辅助模型，相当于自动化的评审者，有助于发现错误、改进推理路径，并协助把关最终输出的质量。
