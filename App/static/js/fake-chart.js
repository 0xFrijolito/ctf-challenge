const ctx = document.getElementById('chart').getContext('2d');


const labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const data = {
  labels: labels,
  datasets: [{
    data: [20, 59, 70, 25, 56, 55, 32, 81, 56, 55, 40, 69],
    fill: false,
    borderColor: 'rgb(75, 192, 192)',
    tension: 0.1
  }]
};

const config = {
    type: 'line',
    data: data,
    options: {
        plugins: {
            legend: {
               display: false
            }
        },
        responsive: true,
        interaction: {
            intersect: false,
        },
        scales: {
            x: {
                display: true,
                title: {
                display: true
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: 'Value'
                },
                suggestedMin: 0,
                suggestedMax: 100
            }
        }
    },
};

const myChart = new Chart(ctx, config);