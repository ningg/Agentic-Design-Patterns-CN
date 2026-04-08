# Appendix C - Quick overview of Agentic Frameworks

> 附录 C：智能体框架速览

## LangChain

> ## LangChain

LangChain is a framework for developing applications powered by LLMs. Its core strength lies in its LangChain Expression Language (LCEL), which allows you to "pipe" components together into a chain. This creates a clear, linear sequence where the output of one step becomes the input for the next. It's built for workflows that are Directed Acyclic Graphs (DAGs), meaning the process flows in one direction without loops.

> LangChain 面向由 LLM 驱动的应用开发。亮点是 LangChain 表达式语言（LCEL）：像搭管道一样把组件串成链，输出逐步传递，形成易读的线性流水线。典型形态是有向无环图（DAG）——数据沿单一方向推进，不出现回路。

Use it for:

> 适用于：

* Simple RAG: Retrieve a document, create a prompt, get an answer from an LLM.  
* Summarization: Take user text, feed it to a summarization prompt, and return the output.  
* Extraction: Extract structured data (like JSON) from a block of text.

> * 简单 RAG：检索文档、构造提示、从 LLM 获得答案。
> * 摘要：接收用户文本，送入摘要提示并返回输出。
> * 抽取：从文本块中提取结构化数据（如 JSON）。

Python

```python
# A simple LCEL chain conceptually # (This is not runnable code, just illustrates the flow) 
chain = prompt | model | output_parse
```

> （以下代码示例为 Python。）

## LangGraph

> ## LangGraph

LangGraph is a library built on top of LangChain to handle more advanced agentic systems. It allows you to define your workflow as a graph with nodes (functions or LCEL chains) and edges (conditional logic). Its main advantage is the ability to create cycles, allowing the application to loop, retry, or call tools in a flexible order until a task is complete. It explicitly manages the application state, which is passed between nodes and updated throughout the process.

> LangGraph 构建在 LangChain 之上，面向更具“智能体特征”的系统：工作流被建模为图，节点可以是函数或整条 LCEL 链，边则承载条件分支。它的最大优势在于支持回路，使应用能够反复尝试、按需调整工具调用顺序，直至任务收敛。状态由框架显式维护，并在节点之间传递与更新。

Use it for:

> 适用于：

* Multi-agent Systems: A supervisor agent routes tasks to specialized worker agents, potentially looping until the goal is met.  
* Plan-and-Execute Agents: An agent creates a plan, executes a step, and then loops back to update the plan based on the result.  
* Human-in-the-Loop: The graph can wait for human input before deciding which node to go to next.

> * 多智能体系统：监督智能体将任务路由给专职工作者，可循环直至目标达成。
> * 规划–执行智能体：智能体制定计划、执行一步，再据结果回环更新计划。
> * 人在回路中：图可在决定下一节点前等待人类输入。

| Feature | LangChain | LangGraph |
| :---- | :---- | :---- |
| Core Abstraction | Chain (using LCEL) | Graph of Nodes |
| Workflow Type | Linear (Directed Acyclic Graph) | Cyclical (Graphs with loops) |
| State Management | Generally stateless per run | Explicit and persistent state object |
| Primary Use | Simple, predictable sequences | Complex, dynamic, stateful agents |

> | 特性 | LangChain | LangGraph |
> | :---- | :---- | :---- |
> | 核心抽象 | 链（使用 LCEL） | 节点图 |
> | 工作流类型 | 线性（有向无环图） | 含环（可循环的图） |
> | 状态管理 | 每次运行通常无状态 | 显式且持久的状态对象 |
> | 主要用途 | 简单、可预测的序列 | 复杂、动态、有状态的智能体 |

### Which One Should You Use?

> ### 该选哪一个？

* Choose LangChain when your application has a clear, predictable, and linear flow of steps. If you can define the process from A to B to C without needing to loop back, LangChain with LCEL is the perfect tool.  
* Choose LangGraph when you need your application to reason, plan, or operate in a loop. If your agent needs to use tools, reflect on the results, and potentially try again with a different approach, you need the cyclical and stateful nature of LangGraph.

