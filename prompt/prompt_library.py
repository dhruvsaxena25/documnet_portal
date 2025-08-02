# Prepare prompt template
from langchain_core.prompts import ChatPromptTemplate

## Documnet Analyzer
document_analysis_prompt = ChatPromptTemplate.from_template("""
You are a highly capable assistant trained to analyze and summarize documents.
Return ONLY valid JSON matching the exact schema below.

{format_instructions}

Analyze this document:
{document_text}
""")


## Document Compare
document_comparision_prompt= ChatPromptTemplate.from_template("""
                                                          
""")




PROMPT_REGISTRY = {"document_analysis": document_analysis_prompt,
                   "documnet_comparision": document_comparision_prompt}