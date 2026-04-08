# Chapter 12: Exception Handling and Recovery

For AI agents to operate reliably in diverse real-world environments, they must be able to manage unforeseen situations, errors, and malfunctions. Just as humans adapt to unexpected obstacles, intelligent agents need robust systems to detect problems, initiate recovery procedures, or at least ensure controlled failure. This essential requirement forms the basis of the Exception Handling and Recovery pattern.

> 若要让 智能体在多样的真实环境中可靠运行，就必须能应对意外情况、错误与故障。正如人会适应突发障碍，智能体也需要稳健机制来发现问题、启动恢复流程，或至少实现受控失败。这一基本要求，正是「异常处理与恢复」模式的根基。

This pattern focuses on developing exceptionally durable and resilient agents that can maintain uninterrupted functionality and operational integrity despite various difficulties and anomalies. It emphasizes the importance of both proactive preparation and reactive strategies to ensure continuous operation, even when facing challenges. This adaptability is critical for agents to function successfully in complex and unpredictable settings, ultimately boosting their overall effectiveness and trustworthiness.

> 该模式侧重打造高度稳健、富有韧性的智能体，使其在各类困难与异常下仍能维持功能连续性与运行完整性。它强调事前预案与事后响应并重，以保障系统在逆境中的持续运转。这种适应能力是智能体在复杂、不可预测环境中有效完成任务的关键，也有助于提升整体效能与可信度。

The capacity to handle unexpected events ensures these AI systems are not only intelligent but also stable and reliable, which fosters greater confidence in their deployment and performance. Integrating comprehensive monitoring and diagnostic tools further strengthens an agent's ability to quickly identify and address issues, preventing potential disruptions and ensuring smoother operation in evolving conditions. These advanced systems are crucial for maintaining the integrity and efficiency of AI operations, reinforcing their ability to manage complexity and unpredictability.

> 具备处理意外事件的能力，这些 AI 系统才称得上既智能又稳定、可靠，也更能赢得人们对其部署与表现的信任。辅以完备的监控与诊断工具，智能体还能更快定位与处置问题、预防潜在中断，并在环境变化时保持顺畅运行。这类系统对维持 AI 运作的完整性与效率尤为关键，也有助于巩固其应对复杂性与不确定性的能力。

This pattern may sometimes be used with reflection. For example, if an initial attempt fails and raises an exception, a reflective process can analyze the failure and reattempt the task with a refined approach, such as an improved prompt, to resolve the error.

> 该模式有时可与「反思」配合使用。例如，初次尝试失败并抛出异常时，反思流程可剖析失败成因，再以改进后的策略（如优化提示）重试任务，从而化解问题。

## Exception Handling and Recovery Pattern Overview

The Exception Handling and Recovery pattern addresses the need for AI agents to manage operational failures. This pattern involves anticipating potential issues, such as tool errors or service unavailability, and developing strategies to mitigate them. These strategies may include error logging, retries, fallbacks, graceful degradation, and notifications. Additionally, the pattern emphasizes recovery mechanisms like state rollback, diagnosis, self-correction, and escalation, to restore agents to stable operation. Implementing this pattern enhances the reliability and robustness of AI agents, allowing them to function in unpredictable environments. Examples of practical applications include chatbots managing database errors, trading bots handling financial errors, and smart home agents addressing device malfunctions. The pattern ensures that agents can continue to operate effectively despite encountering complexities and failures.

> 「异常处理与恢复」模式针对的是 智能体对运行故障的管理能力。它要求系统预见潜在问题（如工具报错或服务不可用），并准备相应的缓解策略，例如错误日志、重试、回退、优雅降级与通知等。此外，还需设计恢复机制，如状态回滚、故障诊断、自我纠正与升级处置，帮助智能体尽快回到稳定状态。实施该模式能够显著提升可靠性与鲁棒性，使智能体在不可预测环境中仍可持续运行。典型场景包括聊天机器人应对数据库故障、交易机器人处理金融异常、家居智能体处理设备失灵等，从而确保系统在复杂性与故障并存时仍能维持有效服务。

Key Components of Exception Handling and Recovery for AI agents

> 智能体侧「异常处理与恢复」的关键组成

Fig.1: Key components of exception handling and recovery for AI agents

> 图 1：智能体「异常处理与恢复」的关键组成部分

**Error Detection:** This involves meticulously identifying operational issues as they arise. This could manifest as invalid or malformed tool outputs, specific API errors such as 404 (Not Found) or 500 (Internal Server Error) codes, unusually long response times from services or APIs, or incoherent and nonsensical responses that deviate from expected formats. Additionally, monitoring by other agents or specialized monitoring systems might be implemented for more proactive anomaly detection, enabling the system to catch potential issues before they escalate.

