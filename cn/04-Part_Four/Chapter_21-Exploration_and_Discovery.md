# Chapter 21: Exploration and Discovery

> 第 21 章：探索与发现

This chapter explores patterns that enable intelligent agents to actively seek out novel information, uncover new possibilities, and identify unknown unknowns within their operational environment. Exploration and discovery differ from reactive behaviors or optimization within a predefined solution space. Instead, they focus on agents proactively venturing into unfamiliar territories, experimenting with new approaches, and generating new knowledge or understanding. This pattern is crucial for agents operating in open-ended, complex, or rapidly evolving domains where static knowledge or pre-programmed solutions are insufficient. It emphasizes the agent's capacity to expand its understanding and capabilities.

> 本章讨论一类模式：驱动智能体主动搜寻新信息、发掘新可能，并在运行环境中识别「未知的未知」。它不同于只在既定解空间中被动响应，或做局部优化。它的核心在于，智能体能够主动进入陌生领域、尝试新方法，并沉淀出新的知识与理解。在开放、复杂或快速演化的领域里，静态知识库与硬编码流程往往不足以支撑持续创新；此时，能否不断扩展认知边界，往往决定了智能体能力的上限。

## Practical Applications & Use Cases

> ## 实际应用场景与用例

AI agents possess the ability to intelligently prioritize and explore, which leads to applications across various domains. By autonomously evaluating and ordering potential actions, these agents can navigate complex environments, uncover hidden insights, and drive innovation. This capacity for prioritized exploration enables them to optimize processes, discover new knowledge, and generate content.

> 当代智能体已经能把「先探哪条路」与「怎么探」结合起来：先对候选行动做优先级评估，再按顺序深入复杂环境，挖掘隐藏关联并催化创新。带优先级的探索，让它们既能优化流程，也能产出新知识和新内容。

Examples:

> 典型示例如下：

* **Scientific Research Automation:** An agent designs and runs experiments, analyzes results, and formulates new hypotheses to discover novel materials, drug candidates, or scientific principles.  
* **Game Playing and Strategy Generation:** Agents explore game states, discovering emergent strategies or identifying vulnerabilities in game environments (e.g., AlphaGo).  
* **Market Research and Trend Spotting:** Agents scan unstructured data (social media, news, reports) to identify trends, consumer behaviors, or market opportunities.  
* **Security Vulnerability Discovery:** Agents probe systems or codebases to find security flaws or attack vectors.  
* **Creative Content Generation:** Agents explore combinations of styles, themes, or data to generate artistic pieces, musical compositions, or literary works.  
* **Personalized Education and Training:** AI tutors prioritize learning paths and content delivery based on a student's progress, learning style, and areas needing improvement.

> * **科研自动化：** 智能体可闭环完成「设计实验—采集数据—解读结果—提出新假设」的流程，用于新材料、候选药物或基础规律发现。
> * **博弈与策略生成：** 通过搜索博弈树或策略空间，捕捉非常规下法或环境漏洞（AlphaGo 即典型范例）。
> * **市场调研与趋势捕捉：** 聚合社交媒体、新闻与研报等非结构化信号，提炼趋势、客群行为与商业机会。
> * **安全漏洞发现：** 对系统与代码库做主动探测，定位缺陷与潜在攻击路径。
> * **创意内容生成：** 在风格、母题与素材之间组合试错，输出视觉、音乐或文本类作品。
> * **个性化教育：** 依据学习进度、认知偏好与薄弱点，对知识路径与内容投放动态排序。

Google Co-Scientist

> Google Co-Scientist（AI 协作科学家）

An AI co-scientist is an AI system developed by Google Research designed as a computational scientific collaborator. It assists human scientists in research aspects such as hypothesis generation, proposal refinement, and experimental design. This system operates on the Gemini LLM..

> AI co-scientist 由 Google Research 推出，定位是「计算科学协作体」：它被设计成真实科研流程中的辅助角色，主要支持假设提出、课题论证与实验设计；底层由 Gemini 系列大模型驱动。

The development of the AI co-scientist addresses challenges in scientific research. These include processing large volumes of information, generating testable hypotheses, and managing experimental planning. The AI co-scientist supports researchers by performing tasks that involve large-scale information processing and synthesis, potentially revealing relationships within data. Its purpose is to augment human cognitive processes by handling computationally demanding aspects of early-stage research.

