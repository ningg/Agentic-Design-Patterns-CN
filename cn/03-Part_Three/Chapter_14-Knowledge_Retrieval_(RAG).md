# Chapter 14: Knowledge Retrieval (RAG)

> 第 14 章：知识检索（RAG）

LLMs exhibit substantial capabilities in generating human-like text. However, their knowledge base is typically confined to the data on which they were trained, limiting their access to real-time information, specific company data, or highly specialized details. Knowledge Retrieval (RAG, or  Retrieval Augmented Generation), addresses this limitation. RAG enables LLMs to access and integrate external, current, and context-specific information, thereby enhancing the accuracy, relevance, and factual basis of their outputs.

> 大语言模型在生成自然语言方面表现出色，但它的知识边界通常受限于训练语料，难以及时获取最新信息、企业内部资料或高度专业化的细节。检索增强生成（RAG，Retrieval Augmented Generation）正是为弥补这一短板而提出的。它让 LLM 在作答前先检索外部、具备时效性且与当前语境相关的材料，再把回答建立在可核验的依据之上，从而提升准确性和相关性。

For AI agents, this is crucial as it allows them to ground their actions and responses in real-time, verifiable data beyond their static training. This capability enables them to perform complex tasks accurately, such as accessing the latest company policies to answer a specific question or checking current inventory before placing an order. By integrating external knowledge, RAG transforms agents from simple conversationalists into effective, data-driven tools capable of executing meaningful work.

> 对智能体来说，这一点尤为关键：它的行动和答复必须建立在可核验、可更新的数据之上，而不能只依赖模型参数中静态而模糊的记忆。这样，系统才能更稳健地完成复杂任务，例如依据最新制度回答员工问题，或在下单前核对实时库存。通过把外部知识接入系统，RAG 能让智能体从单纯「会对话」进一步变成真正「能执行任务」的数据驱动助手。

## Knowledge Retrieval (RAG) Pattern Overview

> ## 知识检索（RAG）模式概览

The Knowledge Retrieval (RAG) pattern significantly enhances the capabilities of LLMs by granting them access to external knowledge bases before generating a response. Instead of relying solely on their internal, pre-trained knowledge, RAG allows LLMs to "look up" information, much like a human might consult a book or search the internet. This process empowers LLMs to provide more accurate, up-to-date, and verifiable answers.

> 「知识检索（RAG）」的核心，是在模型生成回答前先访问外部知识库，从而显著扩展其能力边界。模型不再只能依赖预训练参数中的静态记忆，而是可以像人类查阅资料一样主动检索外部信息。因此，它给出的答案通常更贴近问题，也更具时效性，更便于核对来源。

When a user poses a question or gives a prompt to an AI system using RAG, the query isn't sent directly to the LLM. Instead, the system first scours a vast external knowledge base—a highly organized library of documents, databases, or web pages—for relevant information. This search is not a simple keyword match; it's a "semantic search" that understands the user's intent and the meaning behind their words. This initial search pulls out the most pertinent snippets or "chunks" of information. These extracted pieces are then "augmented," or added, to the original prompt, creating a richer, more informed query. Finally, this enhanced prompt is sent to the LLM. With this additional context, the LLM can generate a response that is not only fluent and natural but also factually grounded in the retrieved data.

> 当用户向带有 RAG 的系统提问时，请求并不会直接送入 LLM。系统会先在外部知识源中检索相关内容，例如文档库、业务数据库或网页索引。这里通常用的不是简单的关键词匹配，而是能够理解查询意图的语义检索。系统随后提取最相关的若干文本片段（chunk），把它们拼接回原始提示，完成上下文增强，再将增强后的提示交给模型。由于多了一层可引用的证据支撑，回答不仅自然流畅，也更不容易偏离事实。

The RAG framework provides several significant benefits. It allows LLMs to access up-to-date information, thereby overcoming the constraints of their static training data. This approach also reduces the risk of "hallucination"—the generation of false information—by grounding responses in verifiable data. Moreover, LLMs can utilize specialized knowledge found in internal company documents or wikis. A vital advantage of this process is the capability to offer "citations," which pinpoint the exact source of information, thereby enhancing the trustworthiness and verifiability of the AI's responses..

> RAG 的收益非常直接：模型可以利用训练截止日期之后产生的新事实；通过把回答建立在检索片段之上，能明显降低幻觉风险；同时还可以接入企业内部 wiki、制度库等私有知识源。另一个重要优势是「可引用」能力。段落级溯源让读者可以回到原始材料自行核验，从而同时提升可信度和可审计性。

To fully appreciate how RAG functions, it's essential to understand a few core concepts (see Fig.1):

> 若要理解 RAG 的工作机制，首先应把握以下几个核心组成部分（见图 1）：

![RAG Core Concept: Chunking, Embeddings, and Vector Database](../assets-new/RAG_Core_Concepts_Chunking_Embeddings_and_Vector_Database.png)

Fig.1: RAG Core Concepts: Chunking, Embeddings, and Vector Database

