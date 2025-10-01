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
        
        # Se não houver filtros nem paginação, retorna todos
        if not filters and not request.args.get("page") and not request.args.get("per_page"):
            atividades_list = AtividadeService.buscar_todas()
            return jsonify({
                "itens": atividades_schema.dump(atividades_list),
                "total": len(atividades_list)
            }), 200
        
        # Paginação + filtros
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
        atividades_pag = AtividadeService.listar_atividades(page, per_page, filters)

        return jsonify({
            "itens": atividades_pag["items"],
            "total": atividades_pag["total"],
            "page": atividades_pag["page"],
            "pages": atividades_pag["pages"],
            "per_page": atividades_pag["per_page"]
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@atividades.route("/<string:funcional>", methods=["GET"])
def get_atividades_by_funcional(funcional):
    try:
        atividades_list = AtividadeService.buscar_por_funcional(funcional)
        return jsonify({"itens": atividades_schema.dump(atividades_list), "total": len(atividades_list)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

