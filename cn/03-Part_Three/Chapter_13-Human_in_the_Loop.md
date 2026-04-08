# Chapter 13: Human-in-the-Loop

The Human-in-the-Loop (HITL) pattern represents a pivotal strategy in the development and deployment of Agents. It deliberately interweaves the unique strengths of human cognition—such as judgment, creativity, and nuanced understanding—with the computational power and efficiency of AI. This strategic integration is not merely an option but often a necessity, especially as AI systems become increasingly embedded in critical decision-making processes.

> 「人在回路中」（Human-in-the-Loop，HITL）是智能体开发与部署中的关键策略：有意把人类在判断、创造力与语境把握上的长处，与 AI 的计算力与效率结合起来。在 AI 越来越多参与关键决策的当下，这种整合往往不只是「可选项」，而是刚需。

The core principle of HITL is to ensure that AI operates within ethical boundaries, adheres to safety protocols, and achieves its objectives with optimal effectiveness. These concerns are particularly acute in domains characterized by complexity, ambiguity, or significant risk, where the implications of AI errors or misinterpretations can be substantial. In such scenarios, full autonomy—where AI systems function independently without any human intervention—may prove to be imprudent. HITL acknowledges this reality and emphasizes that even with rapidly advancing AI technologies, human oversight, strategic input, and collaborative interactions remain indispensable.

> HITL 的核心，是让 AI 在伦理与安全边界内运转，并尽可能高效地达成目标。在复杂、含糊或高风险场景里，误判代价高昂，这一要求尤为迫切。此时若追求「零人工、全自主」，往往并不审慎。HITL 正视这一点：技术进步再快，人类的监督、战略性的参与与协同仍不可被替代。

The HITL approach fundamentally revolves around the idea of synergy between artificial and human intelligence. Rather than viewing AI as a replacement for human workers, HITL positions AI as a tool that augments and enhances human capabilities. This augmentation can take various forms, from automating routine tasks to providing data-driven insights that inform human decisions. The end goal is to create a collaborative ecosystem where both humans and AI Agents can leverage their distinct strengths to achieve outcomes that neither could accomplish alone.

> HITL 的底层逻辑是人机协同，而非以 AI 取代人类：AI 被视为放大与延伸人类能力的工具。其落地形态十分多样，从自动化重复性工作，到以数据洞察辅助决策，皆属此列。最终目标是构建一种协作生态，让人与智能体各展所长，完成任何一方单独都难以达成的任务。

In practice, HITL can be implemented in diverse ways. One common approach involves humans acting as validators or reviewers, examining AI outputs to ensure accuracy and identify potential errors. Another implementation involves humans actively guiding AI behavior, providing feedback or making corrections in real-time. In more complex setups, humans may collaborate with AI as partners, jointly solving problems or making decisions through interactive dialog or shared interfaces. Regardless of the specific implementation, the HITL pattern underscores the importance of maintaining human control and oversight, ensuring that AI systems remain aligned with human ethics, values, goals, and societal expectations.

> 在实践中，HITL 的实现路径十分多样：人类既可作为校验者或审核者，把控输出质量并识别潜在错误；也可在实时交互中持续纠偏，引导模型行为。更复杂的形态则是人机协同，通过对话或共享界面共同解题、联合决策。无论采用何种形式，其核心始终是保留人的掌控与监督，使系统与伦理、价值观、业务目标及社会预期保持一致。

## Human-in-the-Loop Pattern Overview

The Human-in-the-Loop (HITL) pattern integrates artificial intelligence with human input to enhance Agent capabilities. This approach acknowledges that optimal AI performance frequently requires a combination of automated processing and human insight, especially in scenarios with high complexity or ethical considerations. Rather than replacing human input, HITL aims to augment human abilities by ensuring that critical judgments and decisions are informed by human understanding.

> HITL 将人类输入嵌入 AI 流程，用于提升智能体的能力上限。它承认，最佳表现往往来自「自动化处理 + 人类判断」的结合，尤其是在高度复杂或涉及伦理考量的场景中更是如此。其目的并非消除人的参与，而是确保关键裁决始终建立在人类理解之上，从而整体放大人的能力。

