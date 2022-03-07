from __main__ import app

@app.route('/trial', methods=['GET'])
def test1():
    return 'it works!'