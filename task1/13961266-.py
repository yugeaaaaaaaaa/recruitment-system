    #The purpose of this section is to calculate and distinguish the degree of matching between occupations and competencies.
def match_score(seeker,job):
    if not job.required_skills:
        return 0.0
    matched = seeker.skills & job.required_skills
    return matched/len(job.required_skills)
    if not len(matched) == 0:
        return len(matched) / len(job.required_skills)