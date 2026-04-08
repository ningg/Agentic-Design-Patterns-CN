# Chapter 3: Parallelization

> 第三章：并行化（Parallelization）

## Parallelization Pattern Overview

> ## 并行化模式概览

In the previous chapters, we've explored Prompt Chaining for sequential workflows and Routing for dynamic decision-making and transitions between different paths. While these patterns are essential, many complex agentic tasks involve multiple sub-tasks that can be executed *simultaneously* rather than one after another. This is where the **Parallelization** pattern becomes crucial.

> 前几章介绍了顺序工作流中的提示链，以及用于动态决策与路径切换的路由。二者都很重要，但许多复杂的智能体任务包含多个可以*同时*推进、而非逐项串行执行的子任务——这时，**并行化**就尤为关键。

Parallelization involves executing multiple components, such as LLM calls, tool usages, or even entire sub-agents, concurrently (see Fig.1). Instead of waiting for one step to complete before starting the next, parallel execution allows independent tasks to run at the same time, significantly reducing the overall execution time for tasks that can be broken down into independent parts.

> 并行化即并发运行多个组件：LLM 调用、工具使用乃至整条子智能体链路（见图 1）。不必等上一步结束再开下一步；彼此独立的任务可同时推进，从而显著压缩那些能拆成并行块的任务的总耗时。

Consider an agent designed to research a topic and summarize its findings. A sequential approach might:

> 设想一个要调研主题并汇总结论的智能体。若按顺序来做，大致是：

1. Search for Source A.  
2. Summarize Source A.  
3. Search for Source B.  
4. Summarize Source B.  
5. Synthesize a final answer from summaries A and B.

> 1. 检索来源 A。
> 2. 总结来源 A。
> 3. 检索来源 B。
> 4. 总结来源 B。
> 5. 从摘要 A 与 B 综合出最终答案。

A parallel approach could instead:

> 若改走并行，则可以：

1. Search for Source A *and* Search for Source B simultaneously.  
2. Once both searches are complete, Summarize Source A *and* Summarize Source B simultaneously.  
3. Synthesize a final answer from summaries A and B (this step is typically sequential, waiting for the parallel steps to finish).

> 1. *同时*检索来源 A 与来源 B。
> 2. 两次检索均完成后，*同时*总结来源 A 与来源 B。
> 3. 再据摘要 A、B 综合最终答案（这一步一般仍须串行，需等并行阶段全部结束）。

The core idea is to identify parts of the workflow that do not depend on the output of other parts and execute them in parallel. This is particularly effective when dealing with external services (like APIs or databases) that have latency, as you can issue multiple requests concurrently.

> 核心在于识别工作流中那些不依赖其他步骤即时输出的环节，并将它们并行执行。面对 API、数据库等天然存在时延的外部服务时，这种做法尤其划算：可以一次性并发发起多条请求。

Implementing parallelization often requires frameworks that support asynchronous execution or multi-threading/multi-processing. Modern agentic frameworks are designed with asynchronous operations in mind, allowing you to easily define steps that can run in parallel.

> 落地并行化往往需要框架支持异步执行，或多线程/多进程。当代智能体框架多按异步思路设计，定义可并行步骤也相对顺手。

![Parallelization with Sub-Agents](../assets-new/Parallelization_with_Sub_Agents.png)

Fig.1. Example of parallelization with sub-agents

> 图 1. 子智能体并行化示例

Frameworks like LangChain, LangGraph, and Google ADK provide mechanisms for parallel execution. In LangChain Expression Language (LCEL), you can achieve parallel execution by combining runnable objects using operators like | (for sequential) and by structuring your chains or graphs to have branches that execute concurrently. LangGraph, with its graph structure, allows you to define multiple nodes that can be executed from a single state transition, effectively enabling parallel branches in the workflow. Google ADK provides robust, native mechanisms to facilitate and manage the parallel execution of agents, significantly enhancing the efficiency and scalability of complex, multi-agent systems. This inherent capability within the ADK framework allows developers to design and implement solutions where multiple agents can operate concurrently, rather than sequentially.

