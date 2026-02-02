import random


# Simple Reflex Agent
class LevelCrossingAgent:

    def rule_action(self, inbound, outbound, obstacle, manual):

        train = inbound or outbound

        # Priority 1 – Manual emergency
        if manual:
            return "RAISE", "ON", "RED"

        # Priority 2 – Obstacle detected
        elif obstacle:
            return "RAISE", "ON", "RED"

        # Priority 3 – Train detected
        elif train:
            return "LOWER", "ON", "GREEN"

        # Priority 4 – Normal
        else:
            return "RAISE", "OFF", "GREEN"


#Simulation
def simulate(steps):

    agent = LevelCrossingAgent()

    print("Step | In | Out | Obs | Man || Gate | Siren | Signal")
    

    for step in range(steps):

        inbound = random.randint(0,1)
        outbound = random.randint(0,1)
        obstacle = random.randint(0,1)
        manual = random.randint(0,1)

        gate, siren, signal = agent.rule_action(
            inbound, outbound, obstacle, manual
        )

        print(step, "   ",
              inbound, "   ",
              outbound, "   ",
              obstacle, "   ",
              manual, "   ||",
              gate, " ",
              siren, " ",
              signal)


simulate(5)
