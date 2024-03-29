# Assuming you have an NPC object called npc and a message string called message
import vertexai
from vertexai.language_models import TextGenerationModel
from flask import jsonify

def npc_messages(request):
    request_json = request.get_json()
    if request_json and 'text' in request_json:
        text = request_json['text']
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
            text,
            **parameters
        )
        generated_text = response.text
        return jsonify({'success': generated_text}), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'error': 'Invalid request'}), 400, {'ContentType': 'application/json'}