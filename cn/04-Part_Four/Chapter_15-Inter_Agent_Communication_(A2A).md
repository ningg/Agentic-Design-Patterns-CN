# Chapter 15: Inter-Agent Communication (A2A)

> 第十五章：智能体间通信（A2A）

Individual AI agents often face limitations when tackling complex, multifaceted problems, even with advanced capabilities. To overcome this, Inter-Agent Communication (A2A) enables diverse AI agents, potentially built with different frameworks, to collaborate effectively. This collaboration involves seamless coordination, task delegation, and information exchange.

> 即便单体能力突出，单一 智能体面对复杂、多侧面的任务时仍往往力不从心。智能体间通信（A2A）让多种、且可能基于不同框架构建的智能体能够协同工作，实现顺畅协调、任务委派与信息交换。

Google's A2A protocol is an open  standard designed to facilitate this universal communication. This chapter will explore A2A, its practical applications, and its implementation within the Google ADK.

> Google 的 A2A 协议是促进这类通用互连的开放标准。本章将介绍 A2A 的核心思想、实际应用场景，以及在 Google ADK 中的实现方式。

## Inter-Agent Communication Pattern Overview

> ## 智能体间通信模式概览

The Agent2Agent (A2A) protocol is an open standard designed to enable communication and collaboration between different AI agent frameworks. It ensures interoperability, allowing AI agents developed with technologies like LangGraph, CrewAI, or Google ADK to work together regardless of their origin or framework differences.

> Agent2Agent（A2A）协议是开放标准，用于在不同 智能体框架之间建立通信与协作。它保障互操作性，使基于 LangGraph、CrewAI 或 Google ADK 等技术的智能体，无论出自哪家、采用何种框架，都能协同工作。

A2A is supported by a range of technology companies and service providers, including Atlassian, Box, LangChain, MongoDB, Salesforce, SAP, and ServiceNow. Microsoft plans to integrate A2A into Azure AI Foundry and Copilot Studio, demonstrating its commitment to open protocols. Additionally, Auth0 and SAP are integrating A2A support into their platforms and agents.

> A2A 已获多家科技公司与服务商支持，包括 Atlassian、Box、LangChain、MongoDB、Salesforce、SAP 与 ServiceNow。微软计划将 A2A 纳入 Azure AI Foundry 与 Copilot Studio，彰显对开放协议的长期投入。Auth0 与 SAP 等也在将 A2A 能力接入各自平台与智能体产品。

As an open-source protocol, A2A welcomes community contributions to facilitate its evolution and widespread adoption.

> 作为开源协议，A2A 欢迎社区参与共建，推动协议演进与更广泛采纳。

## Core Concepts of A2A

> ## A2A 的核心概念

The A2A protocol provides a structured approach for agent interactions, built upon several core concepts. A thorough grasp of these concepts is crucial for anyone developing or integrating with A2A-compliant systems. The foundational pillars of A2A include Core Actors, Agent Card, Agent Discovery, Communication and Tasks,  Interaction mechanisms, and Security, all of which will be reviewed in detail.

> A2A 协议以若干核心概念为基础，为智能体交互提供结构化框架。在开发或集成符合 A2A 的系统之前，应先充分理解这些概念。其核心支柱包括：核心参与者、智能体卡片（Agent Card）、智能体发现、通信与任务、交互机制与安全；下文将分节说明。

**Core Actors:** A2A involves three main entities:

> **核心参与者：** A2A 体系中有三类主要角色：

* User: Initiates requests for agent assistance.  
* A2A Client (Client Agent): An application or AI agent that acts on the user's behalf to request actions or information.  
* A2A Server (Remote Agent): An AI agent or system that provides an HTTP endpoint to process client requests and return results. The remote agent operates as an "opaque" system, meaning the client does not need to understand its internal operational details.

> * 用户：发起需要智能体协助的请求。
> * A2A 客户端（Client Agent）：代表用户去请求操作或获取信息的应用或 智能体。
> * A2A 服务端（Remote Agent）：提供 HTTP 端点处理客户端请求并返回结果的 智能体或系统。远端智能体以黑盒方式对外提供服务，客户端无须知晓其内部实现。