> LangChain、LangGraph、Google ADK 等框架都提供并行执行能力。在 LangChain 表达式语言（LCEL）中，可通过将多个 runnable 组织成并行结构，让多条路径同时运行。LangGraph 则借助图拓扑来表达工作流：从同一次状态转移中扇出多个节点，自然形成并行分支。Google ADK 则原生支持多智能体的并行编排，有助于提升复杂系统的吞吐与扩展性，让“多智能体同时运行”成为一等能力。

The Parallelization pattern is vital for improving the efficiency and responsiveness of agentic systems, especially when dealing with tasks that involve multiple independent lookups, computations, or interactions with external services. It's a key technique for optimizing the performance of complex agent workflows.

> 并行化能明显提升智能体系统的效率与响应速度，在多次独立查询、并行计算或同时打多条外部接口时尤其明显，是复杂工作流里常用的性能杠杆。

## Practical Applications & Use Cases

> ## 实际应用与用例

Parallelization is a powerful pattern for optimizing agent performance across various applications:

> 并行化在多种场景下都能显著提升智能体系统的表现：

### 1. Information Gathering and Research

> ### 1. 信息收集与研究

Collecting information from multiple sources simultaneously is a classic use case.

> 同时从多处拉取信息，是最典型的用法之一。

* **Use Case:** An agent researching a company.  
  * **Parallel Tasks:** Search news articles, pull stock data, check social media mentions, and query a company database, all at the same time.  
  * **Benefit:** Gathers a comprehensive view much faster than sequential lookups.

> * **用例：** 研究某家公司的智能体。
>   * **并行任务：** 同时搜索新闻、拉取股价数据、查看社交媒体提及，并查询公司数据库。
>   * **收益：** 比顺序查询更快获得全面视图。

### 2. Data Processing and Analysis

> ### 2. 数据处理与分析

Applying different analysis techniques or processing different data segments concurrently.

> 对不同数据块并行套用不同分析手法，或分段处理。

* **Use Case:** An agent analyzing customer feedback.  
  * **Parallel Tasks:** Run sentiment analysis, extract keywords, categorize feedback, and identify urgent issues simultaneously across a batch of feedback entries.  
  * **Benefit:** Provides a multi-faceted analysis quickly.

> * **用例：** 分析客户反馈的智能体。
>   * **并行任务：** 在一批反馈条目上同时运行情感分析、关键词抽取、分类与紧急问题识别。
>   * **收益：** 快速得到多维度分析。

### 3. Multi-API or Tool Interaction

> ### 3. 多 API 或工具交互

Calling multiple independent APIs or tools to gather different types of information or perform different actions.

> 并行调用彼此独立的 API 或工具，分别取数或执行不同动作。

* **Use Case:** A travel planning agent.  
  * **Parallel Tasks:** Check flight prices, search for hotel availability, look up local events, and find restaurant recommendations concurrently.  
  * **Benefit:** Presents a complete travel plan faster.

> * **用例：** 旅行规划智能体。
>   * **并行任务：** 同时查机票、搜酒店空房、查当地活动、找餐厅推荐。
>   * **收益：** 更快呈现完整行程方案。

### 4. Content Generation with Multiple Components

> ### 4. 多组件内容生成

Generating different parts of a complex piece of content in parallel.

> 把一篇复杂内容拆成多块，并行生成后再拼装。

* **Use Case:** An agent creating a marketing email.  
  * **Parallel Tasks:** Generate a subject line, draft the email body, find a relevant image, and create a call-to-action button text simultaneously.  
  * **Benefit:** Assembles the final email more efficiently.

> * **用例：** 撰写营销邮件的智能体。
>   * **并行任务：** 同时生成主题行、正文草稿、相关配图与行动号召按钮文案。
>   * **收益：** 更高效组装最终邮件。

### 5. Validation and Verification

> ### 5. 校验与验证

