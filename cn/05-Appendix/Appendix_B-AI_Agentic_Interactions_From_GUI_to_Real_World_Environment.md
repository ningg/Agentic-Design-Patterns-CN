# Appendix B - AI Agentic Interactions: From GUI to Real World environment

> 附录 B：智能体交互——从图形界面到真实世界环境

AI agents are increasingly performing complex tasks by interacting with digital interfaces and the physical world. Their ability to perceive, process, and act within these varied environments is fundamentally transforming automation, human-computer interaction, and intelligent systems. This appendix explores how agents interact with computers and their environments, highlighting advancements and projects.

> 智能体正越来越多地借助数字界面与物理世界交互来完成复杂任务；在多样环境中感知、处理并行动的能力，正从根本上重塑自动化、人机交互与智能系统。本附录说明智能体如何与计算机及环境互动，并梳理代表性进展与项目。

## Interaction: Agents with Computers

> ## 交互：智能体与计算机

The evolution of AI from conversational partners to active, task-oriented agents is being driven by Agent-Computer Interfaces (ACIs). These interfaces allow AI to interact directly with a computer's Graphical User Interface (GUI), enabling it to perceive and manipulate visual elements like icons and buttons just as a human would. This new method moves beyond the rigid, developer-dependent scripts of traditional automation that relied on APIs and system calls. By using the visual "front door" of software, AI can now automate complex digital tasks in a more flexible and powerful way, a process that involves several key stages:

> AI 正从单纯的对话伙伴演进为主动、任务导向的智能体，而这一转变的重要推动力正是智能体—计算机接口（ACI）。这类接口让 AI 能够直接操作计算机图形界面（GUI），像人类一样识别并点击图标、按钮等视觉元素。它突破了传统自动化脚本对 API 与系统调用的高度依赖，使 AI 能经由软件的视觉“正门”更灵活地自动化复杂数字任务。整个过程通常包含以下关键阶段：

- **Visual Perception:** The agent first captures a visual representation of the screen, essentially taking a screenshot.  
- **GUI Element Recognition:** It then analyzes this image to distinguish between various GUI elements. It must learn to "see" the screen not as a mere collection of pixels, but as a structured layout with interactive components, discerning a clickable "Submit" button from a static banner image or an editable text field from a simple label.  
- **Contextual Interpretation:** The ACI module, acting as a bridge between the visual data and the agent's core intelligence (often a Large Language Model or LLM), interprets these elements within the context of the task. It understands that a magnifying glass icon typically means "search" or that a series of radio buttons represents a choice. This module is crucial for enhancing the LLM's reasoning, allowing it to form a plan based on visual evidence.  
- **Dynamic Action and Response:** The agent then programmatically controls the mouse and keyboard to execute its plan—clicking, typing, scrolling, and dragging. Critically, it must constantly monitor the screen for visual feedback, dynamically responding to changes, loading screens, pop-up notifications, or errors to successfully navigate multi-step workflows.

> - **视觉感知：** 先抓取屏幕画面，通常即截屏。
> - **GUI 元素识别：** 再解析图像，区分控件类型——把界面理解成可交互的结构，而不是像素块；分辨“可点的提交”与纯装饰图、可编辑输入框与静态标签。
> - **语境解释：** ACI 在像素流与智能体核心（多为 LLM）之间搭桥，结合当前任务解读控件含义（如放大镜≈搜索、单选组≈互斥选项）。这一步直接增强 LLM 的规划能力。
> - **动态行动与反馈：** 最后以程序驱动键鼠执行计划（点按、输入、滚动、拖拽），并持续盯屏：根据加载态、弹窗、报错等反馈调整下一步，跑通多步流程。

This technology is no longer theoretical. Several leading AI labs have developed functional agents that demonstrate the power of GUI interaction:

> 该技术已非纸上谈兵。多家领先 AI 实验室已推出可工作的智能体，展示 GUI 交互的力量：

**ChatGPT Operator (OpenAI):** Envisioned as a digital partner, ChatGPT Operator is designed to automate tasks across a wide range of applications directly from the desktop. It understands on-screen elements, enabling it to perform actions like transferring data from a spreadsheet into a customer relationship management (CRM) platform, booking a complex travel itinerary across airline and hotel websites, or filling out detailed online forms without needing specialized API access for each service. This makes it a universally adaptable tool aimed at boosting both personal and enterprise productivity by taking over repetitive digital chores.

