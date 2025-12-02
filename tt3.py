from groq import Groq

client = Groq(api_key="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")

models = client.models.list()

print("\n🔍 Available Groq Models for your API key:\n")
for m in models.data:
    print("-", m.id)
