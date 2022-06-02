from mygo.gtp.frontend import GTPFrontend
from mygo.mcts.mcts import MCTSAgent
from mygo.agent import termination

agent = MCTSAgent(500, 1.5)
strategy = termination.get("opponent_passes")
termination_agent = termination.TerminationAgent(agent, strategy)

frontend = GTPFrontend(termination_agent)
frontend.run()
