import azure.functions as func # Importing the core Azure Functions library
import json # Importing json to format the response properly

# Initializing the FunctionApp object which acts as the entry point for the app
app = func.FunctionApp()

# Defining the HTTP route and setting authorization to Anonymous for testing purposes
@app.route(route="CalculateArea", auth_level=func.AuthLevel.ANONYMOUS)
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    
    # Try block to handle potential errors if the request body is missing or malformed
    try:
        # Parsing the JSON body sent from the frontend
        req_body = req.get_json()
        shape = req_body.get('shape') # Determining which geometric shape to calculate
        data = req_body.get('data')   # Extracting the dimensions required for the calculation
        
        area = 0
        
        # Logic to calculate the area based on the shape identified in the request
        if shape == 'square':
            # Area = side * side
            area = data['side'] ** 2
        elif shape == 'rectangle':
            # Area = width * height
            area = data['width'] * data['height']
        elif shape == 'circle':
            # Area = pi * r^2
            area = 3.14159 * (data['radius'] ** 2)
        elif shape == 'triangle':
            # Area = 0.5 * base * height
            area = 0.5 * data['base'] * data['height']
            
        # Returning a successful HTTP response with the result in JSON format
        # This is the bridge between the backend calculation and the frontend display
        return func.HttpResponse(
            json.dumps({"area": area}), 
            mimetype="application/json"
        )
        
    except Exception as e:
        # Handling errors and returning a 400 Bad Request if something goes wrong
        return func.HttpResponse(
            f"Error processing request: {str(e)}", 
            status_code=400
        )