import web
import graphlab
import json
from StringIO import StringIO
import yaml
import datetime

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Wiki recommender api. <br /> %s" % datetime.datetime.now().strftime("%H:%M:%S.%f")

    def POST(self):
        # i = web.input()
        data = web.data()
        jdata = yaml.safe_load(data)
        people = graphlab.SFrame('people_wiki.gl/')
        print jdata['text']
        sf_jdata = graphlab.SFrame({'URI': ['NA'], 'name': ['NA'], 'text': [jdata['text']]})
        people= people.append(sf_jdata)
        people['word_count'] = graphlab.text_analytics.count_words(people['text'])
        tfidf = graphlab.text_analytics.tf_idf(people['word_count'])
        people['tfidf'] = tfidf['docs']
        knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name')
        jdata_sframe = people[people['name'] == 'NA']        
        query_result = knn_model.query(jdata_sframe)
        print query_result
        arr_res = []
        for i in xrange(1,5):
            p = people[people['name']==query_result[i]["reference_label"]]
            arr_res.append({'name': p["name"][0], 'uri': p["URI"][0]})

        web.header('Content-Type', 'application/json')
        return json.dumps(arr_res)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