> 它瞄准的正是科研中的典型痛点：文献爆炸、可验证假设难提、实验排期复杂等。系统擅长吞吐与综合海量信息，帮助研究者看见跨文献的潜在关联；把算力密集的探索阶段交给模型后，人类就可以把更多精力放在直觉、判断与方向选择上。

**System Architecture and Methodology:** The architecture of the AI co-scientist is based on a multi-agent framework, structured to emulate collaborative and iterative processes. This design integrates specialized AI agents, each with a specific role in contributing to a research objective. A supervisor agent manages and coordinates the activities of these individual agents within an asynchronous task execution framework that allows for flexible scaling of computational resources.

> **系统架构与方法：** 整体采用多智能体拓扑，在流程上模拟实验室中的分工协作。若干专科智能体围绕同一个科研问题各展所长；监督智能体则在异步调度层统一编排，并可按任务规模弹性扩容算力。

The core agents and their functions include (see Fig. 1):

> 核心智能体及其职责划分如下（见图 1）：

* **Generation agent**: Initiates the process by producing initial hypotheses through literature exploration and simulated scientific debates.  
* **Reflection agent**: Acts as a peer reviewer, critically assessing the correctness, novelty, and quality of the generated hypotheses.  
* **Ranking agent**: Employs an Elo-based tournament to compare, rank, and prioritize hypotheses through simulated scientific debates.  
* **Evolution agent**: Continuously refines top-ranked hypotheses by simplifying concepts, synthesizing ideas, and exploring unconventional reasoning.  
* **Proximity agent**: Computes a proximity graph to cluster similar ideas and assist in exploring the hypothesis landscape.  
* **Meta-review agent**: Synthesizes insights from all reviews and debates to identify common patterns and provide feedback, enabling the system to continuously improve.

> * **生成智能体（Generation agent）：** 结合文献检索与「虚拟学术辩论」抛出首批假设，拉开探索序幕。
> * **反思智能体（Reflection agent）：** 以审稿人视角审视假设的科学性、原创度与表述质量。
> * **排序智能体（Ranking agent）：** 借助 Elo 式对抗赛在多轮辩论中比较假设强弱并完成排序。
> * **演化智能体（Evolution agent）：** 对头部假设做概念压缩、思想融合与非常规推理，迭代升级版本。
> * **邻近智能体（Proximity agent）：** 构建相似度图，聚类相近想法，帮助研究者在高维假设空间里导航。
> * **元评审智能体（Meta-review agent）：** 汇总各轮评审与辩论，提炼共性模式与改进信号，驱动下一轮自我进化。

The system's operational foundation relies on Gemini, which provides language understanding, reasoning, and generative abilities. The system incorporates "test-time compute scaling," a mechanism that allocates increased computational resources to iteratively reason and enhance outputs. The system processes and synthesizes information from diverse sources, including academic literature, web-based data, and databases.

> 语言理解、链式推理与内容生成均由 Gemini 支撑；同时系统还引入「测试时算力扩展（test-time compute scaling）」机制，在需要多轮推敲答案时临时加大推理预算。知识侧则融合论文、开放网络和结构化数据库等多源证据。

![AI Co-Scientist: Ideation to Validation](../assets-new/AI_Co_Scientist_Ideation_to_Validation.png)

Fig. 1: (Courtesy of the Authors) AI Co-Scientist: Ideation to Validation

> 图 1：（作者供图）AI Co-Scientist：从创意到验证

The system follows an iterative "generate, debate, and evolve" approach mirroring the scientific method. Following the input of a scientific problem from a human scientist, the system engages in a self-improving cycle of hypothesis generation, evaluation, and refinement. Hypotheses undergo systematic assessment, including internal evaluations among agents and a tournament-based ranking mechanism.

> 工作流与经典科研节奏基本同构：「生成 → 辩论 → 演化」。科学家提出课题后，系统就会进入自我改进闭环：持续产出假设、互评打分，再进一步精炼；内部既有多智能体互审，也有锦标赛式排序充当质量闸门。

**Validation and Results:** The AI co-scientist's utility has been demonstrated in several validation studies, particularly in biomedicine, assessing its performance through automated benchmarks, expert reviews, and end-to-end wet-lab experiments.

> **验证与结果：** 论文与配套实验表明，该系统在生物医学等方向确有落地价值；评估手段覆盖自动基准、领域专家打分，以及完整的湿实验链路。

