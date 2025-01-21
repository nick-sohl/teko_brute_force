from flask import Flask, request, jsonify, render_template
import hashlib
import itertools
import string

app = Flask(__name__)


# Function to calculate MD5
def calculate_md5(keyword):
    md5_hash = hashlib.md5()
    encoded_keyword = keyword.encode('utf-8')
    md5_hash.update(encoded_keyword)
    return md5_hash.hexdigest()


# Function to decrypt MD5 hash
def decrypt_md5(hash_value, len_of_keyword, uppercase):
    ascii_letters = string.ascii_letters if uppercase else string.ascii_lowercase
    combinations = itertools.product(ascii_letters, repeat=len_of_keyword)
    for combination in combinations:
        keyword = ''.join(combination)
        if calculate_md5(keyword) == hash_value:
            return keyword
    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    md5_hash = data.get("md5_hash")
    len_of_keyword = int(data.get("len_of_keyword"))
    uppercase = data.get("uppercase")

    keyword = decrypt_md5(md5_hash, len_of_keyword, uppercase)
    return jsonify({
        "keyword": keyword,
        "status": "success" if keyword else "not found"
    })


if __name__ == "__main__":
    app.run(debug=True)
