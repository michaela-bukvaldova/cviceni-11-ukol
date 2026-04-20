from sorting import bubble_sort

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90 and score <= 100:
            return "A"
        elif score >= 80 and score < 90:
            return "B"
        elif score >= 70 and score < 80:
            return "C"
        elif score >= 60 and score < 70:
            return "D"
        elif score >= 50 and score < 60:
            return "E"
        else:
            return "F"

    def find(self, score):
        positions = []
        for index, value in enumerate(self.scores):
            if value == score:
                positions.append(index)
        return positions

    def get_sorted(self):
        scores = self.scores[:]
        for serazeno_od_konce in range(len(scores)):
            has_changed = False
            print(serazeno_od_konce)
            for pozice_porovnani in range(len(scores) - 1 - serazeno_od_konce):
                if scores[pozice_porovnani] > scores[pozice_porovnani + 1]:
                    has_changed = True
                    scores[pozice_porovnani], scores[pozice_porovnani + 1] = scores[pozice_porovnani + 1], scores[pozice_porovnani]
                if not has_changed:
                    break
        return scores


results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
