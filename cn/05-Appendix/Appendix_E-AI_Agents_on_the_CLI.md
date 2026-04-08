# Appendix E - AI Agents on the CLI

> **附录 E：命令行上的智能体**

## Introduction

> ## 引言

​​The developer's command line, long a bastion of precise, imperative commands, is undergoing a profound transformation. It is evolving from a simple shell into an intelligent, collaborative workspace powered by a new class of tools: AI Agent Command-Line Interfaces (CLIs). These agents move beyond merely executing commands; they understand natural language, maintain context about your entire codebase, and can perform complex, multi-step tasks that automate significant parts of the development lifecycle.

> 对开发者而言，命令行曾是精确、命令式操作的阵地；如今它正被一类新工具重塑——智能体 CLI。终端不再只是敲命令的壳，而逐步变成能对话、能记住仓库上下文的协作空间：智能体不仅代跑指令，还能用自然语言理解意图，串联多步操作，覆盖开发生命周期里大段可自动化的工作。

This guide provides an in-depth look at four leading players in this burgeoning field, exploring their unique strengths, ideal use cases, and distinct philosophies to help you determine which tool best fits your workflow. It is important to note that many of the example use cases provided for a specific tool can often be accomplished by the other agents as well. The key differentiator between these tools frequently lies in the quality, efficiency, and nuance of the results they are able to achieve for a given task. There are specific benchmarks designed to measure these capabilities, which will be discussed in the following sections.

> 下文聚焦四家代表性产品，比较各自的优势、典型场景与产品理念，帮助你判断哪一类工具更适合自身工作流。需要说明的是，文中列举的大多数用例通常也可由其他工具完成，真正拉开差距的往往是相同任务下结果的稳定性、效率与细腻度。文末还会介绍专门用于评测 CLI 智能体能力的基准。

## Claude CLI (Claude Code)

> ## Claude CLI（Claude Code）

Anthropic's Claude CLI is engineered as a high-level coding agent with a deep, holistic understanding of a project's architecture. Its core strength is its "agentic" nature, allowing it to create a mental model of your repository for complex, multi-step tasks. The interaction is highly conversational, resembling a pair programming session where it explains its plans before executing. This makes it ideal for professional developers working on large-scale projects involving significant refactoring or implementing features with broad architectural impacts.

> Claude CLI 面向具备整体仓库理解能力的编码智能体：它会先建立对仓库结构的全局认识，再拆解并推进多步改造任务。其交互风格接近结对编程，通常会在执行前先说明计划。这使它尤其适合大型代码库、深度重构以及影响范围较广的功能演进。

**Example Use Cases:**

> **示例用例：**

1. **Large-Scale Refactoring:** You can instruct it: "Our current user authentication relies on session cookies. Refactor the entire codebase to use stateless JWTs, updating the login/logout endpoints, middleware, and frontend token handling." Claude will then read all relevant files and perform the coordinated changes.  
2. **API Integration:** After being provided with an OpenAPI specification for a new weather service, you could say: "Integrate this new weather API. Create a service module to handle the API calls, add a new component to display the weather, and update the main dashboard to include it."  
3. **Documentation Generation**: Pointing it to a complex module with poorly documented code, you can ask: "Analyze the `./src/utils/data_processing.js` file. Generate comprehensive TSDoc comments for every function, explaining its purpose, parameters, and return value."  

> 1. **大规模重构：** 可指示：「我们当前用户认证依赖会话 cookie。将整个代码库重构为使用无状态 JWT，更新登录/登出端点、中间件与前端令牌处理。」Claude 会阅读相关文件并协调完成修改。
> 2. **API 集成：** 在提供新天气服务的 OpenAPI 规范后，可说：「集成这个新的天气 API。创建服务模块处理 API 调用，新增展示天气的组件，并更新主仪表板以包含该功能。」
> 3. **文档生成：** 指向文档不足的复杂模块，可要求：「分析 `./src/utils/data_processing.js` 文件。为每个函数生成完整 TSDoc 注释，说明用途、参数与返回值。」

