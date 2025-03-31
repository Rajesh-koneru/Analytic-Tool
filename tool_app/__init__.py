from flask import Flask,Blueprint,redirect,render_template

def Ai_tool():

    from tool_app.main import tool

    app=Flask(__name__)

    app.register_blueprint(tool)

    @app.route('/')
    def login_page():
        return render_template('login.html')

    return app