> * 若应用具有清晰、可预测、线性的步骤流，且能从 A→B→C 定义全过程而无需回环，LangChain 与 LCEL 是合适工具。
> * 若需要应用进行推理、规划或在环中运行；若智能体需使用工具、反思结果并可能换思路重试，则需要 LangGraph 的循环与有状态特性。

```python
# Graph state
class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str


# Nodes
def call_llm_1(state: State):
    """First LLM call to generate initial joke"""
    msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}


def call_llm_2(state: State):
    """Second LLM call to generate story"""
    msg = llm.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}


def call_llm_3(state: State):
    """Third LLM call to generate poem"""
    msg = llm.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}


def aggregator(state: State):
    """Combine the joke and story into a single output"""
    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}


# Build workflow
parallel_builder = StateGraph(State)

# Add nodes
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)

parallel_workflow = parallel_builder.compile()

# Show workflow
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])
```

This code defines and runs a LangGraph workflow that operates in parallel. Its main purpose is to simultaneously generate a joke, a story, and a poem about a given topic and then combine them into a single, formatted text output.

> 上述代码定义并运行一个并行运作的 LangGraph 工作流：主要目的是就同一主题并发生成笑话、故事与诗歌，再合并为单一格式化文本输出。

## Google's ADK

> ## Google ADK

Google's Agent Development Kit, or ADK, provides a high-level, structured framework for building and deploying applications composed of multiple, interacting AI agents. It contrasts with LangChain and LangGraph by offering a more opinionated and production-oriented system for orchestrating agent collaboration, rather than providing the fundamental building blocks for an agent's internal logic.

> Google 智能体开发套件（ADK）提供高层、结构化的框架，用于构建与部署由多个交互式 智能体组成的应用。与 LangChain、LangGraph 相比，它更强调“有主见”、面向生产的智能体协作编排，而非仅提供智能体内部逻辑的基础积木。

LangChain operates at the most foundational level, offering the components and standardized interfaces to create sequences of operations, such as calling a model and parsing its output. LangGraph extends this by introducing a more flexible and powerful control flow; it treats an agent's workflow as a stateful graph. Using LangGraph, a developer explicitly defines nodes, which are functions or tools, and edges, which dictate the path of execution. This graph structure allows for complex, cyclical reasoning where the system can loop, retry tasks, and make decisions based on an explicitly managed state object that is passed between nodes. It gives the developer fine-grained control over a single agent's thought process or the ability to construct a multi-agent system from first principles.

> LangChain 处于最底层，提供组件与标准化接口以串联操作（例如调用模型并解析输出）。LangGraph 在此基础上带来更灵活、更强大的控制流，把工作流建模为有状态图：开发者显式声明节点（函数或工具）与边（执行路径）。图结构支撑复杂的循环式推理——系统可以回环、重试，并依据在节点之间传递、由框架显式管理的状态对象做决策。你既可以细粒度地塑造单个智能体的“思路”，也可以从第一性原理出发搭建多智能体系统。

Google's ADK abstracts away much of this low-level graph construction. Instead of asking the developer to define every node and edge, it provides pre-built architectural patterns for multi-agent interaction. For instance, ADK has built-in agent types like SequentialAgent or ParallelAgent, which manage the flow of control between different agents automatically. It is architected around the concept of a "team" of agents, often with a primary agent delegating tasks to specialized sub-agents. State and session management are handled more implicitly by the framework, providing a more cohesive but less granular approach than LangGraph's explicit state passing. Therefore, while LangGraph gives you the detailed tools to design the intricate wiring of a single robot or a team, Google's ADK gives you a factory assembly line designed to build and manage a fleet of robots that already know how to work together.

