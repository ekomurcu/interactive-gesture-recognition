import matplotlib.pyplot as plt


# Histogram matching
# Create hist array
def hist_array(img):
    hist = []
    for i in range(256):
        hist.append(0)
    for i in range(480):
        for j in range(640):
            hist[img[i][j]] += 1
    return hist


def plot_histogram():
    # plot histogram
    plt.figure()
    plt.grid()
    plt.title("Histogram of Image")
    plt.xlabel("Pixel value")
    plt.ylabel("Counts")
    plt.plot(range(256), hist_array(img_gray))

    plt.show()


# Gamma Correction, Contrast and Brightness
def gamma_correction():
    alpha = 2
    beta = 50
    # result=cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)
    # gamma = gamma if gamma > 0 else 0.1
    # adjusted = adjust_gamma(original, gamma=gamma)