> 图 1：RAG 核心概念——分块、嵌入与向量数据库

### Embeddings

In the context of LLMs, embeddings are numerical representations of text, such as words, phrases, or entire documents. These representations are in the form of a vector, which is a list of numbers. The key idea is to capture the semantic meaning and the relationships between different pieces of text in a mathematical space. Words or phrases with similar meanings will have embeddings that are closer to each other in this vector space. For instance, imagine a simple 2D graph. The word "cat" might be represented by the coordinates (2, 3), while "kitten" would be very close at (2.1, 3.1). In contrast, the word "car" would have a distant coordinate like (8, 1), reflecting its different meaning. In reality, these embeddings are in a much higher-dimensional space with hundreds or even thousands of dimensions, allowing for a very nuanced understanding of language.

> 在 LLM 体系中，嵌入（embedding）是把词语、句子或整篇文本表示为一组数字，也就是向量。这样，机器就能在几何空间中度量语义距离：含义越接近的文本，其向量位置通常也越接近。教材中常用二维示意，例如「cat」可能位于 (2,3)，「kitten」则靠近 (2.1,3.1)，而「car」会落在更远的位置如 (8,1)。在真实系统中，嵌入通常处在数百甚至上千维的空间里，以容纳更细粒度的语义差异。

### Text Similarity

Text similarity refers to the measure of how alike two pieces of text are. This can be at a surface level, looking at the overlap of words (lexical similarity), or at a deeper, meaning-based level. In the context of RAG, text similarity is crucial for finding the most relevant information in the knowledge base that corresponds to a user's query. For instance, consider the sentences: "What is the capital of France?" and "Which city is the capital of France?". While the wording is different, they are asking the same question. A good text similarity model would recognize this and assign a high similarity score to these two sentences, even though they only share a few words. This is often calculated using the embeddings of the texts.

> 文本相似度衡量的是两段文本在多大程度上彼此接近。它既可以从词面重合度来理解，也可以从深层语义是否一致来判断。RAG 检索正依赖这一能力，在知识库中找出与用户问题最相关的片段。比如 *What is the capital of France?* 与 *Which city is the capital of France?* 虽然措辞不同，但表达的是同一个问题，优秀的相似度模型仍会给出较高评分。在工程实践中，这通常通过双方 embedding 的距离或相似度来计算。

### Semantic Similarity and Distance

Semantic similarity is a more advanced form of text similarity that focuses purely on the meaning and context of the text, rather than just the words used. It aims to understand if two pieces of text convey the same concept or idea. Semantic distance is the inverse of this; a high semantic similarity implies a low semantic distance, and vice versa. In RAG, semantic search relies on finding documents with the smallest semantic distance to the user's query. For instance, the phrases "a furry feline companion" and "a domestic cat" have no words in common besides "a". However, a model that understands semantic similarity would recognize that they refer to the same thing and would consider them to be highly similar. This is because their embeddings would be very close in the vector space, indicating a small semantic distance. This is the "smart search" that allows RAG to find relevant information even when the user's wording doesn't exactly match the text in the knowledge base.

> 语义相似度更进一步，关注的是「表达的是否是同一概念」，而不仅仅是「是否使用了相同词语」。语义距离则与之相反：相似度越高，距离越小。RAG 中的向量检索，本质上就是寻找与查询 embedding 距离最近的文档片段。例如 *a furry feline companion* 与 *a domestic cat* 几乎不共享关键词，但语义模型仍会把它们映射到相邻的向量位置。正是依赖这种「理解含义」的搜索方式，系统才能在用户换一种说法时，依旧召回知识库中真正相关的内容。



### Chunking of Documents

Chunking is the process of breaking down large documents into smaller, more manageable pieces, or "chunks." For a RAG system to work efficiently, it cannot feed entire large documents into the LLM. Instead, it processes these smaller chunks. The way documents are chunked is important for preserving the context and meaning of the information. For instance, instead of treating a 50-page user manual as a single block of text, a chunking strategy might break it down into sections, paragraphs, or even sentences. For instance, a section on "Troubleshooting" would be a separate chunk from the "Installation Guide." When a user asks a question about a specific problem, the RAG system can then retrieve the most relevant troubleshooting chunk, rather than the entire manual. This makes the retrieval process faster and the information provided to the LLM more focused and relevant to the user's immediate need. Once documents are chunked, the RAG system must employ a retrieval technique to find the most relevant pieces for a given query. The primary method is vector search, which uses embeddings and semantic distance to find chunks that are conceptually similar to the user's question. An older, but still valuable, technique is BM25, a keyword-based algorithm that ranks chunks based on term frequency without understanding semantic meaning. To get the best of both worlds, hybrid search approaches are often used, combining the keyword precision of BM25 with the contextual understanding of semantic search. This fusion allows for more robust and accurate retrieval, capturing both literal matches and conceptual relevance.

