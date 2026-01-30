import json
import os


training_sessions = []
DEFAULT_PATH = 'mike.json'

def create_session(training_date, training_type):
    new_session = {
        'training_date': training_date,
        'training_type': training_type,
        'exercises': []
    }
    training_sessions.append(new_session)
    return new_session

def insert_exercise(training_session, exercise_name):
    new_exercise = {
        'name': normalize_name(exercise_name),
        'sets': []
    }

    for exercise in training_session['exercises']:
        if normalize_name(exercise['name']) == normalize_name(new_exercise['name']):
            return exercise

    training_session['exercises'].append(new_exercise)
    return new_exercise

def add_set(exercise, weight, reps):
    try:
        weight = int(weight)
        reps = int(reps)
    except ValueError:
        return None
    
    if weight < 0 or reps <=0:
        return None

    new_set = {
        'weight': weight,
        'reps': reps,
    }
    exercise['sets'].append(new_set)
    return new_set

def show_training():
    for session in training_sessions:
        print(f"\n{session['training_date']} | Treino {session['training_type']}")
        for idx_exercise, exercise in enumerate(session['exercises']):
            volume = 0
            print(f"\nExercício {idx_exercise+1}: {exercise['name']}")
            for idx_sets, set_exercise in enumerate(exercise['sets']):
                print(f"\nSérie {idx_sets+1}: {set_exercise['weight']}kg x {set_exercise['reps']}")
                volume += set_exercise['weight'] * set_exercise['reps']
            print(f"\nO volume de {exercise['name']} foi de {volume}")

def find_session_by_date(training_date):
    for session in training_sessions:
        if session['training_date'] == training_date:
            return session
    return None

def find_exercise_by_session(session, exercise_name):
    if not session or 'exercises' not in session:
        return None
    
    target_exercise = normalize_name(str(exercise_name))
    
    for exercise in session['exercises']:
        if normalize_name(exercise['name']) == normalize_name(target_exercise):
            return exercise
    return None

def normalize_name(text):
    return text.upper().strip()

def validate_exercise(exercise):
    if exercise is None:
        return False
    
    if not isinstance(exercise, dict):
        return False
    
    if 'sets' not in exercise:
        return False

    return True

def validate_exercise_and_index(exercise, set_index):
    ex = validate_exercise(exercise)
    if ex is False:
        return None
    
    if set_index is None:
        return None
    
    try:
        set_index = int(set_index)
    except (TypeError, ValueError):
        return None
    
    if not(1 <= set_index <= len(exercise['sets'])):
        return None
    return int(set_index)


def update_set(exercise, set_index, weight=None, reps=None):
    idx = validate_exercise_and_index(exercise, set_index)
    if idx == None:
        return False
    idx = idx - 1
    if weight is None and reps is None:
        return False
    
    if weight is not None:
        try:
            weight = int(weight)
        except (TypeError, ValueError):
            return False
        
        if weight < 0:
            return False

        exercise['sets'][idx]['weight'] = weight
    
    if reps is not None:
        try:
            reps = int(reps)
        except (TypeError, ValueError):
            return False
        
        if reps < 1:
            return False
    
        exercise['sets'][idx]['reps'] = reps

    return True


def remove_set(exercise, set_index):
    idx = validate_exercise_and_index(exercise, set_index)
    if idx == None:
        return False
    idx = idx - 1
    exercise['sets'].pop(idx)
    return True

def exercise_volume(exercise):
    ex = validate_exercise(exercise)
    if ex is False:
        return 0
    
    volume_total = 0
    for s in exercise['sets']:
        volume_set = s['weight'] * s['reps']
        volume_total += volume_set
    
    return volume_total

def session_volume(session):
    if session is None:
        return 0
    
    if not isinstance(session, dict):
        return 0
    
    volume_session = 0
    for ex in session['exercises']:
        volume_session += exercise_volume(ex)

    
    return volume_session


def report_session(session):
    if session is None:
        return {}
    
    if not isinstance(session, dict):
        return {}
    
    exercises_report = []
    for ex in session['exercises']:
        exercise_data = {
            'name': ex['name'],
            'sets_count': len(ex['sets']),
            'volume': exercise_volume(ex),
        }
        exercises_report.append(exercise_data)

    session_data = {
        'training_date': session['training_date'],
        'training_type': session['training_type'],
        'total_volume': session_volume(session),
        'exercises': exercises_report
    }

    return session_data

def report_all_sessions(training_sessions_list):
    training_repport = [report_session(session) for session in training_sessions_list]
    return training_repport

def report_volume_by_exercise(training_sessions_list):
    report_by_exercise = {}
    for session in training_sessions_list:
        for ex in session['exercises']:
            name = normalize_name(ex['name'])
            volume = exercise_volume(ex)
            report_by_exercise[name] = report_by_exercise.get(name, 0) + volume

    return report_by_exercise