**Agent Card:** An agent's digital identity is defined by its Agent Card, usually a JSON file. This file contains key information for client interaction and automatic discovery, including the agent's identity, endpoint URL, and version. It also details supported capabilities like streaming or push notifications, specific skills, default input/output modes, and authentication requirements. Below is an example of an Agent Card for a WeatherBot.

> **智能体卡片（Agent Card）：** Agent Card 定义智能体的数字身份，一般为 JSON 文件，汇总客户端交互与自动发现所需信息：身份、端点 URL、版本，以及所支持能力（如流式输出、推送通知）、具体技能、默认输入/输出模式与认证要求。下为 WeatherBot 的 Agent Card 示例。

```json
{
    "name": "WeatherBot",
    "description": "Provides accurate weather forecasts and historical data.",
    "url": "http://weather-service.example.com/a2a",
    "version": "1.0.0",
    "capabilities": {
        "streaming": true,
        "pushNotifications": false,
        "stateTransitionHistory": true
    },
    "authentication": {
        "schemes": [
            "apiKey"
        ]
    },
    "defaultInputModes": [
        "text"
    ],
    "defaultOutputModes": [
        "text"
    ],
    "skills": [
        {
            "id": "get_current_weather",
            "name": "Get Current Weather",
            "description": "Retrieve real-time weather for any location.",
            "inputModes": [
                "text"
            ],
            "outputModes": [
                "text"
            ],
            "examples": [
                "What's the weather in Paris?",
                "Current conditions in Tokyo"
            ],
            "tags": [
                "weather",
                "current",
                "real-time"
            ]
        },
        {
            "id": "get_forecast",
            "name": "Get Forecast",
            "description": "Get 5-day weather predictions.",
            "inputModes": [
                "text"
            ],
            "outputModes": [
                "text"
            ],
            "examples": [
                "5-day forecast for New York",
                "Will it rain in London this weekend?"
            ],
            "tags": [
                "weather",
                "forecast",
                "prediction"
            ]
        }
    ]
}
```

**Agent discovery:** it allows clients to find Agent Cards, which describe the capabilities of available A2A Servers. Several strategies exist for this process:

> **智能体发现：** 让客户端定位描述各 A2A 服务端能力的 Agent Card。常见做法包括：

* Well-Known URI: Agents host their Agent Card at a standardized path (e.g., /.well-known/agent.json). This approach offers broad, often automated, accessibility for public or domain-specific use.  
* Curated Registries**:** These provide a centralized catalog where Agent Cards are published and can be queried based on specific criteria. This is well-suited for enterprise environments needing centralized management and access control.  
* Direct Configuration**:** Agent Card information is embedded or privately shared. This method is appropriate for closely coupled or private systems where dynamic discovery isn't crucial.

> * 知名 URI（Well-Known URI）：将 Agent Card 放在约定路径（如 `/.well-known/agent.json`），便于公网或域内广泛、可自动化的发现。
> * **策展注册表（Curated Registries）：** 集中发布 Agent Card 并支持按条件检索，适合需要统一治理与访问控制的企业环境。
> * **直接配置（Direct Configuration）：** 将 Agent Card 内嵌或线下分发，适合紧耦合或私有部署、且不强调动态发现的场景。

Regardless of the chosen method, it is important to secure Agent Card endpoints. This can be achieved through access control, mutual TLS (mTLS), or network restrictions, especially if the card contains sensitive (though non-secret) information.

> 无论采用哪种发现方式，都应对 Agent Card 端点加以防护——例如访问控制、双向 TLS（mTLS）或网络隔离——尤其当卡片承载敏感（但非密钥级）元数据时。

**Communications and Tasks:** In the A2A framework, communication is structured around asynchronous tasks, which represent the fundamental units of work for long-running processes. Each task is assigned a unique identifier and moves through a series of states—such as submitted, working, or completed—a design that supports parallel processing in complex operations. Communication between agents occurs through a Message.

> **通信与任务：** A2A 以异步任务组织通信；任务是长时运行的基本工作单元，带唯一标识并在「已提交—进行中—已完成」等状态间流转，便于在复杂流程中并行推进。智能体之间通过 Message 交换信息。

