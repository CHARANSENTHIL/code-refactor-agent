from pydantic import BaseModel
from typing import List

class RefactorOutput(BaseModel):
    code_smells: List[str]
    improvements: List[str]
    refactored_code: str
    explanation: str
