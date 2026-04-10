# Preface

Welcome to "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems." As we look across the landscape of modern artificial intelligence, we see a clear evolution from simple, reactive programs to sophisticated, autonomous entities capable of understanding context, making decisions, and interacting dynamically with their environment and other systems. These are the intelligent agents and the agentic systems they comprise.

> 欢迎阅读《Agentic Design Patterns：构建智能系统的实践指南》。纵览当代人工智能，可见一条清晰演进：从简单、被动的程序，到能理解情境、做出决策，并与环境及其他系统动态交互的复杂自主实体——亦即智能体，以及由它们构成的智能体化系统。

The advent of powerful large language models (LLMs) has provided unprecedented capabilities for understanding and generating human-like content such as text and media, serving as the cognitive engine for many of these agents. However, orchestrating these capabilities into systems that can reliably achieve complex goals requires more than just a powerful model. It requires structure, design, and a thoughtful approach to how the agent perceives, plans, acts, and interacts.

> 强大的大语言模型（LLM）带来了前所未有的能力：理解与生成类人内容（如文本与媒体），并成为许多智能体的认知引擎。然而，要把这些能力编排成能可靠达成复杂目标的系统，单靠强大模型远远不够；还需要结构、设计，以及对智能体如何感知、规划、行动与交互的审慎考量。

Think of building intelligent systems as creating a complex work of art or engineering on a canvas. This canvas isn't a blank visual space, but rather the underlying infrastructure and frameworks that provide the environment and tools for your agents to exist and operate. It's the foundation upon which you'll build your intelligent application, managing state, communication, tool access, and the flow of logic.

> 不妨把构建智能系统想象成在一张“画布”上完成一件复杂的艺术或工程作品。这张画布并非空白平面，而是底层基础设施与框架——它为智能体提供存在与运行所需的环境与工具；也是你搭建智能应用的地基，承载状态、通信、工具访问与逻辑流转。

Building effectively on this agentic canvas demands more than just throwing components together. It requires understanding proven techniques – **patterns** – that address common challenges in designing and implementing agent behavior. Just as architectural patterns guide the construction of a building, or design patterns structure software, agentic design patterns provide reusable solutions for the recurring problems you'll face when bringing intelligent agents to life on your chosen canvas.

> 要在智能体化画布上有效构建，不能仅靠堆砌组件；需要掌握经实践检验的方法——**模式**——来应对设计与实现智能体行为时的常见难题。正如建筑模式指导营造、设计模式组织软件，智能体化设计模式为你在选定画布上落地智能体时反复遭遇的问题提供可复用解法。

## What are Agentic Systems?

At its core, an agentic system is a computational entity designed to perceive its environment (both digital and potentially physical), make informed decisions based on those perceptions and a set of predefined or learned goals, and execute actions to achieve those goals autonomously. Unlike traditional software, which follows rigid, step-by-step instructions, agents exhibit a degree of `flexibility` and `initiative`.

> 本质上，智能体系统（`Agentic System`）是一种计算实体：感知环境（数字环境，以及可能的物理环境），在感知与一组预设或习得的目标基础上做出知情决策，并自主行动以达成目标。与传统软件遵循僵硬的逐步指令不同，智能体展现出一定的`灵活性`与`主动性`。

Imagine you need a system to manage customer inquiries. A traditional system might follow a fixed script. An agentic system, however, could perceive the nuances of a customer's query, access knowledge bases, interact with other internal systems (like order management), potentially ask clarifying questions, and proactively resolve the issue, perhaps even anticipating future needs. These agents operate on the canvas of your application's infrastructure, utilizing the services and data available to them.

> 设想你需要一套处理客户咨询的系统：传统方案往往照固定脚本推进；智能体化系统却能捕捉客户问题的细微差别、检索知识库、与订单管理等内部系统联动，必要时追问澄清，并主动推进解决，甚至预判后续需求。这些智能体运行在你应用基础设施这张画布上，调用可用的服务与数据。

Agentic systems are often characterized by features like **autonomy**, allowing them to act without constant human oversight; **proactiveness**, initiating actions towards their goals; and **reactiveness**, responding effectively to changes in their environment. They are fundamentally **goal-oriented**, constantly working towards objectives. A critical capability is **tool use**, enabling them to interact with external APIs, databases, or services – effectively reaching out beyond their immediate canvas. They possess **memory**, retain information across interactions, and can engage in **communication** with users, other systems, or even other agents operating on the same or connected canvases.

