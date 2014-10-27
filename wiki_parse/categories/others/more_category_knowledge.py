BASIC_CATEGORIES = {
  "Biology" : ["Ecology", "Health sciences", "Neuroscience"],
  "Earth sciences" : ["Atmospheric sciences", "Geography", "Geology", "Geophysics", "Oceanography"],
  "Nature" : ["Animals", "Environment", "Humans", "Life", "Natural resources", "Plants", "Pollution"],
  "Physical sciences" : ["Astronomy", "Chemistry", "Climate", "Physics", "Space"],
  "Mathematics" : [],
  "Scientific method" : []
}

SPECIFIC_CATEGORIES = {
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
  return flatten_categories(BASIC_CATEGORIES)

def specific_categories():
  return flatten_categories(SPECIFIC_CATEGORIES)

def flatten_categories(h):
  result = []
  for main_category, sub_categories in h.iteritems():
    result.append(main_category)
    for sub_category in sub_categories:
      result.append(sub_category)
  return sorted(result)