HITL encompasses several key aspects: Human Oversight, which involves monitoring AI agent performance and output (e.g., via log reviews or real-time dashboards) to ensure adherence to guidelines and prevent undesirable outcomes. Intervention and Correction occurs when an AI agent encounters errors or ambiguous scenarios and may request human intervention; human operators can rectify errors, supply missing data, or guide the agent, which also informs future agent improvements. Human Feedback for Learning is collected and used to refine AI models, prominently in methodologies like reinforcement learning with human feedback, where human preferences directly influence the agent's learning trajectory. Decision Augmentation is where an AI agent provides analyses and recommendations to a human, who then makes the final decision, enhancing human decision-making through AI-generated insights rather than full autonomy. Human-Agent Collaboration is a cooperative interaction where humans and AI agents contribute their respective strengths; routine data processing may be handled by the agent, while creative problem-solving or complex negotiations are managed by the human. Finally, Escalation Policies are established protocols that dictate when and how an agent should escalate tasks to human operators, preventing errors in situations beyond the agent's capability.

> HITL 通常可拆分为几个方面：**人类监督**，即通过日志复盘、实时看板等手段持续审视智能体的行为与产出，守住边界并避免偏离目标。**干预与纠正**，即当模型陷入错误、判断含糊或主动请求帮助时，由人工纠错、补充数据并提供方向，这些信号也会反哺后续迭代。**人类反馈用于学习**，即将人的偏好与标注回流到训练流程，在 RLHF 等范式中尤为典型，能够直接影响模型的学习轨迹。**决策增强**，即由模型提供分析与建议，而最终决策权仍掌握在人手中，用 AI 放大判断质量而非取代裁决。**人机协作**，即由智能体处理批量化、结构化事务，将创造性问题求解或复杂谈判保留给人。**升级策略**，即预先明确何时、如何将任务移交给人，避免系统在能力边界之外勉强运行。

Implementing HITL patterns enables the use of Agents in sensitive sectors where full autonomy is not feasible or permitted. It also provides a mechanism for ongoing improvement through feedback loops. For example, in finance, the final approval of a large corporate loan requires a human loan officer to assess qualitative factors like leadership character. Similarly, in the legal field, core principles of justice and accountability demand that a human judge retain final authority over critical decisions like sentencing, which involve complex moral reasoning.

> 引入 HITL 后，智能体才更有可能进入那些「完全自主既不现实，也不合规」的敏感行业，并借助反馈闭环持续演进。例如，在金融业中，大额对公贷款的最终审批通常仍需信贷员评估管理层素质等定性因素；在司法场景里，量刑等涉及深层价值判断的决定，也应继续由法官保留最终裁决权，以维护正义与问责的底线。

**Caveats:** Despite its benefits, the HITL pattern has significant caveats, chief among them being a lack of scalability. While human oversight provides high accuracy, operators cannot manage millions of tasks, creating a fundamental trade-off that often requires a hybrid approach combining automation for scale and HITL for accuracy. Furthermore, the effectiveness of this pattern is heavily dependent on the expertise of the human operators; for example, while an AI can generate software code, only a skilled developer can accurately identify subtle errors and provide the correct guidance to fix them. This need for expertise also applies when using HITL to generate training data, as human annotators may require special training to learn how to correct an AI in a way that produces high-quality data. Lastly, implementing HITL raises significant privacy concerns, as sensitive information must often be rigorously anonymized before it can be exposed to a human operator, adding another layer of process complexity.

> **注意：** HITL 并非万能方案，其最大短板在于可扩展性。人工把关固然准确，但难以覆盖百万级任务量，因此常见折中是「自动化承担规模，HITL 保证精度」。同时，其效果高度依赖执行人员的专业水平：模型或许能够生成代码，但只有经验丰富的工程师才能识别隐蔽缺陷并提出可靠修正。若将 HITL 用于生成训练数据，标注人员往往还需要接受专门培训，学习如何以有利于模型学习的方式进行纠正。此外，隐私治理成本也较高：敏感信息通常需要在暴露给人工处理前完成严格匿名化或脱敏，这会进一步增加流程复杂度。

