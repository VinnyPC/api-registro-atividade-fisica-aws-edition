from flask import Flask, jsonify
from marshmallow import ValidationError
import traceback

def register_error_handlers(app: Flask):
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return jsonify({
            "error": "Erro de validação",
            "messages": err.messages 
        }), 400

    @app.errorhandler(Exception)
    def handle_generic_error(err):
        return jsonify({
            "error": "Erro interno no servidor",
            "details": str(err),
        }), 500