Performing multiple independent checks or validations concurrently.

> 多条彼此独立的校验规则或检查项，可一并跑完。

* **Use Case:** An agent verifying user input.  
  * **Parallel Tasks:** Check email format, validate phone number, verify address against a database, and check for profanity simultaneously.  
  * **Benefit:** Provides faster feedback on input validity.

> * **用例：** 校验用户输入的智能体。
>   * **并行任务：** 同时检查邮箱格式、验证电话、对照数据库校验地址、检测不当用语。
>   * **收益：** 更快反馈输入是否有效。

### 6. Multi-Modal Processing

> ### 6. 多模态处理

Processing different modalities (text, image, audio) of the same input concurrently.

> 针对同一输入，对文本、图像、音频等不同模态并行处理。

* **Use Case:** An agent analyzing a social media post with text and an image.  
  * **Parallel Tasks:** Analyze the text for sentiment and keywords *and* analyze the image for objects and scene description simultaneously.  
  * **Benefit:** Integrates insights from different modalities more quickly.

> * **用例：** 分析同时包含文字与图片的社交媒体帖子的智能体。
>   * **并行任务：** *同时*对文本进行情感与关键词分析，*并*对图像进行物体识别与场景描述分析。
>   * **收益：** 更快整合不同模态的洞见。

### 7. A/B Testing or Multiple Options Generation

> ### 7. A/B 测试或多方案生成

Generating multiple variations of a response or output in parallel to select the best one.

> 并行产出多版回复或结果，便于对比后择优。

* **Use Case:** An agent generating different creative text options.  
  * **Parallel Tasks:** Generate three different headlines for an article simultaneously using slightly different prompts or models.  
  * **Benefit:** Allows for quick comparison and selection of the best option.

> * **用例：** 生成多种创意文案选项的智能体。
>   * **并行任务：** 用略有不同的提示或模型同时为文章生成三个标题。
>   * **收益：** 便于快速比较并选出最佳方案。

Parallelization is a fundamental optimization technique in agentic design, allowing developers to build more performant and responsive applications by leveraging concurrent execution for independent tasks.

> 并行化是智能体设计里的基础优化手段：把能并行的独立任务叠在一起跑，应用会更快、响应更敏捷。

## Hands-On Code Example (LangChain)

> ## 动手代码示例（LangChain）

Parallel execution within the LangChain framework is facilitated by the LangChain Expression Language (LCEL). The primary method involves structuring multiple runnable components within a dictionary or list construct. When this collection is passed as input to a subsequent component in the chain, the LCEL runtime executes the contained runnables concurrently.

> 在 LangChain 里，并行主要靠 LangChain 表达式语言（LCEL）：把多个可运行组件放进字典或列表；该集合再作为下游环节的输入时，LCEL 会并发调度其中的各个 runnable。

In the context of LangGraph, this principle is applied to the graph's topology. Parallel workflows are defined by architecting the graph such that multiple nodes, lacking direct sequential dependencies, can be initiated from a single common node. These parallel pathways execute independently before their results can be aggregated at a subsequent convergence point in the graph.

> LangGraph 把同一思路落在图结构上：让若干彼此没有直接先后依赖的节点，从同一个父节点一并扇出；各分支并行推进，再在后面的汇合节点上汇总结果。

The following implementation demonstrates a parallel processing workflow constructed with the LangChain framework. This workflow is designed to execute two independent operations concurrently in response to a single user query. These parallel processes are instantiated as distinct chains or functions, and their respective outputs are subsequently aggregated into a unified result.

> 下面的示例用 LangChain 搭了一条并行工作流：同一条用户查询会并发触发多条彼此独立的处理链路（摘要、问题、关键词等），最后再合并输出。

The prerequisites for this implementation include the installation of the requisite Python packages, such as langchain, langchain-community, and a model provider library like langchain-openai. Furthermore, a valid API key for the chosen language model must be configured in the local environment for authentication.

