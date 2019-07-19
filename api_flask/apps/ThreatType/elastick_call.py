# from api_flask.apps.Activity.models import Site
from api_flask.apps.Activity.elastick_call import deleteDuplicates

# Models
from api_flask.apps.Attack.models import Country
# Api url
from api_flask.config import elk_url,headers
import requests
import simplejson as json
import datetime
# tiempo 
lte = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
gte = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
#  ['RFI', 'Backdoor\nProtection', 'SQL\ninjection', 'CSS', 'Illegal\nResource\nAccess']
#  ['RFI', 'Backdoor Protection', 'SQL injetion', 'CSS', 'Illegal Resource Access']
threats_list = ['LINK Tag Injetion','Block Bad Bot','Automated SQL Inkection Attack','Suspicious XSS Keywords','Malicious IRA Vectors']

def getDataElk():
    query = json.dumps(
        {
  "aggs": {
    "2": {
      "terms": {
        "field": "incapsula_rule.keyword",
        "order": {
          "_count": "desc"
        },
        "size": 100
      }
    }
  },
  "size": 0,
  "_source": {
    "excludes": []
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [
    {
      "field": "timestamp",
      "format": "date_time"
    }
  ],
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "timestamp": {
              "format": "strict_date_optional_time",
              "gte": gte,
              "lte": lte
            }
          }
        }
      ],
      "filter": [
        {
          "match_all": {}
        },
        {
          "match_all": {}
        }
      ],
      "should": [],
      "must_not": [
        {
          "bool": {
            "should": [
              {
                "match_phrase": {
                  "incapsula_rule.keyword": "n/a"
                }
              },
              {
                "match_phrase": {
                  "incapsula_rule.keyword": ",,,,,,  "
                }
              },
              {
                "match_phrase": {
                  "incapsula_rule.keyword": ","
                }
              },
              {
                "match_phrase": {
                  "incapsula_rule.keyword": ",,"
                }
              },
              {
                "match_phrase": {
                  "incapsula_rule.keyword": ""
                }
              }
            ],
            "minimum_should_match": 1
          }
        },
        {
          "match_phrase": {
            "incapsula_rule.keyword": {
              "query": ",,,,,,"
            }
          }
        }
      ]
    }
  }
}
    )
    try:
        r = requests.post(elk_url, data=query, headers=headers)
        results = json.loads(r.text)
        results = results['aggregations']['2']['buckets']
        return results
    except requests.exceptions.ConnectionError as e:
        print(e)

def getData():
    dataGraph = [0,0,0,0,0]
    data = getDataElk()
    threats_dict = {}
    # threats_dict['raw']= data
    for elm in data:
      threats = elm["key"].split(",")
      threats = deleteDuplicates(threats)
      count = elm['doc_count']
      for threat in threats:
        if threat in threats_dict:
          threats_dict[threat] += count
        else:
          threats_dict[threat] = count
      # threat_keys.append(threat)
    for th in threats_dict:
      if th in threats_list:
        dataGraph[threats_list.index(th)] = threats_dict[th]
    threats_dict['data']= dataGraph
    threats_dict['max']= max(dataGraph)
    threats_dict['legend']= threats_list
    data = []
    data.append(threats_dict)

    return data
 


# response = {
#   "took": 2668,
#   "timed_out": false,
#   "_shards": {
#     "total": 8,
#     "successful": 8,
#     "skipped": 0,
#     "failed": 0
#   },
#   "hits": {
#     "total": 7428789,
#     "max_score": null,
#     "hits": []
#   },
#   "aggregations": {
#     "2": {
#       "doc_count_error_upper_bound": 0,
#       "sum_other_doc_count": 0,
#       "buckets": [
#         {
#           "key": "Block Bad Bot",
#           "doc_count": 64
#         },
#         {
#           "key": "Automated SQL Inkection Attack",
#           "doc_count": 10
#         },
#         {
#           "key": "LINK Tag Injetion",
#           "doc_count": 4
#         },
#         {
#           "key": "DOM Events XSS Attempt",
#           "doc_count": 3
#         },
#         {
#           "key": ",,,,Malicious IRA Vectors,Malicious IRA Vectors,,Script Tag Injection,,,",
#           "doc_count": 2
#         },
#         {
#           "key": "Javascript Injection Attempt,DOM Events XSS Attempt",
#           "doc_count": 2
#         },
#         {
#           "key": "Block Bad Bot,Referer Spam",
#           "doc_count": 1
#         },
#         {
#           "key": "Javascript Injection Attempt",
#           "doc_count": 1
#         },
#         {
#           "key": "Suspicious XSS Keywords,Suspicious XSS Keywords",
#           "doc_count": 1
#         }
#       ]
#     }
#   },
#   "status": 200
# }