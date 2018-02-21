from flask import Flask, render_template, request

from dev_tools.forex.lib import Forex

app = Flask(__name__)

API_KEY = 'dMdjcsMFHtdqJWt9GDCC2VhvvtQ6fpWX'


@app.route("/", methods=["GET"])
def my_forex():
    forex = Forex(API_KEY)

    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')
    quantity = request.args.get('quantity')

    response = dict(
        from_currency=from_currency or "",
        to_currency=to_currency or "",
        quantity=quantity or "",
        quotes=forex.get_default_quotes(from_currency) if from_currency else None,
        symbols=forex.list_symbols(),
        convert_currencies=forex.convert_currencies(from_currency, to_currency, quantity) if all(
            [from_currency, to_currency, quantity]) else None,
        market_status=forex.get_market_status(),
        quota=forex.get_quota()
    )

    return render_template('index.html', **response)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