> 运行前需安装相关 Python 包（如 langchain、langchain-community、langchain-openai 等），并在本机为所选模型提供商配置有效的 API 密钥。

```python
import os
import asyncio
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough


# --- Configuration ---
# Ensure your API key environment variable is set (e.g., OPENAI_API_KEY)
try:
    llm: Optional[ChatOpenAI] = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None


# --- Define Independent Chains ---
# These three chains represent distinct tasks that can be executed in parallel.
summarize_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Summarize the following topic concisely:"),
        ("user", "{topic}"),
    ])
    | llm
    | StrOutputParser()
)

questions_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Generate three interesting questions about the following topic:"),
        ("user", "{topic}"),
    ])
    | llm
    | StrOutputParser()
)

terms_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Identify 5-10 key terms from the following topic, separated by commas:"),
        ("user", "{topic}"),
    ])
    | llm
    | StrOutputParser()
)


# --- Build the Parallel + Synthesis Chain ---
# 1. Define the block of tasks to run in parallel. The results of these,
#    along with the original topic, will be fed into the next step.
map_chain = RunnableParallel(
    {
        "summary": summarize_chain,
        "questions": questions_chain,
        "key_terms": terms_chain,
        "topic": RunnablePassthrough(),  # Pass the original topic through
    }
)

# 2. Define the final synthesis prompt which will combine the parallel results.
synthesis_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Based on the following information:
        Summary: {summary}
        Related Questions: {questions}
        Key Terms: {key_terms}
        Synthesize a comprehensive answer."""
    ),
    ("user", "Original topic: {topic}"),
])

# 3. Construct the full chain by piping the parallel results directly
#    into the synthesis prompt, followed by the LLM and output parser.
full_parallel_chain = map_chain | synthesis_prompt | llm | StrOutputParser()


# --- Run the Chain ---
async def run_parallel_example(topic: str) -> None:
    """
    Asynchronously invokes the parallel processing chain with a specific topic
    and prints the synthesized result.

    Args:
        topic: The input topic to be processed by the LangChain chains.
    """
    if not llm:
        print("LLM not initialized. Cannot run example.")
        return

    print(f"\n--- Running Parallel LangChain Example for Topic: '{topic}' ---")
    try:
        # The input to `ainvoke` is the single 'topic' string,
        # then passed to each runnable in the `map_chain`.
        response = await full_parallel_chain.ainvoke(topic)
        print("\n--- Final Response ---")
        print(response)
    except Exception as e:
        print(f"\nAn error occurred during chain execution: {e}")


if __name__ == "__main__":
    test_topic = "The history of space exploration"
    # In Python 3.7+, asyncio.run is the standard way to run an async function.
    asyncio.run(run_parallel_example(test_topic))
```

The provided Python code implements a LangChain application designed for processing a given topic efficiently by leveraging parallel execution. Note that asyncio provides concurrency, not parallelism. It achieves this on a single thread by using an event loop that intelligently switches between tasks when one is idle (e.g., waiting for a network request). This creates the effect of multiple tasks progressing at once, but the code itself is still being executed by only one thread, constrained by Python's Global Interpreter Lock (GIL).

> 这段 Python 示例借助 LangChain 并发运行多条链路，以加快对同一主题的处理。需要注意的是，`asyncio` 带来的是**并发**（协作式多任务），并不等同于多核意义上的**并行**：在单线程中，它依靠事件循环在 I/O 等待期间切换协程，看起来像是“同时推进”；但受 GIL 影响，CPU 密集型部分通常仍主要在单线程内执行。

The code begins by importing essential modules from `langchain_openai` and `langchain_core`, including components for language models, prompts, output parsing, and runnable structures. The code attempts to initialize a ChatOpenAI instance, specifically using the "gpt-4o-mini" model, with a specified temperature for controlling creativity. A try-except block is used for robustness during the language model initialization. Three independent LangChain "chains" are then defined, each designed to perform a distinct task on the input topic. The first chain is for summarizing the topic concisely, using a system message and a user message containing the topic placeholder. The second chain is configured to generate three interesting questions related to the topic. The third chain is set up to identify between 5 and 10 key terms from the input topic, requesting them to be comma-separated. Each of these independent chains consists of a ChatPromptTemplate tailored to its specific task, followed by the initialized language model and a StrOutputParser to format the output as a string.

