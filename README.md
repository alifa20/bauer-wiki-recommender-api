# bauer-wiki-recommender-api

# Running on aws

* goto /keys folder (This folder is git ignored!)

* ssh into the box

>
	
	ssh -i recomm-key.pem 54.153.199.191


* cd /home/ubuntu/bauer-wiki-recommender-api

>run server

	source activate dato-env
	nohup python p.py
	
* Browse link is:
 

>http://ec2-54-153-199-191.ap-southeast-2.compute.amazonaws.com/
