from thefuzz import fuzz
from thefuzz import process

df = SAS.sd2df("CDE.FUZZY")

df["Employee_Name_FAMILYNAME_MC85_PY"] = df["Employee_Name_FAMILYNAME_MC85"].apply(
  lambda x: process.extractOne(x, df["Employee_Name_FAMILYNAME_MC85"], scorer=fuzz.token_set_ratio)[0]
)

SAS.df2sd(df, "CDE.FUZZYOUT")