def save_sessions(training_session_list, path=DEFAULT_PATH):
    with open(path, 'w', encoding='utf8') as f:
        json.dump(training_session_list, f)
    return True


def load_sessions(training_file=DEFAULT_PATH):
    if not os.path.exists(training_file):
        return None
    with open(training_file, 'r', encoding='utf8') as mike_file:
        complete_training = json.load(mike_file)
    return complete_training

if __name__ == '__main__':
    session1 = create_session('2025-12-04', 'A')
    exercise1 = insert_exercise(session1, 'Agachamento')
    set1 = add_set(exercise1, 90, 8)
    set2 = add_set(exercise1, 90, 7)
    set3 = add_set(exercise1, 90, 5)
    exercise2 = insert_exercise(session1, 'Leg Press')
    set1 = add_set(exercise2, 80, 8)
    set2 = add_set(exercise2, 70, 7)
    set3 = add_set(exercise2, 60, 5)
    exercise3 = insert_exercise(session1, 'Stiff')
    set1 = add_set(exercise3, 50, 8)
    set2 = add_set(exercise3, 40, 7)
    set3 = add_set(exercise3, 30, 5)
    exercise4 = insert_exercise(session1, 'Abdominal')
    set1 = add_set(exercise4, 90, 8)
    set2 = add_set(exercise4, 80, 7)
    set3 = add_set(exercise4, 70, 5)
    session2 = create_session('2025-12-06', 'B')
    exercise1 = insert_exercise(session2, 'Leg Press')
    set1 = add_set(exercise1, 80, 8)
    set2 = add_set(exercise1, 90, 7)
    set3 = add_set(exercise1, 90, 6)
    exercise2 = insert_exercise(session2, 'Abdominal')
    set1 = add_set(exercise2, 90, 8)
    set2 = add_set(exercise2, 70, 7)
    set3 = add_set(exercise2, 90, 6)
    session3 = create_session('2025-12-08', 'C')
    exercise1 = insert_exercise(session3, 'Abdominal')
    set1 = add_set(exercise1, 90, 8)
    set2 = add_set(exercise1, 70, 7)
    set3 = add_set(exercise1, 90, 6)
    exercise2 = insert_exercise(session3, 'aBDOminAL')
    set1 = add_set(exercise2, 90, 8)
    set2 = add_set(exercise2, 70, 7)
    set3 = add_set(exercise2, 90, 6)
    save_sessions(training_sessions)
    # show_training()
    # print(100*'-')
    session_1 = find_session_by_date('2025-12-04')
    # print(session_1)
    volume_session_1 = session_volume(session_1)
    # print(volume_session_1)
    result = find_exercise_by_session(session3, 'Abdominal')
    result1 = find_exercise_by_session(session1, 'Agachamento')
    result2 = find_exercise_by_session(session2, 'Leg Press')
    volume1 = exercise_volume(result)
    volume2 = exercise_volume(result1)
    volume3 = exercise_volume(result2)
    volume4 = exercise_volume('abcd')
    # print(volume1)
    # print(volume2)
    # print(volume3)
    # print(volume4)
    # print(report_session(session1))
    # print(result2)
    update_set(result, 6, 200, 100)
    remove_set(result, 3)
    # show_training()
    assert update_set(result, 4, 200, 90) is True
    assert update_set('abcd', 4, 200, 90) is False
    assert update_set(result, 10, 200, 90) is False
    assert update_set(result, 4) is False
    assert update_set(result, 0) is False
    assert update_set(result, 3, 1000, -1) is False
    assert update_set(result2, 4, 200, 90) is False
    assert remove_set(result, 4) is True
    assert remove_set('abcd', 4) is False
    assert remove_set(result, 10) is False
    assert remove_set(result, '4') is True
    assert remove_set(result, 0) is False
    assert remove_set(result, 6) is False
    assert remove_set(result2, 4) is False
    assert session_volume(None) == 0
    assert session_volume("abcd") == 0
    assert session_volume({"exercises": []}) == 0
    report = report_session(session3)

    assert report["total_volume"] == session_volume(session3)
    assert len(report["exercises"]) == len(session3["exercises"])
    assert report["exercises"][0]["sets_count"] > 0
    # print(json.dumps(report_all_sessions(training_sessions), indent=2))
    # print(report_volume_by_exercise(training_sessions))
    # save_sessions(training_sessions)
    TRAINING = save_sessions(training_sessions)
    assert load_sessions('mike_tyson.json') is None
    new_training = load_sessions('mike_tyson.json')
    if isinstance(new_training, list):
        training_sessions.extend(new_training)

    session_load = load_sessions()
    training_sessions.clear()
    assert len(training_sessions) == 0
    new_training = load_sessions('mike_jhonson.json')
    if isinstance(new_training, list):
        training_sessions.extend(new_training)
    print(training_sessions)