> **错误检测：** 即在问题露头时细致识别运行异常。常见表现包括：无效或格式错误的工具输出，特定 API 报错（如 404「未找到」、500「内部服务器错误」），服务或 API 响应异常缓慢，以及偏离预期格式、语无伦次的回复。亦可借助其他智能体或专用监控系统做更主动的异常发现，在问题扩大前先行拦截。

**Error Handling**: Once an error is detected, a carefully thought-out response plan is essential. This includes recording error details meticulously in logs for later debugging and analysis (logging). Retrying the action or request, sometimes with slightly adjusted parameters, may be a viable strategy, especially for transient errors (retries). Utilizing alternative strategies or methods (fallbacks) can ensure that some functionality is maintained. Where complete recovery is not immediately possible, the agent can maintain partial functionality to provide at least some value (graceful degradation). Finally, alerting human operators or other agents might be crucial for situations that require human intervention or collaboration (notification).

> **错误处理：** 检出错误后，须有周密预案：将详情完整写入日志，便于后续调试与分析（日志记录）；对操作或请求进行重试，并可适度调整参数，这对瞬时故障尤其有效（重试）；改用备选策略或路径（回退），以保留部分能力；若暂时无法完全恢复，可通过降级运行继续提供有限价值（优雅降级）；在需要人工介入或协同处置时，应及时向人类操作员或其他智能体发出告警（通知）。

**Recovery:** This stage is about restoring the agent or system to a stable and operational state after an error. It could involve reversing recent changes or transactions to undo the effects of the error (state rollback). A thorough investigation into the cause of the error is vital for preventing recurrence. Adjusting the agent's plan, logic, or parameters through a self-correction mechanism or replanning process may be needed to avoid the same error in the future. In complex or severe cases, delegating the issue to a human operator or a higher-level system (escalation) might be the best course of action.

> **恢复：** 目标是在出错后把智能体或系统拉回稳定、可运行状态。手段包括：撤销近期变更或事务以抵消错误影响（状态回滚）；彻查根因以防复发；通过自我纠正或重规划调整计划、逻辑或参数，避免重蹈覆辙；在复杂或严重情形下，将问题移交人类操作员或更高级系统（升级）往往是上策。

Implementation of this robust exception handling and recovery pattern can transform AI agents from fragile and unreliable systems into robust, dependable components capable of operating effectively and resiliently in challenging and highly unpredictable environments. This ensures that the agents maintain functionality, minimize downtime, and provide a seamless and reliable experience even when faced with unexpected issues.

> 稳健实施异常处理与恢复，可把 智能体从脆弱、不可靠的系统，锻造成能在高挑战、强不确定环境中有效运转、富有弹性的可靠组件。这有助于保持能力在线、降低停机时间，并在意外发生时仍提供流畅、可预期的体验。

## Practical Applications & Use Cases

Exception Handling and Recovery is critical for any agent deployed in a real-world scenario where perfect conditions cannot be guaranteed.

> 凡部署在无法假设「一切正常」的真实场景中的智能体，异常处理与恢复都不可或缺。

- **Customer Service Chatbots:** If a chatbot tries to access a customer database and the database is temporarily down, it shouldn't crash. Instead, it should detect the API error, inform the user about the temporary issue, perhaps suggest trying again later, or escalate the query to a human agent.  
- **Automated Financial Trading:** A trading bot attempting to execute a trade might encounter an "insufficient funds" error or a "market closed" error. It needs to handle these exceptions by logging the error, not repeatedly trying the same invalid trade, and potentially notifying the user or adjusting its strategy.  
- **Smart Home Automation:** An agent controlling smart lights might fail to turn on a light due to a network issue or a device malfunction. It should detect this failure, perhaps retry, and if still unsuccessful, notify the user that the light could not be turned on and suggest manual intervention.  
- **Data Processing Agents:** An agent tasked with processing a batch of documents might encounter a corrupted file. It should skip the corrupted file, log the error, continue processing other files, and report the skipped files at the end rather than halting the entire process.  
- **Web Scraping Agents:** When a web scraping agent encounters a CAPTCHA, a changed website structure, or a server error (e.g., 404 Not Found, 503 Service Unavailable), it needs to handle these gracefully. This could involve pausing, using a proxy, or reporting the specific URL that failed.  
- **Robotics and Manufacturing:** A robotic arm performing an assembly task might fail to pick up a component due to misalignment. It needs to detect this failure (e.g., via sensor feedback), attempt to readjust, retry the pickup, and if persistent, alert a human operator or switch to a different component.