Claude CLI functions as a specialized coding assistant, with inherent tools for core development tasks, including file ingestion, code structure analysis, and edit generation. Its deep integration with Git facilitates direct branch and commit management. The agent's extensibility is mediated by the Multi-tool Control Protocol (MCP), enabling users to define and integrate custom tools. This allows for interactions with private APIs, database queries, and execution of project-specific scripts. This architecture positions the developer as the arbiter of the agent's functional scope, effectively characterizing Claude as a reasoning engine augmented by user-defined tooling.

> Claude CLI 定位为面向编码场景的智能体：内置读文件、理解代码结构、批量修改等基础能力，并与 Git 深度集成，可在对话中直接完成分支与提交操作。其扩展能力通过 MCP（多工具控制协议）实现，用户可以挂载自定义工具，对接内网 API、数据库或项目脚本。整体上，开发者负责划定能力边界，而 Claude 则在既定工具集合上充当推理核心。

## Gemini CLI

> ## Gemini CLI

Google's Gemini CLI is a versatile, open-source AI agent designed for power and accessibility. It stands out with the advanced Gemini 2.5 Pro model, a massive context window, and multimodal capabilities (processing images and text). Its open-source nature, generous free tier, and "Reason and Act" loop make it a transparent, controllable, and excellent all-rounder for a broad audience, from hobbyists to enterprise developers, especially those within the Google Cloud ecosystem.

> Gemini CLI 兼具开源属性与较低的上手门槛，可接入 Gemini 2.5 Pro、长上下文以及图文多模态能力。其“推理—行动”循环使执行路径相对透明，免费额度也较为友好。无论是个人实验还是企业场景，尤其是已采用 Google Cloud 的团队，它都属于较为均衡的选择。

**Example Use Cases:**

> **示例用例：**

1. **Multimodal Development:** You provide a screenshot of a web component from a design file (gemini describe component.png) and instruct it: "Write the HTML and CSS code to build a React component that looks exactly like this. Make sure it's responsive."  
2. **Cloud Resource Management:** Using its built-in Google Cloud integration, you can command: "Find all GKE clusters in the production project that are running versions older than 1.28 and generate a gcloud command to upgrade them one by one."  
3. **Enterprise Tool Integration (via MCP):** A developer provides Gemini with a custom tool called get-employee-details that connects to the company's internal HR API. The prompt is: "Draft a welcome document for our new hire. First, use the get-employee-details --id=E90210 tool to fetch their name and team, and then populate the welcome_template.md with that information."  
4. **Large-Scale Refactoring**: A developer needs to refactor a large Java codebase to replace a deprecated logging library with a new, structured logging framework. They can use Gemini with a prompt like: Read all *.java files in the 'src/main/java' directory. For each file, replace all instances of the 'org.apache.log4j' import and its 'Logger' class with 'org.slf4j.Logger' and 'LoggerFactory'. Rewrite the logger instantiation and all .info(), .debug(), and .error() calls to use the new structured format with key-value pairs.  

> 1. **多模态开发：** 提供设计稿中某 Web 组件的截图（gemini describe component.png）并指示：「编写 HTML 与 CSS，构建外观与此完全一致的 React 组件，并确保响应式。」
> 2. **云资源管理：** 借助内置 Google Cloud 集成，可命令：「找出生产项目中所有运行版本低于 1.28 的 GKE 集群，并生成逐个升级的 gcloud 命令。」
> 3. **企业工具集成（经 MCP）：** 开发者为 Gemini 提供名为 get-employee-details、连接公司内部 HR API 的自定义工具。提示为：「为新员工起草欢迎文档。先用 get-employee-details --id=E90210 获取其姓名与团队，再将信息填入 welcome_template.md。」
> 4. **大规模重构：** 开发者需将大型 Java 代码库中已弃用的日志库替换为新的结构化日志框架，可使用类似提示：读取 `src/main/java` 下所有 `*.java` 文件；对每个文件，将所有 `org.apache.log4j` 导入及其 `Logger` 类替换为 `org.slf4j.Logger` 与 `LoggerFactory`；重写 logger 实例化及所有 `.info()`、`.debug()`、`.error()` 调用，改用带键值对的新结构化格式。

