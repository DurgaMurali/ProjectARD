from flask import Flask

from bbc.file_read import (
    calculate_marginable_ar,
    read_accounts_receivable,
    read_acounts_payabale,
)

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, it's a web app!"


@app.route("/calculate/ar")
def calculate_ar():
    file_name = "/Users/sahanapranesh/Projects/ProjectARD/bbc/Sample_File_1.xlsx"
    ar = read_accounts_receivable(file_name=file_name)
    Priority_Payables = read_acounts_payabale(file_name=file_name)
    return calculate_marginable_ar(Ar=ar, Priority_Payables=Priority_Payables)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
