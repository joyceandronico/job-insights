from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    # sourcery skip: for-append-to-extend, list-comprehension
    jobs = read(path)
    jobs_list = []
    for job in jobs:
        if job["industry"] != "":
            jobs_list.append(job["industry"])
    print(job["industry"])

    return set(jobs_list)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
