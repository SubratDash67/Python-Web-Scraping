from bs4 import BeautifulSoup
import requests
import time
import os

unfamiliar_skill = input("Enter the skill you are not familiar with: ")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTypeSrc=ft&searchTextText=&txtKeywords=python&txtLocation="
    ).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    if not os.path.exists("posts"):
        os.makedirs("posts")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            skills = job.find("span", class_="srp-skills").text.strip()
            more_info = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")


if __name__ == "__main__":
    while True:
        find_jobs()
        time.sleep(600)  # Run the script every 10 minutes
