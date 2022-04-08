from flask import Flask

import utilit

app = Flask(__name__)


@app.route("/", )
def page_candidates():
    """Вывод данных всех кандидатов в формате: Имя, должность, навыки"""
    candidates = utilit.get_candidates_all()
    return utilit.build_site_list(candidates)


@app.route("/candidate/<int:c_id>")
def page_candidate_id(c_id):
    """Вывод кандидата по ID"""
    candidate = utilit.get_candidate_by_id(c_id)

    page_content = f"img src = {candidate['picture']} \n"
    page_content += f"<pre>"
    page_content += f"{candidate['name']} \n"
    page_content += f"{candidate['position']} \n"
    page_content += f"{candidate['skills']} \n"
    page_content += f"</pre>"

    return page_content


@app.route("/skill/<skill_name>")
def page_candidate_skill(skill_name):
    """Вывод кандидатов по навыкам"""
    candidates = utilit.get_candidate_by_skill(skill_name)
    return utilit.build_site_list(candidates)


app.run()
