# Assuming you have an NPC object called npc and a message string called message
import vertexai
from vertexai.language_models import TextGenerationModel
def npc_messages(response):

    vertexai.init(project="final-year-project-400406", location="us-central1")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(
        """{npc} {message}""",
        **parameters
    )
    print(f"Response from Model: {response.text}")
