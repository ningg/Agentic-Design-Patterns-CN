# Chapter 1: Prompt Chaining

> 第一章：提示链（Prompt Chaining）

## Prompt Chaining Pattern Overview

> ## 提示链模式概览

Prompt chaining, sometimes referred to as Pipeline pattern, represents a powerful paradigm for handling intricate tasks when leveraging large language models (LLMs). Rather than expecting an LLM to solve a complex problem in a single, monolithic step, prompt chaining advocates for a divide-and-conquer strategy. The core idea is to break down the original, daunting problem into a sequence of smaller, more manageable sub-problems. Each sub-problem is addressed individually through a specifically designed prompt, and the output generated from one prompt is strategically fed as input into the subsequent prompt in the chain.

> 提示链，也常被称为流水线（Pipeline）模式，是使用大语言模型（LLM）处理复杂任务时的一种强大范式。与其期望 LLM 在单一、整体的一步中解决复杂问题，不如采取分而治之的策略：把原本棘手的大问题拆解为一系列更小、更易处理的子问题；每个子问题由专门设计的提示分别处理，而前一步的输出再有策略地作为链中下一步的输入。

This sequential processing technique inherently introduces modularity and clarity into the interaction with LLMs. By decomposing a complex task, it becomes easier to understand and debug each individual step, making the overall process more robust and interpretable. Each step in the chain can be meticulously crafted and optimized to focus on a specific aspect of the larger problem, leading to more accurate and focused outputs.

> 这种顺序处理方式在与 LLM 的交互中天然带来模块化与清晰度。分解复杂任务后，每一步都更易理解与调试，整体流程也更稳健、可解释。链中每一步都可精心设计与优化，以聚焦更大问题中的某一侧面，从而得到更准确、更聚焦的输出。

The output of one step acting as the input for the next is crucial. This passing of information establishes a dependency chain, hence the name, where the context and results of previous operations guide the subsequent processing. This allows the LLM to build on its previous work, refine its understanding, and progressively move closer to the desired solution.

> 一步的输出作为下一步的输入至关重要。这种信息传递形成依赖链，因而得名「链」：先前步骤的上下文与结果会引导后续处理，使 LLM 能在已有产出上继续建构、细化理解，并逐步逼近目标答案。

Furthermore, prompt chaining is not just about breaking down problems; it also enables the integration of external knowledge and tools. At each step, the LLM can be instructed to interact with external systems, APIs, or databases, enriching its knowledge and abilities beyond its internal training data. This capability dramatically expands the potential of LLMs, allowing them to function not just as isolated models but as integral components of broader, more intelligent systems.

> 此外，提示链不仅是拆解问题，还能整合外部知识与工具。每一步都可指示 LLM 与外部系统、API 或数据库交互，从而突破训练数据所限。这大幅扩展了 LLM 的潜力，使其不仅能作为孤立模型运行，还能成为更广、更智能系统中的有机组成部分。

The significance of prompt chaining extends beyond simple problem-solving. It serves as a foundational technique for building sophisticated AI agents. These agents can utilize prompt chains to autonomously plan, reason, and act in dynamic environments. By strategically structuring the sequence of prompts, an agent can engage in tasks requiring multi-step reasoning, planning, and decision-making. Such agent workflows can mimic human thought processes more closely, allowing for more natural and effective interactions with complex domains and systems.

> 提示链的意义不止于解题，更是构建复杂 智能体（agent）的基础手段。这些智能体可借助提示链在动态环境中自主规划、推理与行动。通过有策略地排列提示顺序，智能体可承担需要多步推理、规划与决策的任务；此类工作流能更接近人的思维过程，从而与复杂领域和系统更自然、更有效地互动。

**Limitations of single prompts:** For multifaceted tasks, using a single, complex prompt for an LLM can be inefficient, causing the model to struggle with constraints and instructions, potentially leading to instruction neglect where parts of the prompt are overlooked, contextual drift where the model loses track of the initial context, error propagation where early errors amplify, prompts which require a longer context window where the model gets insufficient information to respond back and hallucination where the cognitive load increases the chance of incorrect information. For example, a query asking to analyze a market research report, summarize findings, identify trends with data points, and draft an email risks failure as the model might summarize well but fail to extract data or draft an email properly.

> **单条提示的局限：** 面对多面向任务，把一条复杂提示直接交给 LLM 往往效率不高。模型容易在多重约束与指令之间顾此失彼，并可能出现：指令忽视（遗漏提示中的部分要求）、上下文漂移（偏离初始语境）、错误传播（前期错误被后续步骤放大）、在需要更长上下文时因信息不足而难以作答，以及幻觉（认知负荷升高、编造错误信息的概率上升）。例如，一条查询若同时要求分析市场调研报告、总结发现、提取数据支撑趋势并起草邮件，就很容易失效——模型可能摘要尚可，却无法准确提取数据或妥善完成邮件撰写。