> 智能体化系统的典型特征包括：**自主性**（无需持续人工盯守也能行动）、**主动性**（主动朝目标推进）、**反应性**（对环境变化做出有效响应）。它们从根本上是**目标导向**的。关键能力还包括**工具使用**（调用外部 API、数据库或服务，实质上将能力延展到画布之外）、**记忆**（跨多轮交互保留信息），以及**通信**（与用户、其他系统，或同一画布及互联画布上的其他智能体交互）。

Effectively realizing these characteristics introduces significant complexity. How does the agent maintain state across multiple steps on its canvas? How does it decide *when* and *how* to use a tool? How is communication between different agents managed? How do you build resilience into the system to handle unexpected outcomes or errors?

> 要真正把上述特征落地，会引入显著复杂性：智能体如何在多步流程中维持画布上的状态？如何决定*何时*、*如何*调用工具？多智能体之间的通信如何治理？怎样为系统注入韧性，以消化意外结果或错误？

## Why Patterns Matter in Agent Development

This complexity is precisely why agentic design patterns are indispensable. They are not rigid rules, but rather battle-tested templates or blueprints that offer proven approaches to standard design and implementation challenges in the agentic domain. By recognizing and applying these design patterns, you gain access to solutions that enhance the structure, maintainability, reliability, and efficiency of the agents you build on your canvas.

> 这种复杂性，正是智能体化设计模式不可或缺的原因。它们不是僵死的教条，而是经实战检验的模板与蓝图，为智能体领域常见的设计与实现难题提供成熟路径。识别并运用这些模式，有助于提升你在画布上所构建智能体的结构清晰度、可维护性、可靠性与效率。

Using design patterns helps you avoid reinventing fundamental solutions for tasks like managing conversational flow, integrating external capabilities, or coordinating multiple agent actions. They provide a common language and structure that makes your agent's logic clearer and easier for others (and yourself in the future) to understand and maintain. Implementing patterns designed for error handling or state management directly contributes to building more robust and reliable systems. Leveraging these established approaches accelerates your development process, allowing you to focus on the unique aspects of your application rather than the foundational mechanics of agent behavior.

> 使用设计模式，可以避免在对话流管理、外部能力集成或多智能体协同等任务上反复“造轮子”。它们提供共同的语言与结构，让智能体逻辑更易理解，也更便于交接给“未来的自己”。面向错误处理或状态管理的模式，能直接夯实系统的稳健性与可靠性。借助这些成熟做法，你可以加快交付节奏，把精力集中在应用的独特价值上，而不是智能体行为的底层机制上。

This book extracts 21 key design patterns that represent fundamental building blocks and techniques for constructing sophisticated agents on various technical canvases. Understanding and applying these patterns will significantly elevate your ability to design and implement intelligent systems effectively.

> 本书提炼 21 个关键设计模式，涵盖在不同技术画布上构建复杂智能体所需的基本构件与常用技法。理解并运用它们，将显著提升你设计与实现智能系统的成效。

## Overview of the Book and How to Use It

This book, "Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems," is crafted to be a practical and accessible resource. Its primary focus is on clearly explaining each agentic pattern and providing concrete, runnable code examples to demonstrate its implementation. Across 21 dedicated chapters, we will explore a diverse range of design patterns, from foundational concepts like structuring sequential operations (Prompt Chaining) and external interaction (Tool Use) to more advanced topics like collaborative work (Multi-Agent Collaboration) and self-improvement (Self-Correction).

> 本书力求成为一本实用且易读的参考书：逐一讲清每种智能体化模式，并配以可运行的代码示例演示其落地方式。全书 21 章各聚焦一类模式——从顺序编排（提示链）、外部交互（工具使用）等基础话题，到多智能体协作、自我改进（自校正）等进阶主题。

The book is organized chapter by chapter, with each chapter delving into a single agentic pattern. Within each chapter, you will find:

> 全书按章编排，每章深入讲解一种智能体化模式，结构包括：

- A detailed **Pattern Overview** providing a clear explanation of the pattern and its role in agentic design.  
- A section on **Practical Applications & Use Cases** illustrating real-world scenarios where the pattern is invaluable and the benefits it brings.  
- A **Hands-On Code Example** offering practical, runnable code that demonstrates the pattern's implementation using prominent agent development frameworks. This is where you'll see how to apply the pattern within the context of a technical canvas.  
- **Key Takeaways** summarizing the most crucial points for quick review.  
- **References** for further exploration, providing resources for deeper learning on the pattern and related concepts.