This communication  contains attributes, which are key-value metadata describing the message (like its priority or creation time), and one or more parts, which carry the actual content being delivered, such as plain text, files, or structured JSON data. The tangible outputs generated by an agent during a task are called artifacts. Like messages, artifacts are also composed of one or more parts and can be streamed incrementally as results become available. All communication within the A2A framework is conducted over HTTP(S) using the JSON-RPC 2.0 protocol for payloads. To maintain continuity across multiple interactions, a server-generated contextId is used to group related tasks and preserve context.

> 消息含属性（键值元数据，如优先级、创建时间）与一个或多个部分（parts），承载正文——纯文本、文件或结构化 JSON 等。任务执行中产生的可交付物称为工件（artifacts）；与消息一样由若干 part 组成，并可在结果陆续生成时流式下发。A2A 在 HTTP(S) 上传输，载荷遵循 JSON-RPC 2.0。为串联多轮交互，由服务端生成 `contextId`，将相关任务归组以延续上下文。

**Interaction Mechanisms**: Request/Response (Polling) Server-Sent Events (SSE). A2A provides multiple interaction methods to suit a variety of AI application needs, each with a distinct mechanism:

> **交互机制：** 涵盖同步请求/响应、异步轮询、服务器发送事件（SSE）等。A2A 提供多种交互形态，以匹配不同 AI 应用在时延与连接方式上的需求：

* Synchronous Request/Response: For quick, immediate operations. In this model, the client sends a request and actively waits for the server to process it and return a complete response in a single, synchronous exchange.  
* Asynchronous Polling: Suited for tasks that take longer to process. The client sends a request, and the server immediately acknowledges it with a "working" status and a task ID. The client is then free to perform other actions and can periodically poll the server by sending new requests to check the status of the task until it is marked as "completed" or "failed."  
* Streaming Updates (Server-Sent Events \- SSE): Ideal for receiving real-time, incremental results. This method establishes a persistent, one-way connection from the server to the client. It allows the remote agent to continuously push updates, such as status changes or partial results, without the client needing to make multiple requests.  
* Push Notifications (Webhooks): Designed for very long-running or resource-intensive tasks where maintaining a constant connection or frequent polling is inefficient. The client can register a webhook URL, and the server will send an asynchronous notification (a "push") to that URL when the task's status changes significantly (e.g., upon completion).

> * **同步请求/响应：** 面向低时延、一次性拿全结果的场景；客户端发出请求并在同一次往返内等待服务端返回完整答复。
> * **异步轮询：** 适合耗时任务；服务端先返回「进行中」与任务 ID，客户端可穿插其他工作并周期性拉取状态，直到标记为「完成」或「失败」。
> * **流式更新（SSE）：** 适合实时、增量呈现；建立服务端到客户端的长连接，远端智能体可持续推送状态或片段结果，免却高频轮询。
> * **推送通知（Webhooks）：** 适合超长或重负载任务；客户端预先登记 webhook，状态显著变化（如完结）时由服务端异步回调该 URL。

The Agent Card specifies whether an agent supports streaming or push notification capabilities. Furthermore, A2A is modality-agnostic, meaning it can facilitate these interaction patterns not just for text, but also for other data types like audio and video, enabling rich, multimodal AI applications. Both streaming and push notification capabilities are specified within the Agent Card.

> Agent Card 会声明是否支持流式与推送。A2A 本身与模态解耦，除文本外亦可承载音频、视频等，支撑多模态应用；上述能力均在卡片中显式列出。

```json
# Synchronous Request Example 
{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "sendTask",
    "params": {
        "id": "task-001",
        "sessionId": "session-001",
        "message": {
            "role": "user",
            "parts": [
                {
                    "type": "text",
                    "text": "What is the exchange rate from USD to EUR?"
                }
            ]
        },
        "acceptedOutputModes": [
            "text/plain"
        ],
        "historyLength": 5
    }
}
```

The synchronous request uses the sendTask method, where the client asks for and expects a single, complete answer to its query. In contrast, the streaming request uses the sendTaskSubscribe method to establish a persistent connection, allowing the agent to send back multiple, incremental updates or partial results over time.