> - **客服聊天机器人：** 访问客户数据库时若库端暂时不可用，不应直接崩溃；应识别 API 错误，向用户说明临时状况，可建议稍后再试，或将工单转交人工客服。
> - **自动化金融交易：** 交易机器人可能遇到「资金不足」「市场已闭市」等异常；应记日志、避免对同一无效指令死循环重试，并视情况通知用户或调整策略。
> - **智能家居自动化：** 控制灯具的智能体可能因网络或设备故障无法开灯；应能检出失败并重试；仍失败则告知用户并建议人工处置。
> - **数据处理智能体：** 批处理文档时若遇损坏文件，应跳过该条、记录日志、继续处理其余文件，并在结束时汇总报告，而非整批停摆。
> - **网页抓取智能体：** 遇验证码、页面结构变更或 404、503 等服务器错误时，应妥善应对：可暂停、走代理，或回报失败 URL。
> - **机器人与制造：** 机械臂可能因对位偏差无法拾取；应据传感器等反馈检出失败，尝试重新对位并重试；若仍失败，告警人工或改换工件/流程。

In short, this pattern is fundamental for building agents that are not only intelligent but also reliable, resilient, and user-friendly in the face of real-world complexities.

> 简言之，该模式是打造「既聪明，又在真实世界复杂度面前仍可靠、有韧性、好用」的智能体的基石。

## Hands-On Code Example (ADK)

Exception handling and recovery are vital for system robustness and reliability. Consider, for instance, an agent's response to a failed tool call. Such failures can stem from incorrect tool input or issues with an external service that the tool depends on.

> 异常处理与恢复直接关系到系统鲁棒性与可靠性。例如，智能体在工具调用失败时应如何应对：失败既可能来自参数或输入不当，也可能来自工具所依赖的外部服务故障。

```python
from google.adk.agents import Agent, SequentialAgent


# Agent 1: Tries the primary tool. Its focus is narrow and clear.
primary_handler = Agent(
    name="primary_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
    Your job is to get precise location information. Use the get_precise_location_info
    tool with the user's provided address.
    """,
    tools=[get_precise_location_info],
)

# Agent 2: Acts as the fallback handler, checking state to decide its action.
fallback_handler = Agent(
    name="fallback_handler",
    model="gemini-2.0-flash-exp",
    instruction="""
    Check if the primary location lookup failed by looking at state["primary_location_failed"].
    - If it is True, extract the city from the user's original query and use the get_general_area_info tool.
    - If it is False, do nothing.
    """,
    tools=[get_general_area_info],
)

# Agent 3: Presents the final result from the state.
response_agent = Agent(
    name="response_agent",
    model="gemini-2.0-flash-exp",
    instruction="""
    Review the location information stored in state["location_result"]. Present this information
    clearly and concisely to the user. If state["location_result"] does not exist or is empty,
    apologize that you could not retrieve the location.
    """,
    tools=[],  # This agent only reasons over the final state.
)

# The SequentialAgent ensures the handlers run in a guaranteed order.
robust_location_agent = SequentialAgent(
    name="robust_location_agent",
    sub_agents=[primary_handler, fallback_handler, response_agent],
)
```

This code defines a robust location retrieval system using a ADK's SequentialAgent with three sub-agents. The `primary_handler` is the first agent, attempting to get precise location information using the `get_precise_location_info` tool. The `fallback_handler` acts as a backup, checking if the primary lookup failed by inspecting a state variable. If the primary lookup failed, the fallback agent extracts the city from the user's query and uses the `get_general_area_info` tool. The `response_agent` is the final agent in the sequence. It reviews the location information stored in the state. This agent is designed to present the final result to the user. If no location information was found, it apologizes. The SequentialAgent ensures that these three agents execute in a predefined order. This structure allows for a layered approach to location information retrieval.

> 上述代码借助 ADK 的 `SequentialAgent` 与三个子智能体，搭建了一套稳健的位置检索链路。`primary_handler` 首先调用 `get_precise_location_info`，尝试获取精确地址；`fallback_handler` 通过状态变量判断主路径是否失败，若失败则从用户原始问题中提取城市名称，再调用 `get_general_area_info`。末尾的 `response_agent` 负责汇总状态中的位置结果并清晰呈现给用户；若无结果则礼貌致歉。`SequentialAgent` 保证执行顺序固定，从而形成分层检索与回退机制。

## At a Glance

**What:** AI agents operating in real-world environments inevitably encounter unforeseen situations, errors, and system malfunctions. These disruptions can range from tool failures and network issues to invalid data, threatening the agent's ability to complete its tasks. Without a structured way to manage these problems, agents can be fragile, unreliable, and prone to complete failure when faced with unexpected hurdles. This unreliability makes it difficult to deploy them in critical or complex applications where consistent performance is essential.

