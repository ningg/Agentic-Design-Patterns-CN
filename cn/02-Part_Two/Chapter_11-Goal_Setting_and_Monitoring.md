# Chapter 11: Goal Setting and Monitoring

> 第 11 章：目标设定与监控

For AI agents to be truly effective and purposeful, they need more than just the ability to process information or use tools; they need a clear sense of direction and a way to know if they're actually succeeding. This is where the Goal Setting and Monitoring pattern comes into play. It's about giving agents specific objectives to work towards and equipping them with the means to track their progress and determine if those objectives have been met.

> 若要让 智能体真正有效、有的放矢，仅有信息处理或工具调用能力并不足够；还需要清晰的方向感，以及判断自身是否切实取得进展的手段。「目标设定与监控」模式正回应这一点：为智能体明确待达成的具体目标，并配套跟踪进度、判定目标是否完成的机制。

## Goal Setting and Monitoring Pattern Overview

> ## 目标设定与监控模式概览

Think about planning a trip. You don't just spontaneously appear at your destination. You decide where you want to go (the goal state), figure out where you are starting from (the initial state), consider available options (transportation, routes, budget), and then map out a sequence of steps: book tickets, pack bags, travel to the airport/station, board the transport, arrive, find accommodation, etc. This step-by-step process, often considering dependencies and constraints, is fundamentally what we mean by planning in agentic systems.

> 不妨以规划旅行为喻：人不会凭空出现在目的地。先要明确目的地（目标状态）与起点（初始状态），再权衡交通、路线、预算等选项，继而排出步骤：订票、打包、前往机场或车站、登车或登机、抵达、安排住宿等。这种往往牵涉依赖与约束的分步推进，正是智能体系统中「规划」的含义所在。

In the context of AI agents, planning typically involves an agent taking a high-level objective and autonomously, or semi-autonomously, generating a series of intermediate steps or sub-goals. These steps can then be executed sequentially or in a more complex flow, potentially involving other patterns like tool use, routing, or multi-agent collaboration. The planning mechanism might involve sophisticated search algorithms, logical reasoning, or increasingly, leveraging the capabilities of large language models (LLMs) to generate plausible and effective plans based on their training data and understanding of tasks.

> 在 智能体语境中，「规划」一般指：在获得高层目标后，自主或半自主地拆解出一串中间步骤或子目标；这些步骤既可线性执行，也可交织成更复杂的流程，并与工具调用、路由、多智能体协作等模式并用。其实现既可依托搜索与逻辑推理，也越来越多地借助 LLM，凭其训练所得与任务理解生成可行、有效的行动方案。

A good planning capability allows agents to tackle problems that aren't simple, single-step queries. It enables them to handle multi-faceted requests, adapt to changing circumstances by replanning, and orchestrate complex workflows. It's a foundational pattern that underpins many advanced agentic behaviors, turning a simple reactive system into one that can proactively work towards a defined objective.

> 良好的规划能力使智能体能处理非简单单步查询的问题：应对多面需求、通过重规划适应变化环境，并编排复杂工作流。它是支撑许多高级智能体行为的基础模式，把简单反应式系统转变为能主动朝明确目标推进的系统。

## Practical Applications & Use Cases

> ## 实践应用与用例

The Goal Setting and Monitoring pattern is essential for building agents that can operate autonomously and reliably in complex, real-world scenarios. Here are some practical applications:

> 「目标设定与监控」是构建能在复杂现实环境中自主、可靠运转的智能体时不可或缺的一环。下面列举若干典型应用：