> 代码从 `langchain_openai`、`langchain_core` 引入模型、提示模板、输出解析与 runnable 抽象；尝试创建 `ChatOpenAI`（`gpt-4o-mini`）并设置 temperature，初始化失败时用 try-except 兜底。接着定义三条互不依赖的链：一条做简短摘要，一条生成三个延伸问题，一条抽取 5–10 个逗号分隔的关键词。每条链都是「`ChatPromptTemplate` → 模型 → `StrOutputParser`」。

A RunnableParallel block is then constructed to bundle these three chains, allowing them to execute simultaneously. This parallel runnable also includes a RunnablePassthrough to ensure the original input topic is available for subsequent steps. A separate ChatPromptTemplate is defined for the final synthesis step, taking the summary, questions, key terms, and the original topic as input to generate a comprehensive answer. The full end-to-end processing chain, named `full_parallel_chain`, is created by sequencing the `map_chain` (the parallel block) into the synthesis prompt, followed by the language model and the output parser. An asynchronous function `run_parallel_example` is provided to demonstrate how to invoke this `full_parallel_chain`. This function takes the topic as input and uses invoke to run the asynchronous chain. Finally, the standard Python `if __name__ \== "__main__":` block shows how to execute the `run_parallel_example` with a sample topic, in this case, "The history of space exploration", using asyncio.run to manage the asynchronous execution.

> 随后用 `RunnableParallel` 将三条链组合为并行执行；并行块里还用 `RunnablePassthrough` 把原始 `topic` 原样传给下游。再配一个综合用的 `ChatPromptTemplate`，将摘要、问题、关键词和原始主题一并作为输入传给模型。`full_parallel_chain` 即 `map_chain | synthesis_prompt | llm | StrOutputParser`。`run_parallel_example` 用 `ainvoke` 异步调用整条链；`if __name__ == "__main__":` 里以主题「The history of space exploration」调用 `asyncio.run` 启动示例。

In essence, this code sets up a workflow where multiple LLM calls (for summarizing, questions, and terms) happen at the same time for a given topic, and their results are then combined by a final LLM call. This showcases the core idea of parallelization in an agentic workflow using LangChain.

> 概括而言：先围绕同一主题并行发起多次 LLM 调用（摘要、追问、术语抽取），再由最后一次 LLM 调用完成综合——这就是 LangChain 场景下并行化的典型骨架。

## Hands-On Code Example (Google ADK)

> ## 动手代码示例（Google ADK）

Okay, let's now turn our attention to a concrete example illustrating these concepts within the Google ADK framework. We'll examine how the ADK primitives, such as ParallelAgent and SequentialAgent, can be applied to build an agent flow that leverages concurrent execution for improved efficiency.

> 接下来看 Google ADK 里的具体例子：`ParallelAgent`、`SequentialAgent` 等原语怎样拼出一条「先并行、再汇总」的智能体流水线，以提升整体效率。

