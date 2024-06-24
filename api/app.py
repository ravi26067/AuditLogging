from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from redis import Redis
from .config import ELASTICSEARCH_HOST, REDIS_HOST

app = Flask(__name__)
es = Elasticsearch([ELASTICSEARCH_HOST])
redis_client = Redis(host=REDIS_HOST, port=6379, db=0)

@app.route('/events', methods=['GET'])
def get_events():
    actor = request.args.get('actor')
    action = request.args.get('action')
    resource = request.args.get('resource')
    tenant_id = request.args.get('tenant_id')
    time_from = request.args.get('time_from')
    time_to = request.args.get('time_to')

    # Generate a cache key based on query parameters
    cache_key = f"events:{tenant_id}:{actor}:{action}:{resource}:{time_from}:{time_to}"
    cached_result = redis_client.get(cache_key)

    if cached_result:
        return jsonify(json.loads(cached_result))

    query = {"bool": {"must": []}}
    if tenant_id:
        query["bool"]["must"].append({"term": {"tenant_id": tenant_id}})
    if actor:
        query["bool"]["must"].append({"term": {"actor": actor}})
    if action:
        query["bool"]["must"].append({"term": {"action": action}})
    if resource:
        query["bool"]["must"].append({"term": {"resource": resource}})
    if time_from or time_to:
        time_range = {}
        if time_from:
            time_range["gte"] = time_from
        if time_to:
            time_range["lte"] = time_to
        query["bool"]["must"].append({"range": {"timestamp": time_range}})

    results = es.search(index="events", body={"query": query})

    # Cache the result
    redis_client.set(cache_key, json.dumps(results["hits"]["hits"]), ex=3600)  # Cache expires in 1 hour
    return jsonify(results["hits"]["hits"])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