## Practical Applications & Use Cases

The Human-in-the-Loop pattern is vital across a wide range of industries and applications, particularly where accuracy, safety, ethics, or nuanced understanding are paramount.

> HITL 横跨众多行业与场景，在准确性、安全、伦理合规或细腻判断比速度更重要的地方尤为关键。

* **Content Moderation:** AI agents can rapidly filter vast amounts of online content for violations (e.g., hate speech, spam). However, ambiguous cases or borderline content are escalated to human moderators for review and final decision, ensuring nuanced judgment and adherence to complex policies.  
* **Autonomous Driving:** While self-driving cars handle most driving tasks autonomously, they are designed to hand over control to a human driver in complex, unpredictable, or dangerous situations that the AI cannot confidently navigate (e.g., extreme weather, unusual road conditions).  
* **Financial Fraud Detection:** AI systems can flag suspicious transactions based on patterns. However, high-risk or ambiguous alerts are often sent to human analysts who investigate further, contact customers, and make the final determination on whether a transaction is fraudulent.  
* **Legal Document Review:** AI can quickly scan and categorize thousands of legal documents to identify relevant clauses or evidence. Human legal professionals then review the AI's findings for accuracy, context, and legal implications, especially for critical cases.  
* **Customer Support (Complex Queries):** A chatbot might handle routine customer inquiries. If the user's problem is too complex, emotionally charged, or requires empathy that the AI cannot provide, the conversation is seamlessly handed over to a human support agent.  
* **Data Labeling and Annotation:** AI models often require large datasets of labeled data for training. Humans are put in the loop to accurately label images, text, or audio, providing the ground truth that the AI learns from. This is a continuous process as models evolve.  
* **Generative AI Refinement:** When an LLM generates creative content (e.g., marketing copy, design ideas), human editors or designers review and refine the output, ensuring it meets brand guidelines, resonates with the target audience, and maintains quality.  
* **Autonomous Networks:** AI systems are capable of analyzing alerts and forecasting network issues and traffic anomalies by leveraging key performance indicators (KPIs) and identified patterns. Nevertheless, crucial decisions—such as addressing high-risk alerts—are frequently escalated to human analysts. These analysts conduct further investigation and make the ultimate determination regarding the approval of network changes.

> * **内容审核：** 模型可先大批量过滤明显违规（仇恨言论、垃圾信息等），但灰度案例应交人工终审，以兼顾政策细则与语境判断。
> * **自动驾驶：** 日常可由系统自驾，遇极端天气、怪异路况或高风险场景且系统信心不足时，设计上也应允许人类接管。
> * **反欺诈：** 模型负责打标可疑交易，高风险或含糊个案交给分析师深挖、联络客户并做是否欺诈的终裁。
> * **法律文档：** 模型可快速扫描并归类卷宗，以定位条款与证据；随后由律师复核其准确性、语境与法律后果，在重大案件中尤为重要。
> * **客服（复杂工单）：** 机器人消化常见问题；问题过难、情绪过重或需要真共情时，应顺滑转人工。
> * **数据标注：** 模型训练离不开高质量标注；人类进入回路以提供可靠的 ground truth，并随模型迭代持续更新数据。
> * **生成式内容：** 文案、创意稿等可由 LLM 起草，编辑/设计再按品牌与受众打磨定稿。
> * **自治网络：** 模型可基于 KPI 与模式做告警分析与容量预判，但诸如高风险告警处置、变更审批等关键动作，仍常需分析师拍板。

This pattern exemplifies a practical method for AI implementation. It harnesses AI for enhanced scalability and efficiency, while maintaining human oversight to ensure quality, safety, and ethical compliance.

> 这是一种务实的 AI 落地方式：由模型扩展吞吐、提升效率，由人类守住质量、安全与合规底线。

"Human-on-the-loop" is a variation of this pattern where human experts define the overarching policy, and the AI then handles immediate actions to ensure compliance. Let's consider two examples:

> 「人在环上」（human-on-the-loop）是 HITL 的一种变体：由人设定政策与边界，再由系统在高频、低延迟场景下自动执行，以确保持续符合规则。下面给出两个示例：

* **Automated financial trading system**: In this scenario, a human financial expert sets the overarching investment strategy and rules. For instance, the human might define the policy as: "Maintain a portfolio of 70% tech stocks and 30% bonds, do not invest more than 5% in any single company, and automatically sell any stock that falls 10% below its purchase price." The AI then monitors the stock market in real-time, executing trades instantly when these predefined conditions are met. The AI is handling the immediate, high-speed actions based on the slower, more strategic policy set by the human operator.  
* **Modern call center**:  In this setup, a human manager establishes high-level policies for customer interactions. For instance, the manager might set rules such as "any call mentioning 'service outage' should be immediately routed to a technical support specialist," or "if a customer's tone of voice indicates high frustration, the system should offer to connect them directly to a human agent." The AI system then handles the initial customer interactions, listening to and interpreting their needs in real-time. It autonomously executes the manager's policies by instantly routing the calls or offering escalations without needing human intervention for each individual case. This allows the AI to manage the high volume of immediate actions according to the slower, strategic guidance provided by the human operator.

> * **自动化交易：** 投资经理先设定总体规则，例如「组合 70% 为科技股、30% 为债券；单一公司持仓不超过 5%；跌破成本 10% 自动止损。」随后由系统在盘中实时监控市场，并在条件触发时立即执行交易，将高频执行交给机器，将策略性判断保留给人。
> * **呼叫中心：** 主管先制定「政策层」规则，例如来电提及「服务中断」则直接转接二线支持，客户语气明显焦躁时主动提供人工入口等。一线接待、意图识别与路由由系统实时完成，不必每通电话都由人工处理，但整体方向仍由人类制定的策略所约束。

## Hands-On Code Example

To demonstrate the Human-in-the-Loop pattern, an ADK agent can identify scenarios requiring human review and initiate an escalation process . This allows for human intervention in situations where the agent's autonomous decision-making capabilities are limited or when complex judgments are required. This is not an isolated feature; other popular frameworks have adopted similar capabilities. LangChain, for instance, also provides tools to implement these types of interactions.

> 在演示 HITL 时，可以使用 ADK 智能体识别「需要人工复核」的场景并触发升级机制，在自主决策能力不足或需要复杂裁量时将人纳入流程。这类能力并不罕见，LangChain 等框架也提供了相近的工具链。

```python
from typing import Optional

from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from google.adk.callbacks import CallbackContext
from google.adk.models.llm import LlmRequest
from google.genai import types


# Placeholder for tools (replace with actual implementations if needed)
def troubleshoot_issue(issue: str) -> dict:
    return {"status": "success", "report": f"Troubleshooting steps for {issue}."}


def create_ticket(issue_type: str, details: str) -> dict:
    return {"status": "success", "ticket_id": "TICKET123"}


def escalate_to_human(issue_type: str) -> dict:
    # This would typically transfer to a human queue in a real system
    return {"status": "success", "message": f"Escalated {issue_type} to a human specialist."}


technical_support_agent = Agent(
    name="technical_support_specialist",
    model="gemini-2.0-flash-exp",
    instruction="""
    You are a technical support specialist for our electronics company.
    FIRST, check if the user has a support history in state["customer_info"]["support_history"].
    If they do, reference this history in your responses.

    For technical issues:
    1. Use the troubleshoot_issue tool to analyze the problem.
    2. Guide the user through basic troubleshooting steps.
    3. If the issue persists, use create_ticket to log the issue.

    For complex issues beyond basic troubleshooting:
    1. Use escalate_to_human to transfer to a human specialist.

    Maintain a professional but empathetic tone. Acknowledge the frustration technical issues can cause,
    while providing clear steps toward resolution.
    """,
    tools=[troubleshoot_issue, create_ticket, escalate_to_human],
)


def personalization_callback(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmRequest]:
    """Adds personalization information to the LLM request."""
    # Get customer info from state
    customer_info = callback_context.state.get("customer_info")
    if customer_info:
        customer_name = customer_info.get("name", "valued customer")
        customer_tier = customer_info.get("tier", "standard")
        recent_purchases = customer_info.get("recent_purchases", [])

        personalization_note = (
            f"\nIMPORTANT PERSONALIZATION:\n"
            f"Customer Name: {customer_name}\n"
            f"Customer Tier: {customer_tier}\n"
        )
        if recent_purchases:
            personalization_note += f"Recent Purchases: {', '.join(recent_purchases)}\n"

        if llm_request.contents:
            # Add as a system message before the first content
            system_content = types.Content(
                role="system",
                parts=[types.Part(text=personalization_note)],
            )
            llm_request.contents.insert(0, system_content)

    return None  # Return None to continue with the modified request
```