**Enhanced Reliability Through Sequential Decomposition:** Prompt chaining addresses these challenges by breaking the complex task into a focused, sequential workflow, which significantly improves reliability and control. Given the example above, a pipeline or chained approach can be described as follows:

> **靠顺序分解提升可靠性：** 提示链把复杂任务拆成聚焦的、按序推进的工作流，从而显著提升可靠性与可控性。就上文例子而言，流水线或链式做法可描述如下：

1. Initial Prompt (Summarization): "Summarize the key findings of the following market research report: \[text\]." The model's sole focus is summarization, increasing the accuracy of this initial step.  
2. Second Prompt (Trend Identification): "Using the summary, identify the top three emerging trends and extract the specific data points that support each trend: \[output from step 1\]." This prompt is now more constrained and builds directly upon a validated output.  
3. Third Prompt (Email Composition): "Draft a concise email to the marketing team that outlines the following trends and their supporting data: \[output from step 2\]."

> 1. 初始提示（总结）：「请总结以下市场调研报告的关键发现：\[正文\]。」模型只专注总结，提高第一步的准确度。
> 2. 第二条提示（趋势识别）：「基于上述总结，识别三大新兴趋势，并提取支持每条趋势的具体数据点：\[第 1 步输出\]。」该提示约束更紧，且直接建立在已验证的输出之上。
> 3. 第三条提示（邮件撰写）：「请起草一封简洁邮件给营销团队，列出下列趋势及其支撑数据：\[第 2 步输出\]。」

This decomposition allows for more granular control over the process. Each step is simpler and less ambiguous, which reduces the cognitive load on the model and leads to a more accurate and reliable final output. This modularity is analogous to a computational pipeline where each function performs a specific operation before passing its result to the next. To ensure an accurate response for each specific task, the model can be assigned a distinct role at every stage. For example, in the given scenario, the initial prompt could be designated as "Market Analyst," the subsequent prompt as "Trade Analyst," and the third prompt as "Expert Documentation Writer," and so forth.

> 这种分解有助于对流程进行更细粒度的控制。每一步都更简单、歧义更少，从而减轻模型的认知负荷，使最终输出更准确、更可靠。这种模块化思路类似计算流水线：每个环节完成特定操作后，再将结果传递给下一环节。为确保各子任务得到高质量响应，还可以在每一阶段为模型赋予不同角色。例如在上述场景中，第一步可设为“市场分析师”，第二步设为“行业分析师”，第三步设为“专业文档撰写人”，以此类推。

**The Role of Structured Output:** The reliability of a prompt chain is highly dependent on the integrity of the data passed between steps. If the output of one prompt is ambiguous or poorly formatted, the subsequent prompt may fail due to faulty input. To mitigate this, specifying a structured output format, such as JSON or XML, is crucial.

> **结构化输出的作用：** 提示链的可靠性高度依赖步骤间传递数据的完整性。若某步输出含糊或格式混乱，下一步可能因输入不当而失败。为缓解这一点，指定 JSON、XML 等结构化输出格式至关重要。

For example, the output from the trend identification step could be formatted as a JSON object:

> 例如，趋势识别步骤的输出可格式化为 JSON 对象：

```json
{  "trends": [    
        {      
            "trend_name": "AI-Powered Personalization",      
            "supporting_data": "73% of consumers prefer to do business with brands that use personal information to make their shopping experiences more relevant."    
        },    
        {      
            "trend_name": "Sustainable and Ethical Brands",      
            "supporting_data": "Sales of products with ESG-related claims grew 28% over the last five years, compared to 20% for products without."    
        } 
    ] 
}
```

This structured format ensures that the data is machine-readable and can be precisely parsed and inserted into the next prompt without ambiguity. This practice minimizes errors that can arise from interpreting natural language and is a key component in building robust, multi-step LLM-based systems.

> 该结构化格式保证数据可被机器读取、精确解析并无歧义地填入下一步提示，从而减少「靠自然语言再理解一遍」带来的误差，是构建稳健多步 LLM 系统的关键一环。

## Practical Applications & Use Cases

> ## 实际应用与用例

Prompt chaining is a versatile pattern applicable in a wide range of scenarios when building agentic systems. Its core utility lies in breaking down complex problems into sequential, manageable steps. Here are several practical applications and use cases:

> 在构建智能体系统时，提示链的适用范围非常广；其核心价值在于把复杂问题拆解为可顺序执行、便于管理的步骤。以下列举若干实际应用与用例：