> 同步路径调用 `sendTask`，客户端期待一次拿到完整答案；流式路径使用 `sendTaskSubscribe` 建立长连接，使智能体可持续下发增量或分片结果。

```json
# Streaming Request Example 
{
    "jsonrpc": "2.0",
    "id": "2",
    "method": "sendTaskSubscribe",
    "params": {
        "id": "task-002",
        "sessionId": "session-001",
        "message": {
            "role": "user",
            "parts": [
                {
                    "type": "text",
                    "text": "What's the exchange rate for JPY to GBP today?"
                }
            ]
        },
        "acceptedOutputModes": [
            "text/plain"
        ],
        "historyLength": 5
    }
}
```

**Security:**  Inter-Agent Communication (A2A): Inter-Agent Communication (A2A) is a vital component of system architecture, enabling secure and seamless data exchange among agents. It ensures robustness and integrity through several built-in mechanisms.

> **安全：** 智能体间通信（A2A）是系统架构的关键一环，既要保障智能体之间数据交换的安全与连贯，也依赖多种内置机制维护韧性与完整性。

Mutual Transport Layer Security (TLS): Encrypted and authenticated connections are established to prevent unauthorized access and data interception, ensuring secure communication.

> **双向传输层安全（mTLS）：** 通过加密与双向认证建立信道，降低未授权接入与窃听风险。

Comprehensive Audit Logs: All inter-agent communications are meticulously recorded, detailing information flow, involved agents, and actions. This audit trail is crucial for accountability, troubleshooting, and security analysis.

> **全面审计日志：** 逐笔记录智能体间通信的信息流、参与方与动作，为问责、排障与安全分析提供依据。

Agent Card Declaration: Authentication requirements are explicitly declared in the Agent Card, a configuration artifact outlining the agent's identity, capabilities, and security policies. This centralizes and simplifies authentication management.

> **Agent Card 声明：** 认证方式在 Agent Card 中明示；该配置工件集中描述身份、能力与安全策略，便于统一治理认证。

Credential Handling: Agents typically authenticate using secure credentials like OAuth 2.0 tokens or API keys, passed via HTTP headers. This method prevents credential exposure in URLs or message bodies, enhancing overall security.

> **凭据处理：** 智能体通常经 HTTP 头传递 OAuth 2.0 令牌或 API 密钥等凭据，避免写入 URL 或消息体，降低泄露面。

## A2A vs. MCP

> ## A2A 与 MCP

A2A is a protocol that complements Anthropic's Model Context Protocol (MCP) (see Fig. 1). While MCP focuses on structuring context for agents and their interaction with external data and tools, A2A facilitates coordination and communication among agents, enabling task delegation and collaboration.

> A2A 与 Anthropic 的模型上下文协议（MCP）形成互补（见图 1）：MCP 侧重为智能体组织上下文，并规范其与外部数据、工具的交互；A2A 侧重智能体之间的协调与通信，支撑任务委派与协同。

![Comparison A2A and MCP Protocols](../assets-new/Comparison_A2A_and_MCP_Protocols.png)

Fig.1: Comparison A2A and MCP Protocols

> 图 1：A2A 与 MCP 协议对比

The goal of A2A is to enhance efficiency, reduce integration costs, and foster innovation and interoperability in the development of complex, multi-agent AI systems. Therefore, a thorough understanding of A2A's core components and operational methods is essential for its effective design, implementation, and application in building collaborative and interoperable AI agent systems..

> A2A 旨在提效、降集成成本，并在复杂多智能体系统的研发中推动创新与互操作。若要设计、实现并落地协作型、可互操作的智能体系统，深入理解其核心组件与运行机制不可或缺。

## Practical Applications & Use Cases

> ## 实际应用与用例

Inter-Agent Communication is indispensable for building sophisticated AI solutions across diverse domains, enabling modularity, scalability, and enhanced intelligence.

> 智能体间通信是跨领域构建高阶 AI 方案的关键支撑，有助于模块化、可扩展与整体智能水平的提升。

