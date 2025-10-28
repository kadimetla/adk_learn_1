from pydantic import BaseModel, Field
from google.adk.agents import LlmAgent
from google.genai import types 


class CountryInput(BaseModel):
    country_name: str = Field(
        ...,
        description="The name of the country to get information about.",
    )

class CountryOutput(BaseModel):
    capital: str = Field(description="The capital city of the country.")


country_info_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="country_info_agent",
    description="Provides information about a given country.",
    instruction="""
    You are an expert in world geography. When given the name of a country, you will
    provide the capital city of that country.
    """,
    input_schema=CountryInput,
    output_schema=CountryOutput,
    output_key="capital"
)

root_agent = country_info_agent