```python
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

GEMINI_MODEL = "gemini-2.0-flash"


# --- 1. Define Researcher Sub-Agents (to run in parallel) ---

# Researcher 1: Renewable Energy
researcher_agent_1 = LlmAgent(
    name="RenewableEnergyResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in energy. Research the latest advancements in 'renewable energy sources'. Use the Google Search tool provided. Summarize your key findings concisely (1-2 sentences). Output *only* the summary. """,
    description="Researches renewable energy sources.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="renewable_energy_result",
)

# Researcher 2: Electric Vehicles
researcher_agent_2 = LlmAgent(
    name="EVResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in transportation. Research the latest developments in 'electric vehicle technology'. Use the Google Search tool provided. Summarize your key findings concisely (1-2 sentences). Output *only* the summary. """,
    description="Researches electric vehicle technology.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="ev_technology_result",
)

# Researcher 3: Carbon Capture
researcher_agent_3 = LlmAgent(
    name="CarbonCaptureResearcher",
    model=GEMINI_MODEL,
    instruction="""You are an AI Research Assistant specializing in climate solutions. Research the current state of 'carbon capture methods'. Use the Google Search tool provided. Summarize your key findings concisely (1-2 sentences). Output *only* the summary. """,
    description="Researches carbon capture methods.",
    tools=[google_search],
    # Store result in state for the merger agent
    output_key="carbon_capture_result",
)


# --- 2. Create the ParallelAgent (Runs researchers concurrently) ---
# This agent orchestrates the concurrent execution of the researchers.
# It finishes once all researchers have completed and stored their results in state.
parallel_research_agent = ParallelAgent(
    name="ParallelWebResearchAgent",
    sub_agents=[researcher_agent_1, researcher_agent_2, researcher_agent_3],
    description="Runs multiple research agents in parallel to gather information.",
)


# --- 3. Define the Merger Agent (Runs after the parallel agents) ---
# This agent takes the results stored in the session state by the parallel agents
# and synthesizes them into a single, structured response with attributions.
merger_agent = LlmAgent(
    name="SynthesisAgent",
    model=GEMINI_MODEL,  # Or potentially a more powerful model if needed for synthesis
    instruction="""You are an AI Assistant responsible for combining research findings into a structured report. Your primary task is to synthesize the following research summaries, clearly attributing findings to their source areas. Structure your response using headings for each topic. Ensure the report is coherent and integrates the key points smoothly.

**Crucially:** Your entire response MUST be grounded *exclusively* on the information provided in the 'Input Summaries' below. Do NOT add any external knowledge, facts, or details not present in these specific summaries.

**Input Summaries:**
*   **Renewable Energy:**
    {renewable_energy_result}
*   **Electric Vehicles:**
    {ev_technology_result}
*   **Carbon Capture:**
    {carbon_capture_result}

**Output Format:**
## Summary of Recent Sustainable Technology Advancements

### Renewable Energy Findings (Based on RenewableEnergyResearcher's findings)
[Synthesize and elaborate *only* on the renewable energy input summary provided above.]

### Electric Vehicle Findings (Based on EVResearcher's findings)
[Synthesize and elaborate *only* on the EV input summary provided above.]

### Carbon Capture Findings (Based on CarbonCaptureResearcher's findings)
[Synthesize and elaborate *only* on the carbon capture input summary provided above.]

### Overall Conclusion
[Provide a brief (1-2 sentence) concluding statement that connects *only* the findings presented above.]

Output *only* the structured report following this format. Do not include introductory or concluding phrases outside this structure, and strictly adhere to using only the provided input summary content.
""",
    description="Combines research findings from parallel agents into a structured, cited report, strictly grounded on provided inputs.",
    # No tools needed for merging
    # No output_key needed here, as its direct response is the final output of the sequence
)


# --- 4. Create the SequentialAgent (Orchestrates the overall flow) ---
# This is the main agent that will be run. It first executes the ParallelAgent
# to populate the state, and then executes the MergerAgent to produce the final output.
sequential_pipeline_agent = SequentialAgent(
    name="ResearchAndSynthesisPipeline",
    # Run parallel research first, then merge
    sub_agents=[parallel_research_agent, merger_agent],
    description="Coordinates parallel research and synthesizes the results.",
)

root_agent = sequential_pipeline_agent
```

This code defines a multi-agent system used to research and synthesize information on sustainable technology advancements. It sets up three LlmAgent instances to act as specialized researchers. `ResearcherAgent_1` focuses on renewable energy sources, `ResearcherAgent_2` researches electric vehicle technology, and `ResearcherAgent_3` investigates carbon capture methods. Each researcher agent is configured to use a `GEMINI_MODEL` and the `google_search` tool. They are instructed to summarize their findings concisely (1-2 sentences) and store these summaries in the session state using `output_key`.

