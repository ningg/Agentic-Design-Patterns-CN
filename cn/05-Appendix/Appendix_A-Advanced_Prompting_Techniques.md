# Appendix A: Advanced Prompting Techniques

> 附录 A：高级提示技巧

## Introduction to Prompting

> ## 提示简介

Prompting, the primary interface for interacting with language models, is the process of crafting inputs to guide the model towards generating a desired output. This involves structuring requests, providing relevant context, specifying the output format, and demonstrating expected response types. Well-designed prompts can maximize the potential of language models, resulting in accurate, relevant, and creative responses. In contrast, poorly designed prompts can lead to ambiguous, irrelevant, or erroneous outputs.

> 提示是与语言模型打交道的主要方式：通过设计输入，引导模型产出你想要的结果。它涵盖如何组织请求、补充语境、规定输出格式，以及用示例示范期望的回答形态。提示写得好，模型更容易给出准确、相关且有创意的回复；写得含糊，则往往得到模棱两可、文不对题或明显错误的输出。

The objective of prompt engineering is to consistently elicit high-quality responses from language models. This requires understanding the capabilities and limitations of the models and effectively communicating intended goals. It involves developing expertise in communicating with AI by learning how to best instruct it.

> 提示工程的目标，是让模型在一次次调用中持续给出高质量回答。这要求你理解模型能做什么、做不到什么，并把目标说清楚；也意味着要学会怎样向 AI 下指令，把与模型协作练成一种可迁移的能力。

This appendix details various prompting techniques that extend beyond basic interaction methods. It explores methodologies for structuring complex requests, enhancing the model's reasoning abilities, controlling output formats, and integrating external information. These techniques are applicable to building a range of applications, from simple chatbots to complex multi-agent systems, and can improve the performance and reliability of agentic applications.

> 本附录在基础对话之上，展开一系列提示技巧：如何拆解复杂请求、强化推理、约束输出形态、接入外部知识等。它们既适用于轻量聊天机器人，也适用于复杂多智能体系统，并能整体抬高智能体应用的稳定性与可用性。

Agentic patterns, the architectural structures for building intelligent systems, are detailed in the main chapters. These patterns define how agents plan, utilize tools, manage memory, and collaborate. The efficacy of these agentic systems is contingent upon their ability to interact meaningfully with language models.

> 智能体模式——即搭建智能系统的结构方式——在正文中有系统阐述：它们规定智能体如何规划、调用工具、维护记忆与彼此协作。整套系统是否好用，很大程度上取决于智能体与语言模型之间能否形成清晰、可重复的交互。

## Core Prompting Principles

> ## 核心提示原则

Core Principles for Effective Prompting of Language Models:

> 面向语言模型做有效提示时，应把握以下核心原则：

Effective prompting rests on fundamental principles guiding communication with language models, applicable across various models and task complexities. Mastering these principles is essential for consistently generating useful and accurate responses.

> 有效提示背后，是一套与语言模型沟通的通用原则，并不会因模型迭代或任务复杂化而失效。真正掌握这些原则，才更容易稳定获得有用且准确的回答。

**Clarity and Specificity**: Instructions should be unambiguous and precise. Language models interpret patterns; multiple interpretations may lead to unintended responses. Define the task, desired output format, and any limitations or requirements. Avoid vague language or assumptions. Inadequate prompts yield ambiguous and inaccurate responses, hindering meaningful output.

> **清晰与具体：** 指令要写得没有歧义、边界清楚。模型靠模式补全语义，一句话多种读法就会走向意外结果。请写清任务是什么、希望以什么格式交付、有哪些硬性约束；少用“看着办”式措辞，也少埋隐含前提。提示不到位，输出往往含糊或偏离，难以真正可用。

**Conciseness**: While specificity is crucial, it should not compromise conciseness. Instructions should be direct. Unnecessary wording or complex sentence structures can confuse the model or obscure the primary instruction. Prompts should be simple; what is confusing to the user is likely confusing to the model. Avoid intricate language and superfluous information. Use direct phrasing and active verbs to clearly delineate the desired action. Effective verbs include: Act, Analyze, Categorize, Classify, Contrast, Compare, Create, Describe, Define, Evaluate, Extract, Find, Generate, Identify, List, Measure, Organize, Parse, Pick, Predict, Provide, Rank, Recommend, Return, Retrieve, Rewrite, Select, Show, Sort, Summarize, Translate, Write.

> **简洁：** 具体并不意味着冗长。在信息充分的前提下，应尽量直接表达核心要求：迂回冗长的句子既消耗 token，也容易使模型偏离重点。可以记住一条经验法则：连人都觉得难懂的句子，模型通常也难以准确把握。应多用主动动词明确任务，少用装饰性从句。常见且有效的动词包括：Act、Analyze、Categorize、Classify、Contrast、Compare、Create、Describe、Define、Evaluate、Extract、Find、Generate、Identify、List、Measure、Organize、Parse、Pick、Predict、Provide、Rank、Recommend、Return、Retrieve、Rewrite、Select、Show、Sort、Summarize、Translate、Write。

**Using Verbs:** Verb choice is a key prompting tool. Action verbs indicate the expected operation. Instead of "Think about summarizing this," a direct instruction like "Summarize the following text" is more effective. Precise verbs guide the model to activate relevant training data and processes for that specific task.

> **善用动词：** 动词是提示中最有效的控制杠杆之一，直接决定模型需要执行的操作类型。与其写“想想如何总结下面这段内容”，不如明确写成“总结以下文本”。动词越精确，越能激活与任务相匹配的知识与推理模式。

**Instructions Over Constraints:** Positive instructions are generally more effective than negative constraints. Specifying the desired action is preferred to outlining what not to do. While constraints have their place for safety or strict formatting, excessive reliance can cause the model to focus on avoidance rather than the objective. Frame prompts to guide the model directly. Positive instructions align with human guidance preferences and reduce confusion.

> **指令优于约束：** 多写“请产出什么”，少写一长串“不许怎样”。在安全、合规或版式极严的场景里，否定式约束仍然必要；但若通篇都是禁令，模型容易把注意力耗在躲坑上，反而忘了正事。把力气花在正面引导上，既贴近人类协作习惯，也降低误读空间。

**Experimentation and Iteration:** Prompt engineering is an iterative process. Identifying the most effective prompt requires multiple attempts. Begin with a draft, test it, analyze the output, identify shortcomings, and refine the prompt. Model variations, configurations (like temperature or top-p), and slight phrasing changes can yield different results. Documenting attempts is vital for learning and improvement. Experimentation and iteration are necessary to achieve the desired performance.

> **实验与迭代：** 好提示很少一次写成。更稳妥的路径是：先打一版草稿 → 跑真实用例 → 对照目标找差距 → 再改措辞或结构。换模型、调 temperature / top-p、微调一句话，结果都可能明显不同。把每次版本与效果记下来，复盘成本会低很多；想稳定达到预期，迭代几乎是必修课。

These principles form the foundation of effective communication with language models. By prioritizing clarity, conciseness, action verbs, positive instructions, and iteration, a robust framework is established for applying more advanced prompting techniques.

> 以上原则是与语言模型协作的底层语法：先把事情说清楚、写短写准、用对动词、多用正面指引，并愿意反复试。做到这几条，再谈更复杂的提示模式，会轻松得多。

## Basic Prompting Techniques

> ## 基础提示技术

Building on core principles, foundational techniques provide language models with varying levels of information or examples to direct their responses. These methods serve as an initial phase in prompt engineering and are effective for a wide spectrum of applications.

> 在原则之上，基础技术解决的是“给模型多少示范”：零示例、一条示例，或几条示例。它们几乎是所有提示工作的起点，也能覆盖大量日常应用场景。

### Zero-Shot Prompting

> ### 零样本提示（Zero-Shot）

Zero-shot prompting is the most basic form of prompting, where the language model is provided with an instruction and input data without any examples of the desired input-output pair. It relies entirely on the model's pre-training to understand the task and generate a relevant response. Essentially, a zero-shot prompt consists of a task description and initial text to begin the process.

> 零样本提示最朴素：只描述任务、贴上输入，不给任何“示范答案”。模型完全靠预训练里见过的模式来猜你要什么；提示本身通常就是“任务说明 + 待处理文本”。

* **When to use:** Zero-shot prompting is often sufficient for tasks that the model has likely encountered extensively during its training, such as simple question answering, text completion, or basic summarization of straightforward text. It's the quickest approach to try first.  
* **Example:**  
  Translate the following English sentence to French: 'Hello, how are you?'

> * **何时使用：** 若任务形态在预训练语料里很常见——简单问答、续写、对直白短文做摘要等——零样本往往就够用；也是排查问题时最值得先试的一条捷径。
> * **示例：**
>   将下列英文句子译成法语：'Hello, how are you?'

### One-Shot Prompting

> ### 单样本提示（One-Shot）

One-shot prompting involves providing the language model with a single example of the input and the corresponding desired output prior to presenting the actual task. This method serves as an initial demonstration to illustrate the pattern the model is expected to replicate. The purpose is to equip the model with a concrete instance that it can use as a template to effectively execute the given task.

> 单样本提示会先在正文任务前放一组“输入 → 期望输出”，相当于递给模型一张格式样张；后面的真实请求，就按同一套路来仿写。

* **When to use:** One-shot prompting is useful when the desired output format or style is specific or less common. It gives the model a concrete instance to learn from. It can improve performance compared to zero-shot for tasks requiring a particular structure or tone.  
* **Example:**  
  Translate the following English sentences to Spanish:  
  English: 'Thank you.'  
  Spanish: 'Gracias.'

  English: 'Please.'  
  Spanish:

> * **何时使用：** 一旦目标格式、语气或体裁不太“标准”，单样本通常比光说不练更有效；有一个看得见的实例，模型更容易对齐结构与口吻。
> * **示例：**
>   将下列英文句子译成西班牙语：
>   English: 'Thank you.'
>   Spanish: 'Gracias.'
>
>   English: 'Please.'
>   Spanish:

### Few-Shot Prompting

> ### 少样本提示（Few-Shot）

Few-shot prompting enhances one-shot prompting by supplying several examples, typically three to five, of input-output pairs. This aims to demonstrate a clearer pattern of expected responses, improving the likelihood that the model will replicate this pattern for new inputs. This method provides multiple examples to guide the model to follow a specific output pattern.