**Automated and Expert Evaluation:** On the challenging GPQA benchmark, the system's internal Elo rating was shown to be concordant with the accuracy of its results, achieving a top-1 accuracy of 78.4% on the difficult "diamond set". Analysis across over 200 research goals demonstrated that scaling test-time compute consistently improves the quality of hypotheses, as measured by the Elo rating. On a curated set of 15 challenging problems, the AI co-scientist outperformed other state-of-the-art AI models and the "best guess" solutions provided by human experts. In a small-scale evaluation, biomedical experts rated the co-scientist's outputs as more novel and impactful compared to other baseline models. The system's proposals for drug repurposing, formatted as NIH Specific Aims pages, were also judged to be of high quality by a panel of six expert oncologists.

> **自动化与专家评估：** 在 GPQA 的高难度子集上，内部 Elo 分数与真实准确率高度一致，「diamond set」的 top-1 达到 78.4%。对 200 多个研究目标的统计也显示，只要追加测试时算力，假设质量就会稳定提升，仍以 Elo 作为量化指标。在 15 道精选难题上，系统整体优于同期 SOTA 模型以及人类专家给出的「最佳猜测」。在小规模盲评中，生物医学同行认为其提案比基线模型更新颖、潜在影响力也更高；六名肿瘤专家也对 NIH Specific Aims 风格的药物重定位草案给出了高分。

**End-to-End Experimental Validation:**

> **端到端实验验证：**

Drug Repurposing: For acute myeloid leukemia (AML), the system proposed novel drug candidates. Some of these, like KIRA6, were completely novel suggestions with no prior preclinical evidence for use in AML. Subsequent in vitro experiments confirmed that KIRA6 and other suggested drugs inhibited tumor cell viability at clinically relevant concentrations in multiple AML cell lines.

> **药物重定位：** 面向急性髓系白血病（AML），模型给出了多条候选分子；像 KIRA6 这类建议，在公开 AML 临床前文献中几乎找不到先例。随后的体外实验显示，KIRA6 等同批推荐在临床相关浓度下，可显著抑制多种 AML 细胞系活力。

 Novel Target Discovery: The system identified novel epigenetic targets for liver fibrosis. Laboratory experiments using human hepatic organoids validated these findings, showing that drugs targeting the suggested epigenetic modifiers had significant anti-fibrotic activity. One of the identified drugs is already FDA-approved for another condition, opening an opportunity for repurposing.

> **新靶点发现：** 在肝纤维化场景下，系统指向一组新的表观遗传调控因子。人源肝类器官实验复现了预测：靶向这些因子的化合物展现明确抗纤维化效应，其中一款已是 FDA 批准的老药，为重定位提供捷径。

Antimicrobial Resistance: The AI co-scientist independently recapitulated unpublished experimental findings. It was tasked to explain why certain mobile genetic elements (cf-PICIs) are found across many bacterial species. In two days, the system's top-ranked hypothesis was that cf-PICIs interact with diverse phage tails to expand their host range. This mirrored the novel, experimentally validated discovery that an independent research group had reached after more than a decade of research.

> **抗菌耐药性：** 在一项独立任务中，系统在两天内给出的首选假设，与某团队尚未发表、但已用十余年才完成实验验证的结论一致：可移动遗传元件 cf-PICIs 可能通过结合多种噬菌体尾部蛋白来拓宽宿主谱。换言之，模型在没有任何内幕信息的情况下，「撞」上了真实世界的新知。

**Augmentation, and Limitations:** The design philosophy behind the AI co-scientist emphasizes augmentation rather than complete automation of human research. Researchers interact with and guide the system through natural language, providing feedback, contributing their own ideas, and directing the AI's exploratory processes in a "scientist-in-the-loop" collaborative paradigm. However, the system has some limitations. Its knowledge is constrained by its reliance on open-access literature, potentially missing critical prior work behind paywalls. It also has limited access to negative experimental results, which are rarely published but crucial for experienced scientists. Furthermore, the system inherits limitations from the underlying LLMs, including the potential for factual inaccuracies or "hallucinations".

> **增强与局限：** 它的产品哲学是 **人机共研**，而不是一键替代科学家。用户可以用自然语言输入洞见、纠偏方向，在 scientist-in-the-loop 框架里共同驾驭探索。局限也同样现实：训练语料以开放获取文献为主，付费墙背后的关键论文可能缺席；阴性结果本就稀缺，模型也更难学到「此路不通」的经验；此外，它仍然受制于 LLM 固有的幻觉与事实漂移问题。