> **ChatGPT Operator（OpenAI）：** 定位为数字协作伙伴，可在桌面侧跨应用自动完成任务。它能读懂界面元素，例如把表格数据同步进客户关系管理（CRM）、在航司与酒店站点上预订复杂行程、填写冗长在线表单等，而无需为每个站点单独对接 API。通过承接重复性的数字杂务，它面向个人与企业场景，具备较强的通用适配能力。

**Google Project Mariner:** As a research prototype, Project Mariner operates as an agent within the Chrome browser (see Fig. 1). Its purpose is to understand a user's intent and autonomously carry out web-based tasks on their behalf. For example, a user could ask it to find three apartments for rent within a specific budget and neighborhood; Mariner would then navigate to real estate websites, apply the filters, browse the listings, and extract the relevant information into a document. This project represents Google's exploration into creating a truly helpful and "agentive" web experience where the browser actively works for the user.

> **Google Project Mariner：** 研究原型，以内嵌智能体形态跑在 Chrome 中（见图 1）。它尝试读懂用户意图，并代替用户完成网页侧任务——例如在预算与地段约束下找三处租房：自动打开房源站、套用筛选、翻阅列表并把要点整理进文档。项目方向是让浏览器从“被动渲染”走向主动办事的“智能体化”体验。

Interaction between Agent and the Web Browser

Fig.1: Interaction between and Agent and the Web Browser

> 图 1：智能体与网页浏览器之间的交互

**Anthropic's Computer Use:** This feature empowers Anthropic's AI model, Claude, to become a direct user of a computer's desktop environment. By capturing screenshots to perceive the screen and programmatically controlling the mouse and keyboard, Claude can orchestrate workflows that span multiple, unconnected applications. A user could ask it to analyze data in a PDF report, open a spreadsheet application to perform calculations on that data, generate a chart, and then paste that chart into an email draft—a sequence of tasks that previously required constant human input.

> **Anthropic 的 Computer Use：** 让 Claude 像真实用户一样“坐”在电脑前，通过截屏理解界面，并以程序化方式控制键盘和鼠标，从而串联多个彼此未通过 API 打通的应用。典型流程包括读取 PDF 中的数据、在表格软件中完成运算、生成图表，并将结果粘贴进邮件草稿；这类任务过去通常需要人工逐步操作。

**Browser Use**: This  is an open-source library that provides a high-level API for programmatic browser automation. It enables AI agents to interface with web pages by granting them access to and control over the Document Object Model (DOM). The API abstracts the intricate, low-level commands of browser control protocols, into a more simplified and intuitive set of functions. This allows an agent to perform complex sequences of actions, including data extraction from nested elements, form submissions, and automated navigation across multiple pages. As a result, the library facilitates the transformation of unstructured web data into a structured format that an AI agent can systematically process and utilize for analysis or decision-making.

> **Browser Use：** 面向程序化浏览器自动化的开源库，对外暴露高层 API。它让智能体能读写文档对象模型（DOM），从而与页面深度交互；把底层控制协议里的细碎指令封装成更易用的一组函数，支持嵌套元素抽取、表单提交、跨页跳转等复杂动作链，把杂乱的网页内容整理成可供 AI 进一步分析与决策的结构化数据。

## Interaction: Agents with the Environment

> ## 交互：智能体与环境

Beyond the confines of a computer screen, AI agents are increasingly designed to interact with complex, dynamic environments, often mirroring the real world. This requires sophisticated perception, reasoning, and actuation capabilities.

> 走出屏幕之后，智能体越来越多地面对复杂、动态、往往对应真实场景的环境，因而需要更强的感知、推理与执行能力。

Google's **Project Astra** is a prime example of an initiative pushing the boundaries of agent interaction with the environment. Astra aims to create a universal AI agent that is helpful in everyday life, leveraging multimodal inputs (sight, sound, voice) and outputs to understand and interact with the world contextually. This project focuses on rapid understanding, reasoning, and response, allowing the agent to "see" and "hear" its surroundings through cameras and microphones and engage in natural conversation while providing real-time assistance. Astra's vision is an agent that can seamlessly assist users with tasks ranging from finding lost items to debugging code, by understanding the environment it observes. This moves beyond simple voice commands to a truly embodied understanding of the user's immediate physical context.