### 1. Information Processing Workflows

> ### 1. 信息处理工作流

Many tasks involve processing raw information through multiple transformations. For instance, summarizing a document, extracting key entities, and then using those entities to query a database or generate a report. A prompt chain could look like:

> 许多任务需要对原始信息做多步转换。例如：总结文档、抽取关键实体，再用这些实体查询数据库或生成报告。提示链可以是：

* Prompt 1: Extract text content from a given URL or document.  
* Prompt 2: Summarize the cleaned text.  
* Prompt 3: Extract specific entities (e.g., names, dates, locations) from the summary or original text.  
* Prompt 4: Use the entities to search an internal knowledge base.  
* Prompt 5: Generate a final report incorporating the summary, entities, and search results.

> * 提示 1：从给定 URL 或文档中提取正文。
> * 提示 2：对清洗后的文本做摘要。
> * 提示 3：从摘要或原文中抽取特定实体（如人名、日期、地点）。
> * 提示 4：用这些实体检索内部知识库。
> * 提示 5：生成最终报告，整合摘要、实体与检索结果。

This methodology is applied in domains such as automated content analysis, the development of AI-driven research assistants, and complex report generation.

> 该方法常见于自动内容分析、AI 研究助手开发、复杂报告生成等领域。

### 2. Complex Query Answering

> ### 2. 复杂问答

Answering complex questions that require multiple steps of reasoning or information retrieval is a prime use case. For example, "What were the main causes of the stock market crash in 1929, and how did government policy respond?"

> 需要多步推理或信息检索才能回答的复杂问题，是典型场景。例如：「1929 年股市崩盘的主要原因有哪些？政府政策如何应对？」

* Prompt 1: Identify the core sub-questions in the user's query (causes of crash, government response).  
* Prompt 2: Research or retrieve information specifically about the causes of the 1929 crash.  
* Prompt 3: Research or retrieve information specifically about the government's policy response to the 1929 stock market crash.  
* Prompt 4: Synthesize the information from steps 2 and 3 into a coherent answer to the original query.

> * 提示 1：识别用户问题里的核心子问题（崩盘原因、政府应对）。
> * 提示 2：专门检索 1929 年崩盘原因的相关信息。
> * 提示 3：专门检索政府对 1929 年股市崩盘的政策应对信息。
> * 提示 4：综合第 2、3 步的信息，形成对原始问题的连贯回答。

This sequential processing methodology is integral to developing AI systems capable of multi-step inference and information synthesis. Such systems are required when a query cannot be answered from a single data point but instead necessitates a series of logical steps or the integration of information from diverse sources.

> 这种顺序处理方法是构建能进行多步推理与信息综合的 AI 系统的核心。当问题无法靠单点数据回答，而需要一串逻辑步骤或整合多源信息时，就需要这类系统。

For example, an automated research agent designed to generate a comprehensive report on a specific topic executes a hybrid computational workflow. Initially, the system retrieves numerous relevant articles. The subsequent task of extracting key information from each article can be performed concurrently for each source. This stage is well-suited for parallel processing, where independent sub-tasks are run simultaneously to maximize efficiency.

> 例如，旨在就某一主题生成全面报告的自动研究智能体会执行混合计算工作流：先检索大量相关文章；随后从各篇文章抽取关键信息的任务可按来源并行执行——该阶段适合并行处理，以尽量提高效率。

However, once the individual extractions are complete, the process becomes inherently sequential. The system must first collate the extracted data, then synthesize it into a coherent draft, and finally review and refine this draft to produce a final report. Each of these later stages is logically dependent on the successful completion of the preceding one. This is where prompt chaining is applied: the collated data serves as the input for the synthesis prompt, and the resulting synthesized text becomes the input for the final review prompt. Therefore, complex operations frequently combine parallel processing for independent data gathering with prompt chaining for the dependent steps of synthesis and refinement.

> 然而，各条抽取完成后，流程在本质上变为顺序推进：须先汇总抽取结果，再综合成连贯草稿，最后审阅润色得到终稿；这些后续阶段在逻辑上依赖前一阶段顺利完成。此处正是提示链的用武之地：汇总数据作为综合提示的输入，综合后的文本再作为终稿审阅提示的输入。因此，复杂任务常把「彼此独立的数据收集」交给并行处理，把「综合与润色等相互依赖的步骤」交给提示链。

### 3. Data Extraction and Transformation

> ### 3. 数据抽取与转换

The conversion of unstructured text into a structured format is typically achieved through an iterative process, requiring sequential modifications to improve the accuracy and completeness of the output.

> 将非结构化文本转为结构化格式，通常要经迭代、按序修正，逐步提高输出的准确性与完备性。