> 分块（chunking）是指把长文档切分成较小、可管理的片段后再入库。如果把整本 50 页的手册作为一个整体送入模型，不仅成本高，也容易引入大量无关噪声；而按章节、段落甚至句子切分后，「安装指南」与「故障排查」就可以分别组织。这样，用户查询具体故障时，系统只需召回排障相关片段，速度和准确性都会更好。完成分块后，检索的主路径通常是向量搜索：利用 embedding 找出语义上最接近用户问题的片段；BM25 这类基于词频排序的传统方法依然有价值，尤其适用于专有名词或型号等字面匹配场景。工程实践中常见「向量 + BM25」的混合检索，以兼顾字面精确匹配与语义泛化能力。

### Vector Databases

A vector database is a specialized type of database designed to store and query embeddings efficiently. After documents are chunked and converted into embeddings, these high-dimensional vectors are stored in a vector database. Traditional retrieval techniques, like keyword-based search, are excellent at finding documents containing exact words from a query but lack a deep understanding of language. They wouldn't recognize that "furry feline companion" means "cat." This is where vector databases excel. They are built specifically for semantic search. By storing text as numerical vectors, they can find results based on conceptual meaning, not just keyword overlap. When a user's query is also converted into a vector, the database uses highly optimized algorithms (like HNSW \- Hierarchical Navigable Small World) to rapidly search through millions of vectors and find the ones that are "closest" in meaning. This approach is far superior for RAG because it uncovers relevant context even if the user's phrasing is completely different from the source documents. In essence, while other techniques search for words, vector databases search for meaning. This technology is implemented in various forms, from managed databases like Pinecone and Weaviate to open-source solutions such as Chroma DB, Milvus, and Qdrant. Even existing databases can be augmented with vector search capabilities, as seen with Redis, Elasticsearch, and Postgres (using the pgvector extension). The core retrieval mechanisms are often powered by libraries like Meta AI's FAISS or Google Research's ScaNN, which are fundamental to the efficiency of these systems.

> 向量数据库是专门为存储 embedding 并执行近邻检索而设计的。关键词检索擅长基于词面匹配进行搜索，却难以理解 *furry feline companion* 实际上是在描述「cat」；向量检索则按照语义接近程度来寻找结果。用户查询被向量化之后，数据库可借助 HNSW 等索引结构，在数百万级向量中快速定位语义邻近项。因此，即便用户换一种表达方式，也仍有较高概率召回正确片段。简而言之，传统检索偏向「搜字」，向量检索更接近「搜义」。具体实现既包括 Pinecone、Weaviate 等托管服务，也包括 Milvus、Qdrant、Chroma 等开源方案，还可以通过为 Redis、Elasticsearch、Postgres（借助 pgvector）等系统增加向量能力来实现。其底层效率常依赖 FAISS、ScaNN 等库。

### RAG's Challenges

Despite its power, the RAG pattern is not without its challenges. A primary issue arises when the information needed to answer a query is not confined to a single chunk but is spread across multiple parts of a document or even several documents. In such cases, the retriever might fail to gather all the necessary context, leading to an incomplete or inaccurate answer. The system's effectiveness is also highly dependent on the quality of the chunking and retrieval process; if irrelevant chunks are retrieved, it can introduce noise and confuse the LLM. Furthermore, effectively synthesizing information from potentially contradictory sources remains a significant hurdle for these systems.  Besides that, another challenge is that RAG requires the entire knowledge base to be pre-processed and stored in specialized databases, such as vector or graph databases, which is a considerable undertaking. Consequently, this knowledge requires periodic reconciliation to remain up-to-date, a crucial task when dealing with evolving sources like company wikis. This entire process can have a noticeable impact on performance, increasing latency, operational costs, and the number of tokens used in the final prompt.

> RAG 虽然能力强大，但也面临不少挑战。回答所需证据往往分散在多个片段、多个文档之中；如果检索器只返回少量片段，模型就可能给出不完整的答案。系统效果也高度依赖分块策略和排序质量，一旦噪声片段过多，LLM 反而更容易被误导。面对多源信息相互冲突的情况，如何有效综合仍然是开放问题。在工程层面，知识库需要事先完成切分、向量化并写入专用存储，后续还要持续同步更新，尤其是在处理不断演进的 wiki 或动态文档时，否则知识很快就会过时。与此同时，整条链路也会带来额外的延迟、成本和 prompt token 消耗。

In summary,  the Retrieval-Augmented Generation (RAG) pattern represents a significant leap forward in making AI more knowledgeable and reliable. By seamlessly integrating an external knowledge retrieval step into the generation process, RAG addresses some of the core limitations of standalone LLMs. The foundational concepts of embeddings and semantic similarity, combined with retrieval techniques like keyword and hybrid search, allow the system to intelligently find relevant information, which is made manageable through strategic chunking. This entire retrieval process is powered by specialized vector databases designed to store and efficiently query millions of embeddings at scale. While challenges in retrieving fragmented or contradictory information persist, RAG empowers LLMs to produce answers that are not only contextually appropriate but also anchored in verifiable facts, fostering greater trust and utility in AI.  

