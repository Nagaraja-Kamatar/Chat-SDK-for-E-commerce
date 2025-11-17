from flask import Flask, request, jsonify
from tools import get_order_status, initiate_return, faq_lookup

app = Flask(__name__)

@app.route('/order_status', methods=['GET'])
def order_status():
    order_id = request.args.get('order_id')
    if not order_id:
        return jsonify({"success": False, "error": "order_id is required"}), 400
    result = get_order_status(order_id)
    return jsonify(result)

@app.route('/initiate_return', methods=['POST'])
def return_order():
    data = request.json
    order_id = data.get('order_id')
    reason = data.get('reason')
    if not order_id or not reason:
        return jsonify({"success": False, "error": "order_id and reason are required"}), 400
    result = initiate_return(order_id, reason)
    return jsonify(result)

@app.route('/faq', methods=['GET'])
def faq():
    query = request.args.get('query')
    if not query:
        return jsonify({"success": False, "error": "query is required"}), 400
    result = faq_lookup(query)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)