Gemini CLI is equipped with a suite of built-in tools that allow it to interact with its environment. These include tools for file system operations (like reading and writing), a shell tool for running commands, and tools for accessing the internet via web fetching and searching. For broader context, it uses specialized tools to read multiple files at once and a memory tool to save information for later sessions. This functionality is built on a secure foundation: sandboxing isolates the model's actions to prevent risk, while MCP servers act as a bridge, enabling Gemini to safely connect to your local environment or other APIs.

> 其工具集覆盖文件读写、shell 执行、联网检索与抓取，也支持批量读取文件及跨会话记忆。默认执行环境采用沙箱隔离以控制风险；当需要接入内网系统或私有 API 时，则可通过 MCP 服务器扩展，将外部能力以相对安全的方式接入对话流程。

## Aider

> ## Aider

Aider is an open-source AI coding assistant that acts as a true pair programmer by working directly on your files and committing changes to Git. Its defining feature is its directness; it applies edits, runs tests to validate them, and automatically commits every successful change. Being model-agnostic, it gives users complete control over cost and capabilities. Its git-centric workflow makes it perfect for developers who value efficiency, control, and a transparent, auditable trail of all code modifications.

> Aider 是开源 AI 编码助手，其工作方式非常直接：在仓库中原地修改文件、运行测试进行验证，并在每次成功后自动提交到 Git。由于支持更换底层模型，用户可以自主平衡成本与能力。如果团队以 Git 为中心、重视变更的可追溯性与可审计性，那么该工具尤其契合。

**Example Use Cases:**

> **示例用例：**

1. **Test-Driven Development (TDD):** A developer can say: "Create a failing test for a function that calculates the factorial of a number." After Aider writes the test and it fails, the next prompt is: "Now, write the code to make the test pass." Aider implements the function and runs the test again to confirm.  
2. **Precise Bug Squashing:** Given a bug report, you can instruct Aider: "The `calculate_total` function in billing.py fails on leap years. Add the file to the context, fix the bug, and verify your fix against the existing test suite."  
3. **Dependency Updates:** You could instruct it: "Our project uses an outdated version of the 'requests' library. Please go through all Python files, update the import statements and any deprecated function calls to be compatible with the latest version, and then update requirements.txt."  

> 1. **测试驱动开发（TDD）：** 开发者可说：「为计算数字阶乘的函数写一个会失败的测试。」Aider 写好测试并失败后，下一句提示：「现在编写使测试通过的代码。」Aider 实现函数并再次运行测试确认。
> 2. **精准修 bug：** 根据缺陷报告可指示：「`billing.py` 中的 `calculate_total` 在闰年出错。把该文件加入上下文，修复问题，并用现有测试套件验证。」
> 3. **依赖更新：** 可指示：「项目使用的 `requests` 库版本过旧。请遍历所有 Python 文件，更新 import 与已弃用调用以兼容最新版，并更新 requirements.txt。」

## GitHub Copilot CLI

> ## GitHub Copilot CLI

GitHub Copilot CLI extends the popular AI pair programmer into the terminal, with its primary advantage being its native, deep integration with the GitHub ecosystem. It understands the context of a project *within GitHub*. Its agent capabilities allow it to be assigned a GitHub issue, work on a fix, and submit a pull request for human review.

> Copilot CLI 将 Copilot 能力延伸至终端，核心优势在于与 GitHub 数据面的深度集成：Issue、PR 与代码索引天然联动。在智能体模式下，可承接指定 issue、创建分支修复缺陷并打开拉取请求供人工审阅。

**Example Use Cases:**

> **示例用例：**

