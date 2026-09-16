from agents.skill_gap_agent import SkillGapAgent


agent = SkillGapAgent()


missing_skills = [
    "Artificial Intelligence",
    "Chatbots",
    "Generative AI",
    "Data Analysis"
]


result = agent.analyze_skill_gaps(
    missing_skills
)


print("\n==============================")
print("SKILL GAP ANALYSIS")
print("==============================")


for gap in result["skill_gaps"]:

    print("\nSkill:", gap["skill"])
    print("Importance:", gap["importance"])
    print("Reason:", gap["reason"])

    print("Learning Steps:")

    for step in gap["learning_steps"]:
        print("-", step)