> 总体而言，RAG 让模型从「只依赖训练集记忆」演进为「能够边检索边作答」的系统，是提升可靠性和可用性的重要一步。它通过在生成前插入检索环节，弥补了静态 LLM 的核心短板；embedding、语义相似度、关键词/混合检索以及合理的分块策略，共同决定了系统能否准确找到相关材料；向量数据库则负责在大规模场景下支撑高效近邻搜索。虽然碎片化证据和冲突信息仍是难题，但只要检索和引用环节设计得当，回答就能既贴合语境又便于核验，从而显著提升可信度。

### Graph RAG

GraphRAG is an advanced form of Retrieval-Augmented Generation that utilizes a knowledge graph instead of a simple vector database for information retrieval. It answers complex queries by navigating the explicit relationships (edges) between data entities (nodes) within this structured knowledge base. A key advantage is its ability to synthesize answers from information fragmented across multiple documents, a common failing of traditional RAG. By understanding these connections, GraphRAG provides more contextually accurate and nuanced responses.

> GraphRAG 将「图结构」引入检索管线。它不只计算向量近邻，还会沿着实体（节点）与关系（边）进行路径推理，因此尤其适合处理需要多跳推理的问题。传统 RAG 的一个弱点，在于难以把分散在多篇文档中的信息有效拼接起来；而图结构恰恰擅长把离散事实组织成关联网络，因此生成的回答通常更连贯，也更具上下文完整性。

Use cases include complex financial analysis, connecting companies to market events, and scientific research for discovering relationships between genes and diseases. The primary drawback, however, is the significant complexity, cost, and expertise required to build and maintain a high-quality knowledge graph. This setup is also less flexible and can introduce higher latency compared to simpler vector search systems. The system's effectiveness is entirely dependent on the quality and completeness of the underlying graph structure. Consequently, GraphRAG offers superior contextual reasoning for intricate questions but at a much higher implementation and maintenance cost. In summary, it excels where deep, interconnected insights are more critical than the speed and simplicity of standard RAG.

> 典型场景包括在金融领域把公司、事件与指标组织成关系网络，或在科研中挖掘基因、疾病与通路之间的关联。它的代价在于知识图谱的构建、对齐和增量更新成本都较高，也高度依赖领域专家；与纯向量方案相比，GraphRAG 的架构更重、链路更长，效果又几乎完全取决于图谱的质量和覆盖度。因此，它更适合处理多跳推理、强关系依赖的问题；如果需求只是快速完成段落级检索，标准 RAG 往往更具性价比。

### Agentic RAG

An evolution of this pattern, known as **Agentic RAG** (see Fig.2), introduces a reasoning and decision-making layer to significantly enhance the reliability of information extraction. Instead of just retrieving and augmenting, an "agent"—a specialized AI component—acts as a critical gatekeeper and refiner of knowledge. Rather than passively accepting the initially retrieved data, this agent actively interrogates its quality, relevance, and completeness, as illustrated by the following scenarios.

> **Agentic RAG**（图 2）是在标准 RAG 之上叠加一层具备推理能力的编排机制。它不再只是「检索 + 拼接 prompt」，而是让智能体承担结果质检与知识精炼的角色，主动评估首轮召回是否足够新、足够准、足够全。下面四个情景正体现了这一能力。

First, an agent excels at reflection and source validation. If a user asks, "What is our company's policy on remote work?" a standard RAG might pull up a 2020 blog post alongside the official 2025 policy document. The agent, however, would analyze the documents' metadata, recognize the 2025 policy as the most current and authoritative source, and discard the outdated blog post before sending the correct context to the LLM for a precise answer.

> 其一，是反思与信源排序。用户询问「我司的远程办公政策」时，朴素 RAG 可能同时召回 2020 年的旧博文和 2025 年的正式制度文件；而智能体则可以结合元数据、版本信息和发布渠道进行判断，优先保留现行且权威的文档，把过期内容排除在模型上下文之外。

![Agentic RAG Introduces Reasoning Agent](../assets-new/Agentic_RAG_Introduces_Reasoning_Agent.png)

Fig.2: Agentic RAG introduces a reasoning agent that actively evaluates, reconciles, and refines retrieved information to ensure a more accurate and trustworthy final response.

> 图 2：Agentic RAG 引入推理型智能体，对检索结果做评估、对齐与精炼，以提升最终答复的准确性与可信度。

Second, an agent is adept at reconciling knowledge conflicts. Imagine a financial analyst asks, "What was Project Alpha's Q1 budget?" The system retrieves two documents: an initial proposal stating a €50,000 budget and a finalized financial report listing it as €65,000. An Agentic RAG would identify this contradiction, prioritize the financial report as the more reliable source, and provide the LLM with the verified figure, ensuring the final answer is based on the most accurate data.

> 其二，是冲突消解。分析师询问「Alpha 项目 Q1 预算」时，若一份早期草案写的是 5 万欧元，而另一份定稿财报写的是 6.5 万欧元，智能体就应识别其中矛盾，并结合文档类型与时间戳判断哪一来源更可信。在明确证据优先级后，再交由模型进行总结。

