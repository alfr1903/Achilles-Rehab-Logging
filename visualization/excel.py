from visualization.dataframes.df_init import *
import pandas as pd


def create_excel_document():
    with pd.ExcelWriter(
            path="Alexander_Fredheim_data_olympiatoppen.xlsx",
            engine="xlsxwriter"
    ) as writer:
        create_pain_worksheet(writer, pain_df)
        create_oly_worksheet(
            writer,
            isokin_cr_standing_df,
            isokin_cr_standing_single_leg_df,
            isokin_90_deg_df,
            trip_ex_con_df,
            trip_ex_ecc_df,
            oly_ballhandling_df,
            oly_sprint_df,
            oly_sprint_pull_df,
            oly_sprint_diag_df
        )
        create_sup_ex_worksheet(
            writer,
            static_cr_bw_df,
            static_cr_df,
            static_cr_single_leg_df,
            static_cr_90_df,
            static_cr_resistance_df,
            cr_seated_df,
            cr_seated_one_leg_df,
            cr_standing_one_leg_df,
            skipping_ropes_df
        )
        create_ankle_ex_worksheet(
            writer,
            ankle_vertical_df,
            ankle_dynamic_df,
        )
        create_basket_worksheet(writer, bball_df)
        create_gelatin_worksheet(writer, gelatin_df)
        create_heel_drop_worksheet(writer, heel_drop_straight_df, heel_drop_bent_df)


def create_pain_worksheet(writer, df):
    df.to_excel(writer, sheet_name="Smerte morgen", startrow=1, index=False)
    writer.sheets["Smerte morgen"].write(0, 0, "Smerte morgen akilles tåhev øvelser")

    writer.sheets["Smerte morgen"].set_column("A:D", 15)