> - **模式概述**：阐明模式本身及其在智能体化设计中的位置。
> - **实践应用与用例**：展示模式在真实场景中的价值与收益。
> - **动手代码示例**：基于主流智能体开发框架给出可运行代码，在技术画布的语境下演示模式。
> - **要点回顾**：提炼最关键内容，便于快速复盘。
> - **参考文献**：指向延伸阅读（文献条目仍以英文呈现，见原文）。

While the chapters are ordered to build concepts progressively, feel free to use the book as a reference, jumping to chapters that address specific challenges you face in your own agent development projects. The appendices provide a comprehensive look at advanced prompting techniques, principles for applying AI agents in real-world environments, and an overview of essential agentic frameworks. To complement this, practical online-only tutorials are included, offering step-by-step guidance on building agents with specific platforms like AgentSpace and for the command-line interface. The emphasis throughout is on practical application; we strongly encourage you to run the code examples, experiment with them, and adapt them to build your own intelligent systems on your chosen canvas.

> 各章顺序便于循序渐进，但你也可以把本书当手册，按问题跳读相关章节。附录覆盖高级提示技术、在真实环境中应用 智能体的原则，以及主要智能体化框架速览。另有仅在线发布的实践教程，分步演示如何在 AgentSpace 等平台与命令行环境中构建智能体。全书强调动手：务必运行、改写并实验示例，在你选定的画布上搭建属于自己的智能系统。

A great question I hear is, 'With AI changing so fast, why write a book that could be quickly outdated?' My motivation was actually the opposite. It's precisely because things are moving so quickly that we need to step back and identify the underlying principles that are solidifying. Patterns like RAG, Reflection, Routing, Memory and the others I discuss, are becoming fundamental building blocks. This book is an invitation to reflect on these core ideas, which provide the foundation we need to build upon. Humans need these reflection moments on foundation patterns

> 常有人问：「AI 变化这么快，为何还要写一本可能很快过时的书？」我的动机恰恰相反：正因为变化快，才更需要退后一步，辨认正在沉淀的底层原则。RAG、反思、路由、记忆等我讨论的模式，正逐渐成为基本构件。本书邀请你停下来审视这些核心思想——它们是我们继续建造的基石。人类尤其需要这种针对基础模式的「反思时刻」。

## Introduction to the Frameworks Used

To provide a tangible "canvas" for our code examples (see also Appendix), we will primarily utilize three prominent agent development frameworks. **LangChain**, along with its stateful extension **LangGraph**, provides a flexible way to chain together language models and other components, offering a robust canvas for building complex sequences and graphs of operations. **Crew AI** provides a structured framework specifically designed for orchestrating multiple AI agents, roles, and tasks, acting as a canvas particularly well-suited for collaborative agent systems. The **Google Agent Developer Kit (Google ADK)** offers tools and components for building, evaluating, and deploying agents, providing another valuable canvas, often integrated with Google's AI infrastructure.

> 为了给代码示例一张可触摸的「画布」（另见附录），我们主要采用三种主流智能体开发框架：**LangChain** 及其有状态扩展 **LangGraph**，用于灵活串联语言模型与其他组件，适合搭建复杂的操作链路与图结构；**Crew AI** 专注多智能体、角色与任务编排，尤适协作式智能体系统；**Google Agent Developer Kit（Google ADK）** 提供构建、评估与部署智能体的工具与组件，常与 Google 的 AI 基础设施协同。

These frameworks represent different facets of the agent development canvas, each with its strengths. By showing examples across these tools, you will gain a broader understanding of how the patterns can be applied regardless of the specific technical environment you choose for your agentic systems. The examples are designed to clearly illustrate the pattern's core logic and its implementation on the framework's canvas, focusing on clarity and practicality.

> 这些框架代表了智能体开发画布的不同侧面，各有所长。跨工具对照示例，有助于理解模式如何迁移到你为智能体化系统所选的具体技术栈。示例以「把模式讲清楚」为第一目标，兼顾可读与可落地。

By the end of this book, you will not only understand the fundamental concepts behind 21 essential agentic patterns but also possess the practical knowledge and code examples to apply them effectively, enabling you to build more intelligent, capable, and autonomous systems on your chosen development canvas. Let's begin this hands-on journey!

> 读完本书，你不仅将理解 21 个核心智能体化模式背后的基本概念，还将掌握将其真正落地所需的知识与代码抓手，从而在你选定的开发画布上构建更智能、更强韧、更自主的系统。让我们开启这段动手实践之旅。