Third, an agent can perform multi-step reasoning to synthesize complex answers. If a user asks, "How do our product's features and pricing compare to Competitor X's?" the agent would decompose this into separate sub-queries. It would initiate distinct searches for its own product's features, its pricing, Competitor X's features, and Competitor X's pricing. After gathering these individual pieces of information, the agent would synthesize them into a structured, comparative context before feeding it to the LLM, enabling a comprehensive response that a simple retrieval could not have produced.

> 其三，是多步拆解与综合。对于「我们相较于 X 竞品的功能与定价如何」这类对比型问题，系统可以把它拆分为四次检索（我方功能、我方定价、对方功能、对方定价），由智能体先把材料整理成对照式上下文，再交由模型输出结构化结论。这类覆盖范围往往超出了单次向量召回的能力边界。

Fourth, an agent can identify knowledge gaps and use external tools. Suppose a user asks, "What was the market's immediate reaction to our new product launched yesterday?" The agent searches the internal knowledge base, which is updated weekly, and finds no relevant information. Recognizing this gap, it can then activate a tool—such as a live web-search API—to find recent news articles and social media sentiment. The agent then uses this freshly gathered external information to provide an up-to-the-minute answer, overcoming the limitations of its static internal database.

> 其四，是知识缺口感知与工具扩展。面对「昨天新品上市后，市场的即时反馈如何」这类问题，如果内部知识库只按周同步，智能体就应意识到现有语料缺乏时效性，转而调用实时搜索或舆情 API 补充证据，再据此组织答案，而不是在证据不足时贸然生成。

### Challenges of Agentic RAG

While powerful, the agentic layer introduces its own set of challenges. The primary drawback is a significant increase in complexity and cost. Designing, implementing, and maintaining the agent's decision-making logic and tool integrations requires substantial engineering effort and adds to computational expenses. This complexity can also lead to increased latency, as the agent's cycles of reflection, tool use, and multi-step reasoning take more time than a standard, direct retrieval process. Furthermore, the agent itself can become a new source of error; a flawed reasoning process could cause it to get stuck in useless loops, misinterpret a task, or improperly discard relevant information, ultimately degrading the quality of the final response.

> 智能体层并非没有代价。决策逻辑、工具权限和失败重试机制都需要工程化实现，其算力消耗和响应延迟通常也显著高于「一次检索、一次生成」的简单流程。更重要的是，如果推理链设计不当，还可能引入新的故障模式，例如无效循环、误删相关片段或误解任务目标，反而损害最终答案质量。

### In Summary

Agentic RAG represents a sophisticated evolution of the standard retrieval pattern, transforming it from a passive data pipeline into an active, problem-solving framework. By embedding a reasoning layer that can evaluate sources, reconcile conflicts, decompose complex questions, and use external tools, agents dramatically improve the reliability and depth of the generated answers. This advancement makes the AI more trustworthy and capable, though it comes with important trade-offs in system complexity, latency, and cost that must be carefully managed.

> 小结：Agentic RAG 把传统流水线升级为能够规划、审视并补足信息缺口的主动系统。它借助推理层完成信源评估、冲突仲裁、子问题拆解和工具调用，从而换取更高的可靠性与分析深度；代价则是系统架构更重、响应时延更长、成本更高，因此需要有意识地加以治理。

## Practical Applications & Use Cases

> ## 实践应用与用例

Knowledge Retrieval (RAG) is changing how Large Language Models (LLMs) are utilized across various industries, enhancing their ability to provide more accurate and contextually relevant responses.

> RAG 正在改变各行业落地 LLM 的方式。它让回答更准确，也更贴近当前语境，而不再停留在泛化的预训练记忆复述上。

Applications include:

> 常见落点包括：

* **Enterprise Search and Q\&A:** Organizations can develop internal chatbots that respond to employee inquiries using internal documentation such as HR policies, technical manuals, and product specifications. The RAG system extracts relevant sections from these documents to inform the LLM's response.  
* **Customer Support and Helpdesks:** RAG-based systems can offer precise and consistent responses to customer queries by accessing information from product manuals, frequently asked questions (FAQs), and support tickets. This can reduce the need for direct human intervention for routine issues.  
* **Personalized Content Recommendation:** Instead of basic keyword matching, RAG can identify and retrieve content (articles, products) that is semantically related to a user's preferences or previous interactions, leading to more relevant recommendations.  
* **News and Current Events Summarization:** LLMs can be integrated with real-time news feeds. When prompted about a current event, the RAG system retrieves recent articles, allowing the LLM to produce an up-to-date summary.

> * **企业搜索 / 内部问答：** 将制度、手册、规格书等资料纳入知识库后，员工在咨询 HR、IT 或产品问题时即可先检索再作答，从而减少模型对内部规则的臆测。
> * **客服与工单：** 将手册、FAQ 与历史工单入库后，系统可基于证据对常见问题给出一致回答，从而降低一线重复劳动。
> * **个性化推荐：** 不再局限于关键词匹配，而是可根据用户兴趣的 embedding 检索语义相近的内容或商品。
> * **新闻与时事：** 接入实时信息流后，系统可先检索最新报道再进行摘要，从而避免模型停留在训练截止日期之前的知识状态。

