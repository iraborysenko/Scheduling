import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def create_graph(xpos, id):
    fig, ax = plt.subplots()

    fig.canvas.set_window_title('Календарний план')
    # plt.style.use('ggplot')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator())
    plt.gcf().autofmt_xdate()

    for x in xpos:
        plt.axvline(x[1], ymin=0.0, ymax=0.75, color=x[4], linestyle=':')
        plt.axvline(x[2], ymin=0.0, ymax=0.75, color=x[4], linestyle=':')
        plt.axvline(x[3], ymin=0.0, ymax=0.77, color=x[4], linestyle='-', linewidth=2)
        plt.axvspan(x[1], x[2], ymin=0.0, ymax=0.75, alpha=1, color=x[4])
        plt.text(x[1], 0.88, x[0], rotation=45, fontsize=10)

    plt.yticks([])
    ax.xaxis_date()
    ax.set_xlabel("Час")
    plt.title(id[1])
    fig.autofmt_xdate()
    plt.show()


def save_graph(xpos, id):
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Календарний план')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator())
    plt.gcf().autofmt_xdate()

    for x in xpos:
        plt.axvline(x[1], ymin=0.0, ymax=0.75, color=x[4], linestyle=':')
        plt.axvline(x[2], ymin=0.0, ymax=0.75, color=x[4], linestyle=':')
        plt.axvline(x[3], ymin=0.0, ymax=0.77, color=x[4], linestyle='-', linewidth=2)
        plt.axvspan(x[1], x[2], ymin=0.0, ymax=0.75, alpha=1, color=x[4])
        plt.text(x[1], 0.88, x[0], rotation=45, fontsize=10)

    plt.yticks([])
    ax.xaxis_date()
    ax.set_xlabel("Час")
    plt.title(id[1])
    fig.autofmt_xdate()
    plt.savefig('Pics/' + id[1] + '.png', bbox_inches='tight')