This code offers a blueprint for creating a technical support agent using Google's ADK, designed around a HITL framework. The agent acts as an intelligent first line of support, configured with specific instructions and equipped with tools like `troubleshoot_issue`, `create_ticket`, and `escalate_to_human` to manage a complete support workflow. The escalation tool is a core part of the HITL design, ensuring complex or sensitive cases are passed to human specialists.

> 这段示例展示了如何用 Google ADK 搭建一线技术支持智能体的基本骨架，HITL 思路贯穿其中：清晰的系统指令结合 `troubleshoot_issue`、`create_ticket` 与 `escalate_to_human` 三个工具，构成完整闭环。其中，「升级到人工」是 HITL 的关键支点，用于承接复杂或敏感个案。

A key feature of this architecture is its capacity for deep personalization, achieved through a dedicated callback function. Before contacting the LLM, this function dynamically retrieves customer-specific data—such as their name, tier, and purchase history—from the agent's state. This context is then injected into the prompt as a system message, enabling the agent to provide highly tailored and informed responses that reference the user's history. By combining a structured workflow with essential human oversight and dynamic personalization, this code serves as a practical example of how the ADK facilitates the development of sophisticated and robust AI support solutions.

> 这一架构的一大亮点，是可通过回调机制实现深度个性化：在调用 LLM 前，先从 state 中提取姓名、会员等级、近期订单等信息，再注入系统消息，使回复既更贴合用户，也能引用其历史记录。将固定流程、必要的人类复核与动态上下文结合起来，可以看出 ADK 在构建高可靠客服智能体方面的工程适配性。

## At Glance

**What:** AI systems, including advanced LLMs, often struggle with tasks that require nuanced judgment, ethical reasoning, or a deep understanding of complex, ambiguous contexts. Deploying fully autonomous AI in high-stakes environments carries significant risks, as errors can lead to severe safety, financial, or ethical consequences. These systems lack the inherent creativity and common-sense reasoning that humans possess. Consequently, relying solely on automation in critical decision-making processes is often imprudent and can undermine the system's overall effectiveness and trustworthiness.

> **是什么：** 即便能力再强的 LLM，也会在需要细致判断、伦理推理或深度语境理解的任务上暴露短板。若在高风险场景中追求完全自主，一旦发生失误，安全、财务与声誉层面的代价都可能十分高昂；而纯模型系统又缺乏人类所具备的常识、创造力与价值判断。因此，在关键决策链路中完全依赖自动化，往往既不审慎，也不安全。

**Why:** The Human-in-the-Loop (HITL) pattern provides a standardized solution by strategically integrating human oversight into AI workflows. This agentic approach creates a symbiotic partnership where AI handles computational heavy-lifting and data processing, while humans provide critical validation, feedback, and intervention. By doing so, HITL ensures that AI actions align with human values and safety protocols. This collaborative framework not only mitigates the risks of full automation but also enhances the system's capabilities through continuous learning from human input. Ultimately, this leads to more robust, accurate, and ethical outcomes that neither human nor AI could achieve alone.

> **为什么：** HITL 通过将人的监督嵌入工作流，在 AI 系统中建立起稳定的人类把关机制：模型承担算力密集型处理与大规模吞吐，人类则负责审查、纠偏与经验注入。这样既有助于系统对齐价值观与安全边界，又能降低完全自动化带来的尾部风险，并借助人的反馈不断提升系统的稳定性、准确性与合规性，达到单独依赖任一方都难以实现的效果。

