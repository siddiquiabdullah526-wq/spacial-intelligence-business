"""Minimal scaffold: SI result dict -> Claude -> structured business narrative.

Any track (SI-1/2/3) calls interpret(result_dict) and gets back a dict with
the five report fields (question, key_finding, map_visual,
business_recommendation, confidence_note).
"""
import json
import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

SYSTEM = (
    "You are a location-analytics consultant. You receive summarized results "
    "from a spatial analysis and write a clear recommendation for a business "
    "decision-maker. Use ONLY the numbers provided. Do not invent data. "
    "Return ONLY valid JSON with these keys: question, key_finding, "
    "map_visual, business_recommendation, confidence_note."
)

HUMAN = (
    "Track: {track}\nQuestion: {question}\nStudy area: {study_area}\n"
    "Method: {method}\nKey metrics: {key_metrics}\n"
    "Top results: {top_results}\nCaveats: {caveats}"
)

prompt = ChatPromptTemplate.from_messages([("system", SYSTEM), ("human", HUMAN)])


def interpret(result: dict, model: str | None = None) -> dict:
    llm = ChatAnthropic(
        model=model or os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5"),
        max_tokens=1000,
        temperature=0,
    )
    resp = (prompt | llm).invoke(
        {
            "track": result.get("track"),
            "question": result.get("question"),
            "study_area": result.get("study_area"),
            "method": result.get("method"),
            "key_metrics": json.dumps(result.get("key_metrics", {})),
            "top_results": json.dumps(result.get("top_results", [])),
            "caveats": json.dumps(result.get("caveats", [])),
        }
    )
    text = resp.content if isinstance(resp.content, str) else resp.content[0]["text"]
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)


if __name__ == "__main__":
    demo = {
        "track": "SI-2",
        "question": "Which markets are we underserving?",
        "study_area": "South Los Angeles",
        "method": "Underservice index (demo)",
        "key_metrics": {"tracts_analyzed": 120, "avg_grocery_distance_mi": 1.4},
        "top_results": [{"tract": "DEMO-1", "score": 0.91}],
        "caveats": ["Demo data only"],
    }
    print(json.dumps(interpret(demo), indent=2))
