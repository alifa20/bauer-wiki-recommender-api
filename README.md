# bauer-wiki-recommender-api

# running on aws

* goto /keys folder (This folder is git ignored!)
* ssh into the box

ssh -i recomm-key.pem ubuntu@ec2-54-252-200-68.ap-southeast-2.compute.amazonaws.com

* cd /home/ubuntu/bauer-wiki-recommender-api

>run server

	source activate dato-env
	python p.py
	
* Browse link is:
 

>http://ec2-54-153-199-191.ap-southeast-2.compute.amazonaws.com/