> 少样本提示是在单样本基础上再提供若干组（通常为三到五组）输入—输出示例，使期望模式更为清晰；面对新输入时，模型按该模式生成正确结果的概率通常也会随之提高。

* **When to use:** Few-shot prompting is particularly effective for tasks where the desired output requires adhering to a specific format, style, or exhibiting nuanced variations. It's excellent for tasks like classification, data extraction with specific schemas, or generating text in a particular style, especially when zero-shot or one-shot don't yield consistent results. Using at least three to five examples is a general rule of thumb, adjusting based on task complexity and model token limits.  
* **Importance of Example Quality and Diversity:** The effectiveness of few-shot prompting heavily relies on the quality and diversity of the examples provided. Examples should be accurate, representative of the task, and cover potential variations or edge cases the model might encounter. High-quality, well-written examples are crucial; even a small mistake can confuse the model and result in undesired output. Including diverse examples helps the model generalize better to unseen inputs.  
* **Mixing Up Classes in Classification Examples:** When using few-shot prompting for classification tasks (where the model needs to categorize input into predefined classes), it's a best practice to mix up the order of the examples from different classes. This prevents the model from potentially overfitting to the specific sequence of examples and ensures it learns to identify the key features of each class independently, leading to more robust and generalizable performance on unseen data.  
* **Evolution to "Many-Shot" Learning:** As modern LLMs like Gemini get stronger with long context modeling, they are becoming highly effective at utilizing "many-shot" learning. This means optimal performance for complex tasks can now be achieved by including a much larger number of examples—sometimes even hundreds—directly within the prompt, allowing the model to learn more intricate patterns.  
* **Example:**  
  Classify the sentiment of the following movie reviews as POSITIVE, NEUTRAL, or NEGATIVE:

  Review: "The acting was superb and the story was engaging."  
  Sentiment: POSITIVE

  Review: "It was okay, nothing special."  
  Sentiment: NEUTRAL

  Review: "I found the plot confusing and the characters unlikable."  
  Sentiment: NEGATIVE

  Review: "The visuals were stunning, but the dialogue was weak."  
  Sentiment:

> * **何时使用：** 需要严格版式、固定栏目、细粒度风格差异，或做分类 / 结构化抽取时，少样本往往是标配；若零样本、单样本抖动大，更应加码示例。经验上三到五对是常见起点，再按任务难度和上下文长度微调。
> * **示例质量与多样性的重要性：** 少样本提示的效果高度依赖示例本身。示例应准确、贴近真实业务，并尽量覆盖可能出现的变体与边界情况。哪怕是很小的错误，也可能被模型误学为规律；示例越多样，面对未见过的新输入时表现通常越稳健。
> * **分类任务中打乱类别顺序：** 做分类时，别把同类示例全堆在一起；打乱顺序可以减轻模型对“排列套路”的投机，逼它去学每一类的判别特征，泛化通常更稳。
> * **向“多样本”演进：** 长上下文模型（如 Gemini 系列）使在同一提示中放入大量示例成为可能；对于复杂任务，有时确实需要几十甚至上百条示例，才能让模型掌握更细粒度的模式。
> * **示例：**
>   将下列影评情感分类为 POSITIVE、NEUTRAL 或 NEGATIVE：
>
>   Review: "The acting was superb and the story was engaging."
>   Sentiment: POSITIVE
>
>   Review: "It was okay, nothing special."
>   Sentiment: NEUTRAL
>
>   Review: "I found the plot confusing and the characters unlikable."
>   Sentiment: NEGATIVE
>
>   Review: "The visuals were stunning, but the dialogue was weak."
>   Sentiment:

Understanding when to apply zero-shot, one-shot, and few-shot prompting techniques, and thoughtfully crafting and organizing examples, are essential for enhancing the effectiveness of agentic systems. These basic methods serve as the groundwork for various prompting strategies.

> 清楚何时使用零样本、单样本或少样本提示，并认真打磨示例的顺序与内容，是提升智能体表现成本较低却效果显著的方法；许多更复杂的提示模式，本质上也建立在这层基本功之上。

## Structuring Prompts

> ## 组织提示的结构

Beyond the basic techniques of providing examples, the way you structure your prompt plays a critical role in guiding the language model. Structuring involves using different sections or elements within the prompt to provide distinct types of information, such as instructions, context, or examples, in a clear and organized manner. This helps the model parse the prompt correctly and understand the specific role of each piece of text.

> 光有示例还不够：提示怎么排版、怎么分块，往往决定模型读不读得懂。结构化就是把指令、背景、样例、待处理输入拆成彼此分明的段落或标签，让模型一眼知道每一段扮演什么角色。

### System Prompting

> ### 系统提示（System Prompting）

System prompting sets the overall context and purpose for a language model, defining its intended behavior for an interaction or session. This involves providing instructions or background information that establish rules, a persona, or overall behavior. Unlike specific user queries, a system prompt provides foundational guidelines for the model's responses. It influences the model's tone, style, and general approach throughout the interaction. For example, a system prompt can instruct the model to consistently respond concisely and helpfully or ensure responses are appropriate for a general audience. System prompts are also utilized for safety and toxicity control by including guidelines such as maintaining respectful language.

> 系统提示负责给整段对话定调：说明模型扮演谁、遵守哪些红线、默认语气与深度如何。它不像单条用户提问那样转瞬即逝，而是持续约束后续所有回复；也常承担安全与文明用语等底线规则。

Furthermore, to maximize their effectiveness, system prompts can undergo automatic prompt optimization through LLM-based iterative refinement. Services like the Vertex AI Prompt Optimizer facilitate this by systematically improving prompts based on user-defined metrics and target data, ensuring the highest possible performance for a given task.

> 系统提示同样可以“机器调参”：用 LLM 反复改写、再用你定义的指标打分，自动逼近更优版本。Google Cloud 上的 Vertex AI Prompt Optimizer 就是面向这类闭环的工具之一。

* **Example:**  
  You are a helpful and harmless AI assistant. Respond to all queries in a polite and informative manner. Do not generate content that is harmful, biased, or inappropriate

> * **示例：**
>   You are a helpful and harmless AI assistant. Respond to all queries in a polite and informative manner. Do not generate content that is harmful, biased, or inappropriate

### Role Prompting

> ### 角色提示（Role Prompting）

Role prompting assigns a specific character, persona, or identity to the language model, often in conjunction with system or contextual prompting. This involves instructing the model to adopt the knowledge, tone, and communication style associated with that role. For example, prompts such as "Act as a travel guide" or "You are an expert data analyst" guide the model to reflect the perspective and expertise of that assigned role. Defining a role provides a framework for the tone, style, and focused expertise, aiming to enhance the quality and relevance of the output. The desired style within the role can also be specified, for instance, "a humorous and inspirational style."

> 角色提示让模型“戴上某副眼镜”——指定职业身份、口吻或知识边界，常与系统提示、动态语境一起出现。一句“你是资深导游”“你是偏保守的风险分析师”，就会显著改变推理角度与措辞；也可叠加“要幽默但要专业”这类风格细项。

* **Example:**  
  Act as a seasoned travel blogger. Write a short, engaging paragraph about the best hidden gem in Rome.

> * **示例：**
>   Act as a seasoned travel blogger. Write a short, engaging paragraph about the best hidden gem in Rome.

### Using Delimiters

> ### 使用分隔符