* Prompt 1: Attempt to extract specific fields (e.g., name, address, amount) from an invoice document.  
* Processing: Check if all required fields were extracted and if they meet format requirements.  
* Prompt 2 (Conditional): If fields are missing or malformed, craft a new prompt asking the model to specifically find the missing/malformed information, perhaps providing context from the failed attempt.  
* Processing: Validate the results again. Repeat if necessary.  
* Output: Provide the extracted, validated structured data.

> * 提示 1：尝试从发票类文档中抽取特定字段（如姓名、地址、金额）。
> * 处理：检查必填字段是否齐全、格式是否符合要求。
> * 提示 2（条件式）：若字段缺失或格式错误，构造新提示让模型专门补全或纠正，并可附上失败尝试的上下文。
> * 处理：再次校验结果；必要时重复。
> * 输出：给出已抽取且已校验的结构化数据。

This sequential processing methodology is particularly applicable to data extraction and analysis from unstructured sources like forms, invoices, or emails. For example, solving complex Optical Character Recognition (OCR) problems, such as processing a PDF form, is more effectively handled through a decomposed, multi-step approach.

> 该顺序处理方法特别适用于表单、发票、邮件等非结构化来源的抽取与分析。例如，处理 PDF 表单等复杂 OCR 场景，用分解后的多步方法通常更有效。

Initially, a large language model is employed to perform the primary text extraction from the document image. Following this, the model processes the raw output to normalize the data, a step where it might convert numeric text, such as "one thousand and fifty," into its numerical equivalent, 1050\. A significant challenge for LLMs is performing precise mathematical calculations. Therefore, in a subsequent step, the system can delegate any required arithmetic operations to an external calculator tool. The LLM identifies the necessary calculation, feeds the normalized numbers to the tool, and then incorporates the precise result. This chained sequence of text extraction, data normalization, and external tool use achieves a final, accurate result that is often difficult to obtain reliably from a single LLM query.

> 先用大语言模型从文档图像中完成主要文字抽取；再处理原始输出以规范化数据，例如把「one thousand and fifty」转成数值 1050。精确算术对 LLM 是明显短板，因此后续步骤可把所需运算交给外部计算器：由 LLM 判定算式、把规范化后的数字交给工具，再把精确结果接回链路。文字抽取、数据规范化与外部工具串联这一链条，往往比单次 LLM 查询更可靠地得到准确结果。

### 4. Content Generation Workflows

> ### 4. 内容生成工作流

The composition of complex content is a procedural task that is typically decomposed into distinct phases, including initial ideation, structural outlining, drafting, and subsequent revision

> 复杂内容的写作通常是过程性任务，一般会拆成若干阶段：初步构思、结构提纲、起草与后续修订。

* Prompt 1: Generate 5 topic ideas based on a user's general interest.  
* Processing: Allow the user to select one idea or automatically choose the best one.  
* Prompt 2: Based on the selected topic, generate a detailed outline.  
* Prompt 3: Write a draft section based on the first point in the outline.  
* Prompt 4: Write a draft section based on the second point in the outline, providing the previous section for context. Continue this for all outline points.  
* Prompt 5: Review and refine the complete draft for coherence, tone, and grammar.

> * 提示 1：根据用户大致兴趣生成 5 个选题。
> * 处理：由用户选定其一，或自动择优。
> * 提示 2：基于选定主题生成详细提纲。
> * 提示 3：按提纲第一点撰写一节草稿。
> * 提示 4：按提纲第二点撰写一节草稿，并附上上一节作为上下文；提纲其余各点依此类推。
> * 提示 5：通读全文，就连贯性、语气与语法做审阅与润色。

This methodology is employed for a range of natural language generation tasks, including the automated composition of creative narratives, technical documentation, and other forms of structured textual content.

> 该方法用于多种自然语言生成任务，包括自动创作叙事、技术文档及其他结构化文本。

### 5. Conversational Agents with State

> ### 5. 带状态的对话智能体

Although comprehensive state management architectures employ methods more complex than sequential linking, prompt chaining provides a foundational mechanism for preserving conversational continuity. This technique maintains context by constructing each conversational turn as a new prompt that systematically incorporates information or extracted entities from preceding interactions in the dialogue sequence.

> 完整的状态管理架构往往比单纯的顺序串联更复杂，但提示链仍是维持对话连续性的基础手段：把每一轮对话构造成新提示，并系统性地纳入先前交互中的信息或已抽取实体。

* Prompt 1: Process User Utterance 1, identify intent and key entities.  
* Processing: Update conversation state with intent and entities.  
* Prompt 2: Based on current state, generate a response and/or identify the next required piece of information.  
* Repeat for subsequent turns, with each new user utterance initiating a chain that leverages the accumulating conversation history (state).

