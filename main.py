from app import api, app, jwt_required, current_identity


@app.route('/protected')

def protected():
    return '{}'.format(current_identity)


if __name__ == "__main__":
    app.run(debug=True)