Effective prompting involves clear distinction of instructions, context, examples, and input for language models. Delimiters, such as triple backticks (```), XML tags (<instruction>, <context>), or markers (---), can be utilized to visually and programmatically separate these sections. This practice, widely used in prompt engineering, minimizes misinterpretation by the model, ensuring clarity regarding the role of each part of the prompt.

> 当提示里同时出现规则、背景、例题和真实输入时，务必让它们“物理上”也分得开：三反引号代码块、XML 风格标签（如 `<instruction>` / `<context>`）、或 `---` 一类的显式分隔线都可以。目的只有一个——降低串台，让模型别把你的数据当成新指令。

* **Example:**  
  <instruction>Summarize the following article, focusing on the main arguments presented by the author.</instruction>  
  <article>  
  [Insert the full text of the article here]  
  </article>

> * **示例：**
>   <instruction>Summarize the following article, focusing on the main arguments presented by the author.</instruction>
>   <article>
>   [Insert the full text of the article here]
>   </article>

## Contextual Engineering

> ## 上下文工程（Context Engineering）

Context engineering, unlike static system prompts, dynamically provides background information crucial for tasks and conversations. This ever-changing information helps models grasp nuances, recall past interactions, and integrate relevant details, leading to grounded responses and smoother exchanges. Examples include previous dialogue, relevant documents (as in Retrieval Augmented Generation), or specific operational parameters. For instance, when discussing a trip to Japan, one might ask for three family-friendly activities in Tokyo, leveraging the existing conversational context. In agentic systems, context engineering is fundamental to core agent behaviors like memory persistence, decision-making, and coordination across sub-tasks. Agents with dynamic contextual pipelines can sustain goals over time, adapt strategies, and collaborate seamlessly with other agents or tools—qualities essential for long-term autonomy. This methodology posits that the quality of a model's output depends more on the richness of the provided context than on the model's architecture. It signifies a significant evolution from traditional prompt engineering, which primarily focused on optimizing the phrasing of immediate user queries. Context engineering expands its scope to include multiple layers of information.

> 如果说系统提示定义的是长期角色设定，那么上下文工程关注的就是“模型在当前时刻应当掌握哪些信息”。它把历史轮次、检索到的文档（RAG）、工具返回结果以及业务参数等动态注入上下文窗口，使回答建立在事实与当前上下文之上，而非凭空续写。对智能体而言，上下文工程直接关系到记忆是否连贯、规划是否可靠、多步任务能否保持一致；一条设计良好的上下文管线，往往比单纯更换更大模型更能显著提升效果。这也标志着提示工作正从“打磨一句话”走向“构建多层信息栈”。

These layers include:

> 常见的上下文分层包括：

* **System prompts:** Foundational instructions that define the AI's operational parameters (e.g., "You are a technical writer; your tone must be formal and precise").  
* **External data:**  
  * **Retrieved documents:** Information actively fetched from a knowledge base to inform responses (e.g., pulling technical specifications).  
  * **Tool outputs:** Results from the AI using an external API for real-time data (e.g., querying a calendar for availability).  
* **Implicit data:** Critical information such as user identity, interaction history, and environmental state. Incorporating implicit context presents challenges related to privacy and ethical data management. Therefore, robust governance is essential for context engineering, especially in sectors like enterprise, healthcare, and finance.

> * **系统提示：** 规定模型“默认工作方式”的底层指令（例：“你是技术文档作者，语气必须正式、可核查”）。
> * **外部数据：**
>   * **检索文档：** 从向量库、Wiki、工单系统等拉回的事实片段，用来压住幻觉。
>   * **工具输出：** 计算器、日历、CRM、天气 API 等实时回包，让回答跟现实世界同步。
> * **隐式数据：** 用户画像、权限、历史行为、设备状态等未明说却影响决策的信息。引入这类信号必须同步考虑隐私、同意与留存策略——在金融、医疗、政务场景尤其要有治理台账。

The core principle is that even advanced models underperform with a limited or poorly constructed view of their operational environment. This practice reframes the task from merely answering a question to building a comprehensive operational picture for the agent. For example, a context-engineered agent would integrate a user's calendar availability (tool output), the professional relationship with an email recipient (implicit data), and notes from previous meetings (retrieved documents) before responding to a query. This enables the model to generate highly relevant, personalized, and pragmatically useful outputs. The "engineering" aspect involves creating robust pipelines to fetch and transform this data at runtime and establishing feedback loops to continually improve context quality.

> 一句话概括：再强的模型，如果当前可见信息残缺或噪声过大，表现也会明显受限。上下文工程要做的，是把问题从“模型会不会回答”推进到“模型是否掌握了完成任务所需的完整现场信息”。例如，若在回复邮件前同时具备日历空档（工具输出）、与收件人的项目关系（隐式信息）以及上一轮会议纪要（检索文档），那么输出才更可能既得体又可执行。其工程化部分则包括可靠的数据抓取、清洗、裁剪，以及通过评测结果反哺下一轮上下文设计。

To implement this, specialized tuning systems, such as Google's Vertex AI prompt optimizer, can automate the improvement process at scale. By systematically evaluating responses against sample inputs and predefined metrics, these tools can enhance model performance and adapt prompts and system instructions across different models without extensive manual rewriting. Providing an optimizer with sample prompts, system instructions, and a template allows it to programmatically refine contextual inputs, offering a structured method for implementing the necessary feedback loops for sophisticated Context Engineering.  
This structured approach differentiates a rudimentary AI tool from a more sophisticated, contextually-aware system. It treats context as a primary component, emphasizing what the agent knows, when it knows it, and how it uses that information. This practice ensures the model has a well-rounded understanding of the user's intent, history, and current environment. Ultimately, Context Engineering is a crucial methodology for transforming stateless chatbots into highly capable, situationally-aware systems.

> 落地时，可以借助 Vertex AI Prompt Optimizer 这类平台，把“试提示”工业化：批量喂入样本输入，用你定义的指标自动打分，再迭代改写系统指令或提示模板，减少人肉 A/B。
> 这背后是一种产品哲学的分野——把上下文当成与模型平起平坐的一等公民，明确“何时注入何种信号、如何验证它仍然新鲜”。当意图、历史与环境状态被结构化地呈现给模型，聊天机器人才能从“会接话”进化成“懂现场”的智能体。

## Structured Output

> ## 结构化输出

Often, the goal of prompting is not just to get a free-form text response, but to extract or generate information in a specific, machine-readable format. Requesting structured output, such as JSON, XML, CSV, or Markdown tables, is a crucial structuring technique. By explicitly asking for the output in a particular format and potentially providing a schema or example of the desired structure, you guide the model to organize its response in a way that can be easily parsed and used by other parts of your agentic system or application. Returning JSON objects for data extraction is beneficial as it forces the model to create a structure and can limit hallucinations. Experimenting with output formats is recommended, especially for non-creative tasks like extracting or categorizing data.

> 在很多场景中，你需要的并非一段自由文本，而是可供下游程序直接处理的数据。若在提示中明确指定 JSON、XML、CSV、Markdown 表格等格式，并附上字段说明或样例，模型通常更容易按要求组织输出。对抽取、标注、填表等任务而言，JSON 尤其值得优先考虑，因为字段一旦固定，模型自由发挥的空间就会明显缩小。对于非创意类流程，也建议对不同输出载体进行比较，选择最稳定的方案。

* **Example:**  
  Extract the following information from the text below and return it as a JSON object with keys `name`, `address`, and `phone.number`.

  Text: "Contact John Smith at 123 Main St, Anytown, CA or call (555) 123-4567."

> * **示例：**
>   Extract the following information from the text below and return it as a JSON object with keys `name`, `address`, and `phone.number`.
>
>   Text: "Contact John Smith at 123 Main St, Anytown, CA or call (555) 123-4567."

Effectively utilizing system prompts, role assignments, contextual information, delimiters, and structured output significantly enhances the clarity, control, and utility of interactions with language models, providing a strong foundation for developing reliable agentic systems. Requesting structured output is crucial for creating pipelines where the language model's output serves as the input for subsequent system or processing steps.

> 把系统提示、角色设定、动态上下文、分隔符和结构化输出组合使用，交互就能从普通对话升级为可编排流程；其中结构化输出几乎是所有自动化流水线的硬性前提，缺少它，后续脚本便难以稳定接续。

**Leveraging Pydantic for an Object-Oriented Facade:** A powerful technique for enforcing structured output and enhancing interoperability is to use the LLM's generated data to populate instances of Pydantic objects. Pydantic is a Python library for data validation and settings management using Python type annotations. By defining a Pydantic model, you create a clear and enforceable schema for your desired data structure. This approach effectively provides an object-oriented facade to the prompt's output, transforming raw text or semi-structured data into validated, type-hinted Python objects.

> **用 Pydantic 做类型门面：** 让 LLM 生成 JSON 只是第一步，更稳妥的做法是将结果解析进 Pydantic 模型。Pydantic 使用 Python 类型注解描述字段含义与约束，并在解析时自动完成校验与类型转换，相当于在提示与业务逻辑之间增加了一层强类型校验。

You can directly parse a JSON string from an LLM into a Pydantic object using the `model.validate.json` method. This is particularly useful as it combines parsing and validation in a single step.

> 可直接调用 `model.validate.json`，将 LLM 返回的 JSON 一次性解析并校验为对象，从而减少手动 `json.loads` 与额外条件判断的样板代码。

```python
from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Optional
from datetime import date


# --- Pydantic Model Definition (from above) ---
class User(BaseModel):
    name: str = Field(..., description="The full name of the user.")
    email: EmailStr = Field(..., description="The user's email address.")
    date_of_birth: Optional[date] = Field(None, description="The user's date of birth.")
    interests: List[str] = Field(default_factory=list, description="A list of the user's interests.")


# --- Hypothetical LLM Output ---
llm_output_json = """
{
    "name": "Alice Wonderland",
    "email": "alice.w@example.com",
    "date_of_birth": "1995-07-21",
    "interests": [
        "Natural Language Processing",
        "Python Programming",
        "Gardening"
    ]
}
"""


# --- Parsing and Validation ---
try:
    # Use the model_validate_json class method to parse the JSON string.
    # This single step parses the JSON and validates the data against the User model.
    user_object = User.model_validate_json(llm_output_json)

    # Now you can work with a clean, type-safe Python object.
    print("Successfully created User object!")
    print(f"Name: {user_object.name}")
    print(f"Email: {user_object.email}")
    print(f"Date of Birth: {user_object.date_of_birth}")
    print(f"First Interest: {user_object.interests[0]}")

    # You can access the data like any other Python object attribute.
    # Pydantic has already converted the 'date_of_birth' string to a datetime.date object.
    print(f"Type of date_of_birth: {type(user_object.date_of_birth)}")
except ValidationError as e:
    # If the JSON is malformed or the data doesn't match the model's types,
    # Pydantic will raise a ValidationError.
    print("Failed to validate JSON from LLM.")
    print(e)
```

This Python code demonstrates how to use the Pydantic library to define a data model and validate JSON data. It defines a User model with fields for name, email, date of birth, and interests, including type hints and descriptions. The code then parses a hypothetical JSON output from a Large Language Model (LLM) using the `model.validate.json` method of the User model. This method handles both JSON parsing and data validation according to the model's structure and types. Finally, the code accesses the validated data from the resulting Python object and includes error handling for ValidationError in case the JSON is invalid.

> 这段示例展示完整闭环：先用 Pydantic 描述 User 结构，再将假想的 LLM JSON 传给 `model.validate.json` 做解析与校验；成功时可得到可通过属性访问的 Python 对象，若 JSON 损坏或字段不匹配，则进入 `ValidationError` 分支并打印原因。

For XML data, the xmltodict library can be used to convert the XML into a dictionary, which can then be passed to a Pydantic model for parsing. By using Field aliases in your Pydantic model, you can seamlessly map the often verbose or attribute-heavy structure of XML to your object's fields.

> 若上游是 XML，可先用 xmltodict 之类工具展平成字典，再映射到 Pydantic；借助 `Field(alias=...)` 能把层级很深或属性很多的标签，折叠成干净的 Python 属性名。

This methodology is invaluable for ensuring the interoperability of LLM-based components with other parts of a larger system. When an LLM's output is encapsulated within a Pydantic object, it can be reliably passed to other functions, APIs, or data processing pipelines with the assurance that the data conforms to the expected structure and types. This practice of "parse, don't validate" at the boundaries of your system components leads to more robust and maintainable applications.

> 一旦 LLM 输出被封装为经过校验的对象，后续函数、微服务或队列消费者就能按照明确契约处理数据，而不必在字符串中猜测字段含义。在系统边界上坚持“先解析，再进入业务逻辑”（parse, don't validate），通常能显著缩小故障面，并提升排障效率。

Effectively utilizing system prompts, role assignments, contextual information, delimiters, and structured output significantly enhances the clarity, control, and utility of interactions with language models, providing a strong foundation for developing reliable agentic systems. Requesting structured output is crucial for creating pipelines where the language model's output serves as the input for subsequent system or processing steps.

> 再强调一次：系统提示、角色设定、上下文、分隔符与结构化输出是一套需要协同运作的方法体系；其中结构化输出是将模型稳定嵌入自动化系统的关键环节，缺少这一点，后续步骤往往只能依赖人工兜底。

Structuring Prompts Beyond the basic techniques of providing examples, the way you structure your prompt plays a critical role in guiding the language model. Structuring involves using different sections or elements within the prompt to provide distinct types of information, such as instructions, context, or examples, in a clear and organized manner. This helps the model parse the prompt correctly and understand the specific role of each piece of text.

> （对应前文“Structuring Prompts”段）除了堆示例，提示本身的章节划分同样决定模型读不读得懂：用标签或空行把指令、背景、样例、用户输入隔开，让模型知道哪里是规则、哪里是素材。

# Reasoning and Thought Process Techniques

> # 推理与思维过程技术

Large language models excel at pattern recognition and text generation but often face challenges with tasks requiring complex, multi-step reasoning. This appendix focuses on techniques designed to enhance these reasoning capabilities by encouraging models to reveal their internal thought processes. Specifically, it addresses methods to improve logical deduction, mathematical computation, and planning.

> 大模型读模式、写文字都很强，一旦涉及多步推演就容易跳步或算错。本附录介绍的一系列方法，核心都是让模型把中间推理摊开给人看，从而稳住逻辑、算术与规划类任务。

## Chain of Thought (CoT)

> ## 思维链（Chain of Thought, CoT）

The Chain of Thought (CoT) prompting technique is a powerful method for improving the reasoning abilities of language models by explicitly prompting the model to generate intermediate reasoning steps before arriving at a final answer. Instead of just asking for the result, you instruct the model to "think step by step." This process mirrors how a human might break down a problem into smaller, more manageable parts and work through them sequentially.

> 思维链（CoT）的做法很直白：别只要答案，让模型先把推理过程写出来，再收尾。常用触发语是“Let's think step by step”，效果类似人类把难题拆成一串可检查的小步骤。

CoT helps the LLM generate more accurate answers, particularly for tasks that require some form of calculation or logical deduction, where models might otherwise struggle and produce incorrect results. By generating these intermediate steps, the model is more likely to stay on track and perform the necessary operations correctly.

> 对需要算数、推导或严谨逻辑的任务，CoT 往往显著降错：模型被迫把中间态写出来，就不那么容易一口蒙错。链条本身也便于你事后核对哪一步开始偏航。

There are two main variations of CoT:

> CoT 常见两条路线：

* **Zero-Shot CoT:** This involves simply adding the phrase "Let's think step by step" (or similar phrasing) to your prompt without providing any examples of the reasoning process. Surprisingly, for many tasks, this simple addition can significantly improve the model's performance by triggering its ability to expose its internal reasoning trace.  
  * **Example (Zero-Shot CoT):**  
    If a train travels at 60 miles per hour and covers a distance of 240 miles, how long did the journey take? Let's think step by step.

* **Few-Shot CoT:** This combines CoT with few-shot prompting. You provide the model with several examples where both the input, the step-by-step reasoning process, and the final output are shown. This gives the model a clearer template for how to perform the reasoning and structure its response, often leading to even better results on more complex tasks compared to zero-shot CoT.  
  * **Example (Few-Shot CoT):**  
    Q: The sum of three consecutive integers is 36. What are the integers?  
    A: Let the first integer be x. The next consecutive integer is x+1, and the third is x+2. The sum is x + (x+1) + (x+2) \= 3x + 3. We know the sum is 36, so 3x + 3 \= 36. Subtract 3 from both sides: 3x \= 33. Divide by 3: x \= 11. The integers are 11, 11+1=12, and 11+2=13. The integers are 11, 12, and 13.

    Q: Sarah has 5 apples, and she buys 8 more. She eats 3 apples. How many apples does she have left? Let's think step by step.  
    A: Let's think step by step. Sarah starts with 5 apples. She buys 8 more, so she adds 8 to her initial amount: 5 + 8 \= 13 apples. Then, she eats 3 apples, so we subtract 3 from the total: 13 - 3 \= 10. Sarah has 10 apples left. The answer is 10.

> * **零样本 CoT：** 只追加一句 “Let's think step by step”（或同义改写），不给例题；对不少任务，这一行字就能撬动模型把推理轨迹外化。
>   * **示例（零样本 CoT）：**
>     If a train travels at 60 miles per hour and covers a distance of 240 miles, how long did the journey take? Let's think step by step.
> * **少样本 CoT：** 把“例题里的推理过程也写全”，让模型照抄叙事节奏；步骤复杂时，往往比零样本 CoT 更稳。
>   * **示例（少样本 CoT）：**
>     Q: The sum of three consecutive integers is 36. What are the integers?
>     A: Let the first integer be x. The next consecutive integer is x+1, and the third is x+2. The sum is x + (x+1) + (x+2) \= 3x + 3. We know the sum is 36, so 3x + 3 \= 36. Subtract 3 from both sides: 3x \= 33. Divide by 3: x \= 11. The integers are 11, 11+1=12, and 11+2=13. The integers are 11, 12, and 13.
>
>     Q: Sarah has 5 apples, and she buys 8 more. She eats 3 apples. How many apples does she have left? Let's think step by step.
>     A: Let's think step by step. Sarah starts with 5 apples. She buys 8 more, so she adds 8 to her initial amount: 5 + 8 \= 13 apples. Then, she eats 3 apples, so we subtract 3 from the total: 13 - 3 \= 10. Sarah has 10 apples left. The answer is 10.

CoT offers several advantages. It is relatively low-effort to implement and can be highly effective with off-the-shelf LLMs without requiring fine-tuning. A significant benefit is the increased interpretability of the model's output; you can see the reasoning steps it followed, which helps in understanding why it arrived at a particular answer and in debugging if something went wrong. Additionally, CoT appears to improve the robustness of prompts across different versions of language models, meaning the performance is less likely to degrade when a model is updated. The main disadvantage is that generating the reasoning steps increases the length of the output, leading to higher token usage, which can increase costs and response time.

> CoT 的甜头在于上手快——不用训模型也能涨分；链条展开后，解释性与可调试性都更好，换模型版本时提示也通常更抗漂移。代价同样直观：输出变长，token、时延、账单一起涨。

Best practices for CoT include ensuring the final answer is presented *after* the reasoning steps, as the generation of the reasoning influences the subsequent token predictions for the answer. Also, for tasks with a single correct answer (like mathematical problems), setting the model's temperature to 0 (greedy decoding) is recommended when using CoT to ensure deterministic selection of the most probable next token at each step.

> 实操上记得两点：一是先把推理写透，再落最终答案——前面的 token 会一路约束后面的走向；二是遇到唯一正确答案（典型数学题），把 temperature 拉到 0 做贪心解码，让每一步都走概率最高的续写，减少随机胡闹。

## Self-Consistency

> ## 自洽性（Self-Consistency）

Building on the idea of Chain of Thought, the Self-Consistency technique aims to improve the reliability of reasoning by leveraging the probabilistic nature of language models. Instead of relying on a single greedy reasoning path (as in basic CoT), Self-Consistency generates multiple diverse reasoning paths for the same problem and then selects the most consistent answer among them.

> 自洽性（Self-Consistency）把 CoT 从“单路径”升级成“多路径投票”：同一提示多跑几次、拉高温度换思路，最后对答案做多数决，用统计对抗单次抽风的概率。

Self-Consistency involves three main steps:

> 典型流程分三步：

1. **Generating Diverse Reasoning Paths:** The same prompt (often a CoT prompt) is sent to the LLM multiple times. By using a higher temperature setting, the model is encouraged to explore different reasoning approaches and generate varied step-by-step explanations.  
2. **Extract the Answer:** The final answer is extracted from each of the generated reasoning paths.  
3. **Choose the Most Common Answer:** A majority vote is performed on the extracted answers. The answer that appears most frequently across the diverse reasoning paths is selected as the final, most consistent answer.

> 1. **生成多样推理路径：** 复用同一条（通常已含 CoT 的）提示，多次采样；温度略高，鼓励走出不同论证故事。
> 2. **抽取答案：** 从每条轨迹里抠出最终结论。
> 3. **选取最常见答案：** 对结论做投票，得票最高者当选——相当于用 ensemble 换稳健。

This approach improves the accuracy and coherence of responses, particularly for tasks where multiple valid reasoning paths might exist or where the model might be prone to errors in a single attempt. The benefit is a pseudo-probability likelihood of the answer being correct, increasing overall accuracy. However, the significant cost is the need to run the model multiple times for the same query, leading to much higher computation and expense.

> 它适合“可行思路不止一条”或“单次采样容易失误”的场景；同时还能提供一种近似置信度，票数分布可作为判断答案可靠性的参考。其缺点也很明显：同一问题需要运行 N 次，算力消耗与成本会线性增加。

* **Example (Conceptual):**  
  * *Prompt:* "Is the statement 'All birds can fly' true or false? Explain your reasoning."  
  * *Model Run 1 (High Temp):* Reasons about most birds flying, concludes True.  
  * *Model Run 2 (High Temp):* Reasons about penguins and ostriches, concludes False.  
  * *Model Run 3 (High Temp):* Reasons about birds *in general*, mentions exceptions briefly, concludes True.  
  * *Self-Consistency Result:* Based on majority vote (True appears twice), the final answer is "True". (Note: A more sophisticated approach would weigh the reasoning quality).

> * **示例（概念性）：**
>   * *Prompt:* "Is the statement 'All birds can fly' true or false? Explain your reasoning."
>   * *Model Run 1 (High Temp):* Reasons about most birds flying, concludes True.
>   * *Model Run 2 (High Temp):* Reasons about penguins and ostriches, concludes False.
>   * *Model Run 3 (High Temp):* Reasons about birds *in general*, mentions exceptions briefly, concludes True.
>   * *Self-Consistency Result:* Based on majority vote (True appears twice), the final answer is "True". (Note: A more sophisticated approach would weigh the reasoning quality).

## Step-Back Prompting

> ## 退一步提示（Step-Back Prompting）

Step-back prompting enhances reasoning by first asking the language model to consider a general principle or concept related to the task before addressing specific details. The response to this broader question is then used as context for solving the original problem.

> 退一步提示的核心在于“先抽象、后具体”：先询问与任务相关的一般原则或框架，再将这份高层回答嵌入真正要解决的问题中，作为后续推理的脚手架。

This process allows the language model to activate relevant background knowledge and wider reasoning strategies. By focusing on underlying principles or higher-level abstractions, the model can generate more accurate and insightful answers, less influenced by superficial elements. Initially considering general factors can provide a stronger basis for generating specific creative outputs. Step-back prompting encourages critical thinking and the application of knowledge, potentially mitigating biases by emphasizing general principles.

> 这样先把相关“课本知识”唤醒，再落笔细节，通常能减少被题干表面词带偏的情况；对写作、方案类任务，也能先立住结构再填肉。强调通则还有助于弱化一些刻板印象式的捷径回答——当然仍要配合安全审核。

* **Example:**  
  * *Prompt 1 (Step-Back):* "What are the key factors that make a good detective story?"  
  * *Model Response 1:* (Lists elements like red herrings, compelling motive, flawed protagonist, logical clues, satisfying resolution).  
  * *Prompt 2 (Original Task + Step-Back Context):* "Using the key factors of a good detective story [insert Model Response 1 here], write a short plot summary for a new mystery novel set in a small town."

> * **示例：**
>   * *Prompt 1 (Step-Back):* "What are the key factors that make a good detective story?"
>   * *Model Response 1:* (Lists elements like red herrings, compelling motive, flawed protagonist, logical clues, satisfying resolution).
>   * *Prompt 2 (Original Task + Step-Back Context):* "Using the key factors of a good detective story [insert Model Response 1 here], write a short plot summary for a new mystery novel set in a small town."

## Tree of Thoughts (ToT)

> ## 思维树（Tree of Thoughts, ToT）

Tree of Thoughts (ToT) is an advanced reasoning technique that extends the Chain of Thought method. It enables a language model to explore multiple reasoning paths concurrently, instead of following a single linear progression. This technique utilizes a tree structure, where each node represents a "thought"—a coherent language sequence acting as an intermediate step. From each node, the model can branch out, exploring alternative reasoning routes.

> 思维树（ToT）把 CoT 的直线叙事改成可分支搜索：每个节点是一段完整中间思考，从节点可以继续长出不同假设，像人在脑内试几条路线再择优。

ToT is particularly suited for complex problems that require exploration, backtracking, or the evaluation of multiple possibilities before arriving at a solution. While more computationally demanding and intricate to implement than the linear Chain of Thought method, ToT can achieve superior results on tasks necessitating deliberate and exploratory problem-solving. It allows an agent to consider diverse perspectives and potentially recover from initial errors by investigating alternative branches within the "thought tree."

> 它适合需要试错、回溯或显式比较多条路径的复杂问题；虽然算力成本与工程复杂度都高于线性 CoT，但在策划、谜题求解、组合优化等场景中往往回报可观。对智能体而言，它提供了在某条推理路径失效时切换分支的能力，而不必沿单一路径持续推进。

* **Example (Conceptual):** For a complex creative writing task like "Develop three different possible endings for a story based on these plot points," ToT would allow the model to explore distinct narrative branches from a key turning point, rather than just generating one linear continuation.

> * **示例（概念性）：** 像“给定情节点，写三种收束方式”这类任务，ToT 会在关键情节点同时展开多条故事枝，而不是一口气顺写到底。

These reasoning and thought process techniques are crucial for building agents capable of handling tasks that go beyond simple information retrieval or text generation. By prompting models to expose their reasoning, consider multiple perspectives, or step back to general principles, we can significantly enhance their ability to perform complex cognitive tasks within agentic systems.

> 这些技巧让智能体不止会“查资料 + 润色”，而是能承担真正的多步认知劳动：把推理摊开、多角度自检、必要时回到抽象层重新框定问题。

# Action and Interaction Techniques

> # 行动与交互技术

Intelligent agents possess the capability to actively engage with their environment, beyond generating text. This includes utilizing tools, executing external functions, and participating in iterative cycles of observation, reasoning, and action. This section examines prompting techniques designed to enable these active behaviors.

> 智能体不止“会说话”，还要能动手：查 API、跑函数、读传感器，并在观察 → 思考 → 行动之间循环。本节聚焦如何把这类行为写进提示里，让模型知道何时出手、如何出手。

## Tool Use / Function Calling

> ## 工具使用 / 函数调用

A crucial ability for an agent is using external tools or calling functions to perform actions beyond its internal capabilities. These actions may include web searches, database access, sending emails, performing calculations, or interacting with external APIs. Effective prompting for tool use involves designing prompts that instruct the model on the appropriate timing and methodology for tool utilization.

> 工具调用把模型从“纯文本生成”推进到“可执行工作流”：搜索、查库、发信、执行计算、发起 HTTP 请求等。提示中应写清触发条件、参数格式与失败时的回退策略，否则模型要么滥用工具，要么不敢调用。

Modern language models often undergo fine-tuning for "function calling" or "tool use." This enables them to interpret descriptions of available tools, including their purpose and parameters. Upon receiving a user request, the model can determine the necessity of tool use, identify the appropriate tool, and format the required arguments for its invocation. The model does not execute the tool directly. Instead, it generates a structured output, typically in JSON format, specifying the tool and its parameters. An agentic system then processes this output, executes the tool, and provides the tool's result back to the model, integrating it into the ongoing interaction.

> 新一代模型普遍经过工具调用对齐训练：读得懂 JSON Schema 式的工具说明书，也能在对话中决定“要不要用、用哪一个、传什么参”。真正执行动作的仍是宿主程序——模型只负责生成结构化的调用意图；运行环境执行后，再将 Observation 回传给模型，对话才能闭环。

* **Example:**  
  You have access to a weather tool that can get the current weather for a specified city. The tool is called '`get.current.weather`' and takes a '`city`' parameter (string).

  User: What's the weather like in London right now?

  * *Expected Model Output (Function Call):*  
    {  
      "tool.code": "get.current.weather",  
      "tool.name": "get.current.weather",  
      "parameters": {  
        "city": "London"  
      }  
    }

> * **示例：**
>   You have access to a weather tool that can get the current weather for a specified city. The tool is called '`get.current.weather`' and takes a '`city`' parameter (string).
>
>   User: What's the weather like in London right now?
>
>   * *Expected Model Output (Function Call):*
>     {
>       "tool.code": "get.current.weather",
>       "tool.name": "get.current.weather",
>       "parameters": {
>         "city": "London"
>       }
>     }

## ReAct (Reason & Act)

> ## ReAct（推理与行动）

ReAct, short for Reason and Act, is a prompting paradigm that combines Chain of Thought-style reasoning with the ability to perform actions using tools in an interleaved manner. ReAct mimics how humans operate – we reason verbally and take actions to gather more information or make progress towards a goal.

> ReAct 将“显式思维链式 CoT”与“调用工具获取新信息”编织在同一条轨迹中：模型先 Thought，再 Action，环境返回 Observation，循环直至给出 Final Answer——这一流程非常接近人类边思考边查证资料的习惯。

The ReAct pattern involves a loop:

> 标准循环长这样：

1. **Thought:** The model generates a thought process, explaining its current understanding and plan.  
2. **Action:** Based on the thought, the model decides to perform an action, often using a tool (e.g., Search, Calculator, API call). It outputs the name of the tool and the required input.  
3. **Observation:** The agentic system executes the tool and provides the result (Observation) back to the model.  
4. The loop continues with the model generating a new "Thought" based on the latest "Observation," leading to further "Actions" and "Observations" until the task is complete and the model outputs a "Final Answer."

> 1. **Thought：** 用自然语言交代现状、缺口与下一步打算。
> 2. **Action：** 点名要调的工具及参数（Search、Calculator、HTTP 等）。
> 3. **Observation：** 运行时真正执行工具，将原始结果回写到对话中。
> 4. 如此往复，直到模型判断信息足够，再输出 **Final Answer** 收束。

This interleaved process of thinking and acting allows the agent to dynamically gather information, react to tool outputs, and refine its approach, making it particularly effective for tasks requiring interaction with dynamic environments or external knowledge sources.

> 这种交错结构让智能体可以随着新事实不断修正计划，特别适合信息实时变化或必须查外部世界的任务。

* **Example (Illustrative ReAct Trace):**  
  User: What is the capital of France and its current population?

  Thought: The user is asking for two pieces of information: the capital of France and its population. I can use a search tool to find this information. I will start by confirming the capital, although I am likely to know it.  
  Action: Search({"query": "capital of France"})  
  Observation: Paris

  Thought: Okay, the capital is Paris. Now I need to find the population of Paris.  
  Action: Search({"query": "current population of Paris"})  
  Observation: The population of Paris was estimated to be around 2.1 million people in 2023.

  Thought: I have found both pieces of information. I can now provide the final answer to the user.  
  Final Answer: The capital of France is Paris, and its estimated population in 2023 was around 2.1 million people.

> * **示例（说明性 ReAct 轨迹）：**
>   User: What is the capital of France and its current population?
>
>   Thought: The user is asking for two pieces of information: the capital of France and its population. I can use a search tool to find this information. I will start by confirming the capital, although I am likely to know it.
>   Action: Search({"query": "capital of France"})
>   Observation: Paris
>
>   Thought: Okay, the capital is Paris. Now I need to find the population of Paris.
>   Action: Search({"query": "current population of Paris"})
>   Observation: The population of Paris was estimated to be around 2.1 million people in 2023.
>
>   Thought: I have found both pieces of information. I can now provide the final answer to the user.
>   Final Answer: The capital of France is Paris, and its estimated population in 2023 was around 2.1 million people.

These techniques are vital for building agents that can actively engage with the world, retrieve real-time information, and perform tasks that require interacting with external systems.

> 没有工具调用与 ReAct 式循环，智能体只能停留在“语言模拟”；有了它们，系统才真正接得上外部世界。

## Advanced Techniques

> ## 进阶技术

Beyond the foundational, structural, and reasoning patterns, there are several other prompting techniques that can further enhance the capabilities and efficiency of agentic systems. These range from using AI to optimize prompts to incorporating external knowledge and tailoring responses based on user characteristics.

> 在这些基础方法之外，还可以借助 AI 辅助生成提示、用检索补充知识，或根据受众画像调整语气风格；这些补充技巧往往决定系统能否从演示原型走向生产落地。

### Automatic Prompt Engineering (APE)

> ### 自动提示工程（APE）

Recognizing that crafting effective prompts can be a complex and iterative process, Automatic Prompt Engineering (APE) explores using language models themselves to generate, evaluate, and refine prompts. This method aims to automate the prompt writing process, potentially enhancing model performance without requiring extensive human effort in prompt design.

> 提示设计往往需要反复试验，而 APE 的思路是让另一个（或同一个）LLM 充当提示优化器：批量生成候选提示、自动评分并择优迭代，从而减少人工反复试错的负担。

The general idea is to have a "meta-model" or a process that takes a task description and generates multiple candidate prompts. These prompts are then evaluated based on the quality of the output they produce on a given set of inputs (perhaps using metrics like BLEU or ROUGE, or human evaluation). The best-performing prompts can be selected, potentially refined further, and used for the target task. Using an LLM to generate variations of a user query for training a chatbot is an example of this.

> 典型流水线：先描述任务 → 元模型生成 N 版提示 → 在固定评测集上跑分（自动指标或人工）→ 保留冠军并可继续变异。训练聊天机器人时让 LLM 改写用户问法，也属于同一思想。

* **Example (Conceptual):** A developer provides a description: "I need a prompt that can extract the date and sender from an email." An APE system generates several candidate prompts. These are tested on sample emails, and the prompt that consistently extracts the correct information is selected.

> * **示例（概念性）：** 需求描述可能是“帮我写个提示，稳定抽出邮件日期和发件人”。APE 批量生成若干版本，在真实邮件样本上跑一遍，留下表现最稳的那条。

Of course. Here is a rephrased and slightly expanded explanation of programmatic prompt optimization using frameworks like DSPy:

> 紧接着补一段关于 DSPy 式“程序化提示优化”的说明（在原文基础上略作展开）：

Another powerful prompt optimization technique, notably promoted by the DSPy framework, involves treating prompts not as static text but as programmatic modules that can be automatically optimized. This approach moves beyond manual trial-and-error and into a more systematic, data-driven methodology.

> DSPy 代表的另一条路，是把提示当成代码里的可学习参数：不是死文本，而是随数据与损失函数一起被搜索、被重写，让优化过程可复现、可版本化。

The core of this technique relies on two key components:

> 这一方法依赖两项核心组成：

1. **A Goldset (or High-Quality Dataset):** This is a representative set of high-quality input-and-output pairs. It serves as the "ground truth" that defines what a successful response looks like for a given task.  
2. **An Objective Function (or Scoring Metric):** This is a function that automatically evaluates the LLM's output against the corresponding "golden" output from the dataset. It returns a score indicating the quality, accuracy, or correctness of the response.

> 1. **金标集：** 一批高质量输入—输出对，告诉优化器“满分长什么样”。
> 2. **目标函数：** 自动把模型答案与金标比对，给出可优化的标量分数（准确率、F1、人工偏好均可）。

Using these components, an optimizer, such as a Bayesian optimizer, systematically refines the prompt. This process typically involves two main strategies, which can be used independently or in concert:

> 有了分数，就能交给贝叶斯优化、遗传算法或简单网格搜索去改提示。常见两条支线可以单飞也可以混用：

* **Few-Shot Example Optimization:** Instead of a developer manually selecting examples for a few-shot prompt, the optimizer programmatically samples different combinations of examples from the goldset. It then tests these combinations to identify the specific set of examples that most effectively guides the model toward generating the desired outputs.
* **Instructional Prompt Optimization:** In this approach, the optimizer automatically refines the prompt's core instructions. It uses an LLM as a "meta-model" to iteratively mutate and rephrase the prompt's text—adjusting the wording, tone, or structure—to discover which phrasing yields the highest scores from the objective function.

> * **少样本示例优化：** 不再靠肉眼挑例题，而是让程序在金标集里组合、重排、抽样不同示例子集，看哪一组最能拉高平均分。
> * **指令文本优化：** 让元模型像改稿编辑一样反复 mutate 系统提示——换词、换语气、换段落顺序——直到评分函数满意为止。

The ultimate goal for both strategies is to maximize the scores from the objective function, effectively "training" the prompt to produce results that are consistently closer to the high-quality goldset. By combining these two approaches, the system can simultaneously optimize *what instructions* to give the model and *which examples* to show it, leading to a highly effective and robust prompt that is machine-optimized for the specific task.

> 无论走哪条路，本质都是在最大化同一个目标函数——把提示当成可学习对象去“拟合金标”。两条线一起开，等于同时搜最佳措辞与最佳例题组合，往往比单修其一更狠。

### Iterative Prompting / Refinement

> ### 迭代提示 / 精炼

This technique involves starting with a simple, basic prompt and then iteratively refining it based on the model's initial responses. If the model's output isn't quite right, you analyze the shortcomings and modify the prompt to address them. This is less about an automated process (like APE) and more about a human-driven iterative design loop.

> 与 APE 的自动化相对，这里强调“人眼盯结果”：先写个能跑的朴素提示，看答案哪里软，再针对性补约束、补示例、补语境——经典人机共演。

* **Example:**  
  * *Attempt 1:* "Write a product description for a new type of coffee maker." (Result is too generic).  
  * *Attempt 2:* "Write a product description for a new type of coffee maker. Highlight its speed and ease of cleaning." (Result is better, but lacks detail).  
  * *Attempt 3:* "Write a product description for the 'SpeedClean Coffee Pro'. Emphasize its ability to brew a pot in under 2 minutes and its self-cleaning cycle. Target busy professionals." (Result is much closer to desired).

> * **示例：**
>   * *Attempt 1:* "Write a product description for a new type of coffee maker." (Result is too generic).
>   * *Attempt 2:* "Write a product description for a new type of coffee maker. Highlight its speed and ease of cleaning." (Result is better, but lacks detail).
>   * *Attempt 3:* "Write a product description for the 'SpeedClean Coffee Pro'. Emphasize its ability to brew a pot in under 2 minutes and its self-cleaning cycle. Target busy professionals." (Result is much closer to desired).

### Providing Negative Examples

> ### 提供反例

While the principle of "Instructions over Constraints" generally holds true, there are situations where providing negative examples can be helpful, albeit used carefully. A negative example shows the model an input and an *undesired* output, or an input and an output that *should not* be generated. This can help clarify boundaries or prevent specific types of incorrect responses.

> “多写希望得到什么”仍然是主要原则，但在特定场景下，展示*错误示范*也可能带来帮助：明确告诉模型“这种输出不可接受”，有助于压制某些特定失误模式。不过，反例不宜过多，否则提示又会退化为一长串否定式约束。

* **Example:**  
  Generate a list of popular tourist attractions in Paris. Do NOT include the Eiffel Tower.

  Example of what NOT to do:  
  Input: List popular landmarks in Paris.  
  Output: The Eiffel Tower, The Louvre, Notre Dame Cathedral.

> * **示例：**
>   Generate a list of popular tourist attractions in Paris. Do NOT include the Eiffel Tower.
>
>   Example of what NOT to do:
>   Input: List popular landmarks in Paris.
>   Output: The Eiffel Tower, The Louvre, Notre Dame Cathedral.

### Using Analogies

> ### 使用类比

Framing a task using an analogy can sometimes help the model understand the desired output or process by relating it to something familiar. This can be particularly useful for creative tasks or explaining complex roles.

> 把陌生任务映射成熟悉场景（厨师、教练、侦探……），模型更容易抓住语气、步骤与输出粒度；写故事、做教学设计时尤其好使。

* **Example:**  
  Act as a "data chef". Take the raw ingredients (data points) and prepare a "summary dish" (report) that highlights the key flavors (trends) for a business audience.

> * **示例：**
>   Act as a "data chef". Take the raw ingredients (data points) and prepare a "summary dish" (report) that highlights the key flavors (trends) for a business audience.

### Factored Cognition / Decomposition

> ### 因子化认知 / 分解

For very complex tasks, it can be effective to break down the overall goal into smaller, more manageable sub-tasks and prompt the model separately on each sub-task. The results from the sub-tasks are then combined to achieve the final outcome. This is related to prompt chaining and planning but emphasizes the deliberate decomposition of the problem.

> 面对巨型任务，先切成可独立验证的小块，每块单独提示，再拼装终稿——这和提示链、规划模式是亲戚，只是更强调“分解的颗粒度要可测试”。

* **Example:** To write a research paper:  
  * Prompt 1: "Generate a detailed outline for a paper on the impact of AI on the job market."  
  * Prompt 2: "Write the introduction section based on this outline: [insert outline intro]."  
  * Prompt 3: "Write the section on 'Impact on White-Collar Jobs' based on this outline: [insert outline section]." (Repeat for other sections).  
  * Prompt N: "Combine these sections and write a conclusion."

> * **示例：** 撰写研究论文时：
>   * Prompt 1: "Generate a detailed outline for a paper on the impact of AI on the job market."
>   * Prompt 2: "Write the introduction section based on this outline: [insert outline intro]."
>   * Prompt 3: "Write the section on 'Impact on White-Collar Jobs' based on this outline: [insert outline section]." (Repeat for other sections).
>   * Prompt N: "Combine these sections and write a conclusion."

### Retrieval Augmented Generation (RAG)

> ### 检索增强生成（RAG）

RAG is a powerful technique that enhances language models by giving them access to external, up-to-date, or domain-specific information during the prompting process. When a user asks a question, the system first retrieves relevant documents or data from a knowledge base (e.g., a database, a set of documents, the web). This retrieved information is then included in the prompt as context, allowing the language model to generate a response grounded in that external knowledge. This mitigates issues like hallucination and provides access to information the model wasn't trained on or that is very recent. This is a key pattern for agentic systems that need to work with dynamic or proprietary information.

> RAG 的公式很简单：问句先进检索器，拉回相关片段，再连同原文一起塞进提示。这样回答有“出处”，幻觉显著收敛，也能覆盖训练 cutoff 之后或公司内部才有的知识——是落地智能体系统的标配组件。

* **Example:**  
  * *User Query:* "What are the new features in the latest version of the Python library 'X'?"  
  * *System Action:* Search a documentation database for "Python library X latest features".  
  * *Prompt to LLM:* "Based on the following documentation snippets: [insert retrieved text], explain the new features in the latest version of Python library 'X'."

> * **示例：**
>   * *User Query:* "What are the new features in the latest version of the Python library 'X'?"
>   * *System Action:* Search a documentation database for "Python library X latest features".
>   * *Prompt to LLM:* "Based on the following documentation snippets: [insert retrieved text], explain the new features in the latest version of Python library 'X'."

### Persona Pattern (User Persona)

> ### 人格模式（用户人格）

While role prompting assigns a persona to the *model*, the Persona Pattern involves describing the user or the target audience for the model's output. This helps the model tailor its response in terms of language, complexity, tone, and the kind of information it provides.

> 角色提示回答“模型是谁”；人格模式回答“讲给谁听”。把受众年龄、背景、痛点写清楚，模型会自动调节术语密度、举例风格与信息深度。

* **Example:**  
  You are explaining quantum physics. The target audience is a high school student with no prior knowledge of the subject. Explain it simply and use analogies they might understand.

  Explain quantum physics: [Insert basic explanation request]

> * **示例：**
>   You are explaining quantum physics. The target audience is a high school student with no prior knowledge of the subject. Explain it simply and use analogies they might understand.
>
>   Explain quantum physics: [Insert basic explanation request]

These advanced and supplementary techniques provide further tools for prompt engineers to optimize model behavior, integrate external information, and tailor interactions for specific users and tasks within agentic workflows.

> 这些加分项让提示工程师能在工作流里同时调模型、调数据、调受众画像，把“能跑”打磨成“好用”。

## Using Google Gems

> ## 使用 Google Gems

Google's AI "Gems" (see Fig. 1) represent a user-configurable feature within its large language model architecture. Each "Gem" functions as a specialized instance of the core Gemini AI, tailored for specific, repeatable tasks. Users create a Gem by providing it with a set of explicit instructions, which establishes its operational parameters. This initial instruction set defines the Gem's designated purpose, response style, and knowledge domain. The underlying model is designed to consistently adhere to these pre-defined directives throughout a conversation.

> Google 生态里的 Gems（见图 1）相当于给 Gemini 套一层可保存的“快捷人设”：用户写好自己的系统指令，就得到一个面向固定场景的专用实例，后续对话都会自动继承那份用途、语气与知识边界设定。

This allows for the creation of highly specialized AI agents for focused applications. For example, a Gem can be configured to function as a code interpreter that only references specific programming libraries. Another could be instructed to analyze data sets, generating summaries without speculative commentary. A different Gem might serve as a translator adhering to a particular formal style guide. This process creates a persistent, task-specific context for the artificial intelligence.

> 你可以为不同工种各存一颗 Gem：只解释公司批准过的内部 SDK、只输出数据洞察而不瞎猜因果、或严格遵循某本翻译体例。本质是让用户级上下文变成可复用资产，而不是每次从零复述。

Consequently, the user avoids the need to re-establish the same contextual information with each new query. This methodology reduces conversational redundancy and improves the efficiency of task execution. The resulting interactions are more focused, yielding outputs that are consistently aligned with the user's initial requirements. This framework allows for applying fine-grained, persistent user direction to a generalist AI model. Ultimately, Gems enable a shift from general-purpose interaction to specialized, pre-defined AI functionalities.

> 好处是省掉每次重复的开场铺垫：开聊即专业模式，token 预算花在刀刃上，输出也更一致。它把“用户长期意图”焊进产品层，让通用大模型在体验上像一排垂直助理。

![Example of Google Gem Usage](../assets-new/Example_of_Google_Gem_Usage.png)

Fig.1: Example of Google Gem usage.

> 图 1：Google Gem 使用示例。

## Using LLMs to Refine Prompts (The Meta Approach)

> ## 用 LLM 精炼提示（元方法）

We've explored numerous techniques for crafting effective prompts, emphasizing clarity, structure, and providing context or examples. This process, however, can be iterative and sometimes challenging. What if we could leverage the very power of large language models, like Gemini, to help us *improve* our prompts? This is the essence of using LLMs for prompt refinement – a "meta" application where AI assists in optimizing the instructions given to AI.

> 前文介绍了大量技法，但真正落地时，最耗时的往往仍是反复改写提示。如果让 Gemini 这类模型读取旧提示、分析失败样例，再提出改写建议，会怎样？这正是提示精炼的“元用法”——用 AI 优化提供给 AI 的提示语句。

This capability is particularly "cool" because it represents a form of AI self-improvement or at least AI-assisted human improvement in interacting with AI. Instead of solely relying on human intuition and trial-and-error, we can tap into the LLM's understanding of language, patterns, and even common prompting pitfalls to get suggestions for making our prompts better. It turns the LLM into a collaborative partner in the prompt engineering process.

> 它既像“AI 教 AI”，也像给人类配了个懂套路的共笔：模型见过大量失败提示，往往能一眼指出含糊点、缺失约束或糟糕示例。

How does this work in practice? You can provide a language model with an existing prompt that you're trying to improve, along with the task you want it to accomplish and perhaps even examples of the output you're currently getting (and why it's not meeting your expectations). You then prompt the LLM to analyze the prompt and suggest improvements.

> 实操模板：旧提示 + 任务说明 + 好/坏输出对照 + 你认为的失败原因，然后请评审模型输出“问题清单 + 改写草案”。

A model like Gemini, with its strong reasoning and language generation capabilities, can analyze your existing prompt for potential areas of ambiguity, lack of specificity, or inefficient phrasing. It can suggest incorporating techniques we've discussed, such as adding delimiters, clarifying the desired output format, suggesting a more effective persona, or recommending the inclusion of few-shot examples.

> 强模型能具体告诉你：哪里一句话两读、哪里缺字段约定、哪里示例带毒，并主动提议加标签、加 JSON 样例、换角色或补少样本示例——基本就是把本附录目录又走了一遍。

The benefits of this meta-prompting approach include:

> 这么做的好处很实在：

* **Accelerated Iteration:** Get suggestions for improvement much faster than pure manual trial and error.  
* **Identification of Blind Spots:** An LLM might spot ambiguities or potential misinterpretations in your prompt that you overlooked.  
* **Learning Opportunity:** By seeing the types of suggestions the LLM makes, you can learn more about what makes prompts effective and improve your own prompt engineering skills.  
* **Scalability:** Potentially automate parts of the prompt optimization process, especially when dealing with a large number of prompts.

> * **加速迭代：** 一晚上能试三代提示，而不是三代日历日。
> * **发现盲区：** 自己读十遍也视而不见的歧义，模型可能第一句就点破。
> * **学习机会：** 把建议当案例库，慢慢形成肌肉记忆。
> * **可扩展性：** 有成百上千条提示时，可脚本化批量做提示评审。

It's important to note that the LLM's suggestions are not always perfect and should be evaluated and tested, just like any manually engineered prompt. However, it provides a powerful starting point and can significantly streamline the refinement process.

> 当然，评审模型也会瞎改——所有建议都要回归真实用例测一遍。把它当加速器，而不是自动真理机。

* **Example Prompt for Refinement:**  
  Analyze the following prompt for a language model and suggest ways to improve it to consistently extract the main topic and key entities (people, organizations, locations) from news articles. The current prompt sometimes misses entities or gets the main topic wrong.

  Existing Prompt:  
  "Summarize the main points and list important names and places from this article: [insert article text]"

  Suggestions for Improvement:

> * **用于精炼的示例提示：**
>   Analyze the following prompt for a language model and suggest ways to improve it to consistently extract the main topic and key entities (people, organizations, locations) from news articles. The current prompt sometimes misses entities or gets the main topic wrong.
>
>   Existing Prompt:
>   "Summarize the main points and list important names and places from this article: [insert article text]"
>
>   Suggestions for Improvement:

In this example, we're using the LLM to critique and enhance another prompt. This meta-level interaction demonstrates the flexibility and power of these models, allowing us to build more effective agentic systems by first optimizing the fundamental instructions they receive. It's a fascinating loop where AI helps us talk better to AI.

> 这个例子演示“模型 B 像做代码评审那样审模型 A 的提示”。把底层指令调顺，上层智能体自然更稳——算是套了一层自我对齐的幽默闭环。

## Prompting for Specific Tasks

> ## 面向特定任务的提示

While the techniques discussed so far are broadly applicable, some tasks benefit from specific prompting considerations. These are particularly relevant in the realm of code and multimodal inputs.

> 上面的套路大多通用，但写代码、喂图片/音频时还有额外坑位，需要专门留心。

### Code Prompting

> ### 代码提示

Language models, especially those trained on large code datasets, can be powerful assistants for developers. Prompting for code involves using LLMs to generate, explain, translate, or debug code. Various use cases exist:

> 接受过大量开源代码训练的模型，往往能够在 IDE 中充当高效的开发助手。面向代码的提示大体可分为四类：编写、解释、翻译与修复。

* **Prompts for writing code:** Asking the model to generate code snippets or functions based on a description of the desired functionality.  
  * **Example:** "Write a Python function that takes a list of numbers and returns the average."  
* **Prompts for explaining code:** Providing a code snippet and asking the model to explain what it does, line by line or in a summary.  
  * **Example:** "Explain the following JavaScript code snippet: [insert code]."  
* **Prompts for translating code:** Asking the model to translate code from one programming language to another.  
  * **Example:** "Translate the following Java code to C++: [insert code]."  
* **Prompts for debugging and reviewing code:** Providing code that has an error or could be improved and asking the model to identify issues, suggest fixes, or provide refactoring suggestions.  
  * **Example:** "The following Python code is giving a 'NameError'. What is wrong and how can I fix it? [insert code and traceback]."

> * **写代码：** 用自然语言描述 I/O 与边界，换可运行片段。
>   * **示例：** "Write a Python function that takes a list of numbers and returns the average."
> * **解释代码：** 贴片段，要求逐行或高层摘要。
>   * **示例：** "Explain the following JavaScript code snippet: [insert code]."
> * **翻译代码：** 指定源/目标语言与标准库差异。
>   * **示例：** "Translate the following Java code to C++: [insert code]."
> * **调试与审阅：** 附上报错栈、输入样例、期望行为，请模型定位与改写。
>   * **示例：** "The following Python code is giving a 'NameError'. What is wrong and how can I fix it? [insert code and traceback]."

Effective code prompting often requires providing sufficient context, specifying the desired language and version, and being clear about the functionality or issue.

> 想让代码一次到位，记得交代运行环境、依赖版本、风格约束（类型注解、测试框架），以及“错在哪、对长什么样”。

### Multimodal Prompting

> ### 多模态提示

While the focus of this appendix and much of current LLM interaction is text-based, the field is rapidly moving towards multimodal models that can process and generate information across different modalities (text, images, audio, video, etc.). Multimodal prompting involves using a combination of inputs to guide the model. This refers to using multiple input formats instead of just text.

> 虽然本附录仍以文本交互为主线，产业界已大规模部署图文音混合模型。多模态提示就是把这些不同通道的信号打包进同一条请求，让模型对齐跨模态信息。

* **Example:** Providing an image of a diagram and asking the model to explain the process shown in the diagram (Image Input + Text Prompt). Or providing an image and asking the model to generate a descriptive caption (Image Input + Text Prompt -> Text Output).

> * **示例：** 上传架构图请逐步解释（图 + 文）；或给产品照片生成电商标题（图 + 文 → 文）。

As multimodal capabilities become more sophisticated, prompting techniques will evolve to effectively leverage these combined inputs and outputs.

> 模态越多，提示越要像导演分镜：先告诉模型每张图/每段音频的角色，再下达合成任务。

## Best Practices and Experimentation

> ## 最佳实践与实验

Becoming a skilled prompt engineer is an iterative process that involves continuous learning and experimentation. Several valuable best practices are worth reiterating and emphasizing:

> 提示工程没有一劳永逸的终点，更像一项需要持续打磨的实践。下面这份对照清单值得长期参考：

* **Provide Examples:** Providing one or few-shot examples is one of the most effective ways to guide the model.  
* **Design with Simplicity:** Keep your prompts concise, clear, and easy to understand. Avoid unnecessary jargon or overly complex phrasing.  
* **Be Specific about the Output:** Clearly define the desired format, length, style, and content of the model's response.  
* **Use Instructions over Constraints:** Focus on telling the model what you want it to do rather than what you don't want it to do.  
* **Control the Max Token Length:** Use model configurations or explicit prompt instructions to manage the length of the generated output.  
* **Use Variables in Prompts:** For prompts used in applications, use variables to make them dynamic and reusable, avoiding hardcoding specific values.  
* **Experiment with Input Formats and Writing Styles:** Try different ways of phrasing your prompt (question, statement, instruction) and experiment with different tones or styles to see what yields the best results.  
* **For Few-Shot Prompting with Classification Tasks, Mix Up the Classes:** Randomize the order of examples from different categories to prevent overfitting.  
* **Adapt to Model Updates:** Language models are constantly being updated. Be prepared to test your existing prompts on new model versions and adjust them to leverage new capabilities or maintain performance.  
* **Experiment with Output Formats:** Especially for non-creative tasks, experiment with requesting structured output like JSON or XML.  
* **Experiment Together with Other Prompt Engineers:** Collaborating with others can provide different perspectives and lead to discovering more effective prompts.  
* **CoT Best Practices:** Remember specific practices for Chain of Thought, such as placing the answer after the reasoning and setting temperature to 0 for tasks with a single correct answer.  
* **Document the Various Prompt Attempts:** This is crucial for tracking what works, what doesn't, and why. Maintain a structured record of your prompts, configurations, and results.  
* **Save Prompts in Codebases:** When integrating prompts into applications, store them in separate, well-organized files for easier maintenance and version control.  
* **Rely on Automated Tests and Evaluation:** For production systems, implement automated tests and evaluation procedures to monitor prompt performance and ensure generalization to new data.

> * **提供示例：** few-shot 仍然是最便宜的性能杠杆。
> * **简洁设计：** 能一句话说清就别用从句套娃。
> * **明确输出：** 字数、列表层级、语气、引用格式都写死。
> * **指令优于约束：** 先写主成功路径，再补少数否定项。
> * **控制最大 token：** 结合 `max_tokens` 与提示内字数上限双保险。
> * **使用变量：** 模板化提示，别把客户名写死在 git 里。
> * **试验输入形式与文风：** 同一任务试试祈使句 vs 疑问句，分数可能差一截。
> * **分类少样本打乱类别：** 防模型背顺序。
> * **适配模型更新：** 新模型发布＝回归测试日。
> * **试验输出格式：** 结构化输出往往是工程化的分水岭。
> * **与他人协作实验：** 交叉评审能暴露集体盲区。
> * **CoT 实践：** 先链式推理再答案；客观题配合 temperature 0。
> * **记录尝试：** 若缺乏日志记录，提示调优过程便会沦为难以复盘的黑箱试错。
> * **在代码库中保存提示：** 和代码一起走代码评审。
> * **依赖自动化测试与评估：** 线上漂移最早体现在指标仪表盘。

Prompt engineering is a skill that improves with practice. By applying these principles and techniques, and by maintaining a systematic approach to experimentation and documentation, you can significantly enhance your ability to build effective agentic systems.

> 写得越多、测得越勤、记录得越细，你就越能把模型当成可靠组件，而不是不可预测的黑箱；这也正是迈向更高阶智能体开发的真正门槛。

## Conclusion

> ## 结语

This appendix provides a comprehensive overview of prompting, reframing it as a disciplined engineering practice rather than a simple act of asking questions. Its central purpose is to demonstrate how to transform general-purpose language models into specialized, reliable, and highly capable tools for specific tasks. The journey begins with non-negotiable core principles like clarity, conciseness, and iterative experimentation, which are the bedrock of effective communication with AI. These principles are critical because they reduce the inherent ambiguity in natural language, helping to steer the model's probabilistic outputs toward a single, correct intention. Building on this foundation, basic techniques such as zero-shot, one-shot, and few-shot prompting serve as the primary methods for demonstrating expected behavior through examples. These methods provide varying levels of contextual guidance, powerfully shaping the model's response style, tone, and format. Beyond just examples, structuring prompts with explicit roles, system-level instructions, and clear delimiters provides an essential architectural layer for fine-grained control over the model.

> 本附录把“写提示”升格成可度量的工程：目标不是聊得开心，而是把通用大模型锻造成面向具体任务、可依赖、可复现的工具链一环。一切从三条铁律出发——说清楚、写简短、肯迭代——它们直接决定自然语言这份模糊接口能否被收紧成可执行的意图。零样本、单样本、少样本则是示范期望行为的三档油门，用示例的密度换取对风格、语气、版式的控制力。再往上，系统指令、角色、分隔符共同构成提示的“软件架构”，没有这一层，就很难做细粒度治理。

The importance of these techniques becomes paramount in the context of building autonomous agents, where they provide the control and reliability necessary for complex, multi-step operations. For an agent to effectively create and execute a plan, it must leverage advanced reasoning patterns like Chain of Thought and Tree of Thoughts. These sophisticated methods compel the model to externalize its logical steps, systematically breaking down complex goals into a sequence of manageable sub-tasks. The operational reliability of the entire agentic system hinges on the predictability of each component's output. This is precisely why requesting structured data like JSON, and programmatically validating it with tools such as Pydantic, is not a mere convenience but an absolute necessity for robust automation. Without this discipline, the agent’s internal cognitive components cannot communicate reliably, leading to catastrophic failures within an automated workflow. Ultimately, these structuring and reasoning techniques are what successfully convert a model's probabilistic text generation into a deterministic and trustworthy cognitive engine for an agent.

> 一旦进入自主智能体场景，提示质量几乎就是系统可用性的晴雨表：多步计划、子任务委派、回滚策略，全都建立在每一步输出可预测的前提上。思维链、思维树等推理模板，本质是强迫模型把黑箱思考摊在阳光下，再把大目标切碎成可验证的小票。也正因为如此，JSON Schema + Pydantic 这类“硬接口”不再是锦上添花——没有结构化契约，工具节点之间就会靠猜字符串对齐，自动化流水线随时可能因为一次格式漂移而全线崩溃。换句话说，结构与推理技术负责把概率模型从“会说话”推进到“能当齿轮”。

Furthermore, these prompts are what grant an agent its crucial ability to perceive and act upon its environment, bridging the gap between digital thought and real-world interaction. Action-oriented frameworks like ReAct and native function calling are the vital mechanisms that serve as the agent's hands, allowing it to use tools, query APIs, and manipulate data. In parallel, techniques like Retrieval Augmented Generation (RAG) and the broader discipline of Context Engineering function as the agent's senses. They actively retrieve relevant, real-time information from external knowledge bases, ensuring the agent’s decisions are grounded in current, factual reality. This critical capability prevents the agent from operating in a vacuum, where it would be limited to its static and potentially outdated training data. Mastering this full spectrum of prompting is therefore the definitive skill that elevates a generalist language model from a simple text generator into a truly sophisticated agent, capable of performing complex tasks with autonomy, awareness, and intelligence.

> 最后，提示还是智能体与世界握手的协议：ReAct、函数调用让模型长出可以执行副作用的“手”；RAG、动态语境则提供持续刷新的“感官”，把决策拴在最新事实上，而不是困在训练截止日之前的静态记忆里。把上述全谱方法融会贯通，才算真正完成从“聊天模型”到“能自主推进任务的系统”的跃迁。

## References

Here is a list of resources for further reading and deeper exploration of prompt engineering techniques:

1. Prompt Engineering, [https://www.kaggle.com/whitepaper-prompt-engineering](https://www.kaggle.com/whitepaper-prompt-engineering)
2. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models, [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
3. Self-Consistency Improves Chain of Thought Reasoning in Language Models,  [https://arxiv.org/pdf/2203.11171](https://arxiv.org/pdf/2203.11171)
4. ReAct: Synergizing Reasoning and Acting in Language Models, [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)  
5. Tree of Thoughts: Deliberate Problem Solving with Large Language Models,  [https://arxiv.org/pdf/2305.10601](https://arxiv.org/pdf/2305.10601)
6. Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models, [https://arxiv.org/abs/2310.06117](https://arxiv.org/abs/2310.06117)
7. DSPy: Programming—not prompting—Foundation Models [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