def create_oly_worksheet(
        writer,
        df_straight,
        df_straight_one_leg,
        df_90_deg,
        df_dyn,
        df_ex,
        df_bball,
        df_sprint,
        df_sprint_pull,
        df_sprint_diag,
):
    sheet_name = "Økter olympiatoppen"

    df_straight.to_excel(writer, sheet_name=sheet_name, startrow=1, index=False)
    writer.sheets[sheet_name].write(0, 0, "Stående isokinetisk tåhev i dynamometer")

    row2_left = len(df_straight) + 4

    df_90_deg.to_excel(writer, sheet_name=sheet_name, startrow=row2_left + 1, index=False)
    writer.sheets[sheet_name].write(row2_left, 0, "Sittende isokinetisk tåhev i dynamometer")

    col2 = len(df_straight.columns) + 1

    df_straight_one_leg.to_excel(writer, sheet_name=sheet_name, startrow=1, startcol=col2, index=False)
    writer.sheets[sheet_name].write(0, col2, "Stående isokinetisk tåhev på en fot i dynamometer")

    row2_middle = len(df_straight_one_leg) + 4

    df_dyn.to_excel(writer, sheet_name=sheet_name, startrow=row2_middle + 1, startcol=col2, index=False)
    writer.sheets[sheet_name].write(row2_middle, col2, "dynamisk fraskyv en fot i dynamometer")

    row3_middle = row2_middle + len(df_dyn) + 4

    df_ex.to_excel(writer, sheet_name=sheet_name, startrow=row3_middle + 1, startcol=col2, index=False)
    writer.sheets[sheet_name].write(row3_middle, col2, "eksentrisk fraskyv en fot i dynamometer")

    col3 = col2 + len(df_straight_one_leg.columns) + 1

    df_sprint.to_excel(writer, sheet_name=sheet_name, startrow=1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(0, col3, "løpsteg med resistans fra 1080 sprinten")

    row2_right = len(df_sprint) + 4

    df_bball.to_excel(writer, sheet_name=sheet_name, startrow=row2_right + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(row2_right, col3, "ballbehandling på tå med resistans fra 1080 sprinten")

    row3_right = row2_right + len(df_bball) + 4

    df_sprint_diag.to_excel(writer, sheet_name=sheet_name, startrow=row3_right + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(row3_right, col3, "diagonal sprint og stans med resistans fra 1080 sprinten")

    row4_right = row3_right + len(df_sprint_diag) + 4

    df_sprint_pull.to_excel(writer, sheet_name=sheet_name, startrow=row4_right + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(row4_right, col3, "rett sprint og stans med drag fra 1080 sprinten")

    writer.sheets[sheet_name].set_column("A:O", 15)


def create_sup_ex_worksheet(
        writer,
        df_bw,
        df_two_legs,
        df_one_leg,
        df_90_deg,
        df_bw_resistance,
        df_cr_seated,
        df_cr_seated_one_leg,
        df_cr_standing_one_leg,
        df_skipping_ropes
):
    sheet_name = "Ressurstrening"

    df_bw.to_excel(writer, sheet_name=sheet_name, startrow=1, index=False)
    writer.sheets[sheet_name].write(0, 0, "Ressurstrening - Statisk tåhev i trapp, et ben")

    col2 = len(df_bw.columns) + 1

    df_two_legs.to_excel(writer, sheet_name=sheet_name, startrow=1, startcol=col2, index=False)
    writer.sheets[sheet_name].write(0, col2, "Ressurstrening - Statisk tåhev m/ vekt i leg press maskin, to ben")

    col2_row2 = len(df_two_legs) + 4

    df_one_leg.to_excel(writer, sheet_name=sheet_name, startrow=col2_row2 + 1, startcol=col2, index=False)
    writer.sheets[sheet_name]. \
        write(col2_row2, col2, "Ressurstrening - Statisk tåhev m/ vekt i leg press maskin, et ben")

    col2_row3 = col2_row2 + len(df_one_leg) + 4

    df_90_deg.to_excel(writer, sheet_name=sheet_name, startrow=col2_row3 + 1, startcol=col2, index=False)
    writer.sheets[sheet_name]. \
        write(col2_row3, col2, "Ressurstrening - Statisk tåhev m/ vekt i sittende tåhev maskin, to ben")

    col2_row4 = col2_row3 + len(df_90_deg) + 4

    df_bw_resistance.to_excel(writer, sheet_name=sheet_name, startrow=col2_row4 + 1, startcol=col2, index=False)
    writer.sheets[sheet_name]. \
        write(col2_row4, col2, "Ressurstrening - Statisk tåhev et ben, ekstra belastning ved skyv ovenifra")

    col3 = col2 + len(df_two_legs.columns) + 1

    df_cr_seated.to_excel(writer, sheet_name=sheet_name, startrow=1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(0, col3, "Ressurstrening - Dynamisk sittende tåhev m/ vekt i tåhev apparat")

    col3_row2 = len(df_cr_seated) + 4

    df_cr_seated_one_leg.to_excel(writer, sheet_name=sheet_name, startrow=col3_row2 + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(col3_row2, col3,
                                    "Ressurstrening - Dynamisk sittende tåhev m/ vekt i tåhev apparat, en fot")

    col3_row3 = col3_row2 + len(df_cr_seated_one_leg) + 4

    df_cr_standing_one_leg.to_excel(writer, sheet_name=sheet_name, startrow=col3_row3 + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(col3_row3, col3,
                                    "Ressurstrening - Dynamisk stående tåhev m/ vekt i smith maskin, en fot")

    col3_row4 = col3_row3 + len(df_cr_standing_one_leg) + 4

    df_skipping_ropes.to_excel(writer, sheet_name=sheet_name, startrow=col3_row4 + 1, startcol=col3, index=False)
    writer.sheets[sheet_name].write(col3_row4, col3, "Ressurstrening - Hoppetau")

    writer.sheets[sheet_name].set_column("A:P", 15)


def create_ankle_ex_worksheet(writer, df_vert, df_dyn):
    df_vert.to_excel(writer, sheet_name="Ankel rehab", startrow=1, index=False)
    writer.sheets["Ankel rehab"].write(0, 0, "Ankel rehab - Plantar- og dorsalfleksjon i ankel med fot i luften")

    col2 = len(df_vert.columns) + 1

    df_dyn.to_excel(writer, sheet_name="Ankel rehab", startrow=1, startcol=col2, index=False)
    writer.sheets["Ankel rehab"]. \
        write(0, col2, "Ankel rehab - Dynamiske øvelser (star excursion, knebøy, vektskifte osv.)")

    writer.sheets["Ankel rehab"].set_column("A:F", 15)


def create_basket_worksheet(writer, df):
    df.to_excel(writer, sheet_name="Basket økter", startrow=1, index=False)
    writer.sheets["Basket økter"].write(0, 0, "Basket økter")

    writer.sheets["Basket økter"].set_column("A:D", 15)


def create_gelatin_worksheet(writer, df):
    df.to_excel(writer, sheet_name="Gelatin protokoll", startrow=1, index=False)
    writer.sheets["Gelatin protokoll"]. \
        write(0, 0, "Gelatin protokoll - gelatinpulver blandet med 1 glass appelsinjuice")

    writer.sheets["Gelatin protokoll"].set_column("A:C", 15)

def create_heel_drop_worksheet(writer, df_hdsl, df_hdbk):
    df_hdsl.to_excel(writer, sheet_name="Heel drop protocol", startrow=1, index=False)
    writer.sheets["Heel drop protocol"].write(0, 0, "Alfredson Heel drop protocol, strak høyre fot")

    col2 = len(df_hdsl.columns) + 1

    df_hdbk.to_excel(writer, sheet_name="Heel drop protocol", startrow=1, startcol=col2, index=False)
    writer.sheets["Heel drop protocol"]. \
        write(0, col2, "Alfredson heel drop protocol, bøyd høyre kne")

    writer.sheets["Heel drop protocol"].set_column("A:I", 15)
