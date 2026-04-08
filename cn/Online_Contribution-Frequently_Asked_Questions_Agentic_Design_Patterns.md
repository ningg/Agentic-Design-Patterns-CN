# **Frequently Asked Questions: Agentic Design Patterns**

> **常见问题：智能体设计模式**

## 1. What is an "agentic design pattern"?

> ## 1. 什么是「智能体设计模式」？

An agentic design pattern is a reusable, high-level solution to a common problem encountered when building intelligent, autonomous systems (agents). These patterns provide a structured framework for designing agent behaviors, much like software design patterns do for traditional programming. They help developers build more robust, predictable, and effective AI agents.

> 智能体设计模式是在构建智能自主系统（智能体）时，对常见问题的可复用高层解决方案。这些模式为设计智能体行为提供结构化框架，作用类似于传统编程中的软件设计模式，帮助开发者打造更稳健、可预期、更有效的 智能体。

## 2. What is the main goal of this guide?

> ## 2. 本指南的主要目标是什么？

The guide aims to provide a practical, hands-on introduction to designing and building agentic systems. It moves beyond theoretical discussions to offer concrete architectural blueprints that developers can use to create agents capable of complex, goal-oriented behavior in a reliable way.

> 本指南旨在以实践、动手的方式介绍如何设计与构建智能体系统。它不囿于纯理论，而是给出可落地的架构蓝图，供开发者可靠地构建能完成复杂、目标导向行为的智能体。

## 3. Who is the intended audience for this guide?

> ## 3. 本指南面向哪些读者？

This guide is written for AI developers, software engineers, and system architects who are building applications with large language models (LLMs) and other AI components. It is for those who want to move from simple prompt-response interactions to creating sophisticated, autonomous agents.

> 本指南面向使用大语言模型（LLM）及其他 AI 组件搭建应用的 AI 开发者、软件工程师与系统架构师；同样适合希望从简单的「提示—回复」交互，进阶到构建复杂、自主智能体的读者。

## 4. What are some of the key agentic patterns discussed?

> ## 4. 文中讨论了哪些关键智能体模式？

Based on the table of contents, the guide covers several key patterns, including:

> 据目录，本指南涉及多项关键模式，包括：

- **Reflection:** The ability of an agent to critique its own actions and outputs to improve performance.  
- **Planning:** The process of breaking down a complex goal into smaller, manageable steps or tasks.  
- **Tool Use:** The pattern of an agent utilizing external tools (like code interpreters, search engines, or other APIs) to acquire information or perform actions it cannot do on its own.  
- **Multi-Agent Collaboration:** The architecture for having multiple specialized agents work together to solve a problem, often involving a "leader" or "orchestrator" agent.  
- **Human-in-the-Loop:** The integration of human oversight and intervention, allowing for feedback, correction, and approval of an agent's actions.  

> - **反思（Reflection）：** 使智能体能审视自身行为与产出，并据此改进表现的能力。
> - **规划（Planning）：** 将复杂目标拆解为更小、可执行的步骤或任务的过程。
> - **工具使用（Tool Use）：** 智能体调用外部工具（如代码解释器、搜索引擎或其他 API）获取信息或完成单凭自身无法执行的动作的一种模式。
> - **多智能体协作（Multi-Agent Collaboration）：** 由多名专业智能体协同解题的架构，通常设有「负责人」或「编排」角色。
> - **人在回路中（Human-in-the-Loop）：** 在人类监督与介入之下，对智能体行为给予反馈、纠正与批准。

## 5. Why is "planning" an important pattern

> ## 5. 为什么「规划」是重要的模式？

Planning is crucial because it allows an agent to tackle complex, multi-step tasks that cannot be solved with a single action. By creating a plan, the agent can maintain a coherent strategy, track its progress, and handle errors or unexpected obstacles in a structured manner. This prevents the agent from getting "stuck" or deviating from the user's ultimate goal.

> 规划之所以关键，在于它让智能体能应对无法靠单步动作解决的复杂、多步骤任务。有了计划，智能体才能维持连贯策略、跟踪进度，并以结构化方式处理错误与意外障碍，减少「卡死」或偏离用户最终目标的情况。

## 6. What is the difference between a "tool" and a "skill" for an agent

> ## 6. 对智能体而言，「工具」与「技能」有何不同？

