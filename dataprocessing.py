import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.ticker as mtick

powermetrics = open(os.path.dirname(__file__) +
                    os.path.sep + "data/powermetrics.txt", 'r').readlines()
powermetrics_temp = list(
    map(lambda x: x.split(" ")[3], filter(lambda line: "CPU die" in line, powermetrics)))
powermetrics_fan = list(
    map(lambda x: x.split(" ")[1], filter(lambda line: "Fan" in line, powermetrics)))

with open(os.path.dirname(__file__) + os.path.sep + "data" + os.path.sep + "logs.json", 'r') as f:
    samples = json.load(f)[1:]

for sample, temp, fan in zip(samples, powermetrics_temp[:-1], powermetrics_fan[:-1]):
    sample["cpu_temp"] = round(float(temp), 2)
    sample["fan_rpm"] = round(float(fan), 2)

sdf = pd.DataFrame(samples)
sdf["time"] = sdf.index
sdf["battery"] = sdf["battery"]/100


# ----- CPU usage - Battery --------------------------------
def getFig1():
    meltsdf = sdf.melt(id_vars=["time"], value_vars=["tot_usage", "battery"])
    p1 = plt.figure(figsize=(13, 5))
    sns.color_palette("colorblind")
    sns.set_style("whitegrid")

    sns.lineplot(data=meltsdf, y="value", x="time",
                 hue="variable", palette=["r", "g"], legend=False)

    plt.xlabel("Seconds")
    plt.ylabel("Percentage")
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.yticks(np.arange(0, 1.05, 0.05))
    plt.xticks(np.arange(0, 1260, 60))
    plt.xlim([0, 1200])
    plt.ylim([-0.03, 1.03])
    plt.title("Total CPU usage vs. Battery consumption")
    plt.legend(loc="upper right", title="Variable",
               labels=["CPU_USAGE", "BATTERY"])
    plt.tight_layout()
    plt.savefig('bat_vs_cpu.pdf', bbox_inches="tight", dpi=1000.0)


# # ---- CPU per core usage - Battery --------------------------------
def getFig2():
    corevars = list(map(lambda x: "core_" + str(x) +
                    "_percentage", range(12))) + ["battery"]
    labels = list(map(lambda x: "CORE_" + str(x), range(12))) + ["BATTERY"]
    meltsdfCore = sdf.melt(id_vars=["time"], value_vars=corevars)
    p2 = plt.figure(figsize=(20, 5))
    paletteMine = ['r', 'y', 'b', 'chocolate', 'm', 'c',
                   'navy', 'pink', 'sienna', 'grey', 'darkred', 'tan', 'g']
    sns.lineplot(data=meltsdfCore, x="time", y="value",
                 hue="variable", palette=paletteMine, legend=False)

    plt.xlabel("Seconds")
    plt.ylabel("Percentage")
    plt.title("Core usage vs. Battery consumption")
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    plt.yticks(np.arange(0, 1.05, 0.05))
    plt.xticks(np.arange(0, 1260, 60))
    plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left", title="Variable",
               labels=labels)
    plt.xlim([0, 1200])
    plt.ylim([-0.03, 1.03])
    plt.tight_layout()
    plt.savefig('bat_vs_cpu_each.pdf', dpi=1000.0)


# ----- CPU usage - Heat --------------
def getFig3():
    labels = ["CPU USAGE", "HEAT"]
    fig, ax1 = plt.subplots(1, figsize=(20, 8))
    sns.lineplot(data=sdf, ax=ax1, x="time", y="tot_usage", color='b')
    ax2 = ax1.twinx()
    ax2.set_ylabel("Celsius degrees")
    sns.lineplot(data=sdf, ax=ax2, x="time", y="cpu_temp", color='r')
    ax1.set_xlabel("Seconds")
    ax1.legend(loc="upper left", labels=["CPU USAGE"])
    ax2.legend(loc="upper right", labels=["HEAT"])

    ax1.set_ylabel("Percentage")
    plt.title("CPU usage vs. Heat")
    ax1.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax1.set_yticks(np.arange(0, 1.05, 0.05))
    ax2.set_yticks(np.arange(-140, 130, 5))
    plt.xticks(np.arange(0, 1260, 60))
    plt.xlim([0, 1200])
    ax1.set_ylim([-0.03, 1.03])
    plt.tight_layout()
    plt.savefig('cpu_temp.pdf', dpi=1000.0)

# ----- Heat - Fan


def getFig4():
    labels = ["FAN", "HEAT"]
    fig, ax1 = plt.subplots(1, figsize=(20, 8))
    sns.lineplot(data=sdf, ax=ax1, x="time", y="fan_rpm", color='b')
    ax2 = ax1.twinx()
    ax2.set_ylabel("Celsius degrees")
    sns.lineplot(data=sdf, ax=ax2, x="time", y="cpu_temp", color='r')
    ax1.set_xlabel("Seconds")
    ax1.legend(loc="upper left", labels=["FAN RPM"])
    ax2.legend(loc="upper right", labels=["HEAT"])

    ax1.set_ylabel("RPM")
    plt.title("Fan rpm vs. Heat")
    ax1.set_yticks(np.arange(0, 6000, 400))
    ax2.set_yticks(np.arange(-140, 130, 5))
    plt.xticks(np.arange(0, 1260, 60))
    plt.xlim([0, 1200])
    plt.tight_layout()
    plt.savefig('fan_heat.pdf', dpi=1000.0)