> Google ADK 将大量底层“手动画图”的工作抽象起来：开发者无须逐一声明节点与边，而是可以直接套用多智能体协作的预制模式。例如，框架内置了 SequentialAgent、ParallelAgent 等组件，用于自动管理智能体之间的调度。整体设计以“团队”为中心，常见范式是由主智能体将子任务分派给专长型子智能体；状态与会话通常也由框架隐式维护。与 LangGraph 相比，这种方式更省事，但控制粒度也更粗一些。可以将二者理解为：LangGraph 更像提供完整布线工具箱，而 ADK 更像一条已经为协作预先配置好的装配线。

```python
from google.adk.agents import LlmAgent
from google.adk.tools import google_Search

dice_agent = LlmAgent(
    model="gemini-2.0-flash-exp",
    name="question_answer_agent",
    description="A helpful assistant agent that can answer questions.",
    instruction="""Respond to the query using google search""",
    tools=[google_search],
)
```

This code creates a search-augmented agent. When this agent receives a question, it will not just rely on its pre-existing knowledge. Instead, following its instructions, it will use the Google Search tool to find relevant, real-time information from the web and then use that information to construct its answer.

> 上述代码创建一个搜索增强型智能体。收到问题时，它不仅依赖既有知识，还会按指令使用 Google Search 工具从网络获取相关实时信息，并据此构造回答。

## Crew.AI

> ## Crew.AI

CrewAI offers an orchestration framework for building multi-agent systems by focusing on collaborative roles and structured processes. It operates at a higher level of abstraction than foundational toolkits, providing a conceptual model that mirrors a human team. Instead of defining the granular flow of logic as a graph, the developer defines the actors and their assignments, and CrewAI manages their interaction.

> CrewAI 通过强调协作角色与结构化流程，提供构建多智能体系统的编排框架。它比基础工具包抽象层次更高，概念模型贴近人类团队：开发者定义参与者与分工，由 CrewAI 管理交互，而非把细粒度逻辑流画成图。

The core components of this framework are Agents, Tasks, and the Crew. An Agent is defined not just by its function but by a persona, including a specific role, a goal, and a backstory, which guides its behavior and communication style. A Task is a discrete unit of work with a clear description and expected output, assigned to a specific Agent. The Crew is the cohesive unit that contains the Agents and the list of Tasks, and it executes a predefined Process. This process dictates the workflow, which is typically either sequential, where the output of one task becomes the input for the next in line, or hierarchical, where a manager-like agent delegates tasks and coordinates the workflow among other agents.

> 三大构件是 Agent、Task 与 Crew：Agent 由角色、目标与背景故事刻画，用以约束行为与沟通风格；Task 为可验收的工作单元，含清晰描述与预期产出，并指派给特定 Agent；Crew 聚合 Agents 与 Tasks，按预定义 Process 执行——常见为顺序式（前一任务输出作为后一任务输入），或层级式（管理者型智能体委派与协调其他智能体）。

When compared to other frameworks, CrewAI occupies a distinct position. It moves away from the low-level, explicit state management and control flow of LangGraph, where a developer wires together every node and conditional edge. Instead of building a state machine, the developer designs a team charter. While Googlés ADK provides a comprehensive, production-oriented platform for the entire agent lifecycle, CrewAI concentrates specifically on the logic of agent collaboration and for simulating a team of specialists

> 相较其他框架，CrewAI 的定位十分鲜明：它刻意弱化 LangGraph 式的底层显式状态管理与逐条连线的控制流设计，更强调先定义清晰的“团队宪章”。Google ADK 面向智能体全生命周期的生产级平台，而 CrewAI 则更专注于协作逻辑本身，以及对“专家团队”式分工方式的模拟。

```python
@crew
def crew(self) -> Crew:
   """Creates the research crew"""
   return Crew(
     agents=self.agents,
     tasks=self.tasks,
     process=Process.sequential,
     verbose=True,
   )
```

This code sets up a sequential workflow for a team of AI agents, where they tackle a list of tasks in a specific order, with detailed logging enabled to monitor their progress.

> 上述代码为一队 智能体配置顺序工作流：按既定顺序处理任务列表，并启用详细日志以监视进展。

## Other Agent Development Framework

> ## 其他智能体开发框架