While the terms are often used interchangeably, a "tool" generally refers to an external resource the agent can call upon (e.g., a weather API, a calculator). A "skill" is a more integrated capability that the agent has learned, often combining tool use with internal reasoning to perform a specific function (e.g., the skill of "booking a flight" might involve using calendar and airline APIs).

> 二者常被混用；一般而言，「工具」指智能体可调用的外部资源（如天气 API、计算器）。「技能」则是更内聚的能力，往往融合工具调用与内部推理以完成特定功能（例如「预订航班」可能同时用到日历与航司 API）。

## 7. How does the "Reflection" pattern improve an agent's performance

> ## 7. 「反思」模式如何提升智能体表现？

Reflection acts as a form of self-correction. After generating a response or completing a task, the agent can be prompted to review its work, check for errors, assess its quality against certain criteria, or consider alternative approaches. This iterative refinement process helps the agent produce more accurate, relevant, and high-quality results.

> 反思是一种自我纠正机制。在生成回复或完成任务后，可引导智能体复查产出、排查错误、依标准评估质量或思索替代方案。这种迭代式打磨有助于得到更准确、相关且高质量的答案。

## 8. What is the core idea of the Reflection pattern

> ## 8. 反思模式的核心思想是什么？

The Reflection pattern gives an agent the ability to step back and critique its own work. Instead of producing a final output in one go, the agent generates a draft and then "reflects" on it, identifying flaws, missing information, or areas for improvement. This self-correction process is key to enhancing the quality and accuracy of its responses.

> 反思模式让智能体能够抽身一步、审视自身产出。它并非一次性交终稿，而是先出草稿再加以「反思」，找出疏漏、信息缺口或可改进之处。这一自我纠偏过程，是提升回答质量与准确性的关键。

## 9. Why is simple "prompt chaining" not enough for high-quality output?**

> ## 9. 为什么简单的「提示链」不足以得到高质量输出？**

Simple prompt chaining (where the output of one prompt becomes the input for the next) is often too basic. The model might just rephrase its previous output without genuinely improving it. A true Reflection pattern requires a more structured critique, prompting the agent to analyze its work against specific standards, check for logical errors, or verify facts.

> 简单提示链（上一段输出作为下一段输入）往往过于粗糙，模型可能只是改述前文而并未实质改进。真正的反思需要更有结构的批阅：引导智能体对照具体标准检视产出、排查逻辑漏洞并核实事实。

## 10. What are the two main types of reflection mentioned in this chapter?**

> ## 10. 本章提到的两类主要反思是什么？**

The chapter discusses two primary forms of reflection:

> 本章介绍两大类反思：

- **"Check your work" Reflection:** This is a basic form where the agent is simply asked to review and fix its previous output. It's a good starting point for catching simple errors.  
- **"Internal Critic" Reflection:** This is a more advanced form where a separate, "critic" agent (or a dedicated prompt) is used to evaluate the output of the "worker" agent. This critic can be given specific criteria to look for, leading to more rigorous and targeted improvements.  

> - **「检查你的工作」式反思：** 基础做法——要求智能体复查并修正上一轮输出，适合用来抓简单错误。
> - **「内部批评者」式反思：** 进阶做法——由独立的「批评者」智能体（或专用提示）评审「工作者」的输出；为批评者设定明确评判标准，改进会更严格、更有针对性。

## 11. How does reflection help in reducing "hallucinations"?

> ## 11. 反思如何帮助减少「幻觉」？

By prompting an agent to review its work, especially by comparing its statements against a known source or by checking its own reasoning steps, the Reflection pattern can significantly reduce the likelihood of hallucinations (making up facts). The agent is forced to be more grounded in the provided context and less likely to generate unsupported information.

> 通过提示智能体复查产出——尤其是将陈述与已知来源对照，或逐步核对自身推理——反思模式可显著降低编造事实（即幻觉）的概率，使智能体更紧扣所给上下文，减少缺乏依据的内容。

## 12. Can the Reflection pattern be applied more than once?

> ## 12. 反思模式可以多次应用吗？

Yes, reflection can be an iterative process. An agent can be made to reflect on its work multiple times, with each loop refining the output further. This is particularly useful for complex tasks where the first or second attempt may still contain subtle errors or could be substantially improved.

