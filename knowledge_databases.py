from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
	article_object = Knowledge(
	    topic=topic,
	    title=title,
	    rating=rating)
	session.add(article_object)
	session.commit()


#add_article("Loai","Amit",9)

def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles
print(query_all_articles())


def query_article_by_topic(their_topic):
	articles = session.query(Knowledge).filter_by(topic=their_topic).first()
	return articles
#print(query_article_by_topic("Loai"))


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()
#delete_article_by_topic("Loai")


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
#delete_all_articles()


def edit_article_rating(their_title,their_rating):
	articale_object = session.query(Knowledge).filter_by(title=their_title).first()
	articale_object.rating=their_rating
	session.commit()
#edit_article_rating("Amit",10)
print(query_all_articles())