**Microsoft AutoGen**: AutoGen is a framework centered on orchestrating multiple agents that solve tasks through conversation. Its architecture enables agents with distinct capabilities to interact, allowing for complex problem decomposition and collaborative resolution. The primary advantage of AutoGen is its flexible, conversation-driven approach that supports dynamic and complex multi-agent interactions. However, this conversational paradigm can lead to less predictable execution paths and may require sophisticated prompt engineering to ensure tasks converge efficiently.

> **Microsoft AutoGen：** AutoGen 以通过对话协调多智能体解题为中心。其架构使能力各异的智能体相互交互，支持复杂问题分解与协作求解。主要优势是灵活、对话驱动的动态多智能体交互。但对话范式也可能使执行路径较难预测，并需较高明的提示工程以保证任务高效收敛。

**LlamaIndex**: LlamaIndex is fundamentally a data framework designed to connect large language models with external and private data sources. It excels at creating sophisticated data ingestion and retrieval pipelines, which are essential for building knowledgeable agents that can perform RAG. While its data indexing and querying capabilities are exceptionally powerful for creating context-aware agents, its native tools for complex agentic control flow and multi-agent orchestration are less developed compared to agent-first frameworks. LlamaIndex is optimal when the core technical challenge is data retrieval and synthesis.

> **LlamaIndex：** 本质上是连接大语言模型与外部、私有数据源的数据框架，擅长构建复杂的数据摄取与检索流水线，对能做 RAG 的“有知识”智能体至关重要。其索引与查询在构建语境感知智能体上很强，但相较“智能体优先”的框架，原生的复杂智能体控制流与多智能体编排工具较弱。当核心技术挑战是检索与综合数据时，LlamaIndex 尤为合适。

**Haystac**k: Haystack is an open-source framework engineered for building scalable and production-ready search systems powered by language models. Its architecture is composed of modular, interoperable nodes that form pipelines for document retrieval, question answering, and summarization. The main strength of Haystack is its focus on performance and scalability for large-scale information retrieval tasks, making it suitable for enterprise-grade applications. A potential trade-off is that its design, optimized for search pipelines, can be more rigid for implementing highly dynamic and creative agentic behaviors.

> **Haystack：** Haystack 是开源框架，用于构建可扩展、可投产、由语言模型驱动的搜索系统。架构由可互操作的模块化节点组成流水线，覆盖文档检索、问答与摘要。主要优势是大规模信息检索的性能与可扩展性，适合企业级应用。潜在取舍是：为搜索流水线优化的设计，在实现高度动态、创意型智能体行为时可能较僵硬。

**MetaGPT**: MetaGPT implements a multi-agent system by assigning roles and tasks based on a predefined set of Standard Operating Procedures (SOPs). This framework structures agent collaboration to mimic a software development company, with agents taking on roles like product managers or engineers to complete complex tasks. This SOP-driven approach results in highly structured and coherent outputs, which is a significant advantage for specialized domains like code generation. The framework's primary limitation is its high degree of specialization, making it less adaptable for general-purpose agentic tasks outside of its core design.

> **MetaGPT：** 基于预定义标准作业程序（SOP）分配角色与任务以实现多智能体系统。协作结构模仿软件开发公司，智能体扮演产品经理、工程师等以完成复杂任务。SOP 驱动带来高度结构化、连贯的输出，在代码生成等专业领域优势明显。主要局限是专业化程度高，在其核心设计之外的通用智能体任务上适应性较弱。

**SuperAGI**: SuperAGI is an open-source framework designed to provide a complete lifecycle management system for autonomous agents. It includes features for agent provisioning, monitoring, and a graphical interface, aiming to enhance the reliability of agent execution. The key benefit is its focus on production-readiness, with built-in mechanisms to handle common failure modes like looping and to provide observability into agent performance. A potential drawback is that its comprehensive platform approach can introduce more complexity and overhead than a more lightweight, library-based framework.