* **Multi-Framework Collaboration:** A2A's primary use case is enabling independent AI agents, regardless of their underlying frameworks (e.g., ADK, LangChain, CrewAI), to communicate and collaborate. This is fundamental for building complex multi-agent systems where different agents specialize in different aspects of a problem.  
* **Automated Workflow Orchestration:** In enterprise settings, A2A can facilitate complex workflows by enabling agents to delegate and coordinate tasks. For instance, an agent might handle initial data collection, then delegate to another agent for analysis, and finally to a third for report generation, all communicating via the A2A protocol.  
* **Dynamic Information Retrieval:** Agents can communicate to retrieve and exchange real-time information. A primary agent might request live market data from a specialized "data fetching agent," which then uses external APIs to gather the information and send it back.

> * **多框架协作：** 典型场景是让彼此独立、底层各异（ADK、LangChain、CrewAI 等）的智能体仍能互通协作，这是复杂多智能体系统的底座能力。
> * **自动化工作流编排：** 在企业流程中，A2A 支撑跨智能体的任务委派与协同；例如采集→分析→成稿可由不同智能体接力完成，全程走 A2A。
> * **动态信息检索：** 智能体可互发请求、交换实时数据；主智能体可向专责的「数据拉取智能体」索要行情，后者调用外部 API 后回传结果。

## Hands-On Code Example

> ## 动手代码示例

Let's examine the practical applications of the A2A protocol. The repository at [https://github.com/google-a2a/a2a-samples/tree/main/samples](https://github.com/google-a2a/a2a-samples/tree/main/samples) provides examples in Java, Go, and Python that illustrate how various agent frameworks, such as LangGraph, CrewAI, Azure AI Foundry, and AG2, can communicate using A2A. All code in this repository is released under the Apache 2.0 license. To further illustrate A2A's core concepts, we will review code excerpts focusing on setting up an A2A Server using an ADK-based agent with Google-authenticated tools. Looking at [https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py](https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py)

