from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.atividade_service import AtividadeService
from app.schemas.atividade_schema import AtividadeSchema
from loguru import logger

atividades = Blueprint("atividades", __name__, url_prefix="/atividades")

atividade_schema = AtividadeSchema()
atividades_schema = AtividadeSchema(many=True)

@atividades.route("/", methods=["POST"])
def create_atividade():
    try:

        data = atividade_schema.load(request.json)
        atividade = AtividadeService.criar_atividade(data)
        logger.info(f"Atividade criada: {atividade.id} funcional={atividade.funcional}")
        return jsonify({"message": "Atividade criada!", "id": atividade.id}), 201
    except ValidationError as err:

        logger.warning(f"Erro de validação: {err.messages}")
        return jsonify({"error": str(err)}), 400
    except Exception as e:

        logger.error(f"Erro ao criar atividade: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@atividades.route("/", methods=["GET"])
def get_atividades():
    try:
        filters = {}
        codigoAtividade = request.args.get("codigoAtividade")
        dataHora_inicio = request.args.get("dataHora_inicio")
        dataHora_fim = request.args.get("dataHora_fim")

        if codigoAtividade:
            filters["codigoAtividade"] = codigoAtividade
        if dataHora_inicio and dataHora_fim:
            filters["dataHora_inicio"] = dataHora_inicio
            filters["dataHora_fim"] = dataHora_fim
        
        if not filters and not request.args.get("page") and not request.args.get("per_page"):
            atividades_list = AtividadeService.buscar_todas()
            return jsonify(atividades_schema.dump(atividades_list)), 200

        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
        atividades = AtividadeService.listar_atividades(page, per_page, filters)
        

        return jsonify(atividades), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@atividades.route("/<string:funcional>", methods=["GET"])
def get_atividades_by_funcional(funcional):
    try:
        atividades_list = AtividadeService.buscar_por_funcional(funcional)
        return jsonify(atividades_schema.dump(atividades_list)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@atividades.route("/<int:id>", methods=["PUT"])
def edit_atividade_by_id(id):
    try:
        data = atividade_schema.load(request.json, partial=True) 
        atividade = AtividadeService.editar_atividade(id, data)
        if not atividade:
            return jsonify({"error": "Atividade não encontrada"}), 404

        logger.info(f"Atividade editada: {atividade.id} funcional={atividade.funcional}")
        return jsonify({"message": "Atividade editada!", "atividade": atividade_schema.dump(atividade)}), 200
    except ValidationError as err:
        logger.warning(f"Erro de validação: {err.messages}")
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        logger.error(f"Erro ao editar atividade: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500


@atividades.route("/<int:id>", methods=["DELETE"])
def delete_atividade_by_id(id):
    try:
        deleted = AtividadeService.deletar_atividade(id)
        if not deleted:
            return jsonify({"error": "Atividade não encontrada"}), 404

        logger.info(f"Atividade deletada: {id}")
        return jsonify({"message": f"Atividade {id} deletada com sucesso!"}), 200
    except Exception as e:
        logger.error(f"Erro ao deletar atividade: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500
    