> Google 的 **Project Astra** 是拓展智能体与环境交互边界的代表项目。Astra 志在打造在日常生活中真正有用的通用 智能体，融合视、听、语音等多模态输入与输出，在情境中理解世界并与之互动。项目侧重快速理解、推理与响应：借助摄像头与麦克风，智能体能“看见”“听见”周围，在自然对话里提供实时帮助。长远愿景是：基于对环境的理解，从找失物到调试代码都能无缝协助，不止于简单语音命令，而是贴近用户当下的物理情境。

Google's **Gemini Live**, transforms standard AI interactions into a fluid and dynamic conversation. Users can speak to the AI and receive responses in a natural-sounding voice with minimal delay, and can even interrupt or change topics mid-sentence, prompting the AI to adapt immediately. The interface expands beyond voice, allowing users to incorporate visual information by using their phone's camera, sharing their screen, or uploading files for a more context-aware discussion. More advanced versions can even perceive a user's tone of voice and intelligently filter out irrelevant background noise to better understand the conversation. These capabilities combine to create rich interactions, such as receiving live instructions on a task by simply pointing a camera at it.

> Google 的 **Gemini Live** 将传统问答升级为低延迟、可打断的连续对话：语音更自然，模型也能随话题变化即时调整。输入形式不再局限于语音，摄像头、屏幕共享与文件上传都可纳入同一上下文；更高级的版本还能够识别说话语气，并抑制无关背景噪声。由此，用户可以在操作过程中直接对着镜头提问，并实时获得指导。

OpenAI's **GPT-4o model** is an alternative designed for "omni" interaction, meaning it can reason across voice, vision, and text. It processes these inputs with low latency that mirrors human response times, which allows for real-time conversations. For example, users can show the AI a live video feed to ask questions about what is happening, or use it for language translation. OpenAI provides developers with a "Realtime API" to build applications requiring low-latency, speech-to-speech interactions.

> OpenAI 的 **GPT-4o** 主打 omni（全模态）交互：语音、图像、文字可在同一推理链路里混搭，端到端延迟贴近人类对话节奏。场景包括对着实时画面提问现场情况、做同声传译式翻译等。配套 “Realtime API” 方便开发者搭建语音↔语音的低延迟应用。

OpenAI's **ChatGPT Agent** represents a significant architectural advancement over its predecessors, featuring an integrated framework of new capabilities. Its design incorporates several key functional modalities: the capacity for autonomous navigation of the live internet for real-time data extraction, the ability to dynamically generate and execute computational code for tasks like data analysis, and the functionality to interface directly with third-party software applications. The synthesis of these functions allows the agent to orchestrate and complete complex, sequential workflows from a singular user directive. It can therefore autonomously manage entire processes, such as performing market analysis and generating a corresponding presentation, or planning logistical arrangements and executing the necessary transactions. In parallel with the launch, OpenAI has proactively addressed the emergent safety considerations inherent in such a system. An accompanying "System Card" delineates the potential operational hazards associated with an AI capable of performing actions online, acknowledging the new vectors for misuse. To mitigate these risks, the agent's architecture includes engineered safeguards, such as requiring explicit user authorization for certain classes of actions and deploying robust content filtering mechanisms. The company is now engaging its initial user base to further refine these safety protocols through a feedback-driven, iterative process.

> OpenAI 的 **ChatGPT Agent** 在架构上较前代明显跃迁，整合了多类新能力：可自主浏览实时互联网抓取信息，能按需生成并运行代码（如数据分析），也能直接对接第三方应用。能力叠加后，单条用户指令即可驱动长链条工作流——例如完成市场调研并生成演示文稿，或规划物流并落单支付。与产品同步，OpenAI 也直面这类系统带来的新型安全风险；随附的 “System Card” 梳理了联网执行动作可能触发的危害与滥用面。缓解手段包括：对敏感操作强制用户显式授权、部署更稳健的内容过滤等，并借助早期用户反馈持续迭代安全策略。

**Seeing AI,** a complimentary mobile application from Microsoft, empowers individuals who are blind or have low vision by offering real-time narration of their surroundings. The app leverages artificial intelligence through the device's camera to identify and describe various elements, including objects, text, and even people. Its core functionalities encompass reading documents, recognizing currency, identifying products through barcodes, and describing scenes and colors. By providing enhanced access to visual information, Seeing AI ultimately fosters greater independence for visually impaired users.