* **Customer Support Automation:** An agent's goal might be to "resolve customer's billing inquiry." It monitors the conversation, checks database entries, and uses tools to adjust billing. Success is monitored by confirming the billing change and receiving positive customer feedback. If the issue isn't resolved, it escalates.  
* **Personalized Learning Systems:** A learning agent might have the goal to "improve students’ understanding of algebra." It monitors the student's progress on exercises, adapts teaching materials, and tracks performance metrics like accuracy and completion time, adjusting its approach if the student struggles.  
* **Project Management Assistants:** An agent could be tasked with "ensuring project milestone X is completed by Y date." It monitors task statuses, team communications, and resource availability, flagging delays and suggesting corrective actions if the goal is at risk.  
* **Automated Trading Bots:** A trading agent's goal might be to "maximize portfolio gains while staying within risk tolerance." It continuously monitors market data, its current portfolio value, and risk indicators, executing trades when conditions align with its goals and adjusting strategy if risk thresholds are breached.  
* **Robotics and Autonomous Vehicles:** An autonomous vehicle's primary goal is "safely transport passengers from A to B." It constantly monitors its environment (other vehicles, pedestrians, traffic signals), its own state (speed, fuel), and its progress along the planned route, adapting its driving behavior to achieve the goal safely and efficiently.  
* **Content Moderation:** An agent's goal could be to "identify and remove harmful content from platform X." It monitors incoming content, applies classification models, and tracks metrics like false positives/negatives, adjusting its filtering criteria or escalating ambiguous cases to human reviewers.

> * **客户支持自动化：** 目标可能是「解决客户的账单咨询」；监控对话、查库、用工具调整账单；通过确认账单变更与正向客户反馈判断成功，未解决则升级。
> * **个性化学习系统：** 目标可能是「提升学生对代数的理解」；监控练习进度、调整教材、跟踪准确率与完成时间等，遇困难则调整策略。
> * **项目管理助手：** 任务可能是「确保里程碑 X 在 Y 日前完成」；监控任务状态、团队沟通与资源，有风险时标出延误并建议纠偏。
> * **自动交易机器人：** 目标可能是「在风险承受范围内最大化组合收益」；持续监控市场、持仓与风险指标，条件符合时交易，触及风险阈值则调整策略。
> * **机器人与自动驾驶：** 首要目标多为「安全地将乘客从 A 运到 B」；持续监控环境（他车、行人、信号）与自身状态（速度、燃料）及路线进度，安全高效地调整驾驶行为。
> * **内容审核：** 目标可能是「识别并移除平台 X 上的有害内容」；监控流入内容、应用分类模型，跟踪误报/漏报等指标，调整过滤规则或将疑难案例交人工复核。

This pattern is fundamental for agents that need to operate reliably, achieve specific outcomes, and adapt to dynamic conditions, providing the necessary framework for intelligent self-management.

> 该模式对需要可靠运行、达成特定结果并适应动态条件的智能体至关重要，为智能自我管理提供必要框架。

## Hands-On Code Example

> ## 动手代码示例

To illustrate the Goal Setting and Monitoring pattern, we have an example using LangChain and OpenAI APIs. This Python script outlines an autonomous AI agent engineered to generate and refine Python code. Its core function is to produce solutions for specified problems, ensuring adherence to user-defined quality benchmarks.

> 为阐释「目标设定与监控」，本节提供一个基于 LangChain 与 OpenAI API 的示例：该 Python 脚本刻画了一个能够自主生成并反复修订 Python 代码的 智能体，其核心在于围绕给定问题生成实现，并持续对照用户设定的质量标准进行迭代。

It employs a "goal-setting and monitoring" pattern where it doesn't just generate code once, but enters into an iterative cycle of creation, self-evaluation, and improvement. The agent's success is measured by its own AI-driven judgment on whether the generated code successfully meets the initial objectives. The ultimate output is a polished, commented, and ready-to-use Python file that represents the culmination of this refinement process.

> 它体现了「目标设定 + 监控」的思路：流程并非一次生成即告结束，而是进入「编写—自评—改写」的闭环；是否达标由同一套 AI 基于反馈持续判定。最终交付的是经过多轮打磨、附带注释、可直接运行的 `.py` 文件，作为这一精炼过程的产物。

 **Dependencies**:

> **依赖：**

```python
pip install langchain_openai openai python-dotenv .env file with key in OPENAI_API_KEY
```

You can best understand this script by imagining it as an autonomous AI programmer assigned to a project (see Fig. 1). The process begins when you hand the AI a detailed project brief, which is the specific coding problem it needs to solve.

> 最直观的理解方式，是把脚本看作被指派到项目上的自主 AI 程序员（见图 1）：你交付一份详尽的项目简报，也就是待解决的具体编程问题。