> 可以。反思可以是迭代过程：可让智能体多轮反思，逐轮精炼输出。这对复杂任务尤为有用——初稿、二稿仍可能残留细微错误，或仍有较大改进空间。

## 13. What is the Planning pattern in the context of AI agents?

> ## 13. 在 智能体语境下，规划模式是什么？

The Planning pattern involves enabling an agent to break down a complex, high-level goal into a sequence of smaller, actionable steps. Instead of trying to solve a big problem at once, the agent first creates a "plan" and then executes each step in the plan, which is a much more reliable approach.

> 规划模式是指让智能体把复杂的高层目标拆解为一系列更小、可执行的步骤。与其试图一次性解决整个问题，不如先形成明确计划，再按步骤推进，这种方式通常更为可靠。

## 14. Why is planning necessary for complex tasks?

> ## 14. 为什么复杂任务需要规划？

LLMs can struggle with tasks that require multiple steps or dependencies. Without a plan, an agent might lose track of the overall objective, miss crucial steps, or fail to handle the output of one step as the input for the next. A plan provides a clear roadmap, ensuring all requirements of the original request are met in a logical order.

> LLM 面对多步骤或强依赖的任务时往往难以胜任。若无计划，智能体容易丢掉总体目标、漏掉关键步骤，或不能把上一步产出正确传递给下一步。计划相当于路线图，有助于按逻辑顺序满足原始请求中的各项要求。

## 15. What is a common way to implement the Planning pattern?

> ## 15. 实现规划模式的常见做法是什么？

A common implementation is to have the agent first generate a list of steps in a structured format (like a JSON array or a numbered list). The system can then iterate through this list, executing each step one by one and feeding the result back to the agent to inform the next action.

> 常见做法是先让智能体用结构化格式（如 JSON 数组或编号列表）列出步骤；系统再逐步执行，并把每步结果回传智能体，供其决定下一步。

## 16. How does the agent handle errors or changes during execution?

> ## 16. 执行过程中智能体如何处理错误或变化？

A robust planning pattern allows for dynamic adjustments. If a step fails or the situation changes, the agent can be prompted to "re-plan" from the current state. It can analyze the error, modify the remaining steps, or even add new ones to overcome the obstacle.

> 稳健的规划模式应能动态调整。若某步失败或环境生变，可提示智能体基于当前状态「重规划」：研判失败原因、改写后续步骤，必要时增补新步骤以越过障碍。

## 17. Does the user see the plan?

> ## 17. 用户会看到计划吗？

This is a design choice. In many cases, showing the plan to the user first for approval is a great practice. This aligns with the "Human-in-the-Loop" pattern, giving the user transparency and control over the agent's proposed actions before they are executed.

> 这属于设计取舍。许多场景下，先展示计划并征得用户同意是良好实践，契合「人在回路中」：在执行前提高透明度，并让用户对拟采取的行动拥有控制权。

## 18. What does the "Tool Use" pattern entail?

> ## 18. 「工具使用」模式包含什么？

