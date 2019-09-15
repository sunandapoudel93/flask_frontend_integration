from flask import Flask,render_template


app = Flask(__name__)
post = [
    {
    'id':1,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 1',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/3'

    },
    {
    'id':2,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 2',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/3'
    },
    {
    'id':3,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 2',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/3'
    },

    {
    'id':3,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 3',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/3'
    },

 {
    'id':4,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 4',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/4'
    },

 {
    'id':5,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 5',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/5'
    },

 {
    'id':6,
    'image':"http://placeimg.com/640/480/any",
    'title':'Post Title 6',
    'texts':'lorem ipsum dolor sit',
    'link':'/posts/6'
    }
]


@app.route('/')

def index():
    return render_template("starter_templates.html" ,posts=post)