> * 提示 1：处理用户话语 1，识别意图与关键实体。
> * 处理：用意图与实体更新对话状态。
> * 提示 2：基于当前状态生成回复，和/或识别下一步需要的信息。
> * 后续轮次重复；每轮新的用户话语都会触发一条利用累积对话历史（状态）的链。

This principle is fundamental to the development of conversational agents, enabling them to maintain context and coherence across extended, multi-turn dialogues. By preserving the conversational history, the system can understand and appropriately respond to user inputs that depend on previously exchanged information.

> 该原则是对话智能体开发的基石，使其在长程多轮对话中保持上下文与连贯性；保留对话历史后，系统才能理解并恰当回应依赖先前交流信息的用户输入。

### 6. Code Generation and Refinement

> ### 6. 代码生成与精炼

The generation of functional code is typically a multi-stage process, requiring a problem to be decomposed into a sequence of discrete logical operations that are executed progressively

> 生成可运行代码通常是多阶段过程：需要把问题分解为一串离散逻辑操作，再逐步执行。

* Prompt 1: Understand the user's request for a code function. Generate pseudocode or an outline.  
* Prompt 2: Write the initial code draft based on the outline.  
* Prompt 3: Identify potential errors or areas for improvement in the code (perhaps using a static analysis tool or another LLM call).  
* Prompt 4: Rewrite or refine the code based on the identified issues.  
* Prompt 5: Add documentation or test cases.

> * 提示 1：理解用户对代码函数的请求，生成伪代码或提纲。
> * 提示 2：根据提纲撰写初稿代码。
> * 提示 3：识别潜在错误或改进点（可用静态分析工具或另一次 LLM 调用）。
> * 提示 4：针对问题重写或精炼代码。
> * 提示 5：补充文档或测试用例。

In applications such as AI-assisted software development, the utility of prompt chaining stems from its capacity to decompose complex coding tasks into a series of manageable sub-problems. This modular structure reduces the operational complexity for the large language model at each step. Critically, this approach also allows for the insertion of deterministic logic between model calls, enabling intermediate data processing, output validation, and conditional branching within the workflow. By this method, a single, multifaceted request that could otherwise lead to unreliable or incomplete results is converted into a structured sequence of operations managed by an underlying execution framework.

> 在 AI 辅助软件开发等场景中，提示链的价值在于把复杂编码任务拆成一系列可管理的子问题，降低模型在每一步上的操作负担。更重要的是，可在模型调用之间插入确定性逻辑，支持中间数据处理、输出校验与工作流内的条件分支，从而把原本容易导致不可靠或不完整结果的单次多面请求，转为由底层执行框架管理的有序操作序列。

### 7. Multimodal and multi-step reasoning

> ### 7. 多模态与多步推理

Analyzing datasets with diverse modalities necessitates breaking down the problem into smaller, prompt-based tasks. For example, interpreting an image that contains a picture with embedded text, labels highlighting specific text segments, and tabular data explaining each label, requires such an approach.

> 分析包含多种模态的数据集时，需要把问题拆成更小的、基于提示的子任务。例如，要解读一张同时含嵌入文字、标出特定文字片段的标签，以及解释各标签的表格数据的图像，就适合采用这种做法。

* Prompt 1: Extract and comprehend the text from the user's image request.  
* Prompt 2: Link the extracted image text with its corresponding labels.  
* Prompt 3: Interpret the gathered information using a table to determine the required output.

> * 提示 1：从用户提供的图像请求中提取并理解文字。
> * 提示 2：将图像中的文字与对应标签关联起来。
> * 提示 3：结合表格解释已收集信息，得出所需输出。

# Hands-On Code Example

> # 动手代码示例

Implementing prompt chaining ranges from direct, sequential function calls within a script to the utilization of specialized frameworks designed to manage control flow, state, and component integration. Frameworks such as LangChain, LangGraph, Crew AI, and the Google Agent Development Kit (ADK) offer structured environments for constructing and executing these multi-step processes, which is particularly advantageous for complex architectures.

> 实现提示链，既可以是脚本里直接的顺序函数调用，也可以借助专门管理控制流、状态与组件集成的框架。LangChain、LangGraph、Crew AI 与 Google Agent Development Kit（ADK）等提供构建与执行这些多步流程的结构化环境，对复杂架构尤其有利。

For the purpose of demonstration, LangChain and LangGraph are suitable choices as their core APIs are explicitly designed for composing chains and graphs of operations. LangChain provides foundational abstractions for linear sequences, while LangGraph extends these capabilities to support stateful and cyclical computations, which are necessary for implementing more sophisticated agentic behaviors. This example will focus on a fundamental linear sequence.

