from phi.model.ollama import Ollama
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance Agent",
    model=Ollama(id="qwen2.5-coder:7b"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True, enable_all=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response("Show all detailed information about ALBRK.IS company including sector, industry, number of employees, market value and business summary", stream=True)

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story.")
# print(run.content)

# Print the response in the terminal
# agent.print_response("Share a 2 sentence horror story.")