**Safety:** Safety is a critical consideration, and the system incorporates multiple safeguards. All research goals are reviewed for safety upon input, and generated hypotheses are also checked to prevent the system from being used for unsafe or unethical research. A preliminary safety evaluation using 1,200 adversarial research goals found that the system could robustly reject dangerous inputs. To ensure responsible development, the system is being made available to more scientists through a Trusted Tester Program to gather real-world feedback.

> **安全：** 安全被嵌入默认路径。研究问题在入库前就会先做政策扫描，生成出的假设也要经过二次过滤，以避免系统被滥用于危险实验。对抗性测试集（约 1200 条恶意目标）显示，其拒绝策略整体上较为稳健。团队也在通过 Trusted Tester Program 逐步扩大试用范围，以收集真实滥用场景的反馈，继续迭代护栏。

## Hands-On Code Example

> ## 动手代码示例

Let's look at a concrete example of agentic AI for Exploration and Discovery in action: Agent Laboratory, a project developed by Samuel Schmidgall under the MIT License.

> 接下来用 **Agent Laboratory**（Samuel Schmidgall，MIT 许可）来看探索型智能体如何落地。

"Agent Laboratory" is an autonomous research workflow framework designed to augment human scientific endeavors rather than replace them. This system leverages specialized LLMs to automate various stages of the scientific research process, thereby enabling human researchers to dedicate more cognitive resources to conceptualization and critical analysis.

> Agent Laboratory 是一套自主科研工作流编排器。它的目标，是把机械环节交给专职 LLM，让人类把脑力留给问题建模与批判性反思，而不是简单替代研究员。

The framework integrates "AgentRxiv," a decentralized repository for autonomous research agents. AgentRxiv facilitates the deposition, retrieval, and development of research outputs

> 框架内置 **AgentRxiv**，这是一个面向自治科研智能体的去中心化知识库，支持论文级产物的发布、获取与协同迭代。

Agent Laboratory guides the research process through distinct phases:

> 典型流水线被拆成四个阶段：

1. **Literature Review:** During this initial phase, specialized LLM-driven agents are tasked with the autonomous collection and critical analysis of pertinent scholarly literature. This involves leveraging external databases such as arXiv to identify, synthesize, and categorize relevant research, effectively establishing a comprehensive knowledge base for the subsequent stages.  
2. **Experimentation:** This phase encompasses the collaborative formulation of experimental designs, data preparation, execution of experiments, and analysis of results. Agents utilize integrated tools like Python for code generation and execution, and Hugging Face for model access, to conduct automated experimentation. The system is designed for iterative refinement, where agents can adapt and optimize experimental procedures based on real-time outcomes.  
3. **Report Writing:** In the final phase, the system automates the generation of comprehensive research reports. This involves synthesizing findings from the experimentation phase with insights from the literature review, structuring the document according to academic conventions, and integrating external tools like LaTeX for professional formatting and figure generation.  
4. **Knowledge Sharing**: AgentRxiv is a platform enabling autonomous research agents to share, access, and collaboratively advance scientific discoveries. It allows agents to build upon previous findings, fostering cumulative research progress.

> 1. **文献综述：** 专科智能体自动抓取并批判性阅读相关论文，依托 arXiv 等索引构建可检索的知识基础。
> 2. **实验：** 多智能体协同撰写实验方案、清洗数据、执行实验并解读指标；Python 负责代码生成与执行，Hugging Face 提供模型侧能力，全程支持基于中间结果的滚动优化。
> 3. **报告撰写：** 将实验洞见与文献证据融合，按学术体例排版，并可挂接 LaTeX 生成正式稿件与插图。
> 4. **知识共享：** 通过 AgentRxiv 让不同智能体彼此复用并增量改进历史成果，形成开放式的累积创新。

The modular architecture of Agent Laboratory ensures computational flexibility. The aim is to enhance research productivity by automating tasks while maintaining the human researcher.

> 模块化拆分带来了算力和工具链层面的弹性。它的设计原则是「人类掌握方向，系统承担执行」：通过自动化提升吞吐，而不是削弱人类判断。

**Code analysis:** While a comprehensive code analysis is beyond the scope of this book, I want to provide you with some key insights and encourage you to delve into the code on your own.

> **代码分析：** 受篇幅所限，这里无法逐行拆解代码，只列出几个关键设计抓手；更细的实现细节，建议读者自行克隆仓库继续追踪。

