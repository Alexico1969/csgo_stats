from quickchart import QuickChart

def fill_till(string, wanted_length):
    output = string
    string_length = len(string)
    spaces_to_add = wanted_length - string_length
    output += spaces_to_add * " "
    return output


def chart_url():

    qc = QuickChart()
    qc.width = 500
    qc.height = 300

    # Config can be set as a string or as a nested dict
    qc.config = """{
    type: 'bar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
        {
            label: 'Dataset 1',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
            borderColor: 'rgb(255, 99, 132)',
            borderWidth: 1,
            data: [-31, -70, -30, -33, -9, 14, -41],
        },
        {
            label: 'Dataset 2',
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgb(54, 162, 235)',
            borderWidth: 1,
            data: [73, 41, 29, 61, -65, 59, 38],
        },
        ],
    },
    options: {
        title: {
        display: true,
        text: 'Bar Chart',
        },
        plugins: {
        datalabels: {
            anchor: 'center',
            align: 'center',
            color: '#666',
            font: {
            weight: 'normal',
            },
        },
        },
    },
    }"""

    # You can get the chart URL...
    print(qc.get_url())

    # Get the image as a variable...
    # image = qc.get_image()

    return qc.get_url()

