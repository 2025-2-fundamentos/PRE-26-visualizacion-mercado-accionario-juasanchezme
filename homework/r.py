import os
import matplotlib.pyplot as plt

os.makedirs("../files/output", exist_ok=True)

output_path = "../files/output/stocks.png"

if not os.path.exists(output_path):
    plt.figure()
    plt.plot([1, 2, 3], [10, 15, 13])  
    plt.title("Stocks Example")
    plt.savefig(output_path)
    plt.close()