```python
# MIT License
# Copyright (c) 2025 Mahtab Syed
# https://www.linkedin.com/in/mahtabsyed/

"""
Hands-On Code Example - Iteration 2
-  To illustrate the Goal Setting and Monitoring pattern, we have an example using LangChain and OpenAI APIs:

Objective: Build an AI Agent which can write code for a specified use case based on specified goals:
-  Accepts a coding problem (use case) in code or can be as input.
-  Accepts a list of goals (e.g., "simple", "tested", "handles edge cases")  in code or can be input.
-  Uses an LLM (like GPT-4o) to generate and refine Python code until the goals are met. (I am using max 5 iterations, this could be based on a set goal as well)
-  To check if we have met our goals I am asking the LLM to judge this and answer just True or False which makes it easier to stop the iterations.
-  Saves the final code in a .py file with a clean filename and a header comment.
"""

import os
import random
import re
from pathlib import Path

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv


# 🔐 Load environment variables
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("❌ Please set the OPENAI_API_KEY environment variable.")

# ✅ Initialize OpenAI model
print("📡 Initializing OpenAI LLM (gpt-4o)...")
llm = ChatOpenAI(
    model="gpt-4o",  # If you dont have access to got-4o use other OpenAI LLMs
    temperature=0.3,
    openai_api_key=OPENAI_API_KEY,
)


# --- Utility Functions ---
def generate_prompt(
    use_case: str, goals: list[str], previous_code: str = "", feedback: str = ""
) -> str:
    print("📝 Constructing prompt for code generation...")
    base_prompt = f"""
You are an AI coding agent. Your job is to write Python code based on the following use case:

Use Case: {use_case}

Your goals are:
{chr(10).join(f"- {g.strip()}" for g in goals)}
"""
    if previous_code:
        print("🔄 Adding previous code to the prompt for refinement.")
        base_prompt += f"\nPreviously generated code:\n{previous_code}"
    if feedback:
        print("📋 Including feedback for revision.")
        base_prompt += f"\nFeedback on previous version:\n{feedback}\n"

    base_prompt += "\nPlease return only the revised Python code. Do not include comments or explanations outside the code."
    return base_prompt


def get_code_feedback(code: str, goals: list[str]) -> str:
    print("🔍 Evaluating code against the goals...")
    feedback_prompt = f"""
You are a Python code reviewer. A code snippet is shown below. Based on the following goals:

{chr(10).join(f"- {g.strip()}" for g in goals)}

Please critique this code and identify if the goals are met. Mention if improvements are needed for clarity, simplicity, correctness, edge case handling, or test coverage.

Code:
{code}
"""
    return llm.invoke(feedback_prompt)


def goals_met(feedback_text: str, goals: list[str]) -> bool:
    """
    Uses the LLM to evaluate whether the goals have been met based on the feedback text.
    Returns True or False (parsed from LLM output).
    """
    review_prompt = f"""
You are an AI reviewer.

Here are the goals:
{chr(10).join(f"- {g.strip()}" for g in goals)}

Here is the feedback on the code:
\"\"\"
{feedback_text}
\"\"\"

Based on the feedback above, have the goals been met?

Respond with only one word: True or False.
"""
    response = llm.invoke(review_prompt).content.strip().lower()
    return response == "true"


def clean_code_block(code: str) -> str:
    lines = code.strip().splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "\n".join(lines).strip()


def add_comment_header(code: str, use_case: str) -> str:
    comment = f"# This Python program implements the following use case:\n# {use_case.strip()}\n"
    return comment + "\n" + code


def to_snake_case(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return re.sub(r"\s+", "_", text.strip().lower())


def save_code_to_file(code: str, use_case: str) -> str:
    print("💾 Saving final code to file...")

    summary_prompt = (
        f"Summarize the following use case into a single lowercase word or phrase, "
        f"no more than 10 characters, suitable for a Python filename:\n\n{use_case}"
    )
    raw_summary = llm.invoke(summary_prompt).content.strip()
    short_name = re.sub(r"[^a-zA-Z0-9_]", "", raw_summary.replace(" ", "_").lower())[:10]

    random_suffix = str(random.randint(1000, 9999))
    filename = f"{short_name}_{random_suffix}.py"
    filepath = Path.cwd() / filename

    with open(filepath, "w") as f:
        f.write(code)

    print(f"✅ Code saved to: {filepath}")
    return str(filepath)


# --- Main Agent Function ---
def run_code_agent(use_case: str, goals_input: str, max_iterations: int = 5) -> str:
    goals = [g.strip() for g in goals_input.split(",")]

    print(f"\n🎯 Use Case: {use_case}")
    print("🎯 Goals:")
    for g in goals:
        print(f"  - {g}")

    previous_code = ""
    feedback = ""

    for i in range(max_iterations):
        print(f"\n=== 🔁 Iteration {i + 1} of {max_iterations} ===")
        prompt = generate_prompt(
            use_case,
            goals,
            previous_code,
            feedback if isinstance(feedback, str) else feedback.content,
        )

        print("🚧 Generating code...")
        code_response = llm.invoke(prompt)
        raw_code = code_response.content.strip()
        code = clean_code_block(raw_code)
        print("\n🧾 Generated Code:\n" + "-" * 50 + f"\n{code}\n" + "-" * 50)

        print("\n📤 Submitting code for feedback review...")
        feedback = get_code_feedback(code, goals)
        feedback_text = feedback.content.strip()
        print("\n📥 Feedback Received:\n" + "-" * 50 + f"\n{feedback_text}\n" + "-" * 50)

        if goals_met(feedback_text, goals):
            print("✅ LLM confirms goals are met. Stopping iteration.")
            break

        print("🛠️ Goals not fully met. Preparing for next iteration...")
        previous_code = code

    final_code = add_comment_header(code, use_case)
    return save_code_to_file(final_code, use_case)


# --- CLI Test Run ---
if __name__ == "__main__":
    print("\n🧠 Welcome to the AI Code Generation Agent")

    # Example 1
    use_case_input = "Write code to find BinaryGap of a given positive integer"
    goals_input = "Code simple to understand, Functionally correct, Handles comprehensive edge cases, Takes positive integer input only, prints the results with few examples"
    run_code_agent(use_case_input, goals_input)

    # Example 2
    # use_case_input = "Write code to count the number of files in current directory and all its nested sub directories, and print the total count"
    # goals_input = (
    #     "Code simple to understand, Functionally correct, Handles comprehensive edge cases, Ignore recommendations for performance, Ignore recommendations for test suite use like unittest or pytest"
    # )
    # run_code_agent(use_case_input, goals_input)

    # Example 3
    # use_case_input = "Write code which takes a command line input of a word doc or docx file and opens it and counts the number of words, and characters in it and prints all"
    # goals_input = "Code simple to understand, Functionally correct, Handles edge cases"
    # run_code_agent(use_case_input, goals_input)
```

