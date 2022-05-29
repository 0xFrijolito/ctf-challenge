const form = document.getElementById("form");
form.onsubmit = async function (e) {
    e.preventDefault();

    const payload = {
        "to": e.target[0].value,
        "amount": e.target[1].value
    }

    const res = await fetch("/api/create_transaction",{method:"POST", headers: {"content-type": "application/json"}, body: JSON.stringify(payload)});
    const data = await res.json();

    console.log(data);
    if (res.status == 200) {
        createAlert("success", data.message);
    } else {
        createAlert("danger", data.message);
    }

    updateWallet();
    updateTable();
}

async function updateWallet () {
    const res = await fetch("/api/get_user");
    const data = await res.json();

    const balance = document.getElementById("coins");
    const wallet = document.getElementById("wallet-address")

    wallet.innerHTML = data.message.user.wallet
    balance.innerHTML = "$" + data.message.user.coins
}

async function updateTable () {
    const res = await fetch("/api/get_transactions");
    const data = await res.json();

    const tableBody = document.getElementById("table-body");
    tableBody.innerHTML = "";
    for (let i=0 ; i<data.message.transactions.length ; i++) {
        const row = tableBody.insertRow();
        row.innerHTML = `<th scope="col"> ${data.message.transactions[i].id} </th><th scope="col">  ${data.message.transactions[i].sender} </th><th scope="col">  ${data.message.transactions[i].reciver} </th><th scope="col">  ${data.message.transactions[i].amount} </th>`
    }
}

updateWallet ();
updateTable();