> 示例搭建了一个多智能体调研与综述系统：三个 `LlmAgent` 分头负责可再生能源、电动车技术、碳捕集方法；均使用 `GEMINI_MODEL` 与 `google_search`，各用 1–2 句话写小结，并通过各自的 `output_key` 写回会话状态。（代码里实例名为 `researcher_agent_1` 等。）

A ParallelAgent named ParallelWebResearchAgent is then created to run these three researcher agents concurrently. This allows the research to be conducted in parallel, potentially saving time. The ParallelAgent completes its execution once all its sub-agents (the researchers) have finished and populated the state.

> 接着用 `ParallelAgent`（示例名 ParallelWebResearchAgent）并行拉起三名研究员，缩短墙钟时间；待各子智能体跑完并把结果写入状态，这一阶段即告完成。

Next, a MergerAgent (also an LlmAgent) is defined to synthesize the research results. This agent takes the summaries stored in the session state by the parallel researchers as input. Its instruction emphasizes that the output must be strictly based only on the provided input summaries, prohibiting the addition of external knowledge. The MergerAgent is designed to structure the combined findings into a report with headings for each topic and a brief overall conclusion.

> 再定义 MergerAgent（同样是 `LlmAgent`）做综述：它读取各研究员写入状态的摘要；系统提示要求全文严格依据所给材料、不得臆补；输出按分主题标题组织，并附简短收束段。

Finally, a SequentialAgent named ResearchAndSynthesisPipeline is created to orchestrate the entire workflow. As the primary controller, this main agent first executes the ParallelAgent to perform the research. Once the ParallelAgent is complete, the SequentialAgent then executes the MergerAgent to synthesize the collected information. The `sequential_pipeline_agent` is set as the `root_agent`, representing the entry point for running this multi-agent system. The overall process is designed to efficiently gather information from multiple sources in parallel and then combine it into a single, structured report.

> 最后用 `SequentialAgent`（ResearchAndSynthesisPipeline）串起全局：先跑并行调研，再跑合并智能体。`sequential_pipeline_agent` 作为 `root_agent` 即对外入口。整体思路是「多路并行采数 → 一路结构化成文」。

## At a Glance

> ## 速览

**What:** Many agentic workflows involve multiple sub-tasks that must be completed to achieve a final goal. A purely sequential execution, where each task waits for the previous one to finish, is often inefficient and slow. This latency becomes a significant bottleneck when tasks depend on external I/O operations, such as calling different APIs or querying multiple databases. Without a mechanism for concurrent execution, the total processing time is the sum of all individual task durations, hindering the system's overall performance and responsiveness.

> **是什么：** 很多智能体任务要拆成多段子任务才能完成终局。若一律串行、步步等上一步，整体往往又慢又僵；一旦涉及外部 I/O（多路 API、多个库），等待时间会线性叠加，成为明显瓶颈。没有并发手段，总耗时≈各段耗时之和，系统就显得迟钝。

**Why:** The Parallelization pattern provides a standardized solution by enabling the simultaneous execution of independent tasks. It works by identifying components of a workflow, like tool usages or LLM calls, that do not rely on each other's immediate outputs. Agentic frameworks like LangChain and the Google ADK provide built-in constructs to define and manage these concurrent operations. For instance, a main process can invoke several sub-tasks that run in parallel and wait for all of them to complete before proceeding to the next step. By running these independent tasks at the same time rather than one after another, this pattern drastically reduces the total execution time.

> **为什么：** 并行化把「彼此不抢先后顺序」的步骤叠在同一时间窗里跑，是应对上述瓶颈的常规打法：标出互不阻塞的工具调用或模型调用，再交给框架调度。LangChain、Google ADK 等都提供相应原语。典型形态是：父流程 fork 出多条子任务，等全部返回后再继续。墙钟时间往往从「相加」变成「接近最慢那一条」。

