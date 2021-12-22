if __name__ == '__main__':

    gradesheet = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        gradesheet[name] = score
        
    unique_scores = sorted(set(gradesheet.values()))
    second_lowest_score = unique_scores[1]
    
    for student in sorted(gradesheet.keys()):
        if gradesheet[student] == second_lowest_score:
            print(student)
