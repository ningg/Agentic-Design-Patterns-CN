# Agentic Design Patterns

This repository contains the full text of the book "Agentic Design Patterns" by Antonio Gulli and Mauro Sauco. The content has been compiled and organized by Tom Mathews  for easy access and reference for the community.

> 本仓库收录 Antonio Gulli 与 Mauro Sauco 所著《Agentic Design Patterns》全书正文；内容由 Tom Mathews 整理编排，供社区查阅与参考。

Agentic Design Patterns - Book Cover

> 《Agentic Design Patterns》图书封面

## Authorship and Credit

- **Authors:** [Antonio Gulli](https://www.linkedin.com/in/searchguy/) and [Mauro Sauco](https://www.linkedin.com/in/maurosauco/)
- **Compiled by:** [Tom Mathews](https://www.linkedin.com/in/mathews-tom/)

> - **作者：** [Antonio Gulli](https://www.linkedin.com/in/searchguy/) 与 [Mauro Sauco](https://www.linkedin.com/in/maurosauco/)
> - **汇编：** [Tom Mathews](https://www.linkedin.com/in/mathews-tom/)

### What makes this book stand out?

This 424-page guide tackles the real challenges we face when building intelligent, autonomous AI systems. It bridges the gap between theory and implementation—exactly what our field needs right now. This is the best resource for anyone serious about building real AI systems. If you're an engineer, researcher, or product manager ready to move beyond basic LLM applications and build truly robust AI agents, this is for you.

> 这本 424 页的指南直面构建智能、自主 AI 系统时的真实挑战，在理论与工程实践之间搭起桥梁，恰与当下行业所需相契合。对任何希望认真打造可落地 AI 系统的人而言，它都是极具价值的参考；若你是工程师、研究员或产品经理，正准备从基础大语言模型应用迈向真正稳健的智能体系统，本书正适合你。

The book covers essential agentic patterns including Prompt Chaining, Routing, Planning, and Multi-Agent Systems, all with practical, code-based examples. You'll find comprehensive coverage of Tool Use, Memory Management, and RAG implementation, plus advanced topics like Reasoning Techniques and Inter-Agent Communication.

> 全书涵盖提示链、路由、规划与多智能体协作等核心**智能体设计模式**，均配有可运行的代码示例；同时系统讲解工具使用、记忆管理与 RAG 实现，并延伸到推理技术与智能体间通信等进阶主题。

Inside you will find:

> 书中主要内容包括：

- **Real code examples:** Not just theory, but working implementations.
- **Proven patterns:** Memory handling, exception logic, resource control, safety guardrails.
- **Advanced techniques:** Multi-agent orchestration, inter-agent messaging, human-in-the-loop.
- **Full chapter on MCP (Model Context Protocol):** A key framework for integrating tools with agents.

> - **真实代码示例：** 不止于理论，更有可运行实现。
> - **经实践检验的智能体模式：** 记忆与上下文处理、异常逻辑、资源约束、安全护栏。
> - **进阶技术：** 多智能体编排、智能体间消息传递、人在回路中（human-in-the-loop）。
> - **MCP（模型上下文协议）专章：** 将外部工具与智能体集成的关键框架。

It covers 21 core patterns across 4 sections:

> 全书分四部分介绍 21 种核心智能体模式：

1. Foundational patterns (prompt chaining, routing, tool use)
2. Advanced systems (memory, learning, monitoring)
3. Production concerns (error handling, safety, evaluation)
4. Multi-agent architectures

> 1. 基础模式（提示链、路由、工具使用）
> 2. 高级系统（记忆、学习、监控）
> 3. 生产实践关切（错误处理、安全、评估）
> 4. 多智能体架构

Most AI content stops at “how to call an API.” But in real-world systems you need to ask:

> 多数 AI 内容止步于「如何调用 API」。在真实系统中，你还需要追问：

- What if the agent gets stuck mid-task?
- How do you preserve memory across long sessions?
- How do you prevent chaos when you run 10+ agents?

> - 智能体在任务中途卡住怎么办？
> - 如何在长会话中保持记忆连贯？
> - 同时运行十余个智能体时，如何避免失控与混乱？

This book answers all that with patterns you can actually apply. The 70+ page appendix alone is worth the investment, featuring Advanced Prompting techniques and an overview of Agentic Frameworks.

> 本书以可直接落地的智能体设计模式回答上述问题。仅附录就超过 70 页，涵盖进阶提示工程与智能体开发框架概览。

## Table of Contents

### Introduction

- [Dedication](00-Introduction/01-Dedication.md)
- [Acknowledgment](00-Introduction/02-Acknowledgment.md)
- [Foreword](00-Introduction/03-Foreword.md)
- [A Thought Leader's Perspective: Power and Responsibility](00-Introduction/04-A_Thought_Leaders_Perspective_Power_and_Responsibility.md)
- [Introduction](00-Introduction/05-Introduction.md)
- [What makes an AI system an Agent?](00-Introduction/06-What_makes_an_AI_system_an_Agent.md)

> - [献辞](00-Introduction/01-Dedication.md)
> - [致谢](00-Introduction/02-Acknowledgment.md)
> - [前言](00-Introduction/03-Foreword.md)
> - [思想领袖视角：权力与责任](00-Introduction/04-A_Thought_Leaders_Perspective_Power_and_Responsibility.md)
> - [引言](00-Introduction/05-Introduction.md)
> - [怎样的 AI 系统才算智能体？](00-Introduction/06-What_makes_an_AI_system_an_Agent.md)

### Part One: Foundational Patterns

- [Chapter 1: Prompt Chaining](01-Part_One/Chapter_1-Prompt_Chaining.md)
- [Chapter 2: Routing](01-Part_One/Chapter_2-Routing.md)
- [Chapter 3: Parallelization](01-Part_One/Chapter_3-Parallelization.md)
- [Chapter 4: Reflection](01-Part_One/Chapter_4-Reflection.md)
- [Chapter 5: Tool Use (Function Calling)](01-Part_One/Chapter_5-Tool_Use_(Function_Calling).md)
- [Chapter 6: Planning](01-Part_One/Chapter_6-Planning.md)
- [Chapter 7: Multi-Agent Collaboration](01-Part_One/Chapter_7-Multi-Agent_Collaboration.md)

> - [第 1 章：提示链](01-Part_One/Chapter_1-Prompt_Chaining.md)
> - [第 2 章：路由](01-Part_One/Chapter_2-Routing.md)
> - [第 3 章：并行化](01-Part_One/Chapter_3-Parallelization.md)
> - [第 4 章：反思](01-Part_One/Chapter_4-Reflection.md)
> - [第 5 章：工具使用（函数调用）](01-Part_One/Chapter_5-Tool_Use_(Function_Calling).md)
> - [第 6 章：规划](01-Part_One/Chapter_6-Planning.md)
> - [第 7 章：多智能体协作](01-Part_One/Chapter_7-Multi-Agent_Collaboration.md)

### Part Two: Advanced Systems

- [Chapter 8: Memory Management](02-Part_Two/Chapter_8-Memory_Management.md)
- [Chapter 9: Learning and Adaptation](02-Part_Two/Chapter_9-Learning_and_Adaptation.md)
- [Chapter 10: Model Context Protocol (MCP)](02-Part_Two/Chapter_10-Model_Context_Protocol_(MCP).md)
- [Chapter 11: Goal Setting and Monitoring](02-Part_Two/Chapter_11-Goal_Setting_and_Monitoring.md)

> - [第 8 章：记忆管理](02-Part_Two/Chapter_8-Memory_Management.md)
> - [第 9 章：学习与适应](02-Part_Two/Chapter_9-Learning_and_Adaptation.md)
> - [第 10 章：模型上下文协议（MCP）](02-Part_Two/Chapter_10-Model_Context_Protocol_(MCP).md)
> - [第 11 章：目标设定与监控](02-Part_Two/Chapter_11-Goal_Setting_and_Monitoring.md)

### Part Three: Production Concerns

- [Chapter 12: Exception Handling and Recovery](03-Part_Three/Chapter_12-Exception_Handling_and_Recovery.md)
- [Chapter 13: Human in the Loop](03-Part_Three/Chapter_13-Human_in_the_Loop.md)
- [Chapter 14: Knowledge Retrieval (RAG)](03-Part_Three/Chapter_14-Knowledge_Retrieval_(RAG).md)

> - [第 12 章：异常处理与恢复](03-Part_Three/Chapter_12-Exception_Handling_and_Recovery.md)
> - [第 13 章：人在回路中](03-Part_Three/Chapter_13-Human_in_the_Loop.md)
> - [第 14 章：知识检索（RAG）](03-Part_Three/Chapter_14-Knowledge_Retrieval_(RAG).md)

### Part Four: Multi-Agent Architectures

- [Chapter 15: Inter-Agent Communication (A2A)](04-Part_Four/Chapter_15-Inter_Agent_Communication_(A2A).md)
- [Chapter 16: Resource-Aware Optimization](04-Part_Four/Chapter_16-Resource_Aware_Optimization.md)
- [Chapter 17: Reasoning Techniques](04-Part_Four/Chapter_17-Reasoning_Techniques.md)
- [Chapter 18: Guardrails and Safety Patterns](04-Part_Four/Chapter_18-Guardrails_Safety_Patterns.md)
- [Chapter 19: Evaluation and Monitoring](04-Part_Four/Chapter_19-Evaluation_and_Monitoring.md)
- [Chapter 20: Prioritization](04-Part_Four/Chapter_20-Prioritization.md)
- [Chapter 21: Exploration and Discovery](04-Part_Four/Chapter_21-Exploration_and_Discovery.md)

> - [第 15 章：智能体间通信（A2A）](04-Part_Four/Chapter_15-Inter_Agent_Communication_(A2A).md)
> - [第 16 章：资源感知优化](04-Part_Four/Chapter_16-Resource_Aware_Optimization.md)
> - [第 17 章：推理技术](04-Part_Four/Chapter_17-Reasoning_Techniques.md)
> - [第 18 章：护栏与安全模式](04-Part_Four/Chapter_18-Guardrails_Safety_Patterns.md)
> - [第 19 章：评估与监控](04-Part_Four/Chapter_19-Evaluation_and_Monitoring.md)
> - [第 20 章：优先级排序](04-Part_Four/Chapter_20-Prioritization.md)
> - [第 21 章：探索与发现](04-Part_Four/Chapter_21-Exploration_and_Discovery.md)

### Appendix

- [Appendix A: Advanced Prompting Techniques](05-Appendix/Appendix_A-Advanced_Prompting_Techniques.md)
- [Appendix B: AI Agentic Interactions: From GUI to Real-World Environment](05-Appendix/Appendix_B-AI_Agentic_Interactions_From_GUI_to_Real_World_Environment.md)
- [Appendix C: Quick Overview of Agentic Frameworks](05-Appendix/Appendix_C-Quick_Overview_of_Agentic_Frameworks.md)
- [Appendix D: Building an Agent with AgentSpace (online only)](05-Appendix/Appendix_D-Building_an_Agent_with_AgentSpace_(on_line_only).md)
- [Appendix E - AI Agents on the CLI](05-Appendix/Appendix_E-AI_Agents_on_the_CLI.md)
- [Appendix F: Under the Hood: An Inside Look at the Agent's Reasoning Engines](05-Appendix/Appendix_F-Under_the_Hood_An_Inside_Look_at_the_Agents_Reasoning_Engines.md)
- [Appendix G: Coding Agents](05-Appendix/Appendix_G-Coding_Agents.md)

> - [附录 A：高级提示技巧](05-Appendix/Appendix_A-Advanced_Prompting_Techniques.md)
> - [附录 B：智能体交互：从图形界面到真实世界环境](05-Appendix/Appendix_B-AI_Agentic_Interactions_From_GUI_to_Real_World_Environment.md)
> - [附录 C：智能体设计与开发框架速览](05-Appendix/Appendix_C-Quick_Overview_of_Agentic_Frameworks.md)
> - [附录 D：使用 AgentSpace 构建智能体（仅在线）](05-Appendix/Appendix_D-Building_an_Agent_with_AgentSpace_(on_line_only).md)
> - [附录 E：命令行上的智能体](05-Appendix/Appendix_E-AI_Agents_on_the_CLI.md)
> - [附录 F：幕后揭秘：智能体推理引擎内窥](05-Appendix/Appendix_F-Under_the_Hood_An_Inside_Look_at_the_Agents_Reasoning_Engines.md)
> - [附录 G：编程智能体](05-Appendix/Appendix_G-Coding_Agents.md)

## License

This repository is licensed under the [MIT License](LICENSE.md).

> 本仓库采用 [MIT 许可证](LICENSE.md) 授权。

Agentic Design Patterns

> 《Agentic Design Patterns》（智能体设计模式）