**Judgment:** In order to emulate human evaluative processes, the system employs a tripartite agentic judgment mechanism for assessing outputs. This involves the deployment of three distinct autonomous agents, each configured to evaluate the production from a specific perspective, thereby collectively mimicking the nuanced and multi-faceted nature of human judgment. This approach allows for a more robust and comprehensive appraisal, moving beyond singular metrics to capture a richer qualitative assessment.

> **评判机制：** 为了逼近人类审稿体验，系统实现了 **三评审联评**：三名自治智能体分别强调实验扎实度、领域影响力与创意新颖度，多维打分后再汇总。相比单一的 scalar reward，这种做法更能捕获质性差异。

```python
class ReviewersAgent:
    def __init__(self, model="gpt-4o-mini", notes=None, openai_api_key=None):
        if notes is None:
            self.notes = []
        else:
            self.notes = notes
        self.model = model
        self.openai_api_key = openai_api_key

    def inference(self, plan, report):
        reviewer_1 = "You are a harsh but fair reviewer and expect good experiments that lead to insights for the research topic."
        review_1 = get_score(
            outlined_plan=plan,
            latex=report,
            reward_model_llm=self.model,
            reviewer_type=reviewer_1,
            openai_api_key=self.openai_api_key
        )

        reviewer_2 = "You are a harsh and critical but fair reviewer who is looking for an idea that would be impactful in the field."
        review_2 = get_score(
            outlined_plan=plan,
            latex=report,
            reward_model_llm=self.model,
            reviewer_type=reviewer_2,
            openai_api_key=self.openai_api_key
        )

        reviewer_3 = "You are a harsh but fair open-minded reviewer that is looking for novel ideas that have not been proposed before."
        review_3 = get_score(
            outlined_plan=plan,
            latex=report,
            reward_model_llm=self.model,
            reviewer_type=reviewer_3,
            openai_api_key=self.openai_api_key
        )

        return f"Reviewer #1:\n{review_1}, \nReviewer #2:\n{review_2}, \nReviewer #3:\n{review_3}"
```

The judgment agents are designed with a specific prompt that closely emulates the cognitive framework and evaluation criteria typically employed by human reviewers. This prompt guides the agents to analyze outputs through a lens similar to how a human expert would, considering factors like relevance, coherence, factual accuracy, and overall quality. By crafting these prompts to mirror human review protocols, the system aims to achieve a level of evaluative sophistication that approaches human-like discernment.

> 每位评审代理都绑定了定制化的 system prompt，显式模拟真实审稿人的关注清单，例如相关性、论证链条、事实核查与总体贡献等。通过把人类评审流程模板化，系统希望在自动评分中保留接近人工审稿的细粒度判断。

````python
def get_score(outlined_plan, latex, reward_model_llm, reviewer_type=None, attempts=3, openai_api_key=None):
   e = str()
   for _attempt in range(attempts):
       try:
          
           template_instructions = """
           Respond in the following format:

           THOUGHT:
           <THOUGHT>

           REVIEW JSON:
           ```json
           <JSON>
           ```

           In <THOUGHT>, first briefly discuss your intuitions 
           and reasoning for the evaluation.
           Detail your high-level arguments, necessary choices 
           and desired outcomes of the review.
           Do not make generic comments here, but be specific 
           to your current paper.
           Treat this as the note-taking phase of your review.

           In <JSON>, provide the review in JSON format with 
           the following fields in the order:
           - "Summary": A summary of the paper content and 
           its contributions.
           - "Strengths": A list of strengths of the paper.
           - "Weaknesses": A list of weaknesses of the paper.
           - "Originality": A rating from 1 to 4 
             (low, medium, high, very high).
           - "Quality": A rating from 1 to 4 
             (low, medium, high, very high).
           - "Clarity": A rating from 1 to 4 
             (low, medium, high, very high).
           - "Significance": A rating from 1 to 4 
             (low, medium, high, very high).
           - "Questions": A set of clarifying questions to be
              answered by the paper authors.
           - "Limitations": A set of limitations and potential
              negative societal impacts of the work.
           - "Ethical Concerns": A boolean value indicating 
              whether there are ethical concerns.
           - "Soundness": A rating from 1 to 4 
              (poor, fair, good, excellent).
           - "Presentation": A rating from 1 to 4 
              (poor, fair, good, excellent).
           - "Contribution": A rating from 1 to 4 
             (poor, fair, good, excellent).
           - "Overall": A rating from 1 to 10 
             (very strong reject to award quality).
           - "Confidence": A rating from 1 to 5 
             (low, medium, high, very high, absolute).
           - "Decision": A decision that has to be one of the
             following: Accept, Reject.

           For the "Decision" field, don't use Weak Accept,   
           Borderline Accept, Borderline Reject, or Strong Reject.  
           Instead, only use Accept or Reject.
           This JSON will be automatically parsed, so ensure 
           the format is precise.
           """