> **SuperAGI：** 开源框架，为自主智能体提供完整生命周期管理，包含供给、监控与图形界面等，旨在提升执行可靠性。关键是面向生产的就绪度：内置处理循环等常见故障模式的机制，并提供可观测性。潜在缺点是平台化全面可能带来比轻量库式框架更多的复杂性与开销。

**Semantic Kernel**: Developed by Microsoft, Semantic Kernel is an SDK that integrates large language models with conventional programming code through a system of "plugins" and "planners." It allows an LLM to invoke native functions and orchestrate workflows, effectively treating the model as a reasoning engine within a larger software application. Its primary strength is its seamless integration with existing enterprise codebases, particularly in .NET and Python environments. The conceptual overhead of its plugin and planner architecture can present a steeper learning curve compared to more straightforward agent frameworks.

> **Semantic Kernel：** 微软开发的 SDK，通过“插件”与“规划器”将大语言模型与传统程序代码集成，使 LLM 可调用原生函数并编排工作流，把模型当作更大应用中的推理引擎。主要优势是与现有企业代码库（尤其 .NET 与 Python）的无缝集成。插件与规划器架构的概念负担，相比更直白的智能体框架，学习曲线可能更陡。

**Strands Agents:** An AWS lightweight and flexible SDK that uses a model-driven approach for building and running AI agents. It is designed to be simple and scalable, supporting everything from basic conversational assistants to complex multi-agent autonomous systems. The framework is model-agnostic, offering broad support for various LLM providers, and includes native integration with the MCP for easy access to external tools. Its core advantage is its simplicity and flexibility, with a customizable agent loop that is easy to get started with. A potential trade-off is that its lightweight design means developers may need to build out more of the surrounding operational infrastructure, such as advanced monitoring or lifecycle management systems, which more comprehensive frameworks might provide out-of-the-box.

> **Strands Agents：** AWS 的轻量灵活 SDK，采用模型驱动方式构建与运行 智能体，设计简单且可扩展，从基础对话助手到复杂多智能体自主系统均可支持。框架与模型无关，广泛支持各 LLM 提供商，并原生集成 MCP 以便接入外部工具。核心优势是简单灵活、可定制的智能体循环、易上手。潜在取舍是轻量设计意味着开发者可能需自行补齐更多周边运维基础设施（如高级监控或生命周期管理），而更全面框架可能开箱即有。

## Conclusion

> ## 结语

The landscape of agentic frameworks offers a diverse spectrum of tools, from low-level libraries for defining agent logic to high-level platforms for orchestrating multi-agent collaboration. At the foundational level, LangChain enables simple, linear workflows, while LangGraph introduces stateful, cyclical graphs for more complex reasoning. Higher-level frameworks like CrewAI and Google's ADK shift the focus to orchestrating teams of agents with predefined roles, while others like LlamaIndex specialize in data-intensive applications. This variety presents developers with a core trade-off between the granular control of graph-based systems and the streamlined development of more opinionated platforms. Consequently, selecting the right framework hinges on whether the application requires a simple sequence, a dynamic reasoning loop, or a managed team of specialists. Ultimately, this evolving ecosystem empowers developers to build increasingly sophisticated AI systems by choosing the precise level of abstraction their project demands.

> 智能体框架谱系很宽：既有刻画内部逻辑的底层库，也有专注多智能体编排的上层平台。底座上，LangChain 适合笔直的流水线，LangGraph 则用带状态、可回环的图承载更曲折的推理。再往上，CrewAI、Google ADK 等强调“按角色组团队”；LlamaIndex 一类则把精力放在数据接入与检索。核心权衡在于：要 LangGraph 式的细粒度可控，还是要 ADK 式平台的省事上手。选型时先想清楚——你需要的是线性脚本、会反思的循环，还是一支分工明确的虚拟团队。生态仍在快速演进，开发者可以按项目所需的抽象层级，拼装出越来越复杂的 AI 系统。

References

> 参考文献：以下条目保留英文与原始链接，不作逐条翻译。

1. LangChain, [https://www.langchain.com/](https://www.langchain.com/)
2. LangGraph, [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
3. Google's ADK, [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
4. Crew.AI, [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction)
