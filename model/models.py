from pydantic import BaseModel, Field, RootModel
from typing import Optional, List, Dict, Any, Union

## Document Analysis
class Metadata(BaseModel):
    Summary: List[str] = Field(default_factory=list, description="Summary of the document")
    Title: str
    Author: str
    DateCreated: str   
    LastModifiedDate: str
    Publisher: str
    Language: str
    PageCount: Union[int, str]  # Can be "Not Available"
    SentimentTone: str
    
## Document Compare

class ChangeFormat(BaseModel):
    Page: str
    Changes: str
    

class SummaryResponse(RootModel[list[ChangeFormat]]):
    pass