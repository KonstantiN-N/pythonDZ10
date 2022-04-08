import json


def load_candidates():
    """Выгружаем список кандидатов из файла candidates.json"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
    return candidates


def get_candidates_all():
    """Альтернативное имя для функции load_candidates (в разборе домашки подсказали, что так будет красиво)"""
    return load_candidates()


def get_candidate_by_id(c_id):
    """Выгружаем кандидата по его ID"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] == c_id:
            return candidate


def get_candidate_by_skill(skill_name):
    """Выгружаем список кандидатов по Skills"""
    candidates = load_candidates()
    skilled_candidates = []

    for candidate in candidates:
        """Поиск только полного наименования Skill'а"""
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            skilled_candidates.append(candidate)

    return skilled_candidates


def build_site_list(candidates):
    """Формирует вывод информации о каждом пользователе"""
    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"] + "\n"
        page_content += candidate["position"] + "\n"
        page_content += candidate["skills"] + "\n"
        page_content += "\n"

    return "<pre>" + page_content + "</pre>"
