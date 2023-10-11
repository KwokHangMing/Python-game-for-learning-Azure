# Assuming you have an NPC object called npc and a message string called message
def npc_messages(request):
    import json

    request_json = request.get_json()
    if request_json and 'text' in request_json:
        text = request_json['text']
        # Do something with the text, such as display it in a text box
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 400, {'ContentType': 'application/json'}