The Tool Use pattern allows an agent to extend its capabilities by interacting with external software or APIs. Since an LLM's knowledge is static and it can't perform real-world actions on its own, tools give it access to live information (e.g., Google Search), proprietary data (e.g., a company's database), or the ability to perform actions (e.g., send an email, book a meeting).

> 工具使用模式让智能体经由外部软件或 API 扩展能力。LLM 的知识相对静态，也难以独自完成真实世界中的动作；工具则带来实时信息（如 Google 搜索）、专有数据（如公司库表）以及可执行动作（如发邮件、约会议）。

## 19. How does an agent decide which tool to use?

> ## 19. 智能体如何决定使用哪个工具？

The agent is typically given a list of available tools along with descriptions of what each tool does and what parameters it requires. When faced with a request it can't handle with its internal knowledge, the agent's reasoning ability allows it to select the most appropriate tool from the list to accomplish the task.

> 一般会向智能体提供可用工具清单，并写明各工具的用途与参数。当请求无法仅靠内置知识解决时，智能体可凭推理从清单中挑选最契合任务的工具。

## 20. What is the "ReAct" (Reason and Act) framework mentioned in this context?

> ## 20. 此处提到的「ReAct」（推理与行动）框架是什么？

ReAct is a popular framework that integrates reasoning and acting. The agent follows a loop of **Thought** (reasoning about what it needs to do), **Action** (deciding which tool to use and with what inputs), and **Observation** (seeing the result from the tool). This loop continues until it has gathered enough information to fulfill the user's request.

> ReAct 将推理与行动融为一体的常用框架。智能体反复经历：**思考**（推断下一步该做什么）、**行动**（选定工具并给出输入）、**观察**（读取工具返回），直至信息足以回应用户请求。

## 21. What are some challenges in implementing tool use?

> ## 21. 实现工具使用有哪些挑战？

Key challenges include:

> 主要挑战有：

- **Error Handling:** Tools can fail, return unexpected data, or time out. The agent needs to be able to recognize these errors and decide whether to try again, use a different tool, or ask the user for help.  
- **Security:** Giving an agent access to tools, especially those that perform actions, has security implications. It's crucial to have safeguards, permissions, and often human approval for sensitive operations.  
- **Prompting:** The agent must be prompted effectively to generate correctly formatted tool calls (e.g., the right function name and parameters).  

> - **错误处理：** 工具可能失败、返回异常数据或超时。智能体应能识别这些情况，并决定重试、更换工具或向用户求助。
> - **安全：** 为智能体开放工具（尤其能改变现实状态的工具）会带来安全考量，需有防护与权限设计，敏感操作往往还要人工批准。
> - **提示工程：** 须通过有效提示，让智能体稳定产出格式正确的工具调用（如函数名与参数无误）。

## 22. What is the Human-in-the-Loop (HITL) pattern?

> ## 22. 什么是人在回路中（HITL）模式？

HITL is a pattern that integrates human oversight and interaction into the agent's workflow. Instead of being fully autonomous, the agent pauses at critical junctures to ask for human feedback, approval, clarification, or direction.

> HITL 把人类监督与互动嵌入智能体工作流。智能体不必全程自主，可在关键节点暂停，向人类征求反馈、批准、澄清或指示。

## 23. Why is HITL important for agentic systems?

> ## 23. 为什么 HITL 对智能体系统很重要？

It's crucial for several reasons:

> 其重要性在于：

- **Safety and Control:** For high-stakes tasks (e.g., financial transactions, sending official communications), HITL ensures a human verifies the agent's proposed actions before they are executed.  
- **Improving Quality:** Humans can provide corrections or nuanced feedback that the agent can use to improve its performance, especially in subjective or ambiguous tasks.  
- **Building Trust:** Users are more likely to trust and adopt an AI system that they can guide and supervise.  

> - **安全与控制：** 面对高风险任务（如金融交易、对外正式发文），HITL 要求人类在执行前核对智能体拟采取的动作。
> - **提升质量：** 人类可给出纠正与细粒度反馈，帮助智能体改进表现，对主观性强或表述模糊的任务尤其有效。
> - **建立信任：** 用户更愿意信任、采纳自己能够引导与监督的 AI 系统。

## 24. At what points in a workflow should you include a human?

> ## 24. 工作流中应在哪些环节纳入人类？

Common points for human intervention include:

> 常见介入点包括：

- **Plan Approval:** Before executing a multi-step plan.  
- **Tool Use Confirmation:** Before using a tool that has real-world consequences or costs money.  
- **Ambiguity Resolution:** When the agent is unsure how to proceed or needs more information from the user.  
- **Final Output Review:** Before delivering the final result to the end-user or system.  

> - **计划批准：** 在执行多步计划之前。
> - **工具使用确认：** 在使用有现实世界后果或产生费用的工具之前。
> - **消歧：** 当智能体不确定如何推进或需要用户提供更多信息时。
> - **终稿审阅：** 在向最终用户或系统交付最终结果之前。

## 25. Isn't constant human intervention inefficient?

> ## 25. 持续人工介入难道不低效吗？

It can be, which is why the key is to find the right balance. HITL should be implemented at critical checkpoints, not for every single action. The goal is to build a collaborative partnership between the human and the agent, where the agent handles the bulk of the work and the human provides strategic guidance.

> 的确可能，因此关键在于把握介入粒度。HITL 更适合设置在关键检查点，而非覆盖每一个细粒度动作。理想状态是人机协作：智能体承担主要执行工作，人类则在战略层面把关与纠偏。

## 26. What is the Multi-Agent Collaboration pattern?

> ## 26. 什么是多智能体协作模式？

This pattern involves creating a system composed of multiple specialized agents that work together to achieve a common goal. Instead of one "generalist" agent trying to do everything, you create a team of "specialist" agents, each with a specific role or expertise.

> 该模式通过多名专业智能体协作来达成共同目标。与其让单一“通才”智能体包揽全部工作，不如组织一支分工明确的“专家团队”，各司其职、发挥专长。

## 27. What are the benefits of a multi-agent system?

> ## 27. 多智能体系统有什么好处？

- **Modularity and Specialization:** Each agent can be fine-tuned and prompted for its specific task (e.g., a "researcher" agent, a "writer" agent, a "code" agent), leading to higher quality results.  
- **Reduced Complexity:** Breaking a complex workflow down into specialized roles makes the overall system easier to design, debug, and maintain.  
- **Simulated Brainstorming:** Different agents can offer different perspectives on a problem, leading to more creative and robust solutions, similar to how a human team works.  

> - **模块化与专业化：** 各智能体可围绕本职做微调与提示工程（如「研究」「写作」「代码」角色），整体产出质量往往更高。
> - **降低复杂度：** 将复杂工作流拆分给不同专业角色后，整体设计、调试与维护都会更易于管理。
> - **模拟头脑风暴：** 不同智能体各抒己见，更容易碰撞出有创意且更稳妥的方案，接近人类团队研讨的效果。

## 28. What is a common architecture for multi-agent systems?

> ## 28. 多智能体系统的常见架构是什么？

A common architecture involves an **Orchestrator Agent** (sometimes called a "manager" or "conductor"). The orchestrator understands the overall goal, breaks it down, and delegates sub-tasks to the appropriate specialist agents. It then collects the results from the specialists and synthesizes them into a final output.

> 常见架构包含**编排智能体（Orchestrator Agent）**（有时称「经理」或「指挥」）。编排者把握总体目标、拆解任务，将子任务分派给对口专家，再汇总各方产出并合成为最终结果。

## How do the agents communicate with each other?

> ## 智能体之间如何通信？

Communication is often managed by the orchestrator. For example, the orchestrator might pass the output of the "researcher" agent to the "writer" agent as context. A shared "scratchpad" or message bus where agents can post their findings is another common communication method.

> 通信多由编排者居中调度。例如把「研究」智能体的输出当作上下文交给「写作」智能体。另常见做法是共享「草稿本」或消息总线，供各智能体张贴中间结果。

## Why is evaluating an agent more difficult than evaluating a traditional software program?

> ## 为什么评估智能体比评估传统软件更难？

Traditional software has deterministic outputs (the same input always produces the same output). Agents, especially those using LLMs, are non-deterministic and their performance can be subjective. Evaluating them requires assessing the *quality* and *relevance* of their output, not just whether it's technically "correct."

> 传统软件的输出是确定性的：同一输入恒得同一输出。而基于 LLM 的智能体往往非确定性，优劣也可能带主观色彩。评估时要看的不仅是技术上是否「对」，更是输出的*质量*与*相关性*。

## What are some common methods for evaluating agent performance?

> ## 评估智能体表现的常用方法有哪些？

The guide suggests a few methods:

> 本指南建议从以下角度评估：

- **Outcome-based Evaluation:** Did the agent successfully achieve the final goal? For example, if the task was "book a flight," was a flight actually booked correctly? This is the most important measure.  
- **Process-based Evaluation:** Was the agent's *process* efficient and logical? Did it use the right tools? Did it follow a sensible plan? This helps debug why an agent might be failing.  
- **Human Evaluation:** Having humans score the agent's performance on a scale (e.g., 1-5) based on criteria like helpfulness, accuracy, and coherence. This is crucial for user-facing applications.  

> - **结果导向评估：** 最终目标达成了吗？例如任务是「订机票」，是否确实订对、订成？往往是最核心的指标。
> - **过程导向评估：** *过程*是否高效、合乎逻辑？工具是否选对？计划是否合理？便于定位失败根因。
> - **人工评估：** 请人类按有用性、准确性、连贯性等维度打分（如 1–5），对直接面向用户的场景尤其重要。

## What is an "agent trajectory"?

> ## 什么是「智能体轨迹（agent trajectory）」？

An agent trajectory is the complete log of an agent's steps while performing a task. It includes all its thoughts, actions (tool calls), and observations. Analyzing these trajectories is a key part of debugging and understanding agent behavior.

> 智能体轨迹指执行任务全过程中留下的完整日志，涵盖思考、动作（含工具调用）与观察。研读轨迹是调试行为、理解决策链路的关键环节。

## How can you create reliable tests for a non-deterministic system?

> ## 如何为非确定性系统编写可靠测试？

While you can't guarantee the exact wording of an agent's output, you can create tests that check for key elements. For example, you can write a test that verifies if the agent's final response *contains* specific information or if it successfully called a certain tool with the right parameters. This is often done using mock tools in a dedicated testing environment.

> 虽难保证智能体输出逐字相同，仍可编写断言关键要素的测试。例如检查最终回复是否*含有*指定信息，或是否用对参数调用了目标工具；实践中多在隔离环境里配合 mock 工具完成。

## How is prompting an agent different from a simple ChatGPT prompt?

> ## 给智能体写提示与简单 ChatGPT 提示有何不同？

Prompting an agent involves creating a detailed "system prompt" or constitution that acts as its operating instructions. This goes beyond a single user query; it defines the agent's role, its available tools, the patterns it should follow (like ReAct or Planning), its constraints, and its personality.

> 为智能体设计提示时，通常需要准备详尽的“系统提示”或类似宪章的运行说明，远不止一句用户提问：其中应明确角色、可用工具、应采用的模式（如 ReAct 或规划）、约束边界以及语气风格等。

## What are the key components of a good system prompt for an agent?

> ## 好的智能体系统提示应包含哪些要素？

A strong system prompt typically includes:

> 扎实的系统提示通常包括：

- **Role and Goal:** Clearly define who the agent is and what its primary purpose is.  
- **Tool Definitions:** A list of available tools, their descriptions, and how to use them (e.g., in a specific function-calling format).  
- **Constraints and Rules:** Explicit instructions on what the agent *should not* do (e.g., "Do not use tools without approval," "Do not provide financial advice").  
- **Process Instructions:** Guidance on which patterns to use. For example, "First, create a plan. Then, execute the plan step-by-step."  
- **Example Trajectories:** Providing a few examples of successful "thought-action-observation" loops can significantly improve the agent's reliability.  

> - **角色与目标：** 说清楚智能体扮演谁、核心使命是什么。
> - **工具定义：** 列出可用工具，写明功能与调用方式（如约定的函数调用格式）。
> - **约束与规则：** 明确*不应*做什么（如「未经批准不得使用工具」「不得提供理财建议」）。
> - **流程说明：** 指明宜采用哪些模式，例如「先订计划，再逐步执行」。
> - **示例轨迹：** 附上若干跑通的「思考—行动—观察」样例，往往明显提高稳定性。

## What is "prompt leakage"?

> ## 什么是「提示泄漏（prompt leakage）」？

Prompt leakage occurs when parts of the system prompt (like tool definitions or internal instructions) are inadvertently revealed in the agent's final response to the user. This can be confusing for the user and expose underlying implementation details. Techniques like using separate prompts for reasoning and for generating the final answer can help prevent this.

> 提示泄漏即系统提示中的片段（如工具说明或内部规约）不小心混进对用户的最终回复，既困扰用户也暴露实现细节。把「中间推理」与「面向用户的终稿」拆到不同提示里，是常见缓解手段之一。

## What are some future trends in agentic systems?

> ## 智能体系统有哪些未来趋势？

The guide points towards a future with:

> 本指南所勾勒的趋势包括：

- **More Autonomous Agents:** Agents that require less human intervention and can learn and adapt on their own.  
- **Highly Specialized Agents:** An ecosystem of agents that can be hired or subscribed to for specific tasks (e.g., a travel agent, a research agent).  
- **Better Tools and Platforms:** The development of more sophisticated frameworks and platforms that make it easier to build, test, and deploy robust multi-agent systems.  

> - **更自主的智能体：** 更少依赖人工盯防，具备持续学习与自适应能力。
> - **高度专业化智能体：** 形成可按任务雇佣或订阅的智能体生态（如专职旅行、专职研究等）。
> - **更好的工具与平台：** 框架与平台日趋成熟，降低搭建、测试与上线稳健多智能体系统的门槛。