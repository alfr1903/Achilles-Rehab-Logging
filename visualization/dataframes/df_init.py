import pathlib
import pandas as pd

# relative parent path to the placement of this file
PATH = pathlib.Path(__file__).parent.parent.parent.resolve().joinpath("Data").resolve()

oly_ballhandling_df = pd.read_csv(PATH.joinpath("1080_sprint_ballhandling.csv"))
oly_sprint_pull_df = pd.read_csv(PATH.joinpath("1080_sprint_pull_N_stop.csv"))
oly_sprint_df = pd.read_csv(PATH.joinpath("1080_sprint_resistance.csv"))
oly_sprint_diag_df = pd.read_csv(PATH.joinpath("1080_sprint_resistance_diagonal.csv"))
ankle_dynamic_df = pd.read_csv(PATH.joinpath("ankle_rehab_dynamic.csv"))
ankle_vertical_df = pd.read_csv(PATH.joinpath("ankle_rehab_vertical.csv"))
bball_df = pd.read_csv(PATH.joinpath("bball_session.csv"))
cr_seated_df = pd.read_csv(PATH.joinpath("cr_seated.csv"))
cr_seated_one_leg_df = pd.read_csv(PATH.joinpath("cr_seated_one_leg.csv"))
cr_standing_one_leg_df = pd.read_csv(PATH.joinpath("cr_standing_one_leg.csv"))
gelatin_df = pd.read_csv(PATH.joinpath("gelatin_protocol.csv"))
pain_df = pd.read_csv(PATH.joinpath("pain_morning_cr.csv"))
skipping_ropes_df = pd.read_csv(PATH.joinpath("skipping_ropes.csv"))
isokin_90_deg_df = pd.read_csv(PATH.joinpath("isokinetic_cr_seated.csv"))
isokin_cr_standing_df = pd.read_csv(PATH.joinpath("isokinetic_cr_standing.csv"))
isokin_cr_standing_single_leg_df = pd.read_csv(PATH.joinpath("isokinetic_cr_standing_single_leg.csv"))
static_cr_90_df = pd.read_csv(PATH.joinpath("static_cr_90_degrees.csv"))
static_cr_single_leg_df = pd.read_csv(PATH.joinpath("static_cr_single_leg.csv"))
static_cr_df = pd.read_csv(PATH.joinpath("static_cr.csv"))
static_cr_bw_df = pd.read_csv(PATH.joinpath("static_cr_bw.csv"))
static_cr_resistance_df = pd.read_csv(PATH.joinpath("static_cr_resistance.csv"))
trip_ex_con_df = pd.read_csv(PATH.joinpath("triple_extension_concentric.csv"))
trip_ex_ecc_df = pd.read_csv(PATH.joinpath("triple_extension_eccentric.csv"))


# transform
def transform_date(df):
    df.insert(0, "Time", pd.to_datetime(df["Recording Date"], format='%m/%d/%Y %I:%M %p').dt.time)
    df.insert(0, "Date", pd.to_datetime(df["Recording Date"], format='%m/%d/%Y %I:%M %p').dt.date)
    del df["Recording Date"]


transform_date(oly_ballhandling_df)
transform_date(oly_sprint_pull_df)
transform_date(oly_sprint_df)
transform_date(oly_sprint_diag_df)
transform_date(ankle_dynamic_df)
transform_date(ankle_vertical_df)
transform_date(bball_df)
transform_date(cr_seated_df)
transform_date(cr_seated_one_leg_df)
transform_date(cr_standing_one_leg_df)
transform_date(gelatin_df)
transform_date(isokin_90_deg_df)
transform_date(isokin_cr_standing_df)
transform_date(isokin_cr_standing_single_leg_df)
transform_date(pain_df)
transform_date(skipping_ropes_df)
transform_date(static_cr_90_df)
transform_date(static_cr_single_leg_df)
transform_date(static_cr_df)
transform_date(static_cr_bw_df)
transform_date(static_cr_resistance_df)
transform_date(trip_ex_con_df)
transform_date(trip_ex_ecc_df)