````

In this multi-agent system, the research process is structured around specialized roles, mirroring a typical academic hierarchy to streamline workflow and optimize output.

> 整个实验室模拟的是学院式组织结构：不同智能体分别对应导师、执行者与质检等职能，通过组织化分工提升流程可控性与产出稳定性。

**Professor Agent:** The Professor Agent functions as the primary research director, responsible for establishing the research agenda, defining research questions, and delegating tasks to other agents. This agent sets the strategic direction and ensures alignment with project objectives.

> **教授智能体（Professor Agent）：** 承担 PI 角色，负责立项、拆解研究问题，并把子任务下发给其他代理，对总体路线与里程碑负责。

````python
class ProfessorAgent(BaseAgent):
   def __init__(self, model="gpt4omini", notes=None, max_steps=100, openai_api_key=None):
       super().__init__(model, notes, max_steps, openai_api_key)
       self.phases = ["report writing"]

   def generate_readme(self):
       sys_prompt = f"""You are {self.role_description()} \n Here is the written paper \n{self.report}. Task instructions: Your goal is to integrate all of the knowledge, code, reports, and notes provided to you and generate a readme.md for a github repository."""
       history_str = "\n".join([_[1] for _ in self.history])
       prompt = (
           f"""History: {history_str}\n{'~' * 10}\n"""
           f"Please produce the readme below in markdown:\n")
       model_resp = query_model(model_str=self.model, system_prompt=sys_prompt, prompt=prompt, openai_api_key=self.openai_api_key)
       return model_resp.replace("```markdown", "")
````

**PostDoc Agent:** The PostDoc Agent's role is to execute the research. This includes conducting literature reviews, designing and implementing experiments, and generating research outputs such as papers. Importantly, the PostDoc Agent has the capability to write and execute code, enabling the practical implementation of experimental protocols and data analysis. This agent is the primary producer of research artifacts.

> **博士后智能体（PostDoc Agent）：** 一线执行者，覆盖综述、实验设计、跑数和写初稿；既能写代码也能跑代码，是仓库里大部分 artifact 的直接作者。

```python
class PostdocAgent(BaseAgent):
    def __init__(self, model="gpt4omini", notes=None, max_steps=100, openai_api_key=None):
        super().__init__(model, notes, max_steps, openai_api_key)
        self.phases = ["plan formulation", "results interpretation"]

    def context(self, phase):
        sr_str = str()
        if self.second_round:
            sr_str = (
                f"The following are results from the previous experiments\n",
                f"Previous Experiment code: {self.prev_results_code}\n"
                f"Previous Results: {self.prev_exp_results}\n"
                f"Previous Interpretation of results: {self.prev_interpretation}\n"
                f"Previous Report: {self.prev_report}\n"
                f"{self.reviewer_response}\n\n\n"
            )

        if phase == "plan formulation":
            return (
                sr_str,
                f"Current Literature Review: {self.lit_review_sum}",
            )
        elif phase == "results interpretation":
            return (
                sr_str,
                f"Current Literature Review: {self.lit_review_sum}\n"
                f"Current Plan: {self.plan}\n"
                f"Current Dataset code: {self.dataset_code}\n"
                f"Current Experiment code: {self.results_code}\n"
                f"Current Results: {self.exp_results}"
            )

        return ""
```

**Reviewer Agents:** Reviewer agents perform critical evaluations of research outputs from the PostDoc Agent, assessing the quality, validity, and scientific rigor of papers and experimental results. This evaluation phase emulates the peer-review process in academic settings to ensure a high standard of research output before finalization.

> **评审智能体（Reviewer Agents）：** 负责重点审查 PostDoc 提交的研究产出，从方法严谨性、结果可信度与叙事完整度等维度提出批评意见，相当于自动化的同行评议关口。

