# main.py

import os
from datetime import datetime
from agents import research_agent ,use_case_agent, resource_collection_agent
from tasks import (
    industry_research_prompt
    ,generate_use_cases_prompt ,collect_resources_prompt
)

# Step 1: Conduct industry and company research
company_name = "Tesla"
industry = "Automotive"

industry_analysis = research_agent.run(industry_research_prompt)
print("Industry and Company Research:\n", industry_analysis)

# Step 2: Generate AI/ML and GenAI use cases
use_case_prompt = generate_use_cases_prompt.format(industry_analysis)
use_cases = use_case_agent.run(use_case_prompt)
print("\nGenerated Use Cases:\n", use_cases)

# # Step 3: Collect relevant resource assets
resource_collection_prompt = collect_resources_prompt.format(use_cases)
resources = resource_collection_agent.run(resource_collection_prompt)
print("\nResources:\n", resources)

# Save resources to markdown
filename = "final_output_"+str(datetime.now())+".md" 
#os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as file:
    file.write(resources)

print(f"Resource links saved to {filename}")
