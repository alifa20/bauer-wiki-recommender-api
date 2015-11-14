import web
import graphlab
import json

urls = (
    '/', 'index'
)

class index:
    def GET(self):
    	# sf = graphlab.SFrame('people-example.csv')
    	people = graphlab.SFrame('people_wiki.gl/')
    	people['word_count'] = graphlab.text_analytics.count_words(people['text'])
    	tfidf = graphlab.text_analytics.tf_idf(people['word_count'])
    	people['tfidf'] = tfidf['docs']
    	knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name')
    	obama = people[people['name'] == 'Barack Obama']    	
    	query_result = knn_model.query(obama)
    	print 'query_result[0] \n',query_result[0]
        return query_result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()