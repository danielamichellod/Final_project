import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def punctuality_analysis_panel(df):
    """
    Generates a punctuality analysis panel:
    - On-Time Performance (Completed flights only)
    - Arrival delay distribution (Completed only)
    - Departure delay comparison (Completed vs Diverted)
    - Diversion rate
    
    Diverted flights are excluded from arrival delay metrics
    but analyzed separately.
    """

    # ---- 1️⃣ Separate groups ----
    completed = df[df["FLIGHT_STATUS"] == "Completed"].copy()
    diverted = df[df["FLIGHT_STATUS"] == "Diverted"].copy()

    # ---- 2️⃣ Compute KPIs (Completed only) ----
    completed["ON_TIME"] = (completed["ARRIVAL_DELAY"] <= 15).astype(int)
    
    otp = completed["ON_TIME"].mean() * 100
    avg_arr_delay = completed["ARRIVAL_DELAY"].mean()
    median_arr_delay = completed["ARRIVAL_DELAY"].median()

    # ---- 3️⃣ Diversion KPI ----
    diversion_rate = (df["FLIGHT_STATUS"] == "Diverted").mean() * 100

    # ---- 4️⃣ Create figure layout ----
    fig = plt.figure(figsize=(16, 10))
    
    # Layout grid: 2 rows, 2 columns
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)

    # ---------------------------------------------------
    # 📊 Plot 1 — On-Time Performance
    # ---------------------------------------------------
    ax1 = fig.add_subplot(gs[0, 0])
    sns.barplot(x=["On-Time", "Delayed"],
                y=[otp, 100 - otp],
                palette="pastel",
                ax=ax1)
    ax1.set_title("On-Time Performance (Completed Flights)")
    ax1.set_ylabel("Percentage (%)")
    ax1.set_ylim(0, 100)

    # ---------------------------------------------------
    # 📈 Plot 2 — Arrival Delay Distribution
    # ---------------------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    sns.histplot(completed["ARRIVAL_DELAY"],
                 bins=100,
                 color="skyblue",
                 ax=ax2)
    ax2.set_title("Arrival Delay Distribution (Completed Only)")
    ax2.set_xlim(-100, 300)
    ax2.set_xlabel("Arrival Delay (minutes)")

    # ---------------------------------------------------
    # 🔄 Plot 3 — Departure Delay Comparison
    # ---------------------------------------------------
    ax3 = fig.add_subplot(gs[1, 0])
    sns.boxplot(x="FLIGHT_STATUS",
                y="DEPARTURE_DELAY",
                data=df[df["FLIGHT_STATUS"].isin(["Completed", "Diverted"])],
                palette="pastel",
                ax=ax3)
    ax3.set_title("Departure Delay: Completed vs Diverted")
    ax3.set_ylabel("Departure Delay (minutes)")

    # ---------------------------------------------------
    # 📌 Plot 4 — KPI Summary Text
    # ---------------------------------------------------
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis("off")

    summary_text = f"""
    📌 Punctuality KPIs (Completed Flights Only)

    • On-Time Performance: {otp:.2f}%
    • Avg Arrival Delay: {avg_arr_delay:.2f} min
    • Median Arrival Delay: {median_arr_delay:.2f} min

    🔄 Diversion Rate (All Flights): {diversion_rate:.2f}%
    """

    ax4.text(0.1, 0.6, summary_text, fontsize=12)

    plt.suptitle("Operational Punctuality Analysis", fontsize=16)
    plt.show()

    print("✅ Punctuality analysis completed.")