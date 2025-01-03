import pathlib
import pandas as pd

# relative parent path to the placement of this file
PATH = pathlib.Path(__file__).parent.parent.parent.resolve().joinpath("Data").resolve()

ankle_dynamic_df = pd.read_csv(PATH.joinpath("ankle_rehab_dynamic.csv"))
ankle_vertical_df = pd.read_csv(PATH.joinpath("ankle_rehab_vertical.csv"))
bball_df = pd.read_csv(PATH.joinpath("bball_session.csv"))
cr_seated_df = pd.read_csv(PATH.joinpath("cr_seated.csv"))
cr_seated_one_leg_df = pd.read_csv(PATH.joinpath("cr_seated_one_leg.csv"))
cr_standing_one_leg_df = pd.read_csv(PATH.joinpath("cr_standing_one_leg.csv"))
gelatin_df = pd.read_csv(PATH.joinpath("gelatin_protocol.csv"))
heel_drop_bent_df = pd.read_csv(PATH.joinpath("heel_drops_bent_knee.csv"))
heel_drop_straight_df = pd.read_csv(PATH.joinpath("heel_drops_straight_leg.csv"))
isokin_90_deg_df = pd.read_csv(PATH.joinpath("isokinetic_cr_seated.csv"))
isokin_cr_standing_df = pd.read_csv(PATH.joinpath("isokinetic_cr_standing.csv"))
isokin_cr_standing_single_leg_df = pd.read_csv(PATH.joinpath("isokinetic_cr_standing_single_leg.csv"))
oly_ballhandling_df = pd.read_csv(PATH.joinpath("1080_sprint_ballhandling.csv"))
oly_sprint_df = pd.read_csv(PATH.joinpath("1080_sprint_resistance.csv"))
oly_sprint_diag_df = pd.read_csv(PATH.joinpath("1080_sprint_resistance_diagonal.csv"))
oly_sprint_pull_df = pd.read_csv(PATH.joinpath("1080_sprint_pull_N_stop.csv"))
pain_df = pd.read_csv(PATH.joinpath("pain_morning_cr.csv"))
skipping_ropes_df = pd.read_csv(PATH.joinpath("skipping_ropes.csv"))
static_cr_90_df = pd.read_csv(PATH.joinpath("static_cr_90_degrees.csv"))
static_cr_bw_df = pd.read_csv(PATH.joinpath("static_cr_bw.csv"))
static_cr_df = pd.read_csv(PATH.joinpath("static_cr.csv"))
static_cr_resistance_df = pd.read_csv(PATH.joinpath("static_cr_resistance.csv"))
static_cr_single_leg_df = pd.read_csv(PATH.joinpath("static_cr_single_leg.csv"))
trip_ex_con_df = pd.read_csv(PATH.joinpath("triple_extension_concentric.csv"))
trip_ex_ecc_df = pd.read_csv(PATH.joinpath("triple_extension_eccentric.csv"))


# transform
def transform_date(df):
    df.insert(0, "Time", pd.to_datetime(df["Recording Date"], format='%m/%d/%Y %I:%M %p').dt.time)
    df.insert(0, "Date", pd.to_datetime(df["Recording Date"], format='%m/%d/%Y %I:%M %p').dt.date)
    del df["Recording Date"]

dataframes = [
    ankle_dynamic_df, ankle_vertical_df, bball_df, cr_seated_df, cr_seated_one_leg_df, cr_standing_one_leg_df,
    gelatin_df, heel_drop_bent_df, heel_drop_straight_df, isokin_90_deg_df, isokin_cr_standing_df,
    isokin_cr_standing_single_leg_df, oly_ballhandling_df, oly_sprint_df, oly_sprint_diag_df, oly_sprint_pull_df,
    pain_df, skipping_ropes_df, static_cr_90_df, static_cr_bw_df, static_cr_df, static_cr_resistance_df,
    static_cr_single_leg_df, trip_ex_con_df, trip_ex_ecc_df
]

for dataframe in dataframes:
    transform_date(dataframe)
