from flask import Flask, render_template, request
import os

# Analyzer functions
from analyzer import analyze_code, calculate_summary    , check_similarity

# Database functions
from database import create_table, insert_scan


# Flask App
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


# 🔹 Create database table automatically
create_table()


# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Allowed file types
ALLOWED_EXTENSIONS = {"py", "txt", "java", "js", "cpp"}


# 🔹 Check file extension
def allowed_file(filename):

    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# 🔹 Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# 🔹 Main Route
@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    summary = None
    filename = None
    plagiarism = None
    error = None

    if request.method == "POST":

        file = request.files.get("file")

        # No file selected
        if not file or file.filename == "":
            error = "No file selected"

        # Invalid file type
        elif not allowed_file(file.filename):
            error = "Invalid file type"

        else:

            # Save file
            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # 🔹 Analyze code
            results = analyze_code(filepath)

            # 🔹 Generate summary
            summary = calculate_summary(results)

            # 🔹 Save into database
            insert_scan(file.filename, summary)

            filename = file.filename

            # 🔹 Plagiarism check
            plagiarism = check_similarity(filepath)

    return render_template(
        "index.html",
        results=results,
        summary=summary,
        filename=filename,
        plagiarism=plagiarism,
        error=error
    )


# 🔹 Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

















































