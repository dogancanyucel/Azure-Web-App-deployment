import azure.functions as func
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="CalculateArea", methods=["POST"])
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        shape = req_body.get('shape')
        
        if shape == 'square':
            side = float(req_body.get('side', 0))
            result = side * side
        elif shape == 'circle':
            radius = float(req_body.get('radius', 0))
            result = 3.14159 * radius * radius
        else:
            return func.HttpResponse(json.dumps({"error": "Unknown shape"}), status_code=400, mimetype="application/json")
            
        return func.HttpResponse(json.dumps({"result": result}), status_code=200, mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(json.dumps({"error": str(e)}), status_code=500, mimetype="application/json")