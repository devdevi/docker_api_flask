# Models
from api_flask.apps.AttackCode.models import Attack
# Api url
from api_flask.config import elk_url,headers
import requests
import simplejson as json
import datetime
# tiempo 
lte = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
gte = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
def getDataElk():
    query = json.dumps(
        {
            "aggs": {
                "2": {
                    "terms": {
                        "field": "incapsula_attack.keyword",
                        "order": {"_count": "desc"},
                        "size": 100,
                    }
                }
            },
            "size": 0,
            "_source": {"excludes": []},
            "stored_fields": ["*"],
            "script_fields": {},
            "docvalue_fields": [{"field": "timestamp", "format": "date_time"}],
            "query": {
                "bool": {
                    "must": [
                        {
                            "range": {
                                "timestamp": {
                                    "format": "strict_date_optional_time",
                                    "gte": gte,
                                    "lte": lte,
                                }
                            }
                        }
                    ],
                    "filter": [{"match_all": {}}, {"match_all": {}}],
                    "should": [],
                    "must_not": [
                        {
                            "bool": {
                                "should": [
                                    {
                                        "match_phrase": {
                                            "incapsula_attack.keyword": "n/a"
                                        }
                                    }
                                ],
                                "minimum_should_match": 1,
                            }
                        }
                    ],
                }
            },
        }
    )
    try:
        r = requests.post(elk_url, data=query, headers=headers)
        results = json.loads(r.text)
        return results["aggregations"]["2"]["buckets"]
    except requests.exceptions.ConnectionError as e:
        print(e)



def getData():
    attacks=[]
    data = getDataElk()
    for c in data:
        value = c["doc_count"]
        key = c["key"]
        attack = Attack(key,value)
        attacks.append(attack.__dict__)
    return attacks

            # results = {
        #     "took": 2643,
        #     "timed_out": False,
        #     "_shards": {"total": 8, "successful": 8, "skipped": 0, "failed": 0},
        #     "hits": {"total": 7428798, "max_score": None, "hits": []},
        #     "aggregations": {
        #         "2": {
        #             "doc_count_error_upper_bound": 0,
        #             "sum_other_doc_count": 0,
        #             "buckets": [
        #                 {"key": "200", "doc_count": 64},
        #                 {"key": "30", "doc_count": 10},
        #                 {"key": "901868", "doc_count": 7},
        #                 {"key": "12", "doc_count": 4},
        #                 {"key": "3", "doc_count": 3},
        #                 {"key": "401,3", "doc_count": 2},
        #                 {
        #                     "key": "557700025,555501862,557710025,12999,12999,12999,1111,502,366007,366008,900121",
        #                     "doc_count": 2,
        #                 },
        #                 {"key": "200,40840", "doc_count": 1},
        #                 {"key": "401", "doc_count": 1},
        #                 {"key": "501,501", "doc_count": 1},
        #                 {
        #                     "key": "501336,501336,501252,501407,501514,501740,501438",
        #                     "doc_count": 1,
        #                 },
        #                 {"key": "903045", "doc_count": 1},
        #             ],
        #         }
        #     },
        #     "status": 200,
        # }