> 演示可选用 LangChain 与 LangGraph：二者核心 API 明确面向操作链与操作图的组合。LangChain 提供线性序列的基础抽象；LangGraph 在此基础上支持有状态与循环计算，便于实现更复杂的智能体行为。本例聚焦基本的线性序列。

The following code implements a two-step prompt chain that functions as a data processing pipeline. The initial stage is designed to parse unstructured text and extract specific information. The subsequent stage then receives this extracted output and transforms it into a structured data format.

> 下列代码实现两步提示链，充当数据处理流水线：第一阶段解析非结构化文本并抽取信息；第二阶段接收抽取结果，并转为结构化数据格式。

To replicate this procedure, the required libraries must first be installed. This can be accomplished using the following command:

> 要复现本流程，须先安装所需依赖，可使用如下命令：

```bash
pip install langchain langchain-community langchain-openai langgraph
```

Note that langchain-openai can be substituted with the appropriate package for a different model provider. Subsequently, the execution environment must be configured with the necessary API credentials for the selected language model provider, such as OpenAI, Google Gemini, or Anthropic.

> 注意：`langchain-openai` 可替换为其他模型提供商的对应包。随后须为所选语言模型服务（如 OpenAI、Google Gemini、Anthropic）在执行环境中配置必要的 API 凭证。

```python
import os 
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

# For better security, load environment variables from a .env file 
# from dotenv import load_dotenv 
# load_dotenv() 
# Make sure your OPENAI_API_KEY is set in the .env file 

# Initialize the Language Model (using ChatOpenAI is recommended) 

llm = ChatOpenAI(temperature=0) 

# --- Prompt 1: Extract Information ---

prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the following text:\n\n{text_input}" 
) 

# --- Prompt 2: Transform to JSON --- 

prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}" 
) 

# --- Build the Chain using LCEL --- 
# The StrOutputParser() converts the LLM's message output to a simple string. 
extraction_chain = prompt_extract | llm | StrOutputParser() 

# The full chain passes the output of the extraction chain into the 'specifications' 
# variable for the transformation prompt. 
full_chain = (    
    {"specifications": extraction_chain}
        | 
    prompt_transform
        | 
    llm
        | 
    StrOutputParser() 
) 

# --- Run the Chain --- 

input_text = "The new laptop model features a 3.5 GHz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD." 

# Execute the chain with the input text dictionary. 
final_result = full_chain.invoke({"text_input": input_text})
print("\n--- Final JSON Output ---")
print(final_result)
```

This Python code demonstrates how to use the LangChain library to process text. It utilizes two separate prompts: one to extract technical specifications from an input string and another to format these specifications into a JSON object. The ChatOpenAI model is employed for language model interactions, and the StrOutputParser ensures the output is in a usable string format. The LangChain Expression Language (LCEL) is used to elegantly chain these prompts and the language model together. The first chain, `extraction_chain`, extracts the specifications. The `full_chain` then takes the output of the extraction and uses it as input for the transformation prompt. A sample input text describing a laptop is provided. The `full_chain` is invoked with this text, processing it through both steps. The final result, a JSON string containing the extracted and formatted specifications, is then printed.

> 该 Python 示例展示了如何借助 LangChain 处理文本：两个独立提示分别用于从输入字符串中抽取技术规格，以及将这些规格整理为 JSON。语言模型交互通过 `ChatOpenAI` 完成，`StrOutputParser` 则确保输出被转换为可用的字符串。LangChain 表达式语言（LCEL）负责将提示与模型优雅地串联起来。`extraction_chain` 负责抽取信息；`full_chain` 则把抽取结果作为下一步转换提示的输入。示例提供了一段描述笔记本电脑的样例文本，经 `full_chain` 两步处理后，最终打印出包含抽取与格式化结果的 JSON 字符串。

## Context Engineering and Prompt Engineering

> ## 上下文工程与提示工程

Context Engineering (see Fig.1) is the systematic discipline of designing, constructing, and delivering a complete informational environment to an AI model prior to token generation. This methodology asserts that the quality of a model's output is less dependent on the model's architecture itself and more on the richness of the context provided.

> 上下文工程（见图 1）是在生成 token 之前，为 AI 模型设计、构建并交付完整信息环境的系统学科。该方法论认为，输出质量较少取决于模型架构本身，更多取决于所提供上下文的丰富程度。

![Context Engineering](../assets-new/context_engineering.png)

Fig.1: Context Engineering is the discipline of building a rich, comprehensive informational environment for an AI, as the quality of this context is a primary factor in enabling advanced Agentic performance.