> **Seeing AI** 是微软推出的免费移动应用，以实时语音描述周围环境，帮助视障或低视力用户。应用结合设备摄像头与 AI，识别并讲述物体、文字乃至人物等信息；核心能力涵盖朗读文档、辨认货币、扫码识物、描述场景与色彩等。通过补足视觉信息，Seeing AI 有助于提升视障人士的独立生活能力。

**Anthropic's Claude 4 Series** Anthropic's Claude 4 is another alternative with capabilities for advanced reasoning and analysis. Though historically focused on text, Claude 4 includes robust vision capabilities, allowing it to process information from images, charts, and documents. The model is suited for handling complex, multi-step tasks and providing detailed analysis. While the real-time conversational aspect is not its primary focus compared to other models, its underlying intelligence is designed for building highly capable AI agents.

> **Anthropic 的 Claude 4 系列：** Claude 4 在高级推理与分析上同样出色。尽管长期以文本见长，这一代强化了视觉理解，可消化图像、图表与版式文档。它擅长多步骤、需拆解的任务，并能给出较细的论证。若与强调实时语音交互的模型相比，对话实时性并非其主打，但其底层能力明显面向“可编排的高性能智能体”场景。

## Vibe Coding: Intuitive Development with AI

> ## Vibe Coding：与 AI 的直觉式开发

Beyond direct interaction with GUIs and the physical world, a new paradigm is emerging in how developers build software with AI: "vibe coding." This approach moves away from precise, step-by-step instructions and instead relies on a more intuitive, conversational, and iterative interaction between the developer and an AI coding assistant. The developer provides a high-level goal, a desired "vibe," or a general direction, and the AI generates code to match.

> 除了直接操控 GUI 与物理世界，开发者借助 AI 编写软件的方式也在形成新的范式，即“Vibe Coding”。这种方法弱化了逐条规定的细致规格说明，更依赖开发者与编程助手之间直觉式、对话式且可反复迭代的互动：开发者给出高层目标、期望风格或总体方向，由 AI 生成相应代码。

This process is characterized by:

> 该过程的特点包括：

- **Conversational Prompts:** Instead of writing detailed specifications, a developer might say, "Create a simple, modern-looking landing page for a new app," or, "Refactor this function to be more Pythonic and readable." The AI interprets the "vibe" of "modern" or "Pythonic" and generates the corresponding code.  
- **Iterative Refinement:** The initial output from the AI is often a starting point. The developer then provides feedback in natural language, such as, "That's a good start, but can you make the buttons blue?" or, "Add some error handling to that." This back-and-forth continues until the code meets the developer's expectations.  
- **Creative Partnership:** In vibe coding, the AI acts as a creative partner, suggesting ideas and solutions that the developer may not have considered. This can accelerate the development process and lead to more innovative outcomes.  
- **Focus on "What" not "How":** The developer focuses on the desired outcome (the "what") and leaves the implementation details (the "how") to the AI. This allows for rapid prototyping and exploration of different approaches without getting bogged down in boilerplate code.  
- **Optional Memory Banks:** To maintain context across longer interactions, developers can use "memory banks" to store key information, preferences, or constraints. For example, a developer might save a specific coding style or a set of project requirements to the AI's memory, ensuring that future code generations remain consistent with the established "vibe" without needing to repeat the instructions.

> - **对话式提示：** 与其写长篇规格，不如直接说“给新应用做个简洁现代的落地页”或“把函数改得更 Pythonic、更好读”——模型会自行揣摩“现代感”“Pythonic”并落到代码。
> - **迭代打磨：** 第一版往往只是草稿；接着用口语微调：“按钮换成蓝色？”“这里补下异常处理？”来回几轮直到满意。
> - **共创角色：** AI 不只是执行器，也会抛出新点子，加快试错、拓宽方案面。
> - **先想清楚做什么：** 人盯 outcome（what），实现路径（how）交给模型，利于快速试错，少在样板代码里耗神。
> - **可选记忆库：** 长会话里可把风格约定、项目约束写进“记忆”，后续生成自动对齐，省得每次复读机式提醒。

Vibe coding is becoming increasingly popular with the rise of powerful AI models like GPT-4, Claude, and Gemini, which are integrated into development environments. These tools are not just auto-completing code; they are actively participating in the creative process of software development, making it more accessible and efficient. This new way of working is changing the nature of software engineering, emphasizing creativity and high-level thinking over rote memorization of syntax and APIs.

