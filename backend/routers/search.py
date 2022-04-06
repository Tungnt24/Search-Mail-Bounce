from flask import request, render_template, Blueprint
from backend.utils import _get_collection, get_result

search_bp = Blueprint('search', __name__)


@search_bp.route('/')
@search_bp.route('/search', methods=['GET'])
def index():
    return render_template('search.html')


@search_bp.route("/search", methods=['POST'])
def get_info_by_mail_from():   
    limit = 30
    email = request.form.get("email")
    if not email:
        return {"error": "Email is required"}
    email = f"<{email.strip()}>"
    collection = _get_collection()
    filter = {
        'Status': 'bounced', 
        'From': f'{email}'
    }
    sort = list({'SentAt': -1}.items())
    records = collection.find(
        filter = filter,
        sort = sort,
        limit = limit
    )
    result = get_result(records)
    return render_template('search.html', results=result["records"])
