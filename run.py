from tool_app import Ai_tool

app=Ai_tool()

if __name__ == '__main__':
     # Use Render’s assigned port
    app.run(host="127.0.0.1", port=5000, debug=True)
