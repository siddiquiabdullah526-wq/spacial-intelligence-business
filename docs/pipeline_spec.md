# Pipeline Architecture Spec: Spatial Intelligence for Business

## Stage 1: Spatial Data Layer
- Sources: U.S. Census Bureau (ACS), OpenStreetMap (OSMnx), Google Places, Esri Living Atlas
- Shared format: GeoPandas GeoDataFrame, CRS EPSG:4326 for storage, EPSG:3310 (California Albers) for distance/area work
- Raw data lives in /data (gitignored); code to fetch it lives in each track folder

## 1. Overview
The pipeline turns raw spatial data into a plain-English business recommendation in four stages. Each of the three research tracks (SI-1, SI-2, SI-3) plugs into the same pipeline, so they all produce outputs in the same format.



## Stage 2: SI Engine (one module per track)
Each module returns a dict:

```python
{
  "track": "SI-1",                # SI-1 / SI-2 / SI-3
  "question": "Where should we open our next location?",
  "study_area": "Coastal LA/OC vs Inland San Bernardino",
  "method": "SCEW",
  "key_metrics": {...},           # small dict of headline numbers
  "top_results": [...],           # ranked list of rows (max ~10)
  "geojson_path": "data/out/si1_results.geojson",
  "caveats": ["..."]
}
```

## Stage 3: LLM Interpretation
- shared_pipeline/llm.py takes the result dict, fills a prompt template, calls Claude
- Claude must return JSON matching the Stage 4 schema
- Only summarized results are sent to the LLM, not raw datasets

## Stage 4: Business Decision (aligned with Arezou template)
```json
{
  "question": "",
  "key_finding": "",
  "map_visual": "path or description",
  "business_recommendation": "",
  "confidence_note": ""
}
```

## Open questions for the meeting
1. Confirm the result-dict fields with Stella, Sushma, Glira.
2. Who pays for API usage, and what is the budget?
3. Confirm pilot areas and CRS conventions.
4. Do we log every LLM call (prompt + response) for the evaluation study?
