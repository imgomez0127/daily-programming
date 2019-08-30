def dfs(course,courses_available,courses_taken):
        for prereq in courses_available[course]:
            if prereq not in courses_taken:
                dfs(prereq,courses_available,courses_taken)
        courses_taken.append(course)
def courses_to_take(course_to_prereqs):
    courses_taken = []
    dfs(course_to_prereqs[0],course_to_prereqs,courses_taken)
    for course in course_to_prereqs:
        if course not in courses_taken:
            return None 
    return courses_taken 
courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