> 图 1：上下文工程是为 AI 构建丰富、完备信息环境的学科；上下文质量是支撑高阶智能体表现的主要因素之一。

It represents a significant evolution from traditional prompt engineering, which focuses primarily on optimizing the phrasing of a user's immediate query. Context Engineering expands this scope to include several layers of information, such as the **system prompt**, which is a foundational set of instructions defining the AI's operational parameters—for instance, *"You are a technical writer; your tone must be formal and precise."* The context is further enriched with external data. This includes retrieved documents, where the AI actively fetches information from a knowledge base to inform its response, such as pulling technical specifications for a project. It also incorporates tool outputs, which are the results from the AI using an external API to obtain real-time data, like querying a calendar to determine a user's availability. This explicit data is combined with critical implicit data, such as user identity, interaction history, and environmental state. The core principle is that even advanced models underperform when provided with a limited or poorly constructed view of the operational environment.

> 相较主要优化用户即时查询措辞的传统提示工程，上下文工程是一次显著演进：其范围扩展到多层信息，例如定义 AI 运行参数的**系统提示**（基础指令集）——如「你是技术写作者；语气须正式、精确。」上下文还通过外部数据加厚：包括检索文档（AI 从知识库主动取数以支撑回答，如拉取项目技术规格），以及工具输出（AI 调用外部 API 得到的实时结果，如查日历判断用户是否有空）。显式数据与用户身份、交互历史、环境状态等关键隐式数据相结合。核心原则是：即便先进模型在操作环境视图狭窄或构建不当时也会表现不佳。

This practice, therefore, reframes the task from merely answering a question to building a comprehensive operational picture for the agent. For example, a context-engineered agent would not just respond to a query but would first integrate the user's calendar availability (a tool output), the professional relationship with an email's recipient (implicit data), and notes from previous meetings (retrieved documents). This allows the model to generate outputs that are highly relevant, personalized, and pragmatically useful. The "engineering" component involves creating robust pipelines to fetch and transform this data at runtime and establishing feedback loops to continually improve context quality.

> 因此，该实践把任务从「仅回答问题」重构为「为智能体构建完整的操作图景」。例如，经上下文工程设计的智能体不会只答查询，而会先整合用户日历可用性（工具输出）、与邮件收件人的职业关系（隐式数据）、以往会议笔记（检索文档），从而生成高度相关、个性化且务实有用的输出。「工程」部分包括在运行时拉取与转换数据的稳健流水线，以及建立反馈回路以持续改进上下文质量。

To implement this, specialized tuning systems can be used to automate the improvement process at scale. For example, tools like Google's Vertex AI prompt optimizer can enhance model performance by systematically evaluating responses against a set of sample inputs and predefined evaluation metrics. This approach is effective for adapting prompts and system instructions across different models without requiring extensive manual rewriting. By providing such an optimizer with sample prompts, system instructions, and a template, it can programmatically refine the contextual inputs, offering a structured method for implementing the feedback loops required for sophisticated Context Engineering.

> 实现上可借助专门调优系统，大规模自动化改进流程。例如 Google Vertex AI 的提示优化器可对照样本输入与预定义评估指标系统评估回答，以提升表现，便于在不同模型间迁移提示与系统指令而无需大量手工改写。向优化器提供样本提示、系统指令与模板后，可程序化精炼上下文输入，为复杂上下文工程所需的反馈回路提供结构化手段。

This structured approach is what differentiates a rudimentary AI tool from a more sophisticated and contextually-aware system. It treats the context itself as a primary component, placing critical importance on what the agent knows, when it knows it, and how it uses that information. The practice ensures the model has a well-rounded understanding of the user's intent, history, and current environment. Ultimately, Context Engineering is a crucial methodology for advancing stateless chatbots into highly capable, situationally-aware systems.

> 这种结构化做法区分了简陋的 AI 工具与更成熟、具上下文感知能力的系统：把上下文本身视为首要构件，强调智能体知道什么、何时知道、以及如何使用。它帮助模型对用户意图、历史与当前环境形成周全理解。归根结底，上下文工程是将无状态聊天机器人推进为高能力、情境感知系统的关键方法论。

## At a Glance

> ## 速览

**What:** Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues. The cognitive load on the model increases the likelihood of errors such as overlooking instructions, losing context, and generating incorrect information. A monolithic prompt struggles to manage multiple constraints and sequential reasoning steps effectively. This results in unreliable and inaccurate outputs, as the LLM fails to address all facets of the multifaceted request.

> **是什么：** 复杂任务若在单条提示内处理，常使 LLM 不堪重负并出现明显性能问题；认知负荷升高会增加忽视指令、丢失上下文、生成错误信息等风险。整体式提示难以同时管好多重约束与顺序推理，导致输出不可靠、不准确，无法覆盖多面请求的各个侧面。

