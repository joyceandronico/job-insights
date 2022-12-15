import contextlib
from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    return max(
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"] != "" and job["max_salary"].isdigit()
    )


def get_min_salary(path: str) -> int:
    jobs = read(path)
    return min(
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"] != "" and job["min_salary"].isdigit()
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif (
        not str(job["min_salary"]).isnumeric()
        or not str(job["max_salary"]).isnumeric()
    ):
        raise ValueError

    elif int(job["min_salary"]) >= int(job["max_salary"]):
        raise ValueError

    elif not str(salary).lstrip("-").isnumeric():
        raise ValueError

    else:
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    job_list = []
    for job in jobs:
        with contextlib.suppress(ValueError):
            if matches_salary_range(job, salary):
                job_list.append(job)
    return job_list
