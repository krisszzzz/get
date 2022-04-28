import matplotlib.pyplot as plt
import numpy as np

def read_data(path_to_data: str):
    with open(path_to_data, "r") as file_:
        data_str = file_.read().split()
        data = np.array(list(map(float, data_str)))

    return data

def count_time(data: np.ndarray, freq: float, total_time: float):
    charging_time = data.argmax() * freq
    discharging_time = total_time - charging_time

    return charging_time, discharging_time


def plot_data(path_to_data: str, path_to_stat: str, figsize=(18, 12), markerevery=250, markerstyle="o", color="red",
              save_graph = False, save_name = None):
    
    data = read_data(path_to_data)
    stat = read_data(path_to_stat)
    total_time = stat[3]
    print(total_time)
    freqs      = stat[0]

    Y_values = data
    X_values = np.arange(start=freqs, stop=total_time, step=freqs)
    charg_time, discharg_time = count_time (data, freqs, total_time)
    fig, ax = plt.subplots(figsize=figsize, dpi=200)
    ax.minorticks_on()
    plt.plot(X_values, Y_values, marker=markerstyle, markevery=markerevery, label="V(t)", color=color)
    plt.text(0.82 * X_values.max(), 0.8 * Y_values.max(), 
            f"Total time is: {total_time:.2f} secs\n"
            f"Charging time is: {charg_time:.2f}\n"
            f"Discharging time is: {discharg_time:.2f}\n")

    plt.xlabel("Time, seconds")
    plt.ylabel("Voltage, Volts")
    plt.title("Proccess of capacitor's charging in RC-circut")
    plt.grid(which="major", linestyle="-", linewidth=1)
    plt.grid(which="minor", linestyle="--", linewidth=0.5)
    plt.legend()

    if save_graph and save_name is not None:
        plt.savefig(save_name)

    plt.show()


path_to_data = "./7-1_data.txt"
path_to_stat = "./7-1_settings.txt"

plot_data(path_to_data, path_to_stat, save_graph=True, color="blue", save_name="./7-1_plot.svg")

