from flask import Flask, render_template
from DataSource import DataSource

app = Flask(__name__)


@app.route('/')
def hello_world():
    data_source = DataSource()

    # Example query used for testing
    user_query = "bitcoin"

    # Get an array of coins that resemble the user's query
    # data_source.search_for_coin(user_query)["data"]["coins"] is
    # an array of dictionaries
    return_json = data_source.search_for_coin(user_query)["data"]["coins"]

    # if no coins were found
    if not return_json:
        # tell the user that no results were found
        return "No results found"

    # return the full data with the first uuid
    uuid = return_json[0]["uuid"]

    # price_history is an array of dictionaries as { price: XXX, timestamp: }
    price_history = data_source.get_data_for_coin(uuid)["data"]["history"]
    return render_template("hello_world.html", jsonobj=price_history)

@app.route('/calendar')
def calender_coin():
    calender_source = DataSource()
    user_query = "Ether"

    return_json = calender_source.search_for_coin(user_query)["data"]["coins"]

    # if no coins were found
    if not return_json:
        # tell the user that no results were found
        return "No results found"

    uuid = return_json[0]["uuid"]

    calender_source.timeline_to_1y()
    price_history = calender_source.get_data_for_coin(uuid)["data"]["history"]

    return render_template("calender.html", jsonobj=price_history)

if __name__ == '__main__':
    app.run()
