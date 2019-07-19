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
        "field": "response_code.keyword",
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
              "lte": lte,
            }
          }
        }
      ],
      "filter": [
        {
          "match_all": {}
        }
      ],
      "should": [],
      "must_not": [
             {
          "match_phrase": {
            "response_code.keyword": {
              "query": "n/a"
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
        return results['aggregations']['2']['buckets']
    except requests.exceptions.ConnectionError as e:
        print(e)

def getData(elm):
    key = elm['key']
    count = elm['doc_count']
    buckets=list()
    for bucket in elm['3']['buckets']:
        buckets.append(bucket)
    name=site_name
    count=site_count
    color = ''
    buckets
    buckets_count = 0
    buckets_keys = list()
    if len(buckets) == 0 and count != 0:
        color = 'has-background-success'
    elif len(buckets) == 0 and count == 0:
        color = 'has-background-grey-light'
    else:
        for bucket in buckets:
            buckets_keys.append(bucket["key"])
            buckets_count += bucket["doc_count"]
            # if bucket.key not in buckets_keys:
            #     buckets_keys.append(bucket.key)
            #     buckets_count += bucket.doc_count
            # else:
            #      buckets_count += bucket.doc_count
        if buckets_count > 1000:
            color = 'has-background-danger'
        else:
            color = 'has-background-warning'

    site = Site(name,count,buckets,color,buckets_count,buckets_keys)
    sites.append(site.__dict__)
    return site.__dict__
 

def serverResponse():
    data = getDataElk()
    codes = {
        "200": 0,
        "300": 0,
        "400": 0,
        "500": 0
    }
    last_codes ={
        "200": 96544,
        "300": 20615,
        "400": 2490,
        "500": 0
    }
    codes_dict = [
        { "key": "200", "count": 0 , "last_count": 0, "icon":""},
        { "key": "300", "count": 0 , "last_count": 0, "icon":""},
        { "key": "400", "count": 0 , "last_count": 0, "icon":""},
        { "key": "500", "count": 0 , "last_count": 0, "icon":""},
    ]
    for elm in data:
        key = elm['key'][:1]
        key = f"{key}00"
        codes[key] += elm['doc_count']
    # last_codes = codes
    for code in codes_dict:
        code["count"] = codes[code["key"]]
        code["last_count"] = last_codes[code["key"]]
        if code["count"] >= code["last_count"]:
            code["icon"] = "_up"
        else:
            code["icon"] = "_down"
    last_codes = codes

    return codes_dict

# false = False
# null = None
# response = {
#   "took": 1802,
#   "timed_out": false,
#   "_shards": {
#     "total": 8,
#     "successful": 8,
#     "skipped": 0,
#     "failed": 0
#   },
#   "hits": {
#     "total": 11941584,
#     "max_score": null,
#     "hits": []
#   },
#   "aggregations": {
#     "2": {
#       "doc_count_error_upper_bound": 0,
#       "sum_other_doc_count": 0,
#       "buckets": [
#         {
#           "key": "200",
#           "doc_count": 9631736
#         },
#         {
#           "key": "304",
#           "doc_count": 1315450
#         },
#         {
#           "key": "302",
#           "doc_count": 500170
#         },
#         {
#           "key": "404",
#           "doc_count": 213705
#         },
#         {
#           "key": "303",
#           "doc_count": 125453
#         },
#         {
#           "key": "301",
#           "doc_count": 28975
#         },
#         {
#           "key": "401",
#           "doc_count": 15333
#         },
#         {
#           "key": "400",
#           "doc_count": 13008
#         },
#         {
#           "key": "307",
#           "doc_count": 5370
#         },
#         {
#           "key": "500",
#           "doc_count": 2942
#         },
#         {
#           "key": "300",
#           "doc_count": 2424
#         },
#         {
#           "key": "403",
#           "doc_count": 515
#         },
#         {
#           "key": "503",
#           "doc_count": 268
#         },
#         {
#           "key": "206",
#           "doc_count": 117
#         },
#         {
#           "key": "502",
#           "doc_count": 61
#         },
#         {
#           "key": "504",
#           "doc_count": 23
#         },
#         {
#           "key": "409",
#           "doc_count": 22
#         },
#         {
#           "key": "408",
#           "doc_count": 5
#         },
#         {
#           "key": "405",
#           "doc_count": 2
#         }
#       ]
#     }
#   },
#   "status": 200
# }