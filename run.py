from myapp import app

if __name__ == '__main__':
    app.run(app.config["IP_ADDRESS"], port=2019, debug=True)