> 下面结合实例看 A2A 如何落地。官方样例仓库 [https://github.com/google-a2a/a2a-samples/tree/main/samples](https://github.com/google-a2a/a2a-samples/tree/main/samples) 含 Java、Go、Python 示例，演示 LangGraph、CrewAI、Azure AI Foundry、AG2 等框架如何经 A2A 互通；许可证为 Apache 2.0。为阐明核心概念，下文摘录基于 ADK、并接入 Google 认证日历工具搭建 A2A 服务端的代码，完整见 [https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py](https://github.com/google-a2a/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/adk_agent.py)

```python
import datetime

from google.adk.agents import LlmAgent  # type: ignore[import-untyped]
from google.adk.tools.google_api_tool import CalendarToolset  # type: ignore[import-untyped]


async def create_agent(client_id: str, client_secret: str) -> LlmAgent:
    """Constructs the ADK agent."""
    toolset = CalendarToolset(client_id=client_id, client_secret=client_secret)
    return LlmAgent(
        model="gemini-2.0-flash-001",
        name="calendar_agent",
        description="An agent that can help manage a user's calendar",
        instruction=(
            f""" You are an agent that can help manage a user's calendar. Users will request information about the state of their calendar """
            f""" or to make changes to their calendar. Use the provided tools for interacting with the calendar API. """
            f""" If not specified, assume the calendar the user wants is the 'primary' calendar. """
            f""" When using the Calendar API tools, use well-formed RFC3339 timestamps. Today is {datetime.datetime.now()}. """
        ),
        tools=await toolset.get_tools(),
    )
```

This Python code defines an asynchronous function `create_agent` that constructs an ADK LlmAgent. It begins by initializing a `CalendarToolset` using the provided client credentials to access the Google Calendar API. Subsequently, an `LlmAgent` instance is created, configured with a specified Gemini model, a descriptive name, and instructions for managing a user's calendar. The agent is furnished with calendar tools from the `CalendarToolset`, enabling it to interact with the Calendar API and respond to user queries regarding calendar states or modifications. The agent's instructions dynamically incorporate the current date for temporal context. To illustrate how an agent is constructed, let's examine a key section from the `calendar_agent` found in the A2A samples on GitHub.

> 这段 Python 以异步函数 `create_agent` 构建 ADK `LlmAgent`：先用客户端凭据实例化 `CalendarToolset` 以访问 Google Calendar API；再创建 `LlmAgent`，指定 Gemini 模型、名称与日历管理类指令，并挂载工具集，使其能读写日历并回答状态或变更类问题；指令中注入当前日期以提供时间锚点。接着看同一 A2A 样例里 `calendar_agent` 的启动片段。

The code below shows how the agent is defined with its specific instructions and tools. Please note that only the code required to explain this functionality is shown; you can access the complete file here: [https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py](https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py)

> 下列片段展示如何用技能描述与工具装配智能体；为便于阅读仅保留关键逻辑，完整实现见：[https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py](https://github.com/a2aproject/a2a-samples/blob/main/samples/python/agents/birthday_planner_adk/calendar_agent/__main__.py)

```python
def main(host: str = "0.0.0.0", port: int = 8000):
    # Verify an API key is set.
    # Not required if using Vertex AI APIs.
    if os.getenv("GOOGLE_GENAI_USE_VERTEXAI") != "TRUE" and not os.getenv("GOOGLE_API_KEY"):
        raise ValueError(
            "GOOGLE_API_KEY environment variable not set and "
            "GOOGLE_GENAI_USE_VERTEXAI is not TRUE."
        )

    skill = AgentSkill(
        id="check_availability",
        name="Check Availability",
        description="Checks a user's availability for a time using their Google Calendar",
        tags=["calendar"],
        examples=["Am I free from 10am to 11am tomorrow?"],
    )

    agent_card = AgentCard(
        name="Calendar Agent",
        description="An agent that can manage a user's calendar",
        url=f"http://{host}:{port}/",
        version="1.0.0",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
    )

    adk_agent = asyncio.run(
        create_agent(
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        )
    )

    runner = Runner(
        app_name=agent_card.name,
        agent=adk_agent,
        artifact_service=InMemoryArtifactService(),
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
    )
    agent_executor = ADKAgentExecutor(runner, agent_card)

    async def handle_auth(request: Request) -> PlainTextResponse:
        await agent_executor.on_auth_callback(
            str(request.query_params.get("state")),
            str(request.url),
        )
        return PlainTextResponse("Authentication successful.")

    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor,
        task_store=InMemoryTaskStore(),
    )

    a2a_app = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler,
    )
    routes = a2a_app.routes()
    routes.append(
        Route(
            path="/authenticate",
            methods=["GET"],
            endpoint=handle_auth,
        )
    )
    app = Starlette(routes=routes)

    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
```

This Python code demonstrates setting up an A2A-compliant "Calendar Agent" for checking user availability using Google Calendar. It involves verifying API keys or Vertex AI configurations for authentication purposes. The agent's capabilities, including the "check_availability" skill, are defined within an AgentCard, which also specifies the agent's network address. Subsequently, an ADK agent is created, configured with in-memory services for managing artifacts, sessions, and memory. The code then initializes a Starlette web application, incorporates an authentication callback and the A2A protocol handler, and executes it using Uvicorn to expose the agent via HTTP.

> 该段 Python 演示如何搭建符合 A2A 的「日历智能体」，借助 Google 日历查询空闲时段：启动前校验 API 密钥或 Vertex AI 配置；在 `AgentCard` 中声明能力与 `check_availability` 技能并给出对外 URL；再实例化 ADK 智能体，配以内存型工件、会话与记忆服务；最后组装 Starlette 路由（含 OAuth 回调与 A2A 处理器），由 Uvicorn 对外提供 HTTP 服务。

These examples illustrate the process of building an A2A-compliant agent, from defining its capabilities to running it as a web service. By utilizing Agent Cards and ADK, developers can create interoperable AI agents capable of integrating with tools like Google Calendar. This practical approach demonstrates the application of A2A in establishing a multi-agent ecosystem.

> 上述示例串起「声明能力 → 挂载工具 → 以 Web 服务暴露」的 A2A 智能体搭建路径。结合 Agent Card 与 ADK，可快速做出能与 Google 日历等工具联动的可互操作智能体，体现 A2A 在多智能体生态中的价值。

Further exploration of A2A is recommended through the code demonstration at [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project). Resources available at this link include sample A2A clients and servers in Python and JavaScript, multi-agent web applications, command-line interfaces, and example implementations for various agent frameworks.

> 亦可跟随 [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project) 的图文与代码演练深入 A2A；文中附带 Python/JavaScript 客户端与服务端、多智能体 Web 演示、命令行工具及多框架接入示例。

## At a Glance

> ## 速览

**What:** Individual AI agents, especially those built on different frameworks, often struggle with complex, multi-faceted problems on their own. The primary challenge is the lack of a common language or protocol that allows them to communicate and collaborate effectively. This isolation prevents the creation of sophisticated systems where multiple specialized agents can combine their unique skills to solve larger tasks. Without a standardized approach, integrating these disparate agents is costly, time-consuming, and hinders the development of more powerful, cohesive AI solutions.

> **是什么：** 单个 智能体，尤其是来自不同框架时，往往难以独立处理复杂的跨域问题；根本原因在于缺少能够支持可靠协作的通用“语言”或协议。各自为战会阻碍多类专精智能体协同完成复杂任务；若缺乏统一标准，异构系统集成不仅成本高、周期长，也会限制整体方案的能力上限。

**Why:** The Inter-Agent Communication (A2A) protocol provides an open, standardized solution for this problem. It is an HTTP-based protocol that enables interoperability, allowing distinct AI agents to coordinate, delegate tasks, and share information seamlessly, regardless of their underlying technology. A core component is the Agent Card, a digital identity file that describes an agent's capabilities, skills, and communication endpoints, facilitating discovery and interaction. A2A defines various interaction mechanisms, including synchronous and asynchronous communication, to support diverse use cases. By creating a universal standard for agent collaboration, A2A fosters a modular and scalable ecosystem for building complex, multi-agent Agentic systems.

> **为什么：** A2A 以开放、标准化的 HTTP 协议填补这一空白，让异构智能体能协调、委派任务并顺畅共享信息。Agent Card 充当数字名片，集中描述能力、技能与接入端点，支撑自动发现与对接。协议内建同步、异步、流式等交互模式以覆盖多元场景；统一协作面后，复杂多智能体系统更易模块化生长与横向扩展。

**Rule of Thumb:** Use this pattern when you need to orchestrate collaboration between two or more AI agents, especially if they are built using different frameworks (e.g., Google ADK, LangGraph, CrewAI). It is ideal for building complex, modular applications where specialized agents handle specific parts of a workflow, such as delegating data analysis to one agent and report generation to another. This pattern is also essential when an agent needs to dynamically discover and consume the capabilities of other agents to complete a task.

> **经验法则：** 当需要编排两个及以上 智能体，且其技术栈并不统一（如 Google ADK、LangGraph、CrewAI 等）时，应优先考虑 A2A。它同样适用于复杂的模块化应用：可按子任务拆分专精智能体，例如分别负责分析与成稿。若系统还需在运行时动态发现并调用其他智能体能力以闭环完成任务，A2A 这类标准通常也是关键选择。

**Visual Summary:**

> **图示摘要：**

![A2A Inter-Agent Communication Pattern](../assets-new/A2A_Inter-Agent_Communication_Pattern.png)

Fig.2: A2A inter-agent communication pattern

> 图 2：A2A 智能体间通信模式

## Key Takeaways

> ## 要点

Key Takeaways:

> 本章要点：

* The Google A2A protocol is an open, HTTP-based standard that facilitates communication and collaboration between AI agents built with different frameworks.  
* An AgentCard serves as a digital identifier for an agent, allowing for automatic discovery and understanding of its capabilities by other agents.  
* A2A offers both synchronous request-response interactions (using `tasks/send`) and streaming updates (using `tasks/sendSubscribe`) to accommodate varying communication needs.  
* The protocol supports multi-turn conversations, including an `input-required` state, which allows agents to request additional information and maintain context during interactions.  
* A2A encourages a modular architecture where specialized agents can operate independently on different ports, enabling system scalability and distribution.  
* Tools such as Trickle AI aid in visualizing and tracking A2A communications, which helps developers monitor, debug, and optimize multi-agent systems.  
* While A2A is a high-level protocol for managing tasks and workflows between different agents, the Model Context Protocol (MCP) provides a standardized interface for LLMs to interface with external resources

> * Google A2A 是基于 HTTP 的开放标准，用于跨框架 智能体的通信与协同。
> * AgentCard 是智能体的数字名片，供他方自动发现并理解其能力与接入方式。
> * 协议同时支持同步请求-响应（`tasks/send`）与流式订阅（`tasks/sendSubscribe`），匹配不同时延与连接模型。
> * 内置多轮会话与 `input-required` 等状态，智能体可在交互中索要缺失信息并延续上下文。
> * 鼓励按能力拆分的模块化部署：专精智能体可分端口独立演进，利于伸缩与分布式拓扑。
> * Trickle AI 等工具可观测 A2A 流量，辅助排障与性能调优。
> * A2A 面向跨智能体的任务与工作流编排；MCP 则标准化 LLM 与外部工具、数据源的对接，二者分工互补。

## Conclusions

> ## 结论

The Inter-Agent Communication (A2A) protocol establishes a vital, open standard to overcome the inherent isolation of individual AI agents. By providing a common HTTP-based framework, it ensures seamless collaboration and interoperability between agents built on different platforms, such as Google ADK, LangGraph, or CrewAI. A core component is the Agent Card, which serves as a digital identity, clearly defining an agent's capabilities and enabling dynamic discovery by other agents. The protocol's flexibility supports various interaction patterns, including synchronous requests, asynchronous polling, and real-time streaming, catering to a wide range of application needs.

> 智能体间通信（A2A）以开放标准打破单个智能体彼此隔离的局面：在统一的 HTTP 语义之上，使基于 Google ADK、LangGraph、CrewAI 等技术栈的智能体能够实现互认与互操作。Agent Card 以结构化方式描述身份、技能与端点，支撑运行时发现与按需组合。协议在同步、异步轮询、实时流式等模式间灵活切换，可覆盖从低时延问答到长时任务的广泛场景。

This enables the creation of modular and scalable architectures where specialized agents can be combined to orchestrate complex automated workflows. Security is a fundamental aspect, with built-in mechanisms like mTLS and explicit authentication requirements to protect communications. While complementing other standards like MCP, A2A's unique focus is on the high-level coordination and task delegation between agents. The strong backing from major technology companies and the availability of practical implementations highlight its growing importance. This protocol paves the way for developers to build more sophisticated, distributed, and intelligent multi-agent systems. Ultimately, A2A is a foundational pillar for fostering an innovative and interoperable ecosystem of collaborative AI.

> 在此基础上，可通过专精智能体构建模块化、可横向扩展的自动化流程。安全层面，mTLS、显式认证与审计等机制为跨智能体通信提供保障。与 MCP 等标准并列时，A2A 的独特价值在于面向“智能体对智能体”的高层编排与任务委派。产业界的持续投入与丰富的参考实现，正推动其成为分布式、协作式 AI 生态的重要基础设施之一。

## References

1. Chen, B. (2025, April 22). *How to Build Your First Google A2A Project: A Step-by-Step Tutorial*. Trickle.so Blog. [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project)
2. Google A2A GitHub Repository. [https://github.com/google-a2a/A2A](https://github.com/google-a2a/A2A)
3. Google Agent Development Kit (ADK) [https://google.github.io/adk-docs/](https://google.github.io/adk-docs/)
4. Getting Started with Agent-to-Agent (A2A) Protocol: [https://codelabs.developers.google.com/intro-a2a-purchasing-concierge\#0](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0)
5. Google AgentDiscovery \- [https://a2a-protocol.org/latest/](https://a2a-protocol.org/latest/)
6. Communication between different AI frameworks such as LangGraph, CrewAI, and Google ADK [https://www.trickle.so/blog/how-to-build-google-a2a-project](https://www.trickle.so/blog/how-to-build-google-a2a-project#setting-up-your-a2a-development-environment)
7. Designing Collaborative Multi-Agent Systems with the A2A Protocol [https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/](https://www.oreilly.com/radar/designing-collaborative-multi-agent-systems-with-the-a2a-protocol/)
