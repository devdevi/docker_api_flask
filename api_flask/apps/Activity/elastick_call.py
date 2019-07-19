# Models
from api_flask.apps.Activity.models import Site
# Api url
from api_flask.config import elk_url,headers
import requests
import simplejson as json
import datetime
# tiempo 
lte = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
gte = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
sites = []

def getDataElk():
    query = json.dumps({"aggs":{"2":{"terms":{"field":"site.keyword","order":{"_count":"desc"},"size":40},"aggs":{"3":{"terms":{"field":"incapsula_rule.keyword","order":{"_count":"desc"},"size":30}}}}},"size":0,"_source":{"excludes":[]},"stored_fields":["*"],"script_fields":{},"docvalue_fields":[{"field":"timestamp","format":"date_time"}],"query":{"bool":{"must":[{"range":{"timestamp":{"format":"strict_date_optional_time","gte":gte,"lte":lte}}}],"filter":[{"match_all":{}}],"should":[],"must_not":[]}}})
    try:
        r = requests.post(elk_url, data=query, headers=headers)
        results = json.loads(r.text)
        return results['aggregations']['2']['buckets']
    except requests.exceptions.ConnectionError as e:
        print(e)

def getData(elm):
    name = elm['key']
    alias = getAlias(elm['key'])
    count = elm['doc_count']
    buckets = elm['3']['buckets']
    color = ''
    buckets_count = 0
    buckets_keys = list()
    for bucket in buckets:
        threat = bucket["key"].split(",")
        threat = deleteDuplicates(threat)
        buckets_count += len(threat)*bucket['doc_count']
        buckets_keys.append(threat)
    buckets_keys = [x for x in buckets_keys if x]
    if buckets_count == 0 and count != 0:
        color = 'has-background-success'
    elif buckets_count == 0 and count == 0:
        color = 'has-background-grey-light'
    elif buckets_count > 1000:
        color = 'has-background-danger'
    else:
        color = 'has-background-warning'

    site = Site(name,alias,count,buckets,color,buckets_count,buckets_keys)
    sites.append(site.__dict__)
    return site.__dict__
 

def activitySitesData():
    data = getDataElk()
    for elm in data:
        getData(elm)
    return sites

def deleteDuplicates(x):
    x = list(filter(None,x))
    return list(dict.fromkeys(x))

def getAlias(text):
    text = text.replace('.bancochile.cl','').replace('www.','').replace('.cl','')
    return text