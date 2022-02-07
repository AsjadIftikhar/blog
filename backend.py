# Add methods to use GPT
from happytransformer import HappyGeneration, GENSettings

prompt = """blog ideas for pets include:
1: Why Billionaires Will Never Invest In Pets.
2: 6 Ways Pets Can Find You the Love of Your Life.
3: 12 Secrets About Pets
4: """

# prompt = """blog ideas for pets include:
# 1: Why Billionaires Will Never Invest In Pets
# 2: 6 Ways Pets Can Find You the Love of Your Life
# 3: 12 Secrets About Pets"
#
# blog ideas for cars include:
# 1: A Foolproof Guide to Cars
# 2: An Expert Interview About Cars
# 3: 13 Insane (But True) Things About Cars"

# blog ideas for laptops include:"""

gpt_neo = HappyGeneration(model_type="GPT-NEO", model_name="EleutherAI/gpt-neo-125M")
top_k_sampling_settings = GENSettings(do_sample=True, top_k=30, max_length=15, min_length=10)
output_top_k_sampling = gpt_neo.generate_text(prompt, args=top_k_sampling_settings)

print(output_top_k_sampling.text)