**Why:** Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller, interconnected sub-tasks. Each step in the chain uses a focused prompt to perform a specific operation, significantly improving reliability and control. The output from one prompt is passed as the input to the next, creating a logical workflow that progressively builds towards the final solution. This modular, divide-and-conquer strategy makes the process more manageable, easier to debug, and allows for the integration of external tools or structured data formats between steps. This pattern is foundational for developing sophisticated, multi-step Agentic systems that can plan, reason, and execute complex workflows.

> **为什么：** 提示链通过把复杂问题拆成更小、彼此衔接的子任务序列，提供标准化解法。链中每一步用聚焦提示完成特定操作，显著提升可靠性与可控性；上一步输出作为下一步输入，形成逐步逼近最终答案的逻辑工作流。模块化分治使流程更易管理、更易调试，并允许在步骤间整合外部工具或结构化数据。该模式是开发能规划、推理并执行复杂工作流的多步智能体系统的基础。

**Rule of thumb:** Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building Agentic systems that need to perform multi-step reasoning and maintain state.

> **经验法则：** 当任务对单条提示过于复杂、包含多个明显处理阶段、需要在步骤间调用外部工具，或构建需多步推理与状态维护的智能体系统时，宜采用本模式。

**Visual summary:**

> **图示摘要：**

![Prompt Chaining Pattern](../assets-new/Prompt_Chaining_Pattern.png)

Fig. 2: Prompt Chaining Pattern: Agents receive a series of prompts from the user, with the output of each agent serving as the input for the next in the chain.

> 图 2：提示链模式：智能体接收用户发出的一系列提示，每个智能体的输出作为链中下一个智能体的输入。

## Key Takeaways

> ## 要点

Here are some key takeaways:

> 要点如下：

* Prompt Chaining breaks down complex tasks into a sequence of smaller, focused steps. This is occasionally known as the Pipeline pattern.  
* Each step in a chain involves an LLM call or processing logic, using the output of the previous step as input.  
* This pattern improves the reliability and manageability of complex interactions with language models.  
* Frameworks like LangChain/LangGraph, and Google ADK  provide robust tools to define, manage, and execute these multi-step sequences.

> * 提示链把复杂任务拆成更小、更聚焦的步骤序列；有时也称为流水线模式。
> * 链中每一步是一次 LLM 调用或处理逻辑，并以上一步输出为输入。
> * 该模式提升与语言模型复杂交互的可靠性与可管理性。
> * LangChain/LangGraph 与 Google ADK 等框架提供定义、管理与执行这些多步序列的稳健工具。

## Conclusion

> ## 结语

By deconstructing complex problems into a sequence of simpler, more manageable sub-tasks, prompt chaining provides a robust framework for guiding large language models. This "divide-and-conquer" strategy significantly enhances the reliability and control of the output by focusing the model on one specific operation at a time. As a foundational pattern, it enables the development of sophisticated AI agents capable of multi-step reasoning, tool integration, and state management. Ultimately, mastering prompt chaining is crucial for building robust, context-aware systems that can execute intricate workflows well beyond the capabilities of a single prompt.

> 将复杂问题解构为更简单、更易管理的子任务序列，提示链为引导大语言模型提供了稳健框架。「分而治之」让模型每次只专注一项具体操作，从而显著提升输出的可靠性与可控性。作为基础模式，它支撑开发具备多步推理、工具整合与状态管理能力的复杂 智能体。归根结底，掌握提示链对构建能执行远超单条提示能力的复杂工作流、且具上下文感知能力的稳健系统至关重要。

## References

> 下列为英文参考资料链接（条目保持原文）。

1. LangChain Documentation on LCEL: [https://python.langchain.com/v0.2/docs/core_modules/expression_language/](https://python.langchain.com/v0.2/docs/core_modules/expression_language/)
2. LangGraph Documentation: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)  
3. Prompt Engineering Guide \- Chaining Prompts: [https://www.promptingguide.ai/techniques/chaining](https://www.promptingguide.ai/techniques/chaining)
4. OpenAI API Documentation (General Prompting Concepts): [https://platform.openai.com/docs/guides/gpt/prompting](https://platform.openai.com/docs/guides/gpt/prompting)
5. Crew AI Documentation (Tasks and Processes): [https://docs.crewai.com/](https://docs.crewai.com/)
6. Google AI for Developers (Prompting Guides): [https://cloud.google.com/discover/what-is-prompt-engineering?hl=en](https://cloud.google.com/discover/what-is-prompt-engineering?hl=en)
7. Vertex Prompt Optimizer [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer)
