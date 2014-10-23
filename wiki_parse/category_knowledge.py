from os import listdir, name
from os.path import isfile, join, realpath


BASIC_FIELDS = {
  "Biology" : ["Ecology", "Health sciences", "Neuroscience"],
  "Earth sciences" : ["Atmospheric sciences", "Geography", "Geology", "Geophysics", "Oceanography"],
  "Nature" : ["Animals", "Environment", "Humans", "Life", "Natural resources", "Plants", "Pollution"],
  "Physical sciences" : ["Astronomy", "Chemistry", "Climate", "Physics", "Space"],
  "Mathematics" : [],
  "Scientific method" : []
}

SPECIFIC_FIELDS = {
  "Health science" : ["Clinical research", "Diseases", "Epidemiology", 
    "Midwifery", "Nursing", "Nutrition", "Optometry", "Pharmacy", "Public health"],
  "Medicine" : ["Human medicine", "Alternative medicine", "Cardiology", "Endocrinology", 
    "Forensics", "Gastroenterology", "Human", "Genetics", "Geriatrics", "Gerontology", 
    "Gynecology", "Hematology", "Nephrology", "Neurology", "Obstetrics", "Oncology", 
    "Ophthalmology","Orthopedic", "surgical procedures", "Pathology", "Pediatrics", 
    "Psychiatry", "Rheumatology", "Surgery", "Urology"],
  "Mathematics" : ["Algebra", "Analysis", "Arithmetic", "Education", "Equations", 
    "Geometry", "Heuristics", "Logic", "Measurement", "Numbers", "Proofs", "Theorems", 
    "Trigonometry"],
  "Statistics" : ["Analysis of variance", "Bayesian statistics", "Categorical data",
    "Covariance and correlation", "Data analysis", "Decision theory", "Design of experiments",
    "Logic and statistics", "Multivariate statistics", "Non-parametric statistics",
    "Parametric statistics", "Regression analysis", "Sampling", "Statistical theory",
    "Stochastic processes", "Summary statistics", "Survival analysis", "Time series analysis",
    "Uncertainty of numbers"],
  "Scientific method" : ["Scientists"]
}

def basic_categories():
  return flatten_categories(BASIC_FIELDS)

def specific_categories():
  return flatten_categories(SPECIFIC_FIELDS)

def flatten_categories(h):
  result = []
  for main_category, sub_categories in h.iteritems():
    result.append(main_category)
    for sub_category in sub_categories:
      result.append(sub_category)
  return sorted(result)

def saved_titles(depth):
  p = category_path()
  result = []
  for f in listdir(p):
    if isfile(join(p, f)):
      name = f.split(".")
      if name[0][-1] == str(depth):
        result.append(name[0])
  return result

def category_path():
  if name == 'nt':
    return "C:\\Users\\Swaneet\\github\\AdaptiveAgents\\wiki_parse\\categories\\"  # TODO: fixen how in windows.
  return "%s/categories/" % realpath('') 


