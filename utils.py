import json


def load_candidates(path):
    """загрузка всех кандидатов"""
    with open(path, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_candidates(candidate_id):
    """ вывод кандидатов по id"""
    candidates = load_candidates("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return None



def get_candidates_by_name(candidate_name):
    """ вывод кандидатов по имени"""
    candidates = load_candidates("candidates.json")
    matches = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            matches.append(candidate)
    return matches


def get_candidates_by_skill(skill_name):
    """ вывод кандидатов по определенному навыку"""
    candidates = load_candidates("candidates.json")
    matches = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            matches.append(candidate)
    return matches