Along with this brief, you provide a strict quality checklist, which represents the objectives the final code must meet—criteria like "the solution must be simple," "it must be functionally correct," or "it needs to handle unexpected edge cases."

> 除简报外，你还提供严格的质量清单，代表最终代码必须满足的目标，例如「解法要简单」「功能正确」「能处理意外边界情况」等。

![Goal Setting and Monitor example](../assets-new/Goal_Setting_and_Monitoring.png)

Fig.1: Goal Setting and Monitor example

> 图 1：目标设定与监控示例

With this assignment in hand, the AI programmer gets to work and produces its first draft of the code. However, instead of immediately submitting this initial version, it pauses to perform a crucial step: a rigorous self-review. It meticulously compares its own creation against every item on the quality checklist you provided, acting as its own quality assurance inspector. After this inspection, it renders a simple, unbiased verdict on its own progress: "True" if the work meets all standards, or "False" if it falls short.

> 接到任务后，AI 程序员会先产出代码初稿，但不会立即提交，而是先执行关键一步：严格自审——对照你给出的质量清单逐项核查产出，同时承担作者与质量审查者的双重角色；随后给出简明且审慎的判断：若全部满足要求则为「True」，否则为「False」。

If the verdict is "False," the AI doesn't give up. It enters a thoughtful revision phase, using the insights from its self-critique to pinpoint the weaknesses and intelligently rewrite the code. This cycle of drafting, self-reviewing, and refining continues, with each iteration aiming to get closer to the goals. This process repeats until the AI finally achieves a "True" status by satisfying every requirement, or until it reaches a predefined limit of attempts, much like a developer working against a deadline. Once the code passes this final inspection, the script packages the polished solution, adding helpful comments and saving it to a clean, new Python file, ready for use.