> **是什么：** 真实环境里的 智能体难免遭遇意外、错误与系统故障——工具失灵、网络抖动、脏数据等都会削弱其完成任务的能力。若缺乏结构化的问题管理，智能体易显脆弱，一遇障碍便全线崩溃，因而难以用于要求高稳定性的关键或复杂场景。

**Why**: The Exception Handling and Recovery pattern provides a standardized solution for building robust and resilient AI agents. It equips them with the agentic capability to anticipate, manage, and recover from operational failures. The pattern involves proactive error detection, such as monitoring tool outputs and API responses, and reactive handling strategies like logging for diagnostics, retrying transient failures, or using fallback mechanisms. For more severe issues, it defines recovery protocols, including reverting to a stable state, self-correction by adjusting its plan, or escalating the problem to a human operator. This systematic approach ensures agents can maintain operational integrity, learn from failures, and function dependably in unpredictable settings.

> **为什么：** 「异常处理与恢复」为打造鲁棒、有韧性的智能体提供了一套可复用的做法，使其能预见、承接并从运行故障中恢复。它既包含主动检测（如盯紧工具输出与 API 响应），也包含应对策略（诊断日志、对瞬时故障重试、启用回退等）；对更严重事件则规定恢复路径：回退到稳定态、调整计划自我纠正，或升级至人类操作员。如此系统化地处置，有助于保持运行完整性、从失败中迭代，并在不确定环境中持续可用。

**Rule of Thumb:** Use this pattern for any AI agent deployed in a dynamic, real-world environment where system failures, tool errors, network issues, or unpredictable inputs are possible and operational reliability is a key requirement.

> **经验法则：** 智能体运行在动态、真实的环境里，若系统故障、工具异常、网络波动或输入不可预测皆有可能，且可靠性是硬指标，就应当采用该模式。

**Visual Summary:**

> **可视化摘要：**

Exception Handling Pattern

> 异常处理模式

Fig.2: Exception handling pattern

> 图 2：异常处理模式

## Key Takeaways

Essential points to remember:

> 可重点记住：

- Exception Handling and Recovery is essential for building robust and reliable Agents.  
- This pattern involves detecting errors, handling them gracefully, and implementing strategies to recover.  
- Error detection can involve validating tool outputs, checking API error codes, and using timeouts.  
- Handling strategies include logging, retries, fallbacks, graceful degradation, and notifications.  
- Recovery focuses on restoring stable operation through diagnosis, self-correction, or escalation.  
- This pattern ensures agents can operate effectively even in unpredictable real-world environments.

> - 要建鲁棒、可信的智能体，异常处理与恢复是必修课。
> - 模式涵盖：检出错误、妥善处置、并规划恢复路径。
> - 检测侧可校验工具输出、解读 API 错误码、配合超时等机制。
> - 处置侧常见日志、重试、回退、优雅降级与通知。
> - 恢复侧倚重诊断、自纠或升级，以重回稳定工况。
> - 落实后，智能体在变幻莫测的真实环境中仍能持续交付价值。

## Conclusion

This chapter explores the Exception Handling and Recovery pattern, which is essential for developing robust and dependable AI agents. This pattern addresses how AI agents can identify and manage unexpected issues, implement appropriate responses, and recover to a stable operational state. The chapter discusses various aspects of this pattern, including the detection of errors, the handling of these errors through mechanisms such as logging, retries, and fallbacks, and the strategies used to restore the agent or system to proper function. Practical applications of the Exception Handling and Recovery pattern are illustrated across several domains to demonstrate its relevance in handling real-world complexities and potential failures. These applications show how equipping AI agents with exception handling capabilities contributes to their reliability and adaptability in dynamic environments.

> 本章介绍「异常处理与恢复」模式——构建鲁棒、可依赖的智能体离不开它。内容覆盖：如何识别与处置意外、如何响应并回到稳定运行；从错误检测到日志、重试、回退等处理手段，再到恢复至正常功能的策略。并辅以跨领域用例，说明该模式如何应对真实世界的复杂与故障，以及异常能力如何提升动态环境下的可靠性与适应力。

## References

> 参考文献：以下条目保留英文与原始链接，不作逐条翻译。

1. McConnell, S. (2004). *Code Complete (2nd ed.)*. Microsoft Press.
2. Shi, Y., Pei, H., Feng, L., Zhang, Y., & Yao, D. (2024). *Towards Fault Tolerance in Multi-Agent Reinforcement Learning*. arXiv preprint arXiv:2412.00534.
3. O'Neill, V. (2022). *Improving Fault Tolerance and Reliability of Heterogeneous Multi-Agent IoT Systems Using Intelligence Transfer*. Electronics, 11(17), 2724.