**Rule of Thumb:** Use this pattern when deploying AI in domains where errors have significant safety, ethical, or financial consequences, such as in healthcare, finance, or autonomous systems. It is essential for tasks involving ambiguity and nuance that LLMs cannot reliably handle, like content moderation or complex customer support escalations. Employ HITL when the goal is to continuously improve an AI model with high-quality, human-labeled data or to refine generative AI outputs to meet specific quality standards.

> **经验法则：** 只要错误代价会直接体现在安全、伦理或财务层面（如医疗、金融、载具/机器人等场景），就应认真考虑引入 HITL。对于灰度较大、边界细腻、模型容易凭经验臆断的任务，例如内容审核或复杂客服升级，HITL 几乎是默认配置。若希望依靠高质量人工数据持续迭代模型，或将生成内容提升到可发布水准，也同样离不开人在回路中的参与。

**Visual Summary:**

> **可视化摘要：**

![Human in the Loop Design Pattern](../assets-new/Human_in_the_Loop_Design_Pattern.png)

Fig.1: Human in the loop design pattern

> 图 1：人在回路中（HITL）设计模式

## Key Takeaways

Key takeaways include:

> 可重点把握以下几点：

* Human-in-the-Loop (HITL) integrates human intelligence and judgment into AI workflows.  
* It's crucial for safety, ethics, and effectiveness in complex or high-stakes scenarios.  
* Key aspects include human oversight, intervention, feedback for learning, and decision augmentation.  
* Escalation policies are essential for agents to know when to hand off to a human.  
* HITL allows for responsible AI deployment and continuous improvement.  
* The primary drawbacks of Human-in-the-Loop are its inherent lack of scalability, creating a trade-off between accuracy and volume, and its dependence on highly skilled domain experts for effective intervention.
* Its implementation presents operational challenges, including the need to train human operators for data generation and to address privacy concerns by anonymizing sensitive information.

> * HITL 把人的判断嵌进 AI 流水线。
> * 复杂、高风险场景里，它直接关系到安全、伦理与业务效果。
> * 常见抓手：监督、临场干预、反馈驱动学习、决策增强。
> * 要写清升级规则：机器何时必须交棒给人。
> * 有助于负责任部署与持续迭代。
> * 代价在于可扩展性：精度与吞吐往往难以兼得，而且会持续占用专家资源。
> * 运营上还要培训标注/审核人员，并处理敏感数据的脱敏与合规。

## Conclusion

This chapter explored the vital Human-in-the-Loop (HITL) pattern, emphasizing its role in creating robust, safe, and ethical AI systems. We discussed how integrating human oversight, intervention, and feedback into agent workflows can significantly enhance their performance and trustworthiness, especially in complex and sensitive domains. The practical applications demonstrated HITL's widespread utility, from content moderation and medical diagnosis to autonomous driving and customer support. The conceptual code example provided a glimpse into how ADK can facilitate these human-agent interactions through escalation mechanisms. As AI capabilities continue to advance, HITL remains a cornerstone for responsible AI development, ensuring that human values and expertise remain central to intelligent system design.

> 本章聚焦 HITL，讨论它如何帮助构建稳健、安全且符合伦理要求的 AI 系统。将监督、干预与反馈嵌入智能体流程，能够显著提升系统表现与可信度，这一点在复杂、敏感领域尤为明显。文中用例覆盖内容审核、医疗辅助、自动驾驶与客户服务等场景；示例代码则展示了 ADK 如何通过「升级」机制串联人机协同。随着 AI 能力持续增强，HITL 仍将是负责任研发的重要基座，因为人类的价值判断与专业经验应长期处于系统设计的核心位置。

## References

> 参考文献：以下条目保留英文与原始链接，不作逐条翻译。

1. A Survey of Human-in-the-loop for Machine Learning, Xingjiao Wu, Luwei Xiao, Yixuan Sun, Junhang Zhang, Tianlong Ma, Liang He, [https://arxiv.org/abs/2108.00941](https://arxiv.org/abs/2108.00941)
