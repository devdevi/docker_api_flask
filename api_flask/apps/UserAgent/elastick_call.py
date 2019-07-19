# Models
from api_flask.apps.UserAgent.models import UserAgent

# Api url
from api_flask.config import elk_url, headers

# utilities
from api_flask.apps.Activity.elastick_call import deleteDuplicates
import requests
import simplejson as json
import datetime
import math

# tiempo
lte = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
gte = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
def getDataElk():
    query = json.dumps(
        {
            "aggs": {
                "2": {
                    "terms": {
                        "field": "user_agent.keyword",
                        "order": {"_count": "desc"},
                        "size": 20,
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
                    "filter": [{"match_all": {}}],
                    "should": [],
                    "must_not": [],
                }
            },
        }
    )

    try:
        r = requests.post(elk_url, data=query, headers=headers)
        results = json.loads(r.text)
        results = results["aggregations"]["2"]["buckets"]
        return results
    except requests.exceptions.ConnectionError as e:
        print(e)


def getData():
    userAgents = []
    data = getDataElk()
    agents_dict = {}
    # agents_dict['raw']= data
    for elm in data:
        agents = elm["key"].split(",")
        agents = deleteDuplicates(agents)
        count = elm["doc_count"]
        for agent in agents:
            if agent in agents_dict:
                agents_dict[agent] += count
            else:
                agents_dict[agent] = count
    total = sum(agents_dict.values())
    for uagent in agents_dict:
        count = agents_dict[uagent]
        percentage = math.floor((count * 100) / total)
        if count >= 100000:
            user_type = "warning"
        else:
            user_type = "normal"
        user_agent = UserAgent(uagent, count, user_type, percentage)
        userAgents.append(user_agent.__dict__)
    return userAgents


# response = {
#     {
#   "took": 2065,
#   "timed_out": false,
#   "_shards": {
#     "total": 8,
#     "successful": 8,
#     "skipped": 0,
#     "failed": 0
#   },
#   "hits": {
#     "total": 11021330,
#     "max_score": null,
#     "hits": []
#   },
#   "aggregations": {
#     "2": {
#       "doc_count_error_upper_bound": 23309,
#       "sum_other_doc_count": 4387821,
#       "buckets": [
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#           "doc_count": 2621798
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#           "doc_count": 1053818
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#           "doc_count": 498910
#         },
#         {
#           "key": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
#           "doc_count": 402673
#         },
#         {
#           "key": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
#           "doc_count": 300570
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#           "doc_count": 238985
#         },
#         {
#           "key": "Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1",
#           "doc_count": 211919
#         },
#         {
#           "key": "Banco Chile/2.9.7 (iPhone; iOS 12.3.1; Scale/2.00)",
#           "doc_count": 185616
#         },
#         {
#           "key": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
#           "doc_count": 156973
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
#           "doc_count": 123331
#         },
#         {
#           "key": "Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0",
#           "doc_count": 105509
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
#           "doc_count": 100331
#         },
#         {
#           "key": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#           "doc_count": 98836
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
#           "doc_count": 84694
#         },
#         {
#           "key": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
#           "doc_count": 80824
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3165.0 Safari/537.36",
#           "doc_count": 80570
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
#           "doc_count": 79199
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
#           "doc_count": 72167
#         },
#         {
#           "key": "Banco Chile/2.9.7 (iPhone; iOS 12.3.1; Scale/3.00)",
#           "doc_count": 70863
#         },
#         {
#           "key": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
#           "doc_count": 57808
#         }
#       ]
#     }
#   },
#   "status": 200
# }
# }
