# tasks.py

industry_research_prompt = (
    """Generate an industry-wise list detailing companies and their AI offerings, including core strategies.
    refer to reports and insights on AI and digital transformation from industry-specific sources such as McKinsey, Deloitte, or Nexocode. 
    Identify each company's industry (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare, Technology) 
    and summarize their primary AI products, solutions, or tools. Include strategic focus areas for each company, such as customer experience, 
    supply chain optimization, automation, or R&D. Where available, specify notable AI-driven projects, innovations, or research initiatives they're pursuing. 
    Additionally, capture any overarching vision or strategic goals 
    (e.g., sustainable AI in manufacturing, customer-centric innovation in retail, predictive analytics in healthcare) 
    that define the company's AI development focus."""
)

# industry_research_prompt = (
#     "refer to reports and insights on AI and digital transformation from industry-specific sources such as McKinsey, Deloitte, or Nexocode."
#     "Search for industry-specific use cases (e.g., “how is the retail industry leveraging AI and ML” or “AI applications in automotive manufacturing”)."
#     "Conduct a market analysis of the {} industry for the company {}. "
#     "Include insights on major industry segments, the company's main offerings, "
#     "and its strategic areas of focus, such as customer experience, supply chain, or innovation. "
#     "Additionally, highlight any industry trends or standards relevant to the company's operations."
# )

generate_use_cases_prompt = (
    #"Based on the following analysis: '{}', create use cases for AI and GenAI that could improve operations and customer experiences."
    """
    you are a gen ai bussiness use case generater, you need to generate the use case based on the analysis provided.
    Based on the following analysis: '{}'
    Analyze industry trends and standards within [industry] related to AI, machine learning (ML), and automation. 
    Identify emerging patterns in the use of generative AI (GenAI) and large language models (LLMs) to streamline operations, enhance customer experiences, 
    and boost efficiency. Based on these trends, propose specific use cases where [company name] could effectively 
    implement GenAI, LLMs, or other ML technologies to address challenges, improve processes, and achieve operational goals. Include examples such as:
    Process Improvement: Suggestions on automating repetitive tasks, optimizing workflows, or reducing errors.
    Customer Satisfaction: Ideas to enhance personalization, enable conversational AI, or provide predictive insights for customer needs.
    Operational Efficiency: Strategies for better resource management, predictive maintenance, supply chain optimization, or real-time data analysis.
    Where possible, provide industry benchmarks or standards that may serve as success metrics or guideposts for implementation.
    
    Example Output:
    1. Predictive Maintenance:
    Predictive maintenance uses machine learning (ML) and AI to anticipate equipment failures before they happen, minimizing downtime and maintenance costs. By analyzing real-time data from sensors on equipment, such as temperature, vibration, and pressure, predictive maintenance systems can identify patterns that precede mechanical issues. For Volkswagen, leveraging generative AI (GenAI) can help improve the accuracy of these predictions by generating realistic simulations and filling in gaps in maintenance data. This allows for proactive maintenance, where repairs are scheduled at the most opportune times, reducing unexpected breakdowns, improving efficiency, and extending the life of critical assets.

    2. Supply Chain Optimization:
    Supply chain optimization uses AI and ML to streamline operations, enhance forecasting, and increase responsiveness to disruptions. With large language models (LLMs), Volkswagen could analyze historical data, market trends, and real-time updates to identify patterns that indicate supply chain disruptions, such as delays, demand surges, or resource shortages. LLMs can help make sense of unstructured data from reports, emails, and external news, giving Volkswagen a comprehensive view of its supply chain. This enables smarter inventory management, cost reductions, and improved supplier coordination, helping the company meet demand efficiently and mitigate risks associated with global supply fluctuations.
    """
)

collect_resources_prompt = (
    #"Using the following AI and GenAI use cases: '{}', search for relevant datasets, code repositories, "
    """You are an expert generative AI use case resource locator, tasked with locating valid, 
    accessible resources for a list of provided AI and GenAI use cases. For each use case, 
    gather working links to relevant datasets on platforms such as Kaggle, Hugging Face, and GitHub. 
    Ensure that each dataset is available across all these platforms wherever possible.
    Instructions
    Identify Relevant Datasets:
    Search for datasets that closely align with each specified use case.
    Examples of relevant datasets include:
    Customer interaction data for personalization.
    Supply chain data for operational optimization.
    Maintenance records for predictive analysis.
    Additional use cases that may be specified.
    Organize Results:
    Create a structured document (such as a text file or Markdown file) with organized dataset links.
    Use headers for each use case, followed by dataset links and brief descriptions.
    Dataset Descriptions:
    For each dataset, include:
    Data Source: Identify whether the data is from Kaggle, Hugging Face, GitHub, or other specified sources.
    Usage Notes: Describe any important usage details (e.g., licensing, required preprocessing, limitations).
    Validation:
    Confirm that all links are accessible and directly support the use cases.
    Ensure that each dataset link is valid and relevant to its respective use case, and include examples from all specified platforms wherever possible.
    """
)

# genai_recommendations_prompt = (
#     "Given the company {} in the {} industry, what GenAI solutions can enhance operations and customer experiences?"
# )


    


# Example Output:
#     Use Case 1:
#     Title : Predictive Maintenance
#     Description : Implementing predictive maintenance using GenAI, LLMs, or other ML technologies to anticipate equipment failures before they happen, minimizing downtime and maintenance costs.
#     Resources:
#     - https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020

#     Use Case 2:
#     Title : Supply Chain Optimization
#     Description : Utilizing LLMs to analyze historical data, market trends, and real-time updates to identify patterns that indicate supply chain disruptions, such as delays, demand surges, or resource shortages.
#     Resources:
#     - https://www.kaggle.com/datasets/suraj9727/supply-chain-optimization-for-a-fmcg-company