By incorporating external knowledge, RAG extends the capabilities of LLMs beyond simple communication to function as knowledge processing systems.

> 接入外部知识后，LLM 不再只是一个聊天界面，而是可以承担可审计的知识加工与分发职责。

## Hands-On Code Example (ADK)

> ## 动手代码示例（ADK）

To illustrate the Knowledge Retrieval (RAG) pattern,  let's see three examples.

> 下面通过三个例子展示 RAG 从检索到生成的完整链路。

First, is how to use Google Search to do RAG and ground LLMs to search results. Since RAG involves accessing external information, the Google Search tool is a direct example of a built-in retrieval mechanism that can augment an LLM's knowledge.

> 第一个例子以 Google 搜索作为检索器，把模型输出建立在实时搜索结果之上。RAG 的本质就是「先获取外部证据，再进行生成」，而内置搜索工具正是这一思路最直观的实现方式之一。

```python
from google.adk.tools import google_search
from google.adk.agents import Agent


search_agent = Agent(
    name="research_assistant",
    model="gemini-2.0-flash-exp",
    instruction="You help users research topics. When asked, use the Google Search tool",
    tools=[google_search],
)
```

Second, this section explains how to utilize Vertex AI RAG capabilities within the Google ADK. The code provided demonstrates the initialization of VertexAiRagMemoryService from the ADK. This allows for establishing a connection to a Google Cloud Vertex AI RAG Corpus. The service is configured by specifying the corpus resource name and optional parameters such as `SIMILARITY_TOP_K` and `VECTOR_DISTANCE_THRESHOLD`. These parameters influence the retrieval process. `SIMILARITY_TOP_K` defines the number of top similar results to be retrieved. `VECTOR_DISTANCE_THRESHOLD` sets a limit on the semantic distance for the retrieved results. This setup enables agents to perform scalable and persistent semantic knowledge retrieval from the designated RAG Corpus. The process effectively integrates Google Cloud's RAG functionalities into an ADK agent, thereby supporting the development of responses grounded in factual data.

> 第二段演示如何在 ADK 中接入 Vertex AI RAG。`VertexAiRagMemoryService` 指向云端语料资源，`SIMILARITY_TOP_K` 用于控制召回条数，`VECTOR_DISTANCE_THRESHOLD` 用于过滤语义距离过远的片段。完成配置后，智能体就可以对托管语料执行持久化向量检索，把 GCP 侧的 RAG 能力嵌入 ADK 流水线，从而更容易生成具备证据支撑的回答。

```python
# Import the necessary VertexAiRagMemoryService class from the google.adk.memory module.
from google.adk.memory import VertexAiRagMemoryService


RAG_CORPUS_RESOURCE_NAME = "projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id"

# Define an optional parameter for the number of top similar results to retrieve.
# This controls how many relevant document chunks the RAG service will return.
SIMILARITY_TOP_K = 5

# Define an optional parameter for the vector distance threshold.
# This threshold determines the maximum semantic distance allowed for retrieved results;
# results with a distance greater than this value might be filtered out.
VECTOR_DISTANCE_THRESHOLD = 0.7

# Initialize an instance of VertexAiRagMemoryService.
# This sets up the connection to your Vertex AI RAG Corpus.
# - rag_corpus: Specifies the unique identifier for your RAG Corpus.
# - similarity_top_k: Sets the maximum number of similar results to fetch.
# - vector_distance_threshold: Defines the similarity threshold for filtering results.
memory_service = VertexAiRagMemoryService(
    rag_corpus=RAG_CORPUS_RESOURCE_NAME,
    similarity_top_k=SIMILARITY_TOP_K,
    vector_distance_threshold=VECTOR_DISTANCE_THRESHOLD,
)
```

## Hands-On Code Example (LangChain)

> ## 动手代码示例（LangChain）

Third, let's walk through a complete example using LangChain.

> 第三个例子展示如何借助 LangChain 与 LangGraph 跑通端到端 RAG 流程。