> 随着 GPT-4、Claude、Gemini 等模型深度嵌入 IDE，Vibe Coding 迅速普及：这些工具不再局限于补全单行代码，而是开始参与方案构思与实现。工程实践的重心也随之上移，人们将更多精力投入问题拆解与设计，而不再过度消耗于记忆语法或查阅 API。

## Key takeaways

> ## 要点

- AI agents are evolving from simple automation to visually controlling software through graphical user interfaces, much like a human would.  
- The next frontier is real-world interaction, with projects like Google's Astra using cameras and microphones to see, hear, and understand their physical surroundings.  
- Leading technology companies are converging these digital and physical capabilities to create universal AI assistants that operate seamlessly across both domains.  
- This shift is creating a new class of proactive, context-aware AI companions capable of assisting with a vast range of tasks in users' daily lives.

> - 智能体正由脚本式自动化，演进为通过 GUI 像人一样观察与操作软件。
> - 下一波突破在物理世界：以 Astra 为代表，借助摄像头与麦克风理解周遭环境。
> - 领先科技公司正同步强化数字与物理两侧能力，培育跨场景无缝衔接的通用助手。
> - 由此涌现更主动、更具情境感知能力的 AI 伙伴，可协助完成日常生活中的广泛任务。

## Conclusion

> ## 结语

Agents are undergoing a significant transformation, moving from basic automation to sophisticated interaction with both digital and physical environments. By leveraging visual perception to operate Graphical User Interfaces, these agents can now manipulate software just as a human would, bypassing the need for traditional APIs. Major technology labs are pioneering this space with agents capable of automating complex, multi-application workflows directly on a user's desktop. Simultaneously, the next frontier is expanding into the physical world, with initiatives like Google's Project Astra using cameras and microphones to contextually engage with their surroundings. These advanced systems are designed for multimodal, real-time understanding that mirrors human interaction.

> 智能体正处在深刻转型中：从基础自动化走向与数字世界、物理环境的双重深度交互。凭借视觉感知操作 GUI，它们可以像人一样使用软件，减少对专用 API 的依赖。各大技术实验室正在推进能在桌面上串联多应用、完成复杂流程的智能体。与此同时，下一波前沿伸向真实空间：以 Google Project Astra 为代表，用摄像头与麦克风在情境中与周围世界互动。这些系统面向多模态、低延迟、贴近人类互动方式的理解而构建。

The ultimate vision is a convergence of these digital and physical capabilities, creating universal AI assistants that operate seamlessly across all of a user's environments. This evolution is also reshaping software creation itself through "vibe coding," a more intuitive and conversational partnership between developers and AI. This new method prioritizes high-level goals and creative intent, allowing developers to focus on the desired outcome rather than implementation details. This shift accelerates development and fosters innovation by treating AI as a creative partner. Ultimately, these advancements are paving the way for a new era of proactive, context-aware AI companions capable of assisting with a vast array of tasks in our daily lives.

> 远期图景是把数字与物理能力缝在一起，让助手在办公、出行、家庭等场景里连续可用。软件生产侧，“vibe coding” 也在改写协作方式：对话式、目标驱动的共建取代逐行手写。人负责意图与验收，模型负责展开细节，循环越快，创新越快——最终指向同一类更主动、更懂语境的日常 AI 伙伴。

## References

> 参考文献：以下条目保留英文与原始链接，不作逐条翻译。

1. Open AI Operator, [https://openai.com/index/introducing-operator/](https://openai.com/index/introducing-operator/)
2. Open AI ChatGPT Agent: [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)
3. Browser Use: [https://docs.browser-use.com/introduction](https://docs.browser-use.com/introduction)
4. Project Mariner, [https://deepmind.google/models/project-mariner/](https://deepmind.google/models/project-mariner/)
5. Anthropic Computer use: [https://docs.anthropic.com/en/docs/build-with-claude/computer-use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
6. Project Astra, [https://deepmind.google/models/project-astra/](https://deepmind.google/models/project-astra/)
7. Gemini Live, [https://gemini.google/overview/gemini-live/?hl=en](https://gemini.google/overview/gemini-live/?hl=en)
8. OpenAI's GPT-4,  [https://openai.com/index/gpt-4-research/](https://openai.com/index/gpt-4-research/)
9. Claude 4, [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)