**ML Engineering Agents**:The Machine Learning Engineering Agents serve as machine learning engineers, engaging in dialogic collaboration with a PhD student to develop code. Their central function is to generate uncomplicated code for data preprocessing, integrating insights derived from the provided literature review and experimental protocol. This guarantees that the data is appropriately formatted and prepared for the designated experiment.

> **机器学习工程智能体（ML Engineering Agents）：** 与博士生角色结对，专注把数据清洗到「能喂模型」的状态；代码刻意保持短小可读，并显式吸收上游文献与实验计划里的约束。

```markdown
"You are a machine learning engineer being directed by a PhD student who will help you write the code, and you can interact with them through dialogue.\n"
"Your goal is to produce code that prepares the data for the provided experiment. You should aim for simple code to prepare the data, not complex code. You should integrate the provided literature review and the plan and come up with code to prepare data for this experiment.\n"
```

**SWEngineerAgents:** Software Engineering Agents guide Machine Learning Engineer Agents. Their main purpose is to assist the Machine Learning Engineer Agent in creating straightforward data preparation code for a specific experiment. The Software Engineer Agent integrates the provided literature review and experimental plan, ensuring the generated code is uncomplicated and directly relevant to the research objectives.

> **软件工程智能体（SWEngineerAgents）：** 作为 ML 工程师的 tech lead，把关数据管线实现是否贴合实验设计，避免过度工程化，同时确保需求来自真实文献与方案，而不是幻觉字段。

```markdown
"You are a software engineer directing a machine learning engineer, where the machine learning engineer will be writing the code, and you can interact with them through dialogue.\n"
"Your goal is to help the ML engineer produce code that prepares the data for the provided experiment. You should aim for very simple code to prepare the data, not complex code. You should integrate the provided literature review and the plan and come up with code to prepare data for this experiment.\n"
```

In summary, "Agent Laboratory" represents a sophisticated framework for autonomous scientific research. It is designed to augment human research capabilities by automating key research stages and facilitating collaborative AI-driven knowledge generation. The system aims to increase research efficiency by managing routine tasks while maintaining human oversight.

> 综上，Agent Laboratory 把「文献—实验—写作—共享」串成了一条可编排的流水线，通过多智能体协作提升算力利用率和流程编排效率；人类仍保有监督与纠偏权，而系统则承担大量重复性工作，用来提升整体迭代速度。

## At a Glance

> ## 要点速览

**What:** AI agents often operate within predefined knowledge, limiting their ability to tackle novel situations or open-ended problems. In complex and dynamic environments, this static, pre-programmed information is insufficient for true innovation or discovery. The fundamental challenge is to enable agents to move beyond simple optimization to actively seek out new information and identify "unknown unknowns." This necessitates a paradigm shift from purely reactive behaviors to proactive, Agentic exploration that expands the system's own understanding and capabilities.

> **是什么：** 许多智能体仍受限于预训练知识或人工整理出的知识边界，面对开放式问题时，往往只能停留在「复述已知答案」的层面。面对复杂世界，静态 playbook 很难支撑真正的创新。关键跃迁在于，从「在已知目标函数上微调」转向「主动扩展状态空间」，显式去寻找未知的未知。

**Why:** The standardized solution is to build Agentic AI systems specifically designed for autonomous exploration and discovery. These systems often utilize a multi-agent framework where specialized LLMs collaborate to emulate processes like the scientific method. For instance, distinct agents can be tasked with generating hypotheses, critically reviewing them, and evolving the most promising concepts. This structured, collaborative methodology allows the system to intelligently navigate vast information landscapes, design and execute experiments, and generate genuinely new knowledge. By automating the labor-intensive aspects of exploration, these systems augment human intellect and significantly accelerate the pace of discovery.

> **为什么：** 在工程实践中，这通常会落地为面向探索任务的多智能体体系：不同模型分别承担提出假设、交叉评审、筛选与演化等职能，整体对齐科学方法的闭环。只有这样，系统才能在庞大的文献与实验空间中实现智能导航，把人力从重复试错中解放出来，加速从问题提出到洞见形成的转化过程。

**Rule of Thumb:** Use the Exploration and Discovery pattern when operating in open-ended, complex, or rapidly evolving domains where the solution space is not fully defined. It is ideal for tasks requiring the generation of novel hypotheses, strategies, or insights, such as in scientific research, market analysis, and creative content generation. This pattern is essential when the objective is to uncover "unknown unknowns" rather than merely optimizing a known process.