```python
import os
import requests
from typing import List, Dict, Any, TypedDict

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Weaviate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import StateGraph, END

import weaviate
from weaviate.embedded import EmbeddedOptions
import dotenv


# Load environment variables (e.g., OPENAI_API_KEY)
dotenv.load_dotenv()

# Set your OpenAI API key (ensure it's loaded from .env or set here)
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"


# --- 1. Data Preparation (Preprocessing) ---

# Load data
url = "https://github.com/langchain-ai/langchain/blob/master/docs/docs/how_to/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
    f.write(res.text)

loader = TextLoader("./state_of_the_union.txt")
documents = loader.load()

# Chunk documents
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Embed and store chunks in Weaviate
client = weaviate.Client(embedded_options=EmbeddedOptions())

vectorstore = Weaviate.from_documents(
    client=client,
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    by_text=False,
)

# Define the retriever
retriever = vectorstore.as_retriever()

# Initialize LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


# --- 2. Define the State for LangGraph ---
class RAGGraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str


# --- 3. Define the Nodes (Functions) ---
def retrieve_documents_node(state: RAGGraphState) -> RAGGraphState:
    """Retrieves documents based on the user's question."""
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question, "generation": ""}


def generate_response_node(state: RAGGraphState) -> RAGGraphState:
    """Generates a response using the LLM based on retrieved documents."""
    question = state["question"]
    documents = state["documents"]

    # Prompt template from the PDF
    template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer: """
    prompt = ChatPromptTemplate.from_template(template)

    # Format the context from the documents
    context = "\n\n".join([doc.page_content for doc in documents])

    # Create the RAG chain
    rag_chain = prompt | llm | StrOutputParser()

    # Invoke the chain
    generation = rag_chain.invoke({"context": context, "question": question})

    return {"question": question, "documents": documents, "generation": generation}


# --- 4. Build the LangGraph Graph ---
workflow = StateGraph(RAGGraphState)

# Add nodes
workflow.add_node("retrieve", retrieve_documents_node)
workflow.add_node("generate", generate_response_node)

# Set the entry point
workflow.set_entry_point("retrieve")

# Add edges (transitions)
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the graph
app = workflow.compile()


# --- 5. Run the RAG Application ---
if __name__ == "__main__":
    print("\n--- Running RAG Query ---")
    query = "What did the president say about Justice Breyer"
    inputs = {"question": query}
    for s in app.stream(inputs):
        print(s)

    print("\n--- Running another RAG Query ---")
    query_2 = "What did the president say about the economy?"
    inputs_2 = {"question": query_2}
    for s in app.stream(inputs_2):
        print(s)
```

This Python code illustrates a Retrieval-Augmented Generation (RAG) pipeline implemented with LangChain and LangGraph. The process begins with the creation of a knowledge base derived from a text document, which is segmented into chunks and transformed into embeddings. These embeddings are then stored in a Weaviate vector store, facilitating efficient information retrieval. A StateGraph in LangGraph is utilized to manage the workflow between two key functions: `retrieve_documents_node` and `generate_response_node`. The `retrieve_documents_node` function queries the vector store to identify relevant document chunks based on the user's input. Subsequently, the `generate_response_node` function utilizes the retrieved information and a predefined prompt template to produce a response using an OpenAI Large Language Model (LLM). The `app.stream` method allows the execution of queries through the RAG pipeline, demonstrating the system's capacity to generate contextually relevant outputs.

> 这段 Python 代码把 RAG 流程拆成「建库 → 检索 → 生成」三个阶段：先由 `CharacterTextSplitter` 进行切块，再通过 `OpenAIEmbeddings` 与 Weaviate 完成向量化和存储；随后使用 `StateGraph` 串联 `retrieve_documents_node`（根据问题检索向量近邻）与 `generate_response_node`（把上下文注入提示模板，再调用 ChatOpenAI 生成回答）。`app.stream` 便于观察多步状态流转，演示系统如何产出带有检索证据支撑的回答。

## At Glance

> ## 一览

**What:** LLMs possess impressive text generation abilities but are fundamentally limited by their training data. This knowledge is static, meaning it doesn't include real-time information or private, domain-specific data. Consequently, their responses can be outdated, inaccurate, or lack the specific context required for specialized tasks. This gap restricts their reliability for applications demanding current and factual answers.

> **是什么：** LLM 虽然具备很强的文本生成能力，但它的知识通常冻结在训练快照中：既不了解实时世界，也无法直接访问私有知识库。因此，回答容易过期、含糊，或缺少领域语境。在那些要求「信息最新且可核对」的场景里，这一限制会直接削弱系统可靠性。

**Why:** The Retrieval-Augmented Generation (RAG) pattern provides a standardized solution by connecting LLMs to external knowledge sources. When a query is received, the system first retrieves relevant information snippets from a specified knowledge base. These snippets are then appended to the original prompt, enriching it with timely and specific context. This augmented prompt is then sent to the LLM, enabling it to generate a response that is accurate, verifiable, and grounded in external data. This process effectively transforms the LLM from a closed-book reasoner into an open-book one, significantly enhancing its utility and trustworthiness.

> **为什么：** RAG 提供了一套清晰的方法论：先检索知识库，再把命中的片段拼接进 prompt，相当于让模型在「开卷」条件下作答。证据在场，回答自然更易核验，也更贴近业务事实，从而同步提升整体可信度和可用性。

**Rule of Thumb:** Use this pattern when you need an LLM to answer questions or generate content based on specific, up-to-date, or proprietary information that was not part of its original training data. It is ideal for building Q\&A systems over internal documents, customer support bots, and applications requiring verifiable, fact-based responses with citations.

> **经验法则：** 只要答案必须依赖训练数据之外的特定信息、实时信息或保密信息，就应考虑引入 RAG。内部文档问答、合规客服，以及需要引用出处或支持溯源的写作场景，都是典型应用。

