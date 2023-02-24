import json


def _load_data() -> ():
  with open("input.json", "r") as f:
    data = json.loads(f.read())
    return data.get("team"), data.get("applicants")


def _compute_average(data: {}, key: str) -> float:
  """Compute the average value of an attribute"""
  _sum = 0
  count = 0
  for record in data:
    _sum += record.get("attributes").get(key)
    count += 1
  return _sum / (count * 1.0)


def _compute_delta(team_average: float, team_size: int, applicant: {},
    key) -> float:
  """Compute the change in the team average if the applicant's attribute is added"""
  new_average = (team_average * team_size + applicant.get("attributes").get(
    key)) / (team_size + 1)
  return new_average - team_average


def _do_score(applicant_deltas: {}, max_score) -> {}:
  """Score an applicant based on their effects on team averages"""
  score = 0
  for attribute, delta in applicant_deltas.get("deltas").items():
    if delta > 0:
      score += max_score

  # Scores cannot be greater than 1.0 so normalize them
  if score > 1:
    score = 1.0
  return {
    "name": applicant_deltas.get("name"),
    "score": score
  }


def compute_compatability_score() -> None:
  """Compute applicant compatability score relative to the
  team's average score.

  Score the applicants as follows:
  - If an applicant improves the team's average for a certain category,
  grant them 0.25. 0.25 comes from the fact that there are four categories.
  In order to keep the applicant well-rounded, do not grant additional points
  for categories they excel at.

  - If the applicant does not improve the average for a category, grant them 0 for
  that category.
  """

  team, applicants = _load_data()
  team_averages = {
    "intelligence": _compute_average(team, "intelligence"),
    "strength": _compute_average(team, "strength"),
    "endurance": _compute_average(team, "endurance"),
    "spicyFoodTolerance": _compute_average(team, "spicyFoodTolerance"),
  }
  num_attributes = len(team_averages)
  print("Team averages: ", json.dumps(team_averages, indent=2))

  applicant_deltas = []
  for applicant in applicants:
    applicant_deltas.append({
      "name": applicant.get("name"),
      "deltas": {
        "intelligence": _compute_delta(team_averages.get("intelligence"),
                                       len(team), applicant, "intelligence"),
        "strength": _compute_delta(team_averages.get("strength"), len(team),
                                   applicant, "strength"),
        "endurance": _compute_delta(team_averages.get("endurance"), len(team),
                                    applicant, "endurance"),
        "spicyFoodTolerance": _compute_delta(
          team_averages.get("spicyFoodTolerance"), len(team), applicant,
          "spicyFoodTolerance"),
      }})

  print("Applicant deltas: ", json.dumps(applicant_deltas, indent=2))
  max_score = 1.0/num_attributes
  scores = [_do_score(deltas, max_score) for deltas in applicant_deltas]
  output = {
    "scoredApplicants": scores
  }
  print(json.dumps(output, indent=2))
  with open("output.json", "w") as f:
    f.write(json.dumps(output, indent=2))


if __name__ == "__main__":
  compute_compatability_score()
