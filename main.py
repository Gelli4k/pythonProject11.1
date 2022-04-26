from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route("/")
def list_candidates():
     """Главная страница"""
     candidates = utils.load_candidates("candidates.json")
     return render_template("list.html", candidates=candidates)



@app.route("/candidate/<int:candidate_id>")

def page_candidate(candidate_id):
     """Страница одного кандидата"""
     candidate = utils.get_candidates(candidate_id)
     return render_template("card.html", candidate=candidate)


@app.route("/search/<string:candidate_name>")

def candidates_by_name(candidate_name):
     """Поиск кандидата по имени или буквам имени"""
     candidates = utils.get_candidates_by_name(candidate_name)
     return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route("/skill/<string:skill_name>")

def get_candidates_by_skill(skill_name):
     """Поиск кандидатов по навыку"""
     candidates = utils.get_candidates_by_skill(skill_name)
     return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))

app.run()