**Visual Summary:**

> **图示摘要：**

![Knowledge Retrieval Pattern Database](../assets-new/Knowledge_Retrieval_Pattern_Database.png)

Knowledge Retrieval pattern: an AI agent to query and retrieve information from structured databases

> 知识检索模式：智能体向结构化库发起查询并取回记录

![Knowledge Retrieval Pattern Search](../assets-new/Knowledge_Retrieval_Pattern_Search.png)

Fig. 3: Knowledge Retrieval pattern: an AI agent to find and synthesize information from the public internet in response to user queries.

> 图 3：知识检索模式——智能体应用户问句从公网检索并综合信息

## Key Takeaways

> ## 要点

* Knowledge Retrieval (RAG) enhances LLMs by allowing them to access external, up-to-date, and specific information.  
* The process involves Retrieval (searching a knowledge base for relevant snippets) and Augmentation (adding these snippets to the LLM's prompt).  
* RAG helps LLMs overcome limitations like outdated training data, reduces "hallucinations," and enables domain-specific knowledge integration.  
* RAG allows for attributable answers, as the LLM's response is grounded in retrieved sources.  
* GraphRAG leverages a knowledge graph to understand the relationships between different pieces of information, allowing it to answer complex questions that require synthesizing data from multiple sources.  
* Agentic RAG moves beyond simple information retrieval by using an intelligent agent to actively reason about, validate, and refine external knowledge, ensuring a more accurate and reliable answer.  
* Practical applications span enterprise search, customer support, legal research, and personalized recommendations.

> * RAG 的核心，是先检索外部片段，再把片段送入提示，让模型「带着证据说话」。
> * 它能缓解训练截止日期带来的知识滞后、私域盲区，并降低胡编概率。
> * 片段级引用让答案更可追溯，也更便于审计。
> * GraphRAG 用图结构补足多跳推理和多文档综合的短板。
> * Agentic RAG 用智能体做质检、消歧、多步查询和工具补洞，以换取更高可靠性。
> * 企业搜索、客服、法务检索、个性化推荐等场景都已大量采用这类方案。

## Conclusion

> ## 结语

In conclusion, Retrieval-Augmented Generation (RAG) addresses the core limitation of a Large Language Model's static knowledge by connecting it to external, up-to-date data sources. The process works by first retrieving relevant information snippets and then augmenting the user's prompt, enabling the LLM to generate more accurate and contextually aware responses. This is made possible by foundational technologies like embeddings, semantic search, and vector databases, which find information based on meaning rather than just keywords. By grounding outputs in verifiable data, RAG significantly reduces factual errors and allows for the use of proprietary information, enhancing trust through citations.

> 总的来看，RAG 通过接入外部知识源，弥补了 LLM 静态记忆的短板。它先检索、后生成，让提示中携带明确证据；embedding、语义检索与向量数据库则共同负责按语义定位相关材料。当答案建立在可验证片段之上时，事实性错误与私域知识盲区都能得到缓解，而引用机制又进一步提升了系统的可信度。

An advanced evolution, Agentic RAG, introduces a reasoning layer that actively validates, reconciles, and synthesizes retrieved knowledge for even greater reliability. Similarly, specialized approaches like GraphRAG leverage knowledge graphs to navigate explicit data relationships, allowing the system to synthesize answers to highly complex, interconnected queries. This agent can resolve conflicting information, perform multi-step queries, and use external tools to find missing data. While these advanced methods add complexity and latency, they drastically improve the depth and trustworthiness of the final response. Practical applications for these patterns are already transforming industries, from enterprise search and customer support to personalized content delivery. Despite the challenges, RAG is a crucial pattern for making AI more knowledgeable, reliable, and useful. Ultimately, it transforms LLMs from closed-book conversationalists into powerful, open-book reasoning tools.

> Agentic RAG 进一步叠加推理层，专门处理信源冲突、任务拆解和工具补充数据；GraphRAG 则借助图谱中的显式关系应对多跳综合类问题。两者都需要更高的工程投入，也会带来更高时延，但换来的是回答深度与可信度的显著提升。如今，这些方法已广泛渗透到搜索、客服、内容分发等垂直场景。尽管挑战依然存在，RAG 体系仍是推动 LLM 从「封闭式对话」迈向「基于证据执行任务」的重要路径之一。

## References


1. Lewis, P., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)
2. Google AI for Developers Documentation.  *Retrieval Augmented Generation - [https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview)*
3. Retrieval-Augmented Generation with Graphs (GraphRAG), [https://arxiv.org/abs/2501.00309](https://arxiv.org/abs/2501.00309)
4. LangChain and LangGraph: Leonie Monigatti, "Retrieval-Augmented Generation (RAG): From Theory to LangChain Implementation,"  [*https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2*](https://medium.com/data-science/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2)
5. Google Cloud Vertex AI RAG Corpus [*https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus#corpus-management*](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus#corpus-management)
