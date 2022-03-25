from datasketch import MinHash
from flask import Flask
import werkzeug.serving # this should be removed on prod

app = Flask(__name__)

def test_datasketch():
    data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
            'estimating', 'the', 'similarity', 'between', 'datasets']
    data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
            'estimating', 'the', 'similarity', 'between', 'documents']

    m1, m2 = MinHash(), MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

    s1 = set(data1)
    s2 = set(data2)
    actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
    print("Actual Jaccard for data1 and data2 is", actual_jaccard)
    return actual_jaccard

@app.route("/test",methods = ['POST'])
def test():
    actual_jaccard = test_datasketch()
    return "Actual Jaccard for data1 and data2 is: " + str(actual_jaccard) + '\n'

@app.route("/")
def hello():
    return "Hello World!\n"

@werkzeug.serving.run_with_reloader # this should be removed on prod
def run_server():
    app.debug = True # this should be removed on prod
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_server()