1. **Automated Issue Resolution:** A manager assigns a bug ticket (e.g., "Issue #123: Fix off-by-one error in pagination") to the Copilot agent. The agent then checks out a new branch, writes the code, and submits a pull request referencing the issue, all without manual developer intervention.  
2. **Repository-Aware Q\&A:** A new developer on the team can ask: "Where in this repository is the database connection logic defined, and what environment variables does it require?" Copilot CLI uses its awareness of the entire repo to provide a precise answer with file paths.  
3. **Shell Command Helper:** When unsure about a complex shell command, a user can ask: gh? find all files larger than 50MB, compress them, and place them in an archive folder. Copilot will generate the exact shell command needed to perform the task.  

> 1. **自动化处理 Issue：** 管理者将缺陷单（如「Issue #123：修复分页的 off-by-one 错误」）指派给 Copilot 智能体；智能体检出分支、编写代码并提交引用该 issue 的 PR，全程无需开发者手动介入。
> 2. **仓库感知问答：** 新成员可问：「本仓库中数据库连接逻辑在哪里定义，需要哪些环境变量？」Copilot CLI 利用对整个仓库的感知给出含文件路径的精确答案。
> 3. **Shell 命令助手：** 面对复杂 shell 命令不确定时，用户可问：gh? find all files larger than 50MB, compress them, and place them in an archive folder。Copilot 会生成完成任务所需的确切 shell 命令。

## Terminal-Bench: A Benchmark for AI Agents in Command-Line Interfaces

> ## Terminal-Bench：命令行界面中 智能体的基准测试

Terminal-Bench is a novel evaluation framework designed to assess the proficiency of AI agents in executing complex tasks within a command-line interface. The terminal is identified as an optimal environment for AI agent operation due to its text-based, sandboxed nature. The initial release, Terminal-Bench-Core-v0, comprises 80 manually curated tasks spanning domains such as scientific workflows and data analysis. To ensure equitable comparisons, Terminus, a minimalistic agent, was developed to serve as a standardized testbed for various language models. The framework is designed for extensibility, allowing for the integration of diverse agents through containerization or direct connections. Future developments include enabling massively parallel evaluations and incorporating established benchmarks. The project encourages open-source contributions for task expansion and collaborative framework enhancement.

> Terminal-Bench 用来量化“CLI 智能体到底有多能打”。终端纯文本、易容器化，是理想的评测场。首发 Terminal-Bench-Core-v0 含 80 道人工挑选任务，横跨科研脚本、数据分析等。为公平对比，还提供极简基线智能体 Terminus，方便横向测不同模型。框架支持外挂自家 agent，也规划并行跑分与兼容其他基准，欢迎社区继续加题。

## Conclusion

> ## 结语

The emergence of these powerful AI command-line agents marks a fundamental shift in software development, transforming the terminal into a dynamic and collaborative environment. As we've seen, there is no single "best" tool; instead, a vibrant ecosystem is forming where each agent offers a specialized strength. The ideal choice depends entirely on the developer's needs: Claude for complex architectural tasks, Gemini for versatile and multimodal problem-solving, Aider for git-centric and direct code editing, and GitHub Copilot for seamless integration into the GitHub workflow. As these tools continue to evolve, proficiency in leveraging them will become an essential skill, fundamentally changing how developers build, debug, and manage software.

> 强大 AI CLI 的兴起，正在改写软件开发的面貌：终端正从被动执行器转变为可协作、可编排的工作环境。并不存在放之四海皆准的“最佳工具”，更合理的理解方式是将它们视为互补生态，并按场景选择：偏向架构级改造可优先考虑 Claude，偏向多模态与云原生整合可考虑 Gemini，偏向 Git 闭环与可审计提交可采用 Aider，而深度嵌入 GitHub issue/PR 流程的则更适合 Copilot CLI。随着这些工具持续演进，熟练运用它们将逐渐成为工程师的基础能力。

## References

1. Anthropic. *Claude*. [https://docs.anthropic.com/en/docs/claude-code/cli-reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
2. Google Gemini Cli [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)
3. Aider. [https://aider.chat/](https://aider.chat/)  
4. GitHub *Copilot CLI* [https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli](https://docs.github.com/en/copilot/github-copilot-enterprise/copilot-cli)  
5. Terminal Bench: [https://www.tbench.ai/](https://www.tbench.ai/)