> **经验法则：** 只要问题域开放、演化快，且解空间尚未被形式化，就应启用探索与发现模式。科研、市场洞察、创意生产等需要持续提出新假设或新策略的场景最为典型；如果 KPI 是「找到从未想过的风险或机会」，而不是把旧流程再抠出 1% 效率，这个模式几乎不可或缺。

**Visual Summary:**

> **图示摘要：**

![Exploration and Discovery Design Pattern](../assets-new/Exploration_and_Discovery_Design_Pattern.png)

Fig.2: Exploration and Discovery design pattern

> 图 2：探索与发现设计模式（示意）

## Key Takeaways

> ## 关键要点

* Exploration and Discovery in AI enable agents to actively pursue new information and possibilities, which is essential for navigating complex and evolving environments.  
* Systems such as Google Co-Scientist demonstrate how Agents can autonomously generate hypotheses and design experiments, supplementing human scientific research.  
* The multi-agent framework, exemplified by Agent Laboratory's specialized roles, improves research through the automation of literature review, experimentation, and report writing.  
* Ultimately, these Agents aim to enhance human creativity and problem-solving by managing computationally intensive tasks, thus accelerating innovation and discovery.

> * 探索与发现能力使智能体能够主动扩展信息边界，是应对复杂演化系统的重要保障。
> * Google Co-Scientist 证明，多智能体系统可以自治完成「假设提出—互评—实验设计」的链条，成为人类研究团队中的数字化协作成员。
> * Agent Laboratory 通过分角色流水线自动串联综述、实验与写作，展示了工程化科研助手的可行形态。
> * 将算力密集的搜索与验证任务交给智能体处理后，人类便能把注意力集中在问题定义与价值判断上，整体创新节奏也会随之加快。

## Conclusion

> ## 结论

In conclusion, the Exploration and Discovery pattern is the very essence of a truly agentic system, defining its ability to move beyond passive instruction-following to proactively explore its environment. This innate agentic drive is what empowers an AI to operate autonomously in complex domains, not merely executing tasks but independently setting sub-goals to uncover novel information. This advanced agentic behavior is most powerfully realized through multi-agent frameworks where each agent embodies a specific, proactive role in a larger collaborative process. For instance, the highly agentic system of Google's Co-scientist features agents that autonomously generate, debate, and evolve scientific hypotheses.

> 归根结底，探索与发现刻画了「智能体之所以成为智能体」的关键特征：它不仅执行指令，还会主动拆分子目标、持续搜索潜在线索。面对复杂课题，单一模型往往难以胜任；通常需要多个智能体各司其职、相互博弈，才能逐步逼近真实科研团队的创造力与探索深度。Google Co-Scientist 就是典型例证。

Frameworks like Agent Laboratory further structure this by creating an agentic hierarchy that mimics human research teams, enabling the system to self-manage the entire discovery lifecycle. The core of this pattern lies in orchestrating emergent agentic behaviors, allowing the system to pursue long-term, open-ended goals with minimal human intervention. This elevates the human-AI partnership, positioning the AI as a genuine agentic collaborator that handles the autonomous execution of exploratory tasks. By delegating this proactive discovery work to an agentic system, human intellect is significantly augmented, accelerating innovation. The development of such powerful agentic capabilities also necessitates a strong commitment to safety and ethical oversight. Ultimately, this pattern provides the blueprint for creating truly agentic AI, transforming computational tools into independent, goal-seeking partners in the pursuit of knowledge.

> Agent Laboratory 则进一步用「导师—执行—评审」式层级把流程产品化，让发现链路可以半自治运转。关键在于，它能够编排多代理的涌现行为，使系统即便在弱监督下，仍能追逐长期、开放的目标。人机关系也因此升级：AI 不再只是被动工具，而是能自己开题、试错、汇总的合作者。当然，能力越强，安全与伦理护栏就越要同步加厚；只有把探索关在可控边界内，才能把算力真正转化为可靠的新知生产引擎。

## References

1. Exploration-Exploitation Dilemma**:** A fundamental problem in reinforcement learning and decision-making under uncertainty. [https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitation_dilemma](https://en.wikipedia.org/wiki/Exploration%E2%80%93exploitation_dilemma)
2. Google Co-Scientist: [https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
3. Agent Laboratory: Using LLM Agents as Research Assistants [https://github.com/SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory)
4. AgentRxiv: Towards Collaborative Autonomous Research: [https://agentrxiv.github.io/](https://agentrxiv.github.io/)
