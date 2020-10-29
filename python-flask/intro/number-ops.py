from flask import Flask
app = Flask(__name__)

@app.route('/numi/<int:inum>')
def pNum(inum):
    return 'Positive Integer %d' % inum

@app.route('/numf/<float:fnum>')
def fNum(fnum):
    return 'Float %f' % fnum




if __name__ == '__main__':
    #app.run()
    app.run('0.0.0.0','6700',debug = True)