> 若结论为「False」，流程不会终止，而会进入修订阶段：依据自评暴露出的薄弱环节改写代码。起草、自审、打磨的循环会持续进行，每一轮都力求更接近目标；直至满足全部条件并得到「True」，或触及预设的迭代上限（类似开发者在截止日前进行有限次数的返工）。通过终审后，脚本会将最终成果整理完备、附上说明性注释，并写入一份命名清晰的 `.py` 文件，便于直接使用。

**Caveats and Considerations:** It is important to note that this is an exemplary illustration and not production-ready code. For real-world applications, several factors must be taken into account. An LLM may not fully grasp the intended meaning of a goal and might incorrectly assess its performance as successful. Even if the goal is well understood, the model may hallucinate. When the same LLM is responsible for both writing the code and judging its quality, it may have a harder time discovering it is going in the wrong direction.

> **注意与考量：** 本例仅供演示，不宜直接用于生产。落地时须谨记：LLM 可能曲解目标却仍判定「已完成」；即便理解无误也可能产生幻觉；若同一模型兼司编码与评审，往往更难察觉自身偏离正轨。

Ultimately, LLMs do not produce flawless code by magic; you still need to run and test the produced code. Furthermore, the "monitoring" in the simple example is basic and creates a potential risk of the process running forever.

> 归根结底，LLM 并不能魔术般给出无瑕代码；生成结果仍需实际运行与测试验证。此外，示例里的「监控」较为简陋，存在迭代无法自行终止、理论上可能一直跑下去的风险。

```text
Act as an expert code reviewer with a deep commitment to producing clean, correct, and simple code. Your core mission is to eliminate code "hallucinations" by ensuring every suggestion is grounded in reality and best practices. When I provide you with a code snippet, I want you to: -- Identify and Correct Errors: Point out any logical flaws, bugs, or potential runtime errors. -- Simplify and Refactor: Suggest changes that make the code more readable, efficient, and maintainable without sacrificing correctness. -- Provide Clear Explanations: For every suggested change, explain why it is an improvement, referencing principles of clean code, performance, or security. -- Offer Corrected Code: Show the "before" and "after" of your suggested changes so the improvement is clear. Your feedback should be direct, constructive, and always aimed at improving the quality of the code.
```

A more robust approach involves separating these concerns by giving specific roles to a crew of agents. For instance, I have built a personal crew of AI agents using Gemini where each has a specific role:

> 更稳妥的做法是职责分离，由多个智能体各专一事。例如笔者曾用 Gemini 搭建个人「智能体小队」，角色划分如下：

* The Peer Programmer: Helps write and brainstorm code.  
* The Code Reviewer: Catches errors and suggests improvements.  
* The Documenter: Generates clear and concise documentation.  
* The Test Writer: Creates comprehensive unit tests.  
* The Prompt Refiner: Optimizes interactions with the AI.

> * **同伴程序员：** 协助编写与头脑风暴代码。
> * **代码审查员：** 发现错误并提出改进。
> * **文档撰写者：** 生成清晰简洁的文档。
> * **测试编写者：** 编写全面的单元测试。
> * **提示优化者：** 优化与 AI 的交互。

In this multi-agent system, the Code Reviewer, acting as a separate entity from the programmer agent, has a prompt similar to the judge in the example, which significantly improves objective evaluation. This structure naturally leads to better practices, as the Test Writer agent can fulfill the need to write unit tests for the code produced by the Peer Programmer.

> 在这一多智能体设置中，审查者与编码者彼此独立，前者的提示角色接近示例里的「裁判」，有利于提高评判的客观性；测试编写者则能为同伴程序员的产出补齐单元测试，从结构上推动更稳妥的工程习惯。

I leave to the interested reader the task of adding these more sophisticated controls and making the code closer to production-ready.

> 更复杂的控制与接近生产就绪的改造，留给有兴趣的读者自行完成。

## At a Glance

> ## 一览

**What**: AI agents often lack a clear direction, preventing them from acting with purpose beyond simple, reactive tasks. Without defined objectives, they cannot independently tackle complex, multi-step problems or orchestrate sophisticated workflows. Furthermore, there is no inherent mechanism for them to determine if their actions are leading to a successful outcome. This limits their autonomy and prevents them from being truly effective in dynamic, real-world scenarios where mere task execution is insufficient.

