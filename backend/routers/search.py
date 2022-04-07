import re

from flask import request, render_template, Blueprint
from backend.utils import _get_collection, get_result
from backend.settings import Config

search_bp = Blueprint('search', __name__)


@search_bp.route('/')
@search_bp.route('/search', methods=['GET'])
def index():
    return render_template('search.html')


@search_bp.route('/search', methods=['POST'])
def get_info_by_mail_from():   
    limit = 10
    data = request.form
    email_from = f"<{data.get('email_from')}>"
    filter = {
        'From': f'{email_from}',
    }

    email_to = data.get('email_to')
    if email_to:
        email_to = f"<{data.get('email_to')}>"
        filter.update({'To': f'{email_to}'})

    regx = re.compile(r'^.*(\breputation\b|\bspam\b|\bspamhaus\b|\blisted\b|\bblock\b|\bblocked\b|\bsecurity\b|\bblacklisted\b|\bphish\b|\bphishing\b|\bvirus\b|\bblacklisted\b|\bblacklist\b).*($|[^\w])')
    spam = data.get('spam')
    if spam:
        spam_filter = {"Message": regx}
        filter.update(spam_filter)
    
    sort = list({'SentAt': -1}.items())
    collection = _get_collection()
    query = collection.find(
        filter = filter,
        sort = sort,
        limit = limit
    )
    result = get_result(query)
    return render_template('result.html', results=result["records"])
