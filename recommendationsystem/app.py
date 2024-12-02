from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假資料庫
posts = [
    {"id": 1, "title": "第一篇建言", "author": "Alice", "content": "這是第一篇建言的內容"},
    {"id": 2, "title": "第二篇建言", "author": "Bob", "content": "這是第二篇建言的內容"}
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template("post.html", post=post)
    return "建言未找到", 404

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        new_post = {
            "id": len(posts) + 1,
            "title": request.form["title"],
            "author": request.form["author"],
            "content": request.form["content"]
        }
        posts.append(new_post)
        return redirect(url_for("index"))
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)
