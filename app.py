from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route('/')
def story_select():
    return render_template("stories.html", stories = stories.values())

@app.route('/form')
def get_form():
    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("homeForm.html",story_id = story_id, title = story.title, prompts = prompts)


@app.route('/story')
def get_story():

    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template("story.html", text = text)