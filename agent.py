import os
import json
import anthropic
from dotenv import load_dotenv
from tools import search_web, search_reddit
# import os — access environment variables (API key)
# import json — convert between Python dicts and JSON strings
# import anthropic — the official Anthropic Python library
# load_dotenv — reads our .env file
# from tools import — brings in the two functions we just wrote
# now agent.py can call search_web() and search_reddit()

load_dotenv()
# loads the .env file so ANTHROPIC_API_KEY is available

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
# creates an Anthropic client object
# this is our connection to Claude's API
# os.getenv reads the key from .env
# we store it in "client" so we can use it anywhere in this file

MODEL = "claude-haiku-4-5-20251001"
# the specific Claude model we're using
# Haiku = fastest and cheapest version
# perfect for a prototype — costs fractions of a cent per run

TOOLS = [
# TOOLS is a list that tells Claude what functions it can call
# Claude reads these definitions to understand:
# 1. what tools exist
# 2. what each tool does
# 3. what arguments each tool needs

    {
        "name": "search_web",
        # must match the function name in tools.py exactly

        "description": "Search the web for current news, articles, and information about a topic. Use this to find mainstream and emerging coverage.",
        # Claude reads this description to decide WHEN to use this tool
        # the clearer the description, the better Claude's decisions

        "input_schema": {
        # tells Claude what arguments this function accepts

            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to look up"
                    # Claude will fill this in based on what it decides to search
                }
            },
            "required": ["query"]
            # query is mandatory — Claude must always provide it
        }
    },
    {
        "name": "search_reddit",
        "description": "Search Reddit for posts and discussions about a topic. Use this to find what niche communities and early adopters are saying before it goes mainstream.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                },
                "subreddit": {
                    "type": "string",
                    "description": "Optional specific subreddit to search. Default is 'all'."
                    # optional — Claude can search all of Reddit or target a specific community
                }
            },
            "required": ["query"]
            # only query is required, subreddit is optional
        }
    }
]


def run_agent(industry: str) -> dict:
# this is the main function — the one app.py will call
# industry: str = the user's input e.g. "athletic wear" or "fintech"
# -> dict = returns a Python dictionary with the signals

    """
    Runs the EarlySignal agentic loop.
    Claude autonomously searches the web and Reddit,
    then extracts 3 emerging trend signals.
    """

    system_prompt = """You are EarlySignal, an expert trend intelligence analyst.
Your job is to identify emerging trends in a given industry BEFORE they go mainstream.

You have access to two tools:
- search_web: for finding current news and articles
- search_reddit: for finding what niche communities are discussing

Your process:
1. Search the web for recent developments in the industry
2. Search Reddit to find what early adopters and niche communities are saying
3. Search again if you need more specific information
4. Identify exactly 3 emerging signals that haven't gone mainstream yet

For each signal return:
- title: a short punchy name for the trend (max 6 words)
- description: what's happening and why it matters (2-3 sentences)
- where_its_showing_up: which communities or sources you found it in
- why_it_could_be_big: your analysis of the opportunity (1-2 sentences)
- confidence: your confidence score as a percentage (e.g. 75%)

Return ONLY a JSON object with this exact structure — no extra text:
{
  "signals": [
    {
      "title": "...",
      "description": "...",
      "where_its_showing_up": "...",
      "why_it_could_be_big": "...",
      "confidence": "..."
    }
  ]
}"""
# the system prompt sets Claude's role, behavior, and output format
# it's like the job description we give Claude before it starts working
# being very specific about the JSON structure means we can parse it reliably

    messages = [
        {
            "role": "user",
            "content": f"Find 3 emerging trend signals in the {industry} industry that haven't gone mainstream yet."
        }
    ]
    # messages = the conversation history
    # we start with one user message telling Claude what industry to analyze
    # this list will grow as Claude makes tool calls and we add results

    while True:
    # while True = loop forever until we explicitly break out
    # this is the agentic loop — Claude keeps going until it's done

        response = client.messages.create(
        # sends the current conversation to Claude and gets a response

            model=MODEL,
            max_tokens=4096,
            # max_tokens = maximum length of Claude's response
            # 4096 is generous — enough for multiple tool calls + final answer

            system=system_prompt,
            # passes our system prompt that defines Claude's role

            tools=TOOLS,
            # passes our tool definitions so Claude knows what it can call

            messages=messages
            # passes the full conversation history
        )

        if response.stop_reason == "end_turn":
        # stop_reason tells us WHY Claude stopped
        # "end_turn" = Claude is done — it has finished its response
        # this is our signal to break out of the loop

            final_text = ""
            for block in response.content:
            # response.content is a list of content blocks
            # each block is either text or a tool_use call

                if block.type == "text":
                    final_text += block.text
                    # collect all text blocks into one string

            try:
                clean_text = final_text.strip()
                if "```json" in clean_text:
                    clean_text = clean_text.split("```json")[1].split("```")[0].strip()
                elif "```" in clean_text:
                    clean_text = clean_text.split("```")[1].split("```")[0].strip()
                start = clean_text.find("{")
                end = clean_text.rfind("}") + 1
                if start != -1 and end > start:
                    clean_text = clean_text[start:end]
                return json.loads(clean_text)
            except json.JSONDecodeError:
                return {"error": "Claude returned invalid JSON", "raw": final_text}
                # if Claude didn't return valid JSON for some reason
                # return an error dict instead of crashing

        if response.stop_reason == "tool_use":
        # "tool_use" = Claude wants to call one of our tools
        # it decided it needs more information before it can answer

            messages.append({"role": "assistant", "content": response.content})
            # add Claude's response (including the tool call request) to history
            # important — Claude needs to see its own previous messages

            tool_results = []
            # list to collect results from all tool calls Claude requested

            for block in response.content:
            # loop through Claude's response blocks

                if block.type == "tool_use":
                # this block is a tool call request

                    tool_name = block.name
                    # which tool Claude wants to call: "search_web" or "search_reddit"

                    tool_input = block.input
                    # the arguments Claude wants to pass to the tool
                    # e.g. {"query": "sustainable athletic wear 2026"}

                    if tool_name == "search_web":
                        result = search_web(tool_input["query"])
                        # actually calls our search_web function from tools.py
                        # with the query Claude decided on

                    elif tool_name == "search_reddit":
                        result = search_reddit(
                            tool_input["query"],
                            tool_input.get("subreddit", "all")
                            # .get with default "all" = use specific subreddit if provided
                            # otherwise search all of Reddit
                        )
                    else:
                        result = "Unknown tool"
                        # safety fallback if Claude somehow calls a tool we didn't define

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        # block.id = unique ID that matches this result to Claude's request
                        # Claude uses this to know which result belongs to which call

                        "content": result
                        # the actual search results from tools.py
                    })

            messages.append({"role": "user", "content": tool_results})
            # add the tool results back to the conversation as a user message
            # Claude will read these results and decide what to do next
            # — search again, or produce the final answer
            # then the while loop runs again and Claude responds
