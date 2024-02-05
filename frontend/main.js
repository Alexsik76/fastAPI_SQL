query_button.addEventListener("click", handleQuery);

async function handleQuery() {
    let query = document.getElementById('sql-query').value;
    let data = await getSiteData(query=query);
    fillTable(data);
}

async function getSiteData(query) {
    let source = "http://127.0.0.1:8000/api/sql/";
    const response = await fetch(source, {
        method: 'POST',
        body: query
    });
    const { data } = await response.json();
    let site_data = await data;
    return site_data
  }

function fillTable(data){
    let table = document.getElementById("result_table");
    table.innerHTML = '';
    for (item of data) {
        let new_row = table.insertRow();
            for(value of Object.values(item)) {
                let new_cell = new_row.insertCell();
                new_cell.innerText = value;
            }
    }
}