> **问题：** 智能体常缺乏清晰方向，难以超越简单反应式任务而有目的地行动；没有明确目标就无法独立处理复杂多步问题或编排精细工作流；也缺乏内在机制判断行为是否通向成功。这限制其自主性，使其在动态真实场景中仅靠执行任务难以真正有效。

**Why**: The Goal Setting and Monitoring pattern provides a standardized solution by embedding a sense of purpose and self-assessment into agentic systems. It involves explicitly defining clear, measurable objectives for the agent to achieve. Concurrently, it establishes a monitoring mechanism that continuously tracks the agent's progress and the state of its environment against these goals. This creates a crucial feedback loop, enabling the agent to assess its performance, correct its course, and adapt its plan if it deviates from the path to success. By implementing this pattern, developers can transform simple reactive agents into proactive, goal-oriented systems capable of autonomous and reliable operation.

> **思路：** 「目标设定与监控」模式通过为智能体系统注入目的感与自评机制提供标准化解法：为智能体明确可衡量的目标，并建立监控机制，持续对照目标跟踪智能体进度与环境状态，形成关键反馈回路，使其能评估表现、纠正航向、偏离成功路径时调整计划。实现该模式可将简单反应式智能体转变为主动、目标导向且能自主可靠运行的系统。

**Rule of thumb**: Use this pattern when an AI agent must autonomously execute a multi-step task, adapt to dynamic conditions, and reliably achieve a specific, high-level objective without constant human intervention.

> **经验法则：** 当 智能体须自主执行多步任务、适应动态条件，并在较少人工干预下可靠达成特定高层目标时，采用本模式。

**Visual summary:**

> **图示摘要：**

![Goal Design Pattern](../assets-new/Goal_Design_Pattern.png)

Fig.2: Goal design patterns

> 图 2：目标设计模式

## Key takeaways

> ## 要点

Key takeaways include:

> 要点包括：

* Goal Setting and Monitoring equips agents with purpose and mechanisms to track progress.  
* Goals should be specific, measurable, achievable, relevant, and time-bound (SMART).  
* Clearly defining metrics and success criteria is essential for effective monitoring.  
* Monitoring involves observing agent actions, environmental states, and tool outputs.  
* Feedback loops from monitoring allow agents to adapt, revise plans, or escalate issues.  
* In Google's ADK, goals are often conveyed through agent instructions, with monitoring accomplished through state management and tool interactions.

> * 目标设定与监控为智能体赋予目的与跟踪进度的机制。
> * 目标宜符合 SMART（具体、可衡量、可达成、相关、有时限）。
> * 明确定义指标与成功标准对有效监控至关重要。
> * 监控包括观察智能体行为、环境状态与工具输出。
> * 监控带来的反馈回路使智能体能适应、修订计划或升级问题。
> * 在 Google ADK 中，目标常通过智能体指令传达，监控则常借助状态管理与工具交互完成。

## Conclusion

> ## 结语

This chapter focused on the crucial paradigm of Goal Setting and Monitoring. I highlighted how this concept transforms AI agents from merely reactive systems into proactive, goal-driven entities. The text emphasized the importance of defining clear, measurable objectives and establishing rigorous monitoring procedures to track progress. Practical applications demonstrated how this paradigm supports reliable autonomous operation across various domains, including customer service and robotics. A conceptual coding example illustrates the implementation of these principles within a structured framework, using agent directives and state management to guide and evaluate an agent's achievement of its specified goals. Ultimately, equipping agents with the ability to formulate and oversee goals is a fundamental step toward building truly intelligent and accountable AI systems.

> 本章围绕「目标设定与监控」这一核心范式展开，阐明它如何把 智能体从被动反应式系统，推向主动、目标导向的行为体；并强调可量化目标与严密监控对把握进度不可或缺。应用部分展示该范式如何支撑客服、机器人等场景下的稳健自主运行；示例代码则从工程角度演示如何借助指令与状态管理，引导并检验智能体是否达成既定目标。归根结底，赋予智能体设定目标与审视自身进展的能力，是迈向更可信、更可问责的 AI 系统的基石之一。

## References

1. SMART Goals Framework. [https://en.wikipedia.org/wiki/SMART\_criteria](https://en.wikipedia.org/wiki/SMART_criteria)
