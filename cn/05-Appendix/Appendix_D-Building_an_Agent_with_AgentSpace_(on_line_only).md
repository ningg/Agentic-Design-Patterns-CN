# Appendix D - Building an Agent with AgentSpace

> **附录 D：使用 AgentSpace 构建智能体**

## Overview

> ## 概述

AgentSpace is a platform designed to facilitate an "agent-driven enterprise" by integrating artificial intelligence into daily workflows. At its core, it provides a unified search capability across an organization's entire digital footprint, including documents, emails, and databases. This system utilizes advanced AI models, like Google's Gemini, to comprehend and synthesize information from these varied sources.

> AgentSpace 旨在把人工智能嵌入日常流程，助力打造「智能体驱动型企业」。其核心之一，是在组织的全量数字足迹（文档、邮件、数据库等）上提供统一检索；借助 Google Gemini 等先进模型，理解并综合这些异构来源中的信息。

The platform enables the creation and deployment of specialized AI "agents" that can perform complex tasks and automate processes. These agents are not merely chatbots; they can reason, plan, and execute multi-step actions autonomously. For instance, an agent could research a topic, compile a report with citations, and even generate an audio summary.

> 平台支持创建与部署能够承担复杂任务及流程自动化的专业 AI“智能体”。它们远不止是聊天机器人，而是能够拆解目标、制定步骤并自主执行任务的系统，例如完成主题调研、生成带引用的报告，或产出音频版摘要。

To achieve this, AgentSpace constructs an enterprise knowledge graph, mapping the relationships between people, documents, and data. This allows the AI to understand context and deliver more relevant and personalized results. The platform also includes a no-code interface called Agent Designer for creating custom agents without requiring deep technical expertise.

> 为实现这一点，平台会构建企业级知识图谱，将人员、文档与数据之间的关系显式化，从而使模型给出的回答更贴近业务场景，也更具个性化。平台还提供名为 Agent Designer 的无代码界面，使业务人员也能组合并配置专属智能体。

Furthermore, AgentSpace supports a multi-agent system where different AI agents can communicate and collaborate through an open protocol known as the Agent2Agent (A2A) Protocol. This interoperability allows for more complex and orchestrated workflows. Security is a foundational component, with features like role-based access controls and data encryption to protect sensitive enterprise information. Ultimately, AgentSpace aims to enhance productivity and decision-making by embedding intelligent, autonomous systems directly into an organization's operational fabric.

> 多智能体协作则依托开放的 Agent2Agent（A2A）协议，使不同智能体能够彼此分派任务并同步状态，从而编排更长链条的业务流程。在安全层面，平台原生提供 RBAC、加密等企业级控制能力。整体目标是将“能够自主办理事务”的 AI 嵌入日常运营流程，提升人效与决策质量。

## How to build an Agent with AgentSpace UI

> ## 如何通过 AgentSpace 界面构建智能体

Figure 1 illustrates how to access AgentSpace by selecting AI Applications from the Google Cloud Console.

> 图 1：在 Google Cloud 控制台经由 AI Applications 进入 AgentSpace 的路径示意。

![GCP: Access AgentSpace](../assets-new/GCP_Access_AgentSpace.png)

Fig. 1:  How to use Google Cloud Console to access AgentSpace

> 图 1：如何使用 Google Cloud Console 访问 AgentSpace

Your agent can be connected to various services, including Calendar, Google Mail, Workaday, Jira, Outlook, and Service Now (see Fig. 2).

> 智能体可与 Calendar、Google Mail、Workaday、Jira、Outlook、Service Now 等系统对接（见图 2）。

![GCP: Integrate with diverse services](../assets-new/GCP_Integrate_with_diverse_services.png)

Fig. 2: Integrate with diverse services, including Google and third-party platforms.

> 图 2：与多种服务集成，包括 Google 与第三方平台。

The Agent can then utilize its own prompt, chosen from a gallery of pre-made prompts provided by Google, as illustrated in Fig. 3\.

> 接着可为智能体选定提示：可直接采用 Google 预制模板，如图 3。

![GCP: Googles Gallery of Pre-Assembled Prompts](../assets-new/GCP_Googles_Gallery_of_Pre_Assembled_Prompts.png)

Fig.3: Google's Gallery of Pre-assembled  prompts

> 图 3：Google 的预制提示库

In alternative you can create your own prompt as in Fig.4, which will be then used by your agent  

> 亦可参照图 4 自行编写提示，交由智能体使用。

![GCP: Customizing the Agent's Prompt](../assets-new/GCP_Customizing_the_Agents_Prompt.png)

Fig.4: Customizing the Agent's Prompt

> 图 4：自定义智能体的提示

AgentSpace offers a number of advanced features such as integration with datastores to store your own data, integration with Google Knowledge Graph or with your private Knowledge Graph, Web interface for exposing your agent to the Web, and Analytics to monitor usage, and more (see Fig. 5\)

> AgentSpace 还提供多种高级能力：对接数据存储以托管自有数据、对接 Google 知识图谱或私有知识图谱、通过 Web 界面将智能体对外开放，以及用于观测使用情况的 Analytics 等（见图 5）。

![GCP: AgentSpace Advanced Capabilities](../assets-new/GCP_AgentSpace_Advanced_Capabilities.png)

Fig. 5: AgentSpace advanced capabilities

> 图 5：AgentSpace 高级能力

Upon completion, the AgentSpace chat interface (Fig. 6\) will be accessible.

> 配置结束后，即可在 AgentSpace 对话界面中与智能体交互（图 6）。

![GCP: AgentSpace User Interface for initiating a chat with your Agent](../assets-new/GCP_AgentSpace_User_Interface_for_initiating_a_chat_with_your_Agent.png)

Fig. 6: The AgentSpace User Interface for initiating a chat with your Agent.

> 图 6：用于与智能体发起聊天的 AgentSpace 用户界面

## Conclusion

> ## 结语

In conclusion, AgentSpace provides a functional framework for developing and deploying AI agents within an organization's existing digital infrastructure. The system's architecture links complex backend processes, such as autonomous reasoning and enterprise knowledge graph mapping, to a graphical user interface for agent construction. Through this interface, users can configure agents by integrating various data services and defining their operational parameters via prompts, resulting in customized, context-aware automated systems.

> 综上，AgentSpace 提供了一条在既有 IT 基础设施上落地 智能体的完整路径：后端承载推理、知识图谱等企业级能力，前端则通过可视化向导将数据源、提示与发布方式串联起来，最终形成可定制、具备上下文感知能力的自动化助手。

This approach abstracts the underlying technical complexity, enabling the construction of specialized multi-agent systems without requiring deep programming expertise. The primary objective is to embed automated analytical and operational capabilities directly into workflows, thereby increasing process efficiency and enhancing data-driven analysis. For practical instruction, hands-on learning modules are available, such as the "Build a Gen AI Agent with Agentspace" lab on Google Cloud Skills Boost, which provides a structured environment for skill acquisition.

> 这种做法把底层技术复杂度收进平台，使团队在缺乏深厚编程背景时仍能搭建专业化的多智能体应用。首要目标是把自动化分析与运营能力嵌进业务流程，提升效率并强化数据驱动决策。动手实践可参考 Google Cloud Skills Boost 上的实验课，例如「使用 Agentspace 构建生成式 智能体」，在结构化实验环境中掌握关键技能。

## References

1. Create a no-code agent with Agent Designer, [https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer](https://cloud.google.com/agentspace/agentspace-enterprise/docs/agent-designer)
2. Google Cloud Skills Boost, [https://www.cloudskillsboost.google/](https://www.cloudskillsboost.google/)