**Rule of thumb:** Use this pattern when a workflow contains multiple independent operations that can run simultaneously, such as fetching data from several APIs, processing different chunks of data, or generating multiple pieces of content for later synthesis.

> **经验法则：** 只要工作流里存在「互不依赖、可同时开工」的若干操作，就值得考虑并行化——例如多源拉数、分片处理，或先生成多段素材再统一综合。

**Visual summary:**

> **图示摘要：**

![Parallelization Design Pattern](../assets-new/Parallelization_Design_Pattern.png)

Fig.2: Parallelization design pattern

> 图 2：并行化设计模式

## Key Takeaways

> ## 要点

Here are the key takeaways:

> 可归纳为：

* Parallelization is a pattern for executing independent tasks concurrently to improve efficiency.  
* It is particularly useful when tasks involve waiting for external resources, such as API calls.  
* The adoption of a concurrent or parallel architecture introduces substantial complexity and cost, impacting key development phases such as design, debugging, and system logging.  
* Frameworks like LangChain and Google ADK provide built-in support for defining and managing parallel execution.  
* In LangChain Expression Language (LCEL), RunnableParallel is a key construct for running multiple runnables side-by-side.  
* Google ADK can facilitate parallel execution through LLM-Driven Delegation, where a Coordinator agent's LLM identifies independent sub-tasks and triggers their concurrent handling by specialized sub-agents.  
* Parallelization helps reduce overall latency and makes agentic systems more responsive for complex tasks.

> * 并行化即并发执行彼此独立的子任务，以略高的设计与运维复杂度换取更短的端到端时延与更好吞吐。
> * 外部 I/O 多、等待时间长时，收益通常最大。
> * 并发/并行也会抬高设计、排障与可观测性的成本，要心里有数。
> * LangChain、Google ADK 等框架都内建并行编排能力。
> * LCEL 里常用 `RunnableParallel` 把多个 runnable 并排挂起。
> * ADK 侧还可借助 LLM 协调：由上层智能体识别可并行的子任务，再分发给子智能体同时执行。
> * 合理并行能压低端到端延迟，让系统在重负载下仍保持较好的响应感。

## Conclusion

> ## 结语

The parallelization pattern is a method for optimizing computational workflows by concurrently executing independent sub-tasks. This approach reduces overall latency, particularly in complex operations that involve multiple model inferences or calls to external services.

> 并行化用「同时推进多条独立子任务」来优化工作流，压低整体延迟；在多次模型调用或密集外部依赖的场景里尤其吃香。

Frameworks provide distinct mechanisms for implementing this pattern. In LangChain, constructs like RunnableParallel are used to explicitly define and execute multiple processing chains simultaneously. In contrast, frameworks like the Google Agent Developer Kit (ADK) can achieve parallelization through multi-agent delegation, where a primary coordinator model assigns different sub-tasks to specialized agents that can operate concurrently.

> 不同框架的抓手不一样：LangChain 侧可用 `RunnableParallel` 一类构造，显式声明「这几条链一起跑」；Google Agent Developer Kit（ADK）等则常通过多智能体编排，由协调者把子任务派给可并行的专职智能体。

By integrating parallel processing with sequential (chaining) and conditional (routing) control flows, it becomes possible to construct sophisticated, high-performance computational systems capable of efficiently managing diverse and complex tasks.

> 将并行与顺序链式、条件路由等控制流组合起来，可构建既能承载复杂任务、又能在时延上站得住的智能体系统。

## References

> 下列为英文参考资料链接（条目保持原文）。

Here are some resources for further reading on the Parallelization pattern and related concepts:

1. LangChain Expression Language (LCEL) Documentation (Parallelism): [https://python.langchain.com/docs/concepts/lcel/](https://python.langchain.com/docs/concepts/lcel/)
2. Google Agent Developer Kit (ADK) Documentation (Multi-Agent Systems): [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)  
3. Python `asyncio` Documentation: [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)
