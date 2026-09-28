from flask import Flask, request, render_template_string

app = Flask(__name__)

PASSWORD = "527"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Simple Login</h2>

    <form method="POST">
        <input type="text" name="password"
               placeholder="Enter 3-digit password"
               maxlength="3">
        <button type="submit">Login</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        password = request.form.get("password")

        if password == PASSWORD:
            message = "LOGIN SUCCESS"
        else:
            message = "Invalid password"

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
 